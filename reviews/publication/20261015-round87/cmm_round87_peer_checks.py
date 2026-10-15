"""Round87 publication evidence bindings; no independent re-curation of science."""
from pathlib import Path
import json,re,yaml
SLUGS={'alabandite','secondary-aluminium-dross','simonkolleite'}
AUTHORS={'alabandite':'codex /root/round68_iron_sulfides','secondary-aluminium-dross':'codex /root/round68_new_frontier','simonkolleite':'codex /root/round68_phosphates'}

def verify_native_lineage(w, selected, expected, need, sha):
    """Bind every current-cohort finding to explicitly selected final dispositions."""
    current={}; all_reviews={}; resolved=[]
    for name in expected:
        if name.startswith('reviews/structured/') and name.endswith('/review.yaml'):
            rv=yaml.safe_load((w/name).read_text())
            ids=rv.get('scope',{}).get('reviewed_target_ids',[])
            if any(t in {'cmmmech:'+s for s in SLUGS} for t in ids):
                need(len(ids)==1,'Current cohort review must have one canonical target')
                rid=rv['review_id'];need(rid not in current,'Duplicate native review ID')
                current[rid]=(name,rv);all_reviews[rid]=(name,rv)
    def prior(rid):
        if rid not in all_reviews:
            need(re.fullmatch(r'[A-Za-z0-9_.-]+',rid) is not None,'Unsafe prior review ID')
            name='reviews/structured/'+rid+'/review.yaml';p=w/name
            need(p.is_file() and not p.is_symlink(),'Prior native occurrence missing')
            rv=yaml.safe_load(p.read_text());need(rv['review_id']==rid,'Prior ID/path differs');all_reviews[rid]=(name,rv)
        return all_reviews[rid]
    def trace(rv,f,tid,stack):
        node=(rv['review_id'],f['finding_id']);need(node not in stack,'Cyclic occurrence lineage')
        reached={node}
        for ref in f.get('previous_occurrences',[]):
            need(ref['repository']=='CultureBotAI/CMMMech','Unexpected external occurrence requires explicit assessment')
            pn,pv=prior(ref['review_id']);need(pv['scope']['reviewed_target_ids']==[tid],'Prior target differs')
            matches=[x for x in pv['findings'] if x['finding_id']==ref['finding_id']]
            need(len(matches)==1 and matches[0]['issue_key']==f['issue_key'],'Prior finding identity/key differs')
            need(any(x['path']==pn and x['sha256']==sha(w/pn) for x in rv['source']['inputs']),'Successor does not bind exact prior native bytes')
            need((w/pn).with_suffix('.md').is_file(),'Prior Markdown counterpart missing')
            reached|=trace(pv,matches[0],tid,stack|{node})
        return reached
    for slug,(path,rv) in selected.items():
        tid='cmmmech:'+slug;need(rv['review_id'] in current,'Selected review not in committed current package')
        fs=rv['findings'];need(all(f['status'] in ('resolved','rejected') for f in fs),'Selected review has an unsupported or unresolved finding disposition')
        dispositions={}
        for f in fs:
            need(f['issue_key'] not in dispositions,'Duplicate selected stable issue key')
            dispositions[f['issue_key']]=(f,trace(rv,f,tid,set()))
        for rid,(name,pv) in current.items():
            if pv['scope']['reviewed_target_ids']!=[tid] or rid==rv['review_id']:continue
            for pf in pv['findings']:
                if pf['status'] not in ('open','deferred'):continue
                need(pf['issue_key'] in dispositions,'Earlier open finding omitted by selected final review')
                f,reached=dispositions[pf['issue_key']]
                need(f['status'] in ('resolved','rejected') and (rid,pf['finding_id']) in reached,'Exact earlier finding not explicitly resolved')
                resolved.append(dict(slug=slug,issue_key=pf['issue_key'],prior_review=rid,prior_finding=pf['finding_id'],prior_sha256=sha(w/name),final_review=rv['review_id'],final_finding=f['finding_id'],status=f['status'],external_issues=f.get('external_issues',[])))
    return resolved

