#!/usr/bin/env python3
"""Read-only round85 paginated hosted-run audit. Exit 0=passed, 3=pending, 1=failed.

Discovers exact runs from reviewed receipts and actual GitHub merge metadata.
It never dispatches, retries, cancels, merges, deletes, or changes Git state.
Every invocation writes a unique timestamped receipt; only complete success
also creates cmm-round85-hosted-audit-final.json (never overwrites it).
"""
from pathlib import Path
from datetime import datetime, timezone, timedelta
from concurrent.futures import ThreadPoolExecutor
import argparse, hashlib, json, re, subprocess, uuid

ROOT = Path('/private/tmp')
REPO = 'CultureBotAI/CMMMech'
PREFIX = 'cmm-round85-'
FIELDS = 'databaseId,workflowName,headSha,headBranch,event,status,conclusion,url,jobs,createdAt,updatedAt'
LIST_FIELDS = FIELDS.replace(',jobs', '')
FINAL = ROOT / (PREFIX + 'hosted-audit-final.json')

CONFIG = json.loads((ROOT / 'cmm-round85-helper-config.json').read_text())['publication']
EXPECTED_TITLE = CONFIG['title']
FIXED_RECEIPT_HASHES = CONFIG['receipt_hashes']
FIXED_PR_BODY_HASH = CONFIG['pr_body_sha256']
FIXED_REVIEW_BODY_HASH = CONFIG['review_body_sha256']

class Pending(Exception):
    pass
class Failure(Exception):
    pass

def require(condition, message):
    if not condition:
        raise Failure(message)
def now():
    return datetime.now(timezone.utc).isoformat()
def dt(value):
    return datetime.fromisoformat(value.replace('Z', '+00:00'))
def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def valid_sha(value):
    return isinstance(value, str) and re.fullmatch(r'[0-9a-f]{40}', value) is not None

def execute(cmd):
    began = now()
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=55)
        try:
            data = json.loads(result.stdout)
        except json.JSONDecodeError:
            data = None
        return dict(command=cmd, started_at=began, finished_at=now(), exit_code=result.returncode,
                    stdout=result.stdout, stderr=result.stderr, data=data)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return dict(command=cmd, started_at=began, finished_at=now(), exit_code=-1,
                    stdout='', stderr=repr(exc), data=None)

