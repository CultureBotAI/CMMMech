from pathlib import Path
import json,subprocess,hashlib,datetime,argparse,os,stat
W=Path('/private/tmp/CMMMech-expansion-round96-20261015');T=Path('/private/tmp')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def git(*a):return subprocess.check_output(['git',*a],cwd=W,text=True).strip()
def files_under(directory,pattern):return {str(p.relative_to(W)):sha(p) for p in sorted((W/directory).rglob(pattern)) if p.is_file() and not p.is_symlink()}
def guard(cfg,g,rv,cv,prep,actual,records,histories,reviews,bindings):
 base=cfg['base'];expected=[['just','check'],['uv','run','--locked','cmmmech','validate','--require-records'],['uv','run','--locked','cmmmech','validate-history','--base',base],['uv','run','--locked','python','scripts/render_pages.py','--check']]
 assert g['base']==base and g['worktree']==str(W) and g['exit_code']==0 and g['inputs_unchanged']
 assert [x['command'] for x in g['commands']]==expected and all(x['exit_code']==0 for x in g['commands'])
 assert rv['base']==base and rv['exit_code']==0 and rv['command']==['just','review-check','--base',base,'--require-reviews']
 assert cv['passed'] and cv['root']==str(W) and all(cv[k]==v for k,v in cfg['counts'].items())
 assert records==g['record_inputs']=={x['path']:x['sha256'] for x in cv['records']}
 assert len(records)==cfg['counts']['record_count'] and len(histories)==cfg['counts']['history_count'] and len(reviews)==cfg['counts']['structured_review_count']
 assert all(x['matching_scientific_reviews'] for x in cv['records']) and all(x['available_commit'] for x in cv['bases'])
 assert prep['passed'] is True and prep['base']==base and prep['head']==base
 assert prep['files']==actual and prep['record_inputs']==records and prep['history_inputs']==histories and prep['review_inputs']==reviews and prep['bindings']==bindings

