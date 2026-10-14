"""Independent bounded round77 local publication audit. Reads Git/GitHub; writes only final pair."""
from pathlib import Path
from datetime import datetime,timezone
import ast,hashlib,json,os,re,runpy,subprocess,yaml
W=Path('/private/tmp/CMMMech-expansion-round77-20261014');T=Path('/private/tmp');PUB=W/'reviews/publication/20261014-round77'
BASE='e5e70cfc93a3aa68a166eba7bbbd3dc1053ce60d';BRANCH='curate/cmm-expansion-round77-20261014';ME='codex /root/round68_iron_sulfides'
OUT=None # Read only the coordinator-reserved destination from current config.
EXPECTED={'acanthite':'20261014T172858Z-acanthite-round77-independent','monetite':'20261014T172811Z-monetite-round77-independent','switzerite':'20261014T172811Z-switzerite-round77-independent','spent-tantalum-capacitors':'20261014T172838Z-spent-tantalum-capacitors-round77-independent'}
COUNTS={'record_count':368,'history_count':423,'structured_review_count':437,'review_base_count':78,'covered_records':368}
ISSUES={'corrected_review_issues':[254],'closed_source_issues':[],'open_source_issues':[253]}

def need(c,m):
 if not c:raise AssertionError(m)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def now():return datetime.now(timezone.utc).isoformat()
def git(*args):return subprocess.check_output(['git','-C',str(W),*args],text=True).strip()
def candidates():
 raw=subprocess.check_output(['git','-C',str(W),'diff','--name-only','-z'])+subprocess.check_output(['git','-C',str(W),'ls-files','--others','--exclude-standard','-z'])
 return {os.fsdecode(p) for p in raw.split(b'\0') if p}
def walk(root):
 out=[];seen=set()
 for d,dirs,files in os.walk(root,followlinks=True):
  q=Path(d).resolve()
  if q in seen:dirs[:]=[];continue
  seen.add(q);out.extend(Path(d)/n for n in files)
 return sorted(out)
def objects(x):
 yield x
 if isinstance(x,dict):
  for v in x.values():yield from objects(v)
 elif isinstance(x,list):
  for v in x:yield from objects(v)
def bind(p):return {'path':str(p),'sha256':sha(p),'bytes':Path(p).stat().st_size}
started=now();cfgp=T/'cmm-round77-helper-config.json';cfg=json.loads(cfgp.read_text());cfgsha=sha(cfgp);OUT=Path(cfg['publication_peer_review']);need(OUT.parent==PUB and OUT.name.endswith('-publication-final.json'),'Invalid reserved audit destination')
need(Path(cfg['publication_peer_review'])==OUT and not OUT.exists() and not OUT.with_suffix('.md').exists(),'Audit destination already exists or differs')
need(cfg['base']==BASE and cfg['branch']==BRANCH and cfg['counts']==COUNTS and cfg['issues']==ISSUES and set(cfg['slugs'])==set(EXPECTED) and len(cfg['slugs'])==4,'Cohort/config changed')
need(git('rev-parse','HEAD')==BASE and git('branch','--show-current')==BRANCH and not git('diff','--cached','--name-only'),'Wrong base/branch or staged inputs')
subprocess.run(['git','-C',str(W),'diff','--check'],check=True)
names=candidates();need(names,'Empty package');need(all((W/n).is_file() and not (W/n).is_symlink() for n in names),'Deleted/symlink candidate')
hashes={n:sha(W/n) for n in names}
allowed=lambda n:n in ['README.md','research/ingests/round77-frontier-20261014.json','research/ingests/round77-frontier-20261014.md'] or n.startswith(('pages/','reviews/structured/','reviews/publication/20261014-round77/','research/sources/round77-','research/ingests/round77-checks-20261014/')) or n in ['data/records/'+s+'.yaml' for s in EXPECTED] or any(n.startswith('history/records/'+s+'/') for s in EXPECTED)
need(all(allowed(n) for n in names),'Unscoped schema/governance/code candidate')
need({n for n in names if n.startswith('data/records/')}=={'data/records/'+s+'.yaml' for s in EXPECTED},'Changed owner set differs')
need({n for n in names if n.startswith('reviews/structured/')}=={'reviews/structured/'+v+'/review.'+ext for v in EXPECTED.values() for ext in ['yaml','md']},'Unplanned historical/scientific review change')
manifestp=W/'research/ingests/round77-frontier-20261014.json';manifest=json.loads(manifestp.read_text())
need(manifest['base']==BASE and manifest['branch']==BRANCH and manifest['state']=='working_tree' and manifest['counts']==COUNTS and manifest['issues']==ISSUES,'Manifest identity differs')
mpaths=[x['path'] for x in manifest['pre_manifest_inputs']];excluded={str(manifestp.relative_to(W)),str(manifestp.with_suffix('.md').relative_to(W))}
need(len(mpaths)==len(set(mpaths)) and set(mpaths)==names-excluded,'Manifest candidate coverage incomplete or duplicate')
for x in manifest['pre_manifest_inputs']:need(sha(W/x['path'])==x['sha256'],'Manifest stale: '+x['path'])
package_by_hash={}
for n,h in hashes.items():package_by_hash.setdefault(h,[]).append(n)
def retained(p):
 need(Path(p).is_file() and Path(p).stat().st_size>0,'Missing external evidence '+str(p));need(sha(p) in package_by_hash,'Evidence not retained: '+str(p));return dict(bind(p),retained_paths=package_by_hash[sha(p)])
