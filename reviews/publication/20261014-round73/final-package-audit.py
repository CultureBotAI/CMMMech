"""Independent operational peer audit. Run only on coordinator-frozen round73 package.
Read-only Git/GitHub; writes only unique own publication audit pair and raw receipt.
"""
from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor
import ast,hashlib,html,json,os,re,subprocess,yaml
W=Path('/private/tmp/CMMMech-expansion-round73-20261014');T=Path('/private/tmp');BASE='ea4b9370fdb3d1ab23e5f43f6f9fe5f8d46a31e3';BRANCH='curate/cmm-expansion-round73-20261014';PUB=W/'reviews/publication/20261014-round73'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
now=lambda:datetime.now(timezone.utc).isoformat()
def require(c,m):
 if not c:raise AssertionError(m)
def git(*a):return subprocess.check_output(['git','-C',str(W),*a]).decode().strip()
def names():
 a=subprocess.check_output(['git','-C',str(W),'diff','--name-only','-z']).split(b'\0');b=subprocess.check_output(['git','-C',str(W),'ls-files','--others','--exclude-standard','-z']).split(b'\0');return {os.fsdecode(x) for x in a+b if x}
def binding(p):return dict(path=str(p),sha256=sha(p),bytes=Path(p).stat().st_size)
def walk_obj(x):
 yield x
 if isinstance(x,dict):
  for y in x.values():yield from walk_obj(y)
 elif isinstance(x,list):
  for y in x:yield from walk_obj(y)
def yaml_files(p,name=None):
 result=[];seen=set()
 for d,dirs,files in os.walk(p,followlinks=True):
  real=Path(d).resolve()
  if real in seen:dirs[:]=[];continue
  seen.add(real)
  for f in files:
   if (name and f==name) or (not name and f.endswith(('.yaml','.yml'))):result.append(Path(d)/f)
 return sorted(result)
started=now();cfg=json.loads((T/'cmm-round73-helper-config.json').read_text());require(git('rev-parse','HEAD')==BASE,'Wrong HEAD');require(git('branch','--show-current')==BRANCH,'Wrong branch');require(not git('diff','--cached','--name-only'),'Staged inputs present');subprocess.run(['git','-C',str(W),'diff','--check'],check=True)
require(not list(PUB.glob('*-publication-final.json')),'Existing final audit; do not overwrite')
candidates=names();require(candidates,'No candidate inputs');require(all((W/n).is_file() and not (W/n).is_symlink() for n in candidates),'Unsafe candidate file');manifest=json.loads((W/'research/ingests/round73-frontier-20261014.json').read_text());require(manifest['base']==BASE and manifest['branch']==BRANCH and manifest['counts']==cfg['counts'] and manifest['issues']==cfg['issues'],'Manifest identity/config mismatch')
initial_working={n:sha(W/n) for n in candidates}
manifestpaths=[x['path'] for x in manifest['artifacts']];require(len(set(manifestpaths))==len(manifestpaths),'Duplicate manifest path');require(set(manifestpaths)==candidates-{'research/ingests/round73-frontier-20261014.json','research/ingests/round73-frontier-20261014.md'},'Manifest does not cover exact complete pre-report candidate set')
for x in manifest['artifacts']:require(sha(W/x['path'])==x['sha256'],'Manifest changed '+x['path'])
receipts=[]
for name in ['baseline','final-gates','review-check-final','local-coverage']:
 p=T/f'cmm-round73-{name}.json';d=json.loads(p.read_text());require(d.get('passed',d.get('exit_code')==0) is True,'Failed terminal '+name)
 if 'commands' in d:require(d['commands'] and all(c['exit_code']==0 for c in d['commands']),'Failed command '+name)
 if 'log' in d:require(sha(Path(d['log']))==d['log_sha256'],'Changed log '+name)
 if name in ['baseline','final-gates']:
  require(d.get('base')==BASE and d.get('worktree')==str(W),'Gate identity mismatch '+name)
  require(d['started_at']<d['finished_at'],'Gate timing mismatch '+name)
 if name=='baseline':
  require([c['command'] for c in d['commands']]==[['uv','sync','--quiet','--locked','--extra','dev','--offline'],['just','check'],['uv','run','--locked','cmmmech','validate','--require-records'],['uv','run','--locked','cmmmech','validate-history','--base',BASE]],'Baseline was not actually executed as documented')
  require('317 passed, 3 skipped' in Path(d['log']).read_text(),'Unexpected baseline test result')
 if name=='final-gates':
  require([c['command'] for c in d['commands']]==[['just','check'],['uv','run','--locked','cmmmech','validate','--require-records'],['uv','run','--locked','cmmmech','validate-history','--base',BASE]],'Incomplete final gates')
  text=Path(d['log']).read_text();require('317 passed, 3 skipped' in text,'Unexpected test result')
 if name=='review-check-final':require(d['base']==BASE,'Review base mismatch')
 if name=='local-coverage':require(all(d[k]==v for k,v in cfg['counts'].items()),'Coverage counts mismatch')
 retained=PUB/p.name.removeprefix('cmm-round73-');require(retained.is_file() and sha(retained)==sha(p),'Retained receipt mismatch '+name);receipts.append(binding(p))
