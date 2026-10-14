from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,runpy,shutil,yaml,subprocess
P=Path('/private/tmp');W=P/'CMMMech-expansion-round77-20261014';base='e5e70cfc93a3aa68a166eba7bbbd3dc1053ce60d';branch='curate/cmm-expansion-round77-20261014'
slugs=['acanthite','monetite','spent-tantalum-capacitors','switzerite'];sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not (P/'cmm-round77-helper-config.json').exists()
for n in ['baseline','final-gates','vendored-check']:
 d=json.loads((P/f'cmm-round77-{n}.json').read_text());assert d.get('passed',d.get('exit_code')==0);assert sha(d['log'])==d['log_sha256']
lib=runpy.run_path(str(P/'cmm-round57-recover-original.py'),run_name='snapshot_library');before=json.loads((P/'cmm-round77-preservation-before.json').read_text());current={'main':lib['snapshot'](lib['MAIN'],False),'skill':lib['snapshot'](lib['SKILL'],True)}
assert current==before['snapshots'] and lib['retained_tag']()==before['retained_tag']
now=datetime.now(timezone.utc);pub=W/'reviews/publication/20261014-round77';pub.mkdir(parents=True,exist_ok=True)
reviews=[yaml.safe_load(p.read_text()) for p in (W/'reviews/structured').rglob('review.yaml')]
counts={'record_count':len(list((W/'data/records').rglob('*.yaml'))),'history_count':len(list((W/'history/records').rglob('*.yaml'))),'structured_review_count':len(reviews),'review_base_count':len({r['source']['git_revision'] for r in reviews}),'covered_records':368}
assert counts['record_count']==368
issues=json.loads((P/'cmm-round77-issue-dispositions.json').read_text())
cfg={'title':'Add four reviewed silver-sulfide, phosphate and capacitor records','base':base,'branch':branch,'worktree':str(W),'counts':counts,'issues':issues,'slugs':slugs,'publication_peer_review':str(pub/(now.strftime('%Y%m%dT%H%M%SZ')+'-publication-final.json')),'publication_audit_path_reserved_at':now.isoformat()}
(P/'cmm-round77-helper-config.json').write_text(json.dumps(cfg,indent=2)+'\n')
r={'recorded_at':now.isoformat(),'passed':True,'base':base,'original_snapshot':str(P/'cmm-round77-preservation-before.json'),'original_snapshot_sha256':sha(P/'cmm-round77-preservation-before.json'),'snapshots_match':True,'retained_tag_match':True,'entry_counts':{k:len(v['files']) for k,v in current.items()},'scope':'Exact main nontracked and unrelated skill all-file snapshots, including hidden/ignored files, modes and symlink targets; Git administrative files and external symlink-target contents excluded.'}
(P/'cmm-round77-preservation-precommit.json').write_text(json.dumps(r,indent=2)+'\n')
checks=W/'research/ingests/round77-checks-20261014';checks.mkdir(parents=True,exist_ok=True)
for n in ['baseline.json','baseline.log','final-gates.json','final-gates.log','vendored-check.json','vendored-check.log','preservation-precommit.json','hospital-issue-created.json']:
 dest=checks/n;assert not dest.exists();shutil.copyfile(P/('cmm-round77-'+n),dest)
helpers=pub/'helper-tools';helpers.mkdir(exist_ok=True)
for entry in json.loads((P/'cmm-round77-helper-derivation.json').read_text())['helpers']:
 src=Path(entry['target']);assert sha(src)==entry['target_sha256'];shutil.copyfile(src,helpers/src.name)
shutil.copyfile(P/'cmm-round77-helper-derivation.json',pub/'cmm-round77-operational-derivation.json')
shutil.copyfile(P/'cmm-round57-recover-original.py',helpers/'snapshot-library-round57.py')
shutil.copyfile(P/'cmm-round77-helper-config.json',helpers/'config.prepublication.json')
print(json.dumps(cfg,indent=2))
