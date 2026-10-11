# Round 16 silicate sources and curation handoff

Prepared 2026-10-11T10:26:09.570127+00:00 by codex / GPT-6 / codex (`/root/round16_silicates`).
Trusted base `b714ce2bd8050d5e19ed9ca072460ba2b8154c3b`, branch `curate/cmm-expansion-round16-20261011`. The three records and
CREATE sessions are working changes; independent scientific reviews are separate acceptance artifacts.

## Selection and identity

Forsterite and talc test a useful substrate contrast in [Cai et al. (2013)](https://doi.org/10.1080/01490451.2012.688924): substantial relative magnesium release versus limited release and a secondary-mineral null. These are two material identities in **one experiment**, not independent replication. [Sheng et al. (2026)](https://doi.org/10.1128/aem.02554-25) provides a separate controlled lizardite assay. These minerals add phase-specific magnesium/silicon coverage without inheriting element-level criticality.

The freshly acquired [IMA September 2026 master list](https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf), including visually inspected rows, identifies forsterite `Mg2(SiO4)` on PDF page 77, talc `Mg3Si4O10(OH)2` on PDF page 211, and lizardite `Mg3Si2O5(OH)4` on PDF page 127. All are grandfathered. Forsterite1824 and lizardite 1956 are original-description years, not approval identifiers; talc's year is `?`. Pages 1-2 explain columns and CC BY-SA 3.0 terms. No invented mineral CURIE is added.

## Evidence and limits actually checked

**Cai 2013:** original 12-page author-posted PDF was opened by the web tool. Methods pp303-304, Tables 1-2, Results pp304-305 and Discussion pp307-308 were read. The selected minus-200-mesh, ten-day comparison uses growing *Aspergillus niger*, initially pH 8.15 at 30 C/150 rpm, after washing/acid-cleaning mineral powders. The paper supplies no collection accession for the fungal strain. Fresh NCBI 5061 XML establishes species scope only. The feed-purity XRD claim is explicitly data-not-shown.

Table 1's final supernatant Mg values are 1.854×10^-2mol/L for forsterite and 3.121×10^-4mol/L for talc. Table 2's abiotic forsterite controls have Mg 1.32/5.09/6.10mM for initial oxalic acid 0/100/200mM. These concentrations remain prose rather than unsupported native mg/kg observations or yields. The forsterite product's published Figure 3a XRD assignment is glushinskite; talc has no recovered secondary mineral at ten days. Acid controls are not culture-trajectory matched, no talc-specific uninoculated trajectory is reported, and Tables 1-2 do not specify replication or uncertainty. No sole oxalate cause, pure-product yield or industrial deployment is inferred.

Local direct PDF/figure downloads returned 403. Web screenshot requests returned only reference text, so **visual Cai figure inspection was not achieved**; the curator checked full-text tables and published analytical interpretations/captions, not diffraction peaks or crystal morphologies. Exact web-extracted receipts are retained outside Git; no PDF checksum is invented. An independent reviewer must retain this limit or obtain the visual figures. A browser inspection attempt reported no available browser. The paper's cover reserves copyright and allows private research; no raw article is committed.

**Sheng 2026:** full EuropePMC XML and the supplemental package were newly downloaded; Figure 2 JPG and the IMA lizardite row were visually inspected. Main methods describe the lizardite assay by reference to the 0.6 g/60 mL dissolution setup with MgSO4 omitted. It uses washed C4-10 cells, triplicates, 37 C/180 rpm and 4-48 h sampling. The 75-150µm feed is chemically characterized, but phase purity is not quantified. Cleaning cites an earlier protocol without restating it. Figure 2A supports higher Mg/Si versus no-bacteria controls from 8 h onward. Figure 2B has a dip then rebound; the text's monotonic wording is not adopted. BHm preparation pH 7.0 and control observations near 7.6 remain distinct.

Supplemental pp1-2 explain mineral-associated cell and siderophore assays. The supplement calls siderophore units below 10% negative, despite some plotted positive-valued results under 10%; no every-timepoint siderophore mechanism is asserted. Gene-expression correlations do not establish necessity and the biotite transcriptome arm has different inoculum volume. The selected record omits those gene-specific causal claims and any intracellular localization claim. Feed phase purity, pH-matched controls and purified-product recovery remain missing.

Fresh [NCBI assembly GCA_039631325.1](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_039631325.1/) confirms strain C4-10, taxon 412384, and BioSample SAMN41260351 from soil. The report describes a contig assembly with Oxford Nanopore/Unicycler, whereas the paper calls its genome complete and describes Illumina/SOAPdenovo. This source-provenance discrepancy is unresolved; no completeness or sequencing-platform claim is curated. Species taxonomy is separately verified through NCBI XML. Article XML states CC BY 4.0; publisher supplemental terms reserve author reuse permissions, so the supplemental PDF also remains outside Git.

## Search and acquisition coverage

The paired [JSON receipt](round16-silicate-sources-20261011.json) preserves exact live queries, first-results/unpaginated bounds, URLs, timestamps, statuses, media types and SHA256 hashes. Raw artifacts live at `/private/tmp/cmm-round16-silicate-raw`. No affecting notice surfaced in the two exact-DOI correction/retraction searches; that is not proof of absence. A retrieved AEM.02554-13 retraction concerns another article and is not attributed to AEM.02554-25.

Before creation, ignored/hidden-inclusive searches covered records/research/reviews and named retained round 14/15 mineral directories, with a follow-symlink search for retained sources. Existing Cai 2013 frontier and IMA mentions were retained. No exact new root was found within that checked pre-creation corpus. An initial nonexistent `/private/tmp/cmm-round15-phosphate-raw` path was explicitly excluded from the successful subsequent search. This is not a machine-wide absence or exhaustive literature claim.

## Validation and handoff

Root reported baseline terminal success before authoring: 308 tests passed, 3 skipped, 122 records and 138 histories. Individual author validation receipts and final record hashes are in the JSON. Final batch/history/review gates and exact-hash independent reviews remain root-coordinated acceptance checks. No schema/validator change was needed for these three records.

- [forsterite](../../data/records/forsterite.yaml); CREATE `history/records/forsterite/2026-10-11T102433Z-codex-ff90a8.yaml`.
- [talc](../../data/records/talc.yaml); CREATE `history/records/talc/2026-10-11T102447Z-codex-d0e525.yaml`.
- [lizardite](../../data/records/lizardite.yaml); CREATE `history/records/lizardite/2026-10-11T102453Z-codex-c8e63a.yaml`.

## Next source priorities

1. **Enstatite/olivine:** Klug et al. 2026, [DOI 10.1038/s41598-026-63817-0](https://www.nature.com/articles/s41598-026-63817-0), PMC13473492, PMID42595772. Primary indexed full text surfaced and bibliographic identity is verified. Acquire figures/supplements; assess direct versus cell-free experiments, mixed-feed mineral proportions and mass-balance assumptions before adding enstatite or extending forsterite. No complete assay review this round.
2. **Biotite grouping:** the Sheng study already supplies full primary evidence, but the root identity needs official group nomenclature rather than a guessed species mapping.
3. **Talc-to-struvite:** [2025 Applied Clay Science lead](https://www.sciencedirect.com/science/article/abs/pii/S0169131725002327) needs full methods and activation/biological controls. Abstract claims are not accepted.
4. **Mixed-culture olivine columns:** [DOI 10.1038/s41529-024-00454-w](https://www.nature.com/articles/s41529-024-00454-w) is an available primary lead needing complete assay and phase-scope review. Different feed, microbes and carbon conditions do not directly refute the selected Cai assay.

These concrete leads demonstrate that discovery remains open. Rechecking the saved raw artifacts is distinct from acquiring an updated remote version.
