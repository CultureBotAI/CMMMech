# CMMMech

An evidence-backed knowledge base for **critical minerals and materials**, with
**microbial extraction, transformation, and recovery mechanisms** alongside
their wider resource and material context.

The knowledge base provides a LinkML schema, an offline strict validator,
tests, CI, and a growing reviewed corpus. Each record has a
timestamped scientific review; synthetic test fixtures remain separate.

| Material record | Curated evidence | Evidence boundary |
|---|---|---|
| [Cobalt](data/records/cobalt.yaml) | Acidophilic consortium bioleaching of spent-battery black mass | Laboratory solubilization, not isolated cobalt product |
| [Neodymium](data/records/neodymium.yaml) | Algal biosorption and *Gluconobacter* biolixiviant bioleaching | Separate magnet-leachate and synthetic mixed-phosphate experiments |
| [Palladium](data/records/palladium.yaml) | Resting *Desulfovibrio desulfuricans* cells reduce Pd(II) | Defined soluble salt assay; hydrogenase causality remains inferred |
| [Manganese](data/records/manganese.yaml) | *Pseudomonas putida* GB-1 oxidation of Mn substrates | Laboratory oxide-equivalent assay, without crystalline phase identification |
| [Lithium](data/records/lithium.yaml) | Conditional acidophile bioleaching of jadarite-bearing material | Transient advantage; controls converge and other feeds show null effects |
| [Uranium](data/records/uranium.yaml) | Laboratory bioelectrochemical observations | Inoculated-cell observations do not isolate microbial enhancement |
| [Vanadium](data/records/vanadium.yaml) | Laboratory bioelectrochemical observations | Inoculated-cell observations do not establish a purified product |
| [Spent lamp phosphor](data/records/fluorescent-lamp-phosphor.yaml) | *Gluconobacter* biolixiviant bioleaching of a secondary resource | Retorted mixed powder; total-REE outcome, not an element-specific yield |
| [Cobaltite](data/records/cobaltite.yaml) | IMA September 2026 mineral identity | Distinct from cobalt; no inherited criticality or microbial mechanism |
| [Monazite-(Nd)](data/records/monazite-nd.yaml) | IMA September 2026 mineral identity | Distinct from neodymium and synthetic mixed experimental feeds |

Experimental salts, alloys, mineral species and secondary resources retain
their distinct identities. Criticality entries identify a jurisdiction and
edition; none assert timeless status or industrial process deployment. See the
[initial pilot assessment](docs/pilot-session.md),
[first ingest queue](research/ingests/20261009-priorities.md),
[latest ingest results and priorities](research/ingests/20261009T054507Z-followup.md), and
[record reviews](reviews/records/).

The U/V mechanisms include eight reviewed, source-linked concentration cells.
The [observation contract](docs/records.md#quantitative-source-observations)
keeps measured values, detection limits, sample dates and analysis dates distinct.

## Scope

- Distinguish elements, mineral species, mineral groups, commodities, and
  secondary resources rather than treating those as synonyms.
- Record criticality by jurisdiction, list name, and edition, with a source.
  There is no universal or timeless `is_critical` flag.
- Represent mechanisms such as bioleaching, biosorption, biomineralization,
  redox transformation, separation, recovery, and recycling.
- Mark microbial involvement explicitly; connect identified organisms and
  experimental context to evidence for the particular mechanism.
- Preserve uncertainty and evidence that supports, partially supports, or
  contradicts a mechanism. Validation is not scientific verification.

## Local Checks

```bash
uv sync --extra dev --locked
just check
uv run cmmmech validate
uv run cmmmech validate path/to/record.yaml
uv run cmmmech validate --require-records
```

Without `just`, use `uv run python scripts/check.py`. The same command is used
by CI. This local gate uses no research provider, model, credential, or network
lookup after dependencies are installed. CI also runs the separate canonical
artifact check, which reads the pinned public CLAW revision:

```bash
bash scripts/check_vendored_sync.sh
```

Each record belongs in `data/records/<slug>.yaml`. See
[the record guide](docs/records.md) and the packaged
[LinkML schema](src/cmmmech/schema/cmmmech.yaml). Validation rejects unknown
fields, duplicate YAML keys, malformed references, dangling source references,
and duplicate record identifiers. An empty corpus is reported explicitly;
`--require-records` makes it an error. The shared local/CI gate now uses this
flag so accidental loss of the whole corpus fails `just check`.

Use the local [record-review skill](.claude/skills/review-record/SKILL.md) for
new or changed scientific records. Review artifacts identify the reviewed
commit and working changes, hash the record bytes, and retain unresolved limits.

## Sources

Use the local [source-discovery skill](.claude/skills/cmmmech-discover-sources/SKILL.md)
to investigate CMM data sources, reassess known sources, or identify coverage gaps.
It produces a dated search log, source assessment and ranked curation handoff under
`research/sources/`, keeping discovery leads separate from verified evidence.

Criticality is a designation made by a named authority at a particular time.
Useful discovery sources include the [USGS critical-minerals programme](https://www.usgs.gov/programs/mineral-resources-program/science/about-2025-list-critical-minerals)
and the [EU critical raw materials overview](https://www.consilium.europa.eu/en/policies/the-critical-raw-materials-act/).
These are entry points, not imported datasets or an endorsement of a frozen list.
Curate microbial mechanisms from the underlying research, preserving organism,
substrate, conditions, and the distinction between laboratory results and field
or industrial deployment.

## Integration Status

CLAW [fleet admission](https://github.com/CultureBotAI/culturebotai-claw/pull/581)
registers CMMMech with its measured native capabilities. The 22 applicable
governed artifacts are pinned in `scripts/.vendored_canon_ref`; CI verifies
their bytes and file modes against that immutable public CLAW revision. Use
CLAW's supported synchronizer for updates, never hand-edit governed copies.

The native schema keeps inline `curation_history` events separate from
`history_refs`, which link canonical sidecar sessions. `just new-history` creates
a validated sidecar without rewriting a scientific record; attach its printed
path in a reviewed edit. Both canonical timestamp guards remain unchanged.
History paths reject symlinks, and CI compares committed sessions with the
trusted event base to prevent rewriting or deleting earlier provenance. See
[the history guide](docs/records.md#append-only-curation-history).

The native merge queue is configured for `main` through CLAW's reviewed
plan/apply/check process. Its [receipts and readiness evidence](reviews/integration/queue-20261008/)
distinguish configuration, writer App token readiness, and actual queue execution.
The PR shepherd remains manual and comment-only; its configuration and available
secret names were checked without invoking its model. Other unverified fleet
adapters remain disabled. No research provider is invoked by the native or
canonical-byte validation gates.

The included CI handles pull requests, pushes to `main`, and `merge_group`
events. Operational merge evidence is tracked in [issue #3](https://github.com/CultureBotAI/CMMMech/issues/3).
The [dated integration audit](docs/integration-status.md) records the earlier
pre-admission state, not the current deployment. Coordinated fleet convergence
is tracked in [CLAW issue #580](https://github.com/CultureBotAI/culturebotai-claw/issues/580).

## License

Project-authored code and schemas use BSD-3-Clause. Project-authored data and
narrative documentation use CC-BY-4.0. Third-party materials retain their own
terms. See [LICENSE](LICENSE), [LICENSE-CODE](LICENSE-CODE), and
[LICENSE-DATA](LICENSE-DATA).