receipts=[]
for label in ['baseline','final-gates','review-check-final','local-coverage','vendored-check','preservation-precommit']:
 p=T/f'cmm-round77-{label}.json';d=json.loads(p.read_text());need(d.get('passed',d.get('exit_code')==0) is True,'Failed gate '+label);receipts.append(retained(p))
 if 'log' in d:
  lp=Path(d['log']);need(sha(lp)==d['log_sha256'],'Gate/log mismatch '+label);receipts.append(retained(lp))
 if label=='baseline':
  need(d['base']==BASE and d['worktree']==str(W) and [x['command'] for x in d['commands']]==[['uv','sync','--quiet','--locked','--extra','dev','--offline'],['just','check']] and all(x['exit_code']==0 for x in d['commands']),'Baseline not newly executed expected commands')
  need('317 passed, 3 skipped' in lp.read_text() and 'Checked 364 record(s); 0 failed.' in lp.read_text() and 'Checked 419 history record(s); 0 error(s).' in lp.read_text(),'Baseline counts differ')
 if label=='final-gates':
  need(d['base']==BASE and d['worktree']==str(W) and d['inputs_unchanged'] is True,'Final gate provenance')
  expected=[['just','check'],['uv','run','--locked','cmmmech','validate','--require-records'],['uv','run','--locked','cmmmech','validate-history','--base',BASE],['uv','run','--locked','python','scripts/render_pages.py','--check']]
  need([x['command'] for x in d['commands']]==expected and all(x['exit_code']==0 for x in d['commands']),'Final four-command gate incomplete')
  need('317 passed, 3 skipped' in lp.read_text() and 'Checked 368 record(s); 0 failed.' in lp.read_text() and 'Checked 423 history record(s); 0 error(s).' in lp.read_text() and 'pages/ is current' in lp.read_text(),'Final log differs')
  for n,h in d['record_inputs'].items():need(sha(W/n)==h,'Postgate scientific change '+n)
 if label=='review-check-final':need(d['worktree']==str(W) and d['command']==['just','review-check','--base',BASE,'--require-reviews'] and '437' in lp.read_text(),'Structured review gate identity/count differs')
 if label=='local-coverage':need(all(d[k]==v for k,v in COUNTS.items()) and all(x['available_commit'] for x in d['bases']),'Local coverage receipt differs')
 if label=='vendored-check':need(d['command']==['bash','scripts/check_vendored_sync.sh'] and '22' in lp.read_text(),'Governed checker differs')
 if label=='preservation-precommit':
  need(d['base']==BASE and d['snapshots_match'] is True and d['retained_tag_match'] is True and sha(Path(d['original_snapshot']))==d['original_snapshot_sha256'],'Preservation receipt unbound')
  preservation=d
