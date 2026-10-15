from pathlib import Path
from datetime import datetime, timezone
import ast, copy, hashlib, json, re, yaml

P=Path('/private/tmp/cmm-round93-hosted-peer.py')
W=Path('/private/tmp/CMMMech-expansion-round93-20261015')
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
tree=ast.parse(P.read_text())
loop=next(n for n in ast.walk(tree) if isinstance(n,ast.For) and isinstance(n.target,ast.Name) and n.target.id=='e' and ast.unparse(n.iter)=="v['evidence']")
code=compile(ast.fix_missing_locations(ast.Module(body=[loop],type_ignores=[])),str(P),'exec')
reviewpath=W/'reviews/structured/20261015T104328Z-pig-manure-round93-independent/review.yaml'
v=yaml.safe_load(reviewpath.read_text())
def check(v):
    env={'v':v,'primary':[],'Path':Path,'re':re,'sha':sha,'binding':lambda p:{'path':str(p),'sha256':sha(p)},'need':lambda ok,msg:None if ok else (_ for _ in ()).throw(AssertionError(msg))}
    exec(code,env)
    return env['primary']
actual=check(v)
assert len(actual)==9
source=Path(actual[0]['path']);h=sha(source)
rows=[{'case':'all_nine_actual_pig_manure_primaries','accepted':True,'expected':True,'passed':True}]
empty=Path('/private/tmp/cmm-round93-hosted-empty-locator-fixture')
assert not empty.exists();empty.write_bytes(b'')
for name,loc,hashvalue,expected in [
    ('actual_colon','Actual local artifact: '+str(source),h,True),
    ('artifact_colon','Artifact: '+str(source),h,True),
    ('lower_no_colon','Original text; local artifact '+str(source),h,True),
    ('wrong_hash','Artifact: '+str(source),'0'*64,False),
    ('missing_file','Artifact: /private/tmp/cmm-round93-no-such-source-fixture',h,False),
    ('relative_path','Artifact: wei2018.xml',h,False),
    ('empty_file','Artifact: '+str(empty),sha(empty),False),
    ('no_locator','Original text only',h,False),
]:
    case={'review_id':'fixture','evidence':[{'kind':'primary_source','evidence_id':'E1','locator':loc,'snapshot_sha256':hashvalue}]}
    try:check(case);accepted=True
    except AssertionError:accepted=False
    assert accepted==expected,(name,accepted,expected)
    rows.append({'case':name,'accepted':accepted,'expected':expected,'passed':True})
result={'recorded_at':datetime.now(timezone.utc).isoformat(),'passed':True,'scope':'Executed only the actual AST-extracted primary binding loop; no top-level helper or API execution. Nine immutable actual primary artifacts plus eight positive/negative locator and hash cases.','helper':{'path':str(P),'sha256':sha(P)},'loop_ast_sha256':hashlib.sha256(ast.dump(loop,include_attributes=False).encode()).hexdigest(),'actual_review':{'path':str(reviewpath),'sha256':sha(reviewpath)},'actual_primary_bindings':actual,'cases':rows,'source':{'path':str(Path(__file__)),'sha256':sha(__file__)}}
out=Path('/private/tmp/cmm-round93-hosted-locator-check.json');assert not out.exists();out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'path':str(out),'sha256':sha(out),'passed':True,'actual_primaries':len(actual),'cases':len(rows)},indent=2))
