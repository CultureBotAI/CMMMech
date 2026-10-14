"""Read-only independent operational audit of coordinator-frozen round74 package.
Writes only its unique final publication JSON/Markdown pair; no Git/GitHub mutations.
"""
from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor
import ast,hashlib,html,json,os,re,subprocess,yaml
W=Path('/private/tmp/CMMMech-expansion-round74-20261014');T=Path('/private/tmp');BASE='a524756f3f4f90d81f89035fa7f85f1e1897b99d';BRANCH='curate/cmm-expansion-round74-20261014';PUB=W/'reviews/publication/20261014-round74'
SLUGS={'kaolinite','nontronite','marcasite','violarite','variscite','strengite','cadmium-telluride-photovoltaic-module-scrap'}
EXPECTED_REVIEWS={'kaolinite':'20261014T150450Z-kaolinite-round74-final','nontronite':'20261014T145850Z-nontronite-round74-independent','marcasite':'20261014T145839Z-marcasite-round74-independent','violarite':'20261014T145843Z-violarite-round74-independent','variscite':'20261014T145714Z-variscite-round74-independent','strengite':'20261014T145719Z-strengite-round74-independent','cadmium-telluride-photovoltaic-module-scrap':'20261014T145642Z-cadmium-telluride-module-scrap-round74-independent'}
ME='codex /root/round68_iron_sulfides'
AUDIT_OUT=PUB/'20261014T150443Z-publication-final.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
now=lambda:datetime.now(timezone.utc).isoformat()
def need(c,m):
 if not c:raise AssertionError(m)
def git(*args):return subprocess.check_output(['git','-C',str(W),*args],text=True).strip()
def candidates():
 a=subprocess.check_output(['git','-C',str(W),'diff','--name-only','-z']);b=subprocess.check_output(['git','-C',str(W),'ls-files','--others','--exclude-standard','-z']);return {os.fsdecode(x) for x in (a+b).split(b'\0') if x}
def bind(p):return {'path':str(p),'sha256':sha(p),'bytes':Path(p).stat().st_size}
def walk_files(root):
 found=[];seen=set()
 for d,dirs,files in os.walk(root,followlinks=True):
  q=Path(d).resolve()
  if q in seen:dirs[:]=[];continue
  seen.add(q)
  found.extend(Path(d)/f for f in files)
 return sorted(found)
def yaml_files(root,name=None):return [p for p in walk_files(root) if p.name==name] if name else [p for p in walk_files(root) if p.suffix in ('.yaml','.yml')]
def objects(x):
 yield x
 if isinstance(x,dict):
  for v in x.values():yield from objects(v)
 elif isinstance(x,list):
  for v in x:yield from objects(v)
