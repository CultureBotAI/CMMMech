# CMM source investigation: distinct uranium-vanadate mineral owners

## Scope and provenance

- Saved UTC: 2026-10-14T04:42:30.642731+00:00; researcher/curator: codex, GPT-6, codex tool.
- Worktree: `/private/tmp/CMMMech-expansion-round62-20261014`; branch `curate/cmm-expansion-round62-20261014`; trusted base `11a0b0f8e2714f1863304faf408da4ce0e7c5b53`.
- Scope: new mineral owners with primary microbial context, beginning with brucite, greenockite and carnotite-group phases. No jurisdictional criticality claim was sought or inherited. No experimental mineral is treated as an element, a commodity or a secondary resource.
- Three new records and their actual CREATE history were authored in this round after the root agent's successful baseline. Other concurrent work is outside this source assessment. This report is a curation handoff, not an independent scientific review or acceptance decision.
- Dedupe included hidden and ignored files and followed symlinks: `data`, `research`, `reviews`, `history`; text extensions md/json/yaml/yml/txt and an 8 MB per-file bound. It then searched 372 existing `/private/tmp/cmm*` raw roots cited by that metadata, including HTML/XML; 117 cited roots were missing. Full commands, boundaries, roots and matches are in the JSON manifest. Unextracted binary semantics and unrelated home directories were excluded.
- Repository matches were incidental brucite in `data/records/reverse-osmosis-concentrate.yaml` and deferred greenockite context in `research/sources/round47-indium-minerals/20261012T052552Z-source-investigation.md`. Raw matches were inspected as bounded context; none of the four candidate DOIs matched the searched prior raw text. No accepted owner for these three species was found within this scope. This is not a global literature-exhaustion claim.

## Search and acquisition log

The companion JSON contains all 25 exact web queries, the first returned result-set scope (no pagination or date/domain filters), every direct acquisition URL, start/end UTC, HTTP status, redirect, content type, file path and SHA-256. Individual web-query timestamps were not captured; those searches occurred on 2026-10-14 UTC before this report. Direct-download receipts carry individual timestamps. Indexed text was used to choose acquisition routes, not to verify inaccessible figures.