records=yaml_files(W/'data/records');histories=yaml_files(W/'history/records');reviews=[(p,yaml.safe_load(p.read_text())) for p in yaml_files(W/'reviews/structured','review.yaml')];bases={x['source']['git_revision'] for p,x in reviews};coverage=[]
for p in records:
 d=yaml.safe_load(p.read_text());rp=str(p.relative_to(W));digest=sha(p);matches=[]
 for q,v in reviews:
  if v.get('scientific_review') is True and v.get('completion')=='completed' and v.get('verdict') in ['pass','pass_with_limitations'] and d['id'] in v['scope']['reviewed_target_ids'] and any(t.get('path')==rp and t.get('target_id')==d['id'] for t in v['targets']) and any(i['path']==rp and i['sha256']==digest for i in v['source']['inputs']):matches.append(str(q.relative_to(W)))
 require(matches,'No exact positive scientific review '+rp);coverage.append({'record':rp,'sha256':digest,'reviews':matches})
actual={'record_count':len(records),'history_count':len(histories),'structured_review_count':len(reviews),'review_base_count':len(bases),'covered_records':len(coverage)};require(actual==cfg['counts'],'Actual counts mismatch')
for b in bases:require(git('cat-file','-t',b)=='commit','Unavailable review base '+b)
require(set(cfg['slugs'])=={'microcline','muscovite','artinite','lansfordite','senarmontite','end-of-life-cigs-photovoltaic-modules'} and len(cfg['slugs'])==6,'Wrong round73 configured cohort')
require(len(manifest['records_changed'])==6 and {i['slug'] for i in manifest['records_changed']}==set(cfg['slugs']),'Manifest changed-record set mismatch')
require(cfg['created_slugs']==cfg['slugs'] and cfg['updated_slugs']==[],'Expected six CREATE owners (artinite may also have corrective EDIT)')
final=[];resolutions=[]
for item in manifest['records_changed']:
 p=W/item['path'];d=yaml.safe_load(p.read_text());q=W/item['review'];v=yaml.safe_load(q.read_text());require(item['sha256']==sha(p),'Owner manifest mismatch');require(item['review'] in next(z['reviews'] for z in coverage if z['record']==item['path']),'Selected review not exact positive')
 require(v['reviewer']['independence']=='independent','Final science review not independent')
 if item['slug'] in ['microcline','muscovite']:require(v['reviewer']['identity']!='codex /root/round68_new_frontier','Reviewer authored this silicate; independent acceptance required')
 require(v['source']['git_revision']==BASE and v['source']['state']=='working_tree','Final science base/state')
 for h in d['history_refs']:
  hp=W/h;hv=yaml.safe_load(hp.read_text());require(hv['target']['path']==item['path'] and hv['target']['slug']==item['slug'],'History owner mismatch');require(any(i['path']==h and i['sha256']==sha(hp) for i in v['source']['inputs']),'Final review omits exact history '+h)
 for finding in v.get('findings',[]):require(finding['status'] in ['resolved','rejected','accepted_risk'],'Unresolved final finding '+item['slug'])
 final.append(dict(record=item['path'],sha256=sha(p),review=item['review'],review_sha256=sha(q),reviewer=v['reviewer'],verdict=v['verdict']))
 for f in v.get('findings',[]):
  if f['status']=='resolved':
   require(f.get('previous_occurrences'),'Resolved finding lacks lineage')
   for prev in f['previous_occurrences']:
    old=next((z for op,z in reviews if z['review_id']==prev['review_id']),None);require(old,'Unknown finding predecessor');of=next((z for z in old['findings'] if z['finding_id']==prev['finding_id']),None);require(of and of['issue_key']==f['issue_key'],'Wrong stable finding lineage');resolutions.append(dict(current_review=v['review_id'],finding_id=f['finding_id'],issue_key=f['issue_key'],previous=prev))
