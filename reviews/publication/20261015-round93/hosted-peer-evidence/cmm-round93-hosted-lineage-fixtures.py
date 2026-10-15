from pathlib import Path
import ast,copy,hashlib,json,datetime
P=Path('/private/tmp/cmm-round93-hosted-peer.py');s=P.read_text();tree=ast.parse(s);f=next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='verify_native_lineage');env={'need':lambda ok,msg:None if ok else (_ for _ in ()).throw(AssertionError(msg))};exec(compile(ast.fix_missing_locations(ast.Module(body=[f],type_ignores=[])),str(P),'exec'),env);fn=env['verify_native_lineage'];path='reviews/structured/initial/review.yaml';h='a'*64
prior={'review_id':'initial','findings':[{'finding_id':'F1','status':'open','issue_key':'key','target_ids':['cmmmech:x']}]}
v={'review_id':'final','source':{'inputs':[{'path':path,'sha256':h}]},'findings':[{'finding_id':'F1','status':'resolved','issue_key':'key','target_ids':['cmmmech:x'],'disposition_reason':'checked exact correction','previous_occurrences':[{'review_id':'initial','finding_id':'F1','repository':'CultureBotAI/CMMMech'}]}],'evidence':[]}
rows=[]
for case in ['resolved','rejected','clean','open','deferred','accepted_risk','dismissed','no_reason','no_predecessor','wrong_key','empty_key','wrong_target','wrong_hash','wrong_reference','unretired','evidence_binding']:
 a=copy.deepcopy(v);b=copy.deepcopy(prior);expected=case in ['resolved','rejected','clean','evidence_binding'];selected=[a];changed=[b]
 if case in ['rejected','open','deferred','accepted_risk','dismissed']:a['findings'][0]['status']=case
 if case=='clean':a['findings']=[];changed=[]
 if case=='no_reason':a['findings'][0]['disposition_reason']=''
 if case=='no_predecessor':a['findings'][0]['previous_occurrences']=[]
 if case=='wrong_key':a['findings'][0]['issue_key']='another'
 if case=='empty_key':a['findings'][0]['issue_key']='';b['findings'][0]['issue_key']=''
 if case=='wrong_target':a['findings'][0]['target_ids']=['cmmmech:y']
 if case=='wrong_hash':a['source']['inputs'][0]['sha256']='b'*64
 if case in ['wrong_reference','evidence_binding']:
  a['source']['inputs']=[];a['evidence']=[{'snapshot_sha256':h,'reference':path if case=='evidence_binding' else 'somewhere-else'}]
 if case=='unretired':a['findings']=[]
 try:fn(selected,changed,lambda p:b if p==path else None,lambda p:h);accepted=True
 except (AssertionError,KeyError,TypeError):accepted=False
 assert accepted==expected,(case,expected,accepted)
 rows.append({'case':case,'expected_accept':expected,'actual_accept':accepted,'passed':True})
r={'recorded_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'passed':True,'helper':{'path':str(P),'sha256':hashlib.sha256(P.read_bytes()).hexdigest()},'function_ast_sha256':hashlib.sha256(ast.dump(f,include_attributes=False).encode()).hexdigest(),'fixture_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'cases':rows,'scope':'Actual AST-extracted pure function; no top-level helper/network/publication execution.'};out=Path('/private/tmp/cmm-round93-hosted-lineage-fixtures-final.json');assert not out.exists();out.write_text(json.dumps(r,indent=2)+'\n');print('16/16 actual AST lineage cases passed')
