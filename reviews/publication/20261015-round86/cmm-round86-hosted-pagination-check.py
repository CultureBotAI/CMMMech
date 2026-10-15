from pathlib import Path
import ast,hashlib,json,copy,datetime,re
p=Path('/private/tmp');outputs=[]
class Rejected(Exception):pass
def need(v,m):
 if not v:raise Rejected(m)
expected=[{'path':f'path/{i}.yaml'} for i in range(151)]
lookup=lambda n:hashlib.sha1(n.encode()).hexdigest()
base=[[{'filename':x['path'],'sha':lookup(x['path']),'status':'added'} for x in expected[:100]],[{'filename':x['path'],'sha':lookup(x['path']),'status':'modified'} for x in expected[100:]]]
cases=[]
cases.append(('valid151-two-pages',copy.deepcopy(base),True))
cases.append(('first100-only',copy.deepcopy(base[:1]),False))
x=copy.deepcopy(base);x[1].pop();cases.append(('missing-last-file',x,False))
x=copy.deepcopy(base);x[1][0]=copy.deepcopy(x[0][0]);cases.append(('duplicate-cross-page',x,False))
x=copy.deepcopy(base);x[1][0]['sha']='0'*40;cases.append(('wrong-hosted-blob',x,False))
x=copy.deepcopy(base);x[0][0]['status']='renamed';cases.append(('unexpected-rename',x,False))
x=copy.deepcopy(base);x[1][0]['filename']='extra';cases.append(('same-count-wrong-path-set',x,False))
cases.append(('empty-pages',[],False))
x=copy.deepcopy(base);x.insert(1,[]);cases.append(('empty-intermediate-page',x,False))
x=[copy.deepcopy(base[0][:99]),copy.deepcopy(base[0][99:])+copy.deepcopy(base[1])];cases.append(('nonfull-intermediate-page',x,False))
for fn,name in [('cmm-round86-hosted-peer.py','validate_file_pages'),('cmm-round86-hosted-audit-paginated.py','validate_paginated_files')]:
 path=p/fn;tree=ast.parse(path.read_text());node=next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name==name)
 env={'need':need,'require':need,'valid_sha':lambda x:isinstance(x,str) and re.fullmatch('[0-9a-f]{40}',x) is not None}
 exec(compile(ast.Module(body=[node],type_ignores=[]),str(path),'exec'),env)
 for label,pages,pass_expected in cases:
  try:
   if name=='validate_file_pages':env[name](pages,{x['path']:x for x in expected},lookup,151)
   else:env[name](pages,expected,lookup)
   actual=True
  except Exception:actual=False
  assert actual==pass_expected,(fn,label,actual)
  outputs.append({'helper':fn,'helper_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'case':label,'expected_accept':pass_expected,'actual_accept':actual,'passed':True})
r={'recorded_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'passed':True,'case_count':len(outputs),'scope':'Nonmutating fixtures extracted only the two actual pagination functions by AST; no helper top-level, Git, network or publication operation was executed. Rejects missing second page, duplicate paths, incorrect blobs/status, incomplete pages and same-count wrong paths.','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'cases':outputs}
out=p/'cmm-round86-hosted-pagination-check.json';assert not out.exists();out.write_text(json.dumps(r,indent=2)+'\n');print(out, len(outputs),'PASS')