# Documentation-only corrective issues use their retained operational initial/successor receipts below.
# Any actual resolved scientific finding still requires the native lineage checked above.
# Only observed current-round corrections are required; no inherited historical findings.
require(len(final)==6,'Missing independent final scientific reviews')
# Index only declared round73 scientific raw roots plus exact local artifacts referenced in dossiers/reviews.
sourcejson=[]
for folder in ['round73-carbonates','round73-silicates','round73-antimony-minerals','round73-cigs']:
 pair=list((W/'research/sources'/folder).glob('*.json'));require(pair,'Missing source dossier '+folder)
 for p in pair:require(p.with_suffix('.md').is_file(),'Missing paired source dossier '+str(p))
 sourcejson.extend(pair)
rawroots=[T/n for n in ['cmm-round73-carbonates-research','cmm-round73-silicates-research','cmm-round73-antimony-minerals-research','cmm-round73-cigs-research','cmm-round73-senarmontite-review','cmm-round73-carbonates-independent','cmm-round73-cigs-independent','cmm-round73-microcline-peer']];paths=set()
for root in rawroots:
 seen_raw=set()
 for dp,dirs,files in os.walk(root,followlinks=True):
  resolved=Path(dp).resolve()
  if resolved in seen_raw:dirs[:]=[];continue
  seen_raw.add(resolved)
  for f in files:paths.add(Path(dp)/f)
for p in sourcejson:
 for x in walk_obj(json.loads(p.read_text())):
  if isinstance(x,str) and x.startswith('/private/tmp/'):
   q=Path(x)
   if q.is_file():paths.add(q)
for p,v in reviews:
 if 'round73' not in v['review_id']:continue
 for x in walk_obj(v):
  if isinstance(x,str):
   for st in re.findall(r'/private/tmp/[A-Za-z0-9_./-]+',x):
    q=Path(st.rstrip('.'))
    if q.is_file():paths.add(q)
byhash={}
for p in sorted(paths):
 if p.is_file():byhash.setdefault(sha(p),[]).append(p)
