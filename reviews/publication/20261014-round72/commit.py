from pathlib import Path
from datetime import datetime, timezone
import subprocess, json, hashlib
root=Path('/private/tmp/CMMMech-expansion-round72-20261014')
tmp=Path('/private/tmp')
base='a2f08edab1307aba4281ce1e2a54d84bca88a889'
branch='curate/cmm-expansion-round72-20261014'
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
git=lambda *args:subprocess.check_output(['git',*args],cwd=root,text=True).strip()
assert git('rev-parse','HEAD')==base and git('branch','--show-current')==branch
assert not git('diff','--cached','--name-only')
finals=list((root/'reviews/publication/20261014-round72').glob('*-publication-final.json'))
assert len(finals)==1,finals
a=json.loads(finals[0].read_text())
assert a.get('passed') is True and a.get('verdict') in ['pass','pass_with_limitations']
for name in ['final-gates','review-check-final','local-coverage']:
    v=json.loads((tmp/('cmm-round72-'+name+'.json')).read_text())
    assert v.get('passed',v.get('exit_code')==0),name
m=json.loads((root/'research/ingests/round72-frontier-20261014.json').read_text())
assert all(sha(root/item['path'])==item['sha256'] for item in m['artifacts'])
allowed=['README.md','research/ingests/round72-frontier-20261014.md','research/ingests/round72-frontier-20261014.json']
prefixes=['pages/','reviews/publication/20261014-round72/','research/sources/round72-silicates/','research/sources/round72-carbonates/','research/sources/round72-arsenic-sulfides/','research/sources/round72-hydrocerussite/']
allowed += [a['path'] for a in m['artifacts'] if a['path'].startswith('reviews/structured/')]
for r in m['records_changed']:
    allowed += [r['path'],*r['history'],r['review'],r['review'].replace('review.yaml','review.md')]
names=set(git('diff','--name-only').splitlines())|set(git('ls-files','--others','--exclude-standard').splitlines())
assert names and all(n in allowed or any(n.startswith(p) for p in prefixes) for n in names),names
assert all((root/n).is_file() and not (root/n).is_symlink() for n in names)
require_final_audit(a,root,names,finals[0],base,branch,json.loads((tmp/'cmm-round72-helper-config.json').read_text()))
files=[{'path':n,'sha256':sha(root/n)} for n in sorted(names)]
subprocess.run(['git','diff','--check'],cwd=root,check=True)
subprocess.run(['git','add','--',*sorted(names)],cwd=root,check=True)
assert set(git('diff','--cached','--name-only').splitlines())==names
assert all(sha(root/f['path'])==f['sha256'] for f in files)
subprocess.run(['git','commit','-m',json.loads((tmp/'cmm-round72-helper-config.json').read_text())['title']],cwd=root,check=True)
head=git('rev-parse','HEAD');tree=git('rev-parse','HEAD^{tree}')
assert git('rev-parse','HEAD^')==base and not git('status','--porcelain=v1','--untracked-files=all')
v={'timestamp':datetime.now(timezone.utc).isoformat(),'worktree':str(root),'base':base,'branch':branch,'head':head,'tree':tree,'files':files,'publication_audit':str(finals[0].relative_to(root)),'publication_audit_sha256':sha(finals[0])}
out=tmp/'cmm-round72-commit-receipt.json';assert not out.exists();out.write_text(json.dumps(v,indent=2)+'\n')
print(json.dumps({'head':head,'tree':tree,'files':len(files)}))
