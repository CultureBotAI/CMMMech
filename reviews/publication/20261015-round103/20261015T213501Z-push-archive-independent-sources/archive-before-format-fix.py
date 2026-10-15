from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,stat,subprocess
T=Path('/private/tmp');M=Path('/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CMMMech');archive=M/'reports/publication/round103-20261015'
load=lambda n:json.loads((T/f'cmm-round103-{n}.json').read_text())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();now=lambda:datetime.now(timezone.utc).isoformat()
out=T/'cmm-round103-archive-receipt.json'
slot=out.open('x')
receipt={'started_at':now(),'state':'in_progress'}
json.dump(receipt,slot,indent=2);slot.flush()
try:
    cfg=load('helper-config');commit=load('commit-receipt');final=load('final-preservation');pr=load('pr-created')['pr'];hosted=load('hosted-final-assessment')
    assert final['exit_code']==commit['exit_code']==0
    merge=final['merge_commit'];head=commit['head'];tree=commit['tree'];branch=cfg['branch']
    def git(*args,allowed=(0,)):
     p=subprocess.run(['git','-C',str(M),*args],capture_output=True,text=True);assert p.returncode in allowed,(args,p.stderr);return p.stdout.strip()
    assert git('branch','--show-current')=='main' and git('rev-parse','HEAD')==merge
    assert git('rev-parse','HEAD^{tree}')==tree and not git('status','--porcelain=v1','--untracked-files=all')
    assert not archive.exists() and not archive.is_symlink() and archive.parent.resolve().is_relative_to(M.resolve())
    git('check-ignore','-q',str(archive/'manifest.json'));archive.mkdir();files=[]
    def copy(src,dst):
     assert src.is_file() and not src.is_symlink();data=src.read_bytes();digest=hashlib.sha256(data).hexdigest();dst.parent.mkdir(parents=True,exist_ok=True)
     with dst.open('xb') as f:f.write(data)
     assert sha(src)==digest and sha(dst)==digest
     files.append({'path':str(dst.relative_to(archive)),'source':str(src),'bytes':len(data),'sha256':digest})
    for p in sorted(T.iterdir()):
     if p.name.startswith('cmm-round103-') and p.is_file() and not p.is_symlink() and p.suffix in ('.json','.md','.py','.log') and p.name!='cmm-round103-archive-receipt.json':copy(p,archive/'receipts'/p.name)
    selected=[]
    for name in ('cmm-round103-release-review','cmm-round103-hosted-final','cmm-round103-operational-guard-audit','cmm-round103-hosted-independent','cmm-round103-helper-audit'):
     root=T/name
     if not root.exists():continue
     assert root.is_dir() and not root.is_symlink();selected.append(str(root))
     for p in sorted(root.rglob('*')):
      if p.is_file() and not p.is_symlink() and p.suffix in ('.json','.md','.py','.log','.stderr','.diff','.txt'):copy(p,archive/name/p.relative_to(root))
    summary=f'''# Round103 publication receipt

    PR: {pr['html_url']}
    Merged commit: `{merge}`
    Reviewed topic commit: `{head}`
    Reviewed and merged tree: `{tree}`

    Seven added records: autunite, inyoite, rhabdophane-(Ce), rhabdophane-(La), spent vanadium-flow-battery electrolyte, szaibelyite and torbernite. Corpus total: {cfg['counts']['record_count']}. Each new owner requires CREATE history and independent scientific review; exact final coverage is retained in the final receipts. See `research/ingests/round103-frontier-20261015.md` for owners, paired reviews and source dossiers.

    Validation and issue dispositions: ROUND103_FINAL_VALIDATION_AND_ISSUE_SUMMARY. Populate from actual terminal local, isolated and hosted evidence before execution; no earlier round results are inherited.

    The branch `{branch}` was deleted locally and remotely. Its clean detached worktree remains at `/private/tmp/CMMMech-expansion-round103-20261015`. Original main advanced only by fast-forward. All pre-existing nontracked entries, including hidden/ignored environment files, are verified below against the round103 preservation inventory. The annotated review-base evidence tag is unchanged.

    This additive ignored local archive preserves publication evidence; `manifest.json` hashes every archived file except itself. Raw primary PDFs/XML/images remain outside Git in documented source-research directories and are not copied here. No existing archive was overwritten. Provenance coverage does not repeat every historical scientific review. No source-exhaustion claim is made.
    '''
    p=archive/'README.md'
    with p.open('x') as f:f.write(summary)
    files.append({'path':'README.md','source':'generated publication summary','bytes':p.stat().st_size,'sha256':sha(p)})
    before=load('preservation-before')
    for name,v in before['main']['files'].items():
     p=M/name
     if v['kind']=='symlink':assert p.is_symlink() and os.readlink(p)==v['target'] and stat.S_IMODE(p.lstat().st_mode)==v['mode'],name
     else:assert p.is_file() and not p.is_symlink() and p.stat().st_size==v['bytes'] and sha(p)==v['sha256'] and stat.S_IMODE(p.stat().st_mode)==v['mode'],name
    assert not git('status','--porcelain=v1','--untracked-files=all') and git('rev-parse','HEAD')==merge
    git('show-ref','--verify','--quiet','refs/heads/'+branch,allowed=(1,))
    manifest={'recorded_at':now(),'archive':str(archive),'pr':pr['html_url'],'merge_commit':merge,'topic_head':head,'tree':tree,'files':sorted(files,key=lambda x:x['path']),'preserved_nontracked_entries_after_archive':len(before['main']['files']),'final_preservation_sha256':sha(T/'cmm-round103-final-preservation.json'),'selected_audit_directories':selected,'scope':'Published round103 lifecycle evidence. Hidden/ignored names included in selected directory enumeration; symlinks not copied. Manifest excludes itself; no existing path overwritten.'}
    p=archive/'manifest.json'
    with p.open('x') as f:json.dump(manifest,f,indent=2);f.write('\n')
    for item in files:assert sha(archive/item['path'])==item['sha256']
    result={'recorded_at':now(),'passed':True,'archive':str(archive),'manifest':str(p),'manifest_sha256':sha(p),'archived_files':len(files),'preserved_nontracked_entries':len(before['main']['files']),'main_clean':not git('status','--porcelain=v1','--untracked-files=all'),'main_head':git('rev-parse','HEAD')}
    receipt.update(result,exit_code=0)
except Exception as error:
    receipt.update(passed=False,exit_code=1,error=repr(error))
finally:
    receipt.update(state='completed',finished_at=now())
    slot.seek(0);json.dump(receipt,slot,indent=2);slot.write('\n');slot.truncate();slot.close()
print(json.dumps(receipt,indent=2))
raise SystemExit(receipt['exit_code'])
