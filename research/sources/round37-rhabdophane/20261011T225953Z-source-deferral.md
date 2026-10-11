# Rhabdophane candidate: source-only deferral

UTC: 2026-10-11T22:59:53Z

Investigator: Codex (GPT-6), agent `/root/round27_packaging`; model `GPT-6`, harness `codex`.
Worktree: `/private/tmp/CMMMech-expansion-round37-20261011`. Trusted base: `dcfbedb78bfd682ad06f2ff4517241f490e4f401`.
This is a source-discovery handoff, not a scientific acceptance review. No rhabdophane record or history event is created.

## Decision

**Defer the proposed mineral owner from this source.** [Voutsinos et al. (2024), BMC Biology 22:41](https://doi.org/10.1186/s12915-024-01841-0), PMCID PMC10875860, establishes a useful association between granite weathering, secondary rare-earth phosphate grains and metagenomic potential. It does not establish a precise rhabdophane species, measured hydration or a controlled causal microbial dissolution mechanism for these grains. A generic group record would not repair the missing structural assignment. Preserve this investigation without inflating mineral identity or transferring an elemental criticality designation.

## Evidence acquired and actually inspected

The complete 19-page published article was acquired from the [University of Glasgow repository](https://eprints.gla.ac.uk/320514/2/320514.pdf); full JATS and PMC/publisher HTML were also read. All eight original main figures and original Table 1 were visually inspected. The four original supplementary files were acquired both through the publisher's displayed links and through the EuropePMC supplementary ZIP. All seven pages of Additional file 3 (Figures S1–S9) were visually inspected. All seven workbook sheets were parsed; every mineral-chemistry row in Table S7 and the relevant whole-rock Table S4 rows/units were inspected. The genomic workbook was inventoried, not independently reassembled or statistically reproduced. FASTTREE and sequence-alignment files were acquired for provenance, not used to validate sequence phylogenies.

Raw originals, rendered pages and derived text remain under `/private/tmp/cmm-round37-rhabdophane-research/raw`. The exact URL/access UTC/status/content type/size/SHA-256 receipts are `acquisition1.json` through `acquisition5.json`. Initial PMC PDF and `/bin` downloads returned short HTML pages despite HTTP200; those files are retained as failed content acquisitions, not claimed as PDFs or spreadsheets. The valid 19-page PDF is `primary-glasgow.pdf`; valid workbook and SI PDF names start `publisher-12915_2024_1841_MOESM`. The EuropePMC ZIP contains 22 members, including the same four supplements and original figure/table images.

## Identity and dominant-element assessment

The fresh [IMA-CNMNC September 2026 master](https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf) has exactly the same SHA-256 as the retained authority PDF used in previous rounds. Its original page 184 was visually inspected: rhabdophane-(Ce), -(La), -(Nd) and -(Y) have ideal formulas Ce/La/Nd/Y(PO4)·H2O. Their statuses are Rn, Rn, Rn and A respectively; only the Y row supplies approval 2011-031. The historical special-procedure dates on the renamed species are not newly minted identifiers. No species/group CURIE is asserted here.

The article names rhabdophane in Background and Discussion, including an interpretive discussion of secondary phosphate formation. Results and Figure 6 label the observed particles as secondary lanthanide phosphates/REE-P. Methods use carbon-coated, cleaved biotite grains, SEM at 10 kV and standardless semiquantitative EDX with predicted error at least 10%. They supply no XRD, electron-diffraction or hydration determination for these grains. Crystal habit plus REE and P presence cannot by themselves distinguish every relevant phosphate phase or establish H2O stoichiometry.

Table S7 further prevents one dominant-element identity being imposed on the whole sample:

| Original spot label | Reported rare-earth wt% | Interpretation boundary |
|---|---|---|
| `ei9 sp10` | La 15.75; Ce 34.37 | Ce exceeds measured La; Figure 6a caption instead says `ei19 sp10`. Resolve the spot-label discrepancy before an exact image–chemistry join. |
| `ei11 sp12` | La 13.14; Ce 21.14; Nd 9.81 | Ce is the largest of these measured REE. |
| `ei29 sp47` | La 16.78; Ce 8.38; Nd 14.99 | La and Nd are close relative to stated semiquantitative uncertainty; abundant Si/Al/Fe/Ca warns against treating the spot as a pure REE-phosphate analysis. |
| `ei 33 sp 25` | La 7.80; Nd 6.90; no Ce row | The table does not establish Ce absence; C/O and host-associated elements contribute substantially. |

These are reported normalized spot wt%, not mole fractions, phase purities, recovery yields or dissolved concentrations. The first two groups include atomic-percent columns; later groups instead have standard-label/factory-standard columns. The workbook's 'Standard Label' entries do not override the Methods description of standardless quantification. No Nd/La/Ce-specific species assignment is accepted from these rows.

## Assays, controls and inference boundaries

Samples are natural I-type Burrumbeep granodiorite and associated soil near Rocky Point Bushland Reserve, Ararat, Victoria, Australia. Five initial geochemical samples and, six months later, nine biological samples from the same profile are described. These are spatial weathering comparisons, not a time-course leaching experiment. At least 50 biotite grains per sample and 0–30 secondary REE/P grains per sample were examined. Whole-rock material underwent strong-acid digestion for ICP-MS; the measured concentrations are total bulk composition, not soluble REE release or mass-balanced product recovery.

Genome-resolved metagenomics recovered 136 non-redundant bins with estimated completeness >70% and contamination <10%; a 120-genome subset met the separate ribosomal-tree inclusion criterion. Predicted XoxF systems, transporters and biosynthetic clusters suggest possible lanthanide utilization. No identified isolate/strain was challenged with an independently established rhabdophane phase in this study. No sterile, killed-cell, matched-pH, spent-medium or metabolite-addition comparator establishes microbial contribution to grain dissolution. Neither gene presence nor transporter co-location establishes expression, ligand production or mineral dissolution. The authors explicitly call for experimental characterization. No industrial deployment, isolated REE product, extraction efficiency or criticality claim is supported by this assessment.

## Source discrepancies and contrary constraints retained

- Figure 6a versus S7 spot ID differs (`ei19` versus `ei9`).
- The Results density definition places 2.1 g/cm3 in the moderately weathered category, but the mineral discussion calls RPR1 at 2.1 lightly weathered. S7 of the figure supplement labels RPR1 as 2.1 without resolving that category conflict.
- Reported bulk values 427/264/214/80 ppm concern whole-rock samples. The S4 analytical columns are labeled ppb and need explicit conversion; they are not fluid-assay observations. The author statement 'total lanthanide' should be reconciled with inclusion/exclusion of Y before any quantified reuse.
- Methods use antiSMASH 5.0 while the main Figure 7 caption states 6.0; this is a software-version inconsistency, not evidence that a particular predicted metabolite was experimentally produced.
- Results report 1231 rpS3 groups whereas Methods report 1230 after filtering/clustering. Do not turn these into validated taxon inventories without reconciliation.
- The Discussion's phosphate claim points to Supplementary Table 3, which is the XoxF sequence sheet; elemental chemistry is Table S4. This misplaced locator is preserved as a source issue.
- Alternative explanations remain: abiotic weathering, mineral redistribution and organisms exploiting released nutrients cannot be separated from active microbial solubilization here. No negative-controlled microbial effect has been measured.

## Deduplication and identifiers

Before the decision, `rg --hidden --no-ignore --follow` searched current worktree and original checkout `data/records`, `research`, `reviews` and `history` for rhabdophane, PMC10875860 and the normalized DOI suffix. Hidden and ignored files and symlinked paths were included in these bounded trees. Results are retained in `/private/tmp/cmm-round37-rhabdophane-research/dedup-main-original.txt`. No rhabdophane owner file was identified in that bounded search, but the study was already a round36 frontier lead; it is not a newly discovered publication.

The existing [neodymium record](../../../data/records/neodymium.yaml) describes Marecos et al. 2025 DOI10.1038/s42003-025-08061-4 and synthetic Mon2, a monazite-Nd/rhabdophane-Nd mixture. That is a different experiment and cannot become pure rhabdophane leaching evidence. Its referenced raw HTML/text/workbook and the earlier source-skill trial were inventoried with SHA-256 and searched irrespective of ignore status; exact scope is `/private/tmp/cmm-round37-rhabdophane-research/dedup-referenced-raw.json`. XLSX byte-search is not asserted as a cell-level absence test; existing maintained analysis supplied its experimental identity. These checks are not machine-wide novelty claims.

The issuing [NCBI BioProject numeric-ID page](https://www.ncbi.nlm.nih.gov/bioproject/1065000), inspected through the live web tool, identifies accession PRJNA1065000 as the weathered-granite metagenomic project. The separately retained `bioproject.html` from the accession-route urllib request is only a generic BioProject page and did not itself verify that accession. The exact access clarification is retained in `/private/tmp/cmm-round37-rhabdophane-research/bioproject-web-verification.json`. This accession is a study/data collection, not a mineral or taxon ID. No individual organism external ID was asserted from MAG labels.

## Notices, further sources and next actions

Fresh Crossref works metadata identifies the exact title/DOI and contains an empty relation object with no update-to field. Bounded web queries `"10.1186/s12915-024-01841-0" correction retraction` and `"Weathered granites and soils harbour" correction retraction` returned the article and related records without a verified formal notice. This is not an exhaustive notice audit and does not resolve the internal discrepancies above.

A broader bounded search returned [Kang et al. 2022, DOI10.1007/s00253-021-11721-0](https://pmc.ncbi.nlm.nih.gov/articles/PMC8763747/), already represented by the cerium/phosphorus/struvite evidence chain. It should be rechecked for exact Ce-phosphate crystal identity before proposing a species owner, not counted as a new experiment. Another actionable lead is Jiang et al. (2010), *Biological nano-mineralization of Ce phosphate by Saccharomyces cerevisiae*, Chemical Geology 277:61–69, identified through the cited literature. Its complete primary evidence and identifiers were not acquired in this round and no result is accepted from the secondary citation. Prioritize that original study's diffraction, hydration and killed-cell/abiotic controls in a future bounded acquisition. Existing meta-autunite issue120 blocked routes were not retried.

Next decision requires phase-specific structural and compositional evidence linked to a tested material, then explicit separation of microbial production/ligand effects from abiotic precipitation. For the 2024 grains, contact the authors or locate existing diffraction/hydration measurements and resolve exact SEM spot labels. Do not create an identity-only species record solely to increase the corpus count.

## Handoff and validation

Source-only scope requires no record/history validation and changes no schema or existing scientific record. Parent fresh baseline receipt `/private/tmp/cmm-round37-baseline-terminal.json` reports 308 passed, 3 skipped and 200 records/231 histories valid; this investigator did not rerun that suite. This dossier is ready for publication review as a deferral; it does not claim independent acceptance of a record.

Raw manifest: `/private/tmp/cmm-round37-rhabdophane-research/raw-manifest.json`, SHA-256 `f6f0c5d5edd1ca5be612e790ca756f02cb9c8444a02effbd0d27f2bac013a258`. All bulk source bytes remain outside Git.
