#!/usr/bin/env python3
"""Read-only round96 five-workflow verification. Requires an actual postmerge handoff.

All Git/GitHub operations are reads. Only unique external JSON/Markdown receipts
are written; no workflow dispatch, retry, cancellation, or repository mutation.
"""
from pathlib import Path, PurePosixPath
from datetime import datetime, timezone, timedelta
from concurrent.futures import ThreadPoolExecutor
import argparse
import hashlib
import json
import re
import subprocess
import uuid

REPO = 'CultureBotAI/CMMMech'
TMP = Path('/private/tmp')
PREFIX = 'cmm-round96'
ROLES = {
    'required_pr': ('validate-strict.yaml', 'validate-strict'),
    'merge_group': ('validate-strict.yaml', 'validate-strict'),
    'main_validation': ('validate-strict.yaml', 'validate-strict'),
    'main_integrity': ('verify-merge-integrity.yaml', 'merge-integrity'),
    'pages_deployment': ('pages.yaml', 'deploy'),
}


def now():
    return datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def need(condition, message):
    if not condition:
        raise ValueError(message)


def positive_int(value):
    return type(value) is int and value > 0


def sha40(value):
    return isinstance(value, str) and re.fullmatch(r'[0-9a-f]{40}', value) is not None


def dt(value):
    result = datetime.fromisoformat(value.replace('Z', '+00:00'))
    need(result.tzinfo is not None, 'Timestamp lacks timezone')
    return result


def path_list(values):
    need(isinstance(values, list) and values, 'Empty or invalid commit file list')
    for value in values:
        need(isinstance(value, str) and value and not value.startswith('/')
             and str(PurePosixPath(value)) == value and '..' not in PurePosixPath(value).parts
             and '\\' not in value and '\x00' not in value, 'Unsafe/noncanonical file path')
    need(len(set(values)) == len(values), 'Duplicate commit path')
    return values


def array_pages(pages, expected_count=None):
    need(isinstance(pages, list) and pages and all(isinstance(p, list) for p in pages),
         'Invalid paginated array')
    need(all(len(p) <= 100 for p in pages) and all(len(p) == 100 for p in pages[:-1]),
         'Truncated/oversized array page')
    need(len(pages) == 1 or len(pages[-1]) > 0, 'Unexpected trailing empty array page')
    values = [value for page in pages for value in page]
    if expected_count is not None:
        need(type(expected_count) is int and expected_count >= 0 and len(values) == expected_count,
             'Paginated array total mismatch')
    return values


def object_pages(pages, field):
    need(isinstance(pages, list) and pages and all(isinstance(p, dict) for p in pages),
         'Invalid paginated object: ' + field)
    total = pages[0].get('total_count')
    need(type(total) is int and total >= 0, 'Invalid total_count: ' + field)
    need(all(type(p.get('total_count')) is int and p['total_count'] == total
             and isinstance(p.get(field), list) for p in pages), 'Inconsistent page schema/count: ' + field)
    values = array_pages([p[field] for p in pages], total)
    ids = [v.get('id') for v in values if isinstance(v, dict)]
    need(len(ids) == len(values) and all(positive_int(x) for x in ids)
         and len(set(ids)) == len(ids), 'Missing/duplicate object IDs: ' + field)
    return values


def required_check_run(checks, head):
    matches = [c for c in checks if c.get('name') == 'validate-strict'
               and c.get('app', {}).get('id') == 15368 and c.get('head_sha') == head]
    need(len(matches) == 1, 'Missing/ambiguous exact-head Actions validate-strict check')
    check = matches[0]
    match = re.fullmatch(r'https://github\.com/' + re.escape(REPO)
                         + r'/actions/runs/([1-9][0-9]*)/job/([1-9][0-9]*)(?:\?[^#]*)?',
                         check.get('details_url', ''))
    need(match is not None, 'Required check has no exact repository Actions run/job URL')
    return check, int(match.group(1)), int(match.group(2))