started=now();cfgp=T/'cmm-round74-helper-config.json';cfg=json.loads(cfgp.read_text());cfg_start=sha(cfgp)
need(Path(cfg['publication_peer_review'])==AUDIT_OUT,'Wrong configured final audit destination')
need(git('rev-parse','HEAD')==BASE and git('branch','--show-current')==BRANCH,'Wrong working base/branch');need(not git('diff','--cached','--name-only'),'Staged input present');subprocess.run(['git','-C',str(W),'diff','--check'],check=True)
need(not list(PUB.glob('*-publication-final.json')),'Final audit already exists; preserve it')
need(set(cfg['slugs'])==SLUGS and len(cfg['slugs'])==7 and cfg['created_slugs']==cfg['slugs'] and cfg['updated_slugs']==[],'Wrong seven-owner cohort')
need(cfg['counts']=={'record_count':354,'history_count':409,'structured_review_count':423,'review_base_count':75,'covered_records':354},'Counts changed; reassess scope')
need(cfg['issues']=={'corrected_review_issues':[241,242],'closed_source_issues':[],'open_source_issues':[240]},'Issue scope changed; reassess')
initial_names=candidates();need(initial_names,'No commit candidates');need(all((W/n).is_file() and not (W/n).is_symlink() for n in initial_names),'Unsafe candidate path');initial_hashes={n:sha(W/n) for n in initial_names}
manifestp=W/'research/ingests/round74-frontier-20261014.json';manifest=json.loads(manifestp.read_text());need(manifest['base']==BASE and manifest['branch']==BRANCH and manifest['counts']==cfg['counts'] and manifest['issues']==cfg['issues'],'Manifest/config mismatch')
paths=[x['path'] for x in manifest['artifacts']];need(len(paths)==len(set(paths)),'Duplicate artifact path');need(set(paths)==initial_names-{str(manifestp.relative_to(W)),str(manifestp.with_suffix('.md').relative_to(W))},'Manifest misses or adds pre-report candidates')
for x in manifest['artifacts']:need(sha(W/x['path'])==x['sha256'],'Manifest artifact changed: '+x['path'])
pubfiles=[p for p in walk_files(PUB) if p.is_file() and not p.is_symlink()];pubhashes={}
for p in pubfiles:pubhashes.setdefault(sha(p),[]).append(str(p.relative_to(W)))
def retained(p):
 need(Path(p).is_file() and Path(p).stat().st_size>0,'Missing/empty external artifact '+str(p));need(sha(p) in pubhashes,'Artifact not retained exactly: '+str(p));return dict(bind(p),retained_paths=pubhashes[sha(p)])
receipts=[]
expected_commands=[['just','check'],['uv','run','--locked','cmmmech','validate','--require-records'],['uv','run','--locked','cmmmech','validate-history','--base',BASE]]
for label in ['baseline','final-gates','final-gates-afterfix','review-check-final','local-coverage']:
 p=T/f'cmm-round74-{label}.json';d=json.loads(p.read_text());need(d.get('passed',d.get('exit_code')==0) is True,'Failed terminal receipt '+label)
 if 'commands' in d:need(d['commands'] and all(c['exit_code']==0 for c in d['commands']),'Failed/absent commands '+label)
 if 'log' in d:need(sha(Path(d['log']))==d['log_sha256'],'Receipt/log hash mismatch '+label);receipts.append(retained(Path(d['log'])))
 if label in ['baseline','final-gates','final-gates-afterfix']:
  need(d['base']==BASE and d['worktree']==str(W) and d['started_at']<d['finished_at'],'Wrong gate identity/times '+label)
  expected=([['uv','sync','--quiet','--locked','--extra','dev','--offline']] if label=='baseline' else [])+expected_commands
  need([x['command'] for x in d['commands']]==expected,'Incomplete or reused gate '+label)
  text=Path(d['log']).read_text();need('317 passed, 3 skipped' in text,'Unexpected tests '+label)
  if label=='baseline':need('Checked 347 record(s); 0 failed.' in text and 'Checked 401 history record(s); 0 error(s).' in text,'Baseline counts')
  if label=='final-gates-afterfix':need('Checked 354 record(s); 0 failed.' in text and 'Checked 409 history record(s); 0 error(s).' in text,'Afterfix gate counts')
 if label=='review-check-final':need(d['base']==BASE and d['commands'][0]['command']==['just','review-check','--base',BASE,'--require-reviews'],'Review gate identity')
 if label=='local-coverage':need(all(d[k]==v for k,v in cfg['counts'].items()),'Coverage receipt counts')
 receipts.append(retained(p))
records=yaml_files(W/'data/records');histories=yaml_files(W/'history/records');reviews=[(p,yaml.safe_load(p.read_text())) for p in yaml_files(W/'reviews/structured','review.yaml')];bases={v['source']['git_revision'] for p,v in reviews};coverage={}
for p in records:
 d=yaml.safe_load(p.read_text());rp=str(p.relative_to(W));digest=sha(p);matches=[]
 for q,v in reviews:
  if v.get('scientific_review') is True and v.get('completion')=='completed' and v.get('verdict') in ('pass','pass_with_limitations') and d['id'] in v['scope']['reviewed_target_ids'] and any(t['path']==rp and t['target_id']==d['id'] for t in v['targets']) and any(i['path']==rp and i['sha256']==digest for i in v['source']['inputs']):matches.append(str(q.relative_to(W)))
 need(matches,'No current positive scientific review: '+rp);coverage[rp]=matches
