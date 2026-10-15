from pathlib import Path
import argparse,datetime,hashlib,json,os,stat,subprocess
T=Path('/private/tmp');M=Path('/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CMMMech');BASE='e8cfa60c53e4c94c6093e23fe983cc71fb59e12f';HEAD='cf20cb0681d34d516fffd4985a27dfc8c1ed3982';TREE='3e4c9d804d9e11e6d05a83ba8ff70c338572d6df';BRANCH='curate/cmm-expansion-round101-20261015'
a=argparse.ArgumentParser();a.add_argument('--postmerge',required=True);a.add_argument('--hosted-assessment',required=True);args=a.parse_args();now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
out=T/'cmm-round101-final-preservation.json';slot=out.open('x');r={'started_at':now(),'commands':[]};json.dump({'state':'in_progress'},slot);slot.flush()
def run(cmd,allowed=(0,)):
 p=subprocess.run(cmd,cwd=M,capture_output=True,text=True);r['commands'].append({'at':now(),'command':cmd,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr});assert p.returncode in allowed,(cmd,p.stderr);return p.stdout.strip()
def git(*a,**kw):return run(['git',*a],**kw)
def baseline_unchanged(d):
 for name,b in d['main']['files'].items():
  x=M/name
  if b['kind']=='symlink':assert x.is_symlink() and os.readlink(x)==b['target'] and stat.S_IMODE(x.lstat().st_mode)==b['mode'],name
  else:assert x.is_file() and not x.is_symlink() and x.stat().st_size==b['bytes'] and sha(x)==b['sha256'] and stat.S_IMODE(x.stat().st_mode)==b['mode'],name
try:
 p=json.loads(Path(args.postmerge).read_text());assert p['mode']=='postmerge' and p['exit_code']==0 and p['trusted_base']==BASE and p['topic_head']==HEAD and p['expected_tree']==TREE;MERGE=p['merge_commit'];assert sha(p['log'])==p['log_sha256'];assert sha(p['coverage']['path'])==p['coverage']['sha256'];assert all(c['exit_code'] in c['allowed_exit_codes'] for c in p['commands'])
 c=json.loads((T/'cmm-round101-cleanup-receipt.json').read_text());assert c['exit_code']==0 and c['merge_commit']==MERGE and c['local_branch_absent'] and c['remote_branch_absent']
 # The hosted assessment is manually inspected by the coordinator before invocation.
 h=json.loads(Path(args.hosted_assessment).read_text());r['hosted_assessment']={'path':args.hosted_assessment,'sha256':sha(args.hosted_assessment)}
 before=T/'cmm-round101-preservation-before.json';d=json.loads(before.read_text());assert sha(before)=='c1b380957c987c2217e510490baff408c961234e2f5ea3935701be3518a06ca9';assert Path(d['main']['path'])==M
 assert git('branch','--show-current')=='main' and git('rev-parse','HEAD')==BASE and not git('status','--porcelain=v1','--untracked-files=all');baseline_unchanged(d)
 assert git('ls-remote','origin','refs/heads/main').split()==[MERGE,'refs/heads/main']
 git('fetch','origin','main','--tags');assert git('rev-parse','origin/main')==MERGE;assert git('rev-list','--parents','-n','1',MERGE).split()==[MERGE,BASE];assert git('rev-parse',MERGE+'^{tree}')==TREE
 git('merge','--ff-only',MERGE);assert git('rev-parse','HEAD')==MERGE and not git('status','--porcelain=v1','--untracked-files=all');baseline_unchanged(d)
 git('show-ref','--verify','--quiet','refs/heads/'+BRANCH,allowed=(1,));assert not git('ls-remote','origin','refs/heads/'+BRANCH)
 tag='refs/tags/review-base/cmm-source-survey-20261009';assert git('rev-parse',tag)=='fc4040c3abcd28f0a9cc52467e308100144ad1fd';assert git('rev-parse',tag+'^{}')=='c0adc2c0763e1515ed07dc712b024974d98fb342'
 remote=git('ls-remote','origin',tag,tag+'^{}');assert dict(line.split()[::-1] for line in remote.splitlines())=={tag:'fc4040c3abcd28f0a9cc52467e308100144ad1fd',tag+'^{}':'c0adc2c0763e1515ed07dc712b024974d98fb342'}
 r.update(exit_code=0,main=str(M),base=BASE,merge_commit=MERGE,tree=TREE,branch_deleted=BRANCH,preserved_nontracked_entries=len(d['main']['files']),baseline_path=str(before),baseline_sha256=sha(before),preservation_scope='Every pre-existing nontracked entry including hidden/ignored files, byte count, SHA256, mode and symlink target; no project environment command ran in original main.',postmerge={'path':args.postmerge,'sha256':sha(args.postmerge)},retained_remote_tag=remote,worktrees_after=git('worktree','list','--porcelain'))
except Exception as e:r.update(exit_code=1,error=str(e))
finally:
 r['finished_at']=now();slot.seek(0);json.dump(r,slot,indent=2);slot.write('\n');slot.truncate();slot.close();print(json.dumps({k:v for k,v in r.items() if k not in ['commands','worktrees_after']},indent=2))
raise SystemExit(r['exit_code'])
