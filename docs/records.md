# Record Contract

The authoritative schema is `src/cmmmech/schema/cmmmech.yaml`. The validator
generates a closed JSON Schema from it, then checks source links and identifiers.
It never dereferences URLs or resolves ontology identifiers.

Required record fields are `id`, `name`, `material_kind`, `description`, and a
nonempty `sources` list. IDs use `cmmmech:<lowercase-slug>`. Every source has a
record-local ID, title, HTTPS/HTTP URL, and access date. Quote dates in YAML.
Sources establish provenance; they do not imply that an agent has verified
the publication or that every claim in it is correct.

Optional criticality entries each require jurisdiction, list name, edition,
classification (`critical`, `strategic`, `not_listed`, or `unknown`), and a
`source_ref` matching a source in that record. Omission means unrecorded, not
not critical. A `not_listed` claim requires inspecting the relevant complete list.

Optional mechanisms each need a stable local ID, name, process, description,
context, explicit `microbial` boolean, and nonempty evidence. Evidence names a
source, support direction, and what claim the source bears on. Context records
the material form/substrate and relevant experimental conditions or limitations.
Organisms are optional named entities with a CURIE and label; do not invent a
species identifier for an unresolved community. An organism list is only valid
when microbial involvement is explicitly true. This includes inactive biomass
of microbial origin used for biosorption; `microbial: true` does not assert
growth or metabolism. State living/resting/dried biomass and strain in context.

Mechanisms are not universal requirements for all minerals. A broad material
record can exist before any microbial mechanism has been curated. Known labels
and identifiers are checked structurally only. Human or agent evidence review
is separate from validation. Optional `curation_history` is a nonempty list of
inline events, each requiring `timestamp`, `curator`, `action`, and `summary`.
Quote timestamps as timezone-bearing RFC 3339 strings with a year from 2000
through 2099; malformed dates, missing fields, blank descriptions, and unknown
event fields fail strict validation. Record actual work, never fabricated or
retrospectively invented provenance. Inline events do not replace scientific
reviews or claim adoption of CLAW's separate sidecar-history authoring contract.
The optional `history_refs` list separately links canonical sidecar sessions;
it never changes the shape or meaning of inline `curation_history` events.

## Curation and review

Ground the record's `material_kind` before assigning identifiers. An element
identifier does not identify its ions, host mineral, alloy, commodity stream,
or waste feedstock. Keep those experimental forms explicit in context. For a
criticality list that groups materials or uses commodity names, document how
the listed scope maps to the record; never silently broaden the designation.

For each mechanism, cite the primary experiment and locate supporting methods,
figures or tables in evidence explanations. Include relevant pretreatment,
organism resolution, conditions, controls, outcome and scale. Distinguish
measured from fitted values, dissolved-metal removal from an isolated product,
and observations from a proposed molecular cause. Source contradictions may
be retained as a second `partial` evidence entry explaining the narrower claim.
Do not manufacture a `refute` entry merely to populate every evidence type.

Apply [.claude/skills/review-record/SKILL.md](../.claude/skills/review-record/SKILL.md)
to each new or materially changed record. New rounds use the shared schema and
saver in [record-reviews.md](record-reviews.md), with native scientific rules
retained by [record-review-profile.md](record-review-profile.md). Save one
timestamped YAML/Markdown bundle per record and reviewed state under
`reviews/structured/`; old `reviews/records/` artifacts remain historical.
Record actual times, reviewer independence, Git base plus reviewed byte hashes,
scope, inspected evidence, normalized findings and proposed acceptance checks.
Later substantive edits require a new observation, not changes to a prior report.
These reviews are scientific observations, not canonical curation history or
proof that a proposed correction was performed.

## Append-only curation history

The domain schema imports the governed `mech_shared.yaml` and `history.yaml`
modules from `src/cmmmech/schema/`. Their bytes are managed by CLAW's supported
governance release and synchronization process; do not edit the copies locally.

Create a canonical `HistoryRecord` sidecar with `just new-history`:

```sh
just new-history --slug cobalt --actor-type ai_agent --actor-name codex \
  --model '<actual-model>' --agent-tool codex --event EDIT --outcome changed \
  --summary 'Describe the actual change' --details 'Evidence, checks, and limitations.' \
  --issue 3
```

Supply the actual actor and model; the example's model placeholder must be
replaced. The adapter stamps the current UTC time and creates a collision-safe
file under `history/records/<slug>/`. It requires finished details and refuses
to overwrite an existing session. It does **not** modify the scientific record.
Append the printed repository-relative path to the record's `history_refs`
list as a separate reviewed edit, then validate the record and the history:

```sh
just validate-history
uv run --locked cmmmech validate data/records/cobalt.yaml
```

History presence is advisory; when present, every reference must resolve to a
closed-schema-valid sidecar whose target path and slug identify the exact
record. Sidecar validation also checks session filenames, real UTC timestamps,
actor metadata, complete event details, and all nested fields. Do not backdate
events or infer the actor of earlier work. A migration event describes the
present migration and links earlier review snapshots without claiming to have
performed those reviews.

History files and every directory beneath `history/` must be real repository
paths, without symlinks. Both reading and scaffolding reject aliases, including
links to locations inside the same repository. Discovery rejects linked
subdirectories instead of silently skipping their sessions. Otherwise Git's
append-only comparison could inspect the unchanged link while the backing
history bytes were modified elsewhere.

History sessions are immutable after commit. Correct a previous session by
creating another that identifies the original session and explains the correction.
`just check` compares history with `HEAD` locally; CI sets
`CMMMECH_HISTORY_BASE` to its PR, merge-group, or push base. The explicit
`cmmmech validate-history --base <revision>` form verifies the same append-only
rule against any available reviewed revision. Unknown or unfetched revisions
fail the check. Standalone history validation with neither `--base` nor
`CMMMECH_HISTORY_BASE` checks content and linkage layout, not Git immutability
or whether a historical target still exists. With a base, every **new** sidecar
must identify an existing target file; an imported session cannot silently
introduce a nonexistent target.
Already reviewed immutable sessions may outlive a removed or renamed target.
This distinction preserves the historical audit trail without requiring edits
to old sessions. Unattached sidecars are allowed during the documented
scaffold-then-attach workflow; this does not make history coverage mandatory.


Run individual validation during curation, then `just check` and
`uv run --locked cmmmech validate --require-records` for the batch. `just check`
uses the nonempty-corpus gate; direct validation without the flag still supports
an explicitly empty exploratory directory. Preserve synthetic tests separately.

The small source in `tests/conftest.py` is entirely synthetic and uses
`example.invalid`; it exercises the contract without introducing a scientific
claim into the curated corpus.
