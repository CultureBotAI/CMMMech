from pathlib import Path
import argparse, ast, copy, datetime, hashlib, json, sys, tempfile, types, uuid

source = Path('/private/tmp/cmm-round96-commit.py')
tree = ast.parse(source.read_text())
functions = {n.name:n for n in tree.body if isinstance(n, ast.FunctionDef)}
env = {'Path':Path, 'W':Path('/private/tmp/CMMMech-expansion-round96-20261015'), 'argparse':argparse}
exec(compile(ast.Module(body=[functions['guard'], functions['main']], type_ignores=[]), str(source), 'exec'), env)
base='a'*40
cfg={'base':base,'counts':dict(record_count=1,history_count=1,structured_review_count=1,review_base_count=1,covered_records=1)}
records={'data/records/fixture.yaml':'1'*64}; histories={'history/records/fixture/session.yaml':'2'*64}; reviews={'reviews/structured/fixture/review.yaml':'3'*64}
actual=dict(records,**histories,**reviews);bindings={'helper':'4'*64}
commands=[['just','check'],['uv','run','--locked','cmmmech','validate','--require-records'],['uv','run','--locked','cmmmech','validate-history','--base',base],['uv','run','--locked','python','scripts/render_pages.py','--check']]
g={'base':base,'worktree':str(env['W']),'exit_code':0,'inputs_unchanged':True,'commands':[dict(command=x,exit_code=0) for x in commands],'record_inputs':records}
rv={'base':base,'exit_code':0,'command':['just','review-check','--base',base,'--require-reviews']}
cv=dict(cfg['counts'],passed=True,root=str(env['W']),records=[dict(path=k,sha256=v,matching_scientific_reviews=['fixture']) for k,v in records.items()],bases=[dict(available_commit=True)])
prep=dict(passed=True,base=base,head=base,files=actual,record_inputs=records,history_inputs=histories,review_inputs=reviews,bindings=bindings)
def args(): return json.loads(json.dumps([cfg,g,rv,cv,prep,actual,records,histories,reviews,bindings]))
results=[]
def record(name): results.append({'case':name,'passed':True})
a=args();assert a[1]['record_inputs'] is not a[6] and a[4]['record_inputs'] is not a[6] and a[4]['files'] is not a[5]
a[6]['data/records/fixture.yaml']='f'*64
assert a[1]['record_inputs']['data/records/fixture.yaml']=='1'*64 and a[4]['record_inputs']['data/records/fixture.yaml']=='1'*64
record('Independent JSON fixture inputs do not share mutable dictionaries')
env['guard'](*args());record('Valid isolated receipt contract accepted')
cases=[
 ('Changed record digest',lambda a:a[6].update({'data/records/fixture.yaml':'f'*64})),
 ('Added record',lambda a:a[6].update({'data/records/new.yaml':'f'*64})),
 ('Changed history digest',lambda a:a[7].update({'history/records/fixture/session.yaml':'f'*64})),
 ('Changed review digest',lambda a:a[8].update({'reviews/structured/fixture/review.yaml':'f'*64})),
 ('Changed candidate manifest',lambda a:a[5].update({'README.md':'f'*64})),
 ('Changed bound helper digest',lambda a:a[9].update({'helper':'f'*64})),
 ('Wrong gate base',lambda a:a[1].update(base='b'*40)),
 ('Wrong gate worktree',lambda a:a[1].update(worktree='/private/tmp/other')),
 ('Missing gate success field',lambda a:a[1].pop('exit_code')),
 ('Unstable gate inputs',lambda a:a[1].update(inputs_unchanged=False)),
 ('Failed gate command',lambda a:a[1]['commands'][0].update(exit_code=1)),
 ('Missing gate command',lambda a:a[1]['commands'].pop()),
 ('Wrong review-check base',lambda a:a[2].update(base='b'*40)),
 ('Missing review-check success',lambda a:a[2].pop('exit_code')),
 ('Wrong review-check command',lambda a:a[2].update(command=['true'])),
 ('Missing coverage success',lambda a:a[3].pop('passed')),
 ('Wrong coverage root',lambda a:a[3].update(root='/private/tmp/other')),
 ('Wrong coverage count',lambda a:a[3].update(record_count=2)),
 ('Missing scientific coverage',lambda a:a[3]['records'][0].update(matching_scientific_reviews=[])),
 ('Unavailable review base',lambda a:a[3]['bases'][0].update(available_commit=False)),
 ('Wrong preparation base',lambda a:a[4].update(base='b'*40)),
 ('Wrong preparation head',lambda a:a[4].update(head='b'*40)),
 ('Missing preparation success',lambda a:a[4].pop('passed')),
]
for name,change in cases:
 a=args();change(a)
 try:env['guard'](*a)
 except (AssertionError,KeyError):record(name+' rejected')
 else:raise AssertionError('Not rejected: '+name)

