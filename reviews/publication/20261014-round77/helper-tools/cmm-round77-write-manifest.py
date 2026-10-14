from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess,yaml
P=Path('/private/tmp');W=P/'CMMMech-expansion-round77-20261014';cfg=json.loads((P/'cmm-round77-helper-config.json').read_text());coverage=json.loads((P/'cmm-round77-local-coverage.json').read_text());assert coverage['passed'];sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
checks=W/'research/ingests/round77-checks-20261014'
for name in ['review-check-final.json','review-check-final.log','local-coverage.json']:
 dst=checks/name;assert not dst.exists();shutil.copyfile(P/('cmm-round77-'+name),dst)
records=[]
for slug in cfg['slugs']:
 path='data/records/'+slug+'.yaml';data=yaml.safe_load((W/path).read_text());row=next(x for x in coverage['records'] if x['path']==path);assert row['sha256']==sha(W/path)
 matching=[r for r in row['matching_scientific_reviews'] if 'round77' in r['path']];assert len(matching)==1;review=matching[0];v=yaml.safe_load((W/review['path']).read_text());assert v['reviewer']['independence']=='independent'
 records.append({'slug':slug,'id':data['id'],'name':data['name'],'material_kind':data['material_kind'],'path':path,'sha256':sha(W/path),'review':review,'review_markdown':str(Path(review['path']).with_suffix('.md')),'history_refs':data['history_refs']})
names=set(subprocess.check_output(['git','diff','--name-only'],cwd=W,text=True).splitlines())|set(subprocess.check_output(['git','ls-files','--others','--exclude-standard'],cwd=W,text=True).splitlines());assert all((W/n).is_file() and not (W/n).is_symlink() for n in names)
source_reports=[str(p.relative_to(W)) for folder in sorted((W/'research/sources').glob('round77-*')) for p in sorted(folder.glob('*.md'))]
now=datetime.now(timezone.utc).isoformat();r={'recorded_at':now,'base':cfg['base'],'branch':cfg['branch'],'worktree':str(W),'state':'working_tree','selection':'Four distinct material owners selected from complete primary studies: three minerals and one secondary resource. Phase, culture-control, source-table and strain-identity limits are retained. No constituent criticality or industrial deployment is inferred.','records':records,'counts':cfg['counts'],'issues':cfg['issues'],'source_reports':source_reports,'pre_manifest_inputs':[{'path':n,'sha256':sha(W/n)} for n in sorted(names)],'inventory_scope':'Tracked changes and nonignored untracked commit candidates before this manifest pair and final audit pair. Hidden/ignored-inclusive scientific census and exact-hash coverage are separate receipts; no absence claim about ignored caches.','checks_receipts':{p.name:{'path':str(p.relative_to(W)),'sha256':sha(p)} for p in sorted(checks.glob('*.json'))},'remaining':['Acquire complete Anjum hospital-incinerator bottom-ash original and supplements via a new legitimate route (issue253).','Investigate the documented sepiolite/phlogopite/palygorskite/saponite leads with full originals and complete duplicate checks before accepting claims.','Resolve study-specific phase, culture-control and measurement limits before stronger mechanistic or recovery claims.','Continue bounded discovery; these four additions do not demonstrate exhaustion.'],'publication_status':'Local gates and exact scientific review coverage passed. Commit, hosted exact-head review, isolated squash preflight, native queue merge, branch cleanup and fresh remote-main verification are subsequent steps.'}
out=W/'research/ingests/round77-frontier-20261014.json';assert not out.exists();out.write_text(json.dumps(r,indent=2)+'\n')
rows=[]
for x in records:
 histories=' · '.join(f'[history {i+1}](../../{h})' for i,h in enumerate(x['history_refs']));rows.append(f"| [{x['name']}](../../{x['path']}) | [{x['review']['verdict']}](../../{x['review_markdown']}) · [YAML](../../{x['review']['path']}) | {histories} |")
