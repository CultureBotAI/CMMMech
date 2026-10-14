"""Guarded recovered-access synchronization. Coordinator must review before execution.

Snapshots begin now; they make no claim about the earlier inaccessible period.
Only the original main is fast-forwarded. The unrelated worktree is read only.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import os
import stat
import subprocess

TMP = Path('/private/tmp')
MAIN = Path('/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CMMMech')
SKILL = TMP / 'CMMMech-add-record-skill-20261010'
BASE = '76509ff65c70edb5f212b6b4217febe5493bb0f3'
MERGE = 'b6014c43b8174904e80f71df22be2251a802b418'
TREE = 'd56d644c67b9a480c9b6d0b7be883b33c7398a99'
TOPIC = '92978c8bb4ca2f1bec2e9f02e083f7f5de328a87'
SKILL_HEAD = '6a974c54d2c6e834d3514a9ada6272edc6a2aa74'
SKILL_BRANCH = 'feat/cmmmech-add-record-skill'
REMOTE = 'https://github.com/CultureBotAI/CMMMech.git'
TAG = 'refs/tags/review-base/cmm-source-survey-20261009'
TAG_OBJECT = 'fc4040c3abcd28f0a9cc52467e308100144ad1fd'
TAG_COMMIT = 'c0adc2c0763e1515ed07dc712b024974d98fb342'
BEFORE = TMP / 'cmm-round57-original-recovery-before.json'
AFTER = TMP / 'cmm-round57-original-recovery-after.json'
ENV = dict(os.environ, GIT_OPTIONAL_LOCKS='0', PYTHONDONTWRITEBYTECODE='1')


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b''):
            digest.update(block)
    return digest.hexdigest()


def git(root, *args):
    return subprocess.check_output(
        ['git', '-c', 'core.fsmonitor=false', '-c', 'gc.auto=0',
         '-c', 'maintenance.auto=false', '-c', 'core.hooksPath=/dev/null',
         '-C', str(root), *args], env=ENV)


def textgit(root, *args):
    return git(root, *args).decode().strip()


def state(root):
    return {'head': textgit(root, 'rev-parse', 'HEAD'),
            'tree': textgit(root, 'rev-parse', 'HEAD^{tree}'),
            'branch': textgit(root, 'branch', '--show-current'),
            'status': git(root, 'status', '--porcelain=v1', '--untracked-files=all').decode()}


def identity(path):
    info = path.lstat()
    mode = stat.S_IMODE(info.st_mode)
    if stat.S_ISLNK(info.st_mode):
        return {'kind': 'symlink', 'mode': mode, 'target': os.readlink(path)}
    require(stat.S_ISREG(info.st_mode), 'Unsupported nonregular file: ' + str(path))
    return {'kind': 'file', 'mode': mode, 'bytes': info.st_size, 'sha256': sha(path)}


def snapshot(root, include_tracked):
    require(root.is_dir() and not root.is_symlink(), 'Unsafe worktree root: ' + str(root))
    require(Path(textgit(root, 'rev-parse', '--show-toplevel')).resolve() == root.resolve(),
            'Wrong Git worktree root')
    initial = state(root)
    # Deliberately omit --exclude-standard: hidden and ignored files are included.
    names = set(git(root, 'ls-files', '--others', '-z').split(b'\0')) - {b''}
    if include_tracked:
        names |= set(git(root, 'ls-files', '--cached', '-z').split(b'\0')) - {b''}
    files = {}
    for raw in sorted(names):
        relative = Path(os.fsdecode(raw))
        require(not relative.is_absolute() and '..' not in relative.parts, 'Unsafe file name')
        path = root / relative
        if path.is_dir() and not path.is_symlink():
            # Git can report a nested untracked repository as a directory.
            for directory, dirs, entries in os.walk(path, followlinks=False):
                for name in list(dirs):
                    q = Path(directory) / name
                    if q.is_symlink():
                        files[str(q.relative_to(root))] = identity(q)
                        dirs.remove(name)
                for name in entries:
                    q = Path(directory) / name
                    files[str(q.relative_to(root))] = identity(q)
        else:
            files[str(relative)] = identity(path)
    require(state(root) == initial, 'Git state changed while snapshotting: ' + str(root))
    return {'path': str(root), **initial, 'files': files,
            'scope': 'Tracked plus all nontracked worktree files' if include_tracked
                     else 'All nontracked worktree files, including hidden and ignored',
            'symlink_scope': 'Link targets and modes preserved; external targets are not followed.'}


def retained_tag():
    value = {'object': textgit(MAIN, 'rev-parse', TAG),
             'peeled_commit': textgit(MAIN, 'rev-parse', TAG + '^{commit}')}
    require(value == {'object': TAG_OBJECT, 'peeled_commit': TAG_COMMIT}, 'Retained tag changed')
    return value


def save(path, value):
    with path.open('x') as handle:
        json.dump(value, handle, indent=2)
        handle.write('\n')
        handle.flush()
        os.fsync(handle.fileno())


def main():
    require(not any(os.path.lexists(p) for p in [BEFORE, AFTER]), 'Receipt path collision')
    require(all(p.is_dir() and not p.is_symlink() for p in [MAIN, SKILL]), 'Unsafe worktree root')
    names = ['commit-receipt', 'pr-cleanup', 'postmerge-20261012-published-terminal']
    paths = {n: TMP / ('cmm-round57-' + n + '.json') for n in names}
    require(all(p.is_file() and not p.is_symlink() for p in paths.values()), 'Missing or unsafe prerequisite receipt')
    receipts = {n: json.loads(p.read_text()) for n, p in paths.items()}
    commit, cleanup, post = [receipts[n] for n in names]
    require(commit['base'] == BASE and commit['head'] == TOPIC and commit['tree'] == TREE, 'Wrong reviewed commit')
    require(cleanup['merge'] == MERGE and cleanup['tree'] == TREE and cleanup['head'] == TOPIC, 'Wrong merge receipt')
    require(cleanup['local_branch_absent'] and cleanup['remote_branch_absent'], 'Owned branch cleanup incomplete')
    require(post['exit_code'] == 0 and post['mode'] == 'postmerge' and post['trusted_base'] == BASE
            and post['merge_commit'] == MERGE and post['topic_head'] == TOPIC
            and post['expected_tree'] == TREE, 'Fresh postmerge checks incomplete or mismatched')
    require(sha(post['log']) == post['log_sha256'], 'Postmerge log hash mismatch')
    require(post['commands'] and all(c['exit_code'] in c['allowed_exit_codes'] for c in post['commands']), 'Postmerge command failed')
    require(any(c['command'] == ['just', 'check'] and c['exit_code'] == 0 for c in post['commands']), 'Fresh just check absent')
    require(post['counts'] == dict(record_count=267, history_count=315,
            structured_review_count=325, review_base_count=58, covered_records=267), 'Wrong postmerge counts')
    require(textgit(MAIN, 'remote', 'get-url', 'origin') == REMOTE, 'Wrong original origin')
    original, unrelated = snapshot(MAIN, False), snapshot(SKILL, True)
    require(original['head'] == BASE and original['branch'] == 'main' and not original['status'], 'Original main is dirty or changed')
    require(unrelated['head'] == SKILL_HEAD and unrelated['branch'] == SKILL_BRANCH, 'Unrelated worktree head/branch changed')
    tag = retained_tag()
    before = {'recorded_at': datetime.now(timezone.utc).isoformat(), 'recovered_access': True,
              'source_head': BASE, 'topic_head': TOPIC, 'merge': MERGE, 'tree': TREE,
              'helper_sha256': sha(__file__), 'snapshots': {'main': original, 'skill': unrelated},
              'retained_tag': tag, 'receipt_sha256': {str(p): sha(p) for p in paths.values()},
              'scope': 'Fresh recovered-access snapshots only. No assertion about bytes or access during the earlier unavailable period. Git administrative directories are excluded from file inventories; HEAD/branch/status and the retained tag are checked separately.'}
    save(BEFORE, before)  # Durable receipt exists before the first Git mutation.
    before_hash = sha(BEFORE)
    git(MAIN, 'fetch', '--no-tags', '--no-recurse-submodules', 'origin',
        'refs/heads/main:refs/remotes/origin/main', 'refs/tags/*:refs/tags/*')
    remote = {line.split()[1]: line.split()[0] for line in
              textgit(MAIN, 'ls-remote', 'origin', 'refs/heads/main', TAG, TAG + '^{}').splitlines()}
    require(remote == {'refs/heads/main': MERGE, TAG: TAG_OBJECT, TAG + '^{}': TAG_COMMIT}, 'Remote main/tag mismatch')
    require(textgit(MAIN, 'rev-parse', 'origin/main') == MERGE
            and textgit(MAIN, 'rev-parse', MERGE + '^{tree}') == TREE
            and textgit(MAIN, 'rev-parse', MERGE + '^') == BASE, 'Fetched merge tree/parent mismatch')
    incoming = {os.fsdecode(n) for n in git(MAIN, 'ls-tree', '-r', '-z', '--name-only', MERGE).split(b'\0') if n}
    nontracked = set(original['files'])
    for group, other in [(incoming, nontracked), (nontracked, incoming)]:
        for name in group:
            ancestors = {str(p) for p in Path(name).parents if str(p) != '.'}
            require(name not in other and not ancestors.intersection(other),
                    'Incoming tracked/nontracked path collision: ' + name)
    require(retained_tag() == tag and snapshot(MAIN, False) == original
            and snapshot(SKILL, True) == unrelated, 'State changed before fast-forward')
    git(MAIN, 'merge', '--ff-only', '--no-edit', '--no-autostash', MERGE)
    current, skill_after = snapshot(MAIN, False), snapshot(SKILL, True)
    require(current['head'] == MERGE and current['tree'] == TREE
            and current['branch'] == 'main' and not current['status'], 'Original main did not finish clean at the merge')
    require(current['files'] == original['files'], 'Original nontracked bytes changed')
    require(skill_after == unrelated and retained_tag() == tag, 'Unrelated worktree or retained tag changed')
    require(sha(BEFORE) == before_hash, 'Before receipt changed')
    after = {'recorded_at': datetime.now(timezone.utc).isoformat(), 'passed': True,
             'head': MERGE, 'tree': TREE, 'main': str(MAIN), 'skill': str(SKILL),
             'main_clean': True, 'main_nontracked_preserved': True,
             'unrelated_skill_preserved': True, 'retained_tag_preserved': True,
             'preserved_entry_counts': {'main': len(current['files']), 'skill': len(skill_after['files'])},
             'before_receipt': str(BEFORE), 'before_sha256': before_hash,
             'receipt_sha256': before['receipt_sha256'], 'recovered_access': True,
             'source_head': BASE, 'topic_head': TOPIC, 'merge': MERGE,
             'scope': 'Original main fast-forwarded only after successful fresh postmerge checks. Preservation covers the newly captured recovered-access interval, not the earlier unavailable period. Entire unrelated worktree file inventory and HEAD/branch/status remained identical; no unrelated cleanup or worktree operation ran.'}
    save(AFTER, after)
    print(json.dumps({'receipt': str(AFTER), 'sha256': sha(AFTER), **after}, indent=2))


if __name__ == '__main__':
    main()
