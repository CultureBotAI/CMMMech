from pathlib import Path
from datetime import datetime,timezone
import json,subprocess,hashlib
w=Path('/private/tmp/CMMMech-expansion-round74-20261014');p=Path('/private/tmp');base='a524756f3f4f90d81f89035fa7f85f1e1897b99d';branch='curate/cmm-expansion-round74-20261014'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def git(*a):return subprocess.check_output(['git',*a],cwd=w,text=True).strip()
assert git('rev-parse','HEAD')==base and git('branch','--show-current')==branch
assert not git('diff','--cached','--name-only')
cfg=json.loads((p/'cmm-round74-helper-config.json').read_text())
auditp=Path(cfg['publication_peer_review']);audit=json.loads(auditp.read_text())
assert audit['passed'] is True and audit['base']==base and audit['branch']==branch and audit['unresolved_corrective_findings']==0
names=set(git('diff','--name-only').splitlines())|set(git('ls-files','--others','--exclude-standard').splitlines())
exclusions={str(auditp.relative_to(w)),str(auditp.with_suffix('.md').relative_to(w))}
assert len(audit['working_inputs'])==len(names-exclusions)
assert {x['path'] for x in audit['working_inputs']}==names-exclusions
for x in audit['working_inputs']:assert sha(w/x['path'])==x['sha256'] and not (w/x['path']).is_symlink()
assert all((w/n).is_file() and not (w/n).is_symlink() for n in names)
assert all(n in ['README.md','research/ingests/round74-frontier-20261014.md','research/ingests/round74-frontier-20261014.json'] or n.startswith(('pages/','reviews/structured/','reviews/publication/20261014-round74/','research/sources/round74-')) or n in ['data/records/'+s+'.yaml' for s in cfg['slugs']] or any(n.startswith('history/records/'+s+'/') for s in cfg['slugs']) for n in names)
for suffix in ['final-gates','review-check-final','local-coverage']:
 g=json.loads((p/('cmm-round74-'+suffix+'.json')).read_text());assert g.get('passed',g.get('exit_code')==0),suffix
 if 'log' in g:assert sha(Path(g['log']))==g['log_sha256']
files=[{'path':n,'sha256':sha(w/n)} for n in sorted(names)]
subprocess.run(['git','diff','--check'],cwd=w,check=True)
subprocess.run(['git','add','--',*sorted(names)],cwd=w,check=True)
assert set(git('diff','--cached','--name-only').splitlines())==names
assert all(sha(w/f['path'])==f['sha256'] for f in files)
subprocess.run(['git','commit','-m',cfg['title']],cwd=w,check=True)
head=git('rev-parse','HEAD');tree=git('rev-parse','HEAD^{tree}')
assert git('rev-parse','HEAD^')==base and not git('status','--porcelain=v1','--untracked-files=all')
r={'timestamp':datetime.now(timezone.utc).isoformat(),'worktree':str(w),'base':base,'branch':branch,'head':head,'tree':tree,'files':files,'publication_audit':str(auditp.relative_to(w)),'publication_audit_sha256':sha(auditp)}
f=p/'cmm-round74-commit-receipt.json';assert not f.exists();f.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'head':head,'tree':tree,'files':len(files)}))
