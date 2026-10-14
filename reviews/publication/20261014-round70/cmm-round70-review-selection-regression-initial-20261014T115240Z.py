"""Read-only fixtures execute actual helper selector AST, never publication top levels."""
from pathlib import Path
from datetime import datetime,timezone
import ast,copy,hashlib,json,yaml
r=Path('/private/tmp');root=r/'CMMMech-expansion-round70-20261014';base='1d40bb5d7496a02b937acc1f6ef3aec5af5d32e7'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
files=[r/'cmm-round70-helper-config.json',r/'cmm-round70-build-report.py',r/'cmm-round70-closeout.py']
before={str(p):sha(p) for p in files};cfg=json.loads(files[0].read_text());reviews=[(p,yaml.safe_load(p.read_text())) for p in (root/'reviews/structured').rglob('review.yaml')]
assert cfg['counts']['structured_review_count']==394
c=cfg['resolved_review_successors']['hydroxylapatite'];positive_keys=['original_review','intermediate_review','review']
nodes=[];functions={}
for name in ['build-report','closeout']:
 p=r/f'cmm-round70-{name}.py';tree=ast.parse(p.read_text(),filename=str(p));matches=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='select_scientific_review'];assert len(matches)==1
 node=matches[0];nodes.append(ast.dump(node,include_attributes=False));ns={'sha':sha};exec(compile(ast.Module(body=[node],type_ignores=[]),str(p),'exec'),ns);functions[name]=ns['select_scientific_review']
assert nodes[0]==nodes[1], 'Builder and closeout selector behavior diverged'
outputs=[root/'research/ingests/round70-frontier-20261014.json',root/'research/ingests/round70-frontier-20261014.md',r/'cmm-round70-pr-body.md',r/'cmm-round70-closeout.md',r/'cmm-round70-closeout-posted.json']
output_before={str(p):(p.exists(),sha(p) if p.exists() else None) for p in outputs}
results=[]
def doc(rs,key):return next(d for p,d in rs if str(p.relative_to(root))==c[key])
def invoke(fn,rs,configuration,slug='hydroxylapatite'):
 p=root/'data/records'/f'{slug}.yaml';d=yaml.safe_load(p.read_text());return fn(slug,d['id'],str(p.relative_to(root)),sha(p),rs,configuration,root,base)
def run_case(name,mutator=None,valid=False,slug='hydroxylapatite'):
 for helper,fn in functions.items():
  rs=copy.deepcopy(reviews);configuration=copy.deepcopy(cfg)
  if mutator:mutator(rs,configuration)
  try:selection=invoke(fn,rs,configuration,slug)
  except (AssertionError,KeyError,StopIteration,FileNotFoundError) as e:
   assert not valid,(helper,name,type(e).__name__,str(e));results.append({'helper':helper,'case':name,'expected':'reject','passed':True,'reason':str(e)})
  else:
   assert valid,(helper,name,'unsafe acceptance')
   if slug=='hydroxylapatite':assert str(selection[0].relative_to(root))==c['review']
   results.append({'helper':helper,'case':name,'expected':'accept explicit final' if slug=='hydroxylapatite' else 'accept single original','passed':True,'selected':str(selection[0].relative_to(root))})
run_case('actual explicit three-positive chain',valid=True)
for slug in ['anorthite','boehmite','gibbsite','chlorapatite']:run_case('actual single original '+slug,valid=True,slug=slug)
for key in ['original_review','finding_review','intermediate_review','review']:
 run_case('missing chain member '+key,lambda rs,co,key=key:rs.__setitem__(slice(None),[(p,d) for p,d in rs if str(p.relative_to(root))!=c[key]]))
def extra(rs,co):
 d=copy.deepcopy(doc(rs,'review'));d['review_id']='20991231T235959Z-unapproved-latest';rs.append((root/'reviews/structured/20991231T235959Z-unapproved-latest/review.yaml',d))
