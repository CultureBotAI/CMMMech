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
    status: note
  - task_id: cmmmech-infra-0002
    summary: Add optional MaterialTerm/CriticalMineralRecord metadata slots for IMA mineral symbols and engineered material polymorph/grade identifiers in schema/cmmmech.yaml
    status: note
```
<!-- mech-infra-tasks:end -->

## Tasks

### `cmmmech-infra-0001` — Anchor `scripts/record_review.py` `_directory()` traversal at repository `ROOT`

- **Originating run / cycle / stage**: `mech-goal-sequence-20261019` / cycle `1` / stage `1` (`add_records`)
- **Observation**: `scripts/record_review.py` `_directory()` (`lines 422-436`) opens `/` and traverses every path component downward via `os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=current)` starting at `/Users`. In macOS Seatbelt sandboxes where ancestor directories above the workspace (`/Users`, `/Users/<user>`) disallow `O_RDONLY` directory opens even though the repository root (`/Users/marcin/Documents/VIMSS/ontology/Mechs/CMMMech`) is readable and writable, `python scripts/record_review.py --validate` and `pytest tests/test_record_review_contract.py` fail with `PermissionError: [Errno 1] Operation not permitted: 'Users'`.
- **Desired outcome**: Anchor `_directory()` at `ROOT` (verify `ROOT` is a non-symlink directory, open `ROOT`, and walk only relative components beneath `ROOT` with `O_NOFOLLOW`) so `scripts/record_review.py` and `tests/test_record_review_contract.py` succeed inside standard workspace sandboxes while preserving symlink-traversal protection inside the repository.
- **Evidence paths**: `scripts/record_review.py`, `tests/test_record_review_contract.py`
- **Priority**: medium
- **Dependencies**: None
- **Status**: `note` (pending Stage 6 issue intake)

### `cmmmech-infra-0002` — Optional `CriticalMineralRecord` slots for IMA symbols and polymorph/grade classifications

- **Originating run / cycle / stage**: `mech-goal-sequence-20261019` / cycle `1` / stage `1` (`add_records`)
- **Observation**: During Round 117 (`discover_add`), curating 11 IMA-approved critical-element mineral species (`adamsite-y`, `ammonioborite`, `bainbridgeite-ndce`, `ferrokesterite`, `mckelveyite-y`, `petrukite`, `piilonenite-nd`, `richetite`, `sakuraiite`, `thomasclarkite-y`, `weeksite`) and 3 DOE/USGS/EU synthetic/engineered critical materials (`electrical-steel`, `silicon-carbide`, `synthetic-graphite`) showed that `CriticalMineralRecord` (`schema/cmmmech.yaml`) has `ima_status` and `ima_approval_year` for minerals, but lacks an optional `ima_symbol` slot (e.g., `Ads-Y`, `Abor`, `Bbg-NdCe`, `Fkes`, `Mkv-Y`, `Pet`, `Pii-Nd`, `Rch`, `Sak`, `Tcl-Y`, `Wks`) and lacks a structured polymorph/grade descriptor slot for engineered materials (e.g., `3C-SiC`/`4H-SiC`/`6H-SiC`, `GOES`/`NOES`), requiring those standard identifiers to be placed in `synonyms` or prose `description`.
- **Desired outcome**: Evaluate adding optional backward-compatible `ima_symbol` and material grade/polymorph slots in `schema/cmmmech.yaml` (and surfacing them in `scripts/render_pages.py`) during Stage 6 infrastructure implementation.
- **Evidence paths**: `schema/cmmmech.yaml`, `scripts/render_pages.py`, `reviews/structured/20261019T053000Z-electrical-steel-round117/review.yaml`, `reviews/structured/20261019T053000Z-silicon-carbide-round117/review.yaml`
- **Priority**: low
- **Dependencies**: None
- **Status**: `note` (pending Stage 6 issue intake)

