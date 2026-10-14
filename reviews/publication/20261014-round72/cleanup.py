from pathlib import Path
from datetime import datetime,timezone
import json,subprocess
root=Path('/private/tmp/CMMMech-expansion-round72-20261014');repo='CultureBotAI/CMMMech';tmp=Path('/private/tmp')
c=json.loads((tmp/'cmm-round72-commit-receipt.json').read_text());opened=json.loads((tmp/'cmm-round72-pr-open.json').read_text());number=opened['number'];branch=c['branch']
out=tmp/'cmm-round72-pr-cleanup.json';assert not out.exists()
assert branch=='curate/cmm-expansion-round72-20261014' and c['base']=='a2f08edab1307aba4281ce1e2a54d84bca88a889'
assert opened['headRefOid']==c['head'] and opened['headRefName']==branch and opened['baseRefName']=='main'
def run(cmd,allowed=(0,)):
 p=subprocess.run(cmd,cwd=root,capture_output=True,text=True)
 assert p.returncode in allowed,(cmd,p.returncode,p.stdout,p.stderr)
 return p
def git(*args):return run(['git',*args]).stdout.strip()
pr=json.loads(run(['gh','pr','view',str(number),'--repo',repo,'--json','number,state,mergedAt,mergeCommit,headRefOid,url']).stdout)
assert pr['state']=='MERGED' and pr['headRefOid']==c['head'] and pr['mergedAt']
merge=pr['mergeCommit']['oid'];assert len(merge)==40
assert git('rev-parse','HEAD')==c['head'] and git('branch','--show-current')==branch
assert not git('status','--porcelain=v1','--untracked-files=all')
git('fetch','origin','main')
assert git('rev-parse','origin/main')==merge and git('rev-parse',merge+'^{tree}')==c['tree']
assert git('rev-parse',merge+'^')==c['base']
issues=[]
config=json.loads((tmp/'cmm-round72-helper-config.json').read_text())['issues']
issue_pages=json.loads(run(['gh','api',f'repos/{repo}/issues?state=all&per_page=100','--paginate','--slurp']).stdout)
issue_map={x['number']:x for page in issue_pages for x in page if 'pull_request' not in x}
for n,state in [(n,'CLOSED') for n in config['corrected_review_issues']+config['closed_source_issues']]+[(n,'OPEN') for n in config['open_source_issues']]:
 raw=issue_map[n]
 d={'number':raw['number'],'state':raw['state'].upper(),'url':raw['html_url']}
 assert d['state']==state,(n,d)
 issues.append(d)
ref='refs/heads/'+branch
remote=run(['git','ls-remote','--exit-code','origin',ref],allowed=(0,2))
if remote.returncode==0:
 assert remote.stdout.split()[0]==c['head']
 git('push','--force-with-lease='+ref+':'+c['head'],'origin',':'+ref)
assert run(['git','ls-remote','--exit-code','origin',ref],allowed=(0,2)).returncode==2
git('switch','--detach',merge)
assert git('rev-parse',ref)==c['head']
git('branch','-D','--',branch)
assert run(['git','show-ref','--verify','--quiet',ref],allowed=(0,1)).returncode==1
assert not git('status','--porcelain=v1','--untracked-files=all')
(tmp/'cmm-round72-pr-merged.json').write_text(json.dumps(pr,indent=2)+'\n')
r={'recorded_at':datetime.now(timezone.utc).isoformat(),'pr':number,'merge':merge,'head':c['head'],'tree':c['tree'],'branch':branch,'local_branch_absent':True,'remote_branch_absent':True,'worktree':str(root),'clean_detached_worktree':True,'issue_states':issues}
out.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
