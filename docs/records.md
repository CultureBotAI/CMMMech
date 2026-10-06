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
when microbial involvement is explicitly true.

Mechanisms are not universal requirements for all minerals. A broad material
record can exist before any microbial mechanism has been curated. Known labels
and identifiers are checked structurally only; ontology correspondence,
scientific review, canonical curation history, and fleet governance remain
separate adoption work.

The small source in `tests/conftest.py` is entirely synthetic and uses
`example.invalid`; it exercises the contract without introducing a scientific
claim into the curated corpus.
