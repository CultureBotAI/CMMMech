"""Exercise original and corrected helpers only in isolated paths with subprocess stubs."""
from pathlib import Path
from unittest.mock import patch
import ast,contextlib,datetime,hashlib,io,json,subprocess,tempfile

A=Path('/private/tmp/cmm-round103-helpers-independent')
REAL_MAIN='/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CMMMech'
class Relocate(ast.NodeTransformer):
    def __init__(self,root,main):self.root=root;self.main=main
    def visit_Constant(self,node):
        if node.value=='/private/tmp':return ast.copy_location(ast.Constant(str(self.root)),node)
        if node.value==REAL_MAIN:return ast.copy_location(ast.Constant(str(self.main)),node)
        return node

def run_case(helper,version,occupied,missing_config=False):
    source=(A/f'{helper}-before-receipt-fix.py') if version=='before' else Path(f'/private/tmp/cmm-round103-{helper}.py')
    with tempfile.TemporaryDirectory(prefix='receipt-guard-case-',dir=A) as temp:
        root=Path(temp);main=root/'toy-main';(main/'reports/publication').mkdir(parents=True)
        h='a'*40;t='b'*40;b='c'*40;m='d'*40;branch='curate/toy-round103';title='Toy publication';effects=[]
        cfg={'base':b,'branch':branch,'title':title,'counts':{'record_count':508}}
        pr={'html_url':'https://example.invalid/pull/1','head':{'sha':h,'ref':branch},'base':{'sha':b,'ref':'main'},'title':title,'body':'toy body\n','draft':False}
        fixtures={'helper-config':cfg,'commit-receipt':{'exit_code':0,'head':h,'tree':t},'final-preservation':{'exit_code':0,'merge_commit':m},'pr-created':{'pr':pr},'hosted-final-assessment':{'passed':True},'preservation-before':{'main':{'files':{}}}}
        for name,data in fixtures.items(): (root/f'cmm-round103-{name}.json').write_text(json.dumps(data))
        if missing_config:(root/'cmm-round103-helper-config.json').unlink()
        (root/'cmm-round103-pr-body.md').write_text('toy body\n')
        out=root/('cmm-round103-pr-created.json' if helper=='push-pr' else 'cmm-round103-archive-receipt.json')
        if out.exists():out.unlink()
        target=root/'occupied-target';payload=b'preserve this receipt exactly\n'
        if occupied=='regular':out.write_bytes(payload)
        elif occupied=='symlink':target.write_bytes(payload);out.symlink_to(target)
        elif occupied=='dangling_symlink':out.symlink_to(target)
        pushed=False
        def stub_run(cmd,**kwargs):
            nonlocal pushed
            if cmd[0]=='gh':
                if cmd[1:3]==['pr','create']:effects.append('create_pr');return subprocess.CompletedProcess(cmd,0,'https://example.invalid/pull/1\n','')
                if cmd[1]=='api':return subprocess.CompletedProcess(cmd,0,json.dumps(pr),'')
                raise AssertionError(cmd)
            assert cmd[0]=='git',cmd
            args=cmd[3:] if len(cmd)>2 and cmd[1]=='-C' else cmd[1:]
            rc=0;outtext=''
            if args[:2]==['branch','--show-current']:outtext=branch if helper=='push-pr' else 'main'
            elif args[0]=='rev-parse':outtext=t if args[1]=='HEAD^{tree}' else (h if helper=='push-pr' else m)
            elif args[0]=='status':pass
            elif args[0]=='ls-remote':
                ref=args[-1]
                if ref=='refs/heads/main':outtext=b+'\t'+ref
                elif pushed:outtext=h+'\t'+ref
            elif args[0]=='push':effects.append('push_branch');pushed=True
            elif args[0]=='check-ignore':pass
            elif args[0]=='show-ref':rc=1
            else:raise AssertionError(cmd)
            return subprocess.CompletedProcess(cmd,rc,outtext+'\n' if outtext else '', '')
        tree=Relocate(root,main).visit(ast.parse(source.read_text()));ast.fix_missing_locations(tree)
        error=None;exitcode=None
        with patch('subprocess.run',stub_run),contextlib.redirect_stdout(io.StringIO()):
            try:exec(compile(tree,str(source),'exec'),{'__name__':'__main__','__file__':str(source)})
            except SystemExit as e:exitcode=e.code
            except Exception as e:error=type(e).__name__
        archive=main/'reports/publication/round103-20261015'
        archive_effect=archive.exists()
        if occupied:
            assert error=='FileExistsError',(helper,version,occupied,error,exitcode)
            if occupied=='regular':assert out.read_bytes()==payload and not out.is_symlink()
            elif occupied=='symlink':assert out.is_symlink() and target.read_bytes()==payload
            else:assert out.is_symlink() and not target.exists()
            if version=='after':assert effects==[] and not archive_effect,(effects,archive_effect)
            elif helper=='push-pr':assert effects==['push_branch','create_pr']
            else:assert archive_effect
        else:
            result=json.loads(out.read_text());assert result['state']=='completed'
            if missing_config:assert exitcode==1 and result['exit_code']==1 and not effects and not archive_effect
            else:assert exitcode==0 and result['exit_code']==0 and (effects==['push_branch','create_pr'] if helper=='push-pr' else archive_effect)
        return {'helper':helper,'version':version,'occupied':occupied,'missing_config':missing_config,'exception':error,'exit_code':exitcode,'stubbed_remote_effects':effects,'isolated_archive_created':archive_effect,'passed':True}

results=[]
for helper in ['push-pr','archive']:
    for occupied in ['regular','symlink','dangling_symlink']:
        for version in ['before','after']:results.append(run_case(helper,version,occupied))
    for missing in [False,True]:results.append(run_case(helper,'after',None,missing))
report={'finished_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'passed':True,'cases':results,'count':len(results),'isolation':'All original/corrected helper AST copies relocate both /private/tmp and original main to per-case TemporaryDirectory. subprocess.run is stubbed for the entire execution. No real Git/GH subprocess, repository, network or external ref is touched. Occupied regular/valid-symlink/dangling-symlink bytes and identity are preserved. Original-before cases reproduce effects-before-failure; corrected-after cases prevent them. Empty-path success and missing-config failure both retain terminal receipts.','helper_hashes':{n:hashlib.sha256(Path('/private/tmp/cmm-round103-'+n+'.py').read_bytes()).hexdigest() for n in ['push-pr','archive']}}
p=A/'receipt-guard-regression.json';assert not p.exists();p.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'cases':len(results),'receipt':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()},indent=2))
