from pathlib import Path
from datetime import datetime,timezone
import json,subprocess,hashlib
w=Path('/private/tmp/CMMMech-expansion-round77-20261014');p=Path('/private/tmp');base='e5e70cfc93a3aa68a166eba7bbbd3dc1053ce60d';branch='curate/cmm-expansion-round77-20261014'
def require_final_audit(audit, root, candidate_names, audit_path, base, branch, config):
    if audit.get('passed') is not True or audit.get('verdict') not in ('pass', 'pass_with_limitations'):
        raise RuntimeError('Final publication audit did not pass')
    if type(audit.get('unresolved_corrective_findings')) is not int or audit['unresolved_corrective_findings'] != 0:
        raise RuntimeError('Final publication audit has unresolved corrective findings')
    if audit.get('base') != base or audit.get('branch') != branch or audit.get('state') != 'working_tree':
        raise RuntimeError('Final publication audit does not identify this working tree base/branch')
    if audit.get('counts') != config['counts'] or audit.get('issues') != config['issues']:
        raise RuntimeError('Final publication audit counts or issue dispositions differ from configuration')
    excluded = {str(audit_path.relative_to(root)), str(audit_path.with_suffix('.md').relative_to(root))}
    expected = set(candidate_names) - excluded
    inputs = audit.get('working_inputs', [])
    paths = [item.get('path') for item in inputs]
    if not inputs or len(set(paths)) != len(paths) or set(paths) != expected:
        raise RuntimeError('Final publication audit file coverage differs from commit candidates')
    for item in inputs:
        path = root / item['path']
        if not path.is_file() or path.is_symlink() or hashlib.sha256(path.read_bytes()).hexdigest() != item.get('sha256'):
            raise RuntimeError('Final publication audit input changed: ' + item['path'])
    return True


sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def git(*a):return subprocess.check_output(['git',*a],cwd=w,text=True).strip()
assert git('rev-parse','HEAD')==base and git('branch','--show-current')==branch
assert not git('diff','--cached','--name-only')
cfg=json.loads((p/'cmm-round77-helper-config.json').read_text())
auditp=Path(cfg['publication_peer_review']);audit=json.loads(auditp.read_text())
names=set(git('diff','--name-only').splitlines())|set(git('ls-files','--others','--exclude-standard').splitlines())
require_final_audit(audit,w,names,auditp,base,branch,cfg)
exclusions={str(auditp.relative_to(w)),str(auditp.with_suffix('.md').relative_to(w))}
assert len(audit['working_inputs'])==len(names-exclusions)
assert {x['path'] for x in audit['working_inputs']}==names-exclusions
for x in audit['working_inputs']:assert sha(w/x['path'])==x['sha256'] and not (w/x['path']).is_symlink()
assert all((w/n).is_file() and not (w/n).is_symlink() for n in names)
assert all(n in ['README.md','research/ingests/round77-frontier-20261014.md','research/ingests/round77-frontier-20261014.json'] or n.startswith(('pages/','reviews/structured/','reviews/publication/20261014-round77/','research/sources/round77-','research/ingests/round77-checks-20261014/')) or n in ['data/records/'+s+'.yaml' for s in cfg['slugs']] or any(n.startswith('history/records/'+s+'/') for s in cfg['slugs']) for n in names)
for suffix in ['final-gates','review-check-final','local-coverage']:
 g=json.loads((p/('cmm-round77-'+suffix+'.json')).read_text());assert g.get('passed',g.get('exit_code')==0),suffix
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
f=p/'cmm-round77-commit-receipt.json';assert not f.exists();f.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'head':head,'tree':tree,'files':len(files)}))