records=[p for p in walk(W/'data/records') if p.suffix in ['.yaml','.yml']];histories=[p for p in walk(W/'history/records') if p.suffix in ['.yaml','.yml']];reviews=[(p,yaml.safe_load(p.read_text())) for p in walk(W/'reviews/structured') if p.name=='review.yaml'];bases={v['source']['git_revision'] for p,v in reviews};coverage={}
for p in records:
 d=yaml.safe_load(p.read_text());rp=str(p.relative_to(W));h=sha(p);matches=[]
 for q,v in reviews:
  if v.get('scientific_review') is True and v.get('completion')=='completed' and v.get('verdict') in ['pass','pass_with_limitations'] and d['id'] in v.get('scope',{}).get('reviewed_target_ids',[]) and any(t['path']==rp and t['target_id']==d['id'] for t in v['targets']) and any(i['path']==rp and i['sha256']==h for i in v['source']['inputs']):matches.append(str(q.relative_to(W)))
 need(matches,'No exact positive scientific coverage '+rp);coverage[rp]=matches
actual={'record_count':len(records),'history_count':len(histories),'structured_review_count':len(reviews),'review_base_count':len(bases),'covered_records':len(coverage)};need(actual==COUNTS,'Actual hidden/ignored-inclusive census differs')
for rev in bases:need(git('cat-file','-t',rev)=='commit','Missing retained review base '+rev)
need({n for n in names if n.startswith('history/records/')}=={h for x in manifest['records'] for h in x['history_refs']},'Unexpected history edit')
need(len(manifest['records'])==4 and {x['slug'] for x in manifest['records']}==set(EXPECTED),'Manifest four-owner set differs')
final=[];selected=[]
for x in manifest['records']:
 slug=x['slug'];rp='data/records/'+slug+'.yaml';q=W/('reviews/structured/'+EXPECTED[slug]+'/review.yaml');v=yaml.safe_load(q.read_text());d=yaml.safe_load((W/rp).read_text())
 need(x['path']==rp and x['sha256']==sha(W/rp) and x['id']==d['id'] and x['material_kind']==d['material_kind'],'Owner manifest mismatch '+slug)
 need(x['review']['path']==str(q.relative_to(W)) and x['review']['review_sha256']==sha(q) and x['review']['verdict']==v['verdict'],'Selected review mismatch '+slug)
 need(str(q.relative_to(W)) in coverage[rp] and v['review_id']==EXPECTED[slug] and v['reviewer']['independence']=='independent','Wrong independent scientific observation '+slug)
 need(v['source']['git_revision']==BASE and v['source']['state']=='working_tree' and not v['findings'],'Unexpected current science findings/provenance '+slug)
 need([p for p in coverage[rp] if 'round77' in p]==[str(q.relative_to(W))],'Ambiguous current-round positive selection '+slug)
 if slug=='acanthite':need(v['reviewer']['identity']!=ME,'Own acanthite lacks separate scientific acceptance')
 need(x['history_refs']==d['history_refs'] and len(d['history_refs'])==1,'History scope differs')
 for h in d['history_refs']:
  hv=yaml.safe_load((W/h).read_text());need(hv['target']['path']==rp and hv['target']['slug']==slug and hv['events'][0]['type']=='CREATE','History owner/type differs')
  need(any(i['path']==h and i['sha256']==sha(W/h) for i in v['source']['inputs']),'Selected review lacks exact history')
 for i in v['source']['inputs']:need(sha(W/i['path'])==i['sha256'],'Selected review input changed')
 need(all(c['status']=='passed' for c in v['checks'] if c.get('required')),'Selected scientific required check not passed')
 final.append({'record':rp,'sha256':sha(W/rp),'review':str(q.relative_to(W)),'review_sha256':sha(q),'reviewer':v['reviewer'],'verdict':v['verdict']});selected.append(v)