class ReachedCollect(Exception): pass
called=[]
def forbidden_collect(): called.append('collect');raise ReachedCollect()
env['collect']=forbidden_collect
oldargv=sys.argv;sys.argv=['independent-fixture']
try:
 with tempfile.TemporaryDirectory(prefix='cmm-round96-independent-guard-',dir='/private/tmp') as td:
  env['T']=Path(td);out=Path(td)/'cmm-round96-commit-receipt.json'
  out.write_text('existing')
  try:env['main']()
  except AssertionError:assert not called;record('Existing output rejected before collect/staging')
  else:raise AssertionError('Existing output permitted')
  out.unlink();out.symlink_to(Path(td)/'does-not-exist')
  try:env['main']()
  except AssertionError:assert not called;record('Dangling output symlink rejected before collect/staging')
  else:raise AssertionError('Dangling output permitted')
  out.unlink()
  try:env['main']()
  except ReachedCollect:assert called==['collect'];record('Unused output reaches mocked collection only')
  else:raise AssertionError('Unique output did not reach collection')
finally:sys.argv=oldargv

# Execute only the extracted stage-byte comparison loop against a stub; no Git.
stage = next(n for n in ast.walk(functions['main']) if isinstance(n,ast.For) and any(isinstance(x,ast.Call) and isinstance(x.func,ast.Attribute) and x.func.attr=='check_output' for x in ast.walk(n)))
good=b'reviewed bytes\n';stage_env={'files':['fixture'],'actual':{'fixture':hashlib.sha256(good).hexdigest()},'W':env['W'],'hashlib':hashlib,'subprocess':types.SimpleNamespace(check_output=lambda *a,**kw:good)}
exec(compile(ast.Module(body=[stage],type_ignores=[]),str(source),'exec'),stage_env);record('Exact staged bytes accepted by actual comparison loop')
stage_env['subprocess']=types.SimpleNamespace(check_output=lambda *a,**kw:b'changed')
try:exec(compile(ast.Module(body=[stage],type_ignores=[]),str(source),'exec'),stage_env)
except AssertionError:record('Changed staged bytes rejected by actual comparison loop')
else:raise AssertionError('Changed staged bytes permitted')
assert any(isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr=='open' and any(isinstance(a,ast.Constant) and a.value=='x' for a in n.args) for n in ast.walk(functions['main']))
record('Final receipt uses exclusive-create mode in actual main AST')
out=Path('/private/tmp')/('cmm-round96-independent-commit-guard-results-'+datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid.uuid4().hex[:6]+'.json')
result={'recorded_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'passed':True,'helper_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'test_source':str(Path(__file__)),'test_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'cases':results,'scope':'Actual AST-extracted guard/main precondition/staged-byte loop only, isolated JSON fixtures, forbidden collect stub, temporary output-path fixtures. No collect, API, Git staging/commit or mutation branch executed.'}
with out.open('x') as f:f.write(json.dumps(result,indent=2)+'\n')
print(json.dumps({'path':str(out),'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'cases':len(results),'helper_sha256':result['helper_sha256']}))
