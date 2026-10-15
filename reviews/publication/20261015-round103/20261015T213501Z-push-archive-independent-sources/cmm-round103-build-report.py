from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,shutil,yaml
T=Path('/private/tmp');W=T/'CMMMech-expansion-round103-20261015'
load=lambda n:json.loads((T/f'cmm-round103-{n}.json').read_text())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
cfg=load('helper-config');cv=load('local-coverage');g=load('final-gates');rv=load('review-check-final');pres=load('preservation-before-commit');issues=load('source-issues')
assert cv['passed'] and all(cv[k]==v for k,v in cfg['counts'].items())
assert g['exit_code']==rv['exit_code']==0 and g['inputs_unchanged'] and pres['passed']
assert sha(g['log'])==g['log_sha256'] and sha(rv['log'])==rv['log_sha256']
assert '317 passed, 3 skipped' in Path(g['log']).read_text()
records=[]
for slug in cfg['slugs']:
    path=f'data/records/{slug}.yaml';owner=yaml.safe_load((W/path).read_text());row=next(r for r in cv['records'] if r['path']==path)
    assert row['sha256']==sha(W/path)
    matching=[]
    for x in row['matching_scientific_reviews']:
        r=yaml.safe_load((W/x['path']).read_text())
        if r['source']['git_revision']!=cfg['base']:continue
        assert r['reviewer']['independence']=='independent'
        assert not any(f['severity'] in ('blocker','major') and f['status'] in ('open','deferred') for f in r.get('findings',[]))
        matching.append(x)
    assert len(matching)==1
    records.append(dict(id=owner['id'],name=owner['name'],path=path,sha256=row['sha256'],history_refs=owner['history_refs'],review=matching[0]))
checks=W/'research/ingests/round103-checks-20261015';checks.mkdir()
for name in ['baseline','final-gates','review-check-final','local-coverage','preservation-before-commit','review-bases-local','governed-check']:
    p=T/f'cmm-round103-{name}.json';shutil.copy2(p,checks/p.name)
    if name in ['baseline','final-gates','review-check-final','governed-check']:shutil.copy2(p.with_suffix('.log'),checks/p.with_suffix('.log').name)
selection='Six distinct mineral species and one spent-electrolyte resource extend the corpus. Autunite and torbernite retain qualified synthetic-crystal identity evidence. Inyoite and szaibelyite retain abiotic pressure/thermal observations; rhabdophane-(Ce) and rhabdophane-(La) retain separate hydrothermal/thermal transformations. Spent vanadium flow-battery electrolyte combines two clearly separated abiotic recovery and regeneration studies. Mineral species, elemental materials, fresh electrolyte and used secondary resources remain distinct. No microbial process or elemental criticality is inherited.'
validation='Baseline and final just check passed: 317 tests passed, 3 skipped. Strict nonempty validation, append-only history, generated-page freshness and native review validation passed. All 508 current records have an exact-hash positive scientific review, including independent reviews of all seven new owners. No schema, validator, governed-file or repository code/test changes were needed.'
priorities=['Resolve source follow-ups #385–390 from authoritative corrections or underlying data; current records preserve the unresolved conflicts.','Keep #120 meta-autunite, #129 vanadinite, #130 yeast cerium-phosphate identity and #133 samarium-phosphate figure access deferred; the new abiotic records do not resolve them.','Investigate the acquired hydroboracite thermal/structure/high-pressure source lead in a later bounded curation batch. New candidates remain; this is not a source-exhaustion claim.','Continue prior source gaps and verify PR-shepherd operation through the supported workflow when appropriate. Future fleet changes use supported CLAW admission and synchronization.']
sources=sorted(str(p.relative_to(W)) for p in (W/'research/sources').glob('round103-*/*.md'))
data=dict(recorded_at=datetime.now(timezone.utc).isoformat(),worktree=str(W),branch=cfg['branch'],base=cfg['base'],state='working_tree',selection=selection,records=records,counts=cfg['counts'],source_reports=sources,source_issues=issues,publication_review_issues=[dict(number=391,url='https://github.com/CultureBotAI/CMMMech/issues/391',disposition='Receipt reservation corrected in temporary push/archive/issue helpers, with isolated regressions and independent disposition; closure accompanies the PR lifecycle.')],validation=validation,corrective_findings='No supported corrective scientific owner finding. Publication review #391 concerns temporary helper receipt reservation and rerun behavior, corrected before publication. Source-evidence questions remain qualified and open.',remaining_priorities=priorities,publication_scope='Local curation/review complete. Exact committed-head PR review, isolated squash preflight, native queue and fresh remote-main verification are subsequent publication gates.')
p=W/'research/ingests/round103-frontier-20261015.json'
with p.open('x') as h:json.dump(data,h,indent=2);h.write('\n')
lines=['# Round103: seven reviewed material records','',data['recorded_at'],'',selection,'','| Record | Independent review | Canonical history |','|---|---|---|']
for r in records:lines.append(f"| [{r['name']}](../../{r['path']}) | [Markdown](../../{r['review']['path'].replace('.yaml','.md')}) · [YAML](../../{r['review']['path']}) | "+' · '.join(f'[session](../../{h})' for h in r['history_refs'])+' |')
lines+=['',validation,'',f"Measured totals: {cv['record_count']} records, {cv['history_count']} histories, {cv['structured_review_count']} native reviews and {cv['review_base_count']} available review bases. [Check receipts/logs](round103-checks-20261015/).",'',data['corrective_findings'],'','Open source follow-ups:','']
lines += [f"- [#{i['number']}]({i['url']}): {i['title']}" for i in issues]
lines += ['','The fresh [integration snapshot](../../reviews/publication/20261015-round103/integration-status.json) confirms merged CLAW admission PR #581, closed CMMMech #3 and CLAW #580, 22 governed files matching the immutable pin, and native SQUASH/ALLGREEN queue with validate-strict required. PR-shepherd is configured but the returned run inventory is empty; this does not establish credential absence.','','Remaining priorities:','']+['- '+x for x in priorities]
lines+=['','Source dossiers: '+', '.join(f'[{Path(s).parent.name}](../../{s})' for s in sources)+'. Paired JSON retains exact acquisition provenance and bounded access failures. Raw originals remain outside Git.','','All 9,309 pre-existing nontracked entries, including hidden/ignored files, retain hashes, modes and symlink identity. Original main and unrelated worktrees were preserved. All review bases survive through trusted main history or the retained annotated evidence tag; no topic-only review base is introduced.','',data['publication_scope'],'']
with p.with_suffix('.md').open('x') as h:h.write('\n'.join(lines))
print(p)