source_bindings=[];unbound_context=[]
for p,v in reviews:
 if 'round73' not in v['review_id']:continue
 for e in v.get('evidence',[]):
  if e['kind']!='primary_source':continue
  digest=e.get('snapshot_sha256');ref=e['reference']
  if digest is None:
   require(e.get('support')=='context_only','Hashless supporting primary evidence '+v['review_id']+':'+e['evidence_id'])
   require(any(word in (e.get('summary','')+' '+str(v.get('limitations',[]))).lower() for word in ['unavailable','not acquired','not downloaded','access limit']),'Hashless context lacks explicit access limits')
   unbound_context.append(dict(review=v['review_id'],evidence_id=e['evidence_id'],reference=ref,locator=e['locator'],support=e['support'],summary=e['summary'],disposition='Explicit context-only observation; no supporting evidence or verified local artifact asserted.'))
   continue
  require(isinstance(digest,str) and re.fullmatch('[0-9a-f]{64}',digest) and digest!=hashlib.sha256(b'').hexdigest(),'Missing/empty primary hash '+v['review_id']+':'+e['evidence_id']);matches=byhash.get(digest,[])
  if ref.startswith('/private/tmp/'):
   require(Path(ref).is_file() and sha(Path(ref))==digest,'Explicit primary path/hash mismatch '+ref);matches=[Path(ref)]
  require(matches,'Primary snapshot not backed by current raw bytes '+v['review_id']+':'+e['evidence_id'])
  for path in matches:
   require(path.stat().st_size>0,'Empty primary source')
   if path.suffix.lower()=='.pdf':require(path.read_bytes().startswith(b'%PDF-'),'Primary PDF is not PDF '+str(path))
  source_bindings.append(dict(review=v['review_id'],evidence_id=e['evidence_id'],reference=ref,sha256=digest,matching_local_artifacts=[binding(x) for x in matches]))
require(source_bindings,'No primary bindings')
require({yaml.safe_load((W/i['review']).read_text())['review_id'] for i in manifest['records_changed']} <= {x['review'] for x in source_bindings},'A selected review lacks a nonempty verified primary-source binding')
# Verify prepared/root-retained helper bytes and every final publication input syntactically.
helper_bindings=[]
for p in PUB.glob('*.py'):
 ast.parse(p.read_text());external=T/('cmm-round73-'+p.name)
 if external.exists():require(sha(p)==sha(external),'Retained helper differs '+p.name)
 helper_bindings.append(binding(p))
readme=(W/'README.md').read_text();require(f'currently contains {actual["record_count"]} material records' in readme,'README count');require(all(f'data/records/{s}.yaml' in readme for s in cfg['slugs']),'README missing new owners')
page_bindings=[]
index=json.loads((W/'pages/index.json').read_text());require(len(index)==actual['record_count'],'Generated index count')
for slug in cfg['slugs']:
 owner=yaml.safe_load((W/f'data/records/{slug}.yaml').read_text());page=W/f'pages/materials/{slug}.html';rendered=html.unescape(re.sub('<[^>]+>',' ',page.read_text()));normalized=' '.join(rendered.split());required=[owner['description']]
 for mechanism in owner.get('mechanisms',[]):required.extend([mechanism['description'],mechanism['context']]+[e['explanation'] for e in mechanism['evidence']])
 require(all(' '.join(t.split()) in normalized for t in required),'Generated page differs from current scientific prose '+slug)
 entries=[x for x in index if x['slug']==slug];require(len(entries)==1 and entries[0]['material_kind']==owner['material_kind'] and entries[0]['mechanisms_count']==len(owner.get('mechanisms',[])),'Index owner metadata mismatch '+slug);page_bindings.append(binding(page))
