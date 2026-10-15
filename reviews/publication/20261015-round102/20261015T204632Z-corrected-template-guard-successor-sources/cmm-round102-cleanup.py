from pathlib import Path
import datetime,hashlib,json,subprocess,sys,re
T=Path('/private/tmp');W=T/'CMMMech-expansion-round102-20261015';REPO='CultureBotAI/CMMMech';BASE='1c2a3bb043c4bd267a3d911d0e77b029c742689e';HEAD='ROUND102_TOPIC_HEAD';TREE='ROUND102_TOPIC_TREE';BRANCH='curate/cmm-expansion-round102-20261015';MERGE=sys.argv[1];assert re.fullmatch('[0-9a-f]{40}',MERGE)
now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();o=T/'cmm-round102-cleanup-receipt.json';f=o.open('x');r={'started_at':now(),'merge_commit':MERGE,'head':HEAD,'base':BASE,'tree':TREE,'branch':BRANCH,'commands':[]};json.dump({'state':'in_progress'},f);f.flush()
def run(cmd,allowed=(0,)):
 p=subprocess.run(cmd,cwd=W,capture_output=True,text=True);r['commands'].append({'at':now(),'command':cmd,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr});assert p.returncode in allowed,(cmd,p.stderr);return p.stdout.strip()
def git(*a,**kw):return run(['git',*a],**kw)
def api(path):return json.loads(run(['gh','api',f'repos/{REPO}/'+path]))
try:
 q=json.loads((T/'cmm-round102-queue-receipt.json').read_text());assert q['exit_code']==0 and q['head']==HEAD and q['base']==BASE
 p=api('pulls/ROUND102_PR_NUMBER');assert p['merged'] and p['state']=='closed' and p['merge_commit_sha']==MERGE and p['head']['sha']==HEAD
 c=api('git/commits/'+MERGE);assert [x['sha'] for x in c['parents']]==[BASE] and c['tree']['sha']==TREE
 assert api('git/ref/heads/main')['object']['sha']==MERGE
 assert git('rev-parse','HEAD')==HEAD and git('branch','--show-current')==BRANCH and not git('status','--porcelain=v1','--untracked-files=all')
 assert git('rev-parse','refs/heads/'+BRANCH)==HEAD
 remote=git('ls-remote','origin','refs/heads/'+BRANCH);r['remote_branch_before']=remote
 if remote:
  assert remote.split()==[HEAD,'refs/heads/'+BRANCH]
  git('push','origin','--force-with-lease=refs/heads/'+BRANCH+':'+HEAD,':refs/heads/'+BRANCH)
 assert not git('ls-remote','origin','refs/heads/'+BRANCH)
 git('checkout','--detach',HEAD)
 assert git('rev-parse','refs/heads/'+BRANCH)==HEAD and not git('branch','--show-current')
 assert 'branch refs/heads/'+BRANCH not in git('worktree','list','--porcelain').splitlines()
 git('update-ref','-d','refs/heads/'+BRANCH,HEAD)
 # Retain any branch configuration; deleting it could race with a new branch creator.
 git('show-ref','--verify','--quiet','refs/heads/'+BRANCH,allowed=(1,))
 assert git('rev-parse','HEAD')==HEAD and not git('status','--porcelain=v1','--untracked-files=all')
 assert git('rev-parse','refs/tags/review-base/cmm-source-survey-20261009')=='fc4040c3abcd28f0a9cc52467e308100144ad1fd'
 assert git('rev-parse','refs/tags/review-base/cmm-source-survey-20261009^{}')=='c0adc2c0763e1515ed07dc712b024974d98fb342'
 r['issues']={str(n):api(f'issues/{n}') for n in [186,375,376,377,378,379,380,381,382,383]}
 assert all(r['issues'][str(n)]['state']=='open' for n in [186,375,376,377,378,379])
 assert all(r['issues'][str(n)]['state']=='closed' for n in [380,381,382,383])
 r.update(exit_code=0,worktree_preserved_detached=str(W),remote_branch_absent=True,local_branch_absent=True)
except Exception as e:r.update(exit_code=1,error=str(e))
finally:
 r['finished_at']=now();f.seek(0);json.dump(r,f,indent=2);f.write('\n');f.truncate();f.close();print(json.dumps({k:v for k,v in r.items() if k not in ['commands','issues']},indent=2))
raise SystemExit(r['exit_code'])
