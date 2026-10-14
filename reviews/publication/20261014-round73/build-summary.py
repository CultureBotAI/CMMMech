from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess,yaml
P=Path('/private/tmp');W=P/'CMMMech-expansion-round73-20261014';BASE='ea4b9370fdb3d1ab23e5f43f6f9fe5f8d46a31e3';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
cfg=json.loads((P/'cmm-round73-helper-config.json').read_text());slugs=cfg['slugs'];pub=W/'reviews/publication/20261014-round73'
assert not pub.exists()
for n in ['baseline','final-gates','review-check-final','local-coverage']:
 d=json.loads((P/f'cmm-round73-{n}.json').read_text());assert d.get('passed',d.get('exit_code')==0),n
 if 'log' in d:assert sha(Path(d['log']))==d['log_sha256']
for key in ['final_static_review','publication_peer_review']:
 d=json.loads(Path(cfg[key]).read_text());assert d['passed'] is True,key
pub.mkdir(parents=True)
retained=['baseline.json','baseline.log','final-gates.json','final-gates.log','review-check-final.json','review-check-final.log','local-coverage.json','integration-status.json','vendored.log','preservation-prepublication.json','gates.py','isolated-coverage.py','isolated-verification.py','commit.py','open-pr.py','post-review.py','enqueue.py','cleanup.py','sync-main.py','hosted-audit-paginated.py','hosted-peer.py','final-package-audit.py','helper-config.json','antimony-source-followup.md','source-issues.json','artinite-issue.md','artinite-issue.json','artinite-issue-final.json','helper-issue.md','helper-issue.json','helper-resolution.md','issue-237-closed.json','artinite-resolution.md','issue-236-closed.json','build-summary.py','static-input-regression.py','static-input-regression.json']
retained += [p.name.removeprefix('cmm-round73-') for p in P.glob('cmm-round73-helper-static*.json')]
retained += [p.name.removeprefix('cmm-round73-') for p in P.glob('cmm-round73-helper-static*.md')]
retained += [p.name.removeprefix('cmm-round73-') for p in P.glob('cmm-round73-publication-peer-initial-*.json')]
retained += [p.name.removeprefix('cmm-round73-') for p in P.glob('cmm-round73-publication-peer-initial-*.md')]
retained += [Path(cfg['publication_peer_review']).name.removeprefix('cmm-round73-'),Path(cfg['publication_peer_review']).with_suffix('.md').name.removeprefix('cmm-round73-')]
for n in retained:
 f=P/('cmm-round73-'+n);assert f.is_file() and f.stat().st_size>0,n;shutil.copyfile(f,pub/n)
for folder in P.glob('cmm-round73-helper-static*-sources'):
 assert folder.is_dir() and not folder.is_symlink();shutil.copytree(folder,pub/folder.name.removeprefix('cmm-round73-'))
for folder in P.glob('cmm-round73-publication-peer-initial-*-sources'):
 assert folder.is_dir() and not folder.is_symlink();shutil.copytree(folder,pub/folder.name.removeprefix('cmm-round73-'))
changed=[]
for slug in slugs:
 owner=W/f'data/records/{slug}.yaml';v=yaml.safe_load(owner.read_text());matches=[]
 for f in (W/'reviews/structured').glob('*round73*/review.yaml'):
  r=yaml.safe_load(f.read_text())
  if r.get('scientific_review') is True and r.get('completion')=='completed' and r.get('verdict') in ['pass','pass_with_limitations'] and v['id'] in r['scope']['reviewed_target_ids'] and any(i['path']==str(owner.relative_to(W)) and i['sha256']==sha(owner) for i in r['source']['inputs']):
   assert r['reviewer']['independence']=='independent';assert not any(x['status'] not in ['resolved','rejected','accepted_risk'] for x in r.get('findings',[]));matches.append(str(f.relative_to(W)))
 assert len(matches)==1,(slug,matches)
 changed.append(dict(slug=slug,path=str(owner.relative_to(W)),sha256=sha(owner),history=v['history_refs'],review=matches[0]))
names=set(subprocess.check_output(['git','diff','--name-only'],cwd=W,text=True).splitlines())|set(subprocess.check_output(['git','ls-files','--others','--exclude-standard'],cwd=W,text=True).splitlines())
artifacts=[dict(path=n,sha256=sha(W/n)) for n in sorted(names) if (W/n).is_file()]
report=dict(recorded_at=datetime.now(timezone.utc).isoformat(),worktree=str(W),branch='curate/cmm-expansion-round73-20261014',base=BASE,records_changed=changed,counts=cfg['counts'],issues=cfg['issues'],artifacts=artifacts,scope='Six new material owners with canonical histories and independent scientific reviews. One corrected scientific methods finding and one corrected operational provenance finding. No schema,validator or governed-copy changes. Publication gates follow.')
out=W/'research/ingests/round73-frontier-20261014.json';assert not out.exists();out.write_text(json.dumps(report,indent=2)+'\n')
rows=['| Record | Independent scientific review |','|---|---|']
for r in changed:
 rp='../../'+r['review'];rows.append(f"| [{r['slug']}](../../{r['path']}) | [Markdown]({rp.replace('review.yaml','review.md')}) / [YAML]({rp}) |")
