from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess
T=Path('/private/tmp');W=T/'CMMMech-expansion-round103-20261015';repo='CultureBotAI/CMMMech';cfg=json.loads((T/'cmm-round103-helper-config.json').read_text());c=json.loads((T/'cmm-round103-commit-receipt.json').read_text());body=T/'cmm-round103-pr-body.md';rows=[]
now=lambda:datetime.now(timezone.utc).isoformat()
def run(cmd):
 p=subprocess.run(cmd,cwd=W,capture_output=True,text=True);rows.append({'at':now(),'command':cmd,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr});assert p.returncode==0,(cmd,p.stderr);return p.stdout.strip()
def git(*args):return run(['git',*args])
assert c['exit_code']==0 and git('rev-parse','HEAD')==c['head'] and git('rev-parse','HEAD^{tree}')==c['tree'] and git('branch','--show-current')==cfg['branch'] and not git('status','--porcelain=v1','--untracked-files=all')
assert not git('ls-remote','origin','refs/heads/'+cfg['branch'])
assert git('ls-remote','origin','refs/heads/main').split()==[cfg['base'],'refs/heads/main']
git('push','--set-upstream','origin',cfg['branch'])
assert git('ls-remote','origin','refs/heads/'+cfg['branch']).split()==[c['head'],'refs/heads/'+cfg['branch']]
url=run(['gh','pr','create','--repo',repo,'--base','main','--head',cfg['branch'],'--title',cfg['title'],'--body-file',str(body)]);n=int(url.rsplit('/',1)[1]);pr=json.loads(run(['gh','api',f'repos/{repo}/pulls/{n}']))
assert pr['head']['sha']==c['head'] and pr['head']['ref']==cfg['branch'] and pr['base']['sha']==cfg['base'] and pr['base']['ref']=='main' and pr['title']==cfg['title'] and pr['body']==body.read_text() and not pr['draft']
r={'recorded_at':now(),'pr':pr,'commands':rows,'body_file':str(body),'body_sha256':hashlib.sha256(body.read_bytes()).hexdigest(),'exit_code':0}
with (T/'cmm-round103-pr-created.json').open('x') as f:json.dump(r,f,indent=2);f.write('\n')
print(json.dumps({'url':url,'number':n,'head':c['head'],'tree':c['tree']},indent=2))
