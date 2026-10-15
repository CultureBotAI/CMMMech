"""Independent read-only round95 PR operational audit; external evidence only."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json,os,re,subprocess,sys,uuid,yaml
T=Path('/private/tmp');W=T/'CMMMech-expansion-round95-20261015';repo='CultureBotAI/CMMMech'
parser=argparse.ArgumentParser();parser.add_argument('--pr',required=True,type=int);parser.add_argument('--head',required=True);parser.add_argument('--tree',required=True);args=parser.parse_args();N=args.pr
TRUSTED_BASE='73d4b1c42541ee7ca139effae00b94ddb1c8a631'
EXPECTED_SLUGS={'hauerite', 'alunite', 'heterosite', 'erythrite', 'melanterite', 'annabergite', 'spent-steel-pickling-liquors'}
EXPECTED_COUNTS={'record_count': 459, 'history_count': 525, 'structured_review_count': 542, 'review_base_count': 96, 'covered_records': 459}
now=lambda:datetime.now(timezone.utc).isoformat().replace('+00:00','Z');sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();digest=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
start=now();stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid.uuid4().hex[:6];out=T/f'cmm-round95-hosted-audit-{stamp}.json';result={'started_at':start,'pr':N,'passed':False,'findings':[],'pending':[]};calls=[]
def need(condition,message):
 if not condition:raise AssertionError(message)
def run(cmd):
 p=subprocess.run(cmd,cwd=W,env=dict(os.environ,GIT_OPTIONAL_LOCKS='0'),capture_output=True,text=True)
 if p.returncode:raise RuntimeError(repr(cmd)+': '+p.stderr.strip())
 return p.stdout.strip()
def git(*args):return run(['git',*args])
def gh(*args):
 raw=run(['gh',*args]);d=json.loads(raw);calls.append({'command':['gh',*args],'observed_at':now(),'response_sha256':hashlib.sha256(raw.encode()).hexdigest()});return d
def api(path):return gh('api',path)
def pages(path,key=None):
 ps=gh('api',path+('&' if '?' in path else '?')+'per_page=100','--paginate','--slurp');need(isinstance(ps,list),'Pagination outer shape')
 if key:
  need(ps and all(isinstance(p,dict) and isinstance(p.get(key),list) for p in ps),'Pagination keyed shape');rows=[r for p in ps for r in p[key]];need(len(rows)==ps[0]['total_count'] and all(p['total_count']==ps[0]['total_count'] for p in ps),'Pagination incomplete total')
 else:need(all(isinstance(p,list) for p in ps),'Pagination array shape');rows=[r for p in ps for r in p]
 return ps,rows
def load(p):return json.loads(Path(p).read_text())
def y(p):return yaml.load(Path(p).read_text(),Loader=yaml.CSafeLoader)
def binding(p):return {'path':str(p),'sha256':sha(p)}
def check_log_receipt(p):
 d=load(p);need(d['exit_code']==0 and sha(d['log'])==d['log_sha256'],'Failed/unbound gate '+str(p));return d
def verify_native_lineage(selected, changed_reviews, reader, hash_reader):
 """Require schema-valid terminal findings and exact hashed predecessor retirement."""
 retired=set();dispositions=[]
 for v in selected:
  for f in v.get('findings',[]):
   need(f['status'] in ('resolved','rejected'),'Selected finding is not terminal resolved/rejected')
   need(f.get('issue_key'),'Selected terminal finding lacks stable key')
   need(f.get('disposition_reason') and f.get('previous_occurrences'),'Terminal finding lacks explicit predecessor/reason')
   for prev in f['previous_occurrences']:
    need(prev.get('repository','CultureBotAI/CMMMech')=='CultureBotAI/CMMMech','Foreign predecessor requires separate assessment')
    path='reviews/structured/'+prev['review_id']+'/review.yaml';prior=reader(path)
    need(prior['review_id']==prev['review_id'],'Prior review identity mismatch')
    pf=next((x for x in prior.get('findings',[]) if x['finding_id']==prev['finding_id']),None)
    need(pf is not None and pf.get('issue_key')==f.get('issue_key') and bool(set(pf.get('target_ids',[])) & set(f.get('target_ids',[]))),'Prior finding identity/key/target mismatch')
    h=hash_reader(path)
    bound=any(i['path']==path and i['sha256']==h for i in v['source']['inputs']) or any(e.get('snapshot_sha256')==h and (e.get('reference') in (path,prev['review_id']) or path in e.get('locator','')) for e in v.get('evidence',[]))
    need(bound,'Predecessor artifact is not exact-hash bound')
    retired.add((prev['review_id'],prev['finding_id']));dispositions.append({'review_id':v['review_id'],'finding_id':f['finding_id'],'status':f['status'],'previous_review':prev['review_id'],'previous_finding':prev['finding_id'],'previous_sha256':h,'issue_key':f['issue_key']})
 for v in changed_reviews:
  for f in v.get('findings',[]):
   if f['status'] in ('open','deferred','accepted_risk'):
    need((v['review_id'],f['finding_id']) in retired,'Current-package predecessor has no selected explicit terminal disposition')
 return dispositions

def conversation_inventory():
 _,reviews=pages(f'repos/{repo}/pulls/{N}/reviews');_,comments=pages(f'repos/{repo}/issues/{N}/comments');_,inline=pages(f'repos/{repo}/pulls/{N}/comments');threads=[];cursor=None
 while True:
  q='query($cursor:String){repository(owner:"CultureBotAI",name:"CMMMech"){pullRequest(number:PR_NUMBER){reviewThreads(first:100,after:$cursor){nodes{id isResolved isOutdated path comments(first:100){nodes{id body author{login} createdAt url} pageInfo{hasNextPage endCursor}}} pageInfo{hasNextPage endCursor}}}}}'
  q=q.replace('PR_NUMBER',str(N));cmd=['api','graphql','-f','query='+q]+(['-f','cursor='+cursor] if cursor else []);g=gh(*cmd);need(not g.get('errors'),'GraphQL errors');block=g['data']['repository']['pullRequest']['reviewThreads'];threads+=block['nodes'];need(all(not x['comments']['pageInfo']['hasNextPage'] for x in block['nodes']),'Additional nested thread comments need manual pagination')
  if not block['pageInfo']['hasNextPage']:break
  nxt=block['pageInfo']['endCursor'];need(nxt and nxt!=cursor,'Repeated thread cursor');cursor=nxt
 need(len(threads)==len({x['id'] for x in threads}),'Duplicate thread nodes');conv={'reviews':reviews,'issue_comments':comments,'inline_comments':inline,'review_threads':threads}
 return conv

try:
 c=load(T/'cmm-round95-commit-receipt.json');cfg=load(T/'cmm-round95-helper-config.json');published=load(T/'cmm-round95-publish-receipt.json')
 need(c['head']==args.head and c['tree']==args.tree and c['base']==TRUSTED_BASE,'Handoff identity changed');need(published['pr']['number']==N and published['head']==c['head'] and published['tree']==c['tree'] and published['base']==c['base'],'Publication receipt differs');need(cfg['counts']==EXPECTED_COUNTS and set(cfg['slugs'])==EXPECTED_SLUGS,'Unexpected final cohort/counts');selectionp=T/'cmm-round95-hosted-scientific-selection.json';selection=load(selectionp);need(selection['base']==c['base'] and set(selection['reviews'])==EXPECTED_SLUGS,'Independent selection differs');input_bindings=[binding(p) for p in [T/'cmm-round95-commit-receipt.json',T/'cmm-round95-helper-config.json',T/'cmm-round95-publish-receipt.json',selectionp]]
 result.update({k:c[k] for k in ['head','tree','base','branch']});need(cfg['base']==c['base'] and cfg['branch']==c['branch'],'Config identity differs')
 need(git('rev-parse','HEAD')==c['head'] and git('rev-parse','HEAD^{tree}')==c['tree'] and not git('status','--porcelain=v1','--untracked-files=all'),'Source worktree/head/tree not clean reviewed state');need(git('rev-list','--parents','-n','1','HEAD').split()==[c['head'],c['base']],'Topic sole parent mismatch')
 paths=git('diff','--name-only',c['base'],c['head']).splitlines();need(len(paths)>0 and len(paths)==len(set(paths))==len(c['files']) and set(paths)==set(c['files']),'Local complete changed set differs')
 need(not any(p.startswith(('src/','schema/','scripts/','tests/','.github/','conf/','.claude/','.codex/')) for p in paths),'Unreviewed code/governance scope added')
 files=[{'path':p,'sha256':sha(W/p),'git_blob':git('rev-parse',c['head']+':'+p)} for p in paths];result['committed_inputs']=files
 reportp=W/'research/ingests/round95-frontier-20261015.json';report=load(reportp);need(report['base']==c['base'] and report['branch']==c['branch'] and report['counts']==cfg['counts'],'Report identity/counts mismatch');need({r['slug'] for r in report['records']}==set(cfg['slugs']) and len(report['records'])==7,'Wrong report owner set')
 selected=[];primary=[]
 expected_ids={slug:row['review_id'] for slug,row in selection['reviews'].items()}
 for r in report['records']:
  rp=W/r['path'];vpath=W/r['review']['path'];v=y(vpath);record=y(rp);need(sha(rp)==r['sha256'] and record['id']==r['id'] and record['history_refs']==r['history_refs'],'Owner/report/history refs mismatch '+r['slug']);need(v['review_id']==expected_ids[r['slug']]==r['review']['review_id'] and sha(vpath)==r['review']['review_sha256']==selection['reviews'][r['slug']]['sha256'] and r['review']['path']==selection['reviews'][r['slug']]['path'],'Wrong final scientific review '+r['slug'])
  need(v['completion']=='completed' and v['scientific_review'] is True and v['verdict'] in ['pass','pass_with_limitations'] and v['reviewer']['independence']=='independent','Scientific acceptance invalid')
  need(r['id'] in v['scope']['reviewed_target_ids'] and any(t['target_id']==r['id'] and t['path']==r['path'] for t in v['targets']) and any(i['path']==r['path'] and i['sha256']==r['sha256'] for i in v['source']['inputs']),'Owner target/hash/scope mismatch')
  need(v['source']['git_revision']==c['base'] and v['source']['state']=='working_tree','Review base/state mismatch')
  for i in v['source']['inputs']:need(sha(W/i['path'])==i['sha256'],'Selected review input changed '+i['path'])
  for h in r['history_refs']:need(any(i['path']==h and i['sha256']==sha(W/h) for i in v['source']['inputs']),'Canonical history input unbound')
  need(record['curation_history'] and record['curation_history'][0]['action']=='CREATE' and all(e['action']=='EDIT' for e in record['curation_history'][1:]),'Unexpected owner history action sequence')
  if r['slug']=='spent-steel-pickling-liquors':need(v['reviewer']['identity']=='codex /root','Own authored owner lacks separate reviewer')
  need(any(e['kind']=='primary_source' and e['support']=='supports' for e in v['evidence']),'No supporting primary evidence selected')
  for e in v['evidence']:
   if e['kind']!='primary_source':continue
   loc=e.get('locator','');m=re.search(r'(?:(?:Actual local artifact|Artifact):\s*|local artifact\s+)(/private/tmp/.*)$',loc,re.I);need(m is not None,'No exact raw primary locator '+e['evidence_id']);p=Path(m.group(1).strip());need(p.is_file() and p.stat().st_size>0 and sha(p)==e['snapshot_sha256'],'Primary source binding fails '+str(p));primary.append({'review_id':v['review_id'],'evidence_id':e['evidence_id'],**binding(p),'bytes':p.stat().st_size})
  selected.append({'slug':r['slug'],'id':r['id'],'owner':binding(rp),'history':[binding(W/h) for h in r['history_refs']],'review':binding(vpath),'markdown':binding(vpath.with_suffix('.md')),'review_id':v['review_id'],'reviewer':v['reviewer'],'verdict':v['verdict']})
 result['native_finding_dispositions']=verify_native_lineage([y(x['review']['path']) for x in selected],[y(W/p) for p in paths if p.startswith('reviews/structured/') and p.endswith('/review.yaml')],lambda p:y(W/p),lambda p:sha(W/p))
 result.update(selected_scientific_reviews=selected,primary_evidence_bindings=primary,report=binding(reportp),authorship='Authored spent-steel-pickling-liquors; its independent root-agent scientific review is relied upon. Independently reviewed hauerite and melanterite. This is operational package/hosted verification, not fresh scientific self-acceptance.')
 gates=check_log_receipt(T/'cmm-round95-final-gates.json');need(gates['base']==c['base'] and gates['inputs_unchanged'] and all(x['exit_code']==0 for x in gates['commands']),'Final gate mismatch');need(len(gates['record_inputs'])==cfg['counts']['record_count'] and all(sha(W/p)==h for p,h in gates['record_inputs'].items()),'Final gate owner hash set mismatch')
 requirements=[['just','check'],['uv','run','--locked','cmmmech','validate','--require-records'],['uv','run','--locked','cmmmech','validate-history','--base',c['base']],['uv','run','--locked','python','scripts/render_pages.py','--check']];need([x['command'] for x in gates['commands']]==requirements,'Missing final batch command');need('317 passed, 3 skipped' in Path(gates['log']).read_text(),'Actual full-suite summary absent')
 checker=check_log_receipt(T/'cmm-round95-review-check-final.json');need(checker['command']==['just','review-check','--base',c['base'],'--require-reviews'],'Canonical check command mismatch');need(str(cfg['counts']['structured_review_count']) in Path(checker['log']).read_text(),'Native count not in log')
 coverage=load(T/'cmm-round95-local-coverage.json');need(coverage['passed'] and all(coverage[k]==v for k,v in cfg['counts'].items()),'Coverage counts mismatch');need(len(coverage['records'])==cfg['counts']['record_count'] and len({r['path'] for r in coverage['records']})==cfg['counts']['record_count'] and all(sha(W/r['path'])==r['sha256'] and r['matching_scientific_reviews'] for r in coverage['records']),'Coverage owner hash set mismatch')
 for row in coverage['records']:
  for rv in row['matching_scientific_reviews']:need(sha(W/rv['path'])==rv['review_sha256'],'Covered review changed')
 need(len(coverage['bases'])==cfg['counts']['review_base_count'] and all(x['available_commit'] and git('cat-file','-t',x['revision'])=='commit' for x in coverage['bases']),'Review base unavailable')
 for name in ['final-gates.json','final-gates.log','review-check-final.json','review-check-final.log','local-coverage.json']:
  need(sha(T/('cmm-round95-'+name))==sha(W/'research/ingests/round95-checks-20261015'/name),'Retained gate bytes differ '+name)
 result['local_checks']={n:binding(T/('cmm-round95-'+n+'.json')) for n in ['final-gates','review-check-final','local-coverage']};result['counts']=cfg['counts'];result['gate_boundary']='Actual completed local batch, native checker and current exact-hash coverage are independently bound here. No future queue, merge or fresh-main success is inferred.'
 pr=api(f'repos/{repo}/pulls/{N}');need(pr['state']=='open' and not pr['draft'] and pr['head']['sha']==c['head'] and pr['head']['ref']==c['branch'] and pr['base']['sha']==c['base'] and pr['base']['ref']=='main','Live PR identity mismatch');need(pr['head']['repo']['full_name']==repo and pr['base']['repo']['full_name']==repo,'Repository mismatch')
 body=T/'cmm-round95-pr-body.md';need(pr['title']==cfg['title'] and pr['body']==body.read_text() and sha(body)==published['body_sha256'],'Live title/body differs');result['prepared_body']=binding(body);result['pr_snapshot']=pr
 fp,fs=pages(f'repos/{repo}/pulls/{N}/files');need(len(fs)==len({x['filename'] for x in fs})==pr['changed_files']==len(paths) and {x['filename'] for x in fs}==set(paths),'Incomplete or duplicate hosted file set');lookup={x['path']:x for x in files}
 for f in fs:need(f['status'] in ['added','modified'] and f['sha']==lookup[f['filename']]['git_blob'],'Hosted blob differs '+f['filename'])
 result['file_pages']=fp
 _,commits=pages(f'repos/{repo}/pulls/{N}/commits');need(len(commits)==pr['commits']==1 and commits[0]['sha']==c['head'] and [p['sha'] for p in commits[0]['parents']]==[c['base']],'Hosted commit parent mismatch');gc=api(f'repos/{repo}/git/commits/{c["head"]}');need(gc['tree']['sha']==c['tree'],'Hosted tree differs');result['hosted_git_commit']=gc
 conv=conversation_inventory();result['conversation']=conv;result['conversation_sha256']=digest(conv)
 if any(conv.values()):result['pending'].append('Nonempty conversation requires independent digest-bound disposition before final acceptance')
 cp,checks=pages(f'repos/{repo}/commits/{c["head"]}/check-runs',key='check_runs');need(len(checks)==len({x['id'] for x in checks}),'Duplicate checks');matches=[x for x in checks if x['name']=='validate-strict' and x['head_sha']==c['head'] and x['app']['id']==15368];need(matches,'Required GitHub Actions check missing');strict=max(matches,key=lambda x:x['id']);m=re.search(r'/actions/runs/(\d+)(?:/job/(\d+))?',strict['details_url']);need(m,'No check/run locator');rid=int(m.group(1));wr=api(f'repos/{repo}/actions/runs/{rid}');need(wr['head_sha']==c['head'] and wr['event']=='pull_request' and wr['path']=='.github/workflows/validate-strict.yaml' and wr['head_branch']==c['branch'] and wr['repository']['full_name']==repo,'CI workflow/head/event differs');attempt=wr['run_attempt'];jp,jobs=pages(f'repos/{repo}/actions/runs/{rid}/attempts/{attempt}/jobs',key='jobs');need(jobs and len(jobs)==len({j['id'] for j in jobs}) and all(j['run_id']==rid and j.get('run_attempt') in (None,attempt) and j['head_sha']==c['head'] for j in jobs),'Current-attempt jobs identity mismatch');job=next((j for j in jobs if j['name']=='validate-strict' and (m.group(2) is None or j['id']==int(m.group(2)))),None);need(job is not None,'Required check job missing')
 if strict['status']!='completed' or wr['status']!='completed' or any(j['status']!='completed' for j in jobs):result['pending'].append('Required CI not yet terminal')
 else:need(strict['conclusion']==wr['conclusion']=='success' and all(j['conclusion']=='success' for j in jobs),'Required CI failed')
 ap,annotations=pages(f'repos/{repo}/check-runs/{strict["id"]}/annotations');need(len(annotations)==strict['output']['annotations_count'],'Check annotation count differs');need(all(a['annotation_level']=='notice' and 'ubuntu-latest label will migrate to Ubuntu 26 beginning October 19, 2026' in a['message'] for a in annotations),'Unassessed check annotation needs review');result['ci_annotations']={'pages':ap,'disposition':('Informational runner-image migration notice, not a failed check or current package defect. Workflow unchanged; any runner policy change belongs in CLAW-supported governance.' if annotations else 'No check annotations reported.')}
 result.update(required_check=strict,workflow_run=wr,workflow_jobs=jobs)
 rules=api(f'repos/{repo}/rules/branches/main');need(any(x['type']=='required_status_checks' and {'context':'validate-strict','integration_id':15368} in x['parameters']['required_status_checks'] for x in rules),'Required integration changed');need(any(x['type']=='merge_queue' and x['parameters']['merge_method']=='SQUASH' and x['parameters']['grouping_strategy']=='ALLGREEN' for x in rules),'Native queue rule changed');result['effective_rules']=rules
 issues=[]
 issue_receipts={x['number']:x['receipt_filename'] for x in load(T/'cmm-round95-issue-ledger.json')}
 need({x['number'] for x in report['issues']}==set(issue_receipts),'Report issue set differs')
 for n,filename in issue_receipts.items():
  issue=api(f'repos/{repo}/issues/{n}');op=W/'reviews/publication/20261015-round95'/filename;old=load(op);expected=old['issue'];need(issue['state']=='open' and expected['number']==n and issue['title']==expected['title'] and issue['body']==expected['body'] and hashlib.sha256(issue['body'].encode()).hexdigest()==old['body_sha256'],'Source issue changed '+str(n));issues.append(issue)
 result['live_issues']=issues
 corrective_path=T/'cmm-round95-corrective-issue-ledger.json';corrective_ledger=load(corrective_path);need(isinstance(corrective_ledger,list) and len(corrective_ledger)==len({x['number'] for x in corrective_ledger}),'Malformed corrective ledger');need({x['number'] for x in report['corrective_issues']}=={x['number'] for x in corrective_ledger},'Report corrective issue set differs');corrective=[]
 for row in corrective_ledger:
  n=row['number'];need(row['state']=='CLOSED' and n not in issue_receipts,'Corrective/source issue class mismatch');initialp=W/'reviews/publication/20261015-round95'/row['initial_receipt'];closedp=W/'reviews/publication/20261015-round95'/row['closure_receipt'];initial=load(initialp);closed=load(closedp);live=api(f'repos/{repo}/issues/{n}');need(closed['passed'] and closed['issue']['number']==n and closed['issue']['state']=='CLOSED' and live['number']==n and live['state']=='closed','Corrective closure incomplete');need(closed['initial_receipt_sha256']==sha(initialp),'Closure initial receipt hash differs');need(live['title']==initial['issue']['title']==closed['issue']['title'] and live['body']==initial['issue']['body']==closed['issue']['body'],'Corrective live content differs');corrective.append({'number':n,'live':live,'initial':binding(initialp),'closure':binding(closedp)})
 result['corrective_issues']=corrective;input_bindings.extend([binding(T/'cmm-round95-issue-ledger.json'),binding(corrective_path),binding(body)])
 pp=T/'cmm-round95-preflight-committed-terminal.json'
 if not pp.exists():result['pending'].append('Committed isolated preflight not yet terminal')
 else:
  pre=check_log_receipt(pp);need(pre['mode']=='preflight' and pre['trusted_base']==c['base'] and pre['topic_head']==c['head'] and pre['expected_tree']==c['tree'] and pre['counts']==cfg['counts'],'Preflight identity differs');need(all(x['exit_code'] in x['allowed_exit_codes'] for x in pre['commands']),'Preflight command failed')
  for req in requirements[1:3]+[['just','review-check','--base',c['base'],'--require-reviews']]:need(any(x['command']==req and x['exit_code']==0 for x in pre['commands']),'Required preflight command missing')
  need(len(pre['topic_object_checks'])>=3 and all(x['absent'] for x in pre['topic_object_checks']),'Topic leaked into isolated clone');need(pre['verified_retained_tag']['remote_verified'],'Retained tag not verified');pc=load(pre['coverage_receipt']);need(pc['passed'] and all(pc[k]==v for k,v in cfg['counts'].items()),'Preflight coverage mismatch');need({r['path']:r['sha256'] for r in pc['records']}==gates['record_inputs'] and len(pc['records'])==cfg['counts']['record_count'],'Preflight exact owner coverage mismatch');result['preflight']={**binding(pp),'log_sha256':pre['log_sha256'],'counts':pre['counts'],'coverage':binding(pre['coverage_receipt'])}
 main=api(f'repos/{repo}/git/ref/heads/main');need(main['object']['sha']==c['base'],'Live main moved');end=api(f'repos/{repo}/pulls/{N}');need(all(end[k]==pr[k] for k in ['state','title','body','changed_files','comments','review_comments']) and end['head']['sha']==c['head'] and end['base']['sha']==c['base'],'PR changed during audit');wr_end=api(f'repos/{repo}/actions/runs/{rid}');need(wr_end['run_attempt']==attempt and wr_end['head_sha']==c['head'] and wr_end['status']==wr['status'] and wr_end['conclusion']==wr['conclusion'],'CI attempt/state changed');need(not git('status','--porcelain=v1','--untracked-files=all') and git('rev-parse','HEAD')==c['head'],'Local source changed');need(all(sha(x['path'])==x['sha256'] for x in input_bindings),'Input receipt changed during audit');need(all(sha(W/x['path'])==x['sha256'] for x in files),'Committed file bytes changed during audit');need(digest(conversation_inventory())==digest(conv),'Conversation changed during audit');result['input_receipts']=input_bindings;result['live_main']=main
 result['passed']=not result['pending'];result['status']='passed' if result['passed'] else 'pending';result['limitations']=['Operational current-head acceptance relies on separate independent science for the authored spent-steel-pickling-liquors record. No source or immutable review was modified.','Queue admission, merge-group checks, actual merge tree/parent, owned branch cleanup, fresh-main provenance and original-main synchronization remain future gates.','All reads were bounded to the exact committed package and hosted PR. No new literature or full-suite execution occurred.']
 if result['passed']:
  counts=cfg['counts'];issue_labels=', '.join('#'+str(n) for n in sorted(issue_receipts))
  comment=f"Independent operational review of exact head `{c['head']}` (tree `{c['tree']}`).\n\nVerified all {len(paths)} paginated changed-file blobs, the sole reviewed-base parent, live title/body, all review/comment/thread surfaces, and seven exact independent scientific reviews with owner/history/source bindings. Completed local checks and isolated squash-shaped preflight passed: {counts['record_count']} records, {counts['history_count']} history sessions, {counts['structured_review_count']} native reviews, {counts['review_base_count']} available bases and {counts['covered_records']} current records covered. The local full suite passed 317 tests with 3 skipped. Required `validate-strict` passed for this exact PR head/current Actions attempt: {wr['html_url']}.\n\nI authored spent-steel-pickling-liquors and rely on its separate root-agent scientific acceptance; this operational review does not self-accept that science. I independently reviewed hauerite and melanterite. No supported unresolved corrective finding was found. Source clarification issues {issue_labels} remain open with their limitations represented. Corrective review issues {', '.join('#'+str(x['number']) for x in corrective_ledger)} are closed with retained original findings and verified dispositions.\n\nNative queue and merge-group checks, actual merged tree/parent, owned-branch cleanup, fresh-main provenance and protected-state verification remain required. This is a COMMENT, not an approval.\n"
  q=T/'cmm-round95-hosted-review-comment.md';need(not q.exists() or q.read_text()==comment,'Existing COMMENT differs; preserve before revising');q.write_text(comment);result['comment_draft']=binding(q)
except Exception as exc:
 result['passed']=False;result['status']='needs_attention';result['error']=str(exc)
finally:
 result['finished_at']=now();result['helper']=binding(Path(__file__));result['api_provenance']=calls;need(not out.exists(),'Receipt collision');out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'receipt':str(out),'sha256':sha(out),'passed':result['passed'],'status':result.get('status'),'error':result.get('error'),'pending':result['pending'],'conversation':result.get('conversation'),'ci':{k:result.get('workflow_run',{}).get(k) for k in ['id','status','conclusion','run_attempt']},'comment_draft':result.get('comment_draft')},indent=2))
sys.exit(0 if result['passed'] else (3 if result.get('status')=='pending' else 1))