actual={'record_count':len(records),'history_count':len(histories),'structured_review_count':len(reviews),'review_base_count':len(bases),'covered_records':len(coverage)};need(actual==cfg['counts'],'Actual census differs from config')
for b in bases:need(git('cat-file','-t',b)=='commit','Unavailable review base: '+b)
need(len(manifest['records_changed'])==7 and {x['slug'] for x in manifest['records_changed']}==SLUGS,'Changed owner manifest differs')
final=[];resolutions=[]
for i in manifest['records_changed']:
 p=W/i['path'];d=yaml.safe_load(p.read_text());q=W/i['review'];v=yaml.safe_load(q.read_text());need(i['path']==f"data/records/{i['slug']}.yaml" and i['sha256']==sha(p),'Wrong owner/hash');need(i['review'] in coverage[i['path']],'Selected review is not exact positive')
 need(i['review']==f"reviews/structured/{EXPECTED_REVIEWS[i['slug']]}/review.yaml" and v['review_id']==EXPECTED_REVIEWS[i['slug']],'Unexpected final scientific observation selected')
 need(v['reviewer']['independence']=='independent','Selected scientific review not independent')
 if i['slug'] in ['marcasite','violarite']:need(v['reviewer']['identity']!=ME,'Own science requires separate acceptance')
 need(v['source']['git_revision']==BASE and v['source']['state']=='working_tree','Wrong selected review provenance')
 for h in d['history_refs']:
  hp=W/h;hv=yaml.safe_load(hp.read_text());need(hv['target']['path']==i['path'] and hv['target']['slug']==i['slug'],'History ownership mismatch');need(any(x['path']==h and x['sha256']==sha(hp) for x in v['source']['inputs']),'Selected review lacks exact history '+h)
 for f in v.get('findings',[]):
  need(f['status'] in ['resolved','rejected','accepted_risk'],'Unresolved selected finding')
  if f['status']=='resolved':
   need(f.get('previous_occurrences'),'Resolved finding missing predecessor')
   for prev in f['previous_occurrences']:
    old=next((rv for rp,rv in reviews if rv['review_id']==prev['review_id']),None);need(old is not None,'Unknown predecessor');of=next((x for x in old['findings'] if x['finding_id']==prev['finding_id']),None);need(of and of['issue_key']==f['issue_key'],'Wrong native lineage');resolutions.append({'review':v['review_id'],'finding_id':f['finding_id'],'issue_key':f['issue_key'],'previous':prev})
 final.append({'record':i['path'],'sha256':sha(p),'review':i['review'],'review_sha256':sha(q),'reviewer':v['reviewer'],'verdict':v['verdict']})
need(len(resolutions)==1 and resolutions[0]['issue_key']=='CMMMech.kaolinite.dfam-standard-expansion' and resolutions[0]['previous']['review_id']=='20261014T145845Z-kaolinite-round74-initial' and resolutions[0]['previous']['finding_id']=='F1','Kaolinite correction lineage differs')
sourcefolders=['round74-cdte','round74-clays','round74-phosphates','round74-sulfides'];sourcejson=[]
for folder in sourcefolders:
 ps=list((W/'research/sources'/folder).glob('*.json'));need(ps,'Missing source dossier '+folder)
 for p in ps:need(p.with_suffix('.md').is_file(),'Missing source MD pair '+str(p))
 sourcejson.extend(ps)
