"""Independent round88 precommit audit; writes only its own final JSON/Markdown pair."""
from pathlib import Path
from datetime import datetime, timezone
import ast, hashlib, json, os, re, runpy, subprocess, yaml
W=Path('/private/tmp/CMMMech-expansion-round88-20261015');T=Path('/private/tmp')
BASE='661e752f00ea9ea15e48dfc41f02199dfc16e1fe';BRANCH='curate/cmm-expansion-round88-20261015'
SLUGS={'anhydrite','chromium-tanned-leather-shavings','gersdorffite','gypsum','wulfenite'}
AUTHORS={'anhydrite':'codex /root/round68_phosphates','gypsum':'codex /root/round68_phosphates','chromium-tanned-leather-shavings':'codex /root/round68_new_frontier','gersdorffite':'codex /root/round68_iron_sulfides','wulfenite':'codex /root'}
COUNTS=dict(record_count=422,history_count=483,structured_review_count=500,review_base_count=89,covered_records=422)
ISSUES=None # Actual finalized issue ledger is read and independently checked below.
PUB=W/'reviews/publication/20261015-round88'
def now():return datetime.now(timezone.utc).isoformat().replace('+00:00','Z')
def need(c,m):
    if not c:raise AssertionError(m)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def bind(p):return dict(path=str(p),sha256=sha(p),bytes=Path(p).stat().st_size)
def git(*a):return subprocess.check_output(['git','-C',str(W),*a],text=True).strip()
def walk(root):
    seen=set();out=[]
    for d,dirs,files in os.walk(root,followlinks=True):
        p=Path(d).resolve()
        if p in seen:dirs[:]=[];continue
        seen.add(p);out.extend(Path(d)/x for x in files)
    return sorted(out)
def objects(x):
    yield x
    if isinstance(x,dict):
        for v in x.values():yield from objects(v)
    elif isinstance(x,list):
        for v in x:yield from objects(v)
def candidates():
    b=subprocess.check_output(['git','-C',str(W),'diff','--name-only','-z'])+subprocess.check_output(['git','-C',str(W),'ls-files','--others','--exclude-standard','-z'])
    return {os.fsdecode(x) for x in b.split(b'\0') if x}
started=now();builder_hash=sha(T/'cmm-round88-build-manifest.py');cfgp=T/'cmm-round88-helper-config.json';cfg=json.loads(cfgp.read_text());cfgh=sha(cfgp)
need(cfg['base']==BASE and cfg['branch']==BRANCH and cfg['worktree']==str(W) and set(cfg['slugs'])==SLUGS,'Config identity mismatch')
ISSUES=cfg['issues']
need(cfg['counts']==COUNTS and set(ISSUES)=={'corrected_review_issues','closed_source_issues','open_source_issues'} and ISSUES['corrected_review_issues']==[302,305] and ISSUES['open_source_issues']==[303,304] and not ISSUES['closed_source_issues'],'Final counts/issues not ready')
need(not Path(cfg['publication_peer_review']).exists() and not Path(cfg['publication_peer_review']).with_suffix('.md').exists(),'Existing final audit must be preserved')
need(git('rev-parse','HEAD')==BASE and git('branch','--show-current')==BRANCH and not git('diff','--cached','--name-only'),'Changed base/branch/staging')
subprocess.run(['git','-C',str(W),'diff','--check'],check=True)
names=candidates();need(names and all((W/n).is_file() and not (W/n).is_symlink() for n in names),'Deleted/symlink candidate')
hashes={n:sha(W/n) for n in names}
allowed=lambda n:n in ['README.md','research/ingests/round88-frontier-20261015.json','research/ingests/round88-frontier-20261015.md'] or n.startswith(('pages/','reviews/structured/','reviews/publication/20261015-round88/','research/sources/round88-','research/ingests/round88-checks-20261015/')) or n in {'data/records/'+s+'.yaml' for s in SLUGS} or any(n.startswith('history/records/'+s+'/') for s in SLUGS)
need(all(allowed(n) for n in names),'Out-of-scope candidate')
need({n for n in names if n.startswith('data/records/')}=={'data/records/'+s+'.yaml' for s in SLUGS},'Wrong owner set')
mp=W/'research/ingests/round88-frontier-20261015.json';m=json.loads(mp.read_text())
need(all(m[k]==cfg[k] for k in ['base','branch','worktree','counts','issues']) and m['state']=='working_tree','Manifest provenance mismatch')
# This round's manifest selects owners/reviews and source reports; this audit,
# rather than a claimed pre-manifest inventory, binds every commit candidate.
need(len(m['source_reports'])==len(set(m['source_reports'])) and set(m['source_reports'])=={n for n in names if n.startswith('research/sources/round88-') and n.endswith('.md')},'Source report selection mismatch')
byhash={}
for n,h in hashes.items():byhash.setdefault(h,[]).append(n)
def retained(p):
    need(Path(p).is_file() and Path(p).stat().st_size>0 and sha(p) in byhash,'Not retained '+str(p))
    return dict(bind(p),retained_paths=byhash[sha(p)])
