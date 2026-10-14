from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess,yaml
p=Path('/private/tmp');root=p/'CMMMech-expansion-round72-20261014';base='a2f08edab1307aba4281ce1e2a54d84bca88a889'
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
cfg=json.loads((p/'cmm-round72-helper-config.json').read_text());slugs=cfg['slugs']
for name in ['final-gates','review-check-final','local-coverage']:
 d=json.loads((p/f'cmm-round72-{name}.json').read_text());assert d.get('passed',d.get('exit_code')==0),name
 if 'log' in d:assert sha(Path(d['log']))==d['log_sha256']
package=root/'reviews/publication/20261014-round72';package.mkdir(parents=True,exist_ok=False)
retained=['baseline.json','baseline.log','final-gates.json','final-gates.log','review-check-final.json','review-check-final.log','local-coverage.json','integration-status.json','vendored.log','preservation-prepublication.json','gates.py','isolated-coverage.py','isolated-verification.py','commit.py','open-pr.py','post-review.py','enqueue.py','cleanup.py','sync-main.py','hosted-audit-paginated.py','hosted-peer.py','helper-config.json','hydrocerussite-followup.md','orpiment-followup.md','carbonate-followup.md','source-issues.json','aragonite-summary-issue.md','issue-234-resolution.md','issue-234-closed.json','build-summary.py']
retained += [x.name.removeprefix('cmm-round72-') for x in p.glob('cmm-round72-helper-static*') if x.suffix in ['.md','.json']]
retained += [x.name.removeprefix('cmm-round72-') for x in p.glob('cmm-round72-summary-peer*') if x.suffix in ['.md','.json']]
assert any('helper-static' in n for n in retained),'Independent helper review required'
for n in retained:
 f=p/('cmm-round72-'+n);assert f.is_file() and f.stat().st_size>0
 shutil.copyfile(f,package/n)
changed=[]
for slug in slugs:
 owner=root/f'data/records/{slug}.yaml';v=yaml.safe_load(owner.read_text());matches=[]
 for f in (root/'reviews/structured').glob('*round72*/review.yaml'):
  r=yaml.safe_load(f.read_text())
  if r.get('scientific_review') and r.get('completion')=='completed' and r.get('verdict') in ['pass','pass_with_limitations'] and v['id'] in r['scope']['reviewed_target_ids'] and any(i['path']==str(owner.relative_to(root)) and i['sha256']==sha(owner) for i in r['source']['inputs']):
   assert not any(x['severity'] in ['blocker','major'] and x['status'] not in ['resolved','rejected','accepted_risk'] for x in r.get('findings',[]));matches.append(str(f.relative_to(root)))
 assert len(matches)==1,(slug,matches)
 changed.append({'slug':slug,'path':str(owner.relative_to(root)),'sha256':sha(owner),'history':v['history_refs'],'review':matches[0]})
files=set(subprocess.check_output(['git','diff','--name-only'],cwd=root,text=True).splitlines())|set(subprocess.check_output(['git','ls-files','--others','--exclude-standard'],cwd=root,text=True).splitlines())
artifacts=[{'path':n,'sha256':sha(root/n)} for n in sorted(files) if (root/n).is_file()]
report={'recorded_at':datetime.now(timezone.utc).isoformat(),'worktree':str(root),'branch':'curate/cmm-expansion-round72-20261014','base':base,'records_changed':changed,'counts':cfg['counts'],'issues':cfg['issues'],'artifacts':artifacts,'scope':'Seven new mineral records with canonical CREATE history and independent scientific reviews of their current bytes. No schema, validator or governed-copy changes. Publication and merge remain subsequent gates.'}
out=root/'research/ingests/round72-frontier-20261014.json';assert not out.exists();out.write_text(json.dumps(report,indent=2)+'\n')
rows=['| Record | Scientific review |','|---|---|']
for r in changed:
 rp='../../'+r['review'];rows.append(f"| [{r['slug']}](../../{r['path']}) | [Markdown]({rp.replace('review.yaml','review.md')}) / [YAML]({rp}) |")
