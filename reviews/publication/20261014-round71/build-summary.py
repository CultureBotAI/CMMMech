from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess,yaml
p=Path('/private/tmp');root=p/'CMMMech-expansion-round71-20261014';base='188ce7cb6f6dd1b7966b527546d80f9b4fb7fcec'
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
cfg=json.loads((p/'cmm-round71-helper-config.json').read_text());slugs=cfg['slugs']
for name in ['final-gates','review-check-final','local-coverage']:
 d=json.loads((p/f'cmm-round71-{name}.json').read_text())
 assert d.get('passed',d.get('exit_code')==0),name
 if 'log' in d:assert sha(Path(d['log']))==d['log_sha256']
package=root/'reviews/publication/20261014-round71';package.mkdir(parents=True,exist_ok=False)
retained=['baseline.json','final-gates.json','final-gates.log','review-check-final.json','review-check-final.log','local-coverage.json','integration-status.json','vendored.log','preservation-prepublication.json','gates.py','isolated-coverage.py','isolated-verification.py','commit.py','open-pr.py','post-review.py','enqueue.py','cleanup.py','sync-main.py','hosted-audit-paginated.py','helper-config.json','orthoclase-followup.md','dw018-followup.md','nepheline-review-issue.md','strontianite-review-issue.md','helper-wording-issue.md','helper-static-20261014T122946Z.json','helper-static-20261014T122946Z.md','helper-static-resolution-20261014T123241Z.json','helper-static-resolution-20261014T123241Z.md','initial-helpers-peer.json','helper-resolution-comment.md','issue-227-resolution.md','issue-229-resolution.md','scientific-issue-resolutions.json','build-summary.py']
for n in retained:
 f=p/('cmm-round71-'+n);assert f.is_file() and f.stat().st_size>0
 shutil.copyfile(f,package/n)
changed=[]
for slug in slugs:
 owner=root/f'data/records/{slug}.yaml';v=yaml.safe_load(owner.read_text());matches=[]
 for f in (root/'reviews/structured').glob('*round71*/review.yaml'):
  r=yaml.safe_load(f.read_text())
  if r.get('scientific_review') and r.get('completion')=='completed' and r.get('verdict') in ['pass','pass_with_limitations'] and v['id'] in r['scope']['reviewed_target_ids'] and any(i['path']==str(owner.relative_to(root)) and i['sha256']==sha(owner) for i in r['source']['inputs']):
   assert not any(x['severity'] in ['blocker','major'] and x['status'] not in ['resolved','rejected','accepted_risk'] for x in r.get('findings',[]))
   matches.append(str(f.relative_to(root)))
 assert len(matches)==1,(slug,matches)
 changed.append({'slug':slug,'path':str(owner.relative_to(root)),'sha256':sha(owner),'history':v['history_refs'],'review':matches[0]})
files=set(subprocess.check_output(['git','diff','--name-only'],cwd=root,text=True).splitlines())|set(subprocess.check_output(['git','ls-files','--others','--exclude-standard'],cwd=root,text=True).splitlines())
artifacts=[{'path':n,'sha256':sha(root/n)} for n in sorted(files) if (root/n).is_file()]
report={'recorded_at':datetime.now(timezone.utc).isoformat(),'worktree':str(root),'branch':'curate/cmm-expansion-round71-20261014','base':base,'records_changed':changed,'counts':cfg['counts'],'issues':cfg['issues'],'artifacts':artifacts,'scope':'Five new mineral records with separate CREATE history and independent current-byte scientific reviews. No schema, validator or governed-copy changes. Publication and merge remain subsequent gates.'}
out=root/'research/ingests/round71-frontier-20261014.json';assert not out.exists();out.write_text(json.dumps(report,indent=2)+'\n')
rows=['| Record | Scientific review |','|---|---|']
for r in changed:
 rp='../../'+r['review'];rows.append(f"| [{r['slug']}](../../{r['path']}) | [Markdown]({rp.replace('review.yaml','review.md')}) / [YAML]({rp}) |")