body=T/'cmm-round73-pr-body.md';require(body.is_file(),'Missing PR body');require('341 to 347' in body.read_text() and all('#'+str(n) in body.read_text() for n in cfg['issues']['open_source_issues']),'PR scope/source priorities')
for name in ['integration-status','preservation-prepublication']:
 p=T/f'cmm-round73-{name}.json';v=json.loads(p.read_text());require(sha(PUB/(name+'.json'))==sha(p),'Retained '+name)
 if name=='preservation-prepublication':require(v['passed'] is True and v['preserved_entry_counts']=={'main':7187,'skill':7389},'Preservation failed or changed scope')
 else:
  require(v['admission']['state']=='MERGED' and v['admission']['number']==581 and v['convergence']['state']=='CLOSED' and v['convergence']['number']==580 and v['cmm_integration']['state']=='CLOSED' and v['cmm_integration']['number']==3,'Integration remains incomplete')
  queue=v['queue'];rules={i['type']:i['parameters'] for i in queue['rules']}
  require(queue['enforcement']=='active' and queue['conditions']['ref_name']=={'exclude':[],'include':['refs/heads/main']} and queue['bypass_actors']==[] and queue['current_user_can_bypass']=='never','Queue scope/bypass mismatch')
  require(rules['merge_queue']['merge_method']=='SQUASH' and rules['merge_queue']['grouping_strategy']=='ALLGREEN' and rules['merge_queue']['max_entries_to_merge']==1 and rules['required_status_checks']['required_status_checks']==[{'context':'validate-strict','integration_id':15368}],'Queue checks/method mismatch')
  require(v['vendored_result']=='OK: 22 governed artifacts match the pinned claw revision' and sha(PUB/'vendored.log')==v['vendored_log_sha256'],'Governed artifacts verification mismatch')
 receipts.append(binding(p))
expected={n:'CLOSED' for n in cfg['issues']['corrected_review_issues']+cfg['issues']['closed_source_issues']};expected.update({n:'OPEN' for n in cfg['issues']['open_source_issues']})
def issue(n):return json.loads(subprocess.check_output(['gh','issue','view',str(n),'--repo','CultureBotAI/CMMMech','--json','number,state,title,url,closedAt'],text=True))
with ThreadPoolExecutor(max_workers=4) as ex:live=list(ex.map(issue,sorted(expected)))
require(all(i['state']==expected[i['number']] for i in live),'Live issue disposition mismatch')
# Explicit current independent operational review selection, no latest-wins heuristic.
static_initial=PUB/'helper-static-20261014T140400Z.json'
require(static_initial.is_file(),'Missing immutable OP1 initial observation')
old_static=json.loads(static_initial.read_text());require(old_static['passed'] is False,'Initial OP1 observation must remain failed')
require(len(old_static['findings'])==1 and old_static['findings'][0]['id']=='OP1' and old_static['findings'][0]['status']=='open','Initial OP1 state mismatch')
static_final_path=Path(cfg['final_static_review']);peer_path=Path(cfg['publication_peer_review'])
require(static_final_path!=peer_path,'Separate operational review scopes must be explicit')
static_verified=[]
for src in [static_final_path,peer_path]:
 require(src.is_file(),'Missing explicitly selected operational review '+str(src))
 retained=PUB/src.name.removeprefix('cmm-round73-');require(retained.is_file() and sha(retained)==sha(src),'Operational review not retained '+str(src))
 v=json.loads(src.read_text());require(v.get('passed') is True,'Selected operational review is not passed')
 for f in v.get('findings',[]):require(f.get('status') in ['resolved','rejected','accepted_risk'],'Open operational finding')
 # Actual input shapes may use files/helper or inputs/path, but every declared current binding is checked.
 entries=v.get('inputs',v.get('files',[]))
 if src==static_final_path:
  require(v.get('current_helper')==str(T/'cmm-round73-hosted-audit-paginated.py'),'Unexpected OP1 corrected owner')
  entries=[{'path':v['current_helper'],'sha256':v['current_helper_sha256']}]
 require(entries,'Operational review has no exact input bindings')
 for i in entries:
  original=Path(i.get('path',i.get('helper','')));require(original.is_file() and sha(original)==i['sha256'],'Current static input changed '+str(original))
 static_verified.append(binding(retained))
