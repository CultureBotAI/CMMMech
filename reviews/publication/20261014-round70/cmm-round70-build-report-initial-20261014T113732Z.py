"""Assemble completed local publication evidence without claiming hosted outcomes."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess, yaml
root=Path('/private/tmp/CMMMech-expansion-round70-20261014');tmp=Path('/private/tmp')
base='1d40bb5d7496a02b937acc1f6ef3aec5af5d32e7';branch='curate/cmm-expansion-round70-20261014'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
git=lambda *a:subprocess.check_output(['git',*a],cwd=root,text=True).strip()
assert git('rev-parse','HEAD')==base and git('branch','--show-current')==branch
cfg=json.loads((tmp/'cmm-round70-helper-config.json').read_text());counts=cfg['counts']
pub=root/'reviews/publication/20261014-round70';pub.mkdir(parents=True,exist_ok=True)
checks={};artifacts=[]
def retain(p,name=None):
 d=pub/(name or p.name);assert not d.exists();shutil.copyfile(p,d);artifacts.append(d);return d
for name in ['baseline','final-gates','review-check','local-coverage','preservation-prepublication','integration-status']:
 p=tmp/f'cmm-round70-{name}.json';v=json.loads(p.read_text())
 if name=='integration-status':
  assert v['admission']['state']=='MERGED' and v['convergence']['state']=='CLOSED' and v['cmm_integration']['state']=='CLOSED'
  assert v['vendored_result']=='OK: 22 governed artifacts match the pinned claw revision'
 else:assert v.get('passed',v.get('exit_code')==0),name
 if 'log' in v:
  assert sha(Path(v['log']))==v['log_sha256'];retain(Path(v['log']),name+'.log')
 if 'commands' in v:assert v['commands'] and all(x['exit_code']==0 for x in v['commands'])
 if name in ['baseline','final-gates','review-check']:assert v['base']==base
 if name=='local-coverage':assert all(v[k]==x for k,x in counts.items())
 d=retain(p,name+'.json');checks[name]={'path':str(d.relative_to(root)),'sha256':sha(d)}
for pattern in ['cmm-round70-helper-peer-static.json','cmm-round70-helper-peer-static.md']:
 ps=list(tmp.glob(pattern));assert len(ps)==1;retain(ps[0])
for name in ['helper-derivation.json','audit-binding-regression.json','gibbsite-issue.json','anorthite-issue.json']:
 retain(tmp/('cmm-round70-'+name))
helpers=[]
for name in ['commit','open-pr','post-review','enqueue','cleanup','hosted-audit','isolated-verification','isolated-coverage','sync-main','preservation-check','integration-check','closeout','build-report']:
 p=tmp/('cmm-round70-'+name+'.py');helpers.append({'name':name,'path':str(p),'sha256':sha(p)})
d=pub/'helper-snapshots.json';assert not d.exists();d.write_text(json.dumps({'recorded_at':datetime.now(timezone.utc).isoformat(),'helpers':helpers,'config':cfg},indent=2)+'\n');artifacts.append(d)
reviews=[(p,yaml.safe_load(p.read_text())) for p in (root/'reviews/structured').rglob('review.yaml')]
records=[]
for slug in cfg['slugs']:
 p=root/'data/records'/f'{slug}.yaml';v=yaml.safe_load(p.read_text());relative=str(p.relative_to(root));digest=sha(p)
 matches=[(rp,r) for rp,r in reviews if r.get('scientific_review') is True and r.get('completion')=='completed' and r.get('verdict') in ['pass','pass_with_limitations'] and r.get('scope',{}).get('reviewed_target_ids')==[v['id']] and any(t.get('path')==relative and t.get('target_id')==v['id'] for t in r.get('targets',[])) and any(i.get('path')==relative and i.get('sha256')==digest for i in r['source']['inputs'])]
 assert len(matches)==1,(slug,len(matches));rp,rv=matches[0]
 assert rv['reviewer']['independence']=='independent' and rv['source']['git_revision']==base
 assert all(sha(root/i['path'])==i['sha256'] for i in rv['source']['inputs'])
 assert not any(f.get('severity') in ['blocker','major'] and f['status'] not in ['resolved','rejected'] for f in rv.get('findings',[]))
 records.append({'slug':slug,'operation':'CREATE' if slug in cfg['created_slugs'] else 'EDIT','path':relative,'sha256':digest,'review':str(rp.relative_to(root)),'history':v['history_refs']})
 artifacts += [p,rp,rp.with_name('review.md'),*[root/h for h in v['history_refs']]]
for directory in ['round70-aluminium-minerals','round70-phosphates','round70-silicates','round70-carbonates-handoff']:
 files=[p for p in sorted((root/'research/sources'/directory).rglob('*')) if p.is_file()]
 assert any(p.suffix=='.md' for p in files) and any(p.suffix=='.json' for p in files),directory
 artifacts+=files
changed=set(git('diff','--name-only').splitlines())|set(git('ls-files','--others','--exclude-standard').splitlines())
assert not any(p.startswith(('src/','tests/','.github/','scripts/','.claude/','docs/')) for p in changed)
artifacts += [root/p for p in changed if p=='README.md' or p.startswith(('pages/','reviews/structured/'))]
now=datetime.now(timezone.utc).isoformat();dest=root/'research/ingests/round70-frontier-20261014.json';md=dest.with_suffix('.md');body=tmp/'cmm-round70-pr-body.md'
assert not any(p.exists() for p in [dest,md,body])
report={'recorded_at':now,'author':'Codex (GPT-6), /root; coordinator and independent reviewer of boehmite and gibbsite. Phosphate and silicate curators independently cross-reviewed each other. Root authored this report, README and publication helpers.','base':base,'branch':branch,'worktree':str(root),'records_changed':records,'counts':counts,'issues':cfg['issues'],'checks':checks,'artifacts':[{'path':str(p.relative_to(root)),'sha256':sha(p)} for p in sorted(set(artifacts))],'scope':'Five new mineral owners with primary evidence, immutable history, independent scientific reviews, source dossiers, README and generated pages. Carbonate investigation is a deferred handoff. No schema, validator or governed-file changes.','publication_state':'Local checks completed; exact-head hosted review, isolated squash preflight, native queue, actual merge and fresh-main verification are subsequent gates.'}
rows='\n'.join('| '+v['operation']+' | ['+v['slug']+'](../../'+v['path']+') | [Markdown](../../'+v['review'].replace('review.yaml','review.md')+') / [YAML](../../'+v['review']+') |' for v in records)
md.write_text(f"""# Round 70: silicates, aluminium minerals and apatites