c=cfg['counts'];links=', '.join(f'[{Path(s).parent.name}](../../{s})' for s in source_reports)
md=f'''# Round77: four reviewed mineral and secondary-resource additions

Recorded UTC: {now}. Trusted base `{cfg['base']}`; worktree `{W}`; branch `{cfg['branch']}`.

Four new owners raise the catalogue from 364 to 368 records. Selection prioritized complete primary experiments and useful, distinct identities: acanthite, monetite, switzerite and spent tantalum capacitors. The resource does not inherit the criticality of tantalum; mineral identities do not imply a criticality designation. All accepted biological observations remain laboratory results.

| Record | Independent scientific review | Canonical histories |
|---|---|---|
'''+'\n'.join(rows)+f'''

The final owners have independent qualified scientific passes matching exact current hashes. Their principal limits remain explicit:

- Acanthite is a minority phase assigned by composition plus electron diffraction in processed AG259 cells. Most particles are elemental silver and another type remains unidentified. Missing matched controls, processing effects and proposed sulfur chemistry prevent biological necessity, phase-pure yield or deployment claims.
- Monetite occurs with residual brushite on composite surfaces after live biofilm and filtered spent-broth challenges. The latter retains microbial products and is not fresh inorganic acid. Qualitative diffraction and separate thermal measurements do not establish a mineral yield or distinguish the proposed transformation routes.
- Switzerite is a source-assigned culture product with strain/medium contrasts and reported uninoculated controls, but published hydrate-specific diffraction and water-content measurements are missing. Historical naming and soil-table conflicts remain explicit. Separate natural-specimen dehydration evidence does not establish the same handling outcome for culture precipitates.
- Spent tantalum capacitors are a distinct secondary-resource feed. Acidophile and fungal-filtrate arms support qualified base-metal mobilization, with tantalum nondetection, conflicting tables, incompletely assigned controls and current DSM2182 nomenclature retained. The study overlaps the existing tantalum record; it is not counted as independent replication or isolated tantalum recovery.

Source investigations: {links}. Paired JSON dossiers retain actual acquisition attempts, raw-source locations/checksums and bounded searches. Original articles stay outside Git. The additional silicate report is an explicitly incomplete lead handoff; it does not claim full-source review or complete raw-download deduplication.

[Issue #253](https://github.com/CultureBotAI/CMMMech/issues/253) records the hospital-incinerator bottom-ash source gap after a fresh fully paginated all-state issue search. The publisher and author-upload routes returned HTTP403; no measurements from that unavailable original enter the corpus. It remains open for legitimate full-source acquisition and review. Independent static review of the hosted-review template found minor HP1: a stale claim about correction lineage inherited from the preceding cohort. [Issue #254](https://github.com/CultureBotAI/CMMMech/issues/254) records the actual defect. Only two prose statements were corrected; exact initial snapshots and an independent successor preserve the finding and disposition. No inaccurate COMMENT was posted and behavioral guards are unchanged. The earlier generic publication-helper audit had no findings; this later preparation defect is separate. Final package auditing and live publication still follow this manifest.

Validation: `just check` — 317 passed, 3 skipped; `cmmmech validate --require-records` — {c['record_count']} records, zero failures; trusted-base history check — {c['history_count']} entries; native review check — {c['structured_review_count']} reviews; exact-hash positive scientific coverage — {c['covered_records']}/{c['record_count']} records across {c['review_base_count']} available review bases. Generated pages are current. [Receipts and logs](round77-checks-20261014/) distinguish validation from scientific acceptance. All 22 governed artifacts match the immutable CLAW pin. No schema, validator, tests or governed files changed.

The original main checkout and unrelated skill worktree match initialization, including hidden/ignored files, modes and symlink targets within the documented snapshot bounds. Git administration and external symlink-target contents are excluded. All new native reviews use the trusted main base, which survives squash; existing retained bases remain available. The final independent publication audit will bind this manifest and every commit candidate. It does not replace the required exact-head hosted review, committed squash-shaped preflight, native merge checks and fresh remote-main checks after branch deletion.

This bounded cohort does not establish that no further CMMs exist. The [companion JSON](round77-frontier-20261014.json) binds accepted owners, reviews, history, measured census and the pre-manifest package inventory.
''';out.with_suffix('.md').write_text(md);print(json.dumps({'manifest':str(out),'records':len(records),'counts':c},indent=2))
