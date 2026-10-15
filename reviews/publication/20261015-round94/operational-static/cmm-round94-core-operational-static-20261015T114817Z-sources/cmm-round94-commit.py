from pathlib import Path
from datetime import datetime,timezone
import subprocess,json,hashlib
r=Path('/private/tmp/CMMMech-expansion-round94-20261015');p=Path('/private/tmp');cfg=json.loads((p/'cmm-round94-helper-config.json').read_text());out=p/'cmm-round94-commit-receipt.json';assert not out.exists()
def git(*a):return subprocess.check_output(['git','-C',str(r),*a],text=True).strip()
assert git('branch','--show-current')==cfg['branch'] and git('rev-parse','HEAD')==cfg['base']
for filename in ['cmm-round94-final-gates.json','cmm-round94-review-check-final.json']:
 d=json.loads((p/filename).read_text());assert d['exit_code']==0 and hashlib.sha256(Path(d['log']).read_bytes()).hexdigest()==d['log_sha256']
coverage=json.loads((p/'cmm-round94-local-coverage.json').read_text());assert coverage['passed']
for rec in coverage['records']:assert hashlib.sha256((r/rec['path']).read_bytes()).hexdigest()==rec['sha256']
paths=['README.md','pages','research/ingests/round94-frontier-20261015.md','research/ingests/round94-frontier-20261015.json','research/ingests/round94-checks-20261015','reviews/publication/20261015-round94']
for slug in cfg['slugs']:paths.extend(['data/records/'+slug+'.yaml','history/records/'+slug])
paths.extend(str(q.relative_to(r)) for q in (r/'research/sources').glob('round94-*'))
paths.extend(str(q.relative_to(r)) for q in (r/'reviews/structured').glob('*round94*'))
subprocess.run(['git','-C',str(r),'add','--',*paths],check=True)
rawlogs=['research/ingests/round94-checks-20261015/final-gates.log','research/ingests/round94-checks-20261015/baseline.log']
subprocess.run(['git','-C',str(r),'diff','--cached','--check','--','.',*[':(exclude)'+x for x in rawlogs]],check=True)
for logfile in rawlogs:subprocess.run(['git','-C',str(r),'-c','core.whitespace=-blank-at-eof','diff','--cached','--check','--',logfile],check=True)
for label in ['baseline','final-gates']:
 receipt=json.loads((p/f'cmm-round94-{label}.json').read_text());assert hashlib.sha256((r/f'research/ingests/round94-checks-20261015/{label}.log').read_bytes()).hexdigest()==receipt['log_sha256']
assert not git('diff','--name-only') and not git('ls-files','--others','--exclude-standard')
files=git('diff','--cached','--name-only').splitlines();assert files
subprocess.run(['git','-C',str(r),'commit','-m',cfg['title']],check=True)
head=git('rev-parse','HEAD');tree=git('rev-parse','HEAD^{tree}')
assert git('rev-parse','HEAD^')==cfg['base'] and not git('status','--porcelain=v1','--untracked-files=all')
d={'recorded_at':datetime.now(timezone.utc).isoformat(),'base':cfg['base'],'head':head,'tree':tree,'branch':cfg['branch'],'worktree':str(r),'files':files,'clean':True,'whitespace_note':'Verbatim baseline/final check logs preserve original bytes and hashes; only blank-at-eof is disabled for those exact two logs. All maintained content uses normal whitespace checks.'}
out.write_text(json.dumps(d,indent=2)+'\n');print(json.dumps({k:v for k,v in d.items() if k!='files'},indent=2))
