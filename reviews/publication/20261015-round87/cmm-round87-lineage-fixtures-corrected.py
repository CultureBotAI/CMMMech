from pathlib import Path
import ast,copy,hashlib,json,re,tempfile,datetime,yaml
p=Path('/private/tmp/cmm_round87_peer_checks.py')
tree=ast.parse(p.read_text());fun=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='verify_native_lineage')
ns={'yaml':yaml,'re':re,'SLUGS':{'alabandite','secondary-aluminium-dross','simonkolleite'}}
exec(compile(ast.Module(body=[fun],type_ignores=[]),str(p),'exec'),ns)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def need(x,msg):
 if not x:raise AssertionError(msg)
tid='cmmmech:secondary-aluminium-dross'
def f(status='open',refs=None,key='key1'):
 return {'finding_id':'F1','issue_key':key,'status':status,'previous_occurrences':refs or [],'external_issues':[]}
def rv(rid,fs):return {'review_id':rid,'scope':{'reviewed_target_ids':[tid]},'findings':fs,'source':{'inputs':[]}}
def ref(rid):return {'repository':'CultureBotAI/CMMMech','review_id':rid,'finding_id':'F1'}
results=[]
def case(name,mode,accept):
 with tempfile.TemporaryDirectory(prefix='cmm-round87-lineage-fixture-',dir='/private/tmp') as td:
  w=Path(td);old=rv('initial',[f()]);final=rv('final',[f('resolved',[ref('initial')])]);items={'initial':old,'final':final}
  if mode=='clean':items={'final':rv('final',[])}
  elif mode=='multi':items['intermediate']=rv('intermediate',[f('resolved',[ref('initial')])]);final['findings'][0]['previous_occurrences']=[ref('intermediate')]
  elif mode=='omitted':final['findings']=[]
  elif mode=='open':final['findings'][0]['status']='open'
  elif mode=='rejected':final['findings'][0]['status']='rejected'
  elif mode=='dismissed':final['findings'][0]['status']='dismissed'
  elif mode=='acceptedrisk':final['findings'][0]['status']='accepted_risk'
  elif mode=='wrongkey':final['findings'][0]['issue_key']='other'
  elif mode=='wrongid':final['findings'][0]['previous_occurrences'][0]['finding_id']='F2'
  elif mode=='wrongrepo':final['findings'][0]['previous_occurrences'][0]['repository']='other/repo'
  elif mode=='wrongtarget':old['scope']['reviewed_target_ids']=['cmmmech:alabandite']
  elif mode=='cycle':old['findings'][0]['previous_occurrences']=[ref('final')]
  elif mode=='missingprior':final['findings'][0]['previous_occurrences'][0]['review_id']='missing'
  elif mode=='duplicatekey':final['findings'].append(copy.deepcopy(final['findings'][0]))
  paths={rid:'reviews/structured/'+rid+'/review.yaml' for rid in items}
  def write(rid):
   target=w/paths[rid];target.parent.mkdir(parents=True,exist_ok=True);target.write_text(yaml.safe_dump(items[rid]));target.with_suffix('.md').write_text('Immutable fixture counterpart\n')
  for rid in items:write(rid)
  # Normal chains are serialized bottom-up. Cycle fixture is intentionally not a valid hash fixed-point.
  for rid in ('initial','intermediate','final'):
   if rid not in items:continue
   for finding in items[rid]['findings']:
    for previous in finding['previous_occurrences']:
     pr=previous['review_id']
     if pr in paths:items[rid]['source']['inputs'].append({'path':paths[pr],'sha256':sha(w/paths[pr])})
   write(rid)
  if mode=='wronghash':items['final']['source']['inputs'][0]['sha256']='0'*64;write('final')
  if mode=='nohash':items['final']['source']['inputs']=[];write('final')
  if mode=='nomd':(w/paths['initial']).with_suffix('.md').unlink()
  expected={name:{} for name in paths.values()}
  if mode=='uncommittedfinal':expected.pop(paths['final'])
  try:
   value=ns['verify_native_lineage'](w,{'secondary-aluminium-dross':(w/paths['final'],items['final'])},expected,need,sha)
   success=True;detail={'resolved_occurrences':len(value)}
  except (AssertionError,KeyError) as e:success=False;detail={'rejection':str(e)}
  need(success==accept,name+' unexpected outcome '+str(detail));results.append({'name':name,'expected_accept':accept,'passed':True,**detail})
for name,mode,accept in [('clean_current_manifest','clean',True),('exact_resolution','ok',True),('transitive_resolution','multi',True),('missing_disposition','omitted',False),('unresolved_final','open',False),('schema_valid_rejected','rejected',True),('invalid_dismissed','dismissed',False),('accepted_risk_requires_explicit_policy','acceptedrisk',False),('changed_stable_key','wrongkey',False),('changed_occurrence_id','wrongid',False),('foreign_repository','wrongrepo',False),('changed_target','wrongtarget',False),('cyclic_or_unbound_chain','cycle',False),('missing_predecessor','missingprior',False),('duplicate_issue_key','duplicatekey',False),('wrong_predecessor_hash','wronghash',False),('missing_predecessor_hash','nohash',False),('missing_markdown','nomd',False),('selected_final_outside_commit','uncommittedfinal',False)]:case(name,mode,accept)
out={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'passed':True,'cases':results,'case_count':len(results),'source':str(p),'source_sha256':sha(p),'fixture_source':__file__,'fixture_sha256':sha(__file__),'scope':'Actual verify_native_lineage AST extracted without top-level helper execution; temporary synthetic files only. Does not exercise hosted APIs or imply publication acceptance.'}
q=Path('/private/tmp/cmm-round87-lineage-fixtures-corrected.json');q.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'cases':len(results),'receipt':str(q),'sha256':sha(q)}))
