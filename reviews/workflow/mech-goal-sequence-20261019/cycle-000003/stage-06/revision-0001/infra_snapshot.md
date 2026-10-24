# CMMMech infrastructure tasks

This versioned ledger collects repository requirements and upgrades discovered
during every goal. The workflow profile and its parent govern intake, stage 6
implementation, closure and cycle restart.

## Intake protocol

- Give each actionable task a stable ID such as `cmmmech-infra-0001` and retain it
  across cycles. Record the originating run, cycle and goal, observation,
  desired outcome, evidence paths, priority, dependencies and status.
- Link each task to an actual issue in https://github.com/CultureBotAI/CMMMech/issues.
  Search existing open and closed issues before creating one. If access fails,
  retain an explicit pending-link blocker; never invent an issue number or URL.
- Preserve resolved and deferred entries with their issue, implementation PR,
  validation and disposition. Do not overwrite previous cycle evidence.
- At stage 6, freeze a bounded snapshot, write a dependency-aware plan and
  acceptance criteria, implement selected work, validate, and complete the
  commit sequence, write the closure receipt and stop; only the supervisor
  dispatches another goal. New arrivals after the cutoff enter the next cycle;
  never expand the frozen task-ID scope. A new blocking prerequisite requires
  an explicit deferred disposition for the selected task. Carry unfinished work
  forward explicitly.

## Machine-readable task inventory

This fenced mapping is the inventory stage 6 freezes and reconciles. Each task
uses `task_id`, `summary`, `status` (`note`, `open`, `deferred`, or `resolved`),
optional `issue_url`, and optional `disposition`. Status `note` may have a
pending issue link; all other statuses require a real issue URL. Keep richer
notes below keyed by the same stable task ID.

<!-- mech-infra-tasks:start -->
```yaml
schema_version: '1.0.0'
tasks:
  - task_id: cmmmech-infra-0001
    summary: Anchor scripts/record_review.py _directory() traversal at repository ROOT instead of filesystem root / so review validation runs inside Seatbelt sandboxes
    status: deferred
    issue_url: https://github.com/CultureBotAI/CMMMech/issues/805
    disposition: "Deferred in Cycle 1 Stage 6 and carried forward in Cycle 2 Stage 6 because scripts/record_review.py and tests/test_record_review_contract.py are vendored artifacts governed by CultureBotAI/culturebotai-claw (enforced by scripts/check_vendored_sync.py); tracked under open issue #805 for coordinated upstream implementation and sync."
  - task_id: cmmmech-infra-0002
    summary: Add optional MaterialTerm/CriticalMineralRecord metadata slots for IMA mineral symbols and engineered material polymorph/grade identifiers in src/cmmmech/schema/cmmmech.yaml
    status: resolved
    issue_url: https://github.com/CultureBotAI/CMMMech/issues/806
    disposition: "Resolved in Cycle 1 Stage 6 (issue #806) by adding optional backward-compatible ima_symbol and polymorph_or_grade slots to CriticalMineralRecord in src/cmmmech/schema/cmmmech.yaml, surfacing them in scripts/render_pages.py and src/cmmmech/templates/material.html, and covering them with unit tests in tests/test_validation.py and tests/test_render_pages.py."
  - task_id: cmmmech-infra-0003
    summary: Expand CausalPredicateEnum in src/cmmmech/schema/cmmmech.yaml with solubilizes/dissolves and hydrolyzes/degrades for acidolytic mineral leaching and enzymatic polymer stripping
    status: resolved
    issue_url: https://github.com/CultureBotAI/CMMMech/issues/807
    disposition: "Resolved in Cycle 1 Stage 6 (issue #807) by adding degrades, dissolves, hydrolyzes, and solubilizes to CausalPredicateEnum in src/cmmmech/schema/cmmmech.yaml and validating them in tests/test_validation.py."
  - task_id: cmmmech-infra-0004
    summary: Add a first-class CLI writer helper (scripts/curate_causal_graphs.py) that validates causal_graphs and protein_examples updates and atomically mints history/records sidecars
    status: resolved
    issue_url: https://github.com/CultureBotAI/CMMMech/issues/808
    disposition: "Resolved in Cycle 1 Stage 6 (issue #808) by implementing scripts/curate_causal_graphs.py with canonical key ordering, pre-write schema validation, and atomic EDIT HistoryRecord sidecar creation, verified by tests/test_curate_causal_graphs.py."
  - task_id: cmmmech-infra-0005
    summary: Batch git cat-file object size and content checks in scripts/record_review.py assert_append_only() and source_provenance() via git cat-file --batch
    status: deferred
    issue_url: https://github.com/CultureBotAI/CMMMech/issues/805
    disposition: "Deferred in Cycle 1 Stage 6 and carried forward in Cycle 2 Stage 6 because scripts/record_review.py is a vendored artifact governed by CultureBotAI/culturebotai-claw (enforced by scripts/check_vendored_sync.py); grouped with cmmmech-infra-0001 under open issue #805 for upstream implementation and sync."
  - task_id: cmmmech-infra-0006
    summary: Replace os.link() in src/cmmmech/history.py cmd_new() with exclusive-create or os.replace() fallback so scripts/curate_causal_graphs.py and cmmmech new-history succeed inside macOS Seatbelt sandboxes
    status: resolved
    issue_url: https://github.com/CultureBotAI/CMMMech/issues/822
    disposition: "Resolved in Cycle 2 Stage 6 (issue #822) by adding an exclusive-create fallback (os.open with O_WRONLY | O_CREAT | O_EXCL | O_NOFOLLOW) when os.link() raises PermissionError in src/cmmmech/history.py cmd_new(), verified by unit tests in tests/test_history.py and sandboxed execution of tests/test_curate_causal_graphs.py."
  - task_id: cmmmech-infra-0007
    summary: Add a path-based directory cleanup fallback when shutil.rmtree() raises PermissionError on dir_fd unlinkat() in scripts/render_pages.py so static page rendering succeeds inside macOS Seatbelt sandboxes
    status: note
  - task_id: cmmmech-infra-0008
    summary: Extend scripts/curate_causal_graphs.py apply_curation_patch() to support mechanism-id-keyed organisms, evidence, and observations updates alongside causal_graphs and protein_examples
    status: note
  - task_id: cmmmech-infra-0009
    summary: Node-level protein_examples upsert and mechanism/node parity enforcement in scripts/curate_causal_graphs.py
    status: note
```
<!-- mech-infra-tasks:end -->

