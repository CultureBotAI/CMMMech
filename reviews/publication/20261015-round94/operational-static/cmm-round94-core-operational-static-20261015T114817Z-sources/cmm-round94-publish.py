from pathlib import Path
from datetime import datetime,timezone
import subprocess,json,hashlib
p=Path('/private/tmp');r=p/'CMMMech-expansion-round94-20261015';c=json.loads((p/'cmm-round94-commit-receipt.json').read_text());cfg=json.loads((p/'cmm-round94-helper-config.json').read_text());out=p/'cmm-round94-publish-receipt.json';assert not out.exists();repo='CultureBotAI/CMMMech'
def run(cmd):return subprocess.check_output(cmd,cwd=r,text=True).strip()
def git(*a):return run(['git',*a])
assert git('branch','--show-current')==c['branch'] and git('rev-parse','HEAD')==c['head'] and git('rev-parse','HEAD^{tree}')==c['tree'] and not git('status','--porcelain=v1','--untracked-files=all')
for filename in ['final-gates','review-check-final']:
 d=json.loads((p/f'cmm-round94-{filename}.json').read_text());assert d['exit_code']==0 and hashlib.sha256(Path(d['log']).read_bytes()).hexdigest()==d['log_sha256']
coverage=json.loads((p/'cmm-round94-local-coverage.json').read_text());assert coverage['passed']
for x in coverage['records']:assert hashlib.sha256((r/x['path']).read_bytes()).hexdigest()==x['sha256']
assert not json.loads(run(['gh','pr','list','--repo',repo,'--head',c['branch'],'--state','all','--json','number']))
assert git('ls-remote','origin','refs/heads/main').split()==[c['base'],'refs/heads/main'] and not git('ls-remote','origin','refs/heads/'+c['branch'])
run(['git','push','--set-upstream','origin','HEAD:refs/heads/'+c['branch']])
assert git('ls-remote','origin','refs/heads/'+c['branch']).split()==[c['head'],'refs/heads/'+c['branch']]
url=run(['gh','pr','create','--repo',repo,'--base','main','--head',c['branch'],'--title',cfg['title'],'--body-file',str(p/'cmm-round94-pr-body.md')])
pr=json.loads(run(['gh','pr','view',url,'--repo',repo,'--json','number,url,state,headRefName,headRefOid,baseRefName,baseRefOid,title,body']))
assert pr['state']=='OPEN' and pr['headRefOid']==c['head'] and pr['headRefName']==c['branch'] and pr['baseRefOid']==c['base'] and pr['title']==cfg['title'] and pr['body'].strip()==(p/'cmm-round94-pr-body.md').read_text().strip()
d={'recorded_at':datetime.now(timezone.utc).isoformat(),'pr':pr,'head':c['head'],'tree':c['tree'],'base':c['base'],'body_sha256':hashlib.sha256((p/'cmm-round94-pr-body.md').read_bytes()).hexdigest()};out.write_text(json.dumps(d,indent=2)+'\n');print(json.dumps({'url':url,'number':pr['number'],'head':c['head']},indent=2))
