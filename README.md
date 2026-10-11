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
| [Copper](data/records/copper.yaml) | Defined acidophile cultures leach chalcopyrite concentrate | Consortium-dependent release assay includes dissolved and precipitated copper |
| [Nickel](data/records/nickel.yaml) | *Acidithiobacillus thiooxidans* mixture leaches selected laterites | Matched-pH controls and ore-dependent null outcomes limit generalization |
| [Tellurium](data/records/tellurium.yaml) | Resting *Rhodococcus aetherivorans* BCP1 transforms tellurite to nanorods | Partial high-dose depletion and phase evidence do not establish isolated yield |
| [Zinc](data/records/zinc.yaml) | Controlled *Acidithiobacillus ferrooxidans* FC1 sphalerite leaching | Matched-chemistry null results and source figure/text tension limit generalization |
| [Silver](data/records/silver.yaml) | *Shewanella oneidensis* MR-1 forms XRD-identified Ag(0) | Abiotic salt precipitation, feed ambiguity and toxicity constrain the laboratory result |
| [Gallium](data/records/gallium.yaml) | *Acidithiobacillus thiooxidans* sludge leaching | Acid dissolution dominates; microbial enhancement remains provisional |
| [Arsenic](data/records/arsenic.yaml) | Co-mobilization in the same gallium-sludge experiment | Similar abiotic leaching; no demonstrated arsenic redox reaction or microbial advantage |
| [Cadmium](data/records/cadmium.yaml) | Cd-1 culture-associated cadmium-sulfide formation | Spectroscopy and sulfide assay support immobilization, without a matched cell-free comparison or isolated yield |
| [Chromium](data/records/chromium.yaml) | MR-1 MtrC/OmcA contribution to chromate transformation | Residual mutant activity, inferred precipitate valence and incomplete conversion remain explicit |
| [Platinum](data/records/platinum.yaml) | Hydrogen-driven transformation with CH34 biomass | Equivalent chemical-control removal prevents claiming microbial necessity |
| [Selenium](data/records/selenium.yaml) | Non-growing MR-1 selenite transformation | Conditional mutant involvement and different localization reports limit universal pathway claims |
| [Spent lamp phosphor](data/records/fluorescent-lamp-phosphor.yaml) | *Gluconobacter* biolixiviant bioleaching of a secondary resource | Retorted mixed powder; total-REE outcome, not an element-specific yield |
| [Cobaltite](data/records/cobaltite.yaml) | IMA September 2026 mineral identity | Distinct from cobalt; no inherited criticality or microbial mechanism |
| [Monazite-(Nd)](data/records/monazite-nd.yaml) | IMA September 2026 mineral identity | Distinct from neodymium and synthetic mixed experimental feeds |

Experimental salts, alloys, mineral species and secondary resources retain
their distinct identities. Criticality entries identify a jurisdiction and
edition; none assert timeless status or industrial process deployment. See the
[initial pilot assessment](docs/pilot-session.md),
[first ingest queue](research/ingests/20261009-priorities.md),
[earlier ingest results](research/ingests/20261009T054507Z-followup.md),
[expansion inventory and priorities](research/sources/expansion-authorities/20261011T040103Z.md),
[second expansion review](research/ingests/round2-20261011-publication.md),
[third expansion reviews and remaining priorities](research/ingests/round3-20261011-publication.md), and
[current structured record reviews](reviews/structured/).
Earlier [Markdown reviews](reviews/records/) remain historical evidence.

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

The locked development dependencies include `just`; use `uv run just check`
if it is not otherwise on your PATH. CI runs `uv run python scripts/check.py`,
including the recipe argument-forwarding regressions. This local gate uses no
research provider, model, credential, or network
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

Use [cmmmech-add-record](.claude/skills/cmmmech-add-record/SKILL.md) to turn
primary evidence or a source-discovery handoff into curated records, curation
history and saved scientific reviews.

Use the local [record-review skill](.claude/skills/review-record/SKILL.md) for
new or changed scientific records. Review artifacts identify the reviewed
commit and working changes, hash the record bytes, and retain unresolved limits.
New rounds use the [structured review contract](docs/record-reviews.md).
Before publishing through the squash queue, preserve the inspected source
revisions using the [publication procedure](docs/record-review-profile.md#publishing-through-the-squash-queue).

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
