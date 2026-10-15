"""Verify a reviewed squash tree in a fresh main-only clone before/after merge."""
from pathlib import Path
import argparse,datetime,hashlib,json,os,subprocess,tarfile,re
T=Path('/private/tmp');W=T/'CMMMech-expansion-round103-20261015';REPO='https://github.com/CultureBotAI/CMMMech.git';BASE='44d5b468519eb862b32ef54bf7c066bc0f79ba62';BRANCH='curate/cmm-expansion-round103-20261015'
a=argparse.ArgumentParser();a.add_argument('mode',choices=['preflight','postmerge']);a.add_argument('--topic-head',required=True);a.add_argument('--expected-tree',required=True);a.add_argument('--merge-commit');args=a.parse_args()
for x in [args.topic_head,args.expected_tree]+([args.merge_commit] if args.merge_commit else []):assert re.fullmatch('[0-9a-f]{40}',x)
assert (args.mode=='postmerge')==bool(args.merge_commit)
now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ');prefix=T/f'cmm-round103-{args.mode}-{stamp}';clone=T/f'CMMMech-round103-{args.mode}-{stamp}';logpath=Path(str(prefix)+'.log');out=Path(str(prefix)+'.json');coverage=Path(str(prefix)+'-coverage.json');archive=Path(str(prefix)+'.tar');sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
for p in [clone,logpath,out,coverage,archive]:assert not p.exists() and not p.is_symlink()
config=T/'cmm-round103-helper-config.json';configsha=sha(config);cfg=json.loads(config.read_text());assert cfg['base']==BASE and cfg['branch']==BRANCH
receipt={'mode':args.mode,'started_at':now(),'trusted_base':BASE,'topic_head':args.topic_head,'expected_tree':args.expected_tree,'merge_commit':args.merge_commit,'clone':str(clone),'config_sha256':configsha,'helper_sha256':sha(__file__),'commands':[]};env=dict(os.environ,UV_OFFLINE='1',UV_CACHE_DIR='/private/tmp/cmmmech-uv-cache',PYTHONDONTWRITEBYTECODE='1');log=logpath.open('x');slot=out.open('x');json.dump({'state':'in_progress','started_at':now()},slot);slot.flush()
def run(cmd,cwd=None,allowed=(0,)):
 s=now();p=subprocess.run(cmd,cwd=cwd,env=env,capture_output=True,text=True);log.write('$ '+repr(cmd)+'\n'+p.stdout+p.stderr+'\n');log.flush();receipt['commands'].append({'command':cmd,'cwd':str(cwd) if cwd else None,'started_at':s,'finished_at':now(),'exit_code':p.returncode,'allowed_exit_codes':list(allowed)});assert p.returncode in allowed,(cmd,p.returncode,p.stderr);return p.stdout.strip()
def git(cwd,*a,**kw):return run(['git','-C',str(cwd),*a],**kw)
def no_topic():
 git(clone,'cat-file','-e',args.topic_head+'^{commit}',allowed=(1,128))
try:
 assert git(W,'rev-parse',args.topic_head+'^{tree}')==args.expected_tree
 if args.mode=='preflight':assert git(W,'rev-parse','HEAD')==args.topic_head and not git(W,'status','--porcelain=v1','--untracked-files=all')
 else:
  git(W,'show-ref','--verify','--quiet','refs/heads/'+BRANCH,allowed=(1,));assert not git(W,'ls-remote','origin','refs/heads/'+BRANCH)
 run(['git','clone','--single-branch','--branch','main','--no-tags',REPO,str(clone)]);git(clone,'fetch','origin','--tags');assert git(clone,'config','--get-all','remote.origin.fetch')=='+refs/heads/main:refs/remotes/origin/main';no_topic()
 if args.mode=='preflight':
  assert git(clone,'rev-parse','HEAD')==BASE
  source_paths=set(git(W,'ls-tree','-r','--name-only',args.topic_head).splitlines());old=set(git(clone,'ls-files').splitlines())
  for name in old-source_paths:
   p=clone/name;assert p.is_relative_to(clone) and '..' not in Path(name).parts;p.unlink()
  with archive.open('xb') as f:p=subprocess.run(['git','-C',str(W),'archive','--format=tar',args.topic_head],stdout=f,stderr=subprocess.PIPE);assert p.returncode==0,p.stderr
  with tarfile.open(archive) as tar:
   assert all(not m.name.startswith('/') and '..' not in Path(m.name).parts and '.git' not in Path(m.name).parts for m in tar.getmembers());tar.extractall(clone,filter='data')
  git(clone,'add','--all');git(clone,'-c','user.name=codex','-c','user.email=codex@localhost','-c','commit.gpgsign=false','commit','-m','Synthetic squash verification for round103');receipt['synthetic_commit']=git(clone,'rev-parse','HEAD');assert git(clone,'rev-parse','HEAD^')==BASE
 else:
  assert git(clone,'rev-parse','HEAD')==args.merge_commit;assert git(clone,'rev-list','--parents','-n','1','HEAD').split()==[args.merge_commit,BASE]
 assert git(clone,'rev-parse','HEAD^{tree}')==args.expected_tree;no_topic()
 run(['uv','sync','--quiet','--locked','--extra','dev','--offline'],clone)
 for cmd in [['uv','run','--locked','cmmmech','validate','--require-records'],['uv','run','--locked','cmmmech','validate-history','--base',BASE],['just','review-check','--base',BASE,'--require-reviews']]:run(cmd,clone)
 run([str(clone/'.venv/bin/python'),str(T/'cmm-round103-isolated-coverage.py'),'--clone',str(clone),'--output',str(coverage)],clone)
 cv=json.loads(coverage.read_text());assert cv['passed'];receipt['counts']={k:cv[k] for k in cfg['counts']};receipt['coverage']={'path':str(coverage),'sha256':sha(coverage)}
 assert sha(config)==configsha;assert not git(clone,'status','--porcelain=v1','--untracked-files=all');assert git(clone,'rev-parse','HEAD^{tree}')==args.expected_tree;no_topic();receipt['exit_code']=0
except Exception as e:receipt['exit_code']=1;receipt['error']=str(e)
finally:
 log.close();receipt.update(finished_at=now(),log=str(logpath),log_sha256=sha(logpath));slot.seek(0);json.dump(receipt,slot,indent=2);slot.write('\n');slot.truncate();slot.close();print(json.dumps({k:v for k,v in receipt.items() if k!='commands'},indent=2))
raise SystemExit(receipt['exit_code'])
