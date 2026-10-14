"""Execute only AST-extracted audit guard against temporary fixtures; no helper top-level execution."""
from pathlib import Path
import ast,copy,datetime,hashlib,json,tempfile
HELPER=Path('/private/tmp/cmm-round74-commit.py')
INITIAL=Path('/private/tmp/cmm-round74-helper-peer-20261014T145607Z-sources/cmm-round74-commit.py')
code=HELPER.read_bytes();tree=ast.parse(code);node=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='require_final_audit')
ns={'hashlib':hashlib};exec(compile(ast.Module(body=[node],type_ignores=[]),str(HELPER),'exec'),ns)
oldtree=ast.parse(INITIAL.read_text());oldnode=next(n for n in oldtree.body if isinstance(n,ast.Assert) and "audit['passed']" in ast.unparse(n))
oldcompiled=compile(ast.Module(body=[oldnode],type_ignores=[]),str(INITIAL),'exec')
# This extracted historical assertion demonstrates the reported admission defect only;
# full previous helper is never run and its additional hash checks remain acknowledged.
base='a'*40;branch='curate/test';cfg={'counts':{'record_count':7,'covered_records':7},'issues':{'corrected_review_issues':[99],'closed_source_issues':[],'open_source_issues':[100]}}
cases=[('pass',None,True),('pass_with_limitations',('verdict','pass_with_limitations'),True),('passed_false',('passed',False),False),('passed_truthy',('passed',1),False),('needs_curation',('verdict','needs_curation'),False),('missing_verdict',('delete','verdict'),False),('wrong_state',('state','git_commit'),False),('missing_state',('delete','state'),False),('bool_false_unresolved',('unresolved_corrective_findings',False),False),('float_zero_unresolved',('unresolved_corrective_findings',0.0),False),('string_zero_unresolved',('unresolved_corrective_findings','0'),False),('positive_unresolved',('unresolved_corrective_findings',1),False),('missing_unresolved',('delete','unresolved_corrective_findings'),False),('wrong_base',('base','b'*40),False),('wrong_branch',('branch','main'),False),('missing_counts',('delete','counts'),False),('stale_counts',('counts',{'record_count':6,'covered_records':6}),False),('missing_issues',('delete','issues'),False),('stale_issues',('issues',{'corrected_review_issues':[],'closed_source_issues':[],'open_source_issues':[100]}),False),('missing_input',('missing_input',None),False),('extra_input',('extra_input',None),False),('duplicate_input',('duplicate_input',None),False),('missing_sha',('missing_sha',None),False),('wrong_sha',('wrong_sha',None),False),('changed_bytes',('changed_bytes',None),False),('deleted_file',('deleted_file',None),False),('symlink',('symlink',None),False),('omitted_candidate',('omitted_candidate',None),False),('included_own_audit',('included_own_audit',None),False)]
results=[]
for name,mutation,want in cases:
 with tempfile.TemporaryDirectory(prefix='cmm-round74-audit-fixture-',dir='/private/tmp') as td:
  root=Path(td);record=root/'record.yaml';record.write_text('record: current\n');other=root/'source.json';other.write_text('{}\n');ap=root/'final.json';ap.write_text('{}');ap.with_suffix('.md').write_text('audit');names={'record.yaml','source.json','final.json','final.md'}
  sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
  a={'passed':True,'verdict':'pass','state':'working_tree','unresolved_corrective_findings':0,'base':base,'branch':branch,'counts':copy.deepcopy(cfg['counts']),'issues':copy.deepcopy(cfg['issues']),'working_inputs':[{'path':p.name,'sha256':sha(p)} for p in [record,other]]}
  if mutation:
   k,v=mutation
   if k=='delete':del a[v]
   elif k=='missing_input':a['working_inputs'].pop()
   elif k=='extra_input':a['working_inputs'].append({'path':'unreviewed','sha256':'0'*64})
   elif k=='duplicate_input':a['working_inputs'].append(a['working_inputs'][0].copy())
   elif k=='missing_sha':del a['working_inputs'][0]['sha256']
   elif k=='wrong_sha':a['working_inputs'][0]['sha256']='0'*64
   elif k=='changed_bytes':record.write_text('record: altered\n')
   elif k=='deleted_file':record.unlink()
   elif k=='symlink':record.rename(root/'real.yaml');record.symlink_to(root/'real.yaml')
   elif k=='omitted_candidate':names.add('unreviewed.yaml')
   elif k=='included_own_audit':a['working_inputs'].append({'path':'final.json','sha256':sha(ap)})
   else:a[k]=v
  try:got=ns['require_final_audit'](a,root,names,ap,base,branch,cfg);detail='accepted'
  except (RuntimeError,KeyError,TypeError) as e:got=False;detail=str(e)
  old_accepted=None
  if name in {'needs_curation','missing_verdict','wrong_state','missing_state','bool_false_unresolved','float_zero_unresolved','missing_counts','stale_counts','missing_issues','stale_issues'}:
   try:exec(oldcompiled,{'audit':a,'base':base,'branch':branch});old_accepted=True
   except (AssertionError,KeyError):old_accepted=False
   assert old_accepted is True,(name,'historical demonstration failed')
  results.append({'case':name,'expected_accept':want,'accepted':bool(got),'passed':bool(got)==want,'detail':detail,'historical_assertion_accepted':old_accepted})
assert HELPER.read_bytes()==code,'Helper changed during fixtures'
now=datetime.datetime.now(datetime.timezone.utc);out=Path('/private/tmp')/('cmm-round74-audit-contract-regression-'+now.strftime('%Y%m%dT%H%M%SZ')+'.json')
r={'timestamp':now.isoformat(),'passed':all(r['passed'] for r in results),'cases':results,'case_count':len(results),'helper':str(HELPER),'helper_sha256':hashlib.sha256(code).hexdigest(),'initial_helper':str(INITIAL),'initial_helper_sha256':hashlib.sha256(INITIAL.read_bytes()).hexdigest(),'fixture_source':str(Path(__file__)),'fixture_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Only actual AST function and historical audit-status assertion executed against temporary files. No publication helper top-level, Git or network mutation.'}
out.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'receipt':str(out),'passed':r['passed'],'cases':len(results),'helper_sha256':r['helper_sha256']}));assert r['passed']
