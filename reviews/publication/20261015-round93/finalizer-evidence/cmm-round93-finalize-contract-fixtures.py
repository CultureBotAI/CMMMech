from pathlib import Path
import ast,copy,hashlib,json,datetime
P=Path('/private/tmp/cmm-round93-finalize.py');S=P.read_text();tree=ast.parse(S);begin=next(i for i,n in enumerate(tree.body) if isinstance(n,ast.Assert) and (ast.get_source_segment(S,n) or '').startswith("assert hosted['passed']"));end=next(i for i,n in enumerate(tree.body) if (ast.get_source_segment(S,n) or '').startswith("issues=load('issue-ledger')"));code=compile(ast.fix_missing_locations(ast.Module(body=tree.body[begin:end],type_ignores=[])),str(P),'exec')
T=Path('/private/tmp/cmm-round93-finalize-fixture-inputs');T.mkdir(exist_ok=True);sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();c={'base':'b'*40,'head':'a'*40,'tree':'c'*40,'branch':'curate/fixture'};n=330;merge='d'*40;pre={'log_sha256':'loghash','log':str(T/'pre.log')};(T/'pre.log').write_text('actual fixture log\n');pre['log_sha256']=sha(T/'pre.log');peerpath=T/'peer.json';body=T/'body.md';body.write_text('Exact COMMENT\n');draft={'path':str(body),'sha256':sha(body)};peer=dict(c,passed=True,pr=n,comment_draft=draft);peerpath.write_text(json.dumps(peer));posted={'peer_sha256':sha(peerpath),'body_sha256':sha(body),'review':{'body':body.read_text(),'commit_id':c['head'],'state':'COMMENTED','id':12,'html_url':f'https://github.com/CultureBotAI/CMMMech/pull/{n}#pullrequestreview-12'}}
for label,value in [('commit-receipt',c),('helper-config',{'base':c['base']}),('preflight-committed-terminal',pre)]: (T/f'cmm-round93-{label}.json').write_text(json.dumps(value))
queue={'exit_code':0,'topic':c,'pr':{'number':n},'live_main':c['base'],'preflight_sha256':sha(T/'cmm-round93-preflight-committed-terminal.json'),'preflight_log_sha256':pre['log_sha256'],'review_body_sha256':sha(body),'hosted_review_ids':[12]};(T/'cmm-round93-queue-receipt.json').write_text(json.dumps(queue))
roles={'required_pr':('pull_request',c['head'],'validate-strict.yaml','validate-strict'),'merge_group':('merge_group',merge,'validate-strict.yaml','validate-strict'),'main_validation':('push',merge,'validate-strict.yaml','validate-strict'),'main_integrity':('push',merge,'verify-merge-integrity.yaml','merge-integrity'),'pages_deployment':('push',merge,'pages.yaml','deploy')}
H=dict(c,passed=True,all_five_hosted_runs_and_jobs_succeeded=True,pr=n,merge=merge,findings=[],pending=[],runs={},selected_run_ids={},responses={},inputs={})
for k,path in {'commit':T/'cmm-round93-commit-receipt.json','queue':T/'cmm-round93-queue-receipt.json','config':T/'cmm-round93-helper-config.json','peer':peerpath,'preflight':T/'cmm-round93-preflight-committed-terminal.json','posted_review_body':body,'preflight_log':Path(pre['log'])}.items():H['inputs'][k]={'path':str(path),'sha256':sha(path),'bytes':path.stat().st_size}
for idx,(role,(event,head,wf,jobname)) in enumerate(roles.items(),1):
 branch=c['branch'] if role=='required_pr' else 'gh-readonly-queue/main/fixture' if role=='merge_group' else 'main'
 raw={'id':idx,'head_sha':head,'event':event,'path':'.github/workflows/'+wf,'status':'completed','conclusion':'success','run_attempt':2,'repository':{'full_name':'CultureBotAI/CMMMech'},'head_branch':branch}
 job={'id':100+idx,'run_id':idx,'head_sha':head,'run_attempt':2,'name':jobname,'status':'completed','conclusion':'success','html_url':'https://github.com/CultureBotAI/CMMMech/actions/runs/'+str(idx)+'/job/'+str(100+idx)}
 H['runs'][role]={**raw,'jobs':[copy.deepcopy(job)]};H['selected_run_ids'][role]=idx
 H['responses'][role+'_actual']={'exit_code':0,'data':copy.deepcopy(raw)};H['responses'][role+'_closing']={'exit_code':0,'data':copy.deepcopy(raw)}
 H['responses'][role+'_jobs']={'exit_code':0,'command':['gh','api','--method','GET',f'repos/CultureBotAI/CMMMech/actions/runs/{idx}/attempts/2/jobs?per_page=100','--paginate','--slurp'],'data':[{'total_count':1,'jobs':[copy.deepcopy(job)]}]}
