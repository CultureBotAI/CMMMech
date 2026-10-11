# Chalcopyrite and sphalerite: mineral-host curation

Research and curation on 2026-10-11 UTC in
`/private/tmp/CMMMech-expansion-round4-20261011`, base
`c081a749cd63feafcc25414f5ad006d1f78f1e36`. Actor: codex, GPT-6, codex.
The coordinating agent reported the completed baseline as 307 tests passed,
3 skipped, 21 records and 30 histories valid before these records were written.
This is a source dossier, not the independent scientific review.

## Selection and duplicate boundaries

These mineral species were next in the [round 3 frontier](round3-frontier-20261011.md).
Existing copper and zinc dossiers contain direct concentrate experiments, so
the new records combine verified mineral identity with bounded host-process
evidence. An identity-only treatment would omit supported experimental context.
Neither record inherits criticality from a contained element or commodity.

The search used `rg --no-ignore --hidden -l` on `data`, `research`, `reviews`,
`history`, `.claude` and the three referenced raw directories, with material
names, formula tokens and the three study DOIs. Directory inventory included
hidden and ignored files, and relevant tree paths were checked for symlinks.
Before creation, matches were the existing element records, their dossiers and
reviews, history, and frontier leads; there was no existing mineral root for
either target within these boundaries. This is not an all-filesystem search.

The existing [copper dossier](expansion-copper-20261011.md),
[zinc dossier](round2-zinc-20261011.md), and their independent reviews were
consulted. Their accepted studies are intentionally reused, not counted as new
replications. Fowler and Crundwell 1999 also reuse 1998 data in Figure 10.

## Mineral identity

