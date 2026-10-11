# Independent forward evaluation: cmmmech-add-record

Evaluated 2026-10-10. Repository: `/private/tmp/CMMMech-add-record-skill-20261010`; inspected HEAD `6a974c54d2c6e834d3514a9ada6272edc6a2aa74`. Scope: the new skill and its live local record, schema, history and structured-review contracts. This was a read-only workflow simulation, not curation or a fresh scientific review. No GitHub contact, record creation, history creation or review publication occurred. All evaluation outputs are in this directory.

**Result: no supported blocker, major or minor defect found in the two scenarios.** A small optional clarity suggestion appears below. Required command spellings and ordering are consistent with the current CLI, justfile and contracts.

## Scenario 1: “Use the discovery handoff to add a cobaltite record with the evidence we have.”

1. Read the landscape assessment/search log/acquisition manifest, ingest priorities and current record/reviews. The handoff I1 was already ingested: `data/records/cobaltite.yaml` is a mineral identity record and the queue calls it completed. Hidden/ignored-inclusive searches covered repository `data`, `research`, `reviews`, `history`, plus exact download paths referenced by the acquisition manifest; this was not a machine-wide search.
2. Resolve identity before acting: the existing record denotes cobaltite, CoAsS, from the dated September 2026 IMA list. It does not denote the cobalt element or battery black mass. The 1832 value is described as original-description year, not an IMA approval number. Do not introduce an unverified RRUFF search-probe ID, copy cobalt criticality, or add battery bioleaching as a cobaltite mechanism. These decisions follow skill lines 24–43 and 45–80 and match `docs/records.md`.
3. Deduplicate instead of creating a second record. No additional supported claim was identified in the supplied handoff. A defensible outcome is “already represented; no record change needed,” with links to the existing identity record and scientific review. If later evidence warrants a change, update cobaltite in an isolated worktree, record EDIT history and obtain a final-hash review. Do not manufacture a change just to run the create workflow.
4. Evidence availability: the exact cited local IMA PDF exists and its SHA-256 equals the acquisition manifest (`2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973`). I verified file presence and hash only, not its mineral rows or current remote status. The existing scientific review is `reviews/structured/20261010T011911Z-cobaltite-pr-science/{review.yaml,review.md}`; its target hash equals current cobaltite bytes (`f19fa6105e65527f70525b08c5064a53d85e72cd8dd3823835d635babdb562d5`). Prior review assertions remain attributed to that prior review.

Acceptance checks: one cobaltite material record; mineral rather than element identity; no inherited Co criticality/mechanism; no unsupported external ID; if unchanged, no fabricated CREATE/EDIT provenance; if changed, a new current-hash structured scientific review and explicit prior-finding dispositions when applicable.

## Scenario 2: “Add an experimentally supported material record from a new primary paper, keeping contradictory results, then prepare local review; do not publish.”

I used existing `data/records/lithium.yaml` and its Kirk 2024 primary-paper/dataset handoff as the permitted raw-evidence example. This does not claim a new paper was found or new curation performed. Because lithium already exists, actual application would extend that record if fresh evidence justified it, not create another lithium record.

The skill routes additional investigation to discovery, then returns to curation. Required scientific decisions are concrete in this example: retain a transient jadarite-bearing-material comparison, day-30 uninoculated-control convergence, stronger acid-only result, null spodumene/lepidolite comparisons, unresolved 2 g/200 mL versus 2% loading, differing acid additions, and uncertainty in culture/strain identification. The later dataset findings retain mg/kg versus mg/L ambiguity, aggregate/replicate inconsistencies and duplicated cross-material replicate blocks without choosing invented corrected values. Do not generalize to all Li ores, normalized yields, purified recovery or industrial deployment. The quoted mg/kg source-cell observation contract cannot justify importing recovery percentages or unit-converted values. The retained local article HTML exists and its hash matches the manifest, but I did not re-review its methods in this evaluation.

A concrete command sequence for a future authorized lithium evidence extension is below. These commands are **not executed in this evaluation**. `just new-history` is used only after actual supported changes; replace the example summary/details with a finished account of those actual changes. For a genuinely absent material, use its verified slug and `--event CREATE` instead of lithium/EDIT.

