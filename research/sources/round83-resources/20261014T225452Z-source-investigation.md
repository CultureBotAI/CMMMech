# CMM source investigation: spent potlining and adjacent aluminium-industry residues

## Scope and provenance

Report saved at 2026-10-14T22:54:52.271802+00:00.

This round assessed a distinct secondary resource beyond the 394-record corpus at `6719e1fc18d122bde9ffa947ff70b6b7266622d3`. Researcher: Codex, GPT-6, agent `/root/round68_new_frontier`. The selected material is exhausted aluminium-cell lining, including mixed graphite/refractory waste; it is not aluminium dross, electrolyte waste, red mud, graphite commodity or a pure mineral. No criticality-list membership or microbial mechanism is inferred. Experimental chemistry is relevant to the requested CMM extraction/recovery scope.

Prior round25/27/60/72/77 dross/frontier reports and round64 waste-electrolyte deferral were checked before new searches. Hidden and ignored files were included and relevant links followed in current `data/records`, `research`, `reviews` and `history`, with normalized DOI and material synonyms rather than slug-only matching. The bounded cited raw roots were round25-frontier-raw, round26-root-raw, round27-root-raw, round60-industrial-research, round64-lithium-research, round72-hydrocerussite-research and round77-resources-research under `/private/tmp`. All existed. Extracted text/JSON and other text-compatible content were searched; unparsed binary payloads and unrelated machine directories were not semantically searched. Receipts in the companion JSON bind exact commands/output hashes. No accepted spent-potlining owner or Robshaw2020 experiment duplicate was found within those bounds. Prior issue #202 expressly distinguishes its unavailable waste-electrolyte feed from potlining; that issue remains unresolved.

## Search and acquisition

All searches occurred on 2026-10-14 using the live web search provider, without date/domain filters unless the exact query contains a site term. Returned result sets were bounded, not an exhaustive bibliographic census. Exact query groups and preserved response paths are recorded in the companion JSON. The first four-query result was inspected but not separately archived; its exact queries are retained. Subsequent searches and source opens are retained locally.