rawroots=[T/n for n in ['cmm-round74-pv-research','cmm-round74-clays-research','cmm-round74-phosphates-research','cmm-round74-sulfides-research','cmm-round74-cdte-independent','cmm-round74-clays-peer','cmm-round74-phosphates-independent','cmm-round74-sulfides-review']];rawfiles={p for r in rawroots for p in walk_files(r) if p.is_file()}
for obj in [*[json.loads(p.read_text()) for p in sourcejson],*[v for p,v in reviews if 'round74' in v['review_id']]]:
 for x in objects(obj):
  if isinstance(x,str):
   for st in re.findall(r'/private/tmp/[A-Za-z0-9_./-]+',x):
    p=Path(st.rstrip('.'))
    if p.is_file():rawfiles.add(p)
byhash={}
for p in rawfiles:byhash.setdefault(sha(p),[]).append(p)
primary=[]
for p,v in reviews:
 if 'round74' not in v['review_id']:continue
 for e in v.get('evidence',[]):
  if e['kind']!='primary_source':continue
  h=e.get('snapshot_sha256');need(isinstance(h,str) and re.fullmatch('[0-9a-f]{64}',h) and h!=hashlib.sha256(b'').hexdigest(),'Hashless/empty primary evidence '+v['review_id']+':'+e['evidence_id']);found=byhash.get(h,[])
  if e['reference'].startswith('/private/tmp/'):
   p=Path(e['reference']);need(p.is_file() and sha(p)==h,'Explicit primary path/hash mismatch');found=[p]
  need(found,'No actual raw primary artifact for '+v['review_id']+':'+e['evidence_id'])
  for p in found:
   need(p.stat().st_size>0,'Empty primary file')
   if p.suffix.lower()=='.pdf':need(p.read_bytes().startswith(b'%PDF-'),'Primary PDF is HTML/failure')
  primary.append({'review':v['review_id'],'evidence_id':e['evidence_id'],'reference':e['reference'],'sha256':h,'local_artifacts':[bind(p) for p in sorted(found)]})
need({yaml.safe_load((W/x['review']).read_text())['review_id'] for x in manifest['records_changed']} <= {x['review'] for x in primary},'Selected review lacks actual primary binding')
# Explicit immutable operational lineage, no latest-wins selection.
initialp=T/'cmm-round74-helper-peer-20261014T145607Z.json';successorp=T/'cmm-round74-helper-peer-20261014T145922Z-successor.json';addendump=T/'cmm-round74-helper-peer-20261014T150011Z-afterfix-binding.json';initial=json.loads(initialp.read_text());successor=json.loads(successorp.read_text());addendum=json.loads(addendump.read_text())
need(initial['passed'] is False and {f['id'] for f in initial['findings']}=={'OP1','OP2'},'Missing initial operational defects');need(successor['passed'] is True and successor['issue']==241 and all(f['status']=='resolved' for f in successor['findings']),'Operational corrections not resolved');need(addendum['passed'] is True and addendum['issue']==241,'Missing current afterfix helper binding')
operational=[retained(p) for p in [initialp,successorp,addendump]]
for f in successor['findings']:need(f['previous_occurrence']['audit_sha256']==sha(initialp) and f['previous_occurrence']['finding']==f['id'],'Wrong OP predecessor')
need(addendum['prior_successor']['sha256']==sha(successorp),'Afterfix predecessor changed')
for observation in [initial,successor,addendum]:
 for f in observation['files']:
  snapshot=Path(f['snapshot']);need(sha(snapshot)==f['sha256'],'Historical helper snapshot changed');retained(snapshot)