The [IMA-CNMNC homepage](https://cnmnc.units.it/) was checked live and still linked
the September 2026 master list. A fresh official PDF acquisition matched the
earlier cached SHA-256 `2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973`.
PDF text and rendered pages were inspected; page numbers below are PDF pages,
not invented stable mineral identifiers.

| Record | IMA September 2026 row | Interpretation |
|---|---|---|
| Chalcopyrite | PDF p.40: CuFeS2; G; `1725 ?` | Grandfathered mineral. Preserve uncertainty in original-description year; it is not an approval number. |
| Sphalerite | PDF p.203: ZnS; A; `1980 s.p.` | Approved status and special-procedure entry, not an ordinary sequential approval ID or original discovery date. |

[Master list](https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf)
p.1 defines the columns and `G`, `A`, and `s.p.`. Neither row supplies a
verified external CURIE suitable for the optional identifiers field; no
element, general ZnS-compound, or guessed IMA approval ID is substituted.
Mineral species and experimental impure concentrates remain distinct.

## Chalcopyrite evidence checked

Primary: [Christel et al. 2018](https://doi.org/10.3389/fmicb.2018.03059),
Frontiers in Microbiology 9:3059, PMID 30631311, PMC6315122.
The current publisher full text and fresh Europe PMC XML were read for
Mineral, Bacterial Strains and Growth Conditions, Bioleaching Experiments,
Bioleaching of Chalcopyrite Concentrate, and the conclusions. Figures 1 and 2
were visually inspected from publisher image assets.

- Aitik concentrate: 29.5% Cu; the main Methods call it greater than 98% pure
  on digestion/elemental analysis and mention accompanying bornite at the
  deposit. This is a reported assessment, not independent phase quantitation.
- The record retains the EDTA/NaOH and acetone preparation, size fraction,
  heating, living DSM strains, medium/pH, 2% w/v loading, temperature/shaking,
  four flasks per treatment and all culture combinations plus controls.
- Each species contributes the same inoculum, giving mixtures different total
  starting cell loads. Different oxidation-onset times produce different
  elapsed endpoints. The reported pair-versus-control copper values are not
  a common-time rate or purified-product yield.
- Heated HCl slurry digestion counts dissolved and precipitated released
  copper. No quantitative phase-specific chalcopyrite conversion is inferred.
- The triple mixture underperformed the pairs; the A. caldus-only late
  oxidation may involve surviving environmental contaminants. Repeated pair
  assays reached 593 +/- 15 mV, preventing a universal 550 mV ceiling claim.
- Passivation, chalcocite intermediacy, attachment and genes are interpretations,
  not demonstrated molecular causation. The source calls for scale-up testing.

Species-level NCBI records [33059](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=33059&mode=Info),
[28034](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=28034&mode=Info),
and [178606](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=178606&mode=Info)
were opened and their names, rank, and listed DSM 8584/9293/14647 type strains
checked. Species IDs do not silently become strain accessions.

The publisher supplementary anchor returned the main article; the previous
PMC supplementary-file attempt yielded HTML. A new Europe PMC
`PMC6315122/supplementaryFiles` attempt timed out. No supplement-only numbers,
gene measurements or phase fractions are imported. The retained composition
claims are explicitly those in the main Methods; full supplement inspection
and independent concentrate phase quantitation remain open.

## Sphalerite evidence checked

Primary: [Fowler and Crundwell 1999](https://doi.org/10.1128/AEM.65.12.5285-5292.1999),
PMID 10583978, PMC91718; and
[Fowler and Crundwell 1998](https://doi.org/10.1128/AEM.64.10.3570-3575.1998),
PMID 9758769, PMC106466. Both publisher full texts were read for Methods,
Results and Discussion. The 1999 Figures 2, 3, 5 and 6, and freshly acquired
1998 Figures 4-6, were inspected visually. The 1999 model sections and
Figures 8-10 captions were read; fits were not recomputed from raw data.

- Gamsberg feed was reported as 98% sphalerite by XRD, 53.3% Zn and 7.84% Fe,
  with S, Mn and Pb also quantified. Authors interpret Fe as solid solution;
  no pure ideal-ZnS reagent is asserted. The size cut and 0.5 M sodium-sulfide
  wash materially scope these observations.
- Both studies used living FC1, a stirred/aerated 2 L cell, 5 g/L concentrate,
  10% v/v inoculum, pH 1.6, 35 +/- 0.1 degrees C and 5.9 mg/L oxygen.
  Electrolytic regulation held bulk iron chemistry comparable in inoculated
  and microscopy-checked chemical runs. This apparatus is an experimental
  control device, not evidence for commercial electrorecovery.
- The 1999 elevated-ferrous comparisons diverge after an initially similar
  interval; SEM/EDAX at 100 h and 69 h are separate, later endpoints. Surface
  observations and kinetic models support sulfur-layer removal without
  demonstrating a named enzyme, sulfur mass balance or isolated zinc yield.
- The 1999 1 g/L Fe(II) series visibly departs from equal dissolution despite
  the Discussion's sharp low-ferrous null boundary. The record retains that
  tension and does not assert a universal threshold.
- The 1998 fixed-1-g/L-Fe(II), variable-Fe(III) results are the directly
  relevant null comparator. Figure 3's current caption disagrees with the
  Methods on iron conditions; no current-based numerical claim is curated.
- Ten analytical replicates measure assay precision, not ten independent
  reactors. Biological replication and effect uncertainty remain unresolved.

[NCBITaxon:920](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=920&mode=Info)
currently maps the species name Acidithiobacillus ferrooxidans and lists
Thiobacillus ferrooxidans as a homotypic synonym. This is not a modern genomic
reassignment or a verified strain accession for FC1.

## Bounded correction and counterevidence search

Searches on 2026-10-11 used each exact DOI plus `correction OR erratum OR
retraction`, then `"chalcopyrite" "Sulfobacillus" "Leptospirillum" contrary
redox 2026` and `"sphalerite" "Fowler" "Crundwell" sulfur layer direct
mechanism contrary`. Publisher and PubMed records were checked. Returned
results did not identify a correction/retraction of these exact targets;
this bounded search is not proof none exists. The 1998 null and the source
figure/prose tensions above are preserved rather than erased.

Additional search hits included a primary 2004 diffusion/reaction study
(ScienceDirect PII S0304386X03002743), a natural iron-containing sphalerite
light-effect study (PII S0892687520305227), and a 2022 mechanism review
(DOI 10.1007/s00253-022-12168-7). These are leads only: their full experimental
methods were not reviewed here and no numerical result or purported refutation
from them is accepted. The earlier copper dossier's 2026 Rios lead likewise
remains separate from the evidence used in these records.

## Acquisition and terms

The companion [JSON manifest](round4-mineral-hosts-20261011.json) contains
fresh download receipts, cached-asset reinspection hashes, exact routes,
inspection coverage and failures. Raw primary material remains outside Git in
`/private/tmp/cmm-round4-mineral-hosts-20261011/`, with existing reused assets in
`/private/tmp/cmm-expansion-copper-20261011/` and
`/private/tmp/cmm-round2-zinc-20261011/`. Web-only inspections are explicitly
separate from downloaded artifacts; a failed route is not successful acquisition.

IMA PDF p.2 states CC BY-SA 3.0; Christel 2018 states CC BY. ASM pages carry
copyright/request-permissions notices, with no open redistribution license
established here. The repository contains authored evidence summaries and
provenance, not redistributed full texts or figures. NCBI Taxonomy is used
to resolve identifiers, not as a substitute for the experimental paper.

## Curation handoff

New roots are [chalcopyrite](../../data/records/chalcopyrite.yaml) and
[sphalerite](../../data/records/sphalerite.yaml). Each has an actual CREATE
sidecar and a separate inline event. No schema or validator change was needed;
concentration and assay values stay qualified prose, outside the restricted
mg/kg source-cell observation contract. Independent scientific review and
coordinating-agent final batch gates must cover the final record bytes.
