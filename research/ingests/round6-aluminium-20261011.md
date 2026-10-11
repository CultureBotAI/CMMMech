# Aluminium curation dossier — 2026-10-11 UTC

Record: `data/records/aluminium.yaml`. Curator: codex / GPT-6 / codex.
Worktree: `/private/tmp/CMMMech-expansion-round6-20261011`, branch
`curate/cmm-expansion-round6-20261011`, trusted base
`d09a5611767d94fd196393b31d44cb8cf6657f7f`.

The selected primary study is [Urik et al. (2015), DOI
10.1016/j.jinorgbio.2015.08.022](https://doi.org/10.1016/j.jinorgbio.2015.08.022).
It provides a complete laboratory protocol, no-fungus controls, ICP-OES quality
control and a useful synthetic-acid comparison. It supports an aluminium element
record while leaving the mixed red-mud substrate distinct from the element,
bauxite and alumina. This is a curation dossier, not an independent review.

## Acquisition and identity

The complete primary paper was read in Attachment E of the author's 2017
habilitation thesis, hosted by [Brno University of Technology](https://www.vut.cz/uredni-deska/habilitace?action=priloha&priloha=226417).
PDF pages 80–85 reproduce journal pages 154–159. The 186-page file is retained
outside Git at `/private/tmp/cmm-round6-aluminium-evidence/urik-habilitation.pdf`:
15,760,716 bytes, SHA-256
`1ad163bac045935f00a43d67208749ea3b2091d6fb4d0d3efedabf831f637d84`.
Text was extracted with the isolated PyMuPDF environment; rendered pages 83–84
were visually inspected for Figures 3–9. System Poppler was unavailable; no
environment installation or shared dependency change was made.

The article states copyright 2015 Elsevier Inc., all rights reserved. Public
reading access through an author thesis is not a redistribution license. No
full text or figure is committed. Crossref metadata lists TDM terms, which are
not treated as a general redistribution grant.

Live [ChEBI](https://www.ebi.ac.uk/chebi/CHEBI:28984) resolves CHEBI:28984 to
aluminium atom (Al, charge zero). Live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=5061&retmode=xml)
resolves 5061 to *Aspergillus niger*, species. This anchors the published species
assignment; it does not independently verify strain G-10. [The original final
US 2025 notice](https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm)
contains the Aluminum row. Only that dated designation is curated; there is no
latest-list claim or inheritance by every aluminium-containing material.

The [machine-readable dossier](round6-aluminium-20261011.json) retains exact
queries, source URLs, acquired-file hashes, local paths and access failures.
The first web opening of the thesis failed because its 15.8-MB response was too
large; curl then acquired and validated the actual PDF. Python urllib authority
fetches failed DNS resolution; subsequent curl requests succeeded and their
payloads were inspected. Source files and failed-attempt receipts stay outside
Git; no successful HTTP response was accepted without checking content.

## Search and duplication boundary

`rg --no-ignore --hidden` searched `data/records`, `research`, `reviews` and
`history` for aluminium/aluminum, bauxite, red mud, CHEBI:28984 and the selected
DOI/title. Ignored and hidden files were included. Aluminium was a known frontier
candidate and a reagent in existing gallium/sludge experiments, but no aluminium
element record or reference to this experiment was present before this addition.

Cited acquisition directories were also checked: `/private/tmp/cmm-next-eu`,
`cmm-expansion-authorities-20261011`, `cmm-source-authority-acquisition`,
`cmm-source-datasets-downloads`, `cmm-source-discovery-downloads` and
`cmmmech-source-skill-trial`. No relevant symlinks were present in these or the
four repository search trees. This is a bounded local finding, not a machine-wide
or exhaustive literature novelty claim.

Web searches on 2026-10-11 used aluminium/aluminum with fungal bioleaching,
biosorption, red mud, full text, primary titles and correction/retraction terms.
Only first returned results were examined; no date/domain filters or pagination
were applied. Exact queries appear in JSON. The DOI-specific correction search
found no correction or retraction notice; acquired Crossref metadata has no
`update-to` and an empty `relation`. This does not replace a complete Crossmark
or retraction audit.

## Evidence locators and constraints

| Claim | Primary-paper locator | Curation boundary |
|---|---|---|
| G-10 identity and growing culture | Sections 2.1 and 3.5, journal pp.154–155,158 | Morphology and 612-bp ITS with 99% similarity underpin the authors' species assignment; no strain-specific NCBI ID asserted. |
| Ajka red-mud preparation and loading | Sections 2.2–2.3, p.155 | October 2010 sample, dried, disaggregated, <0.2 mm; 0.2 g in 45 mL broth + 5 mL spores, 250-mL flask. |
| Filter-passing Al result | Sections 2.3,2.5,3.3; Figure 3 | Approximately 141 mg/L at seven days, static 25 C, triplicates. ICP-OES of 0.45-um filtrate; no free-ion speciation or isolated product. |
| No-fungus control | Section 2.3 | Undetected/below detection, without a numerical Al detection limit; not converted to zero. |
| Mixed mineral identity | Table 1 and Section 3.1 | Total Al 6.97% of dry feed; XRD does not resolve Al-host phases. Generic boehmite/sodalite discussion is not experimental phase identification. |
| Acids and pH | Section 3.4, Figure 7a | Final pH 2.3, oxalic 16.0 and citric 28.6 mmol/L support extracellular chemistry; no exclusive physiological acidification cause assigned. |
| Synthetic-acid countercomparison | Sections 2.4,3.4, Figure 8 | Mixture B about 142 mg/L, matching the day-five acid profile, sodium salts/HCl pH adjustment, two-day extraction. Different time and medium prevent a rate or strict superiority comparison with seven-day fungal cultures. |

Additional source tensions remain outside the chosen assay: Figure 5a and
Figure 6 use a 40-g/L label whereas Methods and Figure 5b use 50 g/L. The record
therefore does not curate those higher-loading outcomes. The source's discussion
of ATP-driven proton pumps, glucose oxidase and organic-acid complexation is
not converted into experimentally proven molecular causality for G-10.

Three alternative leads were assessed but not used: [Shah et al. (2020)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7688833/)
was available in full text, but mixed 1%/5% loading descriptions and its high
recovery claims need a separate audit; [Boeris et al. (2016)](https://doi.org/10.1016/j.jbiotec.2016.07.026)
and [the four-strain fungal removal paper](https://pubmed.ncbi.nlm.nih.gov/30406393/)
remained abstract/section-snippet leads in this pass. Their numerical claims
are not transferred into the record.

## Authorship and checks

Parent confirmed the pre-change `just check` baseline passed before record
creation. `just new-history` created the actual CREATE sidecar
`history/records/aluminium/2026-10-11T053805Z-codex-7b51f9.yaml`; a distinct current
UTC inline event and its `history_refs` link were attached before review hashing.

`UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked cmmmech
validate data/records/aluminium.yaml` passed: **1 checked, 0 failed**.
Independent scientific review and final batch/history/review gates are assigned
by the parent and remain separate from this curation receipt.