receipts=[]
for label in ['baseline','final-gates','review-check-final','local-coverage','governed-check','preservation-precommit']:
    p=T/f'cmm-round88-{label}.json';d=json.loads(p.read_text())
    need(d.get('passed',d.get('exit_code')==0) is True,'Failed receipt '+label);receipts.append(retained(p))
    if 'log' in d:
        lp=Path(d['log']);need(sha(lp)==d['log_sha256'],'Log hash mismatch '+label);receipts.append(retained(lp));log=lp.read_text()
    if label=='baseline':
        need(d['base']==BASE and d['worktree']==str(W) and [x['command'] for x in d['commands']]==[['uv','sync','--quiet','--locked','--extra','dev','--offline'],['just','check']] and all(x['exit_code']==0 for x in d['commands']),'Wrong baseline')
        need('317 passed, 3 skipped' in log and 'Checked 417 record(s); 0 failed.' in log and 'Checked 477 history record(s); 0 error(s).' in log,'Wrong baseline census')
    if label=='final-gates':
        cmds=[['just','check'],['uv','run','--locked','cmmmech','validate','--require-records'],['uv','run','--locked','cmmmech','validate-history','--base',BASE],['uv','run','--locked','python','scripts/render_pages.py','--check']]
        need(d['base']==BASE and d['worktree']==str(W) and d['inputs_unchanged'] is True and [x['command'] for x in d['commands']]==cmds and all(x['exit_code']==0 for x in d['commands']),'Wrong final gate')
        need('317 passed, 3 skipped' in log and 'Checked 422 record(s); 0 failed.' in log and 'Checked 483 history record(s); 0 error(s).' in log and 'pages/ is current' in log,'Wrong final census')
        need(len(d['record_inputs'])==422,'Final census inputs')
        for n,h in d['record_inputs'].items():need(sha(W/n)==h,'Owner changed after gate '+n)
    if label=='review-check-final':need(d['worktree']==str(W) and d['command']==['just','review-check','--base',BASE,'--require-reviews'] and '"valid_reviews": 500' in log,'Wrong native review gate')
    if label=='local-coverage':need(all(d[k]==v for k,v in COUNTS.items()) and all(x['available_commit'] for x in d['bases']),'Wrong coverage')
    if label=='governed-check':need(d['command']==['bash','scripts/check_vendored_sync.sh'] and '22' in log,'Wrong governed check')
    if label=='preservation-precommit':
        need(d['passed'] is True and sha(d['original_snapshot'])==d['original_snapshot_sha256'],'Wrong preservation');preservation=d
