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
is separate from validation; canonical curation history and fleet governance
remain pending adoption work.

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
to each new or materially changed record. Save separate timestamped Markdown
rounds under `reviews/records/<slug>/`; never overwrite earlier rounds. Each
review identifies the record, UTC time, HEAD plus working changes and record
SHA-256, scope, checked evidence, severity-ranked findings, corrections,
unresolved questions and verdict. Later substantive edits require a new round.
These reviews are local scientific artifacts, not CLAW canonical history.

Run individual validation during curation, then `just check` and
`uv run --locked cmmmech validate --require-records` for the batch. `just check`
uses the nonempty-corpus gate; direct validation without the flag still supports
an explicitly empty exploratory directory. Preserve synthetic tests separately.

The small source in `tests/conftest.py` is entirely synthetic and uses
`example.invalid`; it exercises the contract without introducing a scientific
claim into the curated corpus.