```sh
git status --short
git worktree list
git rev-parse HEAD
git worktree add -b curate/lithium-paper-20261010 /private/tmp/CMMMech-lithium-paper-20261010 6a974c54d2c6e834d3514a9ada6272edc6a2aa74
cd /private/tmp/CMMMech-lithium-paper-20261010
just check
rg --no-ignore --hidden -n -i 'lithium|1467408|djkf7tkm8d' data research reviews history
# Inspect primary evidence/authorities and make only supported YAML edits.
just new-history --slug lithium --actor-type ai_agent --actor-name codex --model GPT-6 --agent-tool codex --event EDIT --outcome changed --summary 'Extend lithium evidence with inspected primary results and contradictions.' --details 'Describe actual inspected evidence, locators, retained contradictory results, checks already run and unresolved limits.'
# Append the printed path to history_refs; append a distinct actual inline event.
uv run --locked cmmmech validate data/records/lithium.yaml
uv run --locked cmmmech validate-history --base 6a974c54d2c6e834d3514a9ada6272edc6a2aa74
uv run --locked python scripts/record_review.py inspect --targets /private/tmp/cmmmech-add-skill-evaluation/lithium-targets.yaml --input docs/records.md --input src/cmmmech/schema/cmmmech.yaml --input research/ingests/mn-li-evidence.md
# Repeat --input for each new sidecar and other local input informing the review.
# Independent reviewer reads exact inspected bytes, primary evidence and review contract.
# Run required scientific-review checks before claiming completed passing status.
just check
uv run --locked cmmmech validate --require-records
uv run --locked python scripts/record_review.py validate /private/tmp/cmmmech-add-skill-evaluation/completed-lithium-review.yaml
uv run --locked python scripts/record_review.py save --content /private/tmp/cmmmech-add-skill-evaluation/completed-lithium-review.yaml
just review-check --base 6a974c54d2c6e834d3514a9ada6272edc6a2aa74 --require-reviews
```

The completed-review file above is intentionally not supplied: it must contain a real independent assessment, actual UTC times/check results, captured `source`, full target ownership/scope, evidence-linked assessments, findings/actions and limits. Existing `lithium-targets.yaml` is a valid concrete target specification. The inspection JSON must be retained in `source`, with extra inputs added before judging. History references must be attached before this inspection. After a substantive correction, repeat affected validation/evidence checks and inspect/save a new final-byte observation, preserving prior bundles and stable issue keys with exact `previous_occurrences`. After final checks, manually match every changed record hash to its scientific review; `--require-reviews` proves only nonempty coverage.

Acceptance checks: supported narrow observation plus explicit contrary/null results; no invented strain ID or causality; properly scoped criticality only if separately verified; exact source-cell semantics or no numerical observation; real history and final-byte review; no unresolved major/blocker finding hidden by a pass; local YAML/Markdown review artifacts reported; no commits, push, PRs, issues, comments, merge, provenance-tag push or governance changes triggered by “do not publish.”

## Contract and command verification

Read: `CLAUDE.md`, `README.md`, `docs/records.md`, `src/cmmmech/schema/cmmmech.yaml`, `docs/record-reviews.md`, `docs/record-review-profile.md`, discovery and record-review skills, `justfile`, `scripts/check.py`, relevant history/review CLI code and tests. The material kinds, support values, required fields, history sidecar/inline distinction, inspect-before-judgment order, immutable saver outputs and append-only bases agree. Publication instructions are conditional and correctly route retained review bases to the squash-queue procedure.

Actually ran `.venv/bin/python -B scripts/record_review.py inspect` for cobaltite and lithium with the supplied targets and relevant `--input` paths: both exited 0 and returned `inspection_only`, the actual HEAD and input hashes. Outputs: `cobaltite-inspection.json`, `lithium-inspection.json`. No save/new-history commands were run. I did not duplicate the full suite; the parent reported quick validation success, `just check` with 298 passed/3 skipped, 10 valid records, 19 valid histories and 12 valid structured reviews. Those results are parent-reported, not independent executions here.

## Findings and limitations

No supported defect requires a corrective edit. Optional informational wording improvement: skill lines 31–33 could explicitly say “If the record already contains the supported handoff claims, report that no change is needed.” This would make scenario 1's no-op outcome easier to see beside the later unconditional-sounding “Create one…” and history steps. It is not a blocking conflict: current “within requested curation scope,” “actual change,” and no-fabrication instructions already support the correct outcome. Acceptance: a dry run against the current cobaltite handoff produces no duplicate record and no invented curation event.

This evaluation did not establish fresh scientific truth, latest IMA status, live identifier resolution, correction/retraction completeness or publication portability. It establishes that the skill gives a coherent, executable route and appropriate evidence/scope boundaries for these local simulations.