records=[p for p in walk(W/'data/records') if p.suffix in ['.yaml','.yml']]
histories=[p for p in walk(W/'history/records') if p.suffix in ['.yaml','.yml']]
reviews=[(p,yaml.load(p.read_text(),Loader=yaml.CSafeLoader)) for p in walk(W/'reviews/structured') if p.name=='review.yaml']
bases={r['source']['git_revision'] for _,r in reviews};coverage={}
for p in records:
    rec=yaml.load(p.read_text(),Loader=yaml.CSafeLoader);n=str(p.relative_to(W));digest=sha(p);matches=[]
    for q,v in reviews:
        if v.get('scientific_review') is True and v.get('completion')=='completed' and v.get('verdict') in ['pass','pass_with_limitations'] and rec['id'] in v.get('scope',{}).get('reviewed_target_ids',[]) and any(x['path']==n and x['target_id']==rec['id'] for x in v['targets']) and any(x['path']==n and x['sha256']==digest for x in v['source']['inputs']):matches.append(str(q.relative_to(W)))
    need(matches,'No exact positive science '+n);coverage[n]=matches
actual=dict(record_count=len(records),history_count=len(histories),structured_review_count=len(reviews),review_base_count=len(bases),covered_records=len(coverage));need(actual==COUNTS,'Independent census differs')
for b in bases:need(git('cat-file','-t',b)=='commit','Missing base '+b)
need(len(m['records'])==5 and {x['slug'] for x in m['records']}==SLUGS,'Wrong manifest cohort')
selected=[];final=[]
for x in m['records']:
    s=x['slug'];n='data/records/'+s+'.yaml';rec=yaml.load((W/n).read_text(),Loader=yaml.CSafeLoader);q=W/x['review']['path'];v=yaml.load(q.read_text(),Loader=yaml.CSafeLoader);tid='cmmmech:'+s
    need(x['path']==n and x['sha256']==sha(W/n) and x['id']==rec['id']==tid and x['name']==rec['name'],'Wrong owner manifest '+s)
    need(x['review']['sha256']==sha(q) and x['review']['review_id']==v['review_id'] and x['review']['verdict']==v['verdict'] and x['review']['markdown']==str(q.with_suffix('.md').relative_to(W)),'Wrong final review binding '+s)
    need(v['reviewer']['independence']=='independent' and v['source']['git_revision']==BASE and v['source']['state']=='working_tree' and v['scope']['reviewed_target_ids']==[tid],'Wrong review provenance '+s)
    need(len(v['targets'])==1 and v['targets'][0]['target_id']==tid and v['targets'][0]['path']==n,'Wrong canonical target '+s)
    need([z for z in coverage[n] if 'round88' in z]==[str(q.relative_to(W))],'Ambiguous positive review selection '+s)
    need(v['reviewer']['identity']!=AUTHORS[s],'Self-acceptance of authored science '+s)
    need(x['history_refs']==rec['history_refs'] and len(rec['history_refs'])==(2 if s=='wulfenite' else 1),'History count mismatch')
    for i,h in enumerate(rec['history_refs']):
        hv=yaml.load((W/h).read_text(),Loader=yaml.CSafeLoader);need(hv['target']['path']==n and hv['target']['slug']==s and hv['events'][0]['type']==('CREATE' if i==0 else 'EDIT'),'Wrong canonical history')
        need(any(a['path']==h and a['sha256']==sha(W/h) for a in v['source']['inputs']),'History not bound in review')
    for a in v['source']['inputs']:need(sha(W/a['path'])==a['sha256'],'Selected input changed '+a['path'])
    need(all(c['status']=='passed' for c in v['checks'] if c.get('required')),'Required review gate incomplete')
    need(all(f['status'] in ['resolved','rejected'] for f in v['findings']),'Unresolved final finding '+s)
    selected.append(v);final.append(dict(record=n,sha256=sha(W/n),review=str(q.relative_to(W)),review_sha256=sha(q),reviewer=v['reviewer'],verdict=v['verdict']))