for f in addendum['files']:need(sha(Path(f['path']))==f['sha256'],'Current corrected helper changed')
for f in successor['unchanged_helpers']:need(sha(Path(f['path']))==f['sha256'],'Unreviewed helper change')
oldhost=Path(next(f['snapshot'] for f in initial['files'] if f['path'].endswith('hosted-audit-paginated.py')));newhost=T/'cmm-round74-hosted-audit-paginated.py';need(oldhost.read_text().replace('Round73 reuses','Round74 reuses')==newhost.read_text(),'OP2 diff exceeds reviewed correction')
regp=T/'cmm-round74-audit-contract-regression-20261014T145834Z.json';reg=json.loads(regp.read_text());need(reg['passed'] is True and reg['case_count']==29 and all(x['passed'] for x in reg['cases']),'Actual guard regressions failed');fixture=Path(reg['fixture_source']);need(sha(fixture)==reg['fixture_source_sha256'],'Fixture source changed');retained(regp);retained(fixture)
func=lambda s:ast.dump(next(n for n in ast.parse(s).body if isinstance(n,ast.FunctionDef) and n.name=='require_final_audit'),include_attributes=False)
tested=Path(next(f['snapshot'] for f in successor['files'] if f['path'].endswith('commit.py')));current=T/'cmm-round74-commit.py';need(sha(tested)==reg['helper_sha256'] and func(tested.read_text())==func(current.read_text()),'Current guard differs from actual tested AST');need("['final-gates-afterfix','review-check-final','local-coverage']" in current.read_text(),'Commit does not require corrected gates')
helpers=[]
for name in ['commit','open-pr','post-review','enqueue','cleanup','sync-main','isolated-coverage','isolated-verification','hosted-audit-paginated','review-check-final','affected-gates']:
 p=T/f'cmm-round74-{name}.py';ast.parse(p.read_text());helpers.append(retained(p))
helpers.append(retained(T/'cmm-round57-recover-original.py'))
# This exact auditor must be independently peer-read before invocation.
peerp=T/'cmm-round74-package-auditor-peer.json';peer=json.loads(peerp.read_text());need(peer['passed'] is True and not any(f.get('status','open') not in ['resolved','rejected','accepted_risk'] for f in peer.get('findings',[])),'Auditor peer has unresolved findings');entries=peer['files'];need(any(Path(x['path'])==Path(__file__) and x['sha256']==sha(Path(__file__)) for x in entries),'No independent exact auditor peer')
for x in entries:need(sha(Path(x['path']))==x['sha256'],'Peer-reviewed final input changed: '+x['path'])
operational.append(retained(peerp));helpers.append(retained(Path(__file__)))
readme=(W/'README.md').read_text();need('currently contains 354 material records' in readme and all(f'data/records/{s}.yaml' in readme for s in SLUGS),'README current count/owner links')
index=json.loads((W/'pages/index.json').read_text());need(len(index)==354,'Generated index census');pages=[]
for s in sorted(SLUGS):
 o=yaml.safe_load((W/f'data/records/{s}.yaml').read_text());p=W/f'pages/materials/{s}.html';text=' '.join(html.unescape(re.sub('<[^>]+>',' ',p.read_text())).split());prose=[o['description']]
 for m in o.get('mechanisms',[]):prose.extend([m['description'],m['context']]+[x['explanation'] for x in m['evidence']])
 need(all(' '.join(x.split()) in text for x in prose),'Rendered prose mismatch '+s);matches=[x for x in index if x['slug']==s];need(len(matches)==1 and matches[0]['material_kind']==o['material_kind'] and matches[0]['mechanisms_count']==len(o.get('mechanisms',[])),'Index mismatch '+s);pages.append(bind(p))
