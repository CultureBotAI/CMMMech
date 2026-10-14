"""Publish the completed, verified round67 outcome without closing source gaps."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess
p=Path('/private/tmp');repo='CultureBotAI/CMMMech'
load=lambda n:json.loads((p/f'cmm-round67-{n}.json').read_text())
sha=lambda q:hashlib.sha256(Path(q).read_bytes()).hexdigest()
c,cl,post,hosted,sync=[load(n) for n in ['commit-receipt','pr-cleanup','postmerge-merged-terminal','hosted-audit-final','main-preservation-after']]
assert cl['local_branch_absent'] and cl['remote_branch_absent'] and sync['passed']
assert post['exit_code']==0 and post['merge_commit']==cl['merge'] and post['expected_tree']==c['tree'] and sha(post['log'])==post['log_sha256']
assert hosted['passed'] and hosted['all_five_hosted_runs_and_jobs_succeeded'] and hosted['merge']==cl['merge'] and hosted['tree']==c['tree']
assert sync['head']==cl['merge'] and sync['tree']==c['tree'] and sync['main_clean'] and sync['main_nontracked_preserved'] and sync['unrelated_skill_preserved']
pr=json.loads(subprocess.check_output(['gh','pr','view',str(cl['pr']),'--repo',repo,'--json','state,mergeCommit,headRefOid'],text=True))
assert pr['state']=='MERGED' and pr['mergeCommit']['oid']==cl['merge'] and pr['headRefOid']==c['head']
body=p/'cmm-round67-closeout.md';out=p/'cmm-round67-closeout-posted.json';assert not body.exists() and not out.exists()
runs='\n'.join('- '+role.replace('_',' ')+': [passed]('+v['url']+')' for role,v in hosted['runs'].items())
body.write_text(f'''Merged through the native queue as `{cl['merge']}`. The actual squash has the reviewed tree `{c['tree']}` and trusted main parent `{c['base']}`. The topic branch is deleted locally and remotely; the owned worktree is clean and detached. Original main was fast-forwarded after verification, preserving hidden/ignored files and the unrelated skill worktree.

Seven independent exact-byte scientific reviews and the publication audit passed with documented source limitations. A suspected thesis defense-year discrepancy was tested and rejected using the university's explicit 1994 defense metadata; no invented corrective issue or record change was made. Source follow-up #210 remains open for the unavailable Choi supplement and assay reconciliation; earlier #194, #198 and #207 remain open.

Fresh remote-main verification after branch deletion passed `just check` (317 passed, 3 skipped), nonempty validation (312 records), trusted-base history (362 sessions), structured reviews (373 bundles), and exact current scientific coverage (312/312; 68 available review bases). Both isolated preflight and postmerge checks verified the topic commit absent from the main/tag clone and retained provenance available.

All five exact hosted workflows and their jobs passed:
{runs}

The [round67 report](https://github.com/{repo}/blob/{cl['merge']}/research/ingests/round67-frontier-20261014.md) links the per-record reviews and remaining source priorities. This completes publication of this batch; discovery is not exhausted.
''')
url=subprocess.check_output(['gh','pr','comment',str(cl['pr']),'--repo',repo,'--body-file',str(body)],text=True).strip()
assert url.startswith('https://github.com/'+repo+'/pull/'+str(cl['pr'])+'#issuecomment-')
comment_id=url.rsplit('-',1)[1];saved=json.loads(subprocess.check_output(['gh','api',f'repos/{repo}/issues/comments/{comment_id}'],text=True))
assert saved['body']==body.read_text() and saved['html_url']==url
out.write_text(json.dumps({'recorded_at':datetime.now(timezone.utc).isoformat(),'pr':cl['pr'],'merge':cl['merge'],'url':url,'body_sha256':sha(body),'comment':saved},indent=2)+'\n')
print(json.dumps({'url':url,'merge':cl['merge']},indent=2))
