from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, subprocess

T = Path('/private/tmp')
W = T / 'CMMMech-expansion-round103-20261015'
repo = 'CultureBotAI/CMMMech'
drafts = json.loads((T / 'cmm-round103-issue-drafts.json').read_text())
existing = json.loads((T / 'cmm-round103-issues-precreate.json').read_text())
# The one-time inventory covers all 270 title/body rows, not comments.
assert len(existing) == 270
assert len(drafts) == 6 and len({item['title'] for item in drafts}) == 6
for item in drafts:
    assert item['title'] not in [row['title'] for row in existing]
    assert Path(item['body_file']).is_file()
aggregate = T / 'cmm-round103-source-issues.json'
if aggregate.exists() or aggregate.is_symlink():
    raise FileExistsError('Refusing occupied issue receipt: ' + str(aggregate))
now = lambda: datetime.now(timezone.utc).isoformat()
receipt = []
progress = {'status': 'in_progress', 'started_at': now(), 'created_issues': receipt, 'active': None}
# Reserve before any external mutation. open('x') also rejects a racing creator.
with aggregate.open('x') as reserved:
    def persist(value):
        serialized = json.dumps(value, indent=2) + '\n'
        reserved.seek(0)
        reserved.write(serialized)
        reserved.truncate()
        reserved.flush()

    persist(progress)
    try:
        for item in drafts:
            p = Path(item['body_file'])
            body = p.read_text()
            progress['active'] = {'title': item['title'], 'body_file': str(p),
                                  'body_sha256': hashlib.sha256(p.read_bytes()).hexdigest(),
                                  'stage': 'create_pending'}
            persist(progress)
            command = ['gh', 'issue', 'create', '--repo', repo, '--title', item['title'], '--body-file', str(p)]
            r = subprocess.run(command, cwd=W, capture_output=True, text=True)
            progress['active']['create_response'] = {'exit_code': r.returncode, 'stdout': r.stdout, 'stderr': r.stderr}
            persist(progress)
            assert r.returncode == 0, r.stderr
            url = r.stdout.strip()
            number = int(url.rsplit('/', 1)[1])
            progress['active'].update(stage='created_unverified', url=url, number=number)
            persist(progress)
            q = subprocess.run(['gh', 'issue', 'view', str(number), '--repo', repo, '--json', 'number,title,body,state,url'], cwd=W, capture_output=True, text=True)
            progress['active']['verification_response'] = {'exit_code': q.returncode, 'stdout': q.stdout, 'stderr': q.stderr}
            persist(progress)
            assert q.returncode == 0, q.stderr
            data = json.loads(q.stdout)
            assert data['body'] == body and data['title'] == item['title'] and data['state'] == 'OPEN'
            data.update(created_at_observed=now(), body_file=str(p), body_sha256=hashlib.sha256(p.read_bytes()).hexdigest(), dedup_scope='270 all-state title/body rows; comments not searched. Related hidden/ignored local/source searches are retained in the paired source dossiers.')
            receipt.append(data)
            persist(progress)
            with (T / f'cmm-round103-created-issue-{number}.json').open('x') as f:
                json.dump(data, f, indent=2)
                f.write('\n')
            progress['active'] = None
            persist(progress)
            print(f'Created #{number}: {data["title"]}', flush=True)
        # Preserve the established successful receipt shape for consumers.
        persist(receipt)
    except BaseException as error:
        progress.update(status='failed', finished_at=now(), error_type=type(error).__name__, error=str(error))
        persist(progress)
        raise
