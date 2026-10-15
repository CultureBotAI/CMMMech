"""Execute only the actual auditor pure AST predicate, never its top-level audit."""
from pathlib import Path
import ast, datetime, hashlib, json
P=Path('/private/tmp')
auditor=P/'cmm-round87-final-package-audit-scoped.py'
module=P/'cmm_round87_peer_checks.py'
source=auditor.read_text()
f=[n for n in ast.parse(source).body if isinstance(n,ast.FunctionDef) and n.name=='native_status_guards_are_current']
assert len(f)==1
ns={'ast':ast};exec(compile(ast.Module(body=f,type_ignores=[]),str(auditor),'exec'),ns)
predicate=ns['native_status_guards_are_current'];actual=module.read_text()
cases=[
 ('actual-valid-rejected-with-unrelated-GitHub-dismissed-text',actual,True),
 ('extra-unrelated-dismissed-string',actual+'\nNOTE="dismissed"\n',True),
 ('invalid-native-dismissed',actual.replace("('resolved','rejected')","('resolved','dismissed')",1),False),
 ('native-accepted-risk',actual.replace("('resolved','rejected')","('resolved','accepted_risk')",1),False),
 ('one-missing-predicate',actual.replace("f['status'] in ('resolved','rejected')","True",1),False),
 ('missing-target-function',actual.replace('def verify_native_lineage(','def other_lineage(',1),False),
 ('wrong-membership-operator',actual.replace("f['status'] in ('resolved','rejected')","f['status'] not in ('resolved','rejected')",1),False),
 ('third-status-accepted',actual.replace("('resolved','rejected')","('resolved','rejected','open')",1),False),
 ('nonliteral-comparator',actual.replace("('resolved','rejected')","('resolved',allowed_status)",1),False),
 ('duplicate-target-definition',actual+'\ndef verify_native_lineage():\n    pass\n',False)
]
results=[]
for name,s,expected in cases:
 result=predicate(s);results.append(dict(name=name,expected=expected,actual=result,passed=result is expected))
assert all(x['passed'] for x in results)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
out={'recorded_at':datetime.datetime.now(datetime.timezone.utc).isoformat().replace('+00:00','Z'),'reviewer':'codex /root/round68_iron_sulfides','passed':True,'cases':results,'count':len(results),'source':{'path':str(auditor),'sha256':sha(auditor)},'module':{'path':str(module),'sha256':sha(module)},'fixture':{'path':str(Path(__file__)),'sha256':sha(Path(__file__))},'scope':'Only native_status_guards_are_current extracted through actual AST and executed. No full auditor, native module top-level, Git/GitHub or package writes.'}
path=P/('cmm-round87-auditor-scope-independent-fixtures-'+datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'.json')
with path.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({'passed':True,'cases':len(results),'receipt':str(path),'sha256':sha(path)}))