BASE={'Path':Path,'T':T,'sha':sha,'c':c,'n':n,'merge':merge,'pre':pre,'peer':peer,'peerpath':peerpath,'posted':posted,'hosted':H}
def rawjob(e):return e['hosted']['responses']['required_pr_jobs']['data'][0]['jobs'][0]
def sumjob(e):return e['hosted']['runs']['required_pr']['jobs'][0]
def bothjobs(e,key,val):rawjob(e)[key]=val;sumjob(e)[key]=val
cases=[]
def check(label,mut,expected):
 env=copy.deepcopy(BASE);env['load']=lambda name:copy.deepcopy(queue)
 mut(env)
 try:exec(code,env);observed='accepted'
 except (AssertionError,KeyError,ValueError,TypeError,IndexError):observed='rejected'
 cases.append({'case':label,'expected':expected,'observed':observed,'passed':observed==expected})
check('valid exact producer-shaped evidence',lambda e:None,'accepted')
def omit(e):rawjob(e).pop('run_attempt');sumjob(e)['run_attempt']=None
check('omitted raw job attempt with exact pinned endpoint',omit,'accepted')
check('wrong peer PR',lambda e:e['peer'].update(pr=999),'rejected')
check('wrong logical role',lambda e:e['hosted']['runs'].update(unrelated=e['hosted']['runs'].pop('required_pr')),'rejected')
check('changed peer input hash',lambda e:e['hosted']['inputs']['peer'].update(sha256='wrong'),'rejected')
check('wrong input byte count',lambda e:e['hosted']['inputs']['config'].update(bytes=999),'rejected')
check('duplicate selected run',lambda e:e['hosted']['selected_run_ids'].update(main_validation=1),'rejected')
check('wrong run head',lambda e:e['hosted']['runs']['required_pr'].update(head_sha='f'*40),'rejected')
check('changed closing attempt',lambda e:e['hosted']['responses']['required_pr_closing']['data'].update(run_attempt=3),'rejected')
check('job belongs to another head',lambda e:bothjobs(e,'head_sha','f'*40),'rejected')
check('job belongs to another run',lambda e:bothjobs(e,'run_id',999),'rejected')
check('required job absent',lambda e:bothjobs(e,'name','other'),'rejected')
check('raw summary mismatch',lambda e:sumjob(e).update(id=999),'rejected')
check('raw job explicit null attempt',lambda e:bothjobs(e,'run_attempt',None),'rejected')
def wrongendpoint(e):omit(e);e['hosted']['responses']['required_pr_jobs']['command'][4]=e['hosted']['responses']['required_pr_jobs']['command'][4].replace('/attempts/2/','/attempts/1/')
check('omitted job attempt with wrong pinned endpoint',wrongendpoint,'rejected')
check('truncated job response',lambda e:e['hosted']['responses']['required_pr_jobs']['data'][0].update(total_count=2),'rejected')
check('different posted body',lambda e:e['posted']['review'].update(body='other'),'rejected')
check('different posted PR URL',lambda e:e['posted']['review'].update(html_url='https://github.com/CultureBotAI/CMMMech/pull/999#review'),'rejected')
check('different role event',lambda e:e['hosted']['runs']['required_pr'].update(event='push'),'rejected')
out={'at':datetime.datetime.now(datetime.timezone.utc).isoformat().replace('+00:00','Z'),'helper':{'path':str(P),'sha256':sha(P)},'fixture_sha256':sha(__file__),'scope':'Only actual AST-extracted corrected binding block executed with synthetic receipts under a dedicated fixture directory. No full helper, durable report, Git/GitHub or network execution.','cases':cases,'passed':all(x['passed'] for x in cases)}
Path('/private/tmp/cmm-round93-finalize-contract-fixtures.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':out['passed'],'cases':len(cases),'failures':[x for x in cases if not x['passed']]}));raise SystemExit(0 if out['passed'] else 1)
