# Tellurium curation dossier

UTC: 2026-10-11T04:01:00Z. Curator: Codex / GPT-6, subordinate curation agent.
Worktree: `/private/tmp/CMMMech-expansion-20261011`; base
`76cd81d310a6ccb4cf7bdebcc61be050d0863222`.
This is a source handoff and curation record, not an independent scientific review.

## Scope and selection

The new element record is `data/records/tellurium.yaml`. The selected primary
study offers accessible methods, controls and solid-phase characterization.
No speculative extraction yield or industrial operation was added. Curation
used `cmmmech-add-record` and `cmmmech-discover-sources`, the local record
contract/schema, validator tests and palladium as a structural example.
The parent ran the batch baseline before curation.

Hidden/ignored and symlink-following duplicate search covered `data`, `research`,
`reviews`, `.claude`, and this task's downloaded text under
`/private/tmp/cmmmech-tellurium-evidence-20261011`. Queries included tellurium,
tellurite, tellurate, CHEBI:30452 and both selected/precursor DOIs. Initially
no record or scientific dossier matched. A concurrent copper discovery log
contained a generic tellurium search term; it is not a duplicate record.
Unrelated home/temp trees were not a source-absence boundary.

## Authoritative identity and criticality

- [ChEBI:30452](https://www.ebi.ac.uk/chebi/CHEBI:30452), label and neutral Te
  identity inspected live. This does not identify tellurite salt or a mineral.
- [NCBI Taxonomy:191292](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=191292&mode=Info),
  species *Rhodococcus aetherivorans* inspected live; includes BCP1. The
  experimental strain name/DSM accession comes from the primary study, not
  a claim that the species ID identifies one strain.
- [Final US2025 list](https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm),
  complete official list and table inspected; tellurium entry on page 50497.
  The notice explicitly distinguishes proposed draft removal from final
  retention. The record adopts only the named final edition.

## Primary evidence and review handoff

[Presentato et al. 2018](https://link.springer.com/article/10.1038/s41598-018-22320-x),
DOI `10.1038/s41598-018-22320-x`, full publisher text inspected on this date.
Read Results, Figures 1-7 captions, Methods and data availability. Record
claims are deliberately limited to Figures 1-3/5 and the methods/controls.
Figure 7 supplies a hypothesis, not an established necessary enzyme pathway.

The [publisher supplement](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41598-018-22320-x/MediaObjects/41598_2018_22320_MOESM1_ESM.doc)
was acquired as a real OLE Word document and text-extracted with `textutil`.
Read supplementary growth/exposure and assay methods, S1 caption, and
tables/remaining captions. S1 plot pixels were not inspected; the no-abiotic-loss
statement is explicitly reported in main-text Results and the tested controls
are specified in the supplement. No graph values were digitized.

Review-critical boundaries in YAML: experimental mass basis differs between
methods and results labels; controls cover the highest loading; no quantitative
biomass loading or analytical limit supports normalization; no product mass
balance supports equating depletion and yield. The file keeps these limits
explicit and does not create `ConcentrationObservation` rows for percentages.

Main publisher license says CC-BY-4.0. Only original summaries and provenance
are committed; the original article/supplement stays outside the repository.
Supplement SHA-256:
`6fb9ea09cca1c9f3ce46e1647b5f8d2de2fbe799d7a610ba08aab2924f675727`.
Acquired during 2026-10-11T03:58-04:00Z; exact local path:
`/private/tmp/cmmmech-tellurium-evidence-20261011/41598_2018_22320_MOESM1_ESM.doc`.
The web tool rejected its binary content type; shell download initially failed
DNS in sandbox and then succeeded with approved network access. The Nature
URL redirected to an inaccessible identity endpoint; the publisher's Springer
full text was readable. PMC routes returned browser checks and Europe PMC
returned an internal fetch error. These are acquisition limits, not absence
of the papers.

## Other evidence assessed and remaining leads

- [Klonowska et al. 2005](https://journals.asm.org/doi/10.1128/AEM.71.9.5607-5609.2005):
  full text inspected, qualitative MR-1 tellurite transformation with limited
  reported conditions. Deferred rather than silently borrowing selenium
  experimental details for tellurium. This is a future additional mechanism,
  not a second element record.
- [Presentato et al. 2016](https://link.springer.com/article/10.1186/s12934-016-0602-8):
  full methods/results inspected as an earlier growing-cell experiment and
  reference for extraction. Not merged with the resting-cell experiment.
- [Valdivia-González et al. 2018](https://link.springer.com/article/10.1007/s00203-017-1438-2):
  abstract reports species dependence and a TeO2 phase; subscription preview
  prevented checking methods. A useful follow-up to challenge indiscriminate
  Te(0) assignments, not a verified refutation of BCP1.
- [Bajaj and Winter 2014](https://pmc.ncbi.nlm.nih.gov/articles/PMC4254260/):
  search-discovered co-exposure work; full text route browser-blocked. Defer
  selenium/tellurium mixed-particle scope until primary details are acquired.
- [2018 paper reference 25](https://pubs.usgs.gov/publication/70029926): anaerobic
  tellurium respiration is a candidate different mechanism. USGS publication
  metadata resolves DOI `10.1128/AEM.02558-06`; no experimental claims were
  imported without a methods assessment.
- A search also surfaced [2026 lithium intercalation work](https://pmc.ncbi.nlm.nih.gov/articles/PMC13315905/).
  It is a lead for the existing lithium record, not another new element.

The exact-DOI correction/retraction search below and inspected publisher pages
did not identify a notice affecting the selected article. This bounded search
does not establish exhaustive correction coverage or literature saturation.

## Search log

Provider: live web search, 2026-10-11 UTC, first returned results only; no
date/domain filters unless encoded in query. No citation-database exhaustive
pagination. Exact queries:

1. `tellurite reduction bacteria elemental tellurium Shewanella oneidensis primary paper PMC`
2. `USGS final 2025 critical minerals list tellurium`
3. `site.ebi.ac.uk chebi tellurium atom`
4. `"Selenite and Tellurite Reduction by Shewanella oneidensis" correction retraction`
5. `"Selenite and Tellurite Reduction" "30"`
6. `"A comparative analysis of tellurite detoxification" full text`
7. `tellurite reduction Shewanella oneidensis MR-1 PMC abiotic 2023 2024`
8. `tellurite reduction bacteria "heat-killed" "PMC"`
9. `"Rhodococcus aetherivorans BCP1 as cell factory" "control"`
10. `"Rhodococcus aetherivorans" "Taxonomy ID"`
11. `"s41598-018-22320-x" correction retraction`
12. `"BCP1" "resting" "Tris" tellurium`
13. `"Formation of tellurium nanocrystals during anaerobic growth"`

Followed publisher reference links from the Shewanella comparative paper to
the 2016 BCP1 work and from there to the 2018 work. DOI/article/access checks
and supplement inspection are described above. Deferred leads remain evidence
of work still possible; they are not saturation proof.

## Curation and validation

Created canonical CREATE sidecar with `just new-history`, actual GPT-6/Codex
metadata; attached it and a distinct inline event before independent review.
The recipe requires preserved inner shell quotes around multiword arguments;
the initial unquoted expansion failed without creating a session. A subsequent
invocation before the target existed also failed safely. The final invocation
created only the linked sidecar. Independent review and whole-batch final
gates are assigned to the parent; targeted validation results follow below.

- `UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked cmmmech validate data/records/tellurium.yaml`: exit 0, one record, zero failed.
- `UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked cmmmech validate-history --base 76cd81d310a6ccb4cf7bdebcc61be050d0863222`: exit 0, 21 history sessions, zero errors at 2026-10-11T04:01-04:02Z.