def review_package(g,report,commit,cfg,expected,audit,a):
    need,sha,w,base=g['need'],g['sha'],g['WT'],g['BASE']
    report['checks_module']={'path':__file__,'sha256':sha(__file__)}
    need(set(cfg['slugs'])==SLUGS and len(cfg['slugs'])==3,'Current three-owner cohort differs')
    need(a.get('verdict') in ('pass','pass_with_limitations') and a.get('unresolved_corrective_findings')==0,'Publication audit unresolved')
    need(a.get('state')=='working_tree' and a.get('base')==base and a.get('branch')==g['BRANCH'],'Publication audit scope differs')
    need(audit==Path(cfg['publication_peer_review']) and audit.is_relative_to(w),'Publication audit path differs')
    need(a['counts']==cfg['counts'] and a['issues']==cfg['issues'],'Audit/config counts or issues differ')
    inputs=a['working_inputs'];names=[x['path'] for x in inputs]
    excluded={str(audit.relative_to(w)),str(audit.with_suffix('.md').relative_to(w))}
    need(len(names)==len(set(names)) and set(names)==set(expected)-excluded,'Final audit file set differs')
    for x in inputs:need(x['sha256']==expected[x['path']]['sha256']==sha(w/x['path']),'Final audit input changed: '+x['path'])
    mp=w/'research/ingests/round87-frontier-20261015.json';m=json.loads(mp.read_text())
    need(all(m[k]==cfg[k] for k in ('base','branch','worktree','counts','issues')) and m['state']=='working_tree','Manifest/config identity differs')
    rows=m['records'];need(len(rows)==3 and {r['slug'] for r in rows}==SLUGS,'Manifest selected owners differ')
    reviewed=[]; native_by_slug={}
    for row in rows:
        slug=row['slug'];p=w/row['path'];rec=yaml.safe_load(p.read_text());rp=w/row['review']['path'];rv=yaml.safe_load(rp.read_text());tid='cmmmech:'+slug
        need(rec['id']==row['id']==tid and row['path']=='data/records/'+slug+'.yaml' and sha(p)==row['sha256'],'Owner identity/hash differs')
        need(rv['review_id']==row['review']['review_id'] and sha(rp)==row['review']['sha256'],'Selected native review changed')
        need(rv['source']['git_revision']==base and rv['source']['state']=='working_tree' and rv['scope']['reviewed_target_ids']==[tid],'Native review base/state/scope differs')
        need(len(rv['targets'])==1 and rv['targets'][0]['target_id']==tid and rv['targets'][0]['path']==row['path'],'Native canonical target differs')
        need(rv['completion']=='completed' and rv['scientific_review'] is True and rv['verdict'] in ('pass','pass_with_limitations') and rv['reviewer']['independence']=='independent','Native scientific acceptance not complete/independent')
        need(rv['reviewer']['identity']!=AUTHORS[slug],'Owner author is accepting own science')
        for item in rv['source']['inputs']:need(sha(w/item['path'])==item['sha256'],'Native input changed: '+item['path'])
        need(any(i['path']==row['path'] and i['sha256']==row['sha256'] for i in rv['source']['inputs']),'Current owner is unbound')
        need(rec['history_refs']==row['history_refs'] and rec['history_refs'],'Canonical history manifest differs')
        for hp in rec['history_refs']:
            h=yaml.safe_load((w/hp).read_text());need(h['target']['path']==row['path'] and h['target']['slug']==slug,'History target differs')
            need(any(i['path']==hp and i['sha256']==sha(w/hp) for i in rv['source']['inputs']),'History not bound by scientific review')
        need(all(c['status']=='passed' for c in rv['checks'] if c.get('required')),'Required native check incomplete')
        native_by_slug[slug]=(rp,rv)
        reviewed.append({'slug':slug,'owner_sha256':sha(p),'review':str(rp.relative_to(w)),'review_sha256':sha(rp),'review_id':rv['review_id'],'reviewer':rv['reviewer'],'verdict':rv['verdict']})
    report['scientific_resolutions']=verify_native_lineage(w,native_by_slug,expected,need,sha)
    issues=[]
    need(set(cfg['issues'])=={'corrected_review_issues','open_source_issues','closed_source_issues'},'Unexpected issue role')
    issue_numbers=[n for ns in cfg['issues'].values() for n in ns]
    need(all(type(n) is int and n>0 for n in issue_numbers) and len(issue_numbers)==len(set(issue_numbers)),'Duplicate/invalid issue assignment')
    for resolution in report['scientific_resolutions']:
        for url in resolution['external_issues']:
            match=re.fullmatch(r'https://github.com/CultureBotAI/CMMMech/issues/(\d+)',url)
            if match:need(int(match.group(1)) in cfg['issues']['corrected_review_issues'],'Resolved native issue missing from current corrective ledger')
    for role,numbers in cfg['issues'].items():
        for n in numbers:
            x=g['api'](f'repos/{g["REPO"]}/issues/{n}');need(x['number']==n and not x.get('pull_request'),'Issue identity differs')
            expected_state='closed' if role=='closed_source_issues' else 'open'
            need(x['state']==expected_state,'Premerge issue state differs')
            if role=='open_source_issues':need(not re.search(r'(?i)(?:fixes|closes|resolves)\s+#'+str(n)+r'\b',g['body_for_review']),'PR incorrectly closes unresolved source issue')
            if role=='corrected_review_issues':need(re.search(r'(?i)(?:fixes|closes|resolves)\s+#'+str(n)+r'\b',g['body_for_review']),'PR omits intended corrective issue closure')
            issues.append({'number':n,'role':role,'state':x['state'],'url':x['html_url'],'title':x['title'],'body_sha256':g['sha_bytes']((x.get('body') or '').encode())})
    report['review_package']={'manifest':str(mp),'manifest_sha256':sha(mp),'final_audit_input_count':len(inputs),'native_reviews':reviewed,'live_issues':issues,'counts':cfg['counts'],'scope':'Operational record/history/review/config and committed evidence identity; scientific judgments remain those of separate native reviewers and final package auditor.'}

