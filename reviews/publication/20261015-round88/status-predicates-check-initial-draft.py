from pathlib import Path
from datetime import datetime,timezone
import ast,hashlib,json
files=[Path('/private/tmp/cmm-round88-build-manifest.py'),Path('/private/tmp/cmm_round88_peer_checks.py')]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
results=[]; predicates=[]
cases=[('empty',[],True),('resolved',['resolved'],True),('rejected',['rejected'],True),('mixed-terminal',['resolved','rejected'],True),('open',['open'],False),('deferred',['deferred'],False),('accepted-risk',['accepted_risk'],False),('invalid-dismissed',['dismissed'],False)]
for p in files:
 tree=ast.parse(p.read_text());scope=tree if 'build-manifest' in p.name else next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='verify_native_lineage')
 selected=[n for n in ast.walk(scope) if isinstance(n,ast.Call) and isinstance(n.func,ast.Name) and n.func.id=='all' and any(isinstance(c,ast.Subscript) and isinstance(c.slice,ast.Constant) and c.slice.value=='status' for c in ast.walk(n))]
 assert len(selected)==(1 if 'build-manifest' in p.name else 2)
 for n in selected:
  text=ast.get_source_segment(p.read_text(),n);predicates.append({'path':str(p),'sha256':sha(p),'line':n.lineno,'expression':text})
  code=compile(ast.Expression(n),str(p),'eval')
  for name,statuses,want in cases:
   fs=[{'status':s} for s in statuses];got=eval(code,{'all':all,'fs':fs,'v':{'findings':fs}});assert got is want,(p,n.lineno,name,got)
   results.append({'helper':p.name,'line':n.lineno,'case':name,'expected_accept':want,'actual_accept':got,'passed':True})
out={'recorded_at':datetime.now(timezone.utc).isoformat(),'passed':True,'case_count':len(results),'scope':'Only actual AST-extracted terminal-status predicates evaluated; no helper top-level, filesystem mutation by helpers, network, or publication execution. The generic full lineage function separately has19 fixtures.','predicates':predicates,'cases':results,'fixture':str(Path(__file__)),'fixture_sha256':sha(Path(__file__))}
f=Path('/private/tmp/cmm-round88-status-predicates-check.json');assert not f.exists();f.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'cases':len(results),'path':str(f),'sha256':sha(f)}))