def collect():
 import yaml
 cfg=json.loads((T/'cmm-round96-helper-config.json').read_text());names=['helper-config','final-gates','review-check-final','local-coverage','preservation-precommit'];data={n:json.loads((T/f'cmm-round96-{n}.json').read_text()) for n in names};prep=json.loads((T/'cmm-round96-publication-prepared.json').read_text())
 assert git('branch','--show-current')==cfg['branch'] and git('rev-parse','HEAD')==cfg['base']
 preservation=data['preservation-precommit'];assert preservation['passed'] and preservation['base']==cfg['base']
 before_path=Path(preservation['before_receipt']);assert sha(before_path)==preservation['before_sha256'];before=json.loads(before_path.read_text());main=Path(before['main']['path'])
 assert preservation['nontracked_entries_preserved']==len(before['main']['files'])
 assert subprocess.check_output(['git','-C',str(main),'rev-parse','HEAD'],text=True).strip()==cfg['base']
 assert not subprocess.check_output(['git','-C',str(main),'status','--porcelain=v1','--untracked-files=all'],text=True).strip()
 for name,b in before['main']['files'].items():
  q=main/name
  if b['kind']=='symlink':assert q.is_symlink() and os.readlink(q)==b['target'] and stat.S_IMODE(q.lstat().st_mode)==b['mode']
  else:assert q.is_file() and not q.is_symlink() and q.stat().st_size==b['bytes'] and sha(q)==b['sha256'] and stat.S_IMODE(q.stat().st_mode)==b['mode']
 assert not git('diff','--cached','--name-only') and not git('diff','--name-only','--diff-filter=D')
 files=sorted(set(git('diff','--name-only').splitlines()+git('ls-files','--others','--exclude-standard').splitlines()))
 allowed=('data/records/','history/records/','research/sources/round96-','research/ingests/round96-','reviews/structured/20261015','reviews/publication/20261015-round96/','pages/')
 assert files and all(x=='README.md' or x.startswith(allowed) for x in files)
 for f in files:assert (W/f).is_file() and not (W/f).is_symlink()
 actual={f:sha(W/f) for f in files};records=files_under('data/records','*.yaml');histories=files_under('history/records','*.yaml');reviews=files_under('reviews/structured','review.yaml')
 bindings={f'cmm-round96-{n}.json':sha(T/f'cmm-round96-{n}.json') for n in names};bindings['cmm-round96-commit.py']=sha(Path(__file__))
 for n in ['final-gates','review-check-final']:
  r=data[n];assert sha(Path(r['log']))==r['log_sha256'];bindings[Path(r['log']).name]=sha(Path(r['log']))
 guard(cfg,data['final-gates'],data['review-check-final'],data['local-coverage'],prep,actual,records,histories,reviews,bindings)
 # Reconcile the coverage attestation with actual current scientific reviews and linked history.
 for item in data['local-coverage']['records']:
  d=yaml.safe_load((W/item['path']).read_text());assert d['id']==item['id'];valid=[]
  for match in item['matching_scientific_reviews']:
   rp=W/match['path'];assert sha(rp)==match['review_sha256'];r=yaml.safe_load(rp.read_text());assert r['scientific_review'] and r['completion']=='completed' and r['verdict'] in ['pass','pass_with_limitations']
   assert d['id'] in r['scope']['reviewed_target_ids'] and any(t['path']==item['path'] and t['target_id']==d['id'] for t in r['targets'])
   assert any(i['path']==item['path'] and i['sha256']==item['sha256'] for i in r['source']['inputs'])
   if d['id'] in ['cmmmech:'+s for s in cfg['slugs']]:
    assert r['reviewer']['independence']=='independent' and r['source']['git_revision']==cfg['base']
    for i in r['source']['inputs']:assert sha(W/i['path'])==i['sha256']
    for h in d['history_refs']:assert any(i['path']==h and i['sha256']==histories[h] for i in r['source']['inputs'])
   valid.append(r)
  assert valid
 # Existing historical records/reviews are append-only; no old owner or sidecar is changed in this batch.
 for f in files:
  if f.startswith(('data/records/','history/records/','reviews/structured/')):
   x=subprocess.run(['git','cat-file','-e',cfg['base']+':'+f],cwd=W,capture_output=True);assert x.returncode!=0
 assert git('ls-remote','origin','refs/heads/main').split()[0]==cfg['base']
 subprocess.run(['git','diff','--check'],cwd=W,check=True)
 return cfg,files,actual,bindings

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--check-only',action='store_true');args=parser.parse_args();out=T/'cmm-round96-commit-receipt.json'
 # First guard: no index/commit mutation is allowed when the output already exists.
 assert not out.exists() and not out.is_symlink(), 'Commit receipt path already exists'
 cfg,files,actual,bindings=collect()
 if args.check_only:print('Current prepared publication and gate bindings pass; no Git mutation.');return
 assert not out.exists() and not out.is_symlink()
 subprocess.run(['git','add','--',*files],cwd=W,check=True)
 assert sorted(git('diff','--cached','--name-only').splitlines())==files
 for f in files:
  staged=subprocess.check_output(['git','show',':'+f],cwd=W);assert hashlib.sha256(staged).hexdigest()==actual[f]
 subprocess.run(['git','diff','--cached','--check'],cwd=W,check=True)
 assert bindings['cmm-round96-commit.py']==sha(Path(__file__))
 subprocess.run(['git','commit','-m',cfg['title']],cwd=W,check=True)
 assert not git('status','--porcelain=v1','--untracked-files=all')
 d={'recorded_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'base':cfg['base'],'branch':cfg['branch'],'clean':True,'worktree':str(W),'head':git('rev-parse','HEAD'),'tree':git('rev-parse','HEAD^{tree}'),'files':files,'hashes':actual,'preparation_sha256':sha(T/'cmm-round96-publication-prepared.json'),'bindings':bindings}
 with out.open('x') as stream:stream.write(json.dumps(d,indent=2)+'\n')
 print(json.dumps({k:v for k,v in d.items() if k not in ['files','hashes','bindings']},indent=2))
if __name__=='__main__':main()
