"""Read-only round77 package checks; caller supplies logging/API helpers."""
from pathlib import Path
import json,yaml

def review_package(g,report,commit,cfg,expected,audit,a):
    need=g['need'];sha=g['sha'];w=g['WT'];base=g['BASE'];api=g['api'];root=g['ROOT']
    report['checks_module']={'path':__file__,'sha256':sha(__file__)}
    need(a.get('verdict') in ('pass','pass_with_limitations') and type(a.get('unresolved_corrective_findings')) is int and a['unresolved_corrective_findings']==0,'Final audit is not a resolved positive verdict')
    need(a.get('state')=='working_tree' and a.get('base')==base and a.get('branch')==g['BRANCH'],'Final audit scope differs')
    need(audit==Path(cfg['publication_peer_review']) and audit.is_relative_to(w),'Final audit path/worktree binding differs')
    need('worktree' not in a or a['worktree']==str(w),'Explicit final audit worktree differs')
    need(a.get('counts')==cfg['counts'] and a.get('issues')==cfg['issues'],'Final audit counts/issues differ')
    inputs=a.get('working_inputs',[]);names=[x['path'] for x in inputs]
    excluded={str(audit.relative_to(w)),str(audit.with_suffix('.md').relative_to(w))}
    need(len(names)==len(set(names)) and set(names)==set(expected)-excluded,'Final audit does not cover exact committed input set excluding itself')
    for x in inputs:need(x['sha256']==expected[x['path']]['sha256']==sha(w/x['path']),'Final audit input changed: '+x['path'])
    mp=w/'research/ingests/round77-frontier-20261014.json';m=json.loads(mp.read_text())
    need(m['base']==base and m['branch']==g['BRANCH'] and m['counts']==cfg['counts'] and m['issues']==cfg['issues'],'Manifest scope/counts/issues differ')
    arts=m['pre_manifest_inputs'];an=[x['path'] for x in arts]
    need(len(an)==len(set(an)),'Manifest input paths duplicate')
    excluded_manifest=excluded|{str(mp.relative_to(w)),str(mp.with_suffix('.md').relative_to(w))}
    need(set(an)==set(expected)-excluded_manifest,'Manifest does not cover complete pre-manifest input set')
    for x in arts:need(x['path'] in expected and x['sha256']==expected[x['path']]['sha256'],'Manifest input missing or changed: '+x['path'])
    rows=m['records'];need(len(rows)==4 and {x['slug'] for x in rows}==set(cfg['slugs']),'Manifest cohort differs')
    reviewed=[]
    for row in rows:
        path=w/row['path'];rec=yaml.safe_load(path.read_text());rp=w/row['review']['path'];rv=yaml.safe_load(rp.read_text())
        need(sha(path)==row['sha256'] and rec['id']==row['id'] and sha(rp)==row['review']['review_sha256'],'Manifest owner/review bytes differ: '+row['slug'])
        need(rv['completion']=='completed' and rv['scientific_review'] is True and rv['verdict'] in ('pass','pass_with_limitations') and rv['reviewer']['independence']=='independent','Missing completed independent positive review: '+row['slug'])
        need(row['id'] in rv['scope']['reviewed_target_ids'] and any(x['path']==row['path'] and x['sha256']==row['sha256'] for x in rv['source']['inputs']),'Review does not bind final owner: '+row['slug'])
        need(rv['findings']==[],'Unexpected scientific finding; reassess disposition before accepting: '+row['slug'])
        need(rec['history_refs']==row['history_refs'] and bool(row['history_refs']),'Canonical histories differ from manifest')
        for hp in row['history_refs']:
            h=yaml.safe_load((w/hp).read_text());need(h['target']['path']==row['path'] and hp in expected,'History target/package membership differs')
        for x in rv['source']['inputs']:need(sha(w/x['path'])==x['sha256'],'Review input changed: '+x['path'])
        if row['slug'] in ('monetite','switzerite'):need(rv['reviewer']['identity']=='codex /root/round68_iron_sulfides','Authored phosphate record lacks independent iron-agent review')
        reviewed.append({'slug':row['slug'],'owner_sha256':row['sha256'],'review':row['review']['path'],'review_sha256':sha(rp),'reviewer':rv['reviewer']['identity'],'verdict':rv['verdict']})
    gates=[]
    for suffix in ('final-gates','review-check-final'):
        path=root/('cmm-round77-'+suffix+'.json');r=json.loads(path.read_text())
        need(r['exit_code']==0 and r['worktree']==str(w) and r['finished_at'],'Local terminal gate identity/outcome differs')
        if suffix=='final-gates':need(r['base']==base,'Final-gates trusted base differs')
        else:need(r['command']==['just','review-check','--base',base,'--require-reviews'],'Review gate trusted base/command differs')
        commands=r.get('commands',[{'command':r.get('command'),'exit_code':r['exit_code']}])
        need(all(x['exit_code']==0 for x in commands) and sha(r['log'])==r['log_sha256'],'Local terminal gate failed or log changed')
        retained=w/'research/ingests/round77-checks-20261014'/f'{suffix}.json'
        need(sha(retained)==sha(path),'Retained gate receipt differs from actual')
        if suffix=='final-gates':
            need([x['command'] for x in commands]==[['just','check'],['uv','run','--locked','cmmmech','validate','--require-records'],['uv','run','--locked','cmmmech','validate-history','--base',base],['uv','run','--locked','python','scripts/render_pages.py','--check']],'Four actual batch commands differ')
            need(all(r['record_inputs'].get(row['path'])==row['sha256'] for row in rows),'Batch gate does not bind final cohort owners')
            need(r['inputs_unchanged'] is True,'Gate input stability not verified')
        else:need(r['command']==['just','review-check','--base',base,'--require-reviews'],'Review gate command differs')
        gates.append({'path':str(path),'sha256':sha(path),'log_sha256':r['log_sha256'],'finished_at':r['finished_at']})
    issues=[]
    configured=cfg['issues'];need(set(configured)=={'corrected_review_issues','closed_source_issues','open_source_issues'},'Unexpected issue disposition categories')
    allnums=[n for ns in configured.values() for n in ns];need(len(allnums)==len(set(allnums)) and all(type(n) is int and n>0 for n in allnums),'Duplicate or invalid issue number')
    for role,numbers in configured.items():
        for n in numbers:
            x=api(f'repos/{g["REPO"]}/issues/{n}')
            # Corrective work closes through the reviewed PR; it must remain open premerge.
            expected_state='closed' if role=='closed_source_issues' else 'open'
            need(x['number']==n and x['state']==expected_state and 'pull_request' not in x,'Premerge issue disposition differs: '+str(n))
            if role=='corrected_review_issues':
                need(('Closes #'+str(n)) in g['body_for_review'] or ('Fixes #'+str(n)) in g['body_for_review'],'Corrected issue lacks explicit PR closing link: '+str(n))
            issues.append({'number':n,'state':x['state'],'url':x['html_url'],'title':x['title'],'role':role,'body_sha256':g['sha_bytes']((x.get('body') or '').encode())})
    # Expose retained static operational-review artifacts for independent inspection.
    # If this cohort has corrective issues, require initial/successor evidence below.
    operational=[]
    for name in expected:
        if name.startswith('reviews/publication/20261014-round77/') and name.endswith('.json') and 'helper-static' in name:
            z=json.loads((w/name).read_text());operational.append({'path':name,'sha256':sha(w/name),'content':z})
    if configured['corrected_review_issues']:
        need(len(operational)>=2,'Corrected operational issue lacks retained initial/successor audit artifacts')
    report['review_package']={'manifest':str(mp),'manifest_sha256':sha(mp),'manifest_input_count':len(arts),'final_audit_input_count':len(inputs),'native_reviews':reviewed,'operational_review_artifacts':operational,'local_terminal_gates':gates,'live_issues':issues,'counts':cfg['counts']}
