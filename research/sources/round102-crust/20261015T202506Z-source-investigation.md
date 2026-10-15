# Round102 resource-source investigation

UTC: 2026-10-15T20:25:06.647641+00:00. Researcher: Codex (GPT-6; Codex), authoring agent `/root/round100_sulfates`.

Worktree: `/private/tmp/CMMMech-expansion-round102-20261015`. Trusted base: `1c2a3bb043c4bd267a3d911d0e77b029c742689e`. Branch: `curate/cmm-expansion-round102-20261015`. Baseline `just check` passed at 20:20:46Z; its receipt and log hash are in the paired JSON. This assessment supports curation and does not constitute independent acceptance.

## Selection and identity

1. **Uranium mine tailings**: a new secondary-resource owner anchored to DT/RAT solids from water-covered tailings management areas at decommissioned Elliot Lake sites. Keep historic processing details unresolved. Complete primary text and supplementary figures allow unusually explicit contradictory-evidence preservation.
2. **Carbonatite-associated rare-earth ore**: a new primary-resource owner anchored to natural mixed Mushgia Khudag ore. The feed is associated with an alkaline-carbonatite deposit; a modal carbonatite rock definition is not inferred. Separate it from monazite/parisite species, phosphate-rock commodity and secondary residues.
3. **Cobalt-rich ferromanganese crusts**: duplicate of the existing round21/23 owner. No new crust record or history was fabricated.

No resource inherits the criticality of its elements. Criticality lists and economic feasibility were outside this narrow source investigation.

## Search and de-duplication

The paired JSON retains the exact 18 web queries, provider, dates, result-set bounds, acquisition URLs/statuses/times/checksums and raw-output locations. DOI/title correction and retraction queries found no identifiable notice in returned results; Crossref metadata has empty relation objects and no update-to entries. This does not prove no correction exists.

Current records, source reports, ingests, reviews and histories were searched with `rg --no-ignore --hidden --follow`, including ignored files and relevant symlinks. All 261 issue title/body entries in the supplied snapshot were searched; no candidate-DOI or identity hit was returned. Comments were not in that snapshot. Corpus hits concern constituent minerals, an isolate obtained from uranium tailings but assayed in synthetic solution, and a deferred lead; none is an existing whole-feed owner. The raw-source search followed paths in relevant round56/80 dossiers and included transitive historical roots (196 roots, 108 matching lines in 16 files), not all temporary/home files. Hits include bibliography/index references to the tailings original and carbonatite leads; they are not claimed new to every local download. Exact file lists and scopes are retained externally. No applicable ancestral or nested AGENTS.md was found in the scoped worktree/ancestry search; the user's global ignored-file instruction remains applicable.

## Uranium tailings: original evidence and contradictions

