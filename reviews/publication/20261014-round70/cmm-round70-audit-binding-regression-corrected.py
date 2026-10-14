"""Exercise exact acceptance gate in isolation without executing publication mutations."""
from pathlib import Path
import ast,hashlib,json,tempfile,copy,datetime
p=Path('/private/tmp/cmm-round70-commit.py');tree=ast.parse(p.read_text())
fn=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='require_final_audit')
namespace={'hashlib':hashlib};exec(compile(ast.Module(body=[fn],type_ignores=[]),str(p),'exec'),namespace)
check=namespace['require_final_audit'];cases=[]
with tempfile.TemporaryDirectory(prefix='cmm-round70-binding-fixture-',dir='/private/tmp') as d:
 root=Path(d);f=root/'record.yaml';f.write_text('reviewed bytes\n');auditpath=root/'publication-final.json';auditpath.write_text('{}');auditpath.with_suffix('.md').write_text('review')
 config={'counts':{'records':1},'issues':{'fixed':[999]}};names={'record.yaml','publication-final.json','publication-final.md'}
 good={'passed':True,'verdict':'pass_with_limitations','unresolved_corrective_findings':0,'base':'a'*40,'branch':'owned','state':'working_tree','counts':config['counts'],'issues':config['issues'],'working_inputs':[{'path':'record.yaml','sha256':hashlib.sha256(f.read_bytes()).hexdigest()}]}
 def exercise(name,mutate=None,candidate_names=None,expected=False):
  v=copy.deepcopy(good)
  if mutate:mutate(v)
  try:check(v,root,candidate_names if candidate_names is not None else names,auditpath,'a'*40,'owned',config);accepted=True
  except RuntimeError:accepted=False
  assert accepted==expected,(name,accepted,expected)
  cases.append({'case':name,'accepted':accepted,'expected':expected,'passed':True})
 exercise('valid exact package',expected=True)
 exercise('failed with positive verdict',lambda v:v.update(passed=False))
 exercise('pass flag with negative verdict',lambda v:v.update(verdict='needs_curation'))
 exercise('unresolved corrective finding',lambda v:v.update(unresolved_corrective_findings=1))
 exercise('boolean zero is not an integer',lambda v:v.update(unresolved_corrective_findings=False))
 exercise('wrong base',lambda v:v.update(base='b'*40))
 exercise('mismatched counts',lambda v:v.update(counts={'records':2}))
 exercise('mismatched issues',lambda v:v.update(issues={'fixed':[]}))
 exercise('unreviewed extra file',candidate_names=names|{'additional.yaml'})
 exercise('missing candidate file',candidate_names=names-{'record.yaml'})
 exercise('duplicate audit input',lambda v:v['working_inputs'].append(copy.deepcopy(v['working_inputs'][0])))
 f.write_text('changed bytes\n');exercise('changed input bytes')
 f.unlink();f.symlink_to(auditpath);exercise('symlink replacement')
receipt={'recorded_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'passed':True,'scope':'Extracted actual gate AST tested against isolated temporary file fixtures; no Git or GitHub mutations.','helper':{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()},'cases':cases}
out=Path('/private/tmp/cmm-round70-audit-binding-regression-corrected.json');assert not out.exists();out.write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps({'passed':True,'cases':len(cases)}))