run_case('extra positive latest review must not win',extra)
run_case('missing explicit config',lambda rs,co:co.pop('resolved_review_successors'))
run_case('incomplete config',lambda rs,co:co['resolved_review_successors']['hydroxylapatite'].pop('intermediate_review'))
run_case('wrong configured SI hash',lambda rs,co:co['resolved_review_successors']['hydroxylapatite'].__setitem__('correct_si_sha256','0'*64))
for key in ['intermediate_review','review']:
 run_case('wrong SI hash '+key,lambda rs,co,key=key:next(e for e in doc(rs,key)['evidence'] if e['evidence_id']=='si').__setitem__('snapshot_sha256','e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'))
 run_case('wrong SI locator '+key,lambda rs,co,key=key:next(e for e in doc(rs,key)['evidence'] if e['evidence_id']=='si').__setitem__('locator','empty failed download'))
 run_case('missing self-correction disclosure '+key,lambda rs,co,key=key:doc(rs,key)['reviewer'].__setitem__('independence_basis','Independent review.'))
 run_case('successor mislabeled independent '+key,lambda rs,co,key=key:doc(rs,key)['reviewer'].__setitem__('independence','independent'))
run_case('original independence lost',lambda rs,co:doc(rs,'original_review')['reviewer'].__setitem__('independence','self_review'))
run_case('original independence basis lost',lambda rs,co:doc(rs,'original_review')['reviewer'].__setitem__('independence_basis',''))
run_case('intermediate lineage lost',lambda rs,co:doc(rs,'intermediate_review')['findings'][0].__setitem__('previous_occurrences',[]))
for removed in [doc(reviews,'finding_review')['review_id'],doc(reviews,'intermediate_review')['review_id']]:
 run_case('final lineage missing '+removed,lambda rs,co,removed=removed:doc(rs,'review')['findings'][0].__setitem__('previous_occurrences',[v for v in doc(rs,'review')['findings'][0]['previous_occurrences'] if v['review_id']!=removed]))
run_case('final extra lineage',lambda rs,co:doc(rs,'review')['findings'][0]['previous_occurrences'].append({'repository':'CultureBotAI/CMMMech','review_id':'unrelated','finding_id':'F1'}))
run_case('wrong resolution issue key',lambda rs,co:doc(rs,'review')['findings'][0].__setitem__('issue_key','unrelated'))
run_case('wrong original finding status',lambda rs,co:doc(rs,'finding_review')['findings'][0].__setitem__('status','resolved'))
run_case('missing final disposition reason',lambda rs,co:doc(rs,'review')['findings'][0].__setitem__('disposition_reason',''))
run_case('unresolved final major finding',lambda rs,co:doc(rs,'review')['findings'][0].__setitem__('status','open'))
run_case('wrong source base',lambda rs,co:doc(rs,'review')['source'].__setitem__('git_revision','0'*40))
run_case('changed retained input hash',lambda rs,co:doc(rs,'review')['source']['inputs'][1].__setitem__('sha256','0'*64))
assert {str(p):sha(p) for p in files}==before, 'Fixture changed helper/config bytes'
assert {str(p):(p.exists(),sha(p) if p.exists() else None) for p in outputs}==output_before, 'Fixture ran publication side effects'
result={'recorded_at':datetime.now(timezone.utc).isoformat(),'passed':True,'test_count':len(results),'case_count':len(results)//2,'helpers':before,'selector_ast_identical':True,'execution_scope':'Only select_scientific_review FunctionDef extracted from each actual helper AST. No module top levels, report assembly, Git/GitHub mutation or fixture file edits. All cases mutate in-memory copies only.','publication_outputs_unchanged':True,'results':results}
path=r/'cmm-round70-review-selection-regression.json';assert not path.exists();path.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'passed':True,'test_count':len(results),'case_count':len(results)//2,'receipt':str(path)}))
