from pathlib import Path
from datetime import datetime,timezone
import json,subprocess,os,sys
p=Path('/private/tmp');r=p/'CMMMech-expansion-round94-20261015';repo='CultureBotAI/CMMMech';c=json.loads((p/'cmm-round94-commit-receipt.json').read_text());out=p/'cmm-round94-pr-cleanup.json';assert not out.exists()
def run(cmd):return subprocess.check_output(cmd,cwd=r,text=True).strip()
def git(*a):return run(['git',*a])
pr=json.loads(run(['gh','pr','view',str(int(sys.argv[1])),'--repo',repo,'--json','state,mergedAt,mergeCommit,headRefOid,url']))
assert pr['state']=='MERGED' and pr['headRefOid']==c['head'];merge=pr['mergeCommit']['oid']
assert git('branch','--show-current')==c['branch'] and git('rev-parse','HEAD')==c['head'] and not git('status','--porcelain=v1','--untracked-files=all')
git('fetch','--no-tags','origin','refs/heads/main:refs/remotes/origin/main')
assert git('rev-parse','origin/main')==merge and git('rev-parse',merge+'^{tree}')==c['tree']
assert git('rev-list','--parents','-n','1',merge).split()==[merge,c['base']]
remote=git('ls-remote','origin','refs/heads/'+c['branch'])
if remote:
 assert remote.split()==[c['head'],'refs/heads/'+c['branch']]
 git('push','--force-with-lease=refs/heads/'+c['branch']+':'+c['head'],'origin',':refs/heads/'+c['branch'])
assert not git('ls-remote','origin','refs/heads/'+c['branch'])
git('switch','--detach',c['head'])
git('branch','-D',c['branch'])
x=subprocess.run(['git','show-ref','--verify','--quiet','refs/heads/'+c['branch']],cwd=r);assert x.returncode==1
assert not git('branch','--show-current') and git('rev-parse','HEAD')==c['head'] and not git('status','--porcelain=v1','--untracked-files=all')
d={'recorded_at':datetime.now(timezone.utc).isoformat(),'pr':pr,'base':c['base'],'head':c['head'],'tree':c['tree'],'merge':merge,'local_branch_absent':True,'remote_branch_absent':True,'clean_detached_worktree':str(r),'scope':'Deleted only this owned topic branch after verifying actual merged tree and sole parent. Clean detached topic checkout retained; original main and unrelated worktree files untouched.'}
out.write_text(json.dumps(d,indent=2)+'\n');print(json.dumps(d,indent=2))
