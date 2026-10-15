from pathlib import Path
from datetime import datetime,timezone
import json,runpy,hashlib,os
p=Path('/private/tmp');lib=runpy.run_path(str(p/'cmm-round57-recover-original.py'),run_name='snapshot_library');snapshot=lib['snapshot'];git=lib['git'];textgit=lib['textgit'];main=lib['MAIN'];skill=lib['SKILL'];sha=lib['sha'];out=p/'cmm-round90-main-sync.json';assert not out.exists()
before=json.loads((p/'cmm-round90-preservation-before.json').read_text());c=json.loads((p/'cmm-round90-commit-receipt.json').read_text());cleanup=json.loads((p/'cmm-round90-pr-cleanup.json').read_text());post=json.loads((p/'cmm-round90-postmerge-published-terminal.json').read_text());merge=cleanup['merge']
assert cleanup['local_branch_absent'] and cleanup['remote_branch_absent'] and cleanup['tree']==c['tree'] and cleanup['head']==c['head']
assert post['exit_code']==0 and post['mode']=='postmerge' and post['merge_commit']==merge and post['trusted_base']==c['base'] and post['expected_tree']==c['tree'] and post['topic_head']==c['head']
assert sha(post['log'])==post['log_sha256'] and all(x['exit_code'] in x['allowed_exit_codes'] for x in post['commands'])
for required in [['uv','run','--locked','cmmmech','validate','--require-records'],['uv','run','--locked','cmmmech','validate-history','--base',c['base']],['just','review-check','--base',c['base'],'--require-reviews']]:
 assert any(x['command']==required and x['exit_code']==0 for x in post['commands'])
gates=json.loads((p/'cmm-round90-final-gates.json').read_text());assert gates['exit_code']==0 and gates['inputs_unchanged'] and sha(gates['log'])==gates['log_sha256']
assert any(x['command']==['just','check'] and x['exit_code']==0 for x in gates['commands'])
assert post['counts']==json.loads((p/'cmm-round90-helper-config.json').read_text())['counts']
deviation=json.loads((p/'cmm-round90-preservation-precommit.json').read_text());assert deviation['passed'] and deviation['main_preserved'] and deviation['unrelated_skill_preserved'] is False
for x in deviation['dirty_edit_backups']:assert lib['identity'](Path(x['backup']))==x['identity']
a=snapshot(main,False);assert a==before['snapshots']['main'];assert lib['retained_tag']()==before['retained_tag']
assert a['branch']=='main' and a['head']==c['base'] and not a['status']
assert textgit(main,'ls-remote','origin','refs/heads/main').split()[0]==merge
assert textgit(main,'rev-parse','origin/main')==merge and textgit(main,'rev-parse',merge+'^{tree}')==c['tree']
assert textgit(main,'rev-list','--parents','-n','1',merge).split()==[merge,c['base']]
incoming={os.fsdecode(x) for x in git(main,'ls-tree','-r','-z','--name-only',merge).split(b'\0') if x};nontracked=set(a['files'])
for group,other in [(incoming,nontracked),(nontracked,incoming)]:
 for name in group:assert name not in other and not {str(q) for q in Path(name).parents if str(q)!='.'}.intersection(other),name
git(main,'merge','--ff-only','--no-edit','--no-autostash',merge)
after=snapshot(main,False)
assert after['head']==merge and after['tree']==c['tree'] and after['branch']=='main' and not after['status'] and after['files']==a['files']
assert lib['retained_tag']()==before['retained_tag']
d={'recorded_at':datetime.now(timezone.utc).isoformat(),'passed':True,'merge':merge,'tree':c['tree'],'main':str(main),'main_clean':True,'main_nontracked_preserved':True,'unrelated_skill_preserved':False,'unrelated_skill_deviation_receipt':str(p/'cmm-round90-preservation-precommit.json'),'dirty_edits_backup_verified':True,'retained_tag_preserved':True,'preserved_entry_counts':{'main':len(after['files']),'skill_baseline':len(before['snapshots']['skill']['files'])},'scope':before['snapshots']['main']['scope']+'; unrelated skill deviation recorded separately, no restoration or deletion performed','postmerge_receipt_sha256':sha(p/'cmm-round90-postmerge-published-terminal.json')}
out.write_text(json.dumps(d,indent=2)+'\n');print(json.dumps(d,indent=2))