## Tasks

### `cmmmech-infra-0001` — Anchor `scripts/record_review.py` `_directory()` traversal at repository `ROOT`

- **Originating run / cycle / stage**: `mech-goal-sequence-20261019` / cycle `1` / stage `1` (`add_records`)
- **Observation**: `scripts/record_review.py` `_directory()` (`lines 384-407`, with `repository_identity()` at `lines 449-455`) opens `/` and traverses every path component downward via `os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=current)` starting at `/Users`. In macOS Seatbelt sandboxes where ancestor directories above the workspace (`/Users`, `/Users/<user>`) disallow `O_RDONLY` directory opens even though the repository root (`/Users/marcin/Documents/VIMSS/ontology/Mechs/CMMMech`) is readable and writable, `python scripts/record_review.py --validate` and `pytest tests/test_record_review_contract.py` fail with `PermissionError: [Errno 1] Operation not permitted: 'Users'`. Because `scripts/record_review.py` and `tests/test_record_review_contract.py` are governed artifacts synchronized from `CultureBotAI/culturebotai-claw` and checked by `scripts/check_vendored_sync.py`, any change requires coordinated upstream update or explicit Stage 6 disposition.
- **Desired outcome**: Anchor `_directory()` at `ROOT` (verify `ROOT` is a non-symlink directory, open `ROOT`, and walk only relative components beneath `ROOT` with `O_NOFOLLOW`) in `culturebotai-claw` and sync to `scripts/record_review.py` and `tests/test_record_review_contract.py` so review validation succeeds inside standard workspace sandboxes while preserving symlink-traversal protection inside the repository.
- **Evidence paths**: `scripts/record_review.py`, `tests/test_record_review_contract.py`, `scripts/check_vendored_sync.py`
- **Priority**: medium
- **Dependencies**: Upstream `CultureBotAI/culturebotai-claw` vendored-artifact governance (`scripts/check_vendored_sync.py`)
- **Issue**: https://github.com/CultureBotAI/CMMMech/issues/805 (`IGRP-C1S6-001`)
- **Status**: `deferred`
- **Disposition**: Deferred in Cycle 1 Stage 6 because `scripts/record_review.py` and `tests/test_record_review_contract.py` are governed vendored artifacts enforced by `scripts/check_vendored_sync.py`. Tracked in issue `#805` for upstream implementation in `CultureBotAI/culturebotai-claw` and subsequent vendored sync.

### `cmmmech-infra-0002` — Optional `CriticalMineralRecord` slots for IMA symbols and polymorph/grade classifications