current_static=json.loads(static_final_path.read_text());peer=json.loads(peer_path.read_text())
# Check actual OP1 correction lineage and unchanged behavior against retained initial helper bytes.
serialized=json.dumps(current_static)
require('OP1' in serialized and str(static_initial.name) in serialized and sha(static_initial) in serialized,'OP1 successor lacks exact initial occurrence binding')
require('237' in serialized,'OP1 successor lacks issue237 link')
original_helper=Path(next(i['snapshot'] for i in old_static['files'] if i.get('helper','').endswith('hosted-audit-paginated.py')))
require(original_helper.is_file(),'Missing OP1 original source snapshot')
expected_initial=next(i['sha256'] for i in old_static['files'] if i.get('helper','').endswith('hosted-audit-paginated.py'))
require(sha(original_helper)==expected_initial,'Changed OP1 original source snapshot')
for i in old_static['files']:
 original=Path(i['helper'])
 if 'snapshot' in i:
  snapshot=Path(i['snapshot']);require(snapshot.is_file() and sha(snapshot)==i['sha256'],'Initial helper snapshot changed')
  retained_snapshot=PUB/snapshot.parent.name.removeprefix('cmm-round73-')/snapshot.name
  require(retained_snapshot.is_file() and sha(retained_snapshot)==sha(snapshot),'Initial helper snapshot not retained')
 else:require(i.get('scope') and original.name=='cmm-round57-recover-original.py','Unexpected snapshot-less static input')
 if not original.name.endswith('hosted-audit-paginated.py'):require(sha(original)==i['sha256'],'Helper changed outside OP1 reviewed scope '+str(original))
old=original_helper.read_text();new=(T/'cmm-round73-hosted-audit-paginated.py').read_text()
require(old.count('Round71 reuses the round70 pagination correction')==1 and new==old.replace('Round71 reuses the round70 pagination correction','Round73 reuses the round70 pagination correction'),'OP1 correction exceeds reviewed one-label scope')
# Publication peer must explicitly inspect this auditor, hosted peer, config and final builder.
peer_entries=peer.get('inputs',peer.get('files',[]));peer_paths={i.get('path',i.get('helper')) for i in peer_entries}
require({str(Path(__file__)),str(T/'cmm-round73-hosted-peer.py'),str(T/'cmm-round73-helper-config.json'),str(T/'cmm-round73-build-summary.py')}<=peer_paths,'Publication peer did not inspect all final selectors/reporting helpers')
# One actual scientific correction is currently expected: artinite F1 with stable native lineage.
require(len(resolutions)==1 and resolutions[0]['issue_key']=='CMMMech.artinite.daily-shaking-duration' and resolutions[0]['previous']['review_id']=='20261014T140422Z-artinite-round73-initial' and resolutions[0]['previous']['finding_id']=='F1','Artinite corrective lineage differs from reviewed batch')
require(set(cfg['issues']['corrected_review_issues'])=={236,237},'Unexpected corrected issue set; reassess rather than silently accepting new findings')
documentation_dispositions=[]
for n in [236,237]:
 closed=PUB/f'issue-{n}-closed.json';d=json.loads(closed.read_text());require(d['number']==n and d['state']=='CLOSED','Missing retained issue closure '+str(n))
 if 'resolution_sha256' in d:require(sha(PUB/('artinite-resolution.md' if n==236 else 'helper-resolution.md'))==d['resolution_sha256'],'Closure text binding mismatch')
 documentation_dispositions.append(dict(issue=n,closed_receipt=binding(closed),scope='native scientific F1' if n==236 else 'operational OP1',status='resolved'))