UTC {now}. Worktree `{root}`; branch `{branch}`; trusted base `{base}`.

Five new mineral records bring the corpus from 324 to {counts['record_count']}. Selection prioritizes distinct material identities and inspectable primary evidence. Mineral species, synthetic experimental feeds, elements and commodities remain separate; no constituent criticality or industrial performance is inherited.

- **Anorthite:** natural plagioclase contact assays and fungal leaching of source-assigned feed. The bacterial experiment's acid extraction and unmatched water controls remain explicit; calcium responds differently from aluminium/silicon. The fungal paper's bulk chemistry is incompatible with pure anorthite, so phase-specific release and pure-endmember yield are withheld.
- **Böhmite:** explicitly abiotic synthesis from aluminium sec-butoxide. Six recipes and five displayed diffraction fits do not establish pure-product yield, independent replication or an isolated pH effect.
- **Gibbsite:** abiotic alkaline dissolution separates directly observed step retreat from machine-learning reconstruction and constrained molecular simulations. Monomer spectroscopy does not directly identify dissolved dimers; modeled event fractions are not extraction efficiency. Microbial Lee/Fein2000 evidence remains deferred.
- **Hydroxylapatite:** biofilm mineralization preserves fixed-biomass activity, enzyme-buffer contributions and inhibitor effects; it does not establish metabolic necessity or industrial recovery.
- **Chlorapatite:** synthetic substrate identity and growth-associated nutrient accessibility are kept separate from abiotic solution measurements. No matched bacterial dissolution series proves enhanced dissolution.