def run_identity(run, run_id, head, event, branch, workflow):
    need(run.get('id') == run_id and positive_int(run.get('run_attempt'))
         and run.get('head_sha') == head and run.get('event') == event,
         'Run ID/attempt/head/event mismatch')
    need(branch is None or run.get('head_branch') == branch, 'Run branch mismatch')
    need(run.get('path') == '.github/workflows/' + workflow
         and run.get('repository', {}).get('full_name') == REPO, 'Run repository/workflow mismatch')


def jobs_for_attempt(pages, run, required_name):
    jobs = object_pages(pages, 'jobs')
    need(jobs or run.get('status') != 'completed', 'Completed run has no jobs')
    if jobs:
        need(any(j.get('name') == required_name for j in jobs), 'Expected job absent from selected attempt')
    for job in jobs:
        need(job.get('run_id') == run['id'] and job.get('head_sha') == run['head_sha'],
             'Job run/head mismatch')
        # The endpoint pins the attempt; some API representations omit this field.
        if 'run_attempt' in job:
            need(type(job['run_attempt']) is int and job['run_attempt'] == run['run_attempt'],
                 'Job attempt mismatch')
    return jobs


def api(arguments, cwd):
    command = ['gh', 'api', '--method', 'GET', *arguments]
    started = now()
    try:
        process = subprocess.run(command, cwd=cwd, capture_output=True, text=True, timeout=60)
        try:
            data = json.loads(process.stdout)
        except json.JSONDecodeError:
            data = None
        return dict(command=command, started_at=started, finished_at=now(),
                    exit_code=process.returncode, data=data, stderr=process.stderr)
    except subprocess.TimeoutExpired as exc:
        return dict(command=command, started_at=started, finished_at=now(),
                    exit_code=None, data=None, stderr='Read-only API timeout: ' + str(exc))


def arguments():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('head', 'tree', 'base', 'merge'):
        parser.add_argument('--' + name, required=True)
    parser.add_argument('--pr', type=int, required=True)
    parser.add_argument('--queue-receipt', type=Path, required=True)
    parser.add_argument('--peer-receipt', type=Path, required=True)
    parser.add_argument('--commit-receipt', type=Path, default=TMP / (PREFIX + '-commit-receipt.json'))
    parser.add_argument('--preflight-receipt', type=Path,
                        default=TMP / (PREFIX + '-preflight-committed-terminal.json'))
    parser.add_argument('--config', type=Path, default=TMP / (PREFIX + '-helper-config.json'))
    parser.add_argument('--review-body', type=Path, default=TMP / (PREFIX + '-hosted-review-comment.md'))
    parser.add_argument('--worktree', type=Path, default=TMP / 'CMMMech-expansion-round96-20261015')
    parser.add_argument('--issue-state', action='append', default=[], metavar='NUMBER=open|closed',
                        help='Explicit current issue scope; repeat for each issue, never inherited from another round.')
    return parser.parse_args()