expected_reviews={v['review_id'] for v in selected}|{'20261015T051448Z-wulfenite-round88-dose-label-initial'}
need({n for n in names if n.startswith('reviews/structured/')}=={'reviews/structured/'+r+'/review.'+e for r in expected_reviews for e in ['yaml','md']},'Unexpected native bundle edits')
need({n for n in names if n.startswith('history/records/')}=={h for x in m['records'] for h in x['history_refs']},'Unexpected history edit')
primary=[]
for v in selected:
    for e in v['evidence']:
        if e['kind'] not in ['primary_source','authority','database']:continue
        h=e.get('snapshot_sha256');need(isinstance(h,str) and re.fullmatch('[a-f0-9]{64}',h) and h!=hashlib.sha256(b'').hexdigest(),'Missing/empty source hash')
        refs=re.findall(r'/private/tmp/[A-Za-z0-9_./-]+',e.get('locator',''))
        if e['reference'].startswith('/private/tmp/'):refs.append(e['reference'])
        paths={Path(z.rstrip('.')) for z in refs};matches=[p for p in paths if p.is_file() and p.stat().st_size>0 and sha(p)==h]
        need(matches,'No exact source-byte locator '+v['review_id']+'/'+e['evidence_id'])
        for p in matches:
            if p.suffix.lower()=='.pdf':need(p.read_bytes().startswith(b'%PDF-'),'Challenge/nonPDF accepted '+str(p))
        primary.append(dict(review=v['review_id'],evidence_id=e['evidence_id'],kind=e['kind'],reference=e['reference'],sha256=h,artifacts=[bind(p) for p in sorted(matches)]))
need({v['review_id'] for v in selected}<={p['review'] for p in primary if p['kind']=='primary_source'},'No bound primary for cohort target')
sourcejson=[p for p in walk(W/'research/sources') if p.parent.name.startswith('round88-') and p.suffix=='.json']
need(sourcejson and all(p.with_suffix('.md').is_file() for p in sourcejson),'Dossier pairs missing')
bindings=[]
for p in sourcejson:
    for o in objects(json.loads(p.read_text())):
        if not isinstance(o,dict):continue
        ref=next((o[k] for k in ['path','file','artifact','local_path'] if isinstance(o.get(k),str) and o[k].startswith('/private/tmp/')),None);h=o.get('sha256')
        if not(ref and isinstance(h,str) and re.fullmatch('[a-f0-9]{64}',h)):continue
        f=Path(ref)
        need(f.is_file() and sha(f)==h,'Missing/changed dossier artifact '+ref);bindings.append(bind(f))
# Current scientific correction: preserve initial native occurrence and exact successor.
initialp=W/'reviews/structured/20261015T051448Z-wulfenite-round88-dose-label-initial/review.yaml'
initial=yaml.load(initialp.read_text(),Loader=yaml.CSafeLoader)
need(initial['completion']=='partial' and initial['verdict']=='needs_curation' and initial['scientific_review'] is True,'Initial wulfenite observation changed')
need(initial['source']['inputs'][0]['sha256']=='91b7bf7f537e4b8eeef68ca3309f7eb99acc68c1fcd090f2be69449f42ff15ee','Initial owner hash changed')
wv=next(v for v in selected if v['scope']['reviewed_target_ids']==['cmmmech:wulfenite'])
prior=initial['findings'];need(len(prior)==1 and prior[0]['finding_id']=='F1' and prior[0]['status']=='open' and prior[0]['issue_key']=='wulfenite-round88-figure3-dose-label-transcription','Initial finding identity changed')
wf=[f for f in wv['findings'] if f['issue_key']==prior[0]['issue_key']]
need(len(wf)==1 and wf[0]['status']=='resolved','Wulfenite finding not resolved')
wf=wf[0];need({'repository':'CultureBotAI/CMMMech','review_id':initial['review_id'],'finding_id':'F1'} in wf['previous_occurrences'],'Exact previous occurrence omitted')
need('https://github.com/CultureBotAI/CMMMech/issues/302' in wf.get('external_issues',[]),'Resolution omitted issue302')
need(any(i['path']==str(initialp.relative_to(W)) and i['sha256']==sha(initialp) for i in wv['source']['inputs']),'Initial native bytes not bound by successor')
resolution=dict(issue=302,issue_key=wf['issue_key'],initial=bind(initialp),successor_review_id=wv['review_id'],final_finding=wf['finding_id'],status='resolved',scope='Minor Figure3 dose-label transcription corrected by author with canonical EDIT; independent exact native predecessor disposition. Other source uncertainties preserved.')