| Change | Record | Independent exact-state scientific review |
|---|---|---|
{rows}

## Source evidence and follow-ups

The [silicate](../sources/round70-silicates/), [aluminium-mineral](../sources/round70-aluminium-minerals/) and [phosphate](../sources/round70-phosphates/) dossiers retain precise source locators, acquisition failures, hashes, controls and unresolved questions. Bulk raw originals remain outside Git. Searches include hidden/ignored files and relevant symlinks within declared boundaries, without claiming global exhaustion.

[Issue #219](https://github.com/CultureBotAI/CMMMech/issues/219) tracks the missing complete Lee/Fein2000 microbial gibbsite study. [Issue #220](https://github.com/CultureBotAI/CMMMech/issues/220) tracks the Ma2024 anorthite feed composition and final medium discrepancy. Both are new source-assessment follow-ups; neither is falsely closed by a narrower accepted record. No corrective defect was found in the five final scientific states, so no artificial corrective issue or resolution is created.

The [carbonate handoff](../sources/round70-carbonates-handoff/) preserves incomplete calcite/vaterite and rare-earth precipitation research. Its acquired sources are not accepted mechanisms. Complete Tb2024 evidence assessment and legitimate Eu2016 full-text acquisition remain concrete next actions. Existing source issues, including antigorite #217 and meta-autunite #120, remain outside the accepted changes.

## Validation and publication

`just check` passed 317 tests with 3 skips. Nonempty validation passed {counts['record_count']} records; trusted-base history passed {counts['history_count']} sessions; structured checking passed {counts['structured_review_count']} bundles. Exact current positive scientific coverage is {counts['covered_records']}/{counts['record_count']}, with {counts['review_base_count']} available review bases. Five new independent reviews cover all five final records and their CREATE histories. [Publication evidence](../../reviews/publication/20261014-round70/) retains receipts, logs, helper regression/audit results and the final publication audit. The JSON manifest binds scientific and generated artifacts.

All 22 governed artifacts match CLAW's immutable pin. Admission, convergence and CMMMech integration are complete. The native queue is active with SQUASH/ALLGREEN and no bypass; the PR shepherd remains manual/comment-only. Future governance changes must use CLAW's supported admission/synchronization process.

Original main and the unrelated skill worktree matched initialization for scoped hidden/ignored bytes, modes, symlink targets and Git state. Exact hosted head/tree review, isolated squash-shaped preflight, native queue, branch deletion and fresh remote-main verification remain subsequent gates, not preclaimed successes.
""")
dest.write_text(json.dumps(report,indent=2)+'\n')
body.write_text(f"""Adds five evidence-backed mineral records: anorthite, böhmite, gibbsite, hydroxylapatite and chlorapatite. Each has canonical history and an independent scientific review. The records preserve mixed-feed identity, abiotic alternatives, model limitations and source inconsistencies without inherited criticality or industrial recovery claims.

Includes source dossiers, catalogue summaries and generated pages. Calcite/vaterite research remains an explicit handoff. No schema, validator or governed-file changes.

Validation: `just check` (317 passed, 3 skipped), nonempty corpus ({counts['record_count']} records), trusted-base history ({counts['history_count']} sessions), structured reviews ({counts['structured_review_count']} bundles), and exact current scientific coverage ({counts['covered_records']}/{counts['record_count']}; {counts['review_base_count']} review bases available. All 22 governed artifacts match the CLAW pin.

[Evidence, reviews and priorities](research/ingests/round70-frontier-20261014.md). Source follow-ups #219 and #220 remain open with concrete acceptance criteria. No corrective scientific defect found in the five final states.

Exact-head hosted review, isolated squash preflight and native merge queue are required before merge; fresh remote-main verification follows branch deletion.
""")
print(json.dumps({'report':str(dest),'markdown':str(md),'body':str(body),'artifacts':len(report['artifacts'])},indent=2))
