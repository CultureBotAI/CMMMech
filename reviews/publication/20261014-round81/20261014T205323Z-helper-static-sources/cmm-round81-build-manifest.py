from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, subprocess, yaml

w = Path('/private/tmp/CMMMech-expansion-round81-20261014')
p = Path('/private/tmp')
cfg = json.loads((p / 'cmm-round81-helper-config.json').read_text())
sha = lambda q: hashlib.sha256(q.read_bytes()).hexdigest()
now = lambda: datetime.now(timezone.utc).isoformat()
checks = w / 'research/ingests/round81-checks-20261014'
checks.mkdir(parents=True, exist_ok=True)
for suffix in ['baseline', 'final-gates', 'review-check-final', 'local-coverage', 'governed-check', 'preservation-precommit']:
    source = p / ('cmm-round81-' + suffix + '.json')
    receipt = json.loads(source.read_text())
    assert receipt.get('passed', receipt.get('exit_code') == 0), suffix
    destination = checks / (suffix + '.json')
    assert not destination.exists()
    destination.write_bytes(source.read_bytes())
    if 'log' in receipt:
        log = Path(receipt['log'])
        assert sha(log) == receipt['log_sha256']
        (checks / (suffix + '.log')).write_bytes(log.read_bytes())

publication = w / 'reviews/publication/20261014-round81'
publication.mkdir(parents=True, exist_ok=True)
for name in ['helper-config', 'helper-derivation', 'initialization', 'source-issues-posted']:
    source = p / ('cmm-round81-' + name + '.json')
    destination = publication / (name + '.json')
    assert not destination.exists()
    destination.write_bytes(source.read_bytes())

rows = []
reviews = [(rp, yaml.safe_load(rp.read_text())) for rp in (w / 'reviews/structured').glob('*round81*/review.yaml')]
for slug in cfg['slugs']:
    relative = 'data/records/' + slug + '.yaml'
    owner = w / relative
    record = yaml.safe_load(owner.read_text())
    digest = sha(owner)
    matches = []
    for rp, review in reviews:
        if review['completion'] != 'completed' or not review['scientific_review'] or review['verdict'] not in ('pass', 'pass_with_limitations'):
            continue
        if record['id'] not in review['scope']['reviewed_target_ids']:
            continue
        if not any(i['path'] == relative and i['sha256'] == digest for i in review['source']['inputs']):
            continue
        assert review['reviewer']['independence'] == 'independent'
        matches.append((rp, review))
    assert matches, slug
    rp, review = sorted(matches, key=lambda item: item[1]['review_id'])[-1]
    rows.append(dict(slug=slug, id=record['id'], name=record['name'], material_kind=record['material_kind'], path=relative, sha256=digest,
                     review=dict(path=str(rp.relative_to(w)), review_id=review['review_id'], review_sha256=sha(rp), verdict=review['verdict']),
                     review_markdown=str(rp.with_suffix('.md').relative_to(w)), history_refs=record['history_refs']))

source_reports = sorted(str(q.relative_to(w)) for q in (w / 'research/sources').glob('round81-*/*.md'))
paths = set(subprocess.check_output(['git', 'diff', '--name-only'], cwd=w, text=True).splitlines()) | set(subprocess.check_output(['git', 'ls-files', '--others', '--exclude-standard'], cwd=w, text=True).splitlines())
audit = Path(cfg['publication_peer_review'])
assert not paths.intersection({str(audit.relative_to(w)), str(audit.with_suffix('.md').relative_to(w))})
manifest = dict(recorded_at=now(), base=cfg['base'], branch=cfg['branch'], worktree=str(w), state='working_tree',
                selection=cfg['selection'], records=rows, counts=cfg['counts'], issues=cfg['issues'], source_reports=source_reports,
                pre_manifest_inputs=[dict(path=name, sha256=sha(w/name)) for name in sorted(paths)])
destination = w / 'research/ingests/round81-frontier-20261014.json'
assert not destination.exists() and not destination.with_suffix('.md').exists()
destination.write_text(json.dumps(manifest, indent=2) + '\n')
lines = ['# Round81: qualified mineral phases and photographic-fixer additions', '',
         f"Recorded UTC: {manifest['recorded_at']}. Trusted base `{cfg['base']}`; branch `{cfg['branch']}`.", '',
         cfg['selection'], '',
         '| Record | Independent scientific review | Canonical history |', '|---|---|---|']
for row in rows:
    history_links = ' · '.join(f'[history {i+1}](../../{hp})' for i, hp in enumerate(row['history_refs']))
    lines.append(f"| [{row['name']}](../../{row['path']}) | [Markdown](../../{row['review_markdown']}) · [YAML](../../{row['review']['path']}) — {row['review']['verdict']} | {history_links} |")
lines += ['', cfg['limitations'], '', cfg['issue_summary'], '',
          f"Validation: `just check` passed with 317 tests passed and 3 skipped; strict `--require-records` checked {cfg['counts']['record_count']} records; trusted-base history checked {cfg['counts']['history_count']} entries; the structured review checker validated {cfg['counts']['structured_review_count']} bundles. Exact-hash positive scientific coverage is {cfg['counts']['covered_records']}/{cfg['counts']['record_count']} records across {cfg['counts']['review_base_count']} available bases. Generated pages are current, and all 22 governed artifacts match the immutable CLAW pin. No schema, validator, tests or governed configuration changed. [Receipts and logs](round81-checks-20261014/) retain the actual results.", '',
          'Source dossiers: ' + ', '.join(f'[{Path(r).parent.name}](../../{r})' for r in source_reports) + '. Paired JSON files retain acquisition routes, hashes, search scope and limitations; original articles remain outside Git.', '',
          '[Publication evidence](../../reviews/publication/20261014-round81/) retains initialization, helper derivation and the independent final audit. Exact-head hosted review, isolated squash-shaped preflight, native queue merge, branch deletion and fresh remote-main validation remain future steps at this timestamp.', '',
          'Original main and the unrelated skill worktree are protected by snapshots including hidden/ignored bytes, modes and symlink targets. Git administration and external symlink-target contents are excluded. Discovery is bounded; no exhaustion claim is made.', '']
destination.with_suffix('.md').write_text('\n'.join(lines))
print(str(destination), len(rows), 'records;', len(paths), 'pre-manifest inputs')