posted=json.loads((T/'cmm-round88-issues-posted.json').read_text());live=[]
for n in ISSUES['open_source_issues']+ISSUES['corrected_review_issues']+ISSUES['closed_source_issues']:
    d=json.loads(subprocess.check_output(['gh','api',f'repos/CultureBotAI/CMMMech/issues/{n}'],text=True))
    need(d['number']==n and d['state']=='open' and not d.get('pull_request'),'Unexpected live issue state')
    need(any(o.get('number')==n and o.get('title')==d['title'] and o.get('body')==d['body'] for o in posted),'Changed live issue title/body')
    live.append(dict(number=n,state=d['state'],title=d['title'],body_sha256=hashlib.sha256(d['body'].encode()).hexdigest(),url=d['html_url']))
prp=T/'cmm-round88-pr-body.md';pr_body_initial=sha(prp);pr=prp.read_text()
for n in ISSUES['corrected_review_issues']+ISSUES['closed_source_issues']:need(re.search(r'(?i)(?:fixes|closes|resolves)\s+#'+str(n)+r'\b',pr),'Corrected issue not closed in proposed PR')
for n in ISSUES['open_source_issues']:need('#'+str(n) in pr and not re.search(r'(?i)(?:fixes|closes|resolves)\s+#'+str(n)+r'\b',pr),'Source issue closure error')
readme=(W/'README.md').read_text();need('currently contains 422 material records' in readme and 'research/ingests/round88-frontier-20261015.md' in readme,'README count/latest report')
for s in SLUGS:need('data/records/'+s+'.yaml' in readme and (W/'pages/materials'/f'{s}.html').is_file(),'Missing linked record/page')
report=mp.with_suffix('.md').read_text();need(report.startswith('# Round88: five reviewed material records') and '422' in report and all('issues/'+str(n) in report for n in ISSUES['open_source_issues']),'Report counts/issues')
# Original preservation is recomputed using the already established read-only snapshot library.
lib=runpy.run_path(str(T/'cmm-round57-recover-original.py'),run_name='snapshot_library');before=json.loads(Path(preservation['original_snapshot']).read_text());need(before['base']==BASE and before['worktree']==str(W) and before['branch']==BRANCH,'Wrong original preservation scope')
for label,include in [('main',False),('skill',True)]:need(lib['snapshot'](Path(before['snapshots'][label]['path']),include)==before['snapshots'][label],'Original state changed '+label)
need(lib['retained_tag']()==before['retained_tag'],'Retention tag changed')
helper_names=['commit','open-pr','post-review','enqueue','cleanup','sync-main','isolated-verification','isolated-coverage','review-check-final','final-gates','build-manifest']
helpers=[]
for n in helper_names:
    f=T/f'cmm-round88-{n}.py';ast.parse(f.read_text());helpers.append(bind(f))
# Current core mutation helpers were read in full by this auditor, not executed.
# Exact snapshots must be retained; peer-specific implementation/static evidence is separate.
static_bindings=[]
for x in helpers:static_bindings.append(dict(current=x,retained=retained(x['path'])))
for name in ['cmm-round88-hosted-peer.py','cmm_round88_peer_checks.py','cmm-round88-hosted-audit-paginated.py']:
    p=T/name;ast.parse(p.read_text());static_bindings.append(dict(current=bind(p),retained=retained(p)))
# The peer's exact static review and actual focused tests are runtime prerequisites.
staticp=T/'cmm-round88-operational-static-selection.json';selection=json.loads(staticp.read_text());receipts.append(retained(staticp))
for row in selection['artifacts']:
    p=Path(row['path']);need(sha(p)==row['sha256'],'Static artifact changed '+str(p));receipts.append(retained(p))
for row in selection['current_helper_bindings']:
    need(sha(row['path'])==row['sha256'],'Static helper input changed '+row['path'])