def main():
    args = arguments()
    out = dict(started_at=now(), reviewer='codex /root',
               authorship='Root coordinated round96, authored bassanite (independently reviewed by the sulfate agent), and independently reviewed wood ash. This is operational hosted-run verification, not a new scientific review.',
               pr=args.pr, head=args.head, tree=args.tree, base=args.base, merge=args.merge,
               worktree=str(args.worktree), helper_sha256=digest(__file__), inputs={},
               responses={}, findings=[], pending=[], runs={}, selected_run_ids={},
               limitations=['Checks the current selected attempt and every job returned by its attempt-specific endpoint; does not claim historical failed attempts never occurred.',
                            'Does not replace fresh postmerge local checks, branch cleanup or original-main preservation verification.',
                            'Only the explicitly supplied issue states are checked. No discovery/exhaustion claim about all issues.',
                            'No workflow or Git/GitHub mutations are performed.'])

    def load(label, path, expected=None, as_json=True):
        need(path.is_file() and not path.is_symlink(), 'Missing/symlink input: ' + str(path))
        value = path.read_bytes()
        hash_value = hashlib.sha256(value).hexdigest()
        if expected is not None:
            need(hash_value == expected, 'Changed bound input: ' + label)
        out['inputs'][label] = dict(path=str(path), sha256=hash_value, bytes=len(value))
        return json.loads(value) if as_json else value.decode('utf-8')

    def batch(queries):
        with ThreadPoolExecutor(max_workers=5) as pool:
            values = list(pool.map(lambda value: api(value, args.worktree), queries.values()))
        for key, value in zip(queries, values):
            out['responses'][key] = value
        for key in queries:
            value = out['responses'][key]
            need(value['exit_code'] == 0 and value['data'] is not None,
                 'Read-only API failed: ' + key + ': ' + value['stderr'])

    def data(key):
        return out['responses'][key]['data']

    def completion(value, label):
        if value.get('status') != 'completed':
            out['pending'].append(label + ': ' + str(value.get('status')))
        else:
            need(value.get('conclusion') == 'success', 'Completed nonsuccess: ' + label)

    try:
        need(positive_int(args.pr) and all(sha40(getattr(args, name)) for name in ('head', 'tree', 'base', 'merge')),
             'Invalid actual PR or commit identities')
        issues = {}
        for item in args.issue_state:
            match = re.fullmatch(r'([1-9][0-9]*)=(open|closed)', item)
            need(match is not None and match.group(1) not in issues, 'Invalid/duplicate issue state argument')
            issues[match.group(1)] = match.group(2)
        out['expected_issue_states'] = issues
        commit = load('commit', args.commit_receipt)
        queue = load('queue', args.queue_receipt)
        config = load('config', args.config)
        peer = load('peer', args.peer_receipt)
        pre = load('preflight', args.preflight_receipt, queue['preflight_sha256'])
        review_body = load('posted_review_body', args.review_body, queue['review_body_sha256'], False)
        load('preflight_log', Path(pre['log']), pre['log_sha256'], False)
        need([commit[k] for k in ('head', 'tree', 'base')] == [args.head, args.tree, args.base], 'Commit receipt identity')
        need(commit.get('clean') is True and commit['branch'] == config['branch']
             and config['base'] == args.base and Path(commit['worktree']).resolve() == args.worktree.resolve(),
             'Commit/config/worktree mismatch')
        paths = path_list(commit['files'])
        need(peer.get('passed') is True and peer.get('pr') == args.pr
             and [peer.get(k) for k in ('head', 'tree', 'base')] == [args.head, args.tree, args.base],
             'Hosted operational peer receipt mismatch')
        need(type(queue.get('exit_code')) is int and queue['exit_code'] == 0
             and queue['topic'] == commit and queue['pr']['number'] == args.pr,
             'Queue receipt identity/result')
        queued_pr = queue['pr']
        need(queued_pr['state'] == 'OPEN' and queued_pr['isDraft'] is False
             and [queued_pr[k] for k in ('headRefOid', 'baseRefOid', 'headRefName', 'baseRefName')]
             == [args.head, args.base, commit['branch'], 'main']
             and queued_pr['title'] == config['title'] and queue['live_main'] == args.base,
             'Queued PR/config/live base mismatch')
        need(set(path_list(queue['files'])) == set(paths), 'Queue file set mismatch')
        need(Path(queue['preflight_receipt']).resolve() == args.preflight_receipt.resolve()
             and queue['preflight_log_sha256'] == pre['log_sha256'], 'Queue/preflight binding mismatch')
        need(type(pre.get('exit_code')) is int and pre['exit_code'] == 0 and pre['mode'] == 'preflight'
             and [pre[k] for k in ('topic_head', 'expected_tree', 'trusted_base')]
             == [args.head, args.tree, args.base] and pre['counts'] == config['counts'], 'Preflight identity/counts/result')
        commands = pre['commands']
        need(commands and all(type(c.get('exit_code')) is int and c['exit_code'] in c['allowed_exit_codes']
                              for c in commands), 'Preflight command failure')
        for command in (['uv', 'run', '--locked', 'cmmmech', 'validate', '--require-records'],
                        ['uv', 'run', '--locked', 'cmmmech', 'validate-history', '--base', args.base],
                        ['just', 'review-check', '--base', args.base, '--require-reviews']):
            need(any(c['command'] == command and c['exit_code'] == 0 for c in commands), 'Required preflight command absent')
        reviews = queue['hosted_review_ids']
        need(isinstance(reviews, list) and reviews and all(positive_int(x) for x in reviews)
             and len(set(reviews)) == len(reviews), 'Invalid queued review IDs')
        batch({'pr': [f'repos/{REPO}/pulls/{args.pr}'],
               'merge': [f'repos/{REPO}/git/commits/{args.merge}'],
               'files': [f'repos/{REPO}/pulls/{args.pr}/files?per_page=100', '--paginate', '--slurp'],
               'runs': [f'repos/{REPO}/actions/runs?head_sha={args.merge}&per_page=100', '--paginate', '--slurp'],
               'checks': [f'repos/{REPO}/commits/{args.head}/check-runs?filter=latest&per_page=100', '--paginate', '--slurp'],
               **{f'review_{rid}': [f'repos/{REPO}/pulls/{args.pr}/reviews/{rid}'] for rid in reviews},
               **{f'issue_{number}': [f'repos/{REPO}/issues/{number}'] for number in issues}})
        pr = data('pr')
        need(pr['number'] == args.pr and pr['merged'] is True and pr['state'] == 'closed'
             and pr['merge_commit_sha'] == args.merge and pr['draft'] is False, 'Actual PR merge mismatch')
        need(pr['head']['sha'] == args.head and pr['head']['ref'] == commit['branch']
             and pr['base']['sha'] == args.base and pr['base']['ref'] == 'main'
             and pr['base']['repo']['full_name'] == REPO and pr['head']['repo']['full_name'] == REPO,
             'Actual PR head/base/repository mismatch')
        need(pr['title'] == queued_pr['title'] and pr['body'] == queued_pr['body'], 'Actual PR title/body mismatch')
        merge = data('merge')
        need(merge['sha'] == args.merge and merge['tree']['sha'] == args.tree
             and [p['sha'] for p in merge['parents']] == [args.base], 'Actual merge tree/sole parent mismatch')
        files = array_pages(data('files'), pr['changed_files'])
        hosted_paths = path_list([f['filename'] for f in files])
        need(set(hosted_paths) == set(paths) and len(hosted_paths) == len(paths), 'Incomplete or unexpected hosted file set')
        for item in files:
            need(item['status'] in ('added', 'modified'), 'Unexpected file status: ' + item['filename'])
            blob = subprocess.check_output(['git', '-C', str(args.worktree), 'rev-parse', args.tree + ':' + item['filename']],
                                           text=True, timeout=30).strip()
            need(sha40(blob) and item['sha'] == blob, 'Hosted file blob mismatch: ' + item['filename'])
        out['verified_hosted_files'] = [dict(path=f['filename'], blob_sha=f['sha']) for f in files]
        out['file_page_lengths'] = [len(page) for page in data('files')]
        for rid in reviews:
            review = data(f'review_{rid}')
            need(review['id'] == rid and review['commit_id'] == args.head and review['state'] == 'COMMENTED'
                 and review['body'].strip() == review_body.strip(), 'Posted operational comment differs')
        for number, state in issues.items():
            issue = data('issue_' + number)
            need(issue['number'] == int(number) and issue['state'] == state and 'pull_request' not in issue,
                 'Issue identity/state mismatch: ' + number)
        out['issue_states'] = issues
        check, pr_run_id, pr_job_id = required_check_run(object_pages(data('checks'), 'check_runs'), args.head)
        completion(check, 'required PR check')
        runs = object_pages(data('runs'), 'workflow_runs')
        need(all(r['head_sha'] == args.merge for r in runs), 'Run discovery escaped exact merge SHA')
        queue_start = dt(queue['live_main_observed_at']) - timedelta(minutes=2)
        merged_at = dt(pr['merged_at'])
        need(dt(queue['recorded_at']) <= merged_at + timedelta(minutes=2), 'Queue receipt postdates merge interval')
        selections = {'required_pr': (pr_run_id, args.head, 'pull_request', commit['branch'])}
        groups = [r for r in runs if r['event'] == 'merge_group'
                  and r['path'] == '.github/workflows/validate-strict.yaml'
                  and r['head_branch'].startswith('gh-readonly-queue/main/')
                  and queue_start <= dt(r['created_at']) <= merged_at]
        need(len(groups) <= 1, 'Ambiguous exact-merge queue validation runs')
        if groups:
            selections['merge_group'] = (groups[0]['id'], args.merge, 'merge_group', groups[0]['head_branch'])
        else:
            out['pending'].append('Missing exact-merge queue validation run')
        for role in ('main_validation', 'main_integrity', 'pages_deployment'):
            workflow, _ = ROLES[role]
            matches = [r for r in runs if r['path'] == '.github/workflows/' + workflow
                       and r['event'] == 'push' and r['head_branch'] == 'main']
            need(len(matches) <= 1, 'Ambiguous exact-merge push run: ' + role)
            if not matches:
                out['pending'].append('Missing exact-merge push run: ' + role)
            else:
                need(dt(matches[0]['created_at']) >= merged_at - timedelta(minutes=2), 'Push run predates merge: ' + role)
                selections[role] = (matches[0]['id'], args.merge, 'push', 'main')
        batch({role + '_actual': [f'repos/{REPO}/actions/runs/{spec[0]}'] for role, spec in selections.items()})
        queries = {}
        for role, (run_id, head, event, branch) in selections.items():
            run = data(role + '_actual')
            workflow, _ = ROLES[role]
            run_identity(run, run_id, head, event, branch, workflow)
            queries[role + '_jobs'] = [f'repos/{REPO}/actions/runs/{run_id}/attempts/{run["run_attempt"]}/jobs?per_page=100', '--paginate', '--slurp']
            queries['workflow_' + workflow] = [f'repos/{REPO}/actions/workflows/{workflow}']
        batch(queries)
        for role, (run_id, head, event, branch) in selections.items():
            run = data(role + '_actual')
            workflow, job_name = ROLES[role]
            definition = data('workflow_' + workflow)
            need(definition['path'] == run['path'] and definition['id'] == run['workflow_id']
                 and definition['state'] == 'active', 'Workflow API identity mismatch: ' + role)
            jobs = jobs_for_attempt(data(role + '_jobs'), run, job_name)
            if role == 'required_pr':
                need(any(j['id'] == pr_job_id and j['name'] == job_name for j in jobs),
                     'Required check does not point to selected PR attempt job')
            for job in jobs:
                completion(job, role + ' job ' + job['name'])
            completion(run, role + ' run')
            out['selected_run_ids'][role] = run_id
            out['runs'][role] = dict(id=run_id, url=run['html_url'], head_sha=head, event=event,
                                    path=run['path'], head_branch=branch, status=run['status'], conclusion=run['conclusion'],
                                    run_attempt=run['run_attempt'], workflow_id=run['workflow_id'],
                                    job_page_lengths=[len(p['jobs']) for p in data(role + '_jobs')],
                                    jobs=[{k: j.get(k) for k in ('id', 'run_id', 'head_sha', 'run_attempt', 'name', 'status', 'conclusion', 'html_url')}
                                          for j in jobs])
        need(len(set(out['selected_run_ids'].values())) == len(selections), 'Repeated workflow run across roles')
        batch({'closing_pr': [f'repos/{REPO}/pulls/{args.pr}'],
               'closing_main': [f'repos/{REPO}/git/ref/heads/main'],
               **{role + '_closing': [f'repos/{REPO}/actions/runs/{spec[0]}'] for role, spec in selections.items()}})
        closing_pr = data('closing_pr')
        need(closing_pr['merged'] is True and closing_pr['merge_commit_sha'] == args.merge
             and closing_pr['head']['sha'] == args.head and closing_pr['base']['sha'] == args.base
             and closing_pr['title'] == pr['title'] and closing_pr['body'] == pr['body']
             and data('closing_main')['object']['sha'] == args.merge, 'Closing PR/main identity changed')
        for role, (run_id, head, event, branch) in selections.items():
            initial, closing = data(role + '_actual'), data(role + '_closing')
            run_identity(closing, run_id, head, event, branch, ROLES[role][0])
            need(closing['run_attempt'] == initial['run_attempt'], 'Selected run attempt changed: ' + role)
            completion(closing, role + ' closing run')
        for label, entry in out['inputs'].items():
            need(digest(entry['path']) == entry['sha256'], 'Closing input hash changed: ' + label)
        need(digest(__file__) == out['helper_sha256'], 'Helper changed during execution')
        if not out['pending']:
            need(set(selections) == set(ROLES), 'Not all five exact workflow roles verified')
    except Exception as exc:
        out['findings'].append(type(exc).__name__ + ': ' + str(exc))
    out['pending'] = list(dict.fromkeys(out['pending']))
    out['passed'] = not out['findings'] and not out['pending']
    out['verdict'] = 'passed' if out['passed'] else ('failed' if out['findings'] else 'pending')
    out['all_five_hosted_runs_and_jobs_succeeded'] = out['passed']
    out['finished_at'] = now()
    stem = PREFIX + '-hosted-audit-' + datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '-' + uuid.uuid4().hex[:8]
    output = TMP / (stem + '.json')
    encoded = json.dumps(out, indent=2) + '\n'
    with output.open('x') as stream:
        stream.write(encoded)
    markdown = TMP / (stem + '.md')
    lines = [f'Round96 hosted workflow verification: {out["verdict"]}', '',
             f'PR #{args.pr}; head `{args.head}`; merge `{args.merge}`; tree `{args.tree}`.', '',
             out['authorship'], '', f'Observed {out["started_at"]} to {out["finished_at"]}.', '',
             '| Role | Run | Attempt | Result |', '| --- | --- | --- | --- |']
    for role, run in out['runs'].items():
        lines.append(f'| {role} | [{run["id"]}]({run["url"]}) | {run["run_attempt"]} | {run["status"]}/{run["conclusion"]} |')
    for heading, values in (('Pending observations', out['pending']), ('Verification failures', out['findings']),
                            ('Scope limits', out['limitations'])):
        if values:
            lines.extend(['', heading, ''] + ['- ' + value for value in values])
    lines.extend(['', f'Exact raw API responses and receipt hashes: `{output}`.'])
    with markdown.open('x') as stream:
        stream.write('\n'.join(lines) + '\n')
    final = TMP / (PREFIX + '-hosted-audit-final.json')
    alias = None
    if out['passed'] and not final.exists():
        try:
            with final.open('x') as stream:
                stream.write(encoded)
            alias = str(final)
        except FileExistsError:
            pass
    print(json.dumps(dict(receipt=str(output), sha256=digest(output), markdown=str(markdown),
                          markdown_sha256=digest(markdown), passed=out['passed'], verdict=out['verdict'],
                          pending=out['pending'], findings=out['findings'], selected_run_ids=out['selected_run_ids'],
                          final_alias_created=alias), indent=2))
    return 0 if out['passed'] else (1 if out['findings'] else 3)


if __name__ == '__main__':
    raise SystemExit(main())