sourcejson=[]
for folder in ['round77-sulfides','round77-phosphates','round77-resources','round77-silicate-leads']:
 ps=list((W/'research/sources'/folder).glob('*.json'));need(ps and all(p.with_suffix('.md').is_file() for p in ps),'Missing source paired dossier '+folder);sourcejson+=ps
rawroots=[T/'cmm-round77-sulfides-research',T/'cmm-round77-phosphates-research',T/'cmm-round77-phosphates-independent',T/'cmm-round77-resources-research',T/'cmm-round77-capacitor-independent',T/'cmm-round77-acanthite-review',T/'cmm-round10-nb-ta-raw',T/'cmm-round68-phosphates-research']
raw={p for root in rawroots for p in walk(root) if p.is_file()}
for obj in [*[json.loads(p.read_text()) for p in sourcejson],*selected]:
 for value in objects(obj):
  if isinstance(value,str):
   for s in re.findall(r'/private/tmp/[A-Za-z0-9_./-]+',value):
    p=Path(s.rstrip('.'))
    if p.is_file():raw.add(p)
byhash={}
for p in raw:
 if p.stat().st_size>0:byhash.setdefault(sha(p),[]).append(p)
primary=[]
for v in selected:
 for e in v['evidence']:
  if e['kind']!='primary_source':continue
  h=e.get('snapshot_sha256');need(isinstance(h,str) and re.fullmatch('[a-f0-9]{64}',h) and h!=hashlib.sha256(b'').hexdigest(),'Empty/hashless primary '+v['review_id'])
  found=byhash.get(h,[]);need(found,'Primary source hash has no actual nonempty raw artifact '+v['review_id']+':'+e['evidence_id'])
  if e['reference'].startswith('/private/tmp/'):need(Path(e['reference']) in found,'Explicit primary URI/hash mismatch')
  for rawpath in re.findall(r'/private/tmp/[A-Za-z0-9_./-]+',e.get('locator','')):
   p=Path(rawpath.rstrip('.'));need(p.is_file() and sha(p)==h,'Explicit primary locator/hash mismatch '+str(p))
  for p in found:
   if p.suffix.lower()=='.pdf':need(p.read_bytes().startswith(b'%PDF-'),'Claimed PDF is not PDF')
  primary.append({'review':v['review_id'],'evidence_id':e['evidence_id'],'reference':e['reference'],'sha256':h,'artifacts':[bind(p) for p in sorted(found)]})
need({v['review_id'] for v in selected} <= {x['review'] for x in primary},'Review missing bound full primary')

# Static helper assessment, original snapshots and exact derivation remain immutable.
staticp=PUB/'20261014T172217Z-helper-static.json';static=json.loads(staticp.read_text())
need(static['passed'] is True and type(static['unresolved_corrective_findings']) is int and static['unresolved_corrective_findings']==0 and not static['findings'],'Static helper acceptance differs')
need(static['base']==BASE and static['branch']==BRANCH,'Static helper base differs')
helper_bindings=[]
for f in static['files']:
 p=Path(f['path']);need(sha(p)==f['sha256'],'Current helper no longer matches static review: '+str(p));retained(p)
 if p.suffix=='.py':ast.parse(p.read_text())
 if 'snapshot' in f:
  snap=Path(f['snapshot']);need(sha(snap)==f['snapshot_sha256']==f['sha256'],'Original helper snapshot changed');retained(snap)
 else:need(p.name=='cmm-round77-helper-derivation.json','Unexpected snapshot-less helper')
 helper_bindings.append(bind(p))
derivationp=T/'cmm-round77-helper-derivation.json';derivation=json.loads(derivationp.read_text())
need(len(derivation['helpers'])==11,'Helper derivation census differs')
for row in derivation['helpers']:
 p=Path(row['source']);q=Path(row['target']);need(sha(p)==row['source_sha256'] and sha(q)==row['target_sha256'],'Derivation bytes changed')
 expected=p.read_text().replace('round76','round77').replace('Round76','Round77').replace('925a93db824261d146a14900b8367c88d25cbd71',BASE)
 if q.name=='cmm-round77-final-gates.py':expected=expected.replace('== 364','== 368')
 need(q.read_text()==expected,'Undeclared operational helper change '+str(q))