need({str(T/n) for n in ['cmm-round88-hosted-peer.py','cmm_round88_peer_checks.py','cmm-round88-hosted-audit-paginated.py']}<={r['path'] for r in selection['current_helper_bindings']},'Hosted static selection lacks current helpers')
need(selection['passed'] is True and selection['unresolved_corrective_findings']==0,'Operational static selection is not a resolved pass')
for key in ['operational_review','independent_hosted_review']:
    r=selection[key];v=json.loads(Path(r['path']).read_text());need(sha(r['path'])==r['sha256'] and v['passed'] is True and v['unresolved_corrective_findings']==0,'Static review changed/not passed')
    for row in v['files']:need(sha(row['path'])==row['sha256'],'Static review current input differs')
op=json.loads(Path(selection['operational_review']['path']).read_text());need(op['total_actual_focused_cases']==63 and len(op['focused_checks'])==3,'Focused fixture inventory differs')
for row in op['focused_checks']:
    f=Path(row['receipt']);v=json.loads(f.read_text());need(sha(f)==row['sha256'] and v['passed'] is True and v.get('case_count',len(v.get('cases',[])))==row['case_count'] and sha(row['source'])==row['source_sha256'],'Focused fixtures changed/failed')
# Builder OP1 was found before execution, and its immutable observation/single-literal successor is independently checked.
bp=T/'cmm-round88-builder-static-selection.json';bs=json.loads(bp.read_text());receipts.append(retained(bp))
for k in ['initial','successor']:
    p=Path(bs[k]['path']);need(sha(p)==bs[k]['sha256'],'Builder observation changed');receipts.append(retained(p))
bo=json.loads(Path(bs['initial']['path']).read_text());bv=json.loads(Path(bs['successor']['path']).read_text())
need(bo['findings'][0]['issue_key']=='round88-manifest-heading-stale-cohort' and bo['findings'][0]['status']=='open','Builder initial finding identity')
need(bv['passed'] is True and bv['unresolved_corrective_findings']==0 and bv['findings'][0]['status']=='resolved','Builder correction not independently resolved')
need(bv['findings'][0]['previous_occurrence']['sha256']==bs['initial']['sha256'],'Builder exact predecessor not bound')
need(bv['current_builder']['sha256']==sha(T/'cmm-round88-build-manifest.py'),'Final builder differs from resolved review')
need(bs['issue'] in ISSUES['corrected_review_issues'],'Builder issue missing from ledger')
static_bindings.append(dict(builder_resolution=bv))

integration=[]
for label in ['effective-rules','claw-admission','claw-convergence','integration-issue3','shepherd-status']:
    f=T/f'cmm-round88-{label}.json';integration.append(retained(f))