- **Originating run / cycle / stage**: `mech-goal-sequence-20261019` / cycle `1` / stage `1` (`add_records`)
- **Observation**: During Round 117 (`discover_add`), curating 11 IMA-approved critical-element mineral species (`adamsite-y`, `ammonioborite`, `bainbridgeite-ndce`, `ferrokesterite`, `mckelveyite-y`, `petrukite`, `piilonenite-nd`, `richetite`, `sakuraiite`, `thomasclarkite-y`, `weeksite`) and 3 DOE/USGS/EU synthetic/engineered critical materials (`electrical-steel`, `silicon-carbide`, `synthetic-graphite`) showed that `CriticalMineralRecord` (`src/cmmmech/schema/cmmmech.yaml`) has `ima_status` and `ima_approval_year` for minerals, but lacks an optional `ima_symbol` slot (e.g., `Ads-Y`, `Abor`, `Bbg-NdCe`, `Fkes`, `Mkv-Y`, `Pet`, `Pii-Nd`, `Rch`, `Sak`, `Tcl-Y`, `Wks`) and lacks a structured polymorph/grade descriptor slot for engineered materials (e.g., `3C-SiC`/`4H-SiC`/`6H-SiC`, `GOES`/`NOES`), requiring those standard identifiers to be placed in `synonyms` or prose `description`.
- **Desired outcome**: Evaluate adding optional backward-compatible `ima_symbol` and material grade/polymorph slots in `src/cmmmech/schema/cmmmech.yaml` (and surfacing them in `scripts/render_pages.py`) during Stage 6 infrastructure implementation.
- **Evidence paths**: `src/cmmmech/schema/cmmmech.yaml`, `scripts/render_pages.py`, `src/cmmmech/templates/material.html`, `tests/test_validation.py`, `tests/test_render_pages.py`
- **Priority**: low
- **Dependencies**: None
- **Issue**: https://github.com/CultureBotAI/CMMMech/issues/806 (`IGRP-C1S6-002`)
- **Status**: `resolved`
- **Disposition**: Resolved in Cycle 1 Stage 6 by adding optional `ima_symbol` and `polymorph_or_grade` attributes (`range: NonEmptyText`) to `CriticalMineralRecord` in `src/cmmmech/schema/cmmmech.yaml`, rendering badges and indexing search tokens in `scripts/render_pages.py` and `src/cmmmech/templates/material.html`, and verifying with unit tests in `tests/test_validation.py` and `tests/test_render_pages.py`.

### `cmmmech-infra-0003` — Expand `CausalPredicateEnum` for acidolytic leaching and enzymatic binder hydrolysis

- **Originating run / cycle / stage**: `mech-goal-sequence-20261019` / cycle `1` / stage `2` (`causal_graphs`)
- **Observation**: During the Stage 2 corpus-wide causal-graph audit and expansion across 55 records (`42` existing + `13` newly eligible multi-step records), organic-acid mineral dissolution (`moolooite`, `phosphate-rock`, `lindbergite`, `katsarosite`, `humboldtine`, `falottaite`, `bauxite-residue`) and proteolytic gelatin-emulsion stripping (`waste-x-ray-films`) had to use `chelates` or `acts_on` because `CausalPredicateEnum` (`src/cmmmech/schema/cmmmech.yaml:498` and `src/cmmmech/validation.py`) currently permits `['acts_on', 'assembles_into', 'binds', 'catalyzes', 'chelates', 'displays_on_surface', 'drives', 'incorporates_into', 'inhibits', 'modulates', 'negatively_regulates', 'nucleates', 'oxidizes', 'positively_regulates', 'produces', 'provides_electrons_to', 'reduces', 'supplies_substrate_for', 'transforms_into', 'transports']` and omits `solubilizes` / `dissolves` and `hydrolyzes` / `degrades`. In addition, 93 single-step biosorption/bioaccumulation records in `data/records/` document only whole-cell equilibrium sorption or intracellular uptake without resolved molecular intermediates; forcing multi-step `causal_graphs` onto those 93 records would require inventing unsupported intermediate nodes.
- **Desired outcome**: Evaluate adding `solubilizes` and `hydrolyzes` (or `degrades`) to `CausalPredicateEnum` in `src/cmmmech/schema/cmmmech.yaml` and `src/cmmmech/validation.py` during Stage 6 while preserving the strict curation rule that single-step whole-cell sorption/uptake records without resolved intermediates remain represented at the `mechanisms` level rather than via synthetic causal edges.
- **Evidence paths**: `src/cmmmech/schema/cmmmech.yaml`, `tests/test_validation.py`, `data/records/moolooite.yaml`, `data/records/phosphate-rock.yaml`, `data/records/waste-x-ray-films.yaml`
- **Priority**: medium
- **Dependencies**: None
- **Issue**: https://github.com/CultureBotAI/CMMMech/issues/807 (`IGRP-C1S6-003`)
- **Status**: `resolved`
- **Disposition**: Resolved in Cycle 1 Stage 6 by adding `degrades`, `dissolves`, `hydrolyzes`, and `solubilizes` to `CausalPredicateEnum` in `src/cmmmech/schema/cmmmech.yaml` and testing all 4 predicates in `tests/test_validation.py`.

