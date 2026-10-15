from pathlib import Path
from datetime import datetime,timezone
import subprocess,json
p=Path('/private/tmp');r=p/'CMMMech-expansion-round92-20261015';c=json.loads((p/'cmm-round92-commit-receipt.json').read_text());done=json.loads((p/'cmm-round92-pr-cleanup.json').read_text());out=p/'cmm-round92-tracking-cleanup.json';assert not out.exists()
def git(*a):return subprocess.check_output(['git','-C',str(r),*a],text=True).strip()
assert done['head']==c['head'] and done['local_branch_absent'] and done['remote_branch_absent']
assert not git('ls-remote','origin','refs/heads/'+c['branch'])
ref='refs/remotes/origin/'+c['branch'];x=subprocess.run(['git','-C',str(r),'show-ref','--verify','--hash',ref],capture_output=True,text=True)
assert x.returncode in [0,1]
if x.returncode==0:
 assert x.stdout.strip()==c['head'];subprocess.run(['git','-C',str(r),'update-ref','-d',ref,c['head']],check=True)
assert subprocess.run(['git','-C',str(r),'show-ref','--verify','--quiet',ref]).returncode==1
out.write_text(json.dumps({'recorded_at':datetime.now(timezone.utc).isoformat(),'ref':ref,'previous_value':x.stdout.strip() or None,'absent':True,'scope':'Removed only owned stale remote-tracking ref with expected-old-value guard; no pruning.'},indent=2)+'\n')
print('Owned tracking ref absent.')