body=T/'cmm-round74-pr-body.md';bt=body.read_text();need('347 to 354' in bt and '#240' in bt,'PR scope/source follow-up');need(all(re.search(r'(?i)\bfixes\s+#'+str(n)+r'\b',bt) for n in [241,242]),'Missing corrective issue closure instructions')
# Premerge issues intentionally remain open until the reviewed PR merges.
def live_issue(n):return json.loads(subprocess.check_output(['gh','issue','view',str(n),'--repo','CultureBotAI/CMMMech','--json','number,state,title,url,closedAt'],text=True))
with ThreadPoolExecutor(max_workers=3) as ex:issues=list(ex.map(live_issue,[240,241,242]))
need(all(i['state']=='OPEN' for i in issues),'Premerge issue state differs from declared policy')
# Current integration report is an independently acquired snapshot, not inherited assertions.
integrationp=PUB/'20261014T150827Z-integration-current.json';d=json.loads(integrationp.read_text());need(d['passed'] is True and d['verdict']=='pass_with_limitations' and d['base']==BASE and d['worktree']==str(W),'Integration scope mismatch');need(d['pin']==d['live_claw_main']==(W/'scripts/.vendored_canon_ref').read_text().strip(),'Current authority pin mismatch')
for e in d['evidence']:
 p=Path(e['path']);need(p.is_file() and p.stat().st_size==e['bytes'] and sha(p)==e['sha256'],'Integration evidence changed '+str(p))