text='''# Round73: silicates, magnesium carbonates, antimony oxide and CIGS modules

Six new owners extend the corpus from 341 to 347. Selection favored inspectable primary evidence and clear material boundaries. Mineral species remain distinct from elemental commodities and the composite secondary CIGS resource. No new criticality designation or industrial deployment is inferred.

- Microcline: field colonization/weathering of a heterogeneous specimen, with a P-poor comparator and a laboratory null silicon-release result. Inclusion-derived nutrients are not pure-microcline release yields.
- Muscovite: fungal-associated surface alteration of characterized material, retaining the nonsignificant mycelial potassium difference versus the K-depleted control. No recovered potassium or gene-causal mechanism is inferred.
- Senarmontite: a minor source-assigned phase in mixed enrichment-culture products. Isolate diffraction is not displayed; tartrate and cell-free precipitation limit biological necessity claims.
- Artinite: separate abiotic dissolution and concentrated-solution precipitation arms. Impurities, mixed phases, modeled activities and conflicting Raman labels remain explicit.
- Lansfordite: abiotic synthesis/dehydration plus one decay-associated winter cactus occurrence. Microbial causality is unresolved, and natural versus synthetic dehydration products differ.
- End-of-life CIGS photovoltaic modules: chemical leaching of actual source-described discarded panels. Synthetic In/Ga separation tests do not establish whole-panel product recovery.

'''+ '\n'.join(rows)+'''

The paired source dossiers are under [silicates](../sources/round73-silicates/), [carbonates](../sources/round73-carbonates/), [antimony minerals](../sources/round73-antimony-minerals/) and [CIGS](../sources/round73-cigs/). Raw originals remain outside Git. Hidden/ignored-inclusive searches followed relevant symlinks within documented boundaries; this bounded cohort does not establish global source exhaustion.

Review issue [236](https://github.com/CultureBotAI/CMMMech/issues/236) corrected an unsupported daily-shaking duration in both artinite contexts. The initial F1 observation, new EDIT history and independent exact-hash successor are retained. Issue [237](https://github.com/CultureBotAI/CMMMech/issues/237) corrected a stale round label in a publication receipt; exact initial/successor operational reviews are retained. Both corrective issues are closed. Source-access issue [238](https://github.com/CultureBotAI/CMMMech/issues/238) remains open for Abin2014/Yamamura2021 antimonate-respiration polymorph evidence; unavailable full sources have not been converted into accepted claims.

During preparation, two reviewers independently noticed an auditor assumption that every initial static input had a snapshot. The author corrected the explicitly imported library case before execution. The peer's initial capture raced that correction and therefore contains corrected source bytes; it does not prove an unresolved defect in those bytes. That observation, its explicit disposition and five focused checks of the actual validation block are retained. No failed publication run or scientific correction is inferred from this preparation event.

'''
c=cfg['counts'];text+=f"Validation passed: `just check` (317 passed,3 skipped), `validate --require-records` ({c['record_count']} records), trusted-base history ({c['history_count']} sessions), structured reviews ({c['structured_review_count']} bundles), and exact current scientific coverage ({c['covered_records']}/{c['record_count']}). All {c['review_base_count']} distinct review bases are available. Both baseline and final gates were actually executed this round. [Publication evidence](../../reviews/publication/20261014-round73/) contains terminal receipts/logs, immutable findings and bounded publication helpers.\n\n"
text+='Current read-only checks confirm CLAW admission/convergence and history integration are installed, all 22 governed artifacts match the pin, and the native SQUASH/ALLGREEN queue is active without bypass. PR shepherd operation remains manual and comment-only. Future fleet integration must use CLAW’s supported process. Original main and unrelated skill worktree preservation passed. Exact hosted review, isolated squash preflight, queue checks, actual merge/branch deletion and fresh-main verification remain subsequent gates.\n'
out.with_suffix('.md').write_text(text)
body='''This adds six evidence-backed records: microcline, muscovite, senarmontite, artinite, lansfordite and end-of-life CIGS photovoltaic modules, growing the corpus from 341 to 347. Each has a primary-source dossier, canonical history and an independent scientific review of its final bytes. The records preserve null results, mixed phases, source conflicts and laboratory/field limits. Artinite and CIGS treatment are explicitly abiotic; no constituent criticality is inherited.

Adversarial review corrected the artinite daily-shaking duration (#236) and a publication-receipt round label (#237). Initial findings and explicit independent successor dispositions are retained; both corrective issues are closed. Source-access follow-up #238 remains open, with no unsupported antimony-polymorph claim admitted.

Validation: just check (317 passed, 3 skipped), nonempty corpus validation, trusted-base history, structured reviews and exact scientific coverage passed. No schema, validator or governed-file changes.

See research/ingests/round73-frontier-20261014.md for record/review links and reviews/publication/20261014-round73/ for validation evidence. Exact hosted review, isolated squash preflight and native queue checks follow this PR.
'''
(P/'cmm-round73-pr-body.md').write_text(body);print(out)