md='''# Round 71: carbonate, strontium and feldspathoid minerals

Five new mineral records extend the corpus from 329 to 334. Selection prioritizes distinct identities and complete primary evidence. Elements, mineral species, rocks, commodities and experimental mixtures remain separate. No new criticality designation, pure-phase recovery yield or industrial deployment is inferred.

- **Calcite:** two-hour formation in the DW018 terbium assay, plus mixed brine-treatment solids. Rapid Tb removal also occurs without added calcium and is not assigned to calcite.
- **Vaterite:** a source-assigned phase in processed mixed brine-treatment solids. It shares one experiment with calcite and the geothermal-brine resource owner; these are not independent replications.
- **Nepheline:** fungal weathering of characterized mixed Bancroft discs. Sparse destructive sampling, a second-strain label conflict and whole-specimen aluminium release constrain interpretation.
- **Strontianite:** qualified laboratory carbonate formation with bacterial biomass, retaining the uninoculated no-coating result and the source's dosing and analytical limits.
- **Celestine:** laboratory Sr-sulfate formation associated with a cyanobacterial surface layer; the original specimen and control limits remain explicit.

'''+ '\n'.join(rows)+'''

The [carbonate](../sources/round71-carbonates/), [silicate](../sources/round71-silicates/) and [strontium-mineral](../sources/round71-strontium-minerals/) dossiers retain source identities, exact locators, acquisition failures, nonzero file hashes and limitations. Bulk originals remain outside Git. Searches include hidden and ignored files and relevant symlinks within the recorded boundaries; this round does not establish global source exhaustion.

[Issue #225](https://github.com/CultureBotAI/CMMMech/issues/225) tracks the complete orthoclase fungal-weathering original, whose abstract already indicates muscovite contamination. [Issue #226](https://github.com/CultureBotAI/CMMMech/issues/226) tracks DW018 sequence/raw-data provenance. Both remain open source tasks; narrower accepted records do not resolve unavailable evidence. Albite and the Eu2016 carbonate lead also remain deferred. Existing source issues were preserved.

[Review issue #227](https://github.com/CultureBotAI/CMMMech/issues/227) tracks a corrected nepheline figure-legend transcription (234300, not 231300). The initial native finding is preserved and the independent successor explicitly resolves it against corrected owner and history bytes. The source’s 234300/243400 identity conflict remains unresolved. [Review issue #229](https://github.com/CultureBotAI/CMMMech/issues/229) separates a calcium-coating observation from the Sr evidence; its initial finding and independent resolution are retained. [Publication issue #228](https://github.com/CultureBotAI/CMMMech/issues/228) corrects stale attribution of the inherited pagination fix to round 70.

'''
md += f"Validation passed: `just check` (317 passed, 3 skipped), nonempty corpus validation ({cfg['counts']['record_count']} records), trusted-base history ({cfg['counts']['history_count']} sessions), structured reviews ({cfg['counts']['structured_review_count']} bundles) and exact current scientific coverage ({cfg['counts']['covered_records']}/{cfg['counts']['record_count']}). {cfg['counts']['review_base_count']} review bases are available. The baseline reused freshly completed checks on identical main bytes; final gates were executed anew. [Publication evidence](../../reviews/publication/20261014-round71/) retains terminal receipts, logs and bounded publication helpers.\n\n"
md += 'CLAW admission and integration are complete; all 22 governed artifacts match the pin. The native SQUASH/ALLGREEN queue is active without bypass. The PR shepherd remains manual and comment-only. Future integration changes must use CLAW’s supported admission/synchronization process. Original main and unrelated skill worktree preservation passed before publication. Exact hosted review, squash-shaped preflight, merge, branch deletion and fresh remote-main validation remain subsequent gates.\n'
out.with_suffix('.md').write_text(md)
body='''This adds five evidence-backed mineral records: calcite, vaterite, nepheline, strontianite and celestine. Each has primary-source assessment, canonical CREATE history and an independent scientific review of its final bytes. The records retain mixed-phase, control, dosing and source inconsistencies without inferring phase-specific recovery or industrial deployment.

The corpus grows from 329 to 334 records. Review issues #227 and #229 are resolved through source-attribution corrections, appended history and explicit independent successors. Publication issue #228 corrects inherited audit wording without changing behavior. Source follow-ups #225 and #226 remain open; orthoclase and other insufficiently supported leads are deferred.

Validation: `just check` (317 passed, 3 skipped), `validate --require-records`, trusted-base history, native structured reviews and exact scientific coverage passed. No schema, validator or governed-file changes.

See `research/ingests/round71-frontier-20261014.md` for record/review links and `reviews/publication/20261014-round71/` for validation evidence. Hosted review, squash preflight and native queue checks follow this PR.
'''
(p/'cmm-round71-pr-body.md').write_text(body)
print(out)