[Reynier et al. 2021](https://doi.org/10.3390/min11030302) is a 21-page primary article, with a two-page [supplement](https://mdpi-res.com/d_attachment/minerals/minerals-11-00302/article_deploy/minerals-11-00302-s001.pdf). Both were downloaded from the publisher's public asset service, text-read, rendered and visually checked. Main PDF SHA-256: `1e8f6866e947ca8cc3dd2542a78ff91757bee5881e6e9af14c0edcfe5828c0b4`; supplement: `5f2684076ee1b7b163310ae26c4b333f1203690c375d68be76209186f050d653`.

Sections2.1-2.2 establish June2012 DT/RAT sampling, DT-only inoculum enrichment and laboratory acidic assays. Whole-feed chemistry/mineralogy appears in Tables2-3 and Figure1. The community is unresolved; no strain or genus is invented from the introduction's generic examples. The 3L reactors use added sulfuric acid and differ in initial aeration history. Growth-tube negative controls are not matched abiotic leaching controls. Source-reported REE percentages are solution-based outcomes, not recovered products or isolated microbial increments.

The record retains four substantive ambiguities: (1) methods35days versus flask tables8weeks and stirred-tank30days/week4; (2) page12 RAT prose reverses U/Th relative to Table5; (3) Table7 DT uranium reaches89% while FigureS2c remains around50%; (4) Section2.3 describes composite stirred-tank leachate but page12 refers to collecting flask leachate for recovery studies. No reconciled DT uranium yield is adopted. Both supplement figures show variability; no image-derived exact point values are manufactured.

Section3.5, Tables8-9 and Figures6-8 concern a **separate abiotic resin screen**. Solution-only and resin-water blanks are reported. Percent removal denominators are the contacted composite liquid, not original tailings. The proposed TP272-to-SP112 sequence was not demonstrated as an integrated flowsheet; elution, product purity, regeneration and economics remain open. Bulk sulfur and mineralogical estimates are not silently reconciled into a closed phase balance.

The publisher PDF is CC BY4.0; original files remain outside Git. The PDF's update link contains version2, but no earlier file version was compared.

## Carbonatite-associated ore: original evidence and limits

[Bayarsaikhan et al. 2025](https://doi.org/10.1039/D4RA07845D), RSC Advances15:4628-4635, was fully read through official [PMC XML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11811698/fullTextXML). The official EuropePMC supplementaryFiles endpoint returned the article's figures/equation assets (not an independent study or an experimental supplement). All eight figures, both tables, equation1 and the graphical abstract were inspected. XML SHA-256: `064c31ef89032604702ead40c82be69bea08d4990147e1459e858e8c55d40238`; assets ZIP: `f598fbb8e895f1f9575e39c06703c77fff1f0e9021557c9e80dca4a5cf268414`. Publisher PDFs returned403 and the PMC PDF route returned an HTML challenge despite HTTP200; these files are not described as successfully accessed PDFs.

Exact source locators are Sections2.1.1-2.1.3 (ore, cultures, leaching),2.2.1-2.2.4 (analyses) and3.1-3.3, Tables1-2 and Figures1-8. Ore pretreatment and subsequent sulfuric-acid extraction are separate stages. Figure3 shows weak culture-only extraction and a higher acid-leach signal after Tmix pretreatment. No matched sterile-medium pretreatment isolates microbial activity from medium acidity, iron or sulfate. A complete balance across pretreatment liquid, rinses, residue and acid leachate is unavailable; reported percentages are retained as reported extraction figures, not verified integrated-product yields.

ENA version1 records resolve OR053813.1 to *Thiobacillus denitrificans* strain2mn and OR053804.1 to *Bacillus cereus* strain1mn; current NCBI taxonomy resolves species36861/1396. Partial16S identity and paper attribution do not independently prove mixed-culture purity, exhaustive composition or separate member effects. The separate NBRIP culture's printed `4TH0UUSC016` did not resolve through ENA (HTTP400) or the exact web query; it is not replaced with a plausible-looking accession. Its Gram-negative description remains an identity limitation.

Figure5's initial pretreatment pH differs from the later prose1.6/4.0, so no resolved initial pair is adopted. Organic acids, oxygen uptake, direct contact and cooperative causation were not measured in a way establishing the proposed route. Zeta potential is a filtered-suspension measurement. Acid-consumption reduction, environmental benefit, product recovery and deployment are not established. The article's publication date is11February2025; collection date6February2025 is not substituted. Licensing is CC BY-NC3.0 Unported; no original figures/text are redistributed in the repository.

## Related and deferred sources

The [comparative carbonatite original](https://doi.org/10.63278/1371) was downloaded as a complete13-page publisher-linked manuscript and read with all figures/tables. The landing page's31(3):300-309 bibliographic pagination differs from the manuscript's internal1-13 pages; it is recorded explicitly. The study uses the same investigators, sites and Tmix accessions, while feed composition and loading/particle-size conditions differ. No same-sample join or independent replication is asserted. Its Section3.2 also mixes individual-element ranges and total-REE wording; no numerical efficacy is transferred into the RSC assay. It is retained only as study-family context, with separate future curation possible.

The publisher abstract for the [2016 Mushgia chapter](https://doi.org/10.1016/B978-0-12-802328-0.00025-5) distinguishes apatite veins and carbonatite; the full chapter was not acquired and none of its beneficiation numbers is imported. [10.3390/min11090967](https://doi.org/10.3390/min11090967) is a discovered uranium-tailings Bacillus/remediation lead, not an assessed additional experiment here. Both are follow-up leads, not hidden evidence supporting current measurements.

## Handoff and priorities

Owners: `data/records/uranium-mine-tailings.yaml` and `data/records/carbonatite-associated-rare-earth-ore.yaml`, with canonical CREATE histories. No schema change is needed. The current observation schema is for exact mg/kg concentration cells, so leaching percentages remain qualified prose. An independent reviewer must assess the final frozen owner/history bytes; author curation does not constitute acceptance.

Priorities are original data or formal clarification for the DT uranium and timing conflicts; culture identity, initialpH and interstage mass balances for the Mushgia assay; matched sterile-medium controls for causal attribution; and full assessment of the separately discovered uranium-tailings study. No author contact, complete citation-network audit, paid acquisition or exhaustive worldwide source search was performed.
