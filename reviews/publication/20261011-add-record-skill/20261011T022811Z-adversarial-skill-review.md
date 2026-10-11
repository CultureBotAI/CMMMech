# Independent adversarial review of CMMMech add-record skill

Report time: 2026-10-11T02:28:11.747691Z
Reviewer: Codex /root/skill_pr_adversarial, independent agent distinct from the author; no tracked repository edits or GitHub interaction performed.
Verdict: **PASS within the declared scope.** No supported actionable defects found (0 blocker, 0 major, 0 minor). No additional enhancement is raised here.

## Scope and exact state

Repository: `/private/tmp/CMMMech-add-record-publish-20261010`.
Reviewed revision: `f868565e039b3da81da2d0417ef1e6a3fc9962a4`.
Trusted comparison base: `6a974c54d2c6e834d3514a9ada6272edc6a2aa74`.
Working state: clean (`git status --porcelain=v1 --untracked-files=all` returned empty both before and after verification). The five files below cover the entire commit diff. This report assesses skill instructions and their compatibility with native contracts; it does not reassess the corpus's scientific claims.

| Reviewed file | Working-file SHA-256 |
|---|---|
| `.claude/skills/cmmmech-add-record/SKILL.md` | `43003f1f61daeb8297d3961f2c0a6299b75025059375714643bb257d018a6c5c` |
| `.claude/skills/cmmmech-add-record/agents/openai.yaml` | `7825374cafeda8e12eb45593ac942945192caa517c19ed981a9589c4e074d5cc` |
| `.claude/skills/cmmmech-discover-sources/SKILL.md` | `f05618c116fb1e58f7ea01d65a8bfd53306d35569240f1b8fe54504d4dcfb549` |
| `README.md` | `6c3b4d65b6b8aa38011b767e76fc4e7b278b3c409fc3bbd04e8c384e2ef703f2` |
| `CLAUDE.md` | `5a947ff9de7e825362e1e0f8a8c70470db09cfd8a98bbc7a200aeef8ec427d7f` |

## Inspected evidence

- Full five-file diff and full new skill. Native working agreements in `CLAUDE.md`, scope/checks in `README.md`, complete `docs/records.md`, `docs/record-reviews.md`, `docs/record-review-profile.md`, and `.claude/skills/review-record/SKILL.md`.
- Current discovery skill, authoritative `src/cmmmech/schema/cmmmech.yaml`, `src/cmmmech/validation.py`, `src/cmmmech/cli.py`, `src/cmmmech/history.py`, `scripts/record_review.py`, `justfile`, `scripts/check.py`.
- Relevant native tests: `tests/test_skill_frontmatter.py`, `tests/test_validation.py`, `tests/test_cli.py`, `tests/test_history.py`, `tests/test_observations.py`, `tests/test_record_review_contract.py`; representative saved Cobaltite structured review and complete file inventory.
- Inventory/search used `rg --files -uu` and `rg --no-ignore --hidden`, including hidden and ignored files. Deliberate inventory exclusions were Git internals, virtual environments and bytecode directories. Relevant project tests/schema/scripts were searched without ignore filtering. No machine-wide absence claim is made; unrelated home/temp files and unavailable local downloads were not needed for this instruction review.

## Adversarial scenarios and acceptance checks

1. Identity-only record: allowed without criticality or mechanisms. Schema rejects unsupported root kind `ion`; the skill's material distinction and current-kind list agree with that boundary.
2. Inactive biomass: a microbial mechanism with explicit inactive state and `microbial: true` validates; organism assertions with `microbial: false` fail. The instructions do not imply metabolism.
3. Censored concentration: negative-limit encoding retained as `raw_value: '-0.025'`, `detection_limit: 0.025`, `mg/kg`, and an abiotic arm under a microbial mechanism validates. Adding zero as a measured value fails; `mg/L` fails; a duplicate source cell under another ID fails; sampling after analysis fails.
4. Duplicate material: the skill mandates identity/ID deduplication and updates the existing record within scope. The whole-corpus CLI demonstrably rejects duplicate record IDs that individually valid files would not expose.
5. History: instructions create the target before `new-history`, append the helper's printed reference, distinguish inline events, and capture review hashes after history changes. Existing native tests exercised missing metadata, symlink aliases, collision safety, exact target matching, trusted-base append-only enforcement and preservation of historical sessions.
6. Review freshness and unresolved findings: final hashes, new immutable rounds, stable issue keys, exact predecessor links and manual per-record coverage are explicitly required. Existing tests exercised immutable saver pairs, stale input rejection and false-pass rejection; the skill does not treat a nonempty review gate as coverage.
7. Blocked evidence: unavailable full text narrows/defer claims, unresolved details remain explicit and unavailable required checks produce an honest partial/blocked observation. No forced mechanism or invented criticality is required.
8. Publication: local curation does not grant external mutation authorization. Existing authorization is respected. The linked native publication contract enumerates all otherwise-lost bases, exact provenance tags, trusted-base checks and isolated squash/fresh-main verification; saved reviews remain immutable.
9. Skill integration: README/CLAUDE and discovery handoff point to the correct repository-relative file, while the new skill delegates scientific review to the maintained review skill. Agent display metadata parses; frontmatter passes the repository guard.

Executed checks, all exit 0 unless a rejection was the expected boundary result:

- `PYTHONPATH=/private/tmp/CMMMech-add-record-publish-20261010/src PYTHONDONTWRITEBYTECODE=1 PYTEST_ADDOPTS='-p no:cacheprovider' RUFF_NO_CACHE=true /private/tmp/CMMMech-add-record-skill-20261010/.venv/bin/python scripts/check.py`: lint passed; **298 tests passed, 3 skipped**; 10 records validated; 19 history sidecars validated. This invokes the same native script as `just check` using already installed dependencies.
- `PYTHONPATH=/private/tmp/CMMMech-add-record-publish-20261010/src PYTHONDONTWRITEBYTECODE=1 /private/tmp/CMMMech-add-record-skill-20261010/.venv/bin/python scripts/record_review.py check --base 6a974c5 --require-reviews`: 12 valid saved bundles; declared scopes only.
- External scratch harness `/private/tmp/cmmmech-skill-pr-review/boundary-checks.py`: all 10 synthetic scenarios met their expected acceptance/rejection outcomes. Full output retained in `boundary-results.json`; no synthetic record was placed in the repository corpus.
- `git diff --check 6a974c5 HEAD`: passed.

## Findings and limitations

No actionable defect was established in the five-file change. The separate suggestion to make already-satisfied/no-op handoffs explicit was reported by the parent after this review began; it is not needed to repair a demonstrated failure and is not duplicated as a finding here. Any subsequent text change needs a focused review of its new hash.

This review used local contracts and deterministic/synthetic checks. It did not execute a live literature curation, verify remote sources, contact GitHub, exercise queue publication, or independently rerun the networked governed-artifact synchronization check. The three existing test skips were retained as skips, not counted as passes. The full corpus and review bundles were validated structurally; scientific truth and model obedience to every prose instruction are outside this bounded review.

Acceptance: the reviewed bytes can proceed under the existing publication authorization and required repository CI. No corrective action is required by this review.
