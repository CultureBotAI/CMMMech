from pathlib import Path
from datetime import datetime, timezone
import json, subprocess, hashlib
tmp=Path('/private/tmp');root=tmp/'CMMMech-expansion-round71-20261014';repo='CultureBotAI/CMMMech'
c=json.loads((tmp/'cmm-round71-commit-receipt.json').read_text());branch=c['branch'];out=tmp/'cmm-round71-pr-open.json'
assert not out.exists()
def run(args,allowed=(0,)):
    p=subprocess.run(args,cwd=root,capture_output=True,text=True)
    assert p.returncode in allowed,(args,p.returncode,p.stdout,p.stderr)
    return p
git=lambda *a:run(['git',*a]).stdout.strip()
assert branch=='curate/cmm-expansion-round71-20261014'
assert git('rev-parse','HEAD')==c['head'] and git('rev-parse','HEAD^{tree}')==c['tree']
assert not git('status','--porcelain=v1','--untracked-files=all')
assert git('ls-remote','origin','refs/heads/main').split()[0]==c['base']
assert not json.loads(run(['gh','pr','list','--repo',repo,'--state','all','--head',branch,'--json','number']).stdout)
remote=run(['git','ls-remote','--exit-code','origin','refs/heads/'+branch],allowed=(0,2))
assert remote.returncode==2 or remote.stdout.split()[0]==c['head']
git('push','--set-upstream','origin','refs/heads/'+branch+':refs/heads/'+branch)
body=tmp/'cmm-round71-pr-body.md';title=json.loads((tmp/'cmm-round71-helper-config.json').read_text())['title']
created=run(['gh','pr','create','--repo',repo,'--base','main','--head',branch,'--title',title,'--body-file',str(body)])
url=created.stdout.strip();assert url.startswith('https://github.com/'+repo+'/pull/')
pr=json.loads(run(['gh','pr','view',url,'--repo',repo,'--json','number,url,title,body,state,headRefOid,headRefName,baseRefName']).stdout)
assert pr['headRefOid']==c['head'] and pr['headRefName']==branch and pr['baseRefName']=='main' and pr['state']=='OPEN'
assert pr['title']==title and pr['body'].rstrip()==body.read_text().rstrip()
pr['recorded_at']=datetime.now(timezone.utc).isoformat();pr['body_sha256']=hashlib.sha256(body.read_bytes()).hexdigest()
out.write_text(json.dumps(pr,indent=2)+'\n');print(json.dumps({'number':pr['number'],'url':pr['url'],'head':pr['headRefOid']},indent=2))
