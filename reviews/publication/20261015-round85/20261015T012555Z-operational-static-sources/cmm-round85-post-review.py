from pathlib import Path
from datetime import datetime, timezone
import json, subprocess, hashlib
p=Path('/private/tmp');repo='CultureBotAI/CMMMech'
c=json.loads((p/'cmm-round85-commit-receipt.json').read_text());opened=json.loads((p/'cmm-round85-pr-open.json').read_text());n=opened['number']
out=p/'cmm-round85-pr-review-posted.json';assert not out.exists()
peers=[json.loads(x.read_text()) for x in p.glob('cmm-round85-hosted-peer-*.json') if not x.name.endswith('-responses.json')]
assert any(x.get('passed') and x.get('pr')==n and x.get('head')==c['head'] and x.get('tree')==c['tree'] for x in peers)
live=json.loads(subprocess.check_output(['gh','pr','view',str(n),'--repo',repo,'--json','state,headRefOid'],text=True))
assert live['state']=='OPEN' and live['headRefOid']==c['head']
body=(p/'cmm-round85-hosted-review.md').read_text()
payload={'commit_id':c['head'],'event':'COMMENT','body':body}
request=p/'cmm-round85-pr-review-request.json';assert not request.exists();request.write_text(json.dumps(payload,indent=2)+'\n')
review=json.loads(subprocess.check_output(['gh','api','--method','POST',f'repos/{repo}/pulls/{n}/reviews','--input',str(request)],text=True))
assert review['commit_id']==c['head'] and review['state']=='COMMENTED' and review['body']==body
out.write_text(json.dumps(review,indent=2)+'\n')
cfgp=p/'cmm-round85-helper-config.json';cfg=json.loads(cfgp.read_text());assert 'publication' not in cfg
sha=lambda x:hashlib.sha256(x.read_bytes()).hexdigest()
cfg['publication']={'title':opened['title'],'pr':n,'head':c['head'],'tree':c['tree'],'file_count':len(c['files']),'receipt_hashes':{name:sha(p/('cmm-round85-'+name+'.json')) for name in ['commit-receipt','pr-open','pr-review-posted']},'pr_body_sha256':sha(p/'cmm-round85-pr-body.md'),'review_body_sha256':sha(p/'cmm-round85-hosted-review.md')}
cfgp.write_text(json.dumps(cfg,indent=2)+'\n')
print(json.dumps({'pr':n,'review_id':review['id'],'head':review['commit_id'],'state':review['state']},indent=2))