rules=json.loads((T/'cmm-round88-effective-rules.json').read_text())
queue=next(x['parameters'] for x in rules if x['type']=='merge_queue')
need(queue['merge_method']=='SQUASH' and queue['grouping_strategy']=='ALLGREEN','Effective queue identity differs')
need({'context':'validate-strict','integration_id':15368} in next(x['parameters']['required_status_checks'] for x in rules if x['type']=='required_status_checks'),'Required workflow integration differs')
need(json.loads((T/'cmm-round88-claw-admission.json').read_text())['state']=='MERGED' and json.loads((T/'cmm-round88-claw-convergence.json').read_text())['state']=='CLOSED','Historical admission/convergence state differs')
need(json.loads((T/'cmm-round88-integration-issue3.json').read_text())['state']=='CLOSED','Issue3 not closed')
need(json.loads((T/'cmm-round88-shepherd-status.json').read_text())['total_count']==0,'Unexpected shepherd runtime evidence requires assessment')
need((W/'scripts/.vendored_canon_ref').read_text().strip()=='a5d562962c75a2ad9efd8160b548df5944315422','Immutable governance pin differs')
integration.extend([bind(W/'scripts/.vendored_canon_ref'),bind(W/'.github/workflows/pr-shepherd.yml')])
need("git('rev-list','--parents','-n','1',merge).split()==[merge,c['base']]" in (T/'cmm-round88-cleanup.py').read_text(),'Cleanup lacks explicit sole-parent guard')
need('rev-list' in (T/'cmm-round88-isolated-verification.py').read_text(),'Isolated verifier lacks parent-count guard')
need(sha(T/'cmm-round88-build-manifest.py')==builder_hash,'Manifest builder changed during audit')
need(sha(prp)==pr_body_initial,'PR body changed during audit')
need(candidates()==names and {n:sha(W/n) for n in names}==hashes and sha(cfgp)==cfgh,'Package changed during audit')
finished=now();OUT=Path(cfg['publication_peer_review']);need(OUT==PUB/'final-audit.json','Reserved audit path differs')
need(not OUT.exists() and not OUT.with_suffix('.md').exists(),'Audit output collision');PUB.mkdir(parents=True,exist_ok=True)
out=dict(started_at=started,finished_at=finished,reviewer='codex /root/round68_phosphates',authorship='Authored gypsum and anhydrite, accepted independently by root; independently reviewed gersdorffite. This operational audit does not self-accept authored science.',passed=True,verdict='pass_with_limitations',unresolved_corrective_findings=0,worktree=str(W),base=BASE,branch=BRANCH,state='working_tree',counts=actual,issues=ISSUES,working_inputs=[dict(path=n,sha256=hashes[n]) for n in sorted(names)],final_scientific_reviews=final,primary_source_bindings=primary,source_dossiers=[bind(p) for p in sourcejson],resolved_corrective_findings=[resolution,bv],dossier_bindings=bindings,receipts=receipts,configuration=bind(cfgp),review_bases=sorted(bases),current_helpers=helpers,static_helper_bindings=static_bindings,integration_bindings=integration,pr_body=bind(prp),live_issue_states=live,preservation=dict(fresh_snapshot_match=True,retained_tag_match=True,scope=preservation['scope']),auditor=bind(Path(__file__)),findings=[],limitations=['Precommit operational audit; exact hosted head/diff/CI, committed isolated preflight, native queue merge, branch cleanup and fresh-main checks remain separate future gates.','Exact current-hash scientific coverage and source/authority/database byte bindings are verified; no new laboratory replication or instrument reanalysis.','Source issues303 and304 remain open. Wulfenite302 native correction and the pre-execution builder heading correction have preserved initial observations and explicit successors; remote closure follows merge.','Historical fleet admission/convergence is distinguished from current repository integration. Manual/comment-only shepherd does not establish App/model-token readiness or whole-fleet freshness.','Static helper inspection and focused fixtures do not assert future runtime success.','Hidden/ignored census follows relevant links with cycle prevention. Git commit-candidate enumeration uses Git scope. Protected original snapshots exclude Git administration and external symlink-target contents.'])
body=f"""# Independent round88 local publication audit

Verdict: **pass with limitations**. Actual audit interval {started} to {finished}. Worktree `{W}`, base `{BASE}`, branch `{BRANCH}`.

Verified {len(names)} exact candidate files before this audit pair and all five current independent scientific reviews. Measured counts: {actual['record_count']} records, {actual['history_count']} histories, {actual['structured_review_count']} native review bundles, {actual['review_base_count']} available bases and {actual['covered_records']} exact current scientific coverage.

I authored gypsum and anhydrite, accepted independently by root, and independently reviewed gersdorffite. This operational audit does not self-accept authored science. Wulfenite #302 has an immutable initial finding, canonical EDIT and explicit independent native successor. The separate manifest heading correction preserves its original observation and narrow resolved successor; no scientific history is invented for that publication-only correction.

Actual baseline, all four batch commands, native review checker, current coverage, governed copies and protected original state are bound to retained receipts/logs. Source #303 and #304 remain open. README, report and proposed PR narrative were checked at bound byte state; all paths and SHA256 values are in JSON.

Hosted review/CI, committed isolated preflight, queue merge/deletion and fresh-main verification remain future gates. Historical CLAW admission/convergence does not substitute for current repository checks or establish shepherd credential readiness. Source uncertainties and laboratory boundaries remain explicit.
"""
OUT.write_text(json.dumps(out,indent=2)+'\n');OUT.with_suffix('.md').write_text(body)
print(json.dumps({'passed':True,'json':str(OUT),'json_sha256':sha(OUT),'markdown':str(OUT.with_suffix('.md')),'markdown_sha256':sha(OUT.with_suffix('.md')),'working_input_count':len(names),'counts':actual},indent=2))