libp=T/'cmm-round57-recover-original.py';retained(libp)
need(sha(PUB/'helper-tools/config.prepublication.json')==cfgsha,'Retained current configuration mismatch')
builderp=T/'cmm-round77-write-manifest.py';retained(builderp);ast.parse(builderp.read_text());builder_binding=bind(builderp)
# Later hosted-review draft prose correction, saved before any actual hosted execution.
hpinitialp=PUB/'cmm-round77-hosted-helper-static-20261014T173103Z.json';hpinitial=json.loads(hpinitialp.read_text())
hpsuccessorp=PUB/'cmm-round77-hosted-helper-static-successor-20261014T173143Z.json';hpsuccessor=json.loads(hpsuccessorp.read_text())
need(hpinitial['passed'] is False and len(hpinitial['findings'])==1 and hpinitial['findings'][0]['finding_id']=='HP1' and hpinitial['findings'][0]['issue_key']=='round77-hosted-comment-invented-correction-lineage','HP1 initial occurrence differs')
need(hpsuccessor['passed'] is True and type(hpsuccessor['unresolved_corrective_findings']) is int and hpsuccessor['unresolved_corrective_findings']==0 and not hpsuccessor['findings'] and hpsuccessor['initial_review_sha256']==sha(hpinitialp),'HP1 successor does not bind initial')
need(len(hpsuccessor['resolutions'])==1 and hpsuccessor['resolutions'][0]['finding_id']=='HP1' and hpsuccessor['resolutions'][0]['issue_key']==hpinitial['findings'][0]['issue_key'] and hpsuccessor['resolutions'][0]['disposition']=='resolved','HP1 resolution identity differs')
for row in hpsuccessor['files']:
 p=Path(row['path']);old=Path(row['snapshot']);need(sha(p)==row['after_sha256'] and sha(old)==row['before_sha256'],'HP1 source bytes changed');retained(p);retained(old)
 if p.name=='cmm-round77-hosted-peer.py':need(old.read_text().replace('explicit operational-review correction lineage','retained static operational-review evidence')==p.read_text(),'HP1 main correction exceeds literal')
 else:need(p.name=='cmm_round77_peer_checks.py' and ast.dump(ast.parse(old.read_text()),include_attributes=False)==ast.dump(ast.parse(p.read_text()),include_attributes=False),'HP1 module changed executable behavior')
hpissuep=T/'cmm-round77-hp1-issue-created.json';hpissue=json.loads(hpissuep.read_text());retained(hpissuep)
need(hpissue['issue']==254 and 'HP1' in hpissue['body'] and 'cmm-round77-hosted-helper-static-20261014T173103Z' in hpissue['body'],'HP1 issue does not link exact occurrence')
# Reject accidental acceptance of the HTML-challenge named PDF for acanthite.
ac=next(v for v in selected if v['review_id']==EXPECTED['acanthite'])
need(next(e for e in ac['evidence'] if e['evidence_id']=='primary')['snapshot_sha256']==sha(T/'cmm-round77-sulfides-research/klaus1999.html'),'Acanthite primary is not actual complete HTML')
failed=T/'cmm-round77-sulfides-research/klaus1999.pdf';need(not failed.read_bytes().startswith(b'%PDF-') and sha(failed) not in [e['snapshot_sha256'] for e in ac['evidence'] if e['kind']=='primary_source'],'Failed PDF accepted as evidence')
for i in range(1,4):need(next(e for e in ac['evidence'] if e['evidence_id']=='figure'+str(i))['snapshot_sha256']==sha(T/f'cmm-round77-sulfides-research/figure{i}.jpg'),'Acanthite original figure mismatch')
# Independently recheck all claimed source artifact hashes, including primary/authority JSON inventory entries.
dossier_bindings=[]
for p in sourcejson:
 for obj in objects(json.loads(p.read_text())):
  if not isinstance(obj,dict):continue
  ref=next((obj[k] for k in ['path','file','artifact'] if isinstance(obj.get(k),str) and obj[k].startswith('/private/tmp/')),None)
  h=obj.get('sha256')
  if ref and isinstance(h,str) and re.fullmatch('[a-f0-9]{64}',h):
   q=Path(ref);need(q.is_file() and sha(q)==h,'Dossier artifact binding mismatch '+ref);dossier_bindings.append(bind(q))
