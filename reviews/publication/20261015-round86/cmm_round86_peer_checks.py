"""Round86 publication evidence bindings; no independent re-curation of science."""
from pathlib import Path
import json,re,yaml
SLUGS={'churchite-y','hemimorphite','heterogenite','municipal-sewage-sludge','willemite'}
AUTHORS={'churchite-y':'codex /root','hemimorphite':'codex /root/round68_phosphates','heterogenite':'codex /root/round68_iron_sulfides','municipal-sewage-sludge':'codex /root/round68_new_frontier','willemite':'codex /root/round68_phosphates'}
def review_package(g,report,commit,cfg,expected,audit,a):
    need,sha,w,base=g['need'],g['sha'],g['WT'],g['BASE']
    report['checks_module']={'path':__file__,'sha256':sha(__file__)}
    need(set(cfg['slugs'])==SLUGS and len(cfg['slugs'])==5,'Current five-owner cohort differs')
    need(a.get('verdict') in ('pass','pass_with_limitations') and a.get('unresolved_corrective_findings')==0,'Publication audit unresolved')
    need(a.get('state')=='working_tree' and a.get('base')==base and a.get('branch')==g['BRANCH'],'Publication audit scope differs')
    need(audit==Path(cfg['publication_peer_review']) and audit.is_relative_to(w),'Publication audit path differs')
    need(a['counts']==cfg['counts'] and a['issues']==cfg['issues'],'Audit/config counts or issues differ')
    inputs=a['working_inputs'];names=[x['path'] for x in inputs]
    excluded={str(audit.relative_to(w)),str(audit.with_suffix('.md').relative_to(w))}
    need(len(names)==len(set(names)) and set(names)==set(expected)-excluded,'Final audit file set differs')
    for x in inputs:need(x['sha256']==expected[x['path']]['sha256']==sha(w/x['path']),'Final audit input changed: '+x['path'])
    mp=w/'research/ingests/round86-frontier-20261015.json';m=json.loads(mp.read_text())
    need(all(m[k]==cfg[k] for k in ('base','branch','worktree','counts','issues')) and m['state']=='working_tree','Manifest/config identity differs')
    rows=m['records'];need(len(rows)==5 and {r['slug'] for r in rows}==SLUGS,'Manifest selected owners differ')
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
    need(cfg['issues']['corrected_review_issues']==[293],'Expected current churchite correction issue293')
    corrective_issue=cfg['issues']['corrected_review_issues'][0]
    ip=w/'reviews/structured/20261015T023705Z-churchite-y-round86-table-locator-initial/review.yaml'
    initial=yaml.safe_load(ip.read_text());key='churchite-y-round86-irradiation-table-locator'
    need(initial['review_id']=='20261015T023705Z-churchite-y-round86-table-locator-initial' and initial['verdict']=='needs_curation','Initial churchite occurrence differs')
    need(len(initial['findings'])==1 and initial['findings'][0]['finding_id']=='F1' and initial['findings'][0]['issue_key']==key and initial['findings'][0]['status']=='open','Initial F1 differs')
    rp,successor=native_by_slug['churchite-y']
    fs=[f for f in successor['findings'] if f['issue_key']==key]
    need(len(fs)==1 and fs[0]['finding_id']=='F1' and fs[0]['status']=='resolved','Churchite F1 resolution missing')
    f=fs[0]
    need(f['previous_occurrences']==[{'repository':'CultureBotAI/CMMMech','review_id':initial['review_id'],'finding_id':'F1'}],'Exact initial F1 occurrence lineage differs')
    need('https://github.com/CultureBotAI/CMMMech/issues/'+str(corrective_issue) in f.get('external_issues',[]),'Churchite corrective issue binding differs')
    need(any(x['path']==str(ip.relative_to(w)) and x['sha256']==sha(ip) for x in successor['source']['inputs']),'Successor does not bind immutable initial review hash')
    need(any(c['status']=='passed' and c.get('command')=='uv run --locked cmmmech validate-history --base '+base for c in successor['checks']),'Churchite correction history gate missing')
    for slug,(path,rv) in native_by_slug.items():
        need(not [f for f in rv['findings'] if f['status'] in ('open','deferred')],'Final selected scientific review contains unresolved findings: '+slug)
        if slug!='churchite-y':need(rv['findings']==[],'Unexpected new finding requires explicit disposition: '+slug)
    for fp in [ip,ip.with_suffix('.md'),rp,rp.with_suffix('.md')]:need(str(fp.relative_to(w)) in expected,'Churchite finding/resolution artifact omitted from package')
    report['scientific_resolution']={'issue':corrective_issue,'finding_id':'F1','issue_key':key,'initial':str(ip.relative_to(w)),'initial_sha256':sha(ip),'successor':str(rp.relative_to(w)),'successor_sha256':sha(rp),'scope':'Independent final scientific successor explicitly resolves two source-table locators; CREATE and EDIT retained. This operational audit does not replace the scientific assessment.'}
    issues=[]
    need(cfg['issues']['open_source_issues']==[294,295,296] and not cfg['issues']['closed_source_issues'],'Current source issue dispositions differ')
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
        disposition=g['ROOT']/'cmm-round86-conversation-disposition.json'
        if not disposition.is_file():raise g['Pending']('Fetched conversation requires explicit reviewer disposition before acceptance')
        d=json.loads(disposition.read_text())
        need(d.get('pr')==number and d.get('head')==report['head'] and d.get('inventory_sha256')==digest and d.get('unresolved_actionable_findings')==0 and d.get('reviewer') and d.get('assessment'),'Conversation disposition absent, stale or incomplete')
        report['conversation_disposition']={'path':str(disposition),'sha256':g['sha'](disposition),'assessment':d['assessment']}
    report['hosted_conversation_inventory_sha256']=digest
    report['hosted_conversation_counts']={k:len(v) for k,v in raw.items()}
    report['hosted_conversation_scope']='Complete paginated fetched reviews, review comments, issue comments and review threads. General comment text is retained for independent inspection; no inference of approval from silence.'

def verify_preflight(g,report,head,tree,cfg):
    need=g['need'];sha=g['sha'];p=g['ROOT']/'cmm-round86-preflight-committed-terminal.json'
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
