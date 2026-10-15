from pathlib import Path
import ast, copy, datetime, hashlib, json, os, stat, subprocess
from urllib.parse import urlencode

now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
root=Path('/private/tmp')/('cmm-round102-guard-regression-'+datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ'))
root.mkdir(exist_ok=False)
sources={n:Path('/private/tmp')/('cmm-round102-'+n+'.py') for n in ['queue','cleanup','finalize','hosted-final-collector']}
hashes={n:sha(p) for n,p in sources.items()}
trees={n:ast.parse(p.read_text()) for n,p in sources.items()}
commands=[];cases=[];started=now()
env={k:v for k,v in os.environ.items() if not k.startswith('GIT_')}
env.update(GIT_CONFIG_NOSYSTEM='1',GIT_CONFIG_GLOBAL='/dev/null',GIT_AUTHOR_NAME='Disposable regression',GIT_AUTHOR_EMAIL='fixture@example.invalid',GIT_COMMITTER_NAME='Disposable regression',GIT_COMMITTER_EMAIL='fixture@example.invalid')
def git(repo,*args,ok=True):
 assert repo.resolve().is_relative_to(root.resolve())
 cmd=['git','-c','core.hooksPath=/dev/null',*args]
 p=subprocess.run(cmd,cwd=repo,env=env,text=True,capture_output=True)
 commands.append({'at':now(),'cwd':str(repo),'command':cmd,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
 if ok:assert p.returncode==0,(cmd,p.stderr)
 return p
def textgit(repo,*args):return git(repo,*args).stdout.strip()
def record(name,details):cases.append({'name':name,'status':'passed','details':details})
def call_for(tree,operation):
 calls=[n for n in ast.walk(tree) if isinstance(n,ast.Call) and isinstance(n.func,ast.Name) and n.func.id=='git' and n.args and isinstance(n.args[0],ast.Constant) and n.args[0].value==operation]
 assert len(calls)==1,(operation,len(calls));return calls[0]
def arguments(call,bindings):
 return [eval(compile(ast.Expression(x),'<isolated argument>','eval'),{'__builtins__':{}},bindings) for x in call.args]
merge_call=call_for(trees['finalize'],'merge');delete_call=call_for(trees['cleanup'],'update-ref')
assert any(isinstance(a,ast.Constant) and a.value=='--no-overwrite-ignore' for a in merge_call.args)
assert isinstance(delete_call.args[-1],ast.Name) and delete_call.args[-1].id=='HEAD'
preassign=next(n for n in ast.walk(trees['finalize']) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='newly_tracked' for t in n.targets))
preassert=next(n for n in ast.walk(trees['finalize']) if isinstance(n,ast.Assert) and 'newly_tracked' in ast.unparse(n.test))
ownerassert=next(n for n in ast.walk(trees['cleanup']) if isinstance(n,ast.Assert) and "git('worktree'" in ast.unparse(n.test))
def guard(nodes,bindings):
 exec(compile(ast.fix_missing_locations(ast.Module(body=nodes,type_ignores=[])),'<isolated guard>','exec'),bindings)
def expect_refusal(f):
 try:f()
 except AssertionError:return
 raise AssertionError('Expected guard refusal')
def fixture(name,collision):
 repo=root/name;repo.mkdir();git(repo,'init','-q','-b','main')
 (repo/'.gitignore').write_text('collision.txt\nkeep.ignore\n');(repo/'seed.txt').write_text('base\n')
 git(repo,'add','.gitignore','seed.txt');git(repo,'commit','-q','-m','base');base=textgit(repo,'rev-parse','HEAD')
 git(repo,'checkout','-q','-b','incoming');(repo/'collision.txt').write_text('tracked target content\n');git(repo,'add','-f','collision.txt');git(repo,'commit','-q','-m','target');target=textgit(repo,'rev-parse','HEAD')
 git(repo,'checkout','-q','main');(repo/'keep.ignore').write_text('preserved unrelated ignored content\n')
 if collision:(repo/'collision.txt').write_text('valuable ignored content\n');(repo/'collision.txt').chmod(0o600)
 return repo,base,target
def binds(repo,base,target,files):return {'git':lambda *a:textgit(repo,*a),'BASE':base,'MERGE':target,'d':{'main':{'files':files}}}

repo,base,target=fixture('ignored-collision',True)
original=(repo/'collision.txt').read_bytes();mode=stat.S_IMODE((repo/'collision.txt').stat().st_mode)
expect_refusal(lambda:guard([preassign,preassert],binds(repo,base,target,{'collision.txt':{}})))
assert textgit(repo,'rev-parse','HEAD')==base and (repo/'collision.txt').read_bytes()==original
record('preserved-inventory collision rejected before merge','Exact corrected AST preflight rejects the newly tracked ignored path; HEAD and bytes unchanged.')
guard([preassign,preassert],binds(repo,base,target,{}))
p=git(repo,*arguments(merge_call,{'MERGE':target}),ok=False)
assert p.returncode!=0 and textgit(repo,'rev-parse','HEAD')==base and (repo/'collision.txt').read_bytes()==original and stat.S_IMODE((repo/'collision.txt').stat().st_mode)==mode
record('merge flag protects collision absent from old inventory','Exact corrected merge argv refuses an ignored path even when it was not captured in the earlier preservation inventory; HEAD, bytes and mode remain unchanged.')

safe,base2,target2=fixture('safe-fast-forward',False);keep=(safe/'keep.ignore').read_bytes()
guard([preassign,preassert],binds(safe,base2,target2,{'keep.ignore':{}}));git(safe,*arguments(merge_call,{'MERGE':target2}))
assert textgit(safe,'rev-parse','HEAD')==target2 and (safe/'keep.ignore').read_bytes()==keep
record('non-colliding fast-forward succeeds','Exact corrected merge argv advances HEAD and preserves unrelated ignored bytes.')

old,oldbase,oldtarget=fixture('old-behavior-control',True)
oldtree=ast.parse(Path('/private/tmp/cmm-round101-finalize.py').read_text());oldmerge=call_for(oldtree,'merge')
git(old,*arguments(oldmerge,{'MERGE':oldtarget}))
assert textgit(old,'rev-parse','HEAD')==oldtarget and (old/'collision.txt').read_text()=='tracked target content\n'
record('prior behavior reproduces ignored overwrite in disposable control','Prior merge argv overwrites the disposable ignored file, establishing that the regression exercises the identified failure path.')

delete=root/'deletion';delete.mkdir();git(delete,'init','-q','-b','main');(delete/'seed').write_text('base\n');git(delete,'add','seed');git(delete,'commit','-q','-m','base');expected=textgit(delete,'rev-parse','HEAD')
git(delete,'branch','topic');(delete/'seed').write_text('advanced\n');git(delete,'commit','-q','-am','advanced');advanced=textgit(delete,'rev-parse','HEAD');git(delete,'checkout','-q','--detach',expected)
git(delete,'config','branch.topic.description','keep harmless configuration')
guard([ownerassert],{'git':lambda *a:textgit(delete,*a),'BRANCH':'topic'})
git(delete,'update-ref','refs/heads/topic',advanced,expected)
p=git(delete,*arguments(delete_call,{'BRANCH':'topic','HEAD':expected}),ok=False)
assert p.returncode!=0 and textgit(delete,'rev-parse','refs/heads/topic')==advanced and textgit(delete,'rev-parse','HEAD')==expected
record('advanced local branch refuses expected-old-OID deletion','A branch advance after capture makes the exact corrected CAS deletion fail; the advanced reference and detached HEAD survive.')
git(delete,'update-ref','refs/heads/topic',expected,advanced)
guard([ownerassert],{'git':lambda *a:textgit(delete,*a),'BRANCH':'topic'});git(delete,*arguments(delete_call,{'BRANCH':'topic','HEAD':expected}))
assert git(delete,'show-ref','--verify','--quiet','refs/heads/topic',ok=False).returncode==1 and textgit(delete,'rev-parse','HEAD')==expected and textgit(delete,'config','branch.topic.description')=='keep harmless configuration'
record('exact local branch deletion succeeds and retains configuration','Expected OID matches; branch disappears, detached HEAD and harmless branch configuration remain.')
git(delete,'branch','topic',expected);other=root/'owned-worktree';git(delete,'worktree','add','-q',str(other),'topic')
expect_refusal(lambda:guard([ownerassert],{'git':lambda *a:textgit(delete,*a),'BRANCH':'topic'}))
assert textgit(delete,'rev-parse','refs/heads/topic')==expected
record('worktree-owned branch refuses deletion before CAS','The exact corrected ownership assertion rejects a topic branch checked out in another disposable worktree.')

prassert=next(n for n in ast.walk(trees['queue']) if isinstance(n,ast.Assert) and "pr['base']['ref']" in ast.unparse(n.test))
pr={'base':{'ref':'main','repo':{'full_name':'CultureBotAI/CMMMech'}},'head':{'ref':'topic','repo':{'full_name':'CultureBotAI/CMMMech'}}}
guard([prassert],{'pr':pr,'BRANCH':'topic','REPO':'CultureBotAI/CMMMech'})
for arm,field in [('base','ref'),('head','ref'),('base','repo'),('head','repo')]:
 changed=copy.deepcopy(pr);changed[arm][field]={'full_name':'elsewhere/repository'} if field=='repo' else 'wrong-ref'
 expect_refusal(lambda:guard([prassert],{'pr':changed,'BRANCH':'topic','REPO':'CultureBotAI/CMMMech'}))
record('PR identity fixtures bind both refs and repositories','Exact corrected queue assertion accepts intended identities and rejects four wrong-ref/repository alternatives.')

fn=next(n for n in trees['hosted-final-collector'].body if isinstance(n,ast.FunctionDef) and n.name=='workflow')
def workflow_fixture(change):
 head='a'*40;run={'id':101,'created_at':'2026-10-15T20:00:00Z','run_number':5,'run_attempt':1,'head_sha':head,'event':'push','path':'.github/workflows/pages.yaml','status':'completed','conclusion':'success','html_url':'https://fixture.invalid/run/101','updated_at':'2026-10-15T20:01:00Z'}
 job={'id':201,'name':'fixture','status':'completed','conclusion':'success','started_at':'2026-10-15T20:00:00Z','completed_at':'2026-10-15T20:01:00Z','head_sha':head,'run_id':101,'html_url':'https://fixture.invalid/job/201','check_run_url':'https://fixture.invalid/check-runs/301'}
 check={'id':301,'name':'fixture','status':'completed','conclusion':'success','head_sha':head,'output':{'annotations_count':0},'html_url':'https://fixture.invalid/check/301'}
 fresh=copy.deepcopy(run);final=copy.deepcopy(run)
 if change=='new-run':fresh.update(id=102,run_number=6,created_at='2026-10-15T20:02:00Z',status='queued',conclusion=None)
 if change=='new-attempt':fresh['run_attempt']=2;final['run_attempt']=2
 def api(name,*args,**kwargs):
  if name=='fixture-runs':return [{'workflow_runs':[run]}]
  if name=='fixture-runs-final':return [{'workflow_runs':[run,fresh]}] if change=='new-run' else [{'workflow_runs':[fresh]}]
  if name in ['fixture-latest-run','fixture-attempt']:return run
  if name=='fixture-latest-run-recheck':return final
  if name=='fixture-attempt-jobs':return [{'jobs':[job],'total_count':1}]
  if name=='fixture-check-301':return check
  if name=='fixture-check-301-annotations':return [[]]
  raise AssertionError(name)
 ns={'api':api,'repo':'fixture/repository','urlencode':urlencode}
 exec(compile(ast.fix_missing_locations(ast.Module(body=[fn],type_ignores=[])),'<isolated collector function>','exec'),ns)
 return ns['workflow'](('fixture','pages.yaml','push',head))
assert workflow_fixture('unchanged')['passed'] is True
assert workflow_fixture('new-run')['passed'] is False
assert workflow_fixture('new-attempt')['passed'] is False
record('collector fixtures reject newer runs and attempts','Exact corrected workflow function runs only against in-memory API responses. Stable evidence passes; newer matching run and incremented attempt each fail freshness.')

assert all(sha(sources[n])==h for n,h in hashes.items())
receipt={'started_at':started,'finished_at':now(),'status':'passed','scope':'Disposable local Git repositories and isolated AST guard/function fixtures only. Complete publication templates were never executed. No real CMMMech refs, original-main files, remote repository or GitHub API were touched.','test_script':str(Path(__file__)),'test_script_sha256':sha(__file__),'template_sources':[{'path':str(sources[n]),'sha256':h,'contains_binding_sentinels':'ROUND102_' in sources[n].read_text()} for n,h in hashes.items()],'cases':cases,'commands':commands,'non_atomic_limit':'Worktree ownership and final remote evidence observations remain non-atomic; CAS protects a changed local OID, and no perpetual freshness guarantee is asserted.'}
(root/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
Path('/private/tmp/cmm-round102-vanadium-research/operational-guard-regression-result.json').write_text(json.dumps({'path':str(root/'receipt.json'),'sha256':sha(root/'receipt.json'),'cases':len(cases),'status':'passed'},indent=2)+'\n')
print(json.dumps({'receipt':str(root/'receipt.json'),'sha256':sha(root/'receipt.json'),'cases':len(cases),'status':'passed'},indent=2))