The decisive route was [White Rose Research Online record 157796](https://eprints.whiterose.ac.uk/id/eprint/157796/), which supplied the complete version-of-record article and supporting-information PDF. The browser extraction route timed out for the article and rejected the supplement as over its size limit; direct public repository downloads succeeded. Actual PDF signatures, page counts, text and rendered pages were checked. Acquisition receipt `acquisition-1.json` records URLs, timestamps, content types, sizes and SHA256 hashes. Crossref verifies title/authors/DOI and 2020 publication. Repository posting or metadata-update dates are not treated as a new experimental edition.

## Candidate inventory and decisions

| Candidate/source | Evidence inspected | Decision |
|---|---|---|
| Spent potlining; Robshaw et al. 2020, [10.1007/s12649-020-00954-1](https://doi.org/10.1007/s12649-020-00954-1) | Complete original, 15 article pages plus cover; 18 numbered SI pages plus cover; all main Figures 1–6/Tables 1–5 and SI Figures S1–S35/Tables S1–S5 visually inspected | Ready for qualified abiotic record curation; distinct real waste and meaningful leaching/separation evidence |
| Graphite reuse follow-up, 2022 [10.1016/j.clpl.2022.100004](https://doi.org/10.1016/j.clpl.2022.100004) | Crossref/OpenAlex/DOAJ metadata only; full experiment not acquired | Deferred follow-up within the same resource domain, not a second owner or corroborating experiment |
| Waste aluminium electrolyte, Kordloo2025 [10.1016/j.wasman.2025.115043](https://doi.org/10.1016/j.wasman.2025.115043) | Previously retained round64 metadata/access limits and new targeted repository search | Existing #202 remains open; no repeated unchanged denied endpoint and no abstract-derived mechanism |
| Stainless-steel pickling sludge, Zhang et al. 2022 [10.1016/j.chemosphere.2022.134213](https://doi.org/10.1016/j.chemosphere.2022.134213) | Prior full-text access failure and new exact-title/funder-repository searches | Deferred; complete methods/graphics and exact feed identity still needed |
| Aluminium dross | New microbial/fungal keyword searches plus previous reports | No sufficiently complete primary source selected within this bounded pass; no global absence claim |
| Abiotic waste-aluminium-electrolyte study, [10.3390/met14040460](https://doi.org/10.3390/met14040460) | Search-discovered lead only | Not assessed or used; no expansion beyond the completed potlining source |

One attempted 2022 publisher URL used an unverified guessed PII and returned 403; it is rejected as a route and does not establish access status for the actual original. Crossref subsequently identifies the actual PII as `S2666791622000021`. No claim from that paper is accepted. A future legitimate acquisition should begin from verified metadata and inspect the complete original and SI.

## Accepted source and claim-level assessment

Robshaw, Bonser, Coxhill, Dawson and Ogden (2020), *Development of a Combined Leaching and Ion-Exchange System for Valorisation of Spent Potlining Waste*, Waste and Biomass Valorization 11:5467–5481. The main and SI are one experimental family; the mirror, cover and prior-study diagrams do not provide independent replication.

Actual mixed-cut waste was supplied by Trimet Aluminium, Essen, Germany. Grades A/B/C span refractory-rich through mainly graphitic material; exact cells, age and service histories were not given. Experimental and SI Figure S3 support this source-defined secondary-resource identity without an invented authority ID. The study assayed the less-than-1.18 mm and 1.18–9.51 mm fractions after crushing/sieving. It used chemical reagents and a synthetic chelating resin, with no organisms or biomass. Organism, sequence and criticality authorities are therefore inapplicable to the accepted claims.

**Leaching:** Experimental (repository PDF pages 4–6), main Figures 2–4 and Tables 1–3, SI Figures S5–S28 and Table S1 support sequential alkaline-peroxide/acid mobilization of constituents and altered residual solids at laboratory scale. Three-hour alkaline stages precede the acid stage. The record preserves the 0.5 M acid/3 h method versus Figure 4's 1 M and SI Table S2's 2 h. Main Table 3 is stage-leached mass relative to as-received or partially leached solids, not whole-feed composition; Table S3 is previous literature, not this feed. Increased carbon mass percentage is not carbon recovery. Figure 4 error bars represent electrode measurements, not independent batch replication. Cyanate nondetection after dilution cannot establish cyanide destruction, and residual-solid leachability tests were future work.

**Resin separation:** Main Figures 5–6/Table 5 and SI Figures S4, S33–S35/Table S5 support fluoride breakthrough and Al/F coelution from actual sample-A leachates through a 5.50 mL wet-settled, 1.79 g dry La-MTS9501 bed. Method flow is 1.00 bed volume/h, whereas captions give 0.50; the record does not choose one silently. The displayed elution arm is fine sample A, and the other grades do not inherit its result. Main Experimental defines the reported 59.0% by peak area divided by model-derived theoretical column uptake. It is not original-feed recovery. The eluate contains sodium and other constituents. Main Table 4 is modeled speciation; SI Figure S1's probable binding mechanism references earlier work. Neither is a new direct structural measurement.

**Losses and null limits:** SI Table S4/Figures S29–S32 document precipitation during mixed-leachate preparation. Source-assigned cryolite occurs with amorphous material and is an impurity-bearing loss before the resin. Pure product precipitation, multielement mass closure, independent repeated column campaigns, resin durability and industrial deployment were not demonstrated. No isolated pure cryolite yield or completed detoxification is admitted. Main Table 2 is point EDX rather than bulk purity; its selected percentages are not used quantitatively.

## Source files and reuse

- Main original: `robshaw2020.pdf`, 1,355,413 bytes, SHA256 `db9c50c8994aff7d6feffb3da1c7db0bd2a63ef8bae3ff3564a5a5bdedecb593`. Main article explicitly states CC BY 4.0; the retained repository cover is distinguished from article content.
- Supplement: `robshaw2020-si.pdf`, 25,929,468 bytes, SHA256 `df37acb92894b01da43f854646a234791ac42bba4ca2e1d042e4a5b4a53fa805`. Its repository cover has a rights-reserved notice; this assessment does not automatically extend the main article's license to that artifact.
- Originals, extracted text and all page renders remain outside Git in `/private/tmp/cmm-round83-resources-research`. The companion JSON binds all retained files and original URLs. No bulk redistribution is performed. This is not a reusable bulk dataset or importer.

The exact DOI/title correction, erratum and retraction searches, inspected publisher page and Crossref relation metadata displayed no correction during this bounded check. That does not rule out unindexed or future notices. Crossref has an empty relation object and no update-to entry; its Crossmark-policy URL is not itself proof of a correction.

## Priorities and handoff

1. Curate the single `spent-potlining` secondary-resource owner with distinct abiotic leaching and resin-recovery steps, source-local references and the stated limits. No schema change or native concentration-cell import is needed. A canonical CREATE history and independent exact-state scientific review are required before acceptance.
2. Seek citable clarification of the acid/time/flow conflicts and a complete stage-resolved balance before promoting a transferable recipe or feed-based yield. A bounded issue draft is retained externally; source inconsistency is not a defect in the qualified record.
3. Investigate the verified 2022 follow-up only with complete primary access and feed/experiment lineage checks; do not count it as replication merely because it shares a resource and author group.
4. Keep #202 and other inaccessible microbial leads deferred. New repository/funder searches did not close those primary-evidence gaps. No author contact, purchase or repeated unchanged denial was attempted.

No record scientific acceptance or global validation is implied by this source investigation. Actual owner/history hashes and the named-file validation receipt are added in the companion JSON only after those operations occur; independent peer review and final batch gates remain separately owned artifacts.

Actual curation handoff: `data/records/spent-potlining.yaml` SHA256 `28a700b73213bd244b8d3c3d5a52c74393e5ef6d5e1d77b23863fcbfa05b67b5`; canonical CREATE `history/records/spent-potlining/2026-10-14T225433Z-codex-e675a4.yaml` SHA256 `e8822e5aee64dee6b4019d39c89c202d47ba6c78ef2c3d1e5605e56befd9098d`. Named strict validation passed with one record and zero failures; its actual command/log are bound in the companion JSON. Independent scientific review and batch gates are pending at this report time.
