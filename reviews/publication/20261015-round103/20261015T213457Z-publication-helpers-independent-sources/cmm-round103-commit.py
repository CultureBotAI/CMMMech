from pathlib import Path
from datetime import datetime, timezone
import json, subprocess, hashlib
temp=Path('/private/tmp'); root=temp/'CMMMech-expansion-round103-20261015'
cfg=json.loads((temp/'cmm-round103-helper-config.json').read_text())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
now=lambda:datetime.now(timezone.utc).isoformat()
out=temp/'cmm-round103-commit-receipt.json'
receipt={'started_at':now(),'base':cfg['base'],'branch':cfg['branch'],'commands':[]}
def run(cmd):
    p=subprocess.run(cmd,cwd=root,capture_output=True,text=True)
    receipt['commands'].append({'at':now(),'command':cmd,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
    assert p.returncode==0,(cmd,p.stderr)
    return p.stdout.strip()
def git(*args):return run(['git',*args])
with out.open('x') as stream:
    try:
        assert git('rev-parse','HEAD')==cfg['base']
        assert git('branch','--show-current')==cfg['branch']
        for name in ('final-gates','review-check-final'):
            d=json.loads((temp/f'cmm-round103-{name}.json').read_text())
            assert d['exit_code']==0 and sha(d['log'])==d['log_sha256']
        coverage=json.loads((temp/'cmm-round103-local-coverage.json').read_text())
        assert coverage['passed'] and all(coverage[k]==v for k,v in cfg['counts'].items())
        for item in coverage['records']:assert sha(root/item['path'])==item['sha256'],item['path']
        report=json.loads((root/'research/ingests/round103-frontier-20261015.json').read_text())
        assert report['counts']==cfg['counts'] and report['base']==cfg['base']
        paths=['README.md','pages','research/sources/round103-electrolyte','research/sources/round103-borates','research/sources/round103-ree-phosphates','research/sources/round103-uranium','research/ingests/round103-frontier-20261015.json','research/ingests/round103-frontier-20261015.md','research/ingests/round103-checks-20261015','reviews/publication/20261015-round103']
        paths += [f'data/records/{s}.yaml' for s in cfg['slugs']]
        paths += [f'history/records/{s}' for s in cfg['slugs']]
        review_paths=sorted({str(Path(item['review']['path']).parent) for item in report['records']})
        assert len(review_paths)==7
        paths += review_paths
        git('add','--',*paths)
        files=git('diff','--cached','--name-only').splitlines()
        assert files and all(any(f==p or f.startswith(p+'/') for p in paths) for f in files)
        assert not git('diff','--name-only'),'Unstaged tracked changes remain'
        git('diff','--cached','--check')
        hashes={p:sha(root/p) for p in files}
        git('commit','-m',cfg['title'])
        assert not git('status','--porcelain=v1','--untracked-files=all')
        head=git('rev-parse','HEAD');tree=git('rev-parse','HEAD^{tree}')
        assert git('rev-list','--parents','-n','1','HEAD').split()==[head,cfg['base']]
        receipt.update(exit_code=0,head=head,tree=tree,files=files,hashes=hashes,config_sha256=sha(temp/'cmm-round103-helper-config.json'),verification_helper_sha256=sha(temp/'cmm-round103-isolated-verification.py'),coverage_helper_sha256=sha(temp/'cmm-round103-isolated-coverage.py'))
    except Exception as error:receipt.update(exit_code=1,error=str(error))
    receipt['finished_at']=now();json.dump(receipt,stream,indent=2);stream.write('\n')
print(json.dumps({k:v for k,v in receipt.items() if k not in ('commands','files','hashes')},indent=2))
raise SystemExit(receipt['exit_code'])