need(d['admission']['claw_pr581_merged'] is True and d['admission']['claw580_state']=='closed' and d['admission']['cmmmech3_state']=='closed','Admission/convergence status mismatch')
g=d['governed_artifacts'];need(g['count']==22 and g['supported_checker']['exit_code']==0 and g['supported_checker']['passed'] is True,'Supported governed check failed');need(sha(Path(g['supported_checker']['log']))==g['supported_checker']['log_sha256'],'Governed log mismatch');receipts.append(retained(Path(g['supported_checker']['log'])))
for f in g['independent_manifest_comparison']['files']:need(f['passed'] is True and sha(W/f['path'])==f['sha256']==f['expected_sha256'] and format((W/f['path']).stat().st_mode&0o7777,'04o')==f['mode']==f['expected_mode'],'Governed bytes/mode mismatch')
q=d['queue']['ruleset'];rules={r['type']:r.get('parameters',{}) for r in q['rules']};need(q['enforcement']=='active' and q['bypass_actors']==[] and q['conditions']['ref_name']=={'exclude':[],'include':['refs/heads/main']},'Queue scope/bypass mismatch');need(rules['merge_queue']['merge_method']=='SQUASH' and rules['merge_queue']['grouping_strategy']=='ALLGREEN' and rules['merge_queue']['max_entries_to_merge']==1,'Queue method mismatch');need(rules['required_status_checks']['required_status_checks']==[{'context':'validate-strict','integration_id':15368}],'Required CI identity mismatch')
need(any(r['type']=='merge_queue' and r['parameters']['merge_method']=='SQUASH' and r['parameters']['grouping_strategy']=='ALLGREEN' for r in d['queue']['effective_main']),'Effective native queue absent')
priorrun=d['queue']['actual_merge_group'];need(priorrun['head_sha']==BASE and priorrun['event']=='merge_group' and priorrun['conclusion']=='success','Actual current-base queue evidence mismatch')
need(d['shepherd']['queried_total_run_count']==0 and d['shepherd']['model_oauth_runtime_verified'] is False,'Shepherd runtime incorrectly promoted');need(any(f['priority']=='concrete_profile_reconciliation' for f in d['followups']),'Page-profile contradiction omitted');need(d['native_history']['installed'] is True and d['native_history']['shared_generic_curation_enabled'] is False,'Native/shared history scopes confused');receipts.append(retained(integrationp))
p=T/'cmm-round74-preservation-precommit.json';pres=json.loads(p.read_text());initp=T/'cmm-round74-preservation-before.json';init=json.loads(initp.read_text());need(pres['passed'] is True and pres['entry_counts']=={k:len(v['files']) for k,v in init['snapshots'].items()},'Preservation snapshot scope mismatch');need(pres['snapshot_library_sha256']==sha(T/'cmm-round57-recover-original.py'),'Preservation library changed');receipts.append(retained(p));preservation_initial=bind(initp)
working=[{'path':n,'sha256':sha(W/n)} for n in sorted(initial_names)];need(candidates()==initial_names and all(x['sha256']==initial_hashes[x['path']] for x in working),'Working package changed during audit');need(sha(cfgp)==cfg_start,'Config changed during audit');need(git('rev-parse','HEAD')==BASE and git('branch','--show-current')==BRANCH and not git('diff','--cached','--name-only'),'Git state changed during audit')
report={'started_at':started,'finished_at':now(),'reviewer':ME,'authorship':'Operational peer of root publication. Authored marcasite and violarite, independently accepted by a different agent; their science is not self-accepted here. Independently reviewed root CdTe owner. Authored temporary audit-contract fixtures and this auditor, which received a separate exact-source peer read.','base':BASE,'branch':BRANCH,'state':'working_tree','passed':True,'verdict':'pass_with_limitations','unresolved_corrective_findings':0,'counts':actual,'issues':cfg['issues'],'findings':[],'working_inputs':working,'final_scientific_reviews':final,'resolution_lineages':resolutions,'primary_source_bindings':primary,'terminal_receipts':receipts,'operational_review_chain':operational,'helper_bindings':helpers,'generated_pages':pages,'live_issues':issues,'issue_disposition':'Corrective241/242 implemented and independently verified; intentionallyOPEN premerge and closed by explicitPRFixes. Source240 staysOPEN.','prepared_pr_body':bind(body),'manifest':bind(manifestp),'auditor':bind(Path(__file__)),'preservation_initial':preservation_initial,'integration_followups':d['followups'],'limitations':['Exact local package audit only. Hosted review/preflight, nativequeue, actualmerge tree/soleparent, allfive hostedworkflow/jobs, branchdeletion, freshmain validation and preservationcloseout remain subsequent gates.','Complete sourcebytes are bound to independent scientific reviews; this operational audit is not a second full experiment reassessment for all seven owners.','Source inventory is bounded to namedround74 rawroots and exact referencedartifacts, with hidden/ignored-inclusive traversal and symlinkcycleprevention. No global source-exhaustion claim.','Baseline and finalchecks were actually executed thisround. Initial finalgates remain historical; correctedcurrentgate409histories is required beforecommit.']}
out=AUDIT_OUT;md=out.with_suffix('.md');need(not out.exists() and not md.exists(),'Final artifact collision')
with out.open('x') as f:f.write(json.dumps(report,indent=2)+'\n')
text=f'''# Round74 final local publication audit\n\nUTC: {report['finished_at']}. Verdict: pass with limitations; zero unresolved corrective findings. Base `{BASE}`, branch `{BRANCH}`, working-tree state.\n\nThe package contains354records,409history sessions,423native reviews and75available review bases. Every current record has a completed positive exact-byte scientific review. The seven new owners have independent final reviews; kaoliniteF1 explicitly resolves its initial observation. OperationalOP1/OP2 retain immutable initial snapshots, the tested guard correction and the subsequent after-fix receipt binding.\n\nIssues241/242 remain open before merge, with completed verified fixes and explicit PR closure instructions. Source follow-up240 remains open. Current live states were checked.\n\nVerified {len(working)} exact candidate inputs, complete manifest coverage, actual baseline/initial/after-fix checks, final native review checker, complete current coverage, retained helper/source hashes, {len(primary)} nonempty primary-evidence bindings, generated scientific prose, integration evidence and preservation receipt.\n\nThe reviewer authored marcasite and violarite; their scientific acceptance comes from another reviewer. The reviewer independently assessed root-authored CdTe. This operational auditor received a separate exact-source peer review.\n\nPublication still requires exact-head hosted review, isolated squash preflight, queue and actual merge verification, all five successful hosted workflows/jobs, branch cleanup, fresh-main checks and preservation closeout. The JSON companion binds all evidence and limits.\n'''
with md.open('x') as f:f.write(text)
print(json.dumps({'audit':str(out),'sha256':sha(out),'markdown':str(md),'working_inputs':len(working),'primary_bindings':len(primary),'counts':actual},indent=2))