# A source lead dossier makes no claim that incomplete acquisition satisfies curation.
lead=(W/'research/sources/round77-silicate-leads/20261014T171632Z.md').read_text()
need('Referenced raw-download searches remain incomplete' in lead and 'novelty is provisional' in lead,'Silicate discovery limitations lost')
# Independently repeat read-only original checkout and unrelated skill snapshots.
lib=runpy.run_path(str(libp),run_name='snapshot_library');before=json.loads(Path(preservation['original_snapshot']).read_text())
for label,include in [('main',False),('skill',True)]:need(lib['snapshot'](Path(before['snapshots'][label]['path']),include)==before['snapshots'][label],'Preservation changed '+label)
need(lib['retained_tag']()==before['retained_tag'],'Retained review-base tag changed')
issue_states=[]
for num,receipt in [(253,T/'cmm-round77-hospital-issue-created.json'),(254,hpissuep)]:
 created=json.loads(receipt.read_text());retained(receipt)
 d=json.loads(subprocess.check_output(['gh','api',f'repos/CultureBotAI/CMMMech/issues/{num}'],text=True));need(d['number']==num and d['state']=='open' and not d.get('pull_request'),'Unexpected premerge issue state')
 need(d['title']==created['title'] and d['body']==created['body'] and hashlib.sha256(d['body'].encode()).hexdigest()==created['body_sha256'],'Live issue content changed from retained creation receipt')
 issue_states.append({'number':num,'state':d['state'],'url':d['html_url'],'title':d['title'],'updated_at':d['updated_at'],'body_sha256':created['body_sha256'],'creation_receipt':bind(receipt)})
