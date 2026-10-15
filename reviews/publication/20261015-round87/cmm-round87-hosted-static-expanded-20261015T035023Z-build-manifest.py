from pathlib import Path
from datetime import datetime, timezone
import json, yaml, hashlib, shutil

t=Path('/private/tmp'); w=t/'CMMMech-expansion-round87-20261015'
cfg=json.loads((t/'cmm-round87-helper-config.json').read_text())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
checks=w/'research/ingests/round87-checks-20261015'; checks.mkdir(parents=True,exist_ok=True)
pub=w/'reviews/publication/20261015-round87'; pub.mkdir(parents=True,exist_ok=True)
for name in ['baseline','final-gates','review-check-final','local-coverage','governed-check','preservation-precommit']:
    f=t/f'cmm-round87-{name}.json'; v=json.loads(f.read_text())
    assert v.get('passed',v.get('exit_code')==0),name
    d=checks/(name+'.json'); assert not d.exists(); shutil.copyfile(f,d)
    if 'log' in v:
        assert sha(v['log'])==v['log_sha256']; shutil.copyfile(v['log'],checks/(name+'.log'))
for name in ['initialization','issues-posted','effective-rules','claw-admission','claw-convergence','integration-issue3','shepherd-status']:
    f=t/f'cmm-round87-{name}.json'; d=pub/(name+'.json'); assert not d.exists(); shutil.copyfile(f,d)
reviews=[(p,yaml.safe_load(p.read_text())) for p in (w/'reviews/structured').glob('*round87*/review.yaml')]
rows=[]
for slug in cfg['slugs']:
    p=w/'data/records'/f'{slug}.yaml'; record=yaml.safe_load(p.read_text())
    matches=[(q,v) for q,v in reviews if v['completion']=='completed' and v['scientific_review'] is True and v['verdict'] in ('pass','pass_with_limitations') and v['scope']['reviewed_target_ids']==[record['id']] and any(x['path']==str(p.relative_to(w)) and x['sha256']==sha(p) for x in v['source']['inputs'])]
    assert len(matches)==1,(slug,len(matches)); q,v=matches[0]
    assert v['reviewer']['independence']=='independent'
    assert all(f['status'] in ('resolved','dismissed') for f in v['findings'])
    rows.append(dict(slug=slug,id=record['id'],name=record['name'],path=str(p.relative_to(w)),sha256=sha(p),history_refs=record['history_refs'],review=dict(path=str(q.relative_to(w)),markdown=str(q.with_suffix('.md').relative_to(w)),sha256=sha(q),review_id=v['review_id'],verdict=v['verdict'])))
reports=sorted(str(p.relative_to(w)) for p in (w/'research/sources').glob('round87-*/*.md'))
selection='Three distinct material owners: alabandite in a mixed-ore bacterial flotation experiment, simonkolleite in abiotic synthesis and thermal transformation, and secondary aluminium dross in abiotic roasting and leaching. The two mineral species and the mixed secondary resource retain separate identities. No elemental criticality designation is inherited.'
validation='Baseline and final just check, strict nonempty-corpus validation, append-only history, generated pages and canonical review checks passed. Exact current scientific review coverage was checked separately. No schema, validator, tests or governance change was required.'
integration='CLAW admission PR #581 is merged, convergence issue #580 and CMMMech issue #3 are closed. All 22 governed files match immutable pin a5d562962c75a2ad9efd8160b548df5944315422. The effective main queue uses SQUASH/ALLGREEN with required validate-strict. PR shepherd remains manual/comment-only; its current workflow API reports zero runs. A controlled dry run and separate writer/reviewer App/model-token readiness verification remain follow-ups through supported CLAW admission/synchronization.'
limits='This is a bounded source investigation, not an exhausted frontier. Laboratory experiments and industrial feedstock origin do not establish deployment. Mineral fractions, solid-balance extraction estimates and phase assignments do not establish isolated product recovery. Source contradictions and missing controls remain explicit. Raw primary texts and graphics remain outside Git with source hashes. Hosted PR review, squash-shaped preflight, native queue admission, actual merge, branch cleanup and fresh-main verification are subsequent publication gates, not claimed completed here.'
m=dict(recorded_at=datetime.now(timezone.utc).isoformat(),worktree=str(w),branch=cfg['branch'],base=cfg['base'],state='working_tree',counts=cfg['counts'],records=rows,source_reports=reports,issues=cfg['issues'],selection=selection,validation=validation,integration=integration,limits=limits)
p=w/'research/ingests/round87-frontier-20261015.json'; assert not p.exists(); p.write_text(json.dumps(m,indent=2)+'\n')
lines=['# Round87: three reviewed material records','',f"Actual UTC: {m['recorded_at']}",'',selection,'','| Record | Independent scientific review | Curation history |','|---|---|---|']
for x in rows:
    lines.append(f'| [{x["name"]}](../../{x["path"]}) | [Markdown](../../{x["review"]["markdown"]}) · [YAML](../../{x["review"]["path"]}) | '+' · '.join(f'[session](../../{h})' for h in x['history_refs'])+' |')
lines+=['',validation,f"Measured coverage: {cfg['counts']['covered_records']}/{cfg['counts']['record_count']} current records; {cfg['counts']['history_count']} history sessions; {cfg['counts']['structured_review_count']} native reviews; {cfg['counts']['review_base_count']} available review bases. [Receipts and logs](round87-checks-20261015/)."]
for key,label in [('corrected_review_issues','Corrected review findings (closure follows merge)'),('closed_source_issues','Resolved source issues (closure follows merge)'),('open_source_issues','Open source follow-ups')]:
    if cfg['issues'][key]: lines+=['',label+': '+', '.join(f'[#{n}](https://github.com/CultureBotAI/CMMMech/issues/{n})' for n in cfg['issues'][key])+'.']
lines+=['','All selected native reviews cover the final record and history hashes. Earlier findings, when present, retain their original occurrences and explicit successor dispositions. Open source questions have been investigated and the accepted claims narrowed; unavailable clarification is not presented as completed.', '',integration,'',limits,'','Source dossiers: '+', '.join(f'[{Path(x).parent.name}](../../{x})' for x in reports)+'. Each has paired JSON provenance.','','[Publication evidence](../../reviews/publication/20261015-round87/) records issue text and integration status. Original main and the unrelated skill worktree remain preserved, including hidden/ignored files within the documented inventory.','']
p.with_suffix('.md').write_text('\n'.join(lines)); print(p)