# Capture only after all read checks, and reject intervening edits before writing own self-excluded pair.
working=[{'path':n,'sha256':sha(W/n)} for n in sorted(candidates)];require(names()==candidates and all(sha(W/x['path'])==x['sha256']==initial_working[x['path']] for x in working),'Package changed during audit');require(git('rev-parse','HEAD')==BASE and git('branch','--show-current')==BRANCH and not git('diff','--cached','--name-only'),'Git state changed during audit')
report=dict(started_at=started,finished_at=now(),reviewer='codex /root/round68_new_frontier',authorship='Independent operational peer of root-authored publication. Authored microcline and muscovite; their scientific acceptance is supplied by separate independent reviewer(s), not self-accepted here. Independently reviewed peer-authored senarmontite.',base=BASE,branch=BRANCH,state='working_tree',passed=True,verdict='pass_with_limitations',unresolved_corrective_findings=0,counts=actual,issues=cfg['issues'],findings=[],working_inputs=working,final_scientific_reviews=final,resolution_lineages=resolutions,documentation_dispositions=documentation_dispositions,primary_source_bindings=source_bindings,unbound_context_only_primary_observations=unbound_context,generated_page_bindings=page_bindings,terminal_receipts=receipts,live_issues=live,prepared_pr_body=binding(body),helper_bindings=helper_bindings,static_helper_reviews=static_verified,selected_static_helper_review=binding(static_final_path),publication_peer_review=binding(peer_path),auditor=binding(Path(__file__)),manifest=binding(W/'research/ingests/round73-frontier-20261014.json'),limitations=['Local candidate package audit only. Commit/push, exact hosted text/files/checks, isolated squash preflight, native queue, actual squash tree/sole parent, five hosted workflows/jobs, branch deletion, fresh-main validation and preservation closeout remain subsequent gates.','Baseline and final gates were both actually executed in round73; terminal receipts, command identities, worktree/base and log checksums were checked. Subsequent publication gates are not preclaimed.','Raw-source inventory is bounded to declared research/review roots and cited exact files; this is not machine-wide source completeness. Acquisition failures remain historical and are not accepted primary evidence.','Operational source hashes verify provenance, not independent re-performance of every scientific assessment.'])
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ');out=PUB/(stamp+'-publication-final.json');md=out.with_suffix('.md');require(not out.exists() and not md.exists(),'Audit collision')
with out.open('x') as f:f.write(json.dumps(report,indent=2)+'\n')
text='# Round73 final local publication audit\n\n'+f'UTC: {report["finished_at"]}. Verdict: pass with limitations; no unresolved corrective findings. Exact base `{BASE}`, branch `{BRANCH}`, working-tree state.\n\n'
text+=f'The package has {actual["record_count"]} records, {actual["history_count"]} history sessions, {actual["structured_review_count"]} review bundles and {actual["review_base_count"]} available review bases. Every current owner has a completed positive scientific review of its exact bytes. All six new owners have separate independent final scientific reviews. Artinite F1 is resolved through its exact native predecessor, and operational OP1 retains its initial source snapshot and explicit independent successor. Issues236/237 are closed with retained receipts.\n\n'
text+='Open source follow-ups remain '+', '.join('#'+str(n) for n in cfg['issues']['open_source_issues'])+'. Their live issue states match the prepared report.\n\n'
text+=f'Verified {len(working)} exact candidate inputs, the manifest, completed receipt/log hashes, retained helper bytes and {len(source_bindings)} nonempty primary-evidence bindings. Baseline and final gates were actually executed at this base; no inherited pass is claimed. README, generated pages and PR scope preserve abiotic observations, mixed-phase products, laboratory limits, criticality boundaries, null outcomes and unresolved evidence.\n\n'
text+=f'{len(unbound_context)} explicitly context-only primary observations lack a local snapshot hash; accepted supporting primary evidence must bind nonempty inspected artifacts. The JSON records any declared access limits.\n\n'
text+='The reviewer authored microcline and muscovite, whose scientific acceptance comes from separate independent reviewers, and independently assessed peer-authored senarmontite. This operational audit does not self-accept the reviewer’s science. The JSON companion binds exact files, source paths/hashes, review references, helper peers and live issue responses.\n\n'
text+='Publication remains conditional on exact-head hosted review, isolated squash preflight, native queue and actual merge checks, five successful hosted workflow/job runs, branch cleanup, fresh remote-main validation and preservation.\n'
with md.open('x') as f:f.write(text)
print(json.dumps({'audit':str(out),'sha256':sha(out),'markdown':str(md),'working_inputs':len(working),'primary_bindings':len(source_bindings),'counts':actual},indent=2))
