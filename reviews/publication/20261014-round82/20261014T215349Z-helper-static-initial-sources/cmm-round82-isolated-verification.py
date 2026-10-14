"""Read remote main into a NEW temporary clone; never mutate the source checkout."""
import argparse, datetime, hashlib, json, os, re, subprocess, sys, tarfile
from pathlib import Path

BASE='d26b03c7e8346b0caabb106f1aaf8acc3ed51623'
REMOTE='https://github.com/CultureBotAI/CMMMech.git'
BRANCH='curate/cmm-expansion-round82-20261014'
TAG='refs/tags/review-base/cmm-source-survey-20261009'
TAG_OBJECT='fc4040c3abcd28f0a9cc52467e308100144ad1fd'
TAG_COMMIT='c0adc2c0763e1515ed07dc712b024974d98fb342'
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('mode',choices=['preflight','postmerge'])
parser.add_argument('--topic-head',required=True)
parser.add_argument('--expected-tree',required=True)
parser.add_argument('--source',default='/private/tmp/CMMMech-expansion-round82-20261014')
parser.add_argument('--merge-commit')
parser.add_argument('--run-id',help='Unique letters/digits/hyphens suffix; default actual UTC timestamp')
args=parser.parse_args()
for value in [args.topic_head,args.expected_tree]+([args.merge_commit] if args.merge_commit else []):
 if not re.fullmatch('[0-9a-f]{40}',value):parser.error('Commit/tree arguments must be full lowercase 40-hex object IDs.')
if args.mode=='postmerge' and not args.merge_commit:parser.error('--merge-commit is required after actual merge and branch deletion.')
if args.mode=='preflight' and args.merge_commit:parser.error('--merge-commit is not used for preflight.')
run_id=args.run_id or datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
if not re.fullmatch('[A-Za-z0-9-]+',run_id):parser.error('Unsafe run ID.')
source=Path(args.source).resolve()
clone=Path('/private/tmp')/f'CMMMech-round82-{args.mode}-{run_id}'
prefix=Path('/private/tmp')/f'cmm-round82-{args.mode}-{run_id}'
receipt_path=Path(str(prefix)+'-terminal.json')
coverage_path=Path(str(prefix)+'-coverage.json')
log_path=Path(str(prefix)+'.log')
archive_path=Path(str(prefix)+'-topic.tar')
for p in [clone,receipt_path,coverage_path,log_path,archive_path]:
 if p.exists() or p.is_symlink():raise SystemExit('Refusing existing path: '+str(p))