### `cmmmech-infra-0004` — Add a first-class CLI writer helper for `causal_graphs` and `protein_examples` curation

- **Originating run / cycle / stage**: `mech-goal-sequence-20261019` / cycle `1` / stage `2` (`causal_graphs`)
- **Observation**: While `.claude/skills/curate-yaml-record/SKILL.md` and `src/cmmmech/validation.py` define the canonical curation workflow and validation gates, curating or auditing `causal_graphs` and `protein_examples` across 52 records required custom Python scripts to enforce canonical key ordering (`causal_graphs` immediately after `mechanisms`, before `curation_history` and `history_refs`), run `cmmmech.validation.validate_record`, and atomically mint `history/records/<slug>/<timestamp>-<agent>-<hash>.yaml` sidecars.
- **Desired outcome**: Add a dedicated helper CLI (`scripts/curate_causal_graphs.py` or a `cmmmech` CLI subcommand) that validates `causal_graphs` / `protein_examples` against `src/cmmmech/validation.py`, enforces canonical YAML key ordering, and atomically writes the `EDIT` history sidecar and `curation_history`/`history_refs` entries.
- **Evidence paths**: `scripts/curate_causal_graphs.py`, `tests/test_curate_causal_graphs.py`, `src/cmmmech/validation.py`, `src/cmmmech/history.py`
- **Priority**: low
- **Dependencies**: `cmmmech-infra-0002`, `cmmmech-infra-0003`
- **Issue**: https://github.com/CultureBotAI/CMMMech/issues/808 (`IGRP-C1S6-004`)
- **Status**: `resolved`
- **Disposition**: Resolved in Cycle 1 Stage 6 by creating `scripts/curate_causal_graphs.py` with canonical key ordering (`CANONICAL_RECORD_KEYS` and `CANONICAL_MECHANISM_KEYS`), structured patch application, pre-write schema validation, and atomic `EDIT` history sidecar creation via `cmmmech.history.cmd_new`, tested in `tests/test_curate_causal_graphs.py`.

### `cmmmech-infra-0005` — Batch `git cat-file` object checks in `scripts/record_review.py`

- **Originating run / cycle / stage**: `mech-goal-sequence-20261019` / cycle `1` / stage `4` (`record_review`)
- **Observation**: In `scripts/record_review.py`, `assert_append_only()` (`lines 710-733`) spawns two separate `git cat-file` subprocesses (`git cat-file -s` and `git cat-file blob`) for every file in `reviews/structured/` (`1,428` files across `714` historical bundles = `2,856` subprocesses), and `source_provenance()` (`lines 679-686`) spawns `git ls-tree` and `git cat-file blob` per `git_commit` input. As `reviews/structured/` grows beyond `720+` review bundles, `scripts/record_review.py check --require-reviews --base main` spends ~35 seconds in subprocess fork/exec overhead.
- **Desired outcome**: Coordinate with upstream `CultureBotAI/culturebotai-claw` to batch object size and content verification through a single persistent `git cat-file --batch` pipe in `assert_append_only()` and `source_provenance()`, reducing `record_review.py check` runtime by >10x.
- **Evidence paths**: `scripts/record_review.py`, `tests/test_record_review_contract.py`, `scripts/check_vendored_sync.py`
- **Priority**: low
- **Dependencies**: Upstream `CultureBotAI/culturebotai-claw` vendored-artifact governance (`scripts/check_vendored_sync.py`), `cmmmech-infra-0001`
- **Issue**: https://github.com/CultureBotAI/CMMMech/issues/805 (`IGRP-C1S6-001`)
- **Status**: `deferred`
- **Disposition**: Deferred in Cycle 1 Stage 6 because `scripts/record_review.py` is a governed vendored artifact enforced by `scripts/check_vendored_sync.py`. Grouped with `cmmmech-infra-0001` under issue `#805` for coordinated upstream implementation in `CultureBotAI/culturebotai-claw` and subsequent vendored sync.