| Source | Actual inspected acquisition | Decision |
|---|---|---|
| [Glasauer et al. 2022](https://doi.org/10.1016/j.chemgeo.2022.120726) | Complete [KIT postprint](https://publikationen.bibliothek.kit.edu/1000146758/149004078), 15 PDF pages including cover; all pages and original Figures 1-7 and Appendices A-D visually inspected; text read | Curate three distinct identities and bounded phase-occurrence context; omit species-specific mechanisms |
| [LBNL manuscript](https://escholarship.org/content/qt0wq788dk/qt0wq788dk.pdf) | Complete 44-page file acquired; relevant text inspected and original Figures 1-3 on PDF pages 38-40 visually compared | Same study/version corroboration, not independent evidence; confirms Figure 2 hours label |
| [IMA September 2026 list](https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf) | Fresh 244-page official PDF; definition page 1 and species pages 31, 38, 78, 86 and 142 visually inspected; fresh [issuing homepage](https://cnmnc.units.it/) links this edition | Current identity authority; no numbered IMA accession invented for grandfathered species |
| [Tesson et al. 2008](https://doi.org/10.1016/j.marchem.2007.12.005) | Indexed author text and matching HAL/OpenAlex metadata; HAL has `openAccess_bool:false` and no file URL; ResearchGate HTTP 403 | Defer brucite microbial claim pending original complete text and figures |
| [Moon et al. 2013](https://doi.org/10.1007/s10295-013-1321-3) | OUP PDF route HTTP 403; Springer PDF route redirects to HTML article/paywall; OSTI metadata-only record 1098173; OpenAlex has no usable institutional PDF | Defer greenockite/hawleyite phase attribution pending original diffraction and methods |
| [Ye and Jing 2022](https://doi.org/10.7185/geochemlet.2215) | Original main+SI PDF acquired, 22 pages; relevant text inspected, original figures not visually assessed | Reject as direct greenockite experiment: greenockite belongs to the Cd thermodynamic model, not the measured Sb experiment |

The retained `greenockite-thermo.pdf` is HTTP-403 HTML and `greenockite-springer.pdf` is HTML despite their filenames. `greenockite-osti-api.json` is XML. Brucite Crossref returned HTTP 429 with no body. Those artifacts are not represented as complete primary PDFs.

## Ready source assessment: Glasauer et al. (2022)

Crossref, the KIT repository and the primary title/author page agree on Susan Glasauer, Sirine C. Fakra, Sarah Schooling, Peter Weidler, Tolek Tyliszczak and David K. Shuh, *The transformation of U(VI) and V(V) in carnotite group minerals during dissimilatory respiration by a metal reducing bacterium*, *Chemical Geology* 591, 120726, DOI `10.1016/j.chemgeo.2022.120726`. The publication is from 2022; KIT's repository posting is 2023 and does not change the study year. KIT's repository DOI `10.5445/IR/1000146758` identifies the repository object, not a second experiment.

### Identity and field choice

| Owner | September 2026 IMA row | Direct experimental phase context | Curation boundary |
|---|---|---|---|
| Carnotite | PDF p.38, K2(UO2)2(VO4)2·3H2O, G, 1899 | K-carnotite identified in final mixed fine fraction | No assertion that bacteria were necessary or that a unique precursor was established |
| Metatyuyamunite | PDF p.142, Ca(UO2)2(VO4)2·3H2O, G, 1954 | Starting and final mixed fractions both contain assigned metatyuyamunite | Detection is not surviving mass, unchanged crystals or a phase-specific reduction rate |
| Fritzscheite | PDF p.78, Mn2+(UO2)2(VO4)2·4H2O, G, 1865 | Starting phase assigned; not detected in final bulk diffraction | Nondetection is not complete dissolution, elemental removal or an extraction yield |

G means grandfathered; these years are original descriptions, not numbered mineral approvals. The accepted names are distinct species. The study's initial ore is a natural mixed sandstone, not three separately purified feeds. The three owners therefore share **one experiment**, and their optional mechanism fields are deliberately absent. Experimental occurrence belongs in a qualified description until mineral-specific causation can be supported.

### Organism, substrate, conditions and original evidence

Section 2.1 identifies unprocessed uranium-ore stockpile material from southeastern Utah, with yellow uranyl-vanadate coatings on sandstone. The XRD/EDS fine fraction was separated by water agitation/sonication, decanting, centrifugation and drying; fine-fraction concentration comparisons cannot be substituted for whole-feed mass balances. Figure 1b and sections 3.1/3.3 identify initial metatyuyamunite plus fritzscheite and final K-carnotite plus metatyuyamunite. At the final stage fritzscheite was not detected, while fine-fraction Mn/Ba concentrations remained relatively unchanged. The text says biotransformation appeared to cease by ten months; the final fine fraction is compared at that interval.

Section 2.2.1 uses live *Shewanella putrefaciens* CN32: 1.6 g mixed CGM sandstone in 80 mL defined medium, 10 mM sodium lactate and 1 mM phosphate as Na2HPO4. Bottles were nitrogen-degassed, sealed and autoclaved before inoculation, then retained in a 3% H2/97% Ar glovebox; initial density was around 10^8 cfu/mL inferred by protein assay. Treatments were triplicate. A reaction pH and separate ore-incubation temperature were not established from the supplied methods; the room-temperature statements in separate oxic toxicity/biofilm assays were not imported. The complete medium recipe is cited to prior work rather than independently reconstructed here.

Fresh NCBI efetch XML for taxon 319224 resolves *Shewanella putrefaciens* CN-32 with strain rank. This is a naming map, not inoculum authentication. The records assert no organism CURIE because they contain no organism field; the source's strain name remains in the qualified study description.

Figure 2 uses open diamonds for inoculated and filled diamonds for bacteria-free controls. The ore arm shows substantially more V mobilization with culture, with low U in solution. Figure 4 and associated STXM/NEXAFS support partial reduction of V(V) to V(IV) with U predominantly U(VI). V(V) persists. Ten-month V(III) assignments remain qualified because beam-induced reduction of wet material cannot be ruled out; a cited related study did not find V(III) in bulk solution. No gene, inhibitor or isolated-enzyme experiment establishes a unique electron-transfer route. The separate 1 mM soluble uranyl/vanadate assay (Figure 6) exhibits U reduction and must not be substituted for the ore results. Figure 7 is a separate oxic biofilm assay.

Section 4.1 expressly says the two starting minerals' behavior could not be observed separately. Section 4.2 and the conclusion identify biotic V redox changes together with abiotic interlayer-cation exchange favored by medium composition. The material was not chemically pure. No matched final abiotic XRD series, phase-specific mass balance, killed-cell control or pH/cation-matched precipitation comparison isolates carnotite formation as microbial necessity. Bacteria-free solution controls do not close those phase-attribution gaps. Neither industrial deployment nor isolated-product recovery is demonstrated.

### Contradictions and narrower claims retained

1. Section 3.2 places a V plateau at 120 **days**, while original Figure 2 axes in both KIT and LBNL files say **hours**. No exact kinetic endpoint is curated.
2. The discussion/conclusion describe U as undetected or not liberated, while Figure 2b has small positive solution values and section 3.2 describes low U. The records say **low**, not zero or never detected; local U(IV) below detection is not excluded.
3. Section 3.2 names tyuyamunite-to-carnotite conversion; the conclusion names fritzscheite-to-K-carnotite. Initial XRD assignment uses metatyuyamunite. A unique precursor-to-product pathway is not selected.
4. The paper writes fritzscheite with one H2O, unlike four H2O in the current IMA formula. Canonical identity and reported-feed specification remain separate; no hydration correction is silently imposed on the historical sample.
5. Figure 3 and Appendix B have questionable micrometre scale labels for bacterial images. No derived particle/cell dimensions are curated from those captions.
6. Abstract versus results contain inconsistent mM/M biofilm-concentration notation. Those separate biofilm endpoints are excluded.
7. Autunite-like material and V-oxide particles have microscopy/spectroscopy interpretations but no bulk XRD confirmation in this paper. They do not create new confirmed mineral owners here.

Exact DOI/title correction, retraction and erratum searches were bounded to returned first result sets. No affecting notice was identified there; Crossref's fetched record contains no `update-to` notice and an empty `relation` object. This is not an exhaustive assurance against later or unindexed corrections. The retained contradictions themselves are adverse evidence, not erased to produce a clean mechanistic narrative.

### Access, license and retained originals

The KIT PDF identifies itself as a postprint/reviewed manuscript and carries a CC BY-NC-ND notice. The retained originals remain outside Git; no redistributability is inferred for the IMA PDF, publisher sources or the other manuscript. This repository receives paraphrased assessments and provenance, not bulk copyrighted full text or images. The IMA list is a PDF authority table, not a numerical experimental dataset. The paper supplies graphical data and a fine-fraction table rather than an archived raw instrument dataset; no raw-XRD/STXM accession was established during this bounded inspection. No quantitative-observation import is attempted.

## Local curation and checks

Created `data/records/carnotite.yaml`, `data/records/metatyuyamunite.yaml` and `data/records/fritzscheite.yaml`, each with actual inline CREATE provenance and a `just new-history --event CREATE` sidecar. All actor metadata are codex / GPT-6 / codex. Exact record/history hashes and named command receipts are in the manifest. Each named `uv run --locked cmmmech validate data/records/<slug>.yaml` returned **1 checked, 0 failed**. The first history command failed on the sandbox-denied default uv cache before writing a sidecar; rerunning offline with a writable task cache succeeded. The failed and successful receipts are retained.

The root baseline receipt at `/private/tmp/cmm-round62-baseline.json` records `just check` exit 0 at the trusted base; its log reports 317 tests passed and 3 skipped. These are baseline results, not final-batch or independent-review results. Final corpus/history/review gates and independently saved scientific reviews remain the root workflow's responsibility after this handoff.

## Priorities and unresolved questions

1. Independently review the three final owner bytes against the retained primary and IMA originals. Require explicit resolution if a phase-specific mechanism is later proposed; do not fill the empty mechanism fields from the shared-ore redox result.
2. Obtain mineral-resolved controls, raw phase data or author clarification for the hours/days, precursor and fritzscheite hydration discrepancies before deriving kinetics or phase-specific transformations.
3. Obtain the complete original brucite diatom study, including diffraction/figures and controls, through a legitimate publisher or institutional route. HAL/OpenAlex metadata and indexed text do not close that gap.
4. Obtain Moon et al. (2013) complete main/supporting material to distinguish greenockite and hawleyite fractions and synthetic CdS conditions. Current metadata-only/blocked routes do not justify a mineral mechanism record.
5. Other manganese-carbonate candidates were not systematically searched after the stronger uranium-vanadate source emerged. No claim of exhaustive mineral coverage is made.
