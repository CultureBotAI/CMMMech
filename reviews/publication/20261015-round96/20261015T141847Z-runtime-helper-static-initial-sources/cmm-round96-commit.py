from pathlib import Path
import json,subprocess,hashlib,datetime
T=Path('/private/tmp');W=T/'CMMMech-expansion-round96-20261015';cfg=json.loads((T/'cmm-round96-helper-config.json').read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def git(*a):return subprocess.check_output(['git',*a],cwd=W,text=True).strip()
assert git('branch','--show-current')==cfg['branch'] and git('rev-parse','HEAD')==cfg['base']
for name in ['final-gates','review-check-final','local-coverage','preservation-precommit']:
 d=json.loads((T/f'cmm-round96-{name}.json').read_text());assert d.get('exit_code',0)==0 and d.get('passed',True)
 if 'log' in d:assert sha(Path(d['log']))==d['log_sha256']
files=sorted(set(git('diff','--name-only').splitlines()+git('ls-files','--others','--exclude-standard').splitlines()))
allowed=('data/records/','history/records/','research/sources/round96-','research/ingests/round96-','reviews/structured/20261015','reviews/publication/20261015-round96/','pages/')
assert files and all(x=='README.md' or x.startswith(allowed) for x in files)
assert not git('diff','--name-only','--diff-filter=D')
assert git('ls-remote','origin','refs/heads/main').split()[0]==cfg['base']
subprocess.run(['git','diff','--check'],cwd=W,check=True)
subprocess.run(['git','add','--',*files],cwd=W,check=True)
assert sorted(git('diff','--cached','--name-only').splitlines())==files
subprocess.run(['git','commit','-m',cfg['title']],cwd=W,check=True)
assert not git('status','--porcelain=v1','--untracked-files=all')
d={'recorded_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'base':cfg['base'],'branch':cfg['branch'],'clean':True,'worktree':str(W),'head':git('rev-parse','HEAD'),'tree':git('rev-parse','HEAD^{tree}'),'files':files,'hashes':{f:sha(W/f) for f in files}}
p=T/'cmm-round96-commit-receipt.json';assert not p.exists();p.write_text(json.dumps(d,indent=2)+'\n');print(json.dumps({k:v for k,v in d.items() if k not in ['files','hashes']},indent=2))