### `cmmmech-infra-0006` — Exclusive-create fallback for `os.link()` in `src/cmmmech/history.py` `cmd_new()`

- **Originating run / cycle / stage**: `mech-goal-sequence-20261019` / cycle `2` / stage `2` (`causal_graphs`)
- **Observation**: During the Cycle 2 Stage 2 corpus-wide causal-graph review and curation across all 631 records (`24` records curated via `scripts/curate_causal_graphs.py`: `10` existing `causal_graphs` records upgraded to use `hydrolyzes`, `solubilizes`, and `dissolves` from `cmmmech-infra-0003` + `14` newly grounded multi-step `causal_graphs` records, raising `causal_graphs` coverage from `63` records / `66` graphs to `77` records / `81` graphs while preserving `412` single-step whole-cell sorption/uptake records without resolved molecular intermediates at the `mechanisms` level and `142` criticality-only records without microbial mechanisms), invoking `scripts/curate_causal_graphs.py` inside the macOS Seatbelt sandbox failed at `src/cmmmech/history.py:288` (`os.link(stream.name, path)`) with `PermissionError: [Errno 1] Operation not permitted`. Because macOS Seatbelt sandboxes block hardlink creation (`os.link`) even within writable workspace directories, `cmmmech new-history` and `scripts/curate_causal_graphs.py` currently require running outside the sandbox.
- **Desired outcome**: Update `cmd_new()` in `src/cmmmech/history.py` during Stage 6 so that when `os.link(stream.name, path)` raises `PermissionError` (or by using `os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)` directly), it atomically writes new history sidecars inside standard Seatbelt sandboxes while preserving the append-only guarantee that existing session files are never overwritten or truncated.
- **Evidence paths**: `src/cmmmech/history.py`, `tests/test_history.py`, `scripts/curate_causal_graphs.py`, `tests/test_curate_causal_graphs.py`
- **Priority**: low
- **Dependencies**: `cmmmech-infra-0004`
- **Issue**: https://github.com/CultureBotAI/CMMMech/issues/822 (`IGRP-C2S6-001`)
- **Status**: `resolved`
- **Disposition**: Resolved in Cycle 2 Stage 6 by updating `cmd_new()` in `src/cmmmech/history.py` to fall back to exclusive file creation (`os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | O_NOFOLLOW, 0o644)`) with `fsync` when `os.link()` raises `PermissionError`, preserving atomic non-overwriting semantics and verified by `test_scaffolder_falls_back_to_exclusive_create_when_hardlink_blocked` in `tests/test_history.py`.

### `cmmmech-infra-0007` — Path-based cleanup fallback for `shutil.rmtree()` in `scripts/render_pages.py`

- **Originating run / cycle / stage**: `mech-goal-sequence-20261019` / cycle `3` / stage `1` (`add_records`)
- **Observation**: During Round 119 (`add_records`), running `.venv/bin/python scripts/render_pages.py` inside the macOS Seatbelt sandbox failed at `scripts/render_pages.py:584` (`shutil.rmtree(args.out)`) with `PermissionError: [Errno 1] Operation not permitted: PosixPath('/Users/marcin/Documents/VIMSS/ontology/Mechs/CMMMech/pages')` because Python 3.13's `shutil._rmtree_safe_fd()` uses `os.unlink(entry.name, dir_fd=topfd)` (`unlinkat`), which Seatbelt blocks inside the standard sandbox even when path-based `Path.unlink()` and `Path.rmdir()` are permitted inside the workspace (`scripts/render_pages.py --check` already succeeds inside the sandbox because it renders into `/tmp`).
- **Desired outcome**: Add a path-based recursive removal fallback (or write/prune files in place without `dir_fd`-based `shutil.rmtree(args.out)`) in `scripts/render_pages.py` during Stage 6 so that `scripts/render_pages.py` runs inside standard macOS Seatbelt sandboxes.
- **Evidence paths**: `scripts/render_pages.py`, `tests/test_render_pages.py`
- **Priority**: low
- **Dependencies**: None
- **Issue**: Pending Stage 6 issue creation
- **Status**: `note`

### `cmmmech-infra-0008` — Extend `scripts/curate_causal_graphs.py` `apply_curation_patch()` for mechanism-level `organisms`, `evidence`, and `observations`