env=dict(os.environ,GIT_OPTIONAL_LOCKS='0',UV_OFFLINE='1',UV_CACHE_DIR='/private/tmp/cmmmech-uv-cache',PYTHONDONTWRITEBYTECODE='1')
now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
receipt={'started_at':now(),'mode':args.mode,'source':str(source),'clone':str(clone),'trusted_base':BASE,'topic_head':args.topic_head,'expected_tree':args.expected_tree,'merge_commit':args.merge_commit,'commands':[],'log':str(log_path),'scope':'Source checkout read only. Remote operations are clone, fetch tags and ls-remote only. All new worktree/index/synthetic-commit operations are inside a fresh /private/tmp clone. No branch deletion, push, source checkout switch or source Git mutation. Existing paths are never removed or overwritten.'}
log=log_path.open('x')
def run(cmd,cwd=None,allowed=(0,),binary=False):
 start=now();p=subprocess.run(cmd,cwd=cwd,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
 output=p.stdout.decode('utf-8',errors='replace')
 log.write('$ '+repr(cmd)+'\n'+output+'\n');log.flush()
 receipt['commands'].append({'command':cmd,'cwd':str(cwd) if cwd else None,'started_at':start,'finished_at':now(),'exit_code':p.returncode,'allowed_exit_codes':list(allowed)})
 if p.returncode not in allowed:raise RuntimeError('Command failed with exit '+str(p.returncode)+': '+repr(cmd))
 return p.stdout if binary else output.strip()
def git(root,*cmd,**kw):return run(['git','-C',str(root),*cmd],**kw)
def require(condition,message):
 if not condition:raise RuntimeError(message)
def no_topic():
 p=subprocess.run(['git','-C',str(clone),'cat-file','-e',args.topic_head+'^{commit}'],env=env,capture_output=True)
 receipt.setdefault('topic_object_checks',[]).append({'recorded_at':now(),'exit_code':p.returncode,'absent':p.returncode!=0})
 require(p.returncode!=0,'Topic commit unexpectedly exists in fresh main/tag object database.')
def ensure_clone_path(p):
 require(p.is_relative_to(clone),'Unsafe clone-local removal path.')

try:
 require(source.is_dir(),'Source worktree missing.')
 require(git(source,'rev-parse',args.topic_head+'^{tree}')==args.expected_tree,'Source topic commit/tree differs from supplied reviewed tree.')
 if args.mode=='preflight':
  require(git(source,'rev-parse','HEAD')==args.topic_head,'Preflight source HEAD is not the supplied topic commit.')
  require(not git(source,'status','--porcelain=v1','--untracked-files=all'),'Preflight source worktree has uncommitted files.')
 else:
  git(source,'show-ref','--verify','--quiet','refs/heads/'+BRANCH,allowed=(0,1))
  require(receipt['commands'][-1]['exit_code']==1,'Local topic branch must be deleted by coordinator before postmerge verification.')
  remote_ref=git(source,'ls-remote','--exit-code',REMOTE,'refs/heads/'+BRANCH,allowed=(0,2))
  require(not remote_ref,'Remote topic branch must be deleted by coordinator before postmerge verification.')
 run(['git','clone','--single-branch','--branch','main','--no-tags',REMOTE,str(clone)])
 require(git(clone,'config','--get-all','remote.origin.fetch')=='+refs/heads/main:refs/remotes/origin/main','Clone fetch scope is not single-branch main.')
 git(clone,'fetch','origin','--tags')
 require(git(clone,'rev-parse',TAG)==TAG_OBJECT,'Preservation tag object mismatch.')
 require(git(clone,'rev-parse',TAG+'^{commit}')==TAG_COMMIT,'Preservation tag commit mismatch.')
 tag_remote=git(clone,'ls-remote','origin',TAG,TAG+'^{}')
 refs={line.split('\t')[1]:line.split('\t')[0] for line in tag_remote.splitlines()}
 require(refs.get(TAG)==TAG_OBJECT and refs.get(TAG+'^{}')==TAG_COMMIT,'Remote annotated tag no longer matches expected preservation target.')
 receipt['verified_retained_tag']={'ref':TAG,'tag_object':TAG_OBJECT,'peeled_commit':TAG_COMMIT,'remote_verified':True}
 no_topic()
 if args.mode=='preflight':
  require(git(clone,'rev-parse','HEAD')==BASE,'Remote main moved from trusted base; refresh review scope before preflight.')
  source_paths={x.decode() for x in git(source,'ls-tree','-r','-z','--name-only',args.topic_head,binary=True).split(b'\0') if x}
  main_paths={x.decode() for x in git(clone,'ls-files','-z',binary=True).split(b'\0') if x}
  for name in sorted(main_paths-source_paths):
   p=clone/name;ensure_clone_path(p)
   require(p.is_file() or p.is_symlink(),'Expected tracked clone file missing: '+name)
   p.unlink()
  with archive_path.open('xb') as archive:
   p=subprocess.run(['git','-C',str(source),'archive','--format=tar',args.topic_head],env=env,stdout=archive,stderr=subprocess.PIPE)
  require(p.returncode==0,'Source archive failed: '+p.stderr.decode())
  receipt['archive']={'path':str(archive_path),'sha256':hashlib.sha256(archive_path.read_bytes()).hexdigest(),'source_commit':args.topic_head}
  with tarfile.open(archive_path,'r') as archive:
   require(all(not m.name.startswith('/') and '..' not in Path(m.name).parts and '.git' not in Path(m.name).parts for m in archive.getmembers()),'Unsafe archive member.')
   archive.extractall(clone,filter='data')
  git(clone,'add','--all')
  git(clone,'-c','user.name=codex','-c','user.email=codex@localhost','-c','commit.gpgsign=false','commit','-m','Synthetic squash verification for reviewed round82 integration tree')
  require(git(clone,'rev-parse','HEAD^')==BASE,'Synthetic commit parent differs from trusted main base.')
  receipt['synthetic_commit']=git(clone,'rev-parse','HEAD')
 else:
  require(git(clone,'rev-parse','HEAD')==args.merge_commit,'Fresh remote main does not equal supplied actual merge commit.')
  require(git(clone,'rev-parse','HEAD^')==BASE,'Actual squash parent differs from reviewed trusted base.')
 require(git(clone,'rev-parse','HEAD^{tree}')==args.expected_tree,'Fresh squash/main tree differs from exact reviewed topic tree.')
 no_topic()
 run(['uv','sync','--quiet','--locked','--extra','dev','--offline'],cwd=clone)
 if args.mode=='postmerge':run(['just','check'],cwd=clone)
 run(['uv','run','--locked','cmmmech','validate','--require-records'],cwd=clone)
 run(['uv','run','--locked','cmmmech','validate-history','--base',BASE],cwd=clone)
 run(['just','review-check','--base',BASE,'--require-reviews'],cwd=clone)
 run([str(clone/'.venv/bin/python'),'/private/tmp/cmm-round82-isolated-coverage.py','--clone',str(clone),'--output',str(coverage_path)],cwd=clone)
 coverage=json.loads(coverage_path.read_text());require(coverage['passed'],'Exact coverage/count/base audit failed.')
 receipt['coverage_receipt']=str(coverage_path)
 receipt['counts']={k:coverage[k] for k in ['record_count','history_count','structured_review_count','review_base_count','covered_records']}
 require(not git(clone,'status','--porcelain=v1','--untracked-files=all'),'Fresh verification clone has tracked/unignored changes after gates.')
 require(git(clone,'rev-parse','HEAD^{tree}')==args.expected_tree,'Tree changed during verification.')
 no_topic()
 receipt['exit_code']=0
except Exception as exc:
 receipt['exit_code']=1;receipt['error']=str(exc)
finally:
 receipt['finished_at']=now();log.close();receipt['log_sha256']=hashlib.sha256(log_path.read_bytes()).hexdigest();receipt_path.write_text(json.dumps(receipt,indent=2)+'\n')
 print(json.dumps({'receipt':str(receipt_path),'log':str(log_path),'clone':str(clone),'exit_code':receipt['exit_code'],'error':receipt.get('error'),'counts':receipt.get('counts')},indent=2))
raise SystemExit(receipt['exit_code'])
