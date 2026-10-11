# Third expansion batch: evidence, review and publication preparation

Trusted base: `5892e9a0aca54ef3f45d2ce87a6dcfb80d1569da`.
Worktree: `/private/tmp/CMMMech-expansion-round3-20261011`.
Branch: `curate/cmm-expansion-round3-20261011`.

## Records and evidence boundaries

The add-record workflow selected four elements from the authority inventory
and prior handoffs for accessible primary methods and useful controls. These
records retain the distinction between element identity, experimental salts,
commodity designations, minerals and secondary resources. No mechanism or
criticality is inherited by an uncurated host or waste stream.

| Record | Primary evidence dossier | Accepted boundary |
|---|---|---|
| [Cadmium](../../data/records/cadmium.yaml) | [Sharma2000](round3-cadmium-20261011.md) | CdS-associated laboratory immobilization; sulfide assay is not a cadmium recovery yield; no matched cell-free comparison |
| [Chromium](../../data/records/chromium.yaml) | [Belchik2011](round3-chromium-20261011.md) | MtrC/OmcA contribution with residual mutant activity; precipitate valence inferred; source figure-label conflict preserved |
| [Platinum](../../data/records/platinum.yaml) | [Maes2017](round3-platinum-20261011.md) | CH34-associated transformation under H2; equivalent chemical removal prevents a microbial-necessity claim |
| [Selenium](../../data/records/selenium.yaml) | [Li2014 and Klonowska2005](round3-selenium-20261011.md) | Non-growing MR-1 transformation; conditional mutant effects and different localization observations; supplementary plot rendering remains limited |

Cadmium cites India's June2023 committee list, distinct from the statutory
schedule. Chromium and platinum cite the final US2025 list. Selenium cites
Australia's20February2024 revision. Each mapping, authority, jurisdiction and
edition is explicit in its record. None asserts a timeless designation or
industrial deployment.

Four canonical CREATE sidecars and separate inline events were attached before
review. The existing17 records, histories and reviews were preserved. The schema
already expresses these bounded claims; no schema, validator, dependency,
test behavior or governed artifact changed. Measurements outside the exact
mg/kg observation contract remain qualified prose.

## Adversarial review and acceptance issue

Curators and scientific reviewers were different agents for each record:
the chromium curator reviewed cadmium, the platinum curator reviewed chromium,
the root reviewed platinum, and the cadmium curator reviewed selenium.
Reviewers captured exact target hashes before assessment and independently
inspected primary evidence and authority mappings. Their reports distinguish
live authority checks from reinspection of retained, hashed source artifacts.

[Issue25](https://github.com/CultureBotAI/CMMMech/issues/25) tracks concrete
scientific and publication acceptance. It does not falsely allege that the
prepared records omitted their source caveats. No actionable record defect was
identified in the completed independent reviews. Qualified passing verdicts
retain the source limitations rather than claiming the experiments themselves
have been corrected. Publication receipts link the final four YAML/Markdown
review pairs and their record hashes.

## Validation

- Baseline `just check`:307 passed,3 skipped;17 records and26 histories valid.
- Final scientific batch `just check`:307 passed,3 skipped in56.44s;
  21 records and30 histories valid; exit0.
- `cmmmech validate --require-records`:21 checked,0 failed.
- `cmmmech validate-history --base 5892e9a0aca54ef3f45d2ce87a6dcfb80d1569da`:
  30 checked,0 errors.
- `bash scripts/check_vendored_sync.sh`:22 governed artifacts match public
  CLAW pin `a5d562962c75a2ad9efd8160b548df5944315422`.
- Structured-review validation and exact final-hash coverage are separate
  gates; the final PR receipt records them and the squash/fresh-main checks.

Raw full text, figures and supplementary files remain outside Git. Adjacent
JSON acquisition receipts retain exact URLs, UTC attempts, sizes, hashes,
successes and failures. A challenge HTML response is not accepted as scientific
content. Reading a caption or converted text is not claimed as inspection of
unrendered plot pixels. Source terms remain source-specific.

## Integration and durable provenance

Fleet admission, canonical history and the22 governed artifacts are installed;
this curation does not change integration configuration. Native main-branch
queue publication and required CI are used without bypass. The PR shepherd
remains manual/comment-only. Future integration changes must follow CLAW's
supported admission/synchronization process, not edits to vendored copies.

All new reviews use the trusted main revision above. The older annotated
`review-base/cmm-source-survey-20261009` reference must remain available:
tag object `fc4040c3abcd28f0a9cc52467e308100144ad1fd`, peeled commit
`c0adc2c0763e1515ed07dc712b024974d98fb342`. Distinct review bases are enumerated
and checked before publication. The final PR receipt records queue CI, actual
merge revision, topic-branch deletion and verification in a fresh remote-main
checkout with tags. This preparation document does not preclaim those future
events.

## Remaining priorities

The [fresh frontier snapshot](round3-frontier-20261011.md) reconciles the
historical inventory with current records without rewriting that inventory.
Unrepresented elements, grade-specific commodities, mineral hosts and resources
remain candidates. Further source acquisition is required for platinum's
analytical preparation and alternative sludge mechanisms, detailed selenium
supplement quantification, cadmium alternatives, and additional host/resource
records. Source discovery and record curation are separate acceptance steps.
This batch advances coverage; it does not establish that no new CMMs remain.