def validate_paginated_files(pages, expected_files, blob_lookup):
    """Bind every paginated PR file to the exact reviewed path and Git blob."""
    require(isinstance(pages, list) and pages, 'Missing paginated file pages')
    require(all(isinstance(page, list) and 0 < len(page) <= 100 for page in pages), 'Invalid paginated file page shape')
    require(all(len(page) == 100 for page in pages[:-1]), 'Incomplete intermediate file page')
    require(isinstance(expected_files, list) and expected_files, 'Missing expected file list')
    expected_paths = [item.get('path') for item in expected_files]
    require(all(isinstance(path, str) and path for path in expected_paths) and len(set(expected_paths)) == len(expected_paths), 'Duplicate or invalid expected file path')
    files = [item for page in pages for item in page]
    require(all(isinstance(item, dict) for item in files), 'Invalid paginated file entry')
    paths = [item.get('filename') for item in files]
    require(all(isinstance(path, str) and path for path in paths) and len(set(paths)) == len(paths), 'Duplicate or invalid hosted file path')
    require(len(files) == len(expected_files) and set(paths) == set(expected_paths), 'Paginated live PR file set differs from exact reviewed files')
    verified = []
    for item in files:
        path = item['filename']
        require(item.get('status') in ('added', 'modified'), 'Unexpected hosted file status: ' + path)
        require(valid_sha(item.get('sha')), 'Invalid hosted blob SHA: ' + path)
        expected_blob = blob_lookup(path)
        require(valid_sha(expected_blob) and item['sha'] == expected_blob, 'Hosted file blob differs from reviewed commit: ' + path)
        verified.append(dict(path=path, blob_sha=item['sha'], status=item['status']))
    return verified

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--reviewer', required=True)
    parser.add_argument('--authorship', required=True)
    args = parser.parse_args()
    started = now()
    report = dict(reviewer=args.reviewer, authorship=args.authorship, started_at=started, repository=REPO,
                  helper_sha256=sha(__file__), receipts={}, responses={}, findings=[],
                  scope='Read-only exact reviewed PR/head/tree, current required PR check, actual squash merge-group validation and main push validation/integrity/Pages deployment runs with all jobs. Cleanup receipts are crosschecked when present; cleanup is not performed.',
                  limitations=['Discovery bounded to 100 runs per exact commit/event. No unrelated latest repository run is accepted.',
                               'Assumes verified native SQUASH queue tests the actual eventual merge commit; a different commit is not substituted.',
                               'Hosted success is distinct from scientific review, fresh local postmerge gates and whole-fleet status.',
                               'Missing receipts/runs or unfinished runs return pending; completed non-success required runs/jobs return failed. API/access errors fail rather than being treated as absence.'])
    def receipt(name, required=True):
        path = ROOT / (PREFIX + name + '.json')
        if not path.exists():
            if required:
                raise Pending('Required local receipt not yet present: ' + str(path))
            return None
        require(path.is_file() and not path.is_symlink(), 'Unsafe receipt path: ' + str(path))
        value = json.loads(path.read_text())
        report['receipts'][name] = dict(path=str(path), sha256=sha(path))
        return value
    def batch(queries):
        with ThreadPoolExecutor(max_workers=4) as executor:
            for key, response in zip(queries, executor.map(execute, queries.values())):
                report['responses'][key] = response
        for key in queries:
            response = report['responses'][key]
            if key == 'required_pr_checks':
                if response['exit_code'] == 8 and isinstance(response['data'], list):
                    continue
                if response['exit_code'] == 1 and response['data'] is None and re.fullmatch(r'no checks reported on the .+ branch', (response['stdout'] + response['stderr']).strip(), re.IGNORECASE):
                    raise Pending('Required PR checks have not appeared yet')
            require(response['exit_code'] == 0 and response['data'] is not None,
                    'Read API failed for ' + key + ': ' + response['stderr'])
    def data(key):
        return report['responses'][key]['data']
    status = 'failed'
    try:
        commit = receipt('commit-receipt')
        opened = receipt('pr-open')
        posted = receipt('pr-review-posted')
        topic, tree, base, branch = (commit[k] for k in ('head', 'tree', 'base', 'branch'))
        number = opened['number']
        require(all(valid_sha(x) for x in (topic, tree, base)), 'Invalid commit/tree receipt values')
        require(isinstance(number, int) and number > 0, 'Invalid PR number')
        require(branch == 'curate/cmm-expansion-round85-20261015', 'Wrong owned branch')
        require(base == '51adf4be6c544642f6bf54a4e7f514adb84aa34e', 'Wrong reviewed base')
        require(opened['headRefOid'] == topic and opened['headRefName'] == branch and opened['baseRefName'] == 'main', 'PR-open receipt mismatch')
        require(topic == CONFIG['head'] and tree == CONFIG['tree'] and number == CONFIG['pr'], 'Wrong reviewed topic/tree/PR')
        for name, digest in FIXED_RECEIPT_HASHES.items():
            require(sha(ROOT / (PREFIX + name + '.json')) == digest, 'Initial receipt changed: ' + name)
        body_file = ROOT / (PREFIX + 'pr-body.md')
        review_file = ROOT / (PREFIX + 'hosted-review.md')
        require(sha(body_file) == FIXED_PR_BODY_HASH and sha(review_file) == FIXED_REVIEW_BODY_HASH, 'Reviewed publication text changed')
        require(opened['body'].rstrip() == body_file.read_text().rstrip(), 'Open receipt differs from prepared PR body')
        require(len(commit['files']) == CONFIG['file_count'], 'Unexpected reviewed file count')
        for item in commit['files']:
            path = Path(commit['worktree']) / item['path']
            require(path.is_file() and not path.is_symlink() and sha(path) == item['sha256'], 'Reviewed committed content changed: ' + str(path))
        audit = Path(commit['worktree']) / commit['publication_audit']
        require(sha(audit) == commit['publication_audit_sha256'] and json.loads(audit.read_text())['passed'], 'Final independent publication audit changed or failed')
        report['publication_text'] = dict(pr_title=EXPECTED_TITLE, body_file=str(body_file), body_sha256=sha(body_file), review_file=str(review_file), review_sha256=sha(review_file), reviewed_files=CONFIG['file_count'])
        require(posted['commit_id'] == topic and posted['state'] == 'COMMENTED', 'Review receipt not bound to exact head')
        report.update(pr=number, topic=topic, tree=tree, base=base, branch=branch)
        batch({
            'pr': ['gh', 'pr', 'view', str(number), '--repo', REPO, '--json', 'number,state,mergedAt,mergeCommit,headRefOid,headRefName,baseRefName,url,title,body'],
            'review': ['gh', 'api', f'repos/{REPO}/pulls/{number}/reviews/{posted["id"]}'],
            'pr_files': ['gh', 'api', f'repos/{REPO}/pulls/{number}/files?per_page=100', '--paginate', '--slurp'],
            'required_pr_checks': ['gh', 'pr', 'checks', str(number), '--repo', REPO, '--required', '--json', 'name,state,bucket,link'],
            'pr_runs': ['gh', 'run', 'list', '--repo', REPO, '--commit', topic, '--event', 'pull_request', '--limit', '100', '--json', LIST_FIELDS]
        })
        pr, review, checks = data('pr'), data('review'), data('required_pr_checks')
        require(pr['number'] == number and pr['headRefOid'] == topic and pr['headRefName'] == branch and pr['baseRefName'] == 'main' and pr['url'] == opened['url'], 'Live PR differs from reviewed head/identity')
        require(pr['title'] == EXPECTED_TITLE and pr['body'].rstrip() == body_file.read_text().rstrip(), 'Live PR title/body differs from exact reviewed publication text')
        def reviewed_blob(path):
            return subprocess.check_output(['git', '-C', commit['worktree'], 'rev-parse', tree + ':' + path], text=True, timeout=55).strip()
        report['verified_hosted_files'] = validate_paginated_files(data('pr_files'), commit['files'], reviewed_blob)
        report['file_page_lengths'] = [len(page) for page in data('pr_files')]
        report['pagination_correction'] = 'Round85 reuses the round70 pagination correction documented in issue224. Exact complete path set and every hosted blob are bound to the exact reviewed tree, independent of branch retention; no round85 first100-file failure is asserted.'
        require(review['id'] == posted['id'] and review['commit_id'] == topic and review['state'] == 'COMMENTED' and review['body'] == posted['body'] and review['body'].rstrip() == review_file.read_text().rstrip(), 'Live comment review differs from exact reviewed text/head')
        require(isinstance(checks, list), 'Unexpected required-check response shape')
        if not checks:
            raise Pending('Required PR checks have not appeared yet')
        if any(c['bucket'] == 'fail' for c in checks):
            raise Failure('A required PR check has failed')
        if any(c['bucket'] not in ('pass', 'pending') for c in checks):
            raise Failure('Required PR check is skipped, cancelled, or otherwise not passing')
        if any(c['bucket'] == 'pending' for c in checks):
            raise Pending('Required PR checks are still pending')
        require(any(c['name'] == 'validate-strict' for c in checks), 'Expected required validate-strict context missing')
        ids = {int(m.group(1)) for c in checks if c['name'] == 'validate-strict' for m in [re.search(r'/actions/runs/(\d+)(?:/|$)', c['link'])] if m}
        prs = [r for r in data('pr_runs') if r['databaseId'] in ids and r['workflowName'] == 'Validate strictly' and r['headSha'] == topic and r['event'] == 'pull_request' and r['headBranch'] == branch]
        require(len(prs) == 1, 'Cannot uniquely bind required PR check link to expected head/workflow/event')
        if pr['state'] != 'MERGED':
            require(pr['state'] == 'OPEN', 'PR was closed without merge')
            raise Pending('Reviewed PR is open; awaiting native queue merge')
        require(pr['mergedAt'] and pr.get('mergeCommit') and valid_sha(pr['mergeCommit']['oid']), 'Invalid actual merge metadata')
        merge = pr['mergeCommit']['oid']; report['merge'] = merge
        queue = receipt('queue-request')
        require(queue['exit_code'] == 0 and queue['head'] == topic and queue['pr'] == number, 'Queue receipt mismatch')
        merged_receipt = receipt('pr-merged', required=False)
        if merged_receipt:
            require(merged_receipt['number'] == number and merged_receipt['headRefOid'] == topic and merged_receipt['state'] == 'MERGED' and merged_receipt['mergeCommit']['oid'] == merge and merged_receipt['mergedAt'] == pr['mergedAt'], 'Saved merge receipt differs from live merge')
        cleanup = receipt('pr-cleanup', required=False)
        if cleanup:
            require(all(cleanup[k] == v for k, v in {'pr': number, 'merge': merge, 'head': topic, 'tree': tree, 'branch': branch}.items()), 'Cleanup receipt identity mismatch')
            require(cleanup['local_branch_absent'] and cleanup['remote_branch_absent'] and cleanup['clean_detached_worktree'], 'Cleanup receipt is not complete')
        report['cleanup_receipt_checked'] = cleanup is not None
        batch({
            'merge_object': ['gh', 'api', f'repos/{REPO}/git/commits/{merge}'],
            'merge_group_runs': ['gh', 'run', 'list', '--repo', REPO, '--commit', merge, '--event', 'merge_group', '--limit', '100', '--json', LIST_FIELDS],
            'main_runs': ['gh', 'run', 'list', '--repo', REPO, '--commit', merge, '--event', 'push', '--limit', '100', '--json', LIST_FIELDS]
        })
        obj = data('merge_object')
        require(obj['sha'] == merge and obj['tree']['sha'] == tree and [p['sha'] for p in obj['parents']] == [base], 'Actual squash commit differs from reviewed tree/base')
        groups = [r for r in data('merge_group_runs') if r['workflowName'] == 'Validate strictly' and r['headSha'] == merge and r['event'] == 'merge_group' and r['headBranch'].startswith('gh-readonly-queue/main/') and dt(queue['recorded_at']) - timedelta(minutes=2) <= dt(r['createdAt']) <= dt(pr['mergedAt'])]
        if not groups:
            raise Pending('No exact-merge validation run visible within native queue-to-merge interval')
        group = max(groups, key=lambda r: (r['createdAt'], r['databaseId']))
        selected = [('required_pr', prs[0]), ('merge_group', group)]
        for role, workflow in [('main_validation', 'Validate strictly'), ('main_integrity', 'Verify merge integrity'), ('pages_deployment', 'Deploy GitHub Pages')]:
            matches = [r for r in data('main_runs') if r['workflowName'] == workflow and r['headSha'] == merge and r['event'] == 'push' and r['headBranch'] == 'main' and dt(r['createdAt']) >= dt(pr['mergedAt']) - timedelta(minutes=2)]
            if not matches:
                raise Pending('No ' + workflow + ' push run visible for actual merge commit')
            selected.append((role, max(matches, key=lambda r: (r['createdAt'], r['databaseId']))))
        require(len({r['databaseId'] for _, r in selected}) == 5, 'Expected five distinct hosted runs')
        report['selected_run_ids'] = {role: r['databaseId'] for role, r in selected}
        batch({role: ['gh', 'run', 'view', str(run['databaseId']), '--repo', REPO, '--json', FIELDS] for role, run in selected})
        report['runs'] = {role: data(role) for role, _ in selected}
        pending = []
        for role, expected in selected:
            run = data(role)
            require(all(run[k] == expected[k] for k in ('databaseId', 'workflowName', 'headSha', 'headBranch', 'event')), 'Run identity changed for ' + role)
            if run['status'] != 'completed':
                pending.append(role + ' run ' + str(run['databaseId']) + ' is ' + run['status'])
                continue
            require(run['conclusion'] == 'success', role + ' completed without success')
            require(run['jobs'], role + ' has no jobs')
            for job in run['jobs']:
                if job['status'] != 'completed':
                    pending.append(role + ' job ' + job['name'] + ' is ' + job['status'])
                else:
                    require(job['conclusion'] == 'success', role + ' job ' + job['name'] + ' completed without success')
            if run['workflowName'] == 'Validate strictly':
                require(any(j['name'] == 'validate-strict' for j in run['jobs']), role + ' lacks validate-strict job')
            if role == 'main_integrity':
                require(any(j['name'] == 'merge-integrity' for j in run['jobs']), role + ' lacks merge-integrity job')
            if role == 'pages_deployment':
                require(any(j['name'] == 'deploy' for j in run['jobs']), role + ' lacks deploy job')
        # Bind actual workflow files and every paginated job, independently of gh run view limits.
        workflow_files={'required_pr':'validate-strict.yaml','merge_group':'validate-strict.yaml','main_validation':'validate-strict.yaml','main_integrity':'verify-merge-integrity.yaml','pages_deployment':'pages.yaml'}
        queries={}
        for role, expected in selected:
            rid=expected['databaseId']
            queries[role+'_api']=['gh','api',f'repos/{REPO}/actions/runs/{rid}']
            queries[role+'_jobs']=['gh','api',f'repos/{REPO}/actions/runs/{rid}/jobs?per_page=100','--paginate','--slurp']
        for file in set(workflow_files.values()):queries['workflow_'+file]=['gh','api',f'repos/{REPO}/actions/workflows/{file}']
        batch(queries)
        report['paginated_jobs']={}
        for role, expected in selected:
            run=data(role+'_api');wf=data('workflow_'+workflow_files[role]);pages=data(role+'_jobs')
            require(run['id']==expected['databaseId'] and run['head_sha']==expected['headSha'] and run['event']==expected['event'] and run['head_branch']==expected['headBranch'],'Exact run API identity differs: '+role)
            require(wf['path']=='.github/workflows/'+workflow_files[role] and wf['state']=='active' and run['workflow_id']==wf['id'] and run['path']==wf['path'] and run['repository']['full_name']==REPO,'Workflow identity differs: '+role)
            require(isinstance(pages,list) and pages and all(isinstance(x.get('jobs'),list) for x in pages),'Invalid jobs pages: '+role)
            jobs=[j for page in pages for j in page['jobs']]
            require(jobs and len({j['id'] for j in jobs})==len(jobs) and all(len(p['jobs'])==100 for p in pages[:-1]),'Incomplete/duplicate jobs pages: '+role)
            require(len(jobs)==pages[0]['total_count'],'Paginated jobs count differs: '+role)
            for job in jobs:
                require(job['run_id']==run['id'] and job['head_sha']==expected['headSha'],'Job identity differs: '+role)
                if job['status']!='completed':pending.append(role+' job '+job['name']+' pending')
                else:require(job['conclusion']=='success','Paginated job failed: '+role+' '+job['name'])
            report['paginated_jobs'][role]={'workflow_id':wf['id'],'workflow_path':wf['path'],'run_id':run['id'],'page_lengths':[len(x['jobs']) for x in pages],'jobs':[{k:j[k] for k in ('id','name','status','conclusion','html_url')} for j in jobs]}
        if pending:
            raise Pending('; '.join(pending))
        report['all_five_hosted_runs_and_jobs_succeeded'] = True
        report['package_and_review_match'] = True
        status = 'passed'
    except Pending as exc:
        status = 'pending'; report['pending_reason'] = str(exc)
    except (Failure, KeyError, ValueError, OSError, TypeError, subprocess.SubprocessError) as exc:
        status = 'failed'; report['findings'].append(str(exc))
    report.update(finished_at=now(), verdict=status, passed=status == 'passed')
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '-' + uuid.uuid4().hex[:6]
    path = ROOT / (PREFIX + 'hosted-audit-' + stamp + '.json')
    with path.open('x') as handle:
        handle.write(json.dumps(report, indent=2) + '\n')
    final_written = False
    if status == 'passed' and not FINAL.exists():
        with FINAL.open('x') as handle:
            handle.write(json.dumps(report, indent=2) + '\n')
        final_written = True
    print(json.dumps(dict(receipt=str(path), sha256=sha(path), verdict=status,
                         pending_reason=report.get('pending_reason'), findings=report['findings'],
                         final_receipt=str(FINAL) if final_written else None,
                         final_sha256=sha(FINAL) if final_written else None,
                         selected_run_ids=report.get('selected_run_ids')), indent=2))
    return {'passed': 0, 'pending': 3, 'failed': 1}[status]

if __name__ == '__main__':
    raise SystemExit(main())