prbodyp=T/'cmm-round77-pr-body.md';prbody=prbodyp.read_text();need('#253' in prbody and not re.search(r'(?i)(?:fixes|closes|resolves)\s+#253',prbody) and re.search(r'(?i)(?:fixes|closes|resolves)\s+#254',prbody),'PR issue closure/source scope differs')
readme=(W/'README.md').read_text();need('currently contains 368 material records' in readme,'README census stale')
for slug in EXPECTED:need('data/records/'+slug+'.yaml' in readme,'README missing owner')
need('Minority silver-sulfide' in readme and 'cell-free spent broth' in readme and 'Missing culture diffraction' in readme and 'Tantalum nondetection' in readme,'README scope qualification lost')
md=manifestp.with_suffix('.md').read_text();need('#253' in md and '#254' in md and '437' in md and '368/368' in md and '78' in md,'Ingest report issue/count mismatch')
need('not counted as independent replication' in md and 'all 22' in md.lower(),'Report loses lineage or governance scope')
need(candidates()==names and {n:sha(W/n) for n in names}==hashes and sha(cfgp)==cfgsha,'Inputs changed during audit')
finished=now();out={'started_at':started,'finished_at':finished,'path_reserved_at':cfg['publication_audit_path_reserved_at'],'filename_note':'Destination timestamp was reserved before execution; actual audit interval recorded separately.','reviewer':ME,'authorship':'Authored acanthite, independently accepted scientifically by frontier agent. Independently reviewed monetite/switzerite. Operational audit is independent of root-authored manifest/helpers and does not replace own-record independent science.','passed':True,'verdict':'pass_with_limitations','unresolved_corrective_findings':0,'base':BASE,'branch':BRANCH,'state':'working_tree','counts':actual,'issues':ISSUES,'working_inputs':[{'path':n,'sha256':hashes[n]} for n in sorted(names)],'final_scientific_reviews':final,'primary_source_bindings':primary,'source_dossiers':[bind(p) for p in sourcejson],'dossier_artifact_bindings':dossier_bindings,'receipts':receipts,'static_helper_audit':bind(staticp),'hosted_helper_correction':{'initial':bind(hpinitialp),'successor':bind(hpsuccessorp),'issue':254,'disposition':'Resolved before execution; issue remains open for PR-linked closure. Successor predates issue assignment and preserves that timing.'},'current_helper_bindings':helper_bindings,'helper_derivation':bind(derivationp),'configuration':bind(cfgp),'static_timing_qualification':static['timing'],'pr_body':bind(prbodyp),'manifest_builder':builder_binding,'live_issue_states':issue_states,'review_bases':sorted(bases),'preservation':{'fresh_snapshot_match':True,'retained_tag_match':True,'scope':preservation['scope']},'findings':[],'limitations':['No PR CI, committed synthetic-squash preflight, native merge, cleanup or fresh postmerge result is asserted by this precommit audit.','Acanthite authored by this auditor has a separate exact-hash independent scientific review.','Source-specific phase/control/measurement limitations remain in records; issue253 stays open and silicate discovery novelty is explicitly provisional.','Original source PDFs/HTML and graphics remain outside Git; current nonempty bytes are independently bound and no failed placeholder supplies an accepted primary.','Hidden/ignored scientific census and followed symlinks are distinct from exact Git candidate inventory; original-checkout preservation excludes Git administration and external symlink target contents.']}
body=f"""# Independent round77 local publication audit

Verdict: **pass with limitations**. Actual UTC audit interval {started} to {finished}; destination reserved at {cfg['publication_audit_path_reserved_at']}. Base `{BASE}`, branch `{BRANCH}`, state `working_tree`.

The companion JSON binds {len(names)} exact commit candidates, the manifest and prepared PR body. Four frozen owner/history/review links match exact current hashes. All selected independent scientific reviews are qualified passes with no corrective findings. The auditor authored acanthite; its independent scientific acceptance belongs to the frontier reviewer. The auditor independently reviewed monetite and switzerite. Operational review does not self-accept acanthite science.

Actual hidden/ignored-inclusive census:368 records,423 histories,437 structured reviews,78 available review bases and368/368 exact positive scientific coverage. Newly executed baseline, all four final batch commands, full native review checker, current coverage,22-file governed-sync and preservation receipts/logs are checked. No schema, validator, tests or governed artifacts changed.

All {len(primary)} primary evidence entries bind nonempty original bytes. Acanthite uses the complete HTML and three original JPEGs; the named PDF challenge is explicitly excluded. Switzerite hydration/diffraction and natural-versus-synthetic limits, monetite filtered-effluent provenance, and capacitor strain/table/nondetection qualifications remain in owner reviews and README. Shared study lineage is not replication. Paired source dossiers and exact retained acquisition/authority bindings were checked; the silicate handoff explicitly has incomplete original acquisition and raw deduplication.

The generic static helper audit reports no corrective findings. A later independent hosted-helper check found minor HP1: a prepared COMMENT overstated operational correction-lineage review. Original sources and observation were preserved before the two prose-only corrections; the exact successor is independently verified here. Issue254 links HP1 and remains open for PR-linked closure; no COMMENT had been posted with the faulty wording. The generic audit timing qualification, immutable snapshots and exact derivation are preserved; final config and builder are bound here. Source issue253 is verified open and not closed by the PR body. Both live titles and complete bodies match retained creation receipts. Original main and unrelated skill snapshots and retained review-base tag were independently rechecked within their stated scope.

This audit does not assert future hosted review, CI, isolated committed preflight, native queue merge, cleanup or postmerge results. Those remain subsequent publication gates.
"""
OUT.write_text(json.dumps(out,indent=2)+'\n');OUT.with_suffix('.md').write_text(body)
print(json.dumps({'passed':True,'audit':str(OUT),'sha256':sha(OUT),'input_count':len(names),'primary_bindings':len(primary),'counts':actual},indent=2))
