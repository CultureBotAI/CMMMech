from pathlib import Path
import datetime,json,hashlib,yaml,ast,subprocess,re
W=Path('/private/tmp/CMMMech-expansion-round95-20261015');T=Path('/private/tmp')
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda n:json.loads((T/f'cmm-round95-{n}.json').read_text())
inputs=[]
def bind(p):
    p=Path(p);assert p.is_file() and p.stat().st_size;inputs.append({'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size});return p
cfg=load('helper-config');expected={'record_count':459,'history_count':525,'structured_review_count':542,'review_base_count':96,'covered_records':459};assert cfg['counts']==expected
assert cfg['base']=='73d4b1c42541ee7ca139effae00b94ddb1c8a631'
reportpath=bind(W/'research/ingests/round95-frontier-20261015.json');report=json.loads(reportpath.read_text());md=bind(reportpath.with_suffix('.md')).read_text();body=bind(T/'cmm-round95-pr-body.md').read_text();builder=bind(T/'cmm-round95-build-report.py');ast.parse(builder.read_text());readme=bind(W/'README.md').read_text()
assert report['base']==cfg['base'] and report['branch']==cfg['branch'] and report['state']=='working_tree' and Path(report['worktree']).resolve()==W
assert report['counts']==expected
assert len(list((W/'data/records').glob('*.yaml')))==459
assert len(list((W/'history/records').rglob('*.yaml')))==525
assert len(list((W/'reviews/structured').glob('*/review.yaml')))==542
assert [x['slug'] for x in report['records']]==cfg['slugs'] and len(cfg['slugs'])==7
cv=load('local-coverage');assert cv['passed'] and {k:cv[k] for k in expected}==expected
assert Path(cv['root']).resolve()==W and len(cv['records'])==459
for c in cv['records']:
    assert sha(W/c['path'])==c['sha256'] and c['matching_scientific_reviews']
    assert all(v['verdict'] in ['pass','pass_with_limitations'] and sha(W/v['path'])==v['review_sha256'] for v in c['matching_scientific_reviews'])
for name in ['helper-config','local-coverage','final-gates','review-check-final','issue-ledger','corrective-issue-ledger','integration-status','preservation-precommit']:
    bind(T/f'cmm-round95-{name}.json')
gate=load('final-gates');assert gate['exit_code']==0 and gate['inputs_unchanged'] is True and gate['base']==cfg['base'] and Path(gate['worktree']).resolve()==W
commands=[['just','check'],['uv','run','--locked','cmmmech','validate','--require-records'],['uv','run','--locked','cmmmech','validate-history','--base',cfg['base']],['uv','run','--locked','python','scripts/render_pages.py','--check']]
assert [x['command'] for x in gate['commands']]==commands and all(x['exit_code']==0 for x in gate['commands']);assert sha(bind(gate['log']))==gate['log_sha256'];gt=Path(gate['log']).read_text();assert re.search(r'317 passed, 3 skipped',gt) and 'Checked 459 record(s); 0 failed.' in gt and 'Checked 525 history record(s); 0 error(s).' in gt
rv=load('review-check-final');assert rv['exit_code']==0 and Path(rv['worktree']).resolve()==W and cfg['base'] in rv['command'];assert sha(bind(rv['log']))==rv['log_sha256'];assert '542' in Path(rv['log']).read_text()
selected=[]
for row in report['records']:
    owner=bind(W/row['path']);data=yaml.safe_load(owner.read_text());assert data['id']==row['id'] and data['name']==row['name'] and sha(owner)==row['sha256']==gate['record_inputs'][row['path']]
    rp=bind(W/row['review']['path']);r=yaml.safe_load(rp.read_text());bind(W/row['review']['markdown']);assert sha(rp)==row['review']['review_sha256'];assert r['review_id']==row['review']['review_id'] and r['verdict'] in ['pass','pass_with_limitations'] and r['completion']=='completed' and r['scientific_review'] is True and r['reviewer']['independence']=='independent'
    assert r['scope']['reviewed_target_ids']==[row['id']] and r['source']['git_revision']==cfg['base'] and r['source']['state']=='working_tree'
    for x in r['source']['inputs']:assert sha(W/x['path'])==x['sha256'],x['path']
    assert any(x['path']==row['path'] and x['sha256']==row['sha256'] for x in r['source']['inputs'])
    for hp in row['history_refs']:bind(W/hp);assert hp in [x['path'] for x in r['source']['inputs']]
    assert not [f for f in r.get('findings',[]) if f['status'] in ['open','deferred'] and f['severity'] in ['blocker','major']]
    if row['slug']=='heterosite':
        f=next(x for x in r['findings'] if x['issue_key']=='heterosite-round95-methods-section-locator');assert f['status']=='resolved' and any(x['review_id']=='20261015T125439Z-heterosite-round95-initial-locator' and x['finding_id']=='F1' for x in f['previous_occurrences'])
    selected.append({'slug':row['slug'],'owner_sha256':row['sha256'],'review_path':row['review']['path'],'review_id':r['review_id'],'review_sha256':sha(rp),'reviewer':r['reviewer']['identity']})
selection=json.loads(bind(T/'cmm-round95-hosted-scientific-selection.json').read_text());assert selection['base']==cfg['base'] and set(selection['reviews'])==set(cfg['slugs'])
for x in selected:
    assert selection['reviews'][x['slug']]=={'review_id':x['review_id'],'path':x['review_path'],'sha256':x['review_sha256']}
assert report['source_reports']==sorted(str(x.relative_to(W)) for x in (W/'research/sources').glob('round95-*/*.md'))
for p in report['source_reports']:bind(W/p);bind((W/p).with_suffix('.json'))
sources=load('issue-ledger');fixes=load('corrective-issue-ledger');assert report['issues']==sources and report['corrective_issues']==fixes
assert {x['number'] for x in sources}=={340,341,342,343} and all(x['state']=='OPEN' for x in sources)
assert {x['number'] for x in fixes}=={339,344,345} and all(x['state']=='CLOSED' for x in fixes)
assert all(f'#{n}' in md and f'#{n}' in body for n in range(339,346))
assert 'synthetic heterosite-structure powder preparation and lithium uptake' in md and 'synthetic heterosite-structure powder preparation and lithium uptake' in report['selection']
assert 'Synthetic heterosite-structure powder preparation and lithium uptake' in readme and 'Natural species, engineered powder and distinct brines' in readme
assert 'synthetic heterosite electrode transformation' not in md and 'Synthetic electrode transformation' not in readme
assert 'Hosted PR/queue/merge and fresh-main checks are subsequent' in report['scope_limits']
integration=load('integration-status');assert all(integration[k]['exit_code']==0 for k in ['main','rules','issue3','claw_admission','claw_convergence','shepherd_runs'])
assert integration['main']['data']['object']['sha']==cfg['base'] and integration['claw_admission']['data']['state']=='MERGED' and integration['claw_convergence']['data']['state']=='CLOSED' and integration['issue3']['data']['state']=='CLOSED' and integration['shepherd_runs']['data']['total_count']==0
rules=integration['rules']['data'];q=next(x for x in rules if x['type']=='merge_queue')['parameters'];assert q['merge_method']=='SQUASH' and q['grouping_strategy']=='ALLGREEN';assert any(x['context']=='validate-strict' for r in rules if r['type']=='required_status_checks' for x in r['parameters']['required_status_checks'])
pin=bind(W/'scripts/.vendored_canon_ref').read_text().strip();assert pin=='a5d562962c75a2ad9efd8160b548df5944315422';assert 'OK: 22 governed artifacts match' in bind(T/'cmm-round95-governed-check.log').read_text()
pres=load('preservation-precommit');assert pres['passed'] and pres['base']==cfg['base'] and pres['nontracked_entries_preserved']==7426 and sha(bind(pres['before_receipt']))==pres['before_sha256']
prior=[]
for n in ['report-static-initial-20261015T130252Z','report-static-expanded-20261015T130412Z','report-op2-correction-20261015T130449Z','report-op2-issue-disposition-20261015T130559Z']:
    p=bind(T/f'cmm-round95-{n}.json');prior.append({'path':str(p),'sha256':sha(p)})
time=datetime.datetime.now(datetime.timezone.utc);out=T/f'cmm-round95-generated-report-review-{time.strftime("%Y%m%dT%H%M%SZ")}'
res={'recorded_at':time.isoformat(),'passed':True,'verdict':'pass_with_limitations','scientific_review':False,'reviewer':'codex /root/round68_phosphates','authorship':'Authored heterosite/alunite; independently scientifically reviewed arsenates. This report consistency review relies on separate independent scientific reviews for authored records and does not replace their acceptance.','scope':'Current generated report JSON/MD, seven exact selected native reviews/owner/history/dossier inputs, PR text, corrected README, actual final/review/coverage receipts, retained current integration and preservation evidence. Read-only runtime; no Git/GitHub mutations or test-suite rerun.','base':cfg['base'],'branch':cfg['branch'],'counts':expected,'selected_reviews':selected,'issues':{'corrective_closed':[339,344,345],'source_open':[340,341,342,343]},'findings':[{'finding_id':'OP2','issue_key':'cmmmech.round95.report-heterosite-material-form','severity':'minor','status':'resolved','previous_occurrences':prior,'disposition':'Actual README and generated JSON/MD use the qualified powder material form; initial summaries, exact minimal corrections and root independent primary-source verification are retained. No scientific field was changed for this report correction. GitHub345 closure is represented by the current actual ledger.'}],'inputs':inputs,'limitations':['No claim of hosted PR/queue/merge or fresh-main success; these remain separate subsequent gates.','This consumes and hash-verifies retained coordinator validation/governance/preservation receipts; it does not repeat suites or independently recompute all7426 inventory entries.','Scientific source limitations in owners and source issues340–343 remain unresolved.']}
out.with_suffix('.json').write_text(json.dumps(res,indent=2)+'\n');out.with_suffix('.md').write_text('# Round95 generated-report consistency review\n\nQualified operational pass. Exact seven owners/independent selected native reviews and final459 records,525 histories,542 reviews,96 bases,459 covered records agree with completed receipts. Sources340–343 remain open; corrective339/344/345 are closed in the retained ledger. OP2/#345 is explicitly resolved in the actual README and generated report with the powder wording.\n\nPrimary scientific acceptance remains with each separate reviewer. Current queue/governance and7426-entry preservation receipts support the bounded integration claims; no hosted or postmerge completion is asserted. The paired JSON records exact inputs and predecessor hashes.\n');print(out.with_suffix('.json'));print(sha(out.with_suffix('.json')))
