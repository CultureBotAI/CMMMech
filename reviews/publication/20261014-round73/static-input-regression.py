from pathlib import Path
from tempfile import TemporaryDirectory
from copy import deepcopy
import ast,json,hashlib,datetime,shutil
T=Path('/private/tmp'); helper=T/'cmm-round73-final-package-audit.py'; source=helper.read_text(); old=json.loads((T/'cmm-round73-helper-static-20261014T140400Z.json').read_text())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
node=next(n for n in ast.parse(source).body if isinstance(n,ast.For) and ast.unparse(n.iter)=="old_static['files']")
code=compile(ast.Module(body=[node],type_ignores=[]),str(helper),'exec')
def require(c,m):
 if not c:raise AssertionError(m)
with TemporaryDirectory(prefix='cmm-round73-static-input-fixtures-',dir=T) as td:
 pub=Path(td)
 for i in old['files']:
  if 'snapshot' in i:
   p=Path(i['snapshot']);dest=pub/p.parent.name.removeprefix('cmm-round73-')/p.name;dest.parent.mkdir(exist_ok=True);shutil.copyfile(p,dest)
 def run(name, mutate=None, current_bad=None, expected=True):
  d=deepcopy(old)
  if mutate:mutate(d)
  def digest(p):return 'f'*64 if str(p)==current_bad else sha(p)
  try:exec(code,{'old_static':d,'Path':Path,'PUB':pub,'sha':digest,'require':require});ok=True;error=None
  except Exception as e:ok=False;error=type(e).__name__+': '+str(e)
  assert ok==expected,(name,ok,error)
  return dict(name=name,expected_accept=expected,accepted=ok,passed=True,error=error)
 cases=[run('declared library and all thirteen real snapshots accepted'),run('changed imported library rejected',current_bad='/private/tmp/cmm-round57-recover-original.py',expected=False),run('missing round73 snapshot rejected',mutate=lambda d:d['files'][0].pop('snapshot'),expected=False),run('changed round73 snapshot digest rejected',mutate=lambda d:d['files'][0].update(sha256='f'*64),expected=False),run('changed current round73 helper rejected',current_bad='/private/tmp/cmm-round73-commit.py',expected=False)]
 out=T/'cmm-round73-static-input-regression.json';assert not out.exists();out.write_text(json.dumps(dict(recorded_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),passed=True,helper=str(helper),helper_sha256=sha(helper),fixture_source_sha256=sha(Path(__file__)),test_scope='Executes actual AST-selected original-input validation loop only; no top-level helper, Git, network or publication action.',cases=cases),indent=2)+'\n');print(out)
