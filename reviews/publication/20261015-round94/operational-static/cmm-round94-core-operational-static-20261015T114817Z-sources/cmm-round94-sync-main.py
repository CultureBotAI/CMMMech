from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,os,stat,subprocess
p=Path('/private/tmp');before=json.loads((p/'cmm-round94-preservation-before.json').read_text());r=Path(before['main']['path']);c=json.loads((p/'cmm-round94-commit-receipt.json').read_text());cleanup=json.loads((p/'cmm-round94-pr-cleanup.json').read_text());post=json.loads((p/'cmm-round94-postmerge-published-terminal.json').read_text());out=p/'cmm-round94-main-sync.json';assert not out.exists()
def git(*a):return subprocess.check_output(['git','-C',str(r),*a],text=True).strip()
def sha(q):return hashlib.sha256(q.read_bytes()).hexdigest()
def check_originals():
 for name,b in before['main']['files'].items():
  q=r/name
  if b['kind']=='symlink':assert q.is_symlink() and os.readlink(q)==b['target'] and stat.S_IMODE(q.lstat().st_mode)==b['mode'],name
  else:assert q.is_file() and not q.is_symlink() and q.stat().st_size==b['bytes'] and sha(q)==b['sha256'] and stat.S_IMODE(q.stat().st_mode)==b['mode'],name
 assert sha(Path(before['durable_backup_manifest']))==before['durable_backup_manifest_sha256']
 assert git('rev-parse','refs/tags/review-base/cmm-source-survey-20261009')==before['retained_tag']['object']
 assert git('rev-parse','refs/tags/review-base/cmm-source-survey-20261009^{commit}')==before['retained_tag']['peeled_commit']
merge=cleanup['merge'];assert cleanup['local_branch_absent'] and cleanup['remote_branch_absent']
assert post['exit_code']==0 and post['mode']=='postmerge' and post['merge_commit']==merge and post['expected_tree']==c['tree'] and post['topic_head']==c['head'] and post['trusted_base']==c['base']
assert sha(Path(post['log']))==post['log_sha256'] and all(x['exit_code'] in x['allowed_exit_codes'] for x in post['commands'])
for cmd in [['uv','run','--locked','cmmmech','validate','--require-records'],['uv','run','--locked','cmmmech','validate-history','--base',c['base']],['just','review-check','--base',c['base'],'--require-reviews']]:assert any(x['command']==cmd and x['exit_code']==0 for x in post['commands'])
check_originals();assert git('branch','--show-current')=='main' and git('rev-parse','HEAD')==c['base'] and not git('status','--porcelain=v1','--untracked-files=all')
assert git('ls-remote','origin','refs/heads/main').split()==[merge,'refs/heads/main']
assert git('rev-parse',merge+'^{tree}')==c['tree'] and git('rev-list','--parents','-n','1',merge).split()==[merge,c['base']]
raw=subprocess.check_output(['git','-C',str(r),'ls-files','--others','-z']);nontracked={os.fsdecode(x) for x in raw.split(b'\0') if x}
raw=subprocess.check_output(['git','-C',str(r),'ls-tree','-r','-z','--name-only',merge]);incoming={os.fsdecode(x) for x in raw.split(b'\0') if x}
for group,other in [(incoming,nontracked),(nontracked,incoming)]:
 for name in group:assert name not in other and not {str(q) for q in Path(name).parents if str(q)!='.'}.intersection(other),name
subprocess.run(['git','-C',str(r),'merge','--ff-only','--no-edit','--no-autostash',merge],check=True,stdout=subprocess.DEVNULL)
check_originals();assert git('branch','--show-current')=='main' and git('rev-parse','HEAD')==merge and git('rev-parse','HEAD^{tree}')==c['tree'] and not git('status','--porcelain=v1','--untracked-files=all')
d={'recorded_at':datetime.now(timezone.utc).isoformat(),'passed':True,'merge':merge,'tree':c['tree'],'main':str(r),'main_clean':True,'baseline_nontracked_entries_preserved':len(before['main']['files']),'retained_tag_preserved':True,'durable_backup_manifest_preserved':True,'scope':'Fast-forwarded only clean main at reviewed base, after exact published-tree checks and hidden/ignored path-conflict checks. All original nontracked entries preserved. No unrelated checkout restoration/deletion/pruning.'};out.write_text(json.dumps(d,indent=2)+'\n');print(json.dumps(d,indent=2))