def review_inventory(g, report, number):
    need,get=g['need'],g['get'];repo=g['REPO'];raw={}
    for key,route in [('reviews',f'pulls/{number}/reviews'),('review_comments',f'pulls/{number}/comments'),('issue_comments',f'issues/{number}/comments')]:
        pages=json.loads(get(['gh','api',f'repos/{repo}/{route}?per_page=100','--paginate','--slurp']))
        need(isinstance(pages,list) and all(isinstance(p,list) for p in pages),'Conversation pagination shape differs')
        items=[x for p in pages for x in p];need(len({x['id'] for x in items})==len(items),'Duplicate conversation IDs')
        raw[key]=items
    owner,name=repo.split('/');cursor=None;threads=[];cursors=set()
    query='query($owner:String!,$name:String!,$number:Int!,$cursor:String){repository(owner:$owner,name:$name){pullRequest(number:$number){reviewThreads(first:100,after:$cursor){nodes{id isResolved isOutdated path line comments(first:100){nodes{id databaseId body url author{login} createdAt pullRequestReview{databaseId state commit{oid}}}pageInfo{hasNextPage endCursor}}}pageInfo{hasNextPage endCursor}}}}}'
    while True:
        args=['gh','api','graphql','-f','query='+query,'-f','owner='+owner,'-f','name='+name,'-F','number='+str(number)]
        if cursor:args+=['-f','cursor='+cursor]
        result=json.loads(get(args));need(not result.get('errors'),'GraphQL thread inventory errors')
        connection=result['data']['repository']['pullRequest']['reviewThreads'];threads.extend(connection['nodes']);page=connection['pageInfo']
        if not page['hasNextPage']:break
        cursor=page['endCursor'];need(cursor and cursor not in cursors,'Invalid repeated thread cursor');cursors.add(cursor)
    need(len({x['id'] for x in threads})==len(threads),'Duplicate review thread')
    # Every thread's comments are independently paginated; no first-100 truncation assumption.
    cq='query($id:ID!,$cursor:String){node(id:$id){... on PullRequestReviewThread{comments(first:100,after:$cursor){nodes{id databaseId body url author{login} createdAt pullRequestReview{databaseId state commit{oid}}}pageInfo{hasNextPage endCursor}}}}}'
    for t in threads:
        conn=t['comments'];comments=list(conn['nodes']);seen=set()
        while conn['pageInfo']['hasNextPage']:
            cursor=conn['pageInfo']['endCursor'];need(cursor and cursor not in seen,'Repeated thread-comment cursor');seen.add(cursor)
            result=json.loads(get(['gh','api','graphql','-f','query='+cq,'-f','id='+t['id'],'-f','cursor='+cursor]));need(not result.get('errors'),'GraphQL thread comment errors');conn=result['data']['node']['comments'];comments.extend(conn['nodes'])
        need(len({x['id'] for x in comments})==len(comments),'Duplicate thread comments');t['comments']=comments
    raw['review_threads']=threads
    report['hosted_conversation']=raw
    need(not [r for r in raw['reviews'] if r['state']=='CHANGES_REQUESTED'],'Existing non-dismissed change-request review requires assessment')
    need(not [t for t in threads if not t['isResolved']],'Unresolved hosted review thread requires assessment')
    # Do not silently classify free-text comments as non-actionable.
    digest=g['sha_bytes'](json.dumps(raw,sort_keys=True,separators=(',',':')).encode())
    if any(raw.values()):
        disposition=g['ROOT']/'cmm-round87-conversation-disposition.json'
        if not disposition.is_file():raise g['Pending']('Fetched conversation requires explicit reviewer disposition before acceptance')
        d=json.loads(disposition.read_text())
        need(d.get('pr')==number and d.get('head')==report['head'] and d.get('inventory_sha256')==digest and d.get('unresolved_actionable_findings')==0 and d.get('reviewer') and d.get('assessment'),'Conversation disposition absent, stale or incomplete')
        report['conversation_disposition']={'path':str(disposition),'sha256':g['sha'](disposition),'assessment':d['assessment']}
    report['hosted_conversation_inventory_sha256']=digest
    report['hosted_conversation_counts']={k:len(v) for k,v in raw.items()}
    report['hosted_conversation_scope']='Complete paginated fetched reviews, review comments, issue comments and review threads. General comment text is retained for independent inspection; no inference of approval from silence.'

def verify_preflight(g,report,head,tree,cfg):
    need=g['need'];sha=g['sha'];p=g['ROOT']/'cmm-round87-preflight-committed-terminal.json'
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
    need(get(['git','-C',clone,'rev-list','--parents','-n','1','HEAD']).split()==[r['synthetic_commit'],g['BASE']] and get(['git','-C',clone,'rev-parse','HEAD^{tree}']).strip()==tree,'Synthetic sole parent/tree differ')
    need(not get(['git','-C',clone,'status','--porcelain=v1','--untracked-files=all']).strip(),'Isolated verification checkout changed')
    report['committed_preflight']={'path':str(p),'sha256':sha(p),'log_sha256':r['log_sha256'],'coverage_receipt':str(cov_path),'coverage_sha256':sha(cov_path),'counts':r['counts'],'synthetic_commit':r['synthetic_commit'],'expected_tree':tree,'topic_absence_checks':r['topic_object_checks'],'retained_tag':tag,'finished_at':r['finished_at']}