md='''# Round 72: carbonate, arsenic-sulfide and feldspar minerals

Seven new mineral owners extend the corpus from 334 to 341. Selection prioritizes identifiable phases and inspectable primary evidence. Elements, mineral species, experimental mixtures and resources remain distinct. No new criticality designation or industrial deployment is inferred.

- **Albite:** controlled abiotic dissolution of characterized clevelandite, retaining sodium-loss transients, solution chemistry, model-dependent surface interpretation and contrary evidence.
- **Orthoclase:** abiotic alkaline dissolution of natural Na-bearing material. The inspected author thesis supplies experimental graphics; readable final-journal text corroborates the same study. Four interruptions of one run are not independent replicates; projections remain model results. The microbial lead in issue #225 remains unresolved.
- **Aragonite and monohydrocalcite:** qualified carbonate-phase observations in bacterial culture studies. Source phase/run conflicts and the ON000249.1 environmental-clone versus named-culture identity discrepancy remain explicit. Shared experiments are not independent replications.
- **Realgar:** early culture-associated arsenic mobilization followed by below-control dissolved concentration. Feed purity/impurity conflicts and proposed late sequestration remain separate from measured results.
- **Orpiment:** a source-assigned secondary phase in mixed arsenopyrite-leaching products. The existing arsenopyrite owner describes the same experiment. Amorphous As2S3 in Newman1997 is not treated as crystalline orpiment evidence.
- **Hydrocerussite:** a phase in processed KKY-29 cell products, mixed with pyromorphite. Contradictory phosphate labels, biomass units and non-phase-specific intracellular imaging preclude precise condition/yield and causal claims.

'''+ '\n'.join(rows)+'''

The [carbonate](../sources/round72-carbonates/), [silicate](../sources/round72-silicates/), [arsenic-sulfide](../sources/round72-arsenic-sulfides/) and [hydrocerussite](../sources/round72-hydrocerussite/) dossiers retain exact sources, inspected locators, hashes, acquisition failures and limitations. Raw originals remain outside Git. Searches include hidden/ignored files and relevant symlinks within recorded boundaries; they do not establish global source exhaustion.

'''
for n in cfg['issues']['open_source_issues']:
 md += f'- [Source issue #{n}](https://github.com/CultureBotAI/CMMMech/issues/{n}) remains open; unavailable evidence was not silently converted into accepted claims.\n'
md += '\nIndependent scientific review found no supported corrective defect in the seven final records. [Review issue #234](https://github.com/CultureBotAI/CMMMech/issues/234) corrected the README aragonite boundary so it no longer inherits the monohydrocalcite source-condition conflict. The initial document finding and explicit independent successor are retained. Source gaps remain separate.\n\n'
md += f"Validation passed: `just check` (317 passed, 3 skipped), nonempty corpus validation ({cfg['counts']['record_count']} records), trusted-base history ({cfg['counts']['history_count']} sessions), structured reviews ({cfg['counts']['structured_review_count']} bundles) and exact current scientific coverage ({cfg['counts']['covered_records']}/{cfg['counts']['record_count']}). {cfg['counts']['review_base_count']} review bases are available. Baseline and final gates were both executed anew this round. [Publication evidence](../../reviews/publication/20261014-round72/) retains terminal receipts, logs and bounded publication helpers.\n\n"
md += 'Current read-only checks confirm CLAW admission and convergence are complete, all 22 governed artifacts match the pin, and the native SQUASH/ALLGREEN queue is active without bypass. The PR shepherd remains manual and comment-only. Future integration changes must use CLAW’s supported process. Original main and unrelated skill worktree preservation passed before publication. Exact hosted review, squash preflight, actual merge/branch deletion and fresh remote-main validation remain subsequent gates.\n'
out.with_suffix('.md').write_text(md)
body='''This adds seven evidence-backed mineral records: albite, orthoclase, aragonite, monohydrocalcite, realgar, orpiment and hydrocerussite, growing the corpus from 334 to 341. Each has a primary-source dossier, canonical CREATE history and an independent scientific review of its final bytes. Albite and orthoclase are explicitly abiotic. The remaining records retain source condition, taxonomy, mixed-phase and control limits without inferring isolated-product recovery or industrial deployment.

Independent scientific review found no supported corrective defects in these final records. Review issue #234 corrected a README attribution error and was independently rechecked; both document-review states are retained. Source evidence gaps remain open: ''' + ', '.join('#'+str(n) for n in cfg['issues']['open_source_issues']) + '''. Existing source tasks are preserved; narrow accepted records do not resolve unavailable evidence.

Validation: `just check` (317 passed, 3 skipped), `validate --require-records`, trusted-base history, structured reviews and exact scientific coverage passed. No schema, validator or governed-file changes.

See `research/ingests/round72-frontier-20261014.md` for record/review links and `reviews/publication/20261014-round72/` for validation evidence. Exact hosted review, isolated squash preflight and native queue checks follow this PR.
'''
(p/'cmm-round72-pr-body.md').write_text(body);print(out)