def verify_preflight(g,report,head,tree,cfg):
    need=g['need'];sha=g['sha'];p=g['ROOT']/'cmm-round77-preflight-committed-terminal.json'
    if not p.is_file():raise g['Pending']('Actual committed synthetic-squash preflight is not terminal yet')
    r=json.loads(p.read_text())
    need(r['exit_code']==0 and r['mode']=='preflight' and r['trusted_base']==g['BASE'] and r['topic_head']==head and r['expected_tree']==tree,'Committed preflight identity/outcome differs')
    need(r['finished_at'] and sha(r['log'])==r['log_sha256'],'Preflight log incomplete or changed')
    need(all(c['exit_code'] in c['allowed_exit_codes'] for c in r['commands']),'Preflight command failed')
    commands=[c['command'] for c in r['commands'] if c['exit_code']==0]
    for cmd in [['uv','run','--locked','cmmmech','validate','--require-records'],['uv','run','--locked','cmmmech','validate-history','--base',g['BASE']],['just','review-check','--base',g['BASE'],'--require-reviews']]:
        need(cmd in commands,'Required actual preflight gate missing: '+str(cmd))
    need(r['counts']==cfg['counts'],'Preflight exact counts differ')
    need(len(r['topic_object_checks'])==3 and all(x['absent'] is True and x['exit_code']!=0 for x in r['topic_object_checks']),'Topic commit not demonstrated absent from squash clone at all three checks')
    tag=r['verified_retained_tag'];need(tag=={'ref':'refs/tags/review-base/cmm-source-survey-20261009','tag_object':'fc4040c3abcd28f0a9cc52467e308100144ad1fd','peeled_commit':'c0adc2c0763e1515ed07dc712b024974d98fb342','remote_verified':True},'Required preservation tag identity differs')
    cov_path=Path(r['coverage_receipt']);cov=json.loads(cov_path.read_text());need(cov['passed'] is True and {k:cov[k] for k in cfg['counts']}==cfg['counts'],'Isolated positive review coverage/counts differ')
    clone=r['clone'];get=g['get']
    need(get(['git','-C',clone,'rev-parse','HEAD']).strip()==r['synthetic_commit'] and r['synthetic_commit']!=head,'Preflight clone is not distinct synthetic commit')
    need(get(['git','-C',clone,'rev-parse','HEAD^']).strip()==g['BASE'] and get(['git','-C',clone,'rev-parse','HEAD^{tree}']).strip()==tree,'Synthetic parent/tree differ')
    need(not get(['git','-C',clone,'status','--porcelain=v1','--untracked-files=all']).strip(),'Isolated verification checkout changed')
    report['committed_preflight']={'path':str(p),'sha256':sha(p),'log_sha256':r['log_sha256'],'coverage_receipt':str(cov_path),'coverage_sha256':sha(cov_path),'counts':r['counts'],'synthetic_commit':r['synthetic_commit'],'expected_tree':tree,'topic_absence_checks':r['topic_object_checks'],'retained_tag':tag,'finished_at':r['finished_at']}
