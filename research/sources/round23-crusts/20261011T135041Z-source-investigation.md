# CMM source investigation: cobalt-rich ferromanganese crust assay extension

## Scope and provenance

- UTC: 2026-10-11T13:50:41.873347+00:00; codex (GPT-6; codex), `round23_crusts`.
- Worktree: `/private/tmp/CMMMech-expansion-round23-20261011`; branch `curate/cmm-expansion-round23-20261011`; base `80899a3d3ea5c0f7c5d54f1b3583e43768e92767`.
- Existing resource: `cmmmech:cobalt-rich-ferromanganese-crusts`; natural hydrogenetic marine crust, not elemental cobalt, a pure mineral or secondary waste.
- Research question: what survives a methods/control/overlap audit of the known Sujith 2017 lead? No criticality designation or new identity is sought.

## Search and acquisition log

The [paired JSON assessment](../../ingests/round23-crusts-sources-20261011.json) contains all 27 exact queries, source URLs, timed direct acquisition attempts, content-type checks and raw-artifact hashes. The [full Markdown assessment](../../ingests/round23-crusts-sources-20261011.md) documents hidden/ignored/symlink-inclusive deduplication, first-result-set bounds, primary full-text passages, failed supplement routes and unavailable visual figures. A 200-response HTML access denial is explicitly distinguished from a PDF. No challenge was bypassed.

## Candidate inventory and source assessments

| Candidate | Inspected scope | Decision |
|---|---|---|
| Sujith 2017, DOI 10.1080/1064119X.2017.1298169 | Full primary text; Methods, Results, Tables 1–3; figure captions only | Narrow Co redistribution claim with explicit partial causal evidence; preserve abiotic Ni advantage and indirect endpoint |
| Companion 2017, DOI 10.1007/s12665-017-6495-y | Publisher identity and primary Methods pp.2,4–5 | Context only: azide warning and distinct sample/pressure/glucose protocol |
| Sujith 2014, DOI 10.1016/j.chemosphere.2013.09.103 | Referenced methods 2.2,2.4,2.5.1–2.5.4 and Table 1 | Dossier-only protocol context; do not transfer Mn assay performance or controls |
| Herrera-Melián 1997, DOI 10.1021/ed074p1444 | Metadata only; full text unavailable | Defer detailed analytical reproduction |
| Sujith thesis | Catalog lead; no chapter acquired | Defer exact overlap audit; do not count an independent experiment |

## Priorities and handoff

The author has extended the existing record using `process: other` to avoid claiming an identified sorption/precipitation route. New EDIT history is `history/records/cobalt-rich-ferromanganese-crusts/2026-10-11T134811Z-codex-cb3d65.yaml`. Named strict validation passed; an independent review and full batch gates remain separate. No new schema or validator behavior was required.

Obtain actual focal plots and Tables S1–S4, then resolve solution endpoints/blank chemistry. Next audit thesis lineage and pressure-study heat-killed controls; finally pursue distinct original crust-bioleaching experiments. No whole-corpus exhaustion claim follows from this bounded investigation.

## Limits and unresolved questions

Cobalt loss is an aqueous difference, not a measured product. Greater apparent Ni sorption in an abiotic arm contradicts universal microbial enhancement. Azide changes control chemistry. Temperature/sign/pH wording is internally inconsistent. Visual figure payloads and SI were unavailable, and no raw experimental table was imported. Copyrighted text stays outside Git; no redistribution rights are inferred from reading access. Details, source locators and retained checksums are in the linked assessment.