- **Originating run / cycle / stage**: `mech-goal-sequence-20261019` / cycle `3` / stage `2` (`causal_graphs`)
- **Observation**: During the Cycle 3 Stage 2 corpus-wide causal-graph review and curation across all 646 records (`15` records / `17` mechanisms curated via `scripts/curate_causal_graphs.py` — `silver`, `rhodium` [2 mechanisms], `chromite-ore-processing-residue`, `anglesite`, `galena`, `arsenopyrite`, `orpiment`, `realgar`, `bornite`, `djurleite`, `marcasite`, `kesterite`, `stannite`, `electroplating-sludge` [2 mechanisms], and `nickel-flotation-tailings` — raising `causal_graphs` coverage from `89` records / `96` graphs to `104` records / `113` graphs while preserving `178` species/genus-grounded single-step whole-cell sorption/precipitation/bioleaching records without resolved multi-step molecular intermediates in their cited primary sources, `212` ungrounded/consortium/mixed-culture mechanism records without species-level `ncbi_taxon_id`, and `152` criticality-only records without microbial mechanisms), `apply_curation_patch()` in `scripts/curate_causal_graphs.py` (`lines 108-171`) only accepts patch keys `ima_symbol`, `polymorph_or_grade`, `sources`, `mechanism_protein_examples`, and `causal_graphs`. When curating records whose mechanisms require simultaneous `organisms` (e.g., adding species-level `ncbi_taxon_id`), `evidence`, or `observations` updates alongside `causal_graphs`, the writer helper cannot apply those mechanism-level fields in the same atomic `EDIT` history pass.
- **Desired outcome**: Extend `apply_curation_patch()` in `scripts/curate_causal_graphs.py` during Stage 6 to support optional mechanism-ID-keyed patches for `organisms`, `evidence`, and `observations` (with full pre-write `validate_record()` enforcement and `mechanisms` section tracking in `HistoryRecord`).
- **Evidence paths**: `scripts/curate_causal_graphs.py`, `tests/test_curate_causal_graphs.py`
- **Priority**: low
- **Dependencies**: `cmmmech-infra-0004`
- **Issue**: Pending Stage 6 issue creation
- **Status**: `note`

### `cmmmech-infra-0009` — Node-level `protein_examples` upsert and mechanism/node parity enforcement in `scripts/curate_causal_graphs.py`

- **Originating run / cycle / stage**: `mech-goal-sequence-20261019` / cycle `3` / stage `3` (`protein_examples`)
- **Observation**: During the Cycle 3 Stage 3 corpus-wide `protein_examples` review across all `646` records (`104` `causal_graphs` records / `111` graphs with `177` `GROUNDED` `GENE_OR_PROTEIN` nodes and `6` source-limited `UNGROUNDED` `GENE_OR_PROTEIN` nodes across `coal-combustion-residuals.yaml`, `potash.yaml`, and `vanadium-bearing-shale.yaml`; `8` records expanded with `14` live-verified UniProtKB `ProteinExample` entries across `11` `GENE_OR_PROTEIN` nodes and their parent `mechanisms` — `dittmarite`, `glushinskite`, `magnesium`, `phosphorus`, `struvite`, `tetrahedrite-concentrate`, `waste-liquid-crystal-display-panels`, and `traction-battery-hydrometallurgical-residue` — raising total `ProteinExample` instances from `212` to `226` across `57` unique UniProtKB accessions, while preserving `178` single-step species/genus-grounded whole-cell records, `212` ungrounded/consortium records, and `152` criticality-only records as inapplicable / source-limited), `apply_curation_patch()` in `scripts/curate_causal_graphs.py` requires callers to construct both `mechanism_protein_examples` and a full `causal_graphs` copy when appending `protein_examples` to an existing `GENE_OR_PROTEIN` node, rather than supporting a concise `(graph_id, node_id) -> protein_examples` patch that automatically synchronizes `mechanisms[].protein_examples` via `graph.mechanism_ref`.
- **Desired outcome**: Add optional `node_protein_examples` upsert support and automatic `mechanisms[].protein_examples` ↔ `causal_graphs[].nodes[].protein_examples` parity synchronization in `scripts/curate_causal_graphs.py` during Stage 6.
- **Evidence paths**: `scripts/curate_causal_graphs.py`, `tests/test_curate_causal_graphs.py`
- **Priority**: low
- **Dependencies**: `cmmmech-infra-0004`
- **Issue**: Pending Stage 6 issue creation
- **Status**: `note`



