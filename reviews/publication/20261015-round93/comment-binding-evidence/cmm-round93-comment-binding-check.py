from pathlib import Path
from datetime import datetime,timezone
import ast,hashlib,json,tempfile
T=Path('/private/tmp');src=T/'cmm-round93-post-review.py';raw=src.read_bytes();tree=ast.parse(raw);sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();now=lambda:datetime.now(timezone.utc).isoformat();start=now()
initial_nodes=[n for n in tree.body if n.lineno in (7,8)];closing_nodes=[n for n in tree.body if n.lineno==17];assert len(initial_nodes)==3 and len(closing_nodes)==1
assert all(isinstance(n,(ast.Assign,ast.Assert)) for n in initial_nodes+closing_nodes)
initial=compile(ast.fix_missing_locations(ast.Module(body=initial_nodes,type_ignores=[])),str(src),'exec');closing=compile(ast.fix_missing_locations(ast.Module(body=closing_nodes,type_ignores=[])),str(src),'exec');rows=[]
with tempfile.TemporaryDirectory(prefix='cmm-round93-comment-fixture-',dir=T) as d:
 root=Path(d)
 for name in ['valid','wrong_path','wrong_hash','changed_file_after_first_guard','captured_text_mismatch','symlink']:
  bodypath=root/'comment.md';bodypath.unlink(missing_ok=True);bodypath.write_text('accepted exact COMMENT\n');env={'Path':Path,'hashlib':hashlib,'bodypath':bodypath,'body':bodypath.read_text(),'a':{'comment_draft':{'path':str(bodypath),'sha256':sha(bodypath)}}};expected=name=='valid'
  if name=='wrong_path':env['a']['comment_draft']['path']=str(root/'other.md')
  if name=='wrong_hash':env['a']['comment_draft']['sha256']='0'*64
  if name=='symlink':
   other=root/'backing.md';other.write_text(bodypath.read_text());bodypath.unlink();bodypath.symlink_to(other)
  try:
   exec(initial,env)
   if name=='changed_file_after_first_guard':bodypath.write_text('modified COMMENT\n')
   if name=='captured_text_mismatch':env['body']='different initially captured text\n'
   exec(closing,env);accepted=True
  except AssertionError:accepted=False
  assert accepted==expected,(name,accepted,expected)
  rows.append({'case':name,'expected_accept':expected,'actual_accept':accepted,'passed':True})
assert sha(src)==hashlib.sha256(raw).hexdigest()
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ');stem=T/f'cmm-round93-comment-binding-successor-{stamp}';snapshot=stem.with_suffix('.py');snapshot.write_bytes(raw)
initialp=T/'cmm-round93-comment-binding-initial-20261015T103919Z.json';d={'started_at':start,'finished_at':now(),'passed':True,'verdict':'resolved','scientific_review':False,'scope':'Independent bounded static successor plus actual AST-extracted COMMENT guards in isolated temporary fixtures. No top-level helper, Git or GitHub mutation executed.','files':[{'path':str(src),'sha256':sha(src),'snapshot':str(snapshot)}],'previous_occurrences':[{'path':str(initialp),'sha256':sha(initialp),'finding_id':'OP1','issue_key':'CMMMech.round93.post-review-comment-binding'}],'findings':[{'finding_id':'OP1','issue_key':'CMMMech.round93.post-review-comment-binding','severity':'minor','status':'resolved','summary':'Fixed-path/non-symlink and exact SHA guards precede request creation; closing hash and captured-text equality guard verified independently. Actual six focused guards pass.'}],'checks':rows,'fixture_source':{'path':__file__,'sha256':sha(__file__)},'limitations':['Static and extracted-guard verification only. Actual peer receipt and unchanged COMMENT remain runtime prerequisites; no posted review claimed.']};stem.with_suffix('.json').write_text(json.dumps(d,indent=2)+'\n');stem.with_suffix('.md').write_text('# Round93 COMMENT binding successor\n\nOP1 resolved against exact initial occurrence. Actual AST-extracted guards passed six focused cases: accepted bytes pass; wrong path, wrong hash, changed file, captured-text mismatch and symlink fail before posting. No top-level helper/API execution.\n\nCurrent helper SHA256 `'+sha(src)+'`.\n');print(stem.with_suffix('.json'));print(sha(stem.with_suffix('.json')))
