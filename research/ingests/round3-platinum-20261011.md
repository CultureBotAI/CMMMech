# Platinum curation dossier

Prepared 2026-10-11 UTC by Codex (GPT-6), agent `cmm3_platinum`, in
`/private/tmp/CMMMech-expansion-round3-20261011`, base
`5892e9a0aca54ef3f45d2ce87a6dcfb80d1569da`. This is a research and curation
handoff; the independent scientific review is a separate artifact.

## Selection and identity

Selected [Maes et al. 2017](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0169093),
PLOS ONE 12(1):e0169093, DOI `10.1371/journal.pone.0169093`, PMID `28046131`,
PMC `PMC5207411`. Full text and relevant figures/supplements are accessible,
and the explicit chemical controls, biomass-state comparisons, complex-specific
null results, and XANES/EXAFS permit a defensible, limited claim. Selected one
CH34/Pt(II)/hydrogen experiment rather than merging conditions across organisms
or treating every reported removal as Pt(0) yield.

The article's endpoint does **not** show that microbial activity is necessary:
the cell-free hydrogen arm reaches the same reported Pt(II) removal. The record
therefore says transformation in the presence of microbial biomass, preserving
that counterevidence. The physical association with biomass and authors'
spectroscopic product interpretation are the affirmative observations.

- [ChEBI:33364](https://www.ebi.ac.uk/chebi/CHEBI:33364), directly opened on
  2026-10-11, names **platinum atom**, formula Pt, charge 0, modified
  8 September 2026. It identifies the element, not K2PtCl4 or any mineral.
- [NCBI Taxonomy 266264](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=266264&mode=Info)
  directly opened on 2026-10-11, identifies **Cupriavidus metallidurans CH34**,
  rank no rank, with strain CH34 equivalents. This matches the paper's named
  culture from SCK-CEN; no gene-function inference derives from taxonomy.
- [Final US 2025 list](https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm)
  directly opened and its final table inspected on 2026-10-11. DOI is not
  asserted for this notice. It is the Department of Interior/USGS notice,
  7 November 2025, 90 FR 50494-50497, FR Doc 2025-19813. Platinum is named
  individually. The commodity-to-element mapping is explicit in the record;
  no criticality is inherited by salts, minerals, or waste. This is an edition
  claim, not a claim that no later designation exists.

## Search and deduplication

Web searches on 2026-10-11 used the available web search provider, first returned
result set only, without date filters or pagination:

1. `platinum reduction Shewanella primary platinum nanoparticles XPS abiotic controls PMC`
2. `platinum recovery Desulfovibrio primary hydrogen Pt(IV) Pt(II) X-ray diffraction microbial`
3. `site.ebi.ac.uk/chebi "platinum atom"`
4. `"Reduction of platinum (IV) ions to elemental platinum nanoparticles by anaerobic sludge" correction retraction`
5. `"Biological Recovery of Platinum Complexes from Diluted Aqueous Streams" correction retraction`
6. `"platinum atom" "CHEBI:"`
7. `"platinum" "CHEBI:33364"`
8. `"10.1371/journal.pone.0169093" correction retraction`
9. `"Platinum Recovery from Synthetic Extreme Environments" pdf Maes`
10. `"Cupriavidus" "platinum" "abiotic" "hydrogen" Maes`
11. `"0169093" "correction"`
12. `"0169093" "retraction"`

The exact-title/DOI correction searches returned the original article and related
literature, with no applicable notice identified in these returned sets. Bare
number queries produced irrelevant patent hits and add little coverage. PLOS
full text and Europe PMC XML were inspected; XML metadata states `is-retracted`
`no`. This is a bounded check, not an exhaustive retraction-registry audit.

Local dedup used `rg --no-ignore --hidden` over `data`, `research`, `reviews`,
and `history`, for `platinum|Pt\(IV\)|Pt\(II\)|33364`, and separately exact
`10.1371/journal.pone.0169093|CHEBI:33364|cmmmech:platinum`. Hidden and ignored
files were included. Broad hits were authority candidate inventories and
palladium group context; the exact check found no match before creation.
This boundary and this task's evidence directory were inspected; no
machine-wide absence claim is made. Publisher/PMC/Europe PMC copies are one
study, not independent experiments.

## Primary evidence inspected

Full XML and publisher HTML: all Methods, Results and Discussion, Table 1,
references relevant to omitted analytical preparation, supplement captions and
article metadata. Images were downloaded from actual links in the HTML and
visually inspected: main Figures 1, 3, 5 and Table 1, supplementary Figure S1
and Table S1. TIFF supplements were converted locally with macOS `sips` only
for viewing; the original TIFFs and their hashes remain the source receipts.

| Claim or limit | Exact primary locator and reading |
|---|---|
| Strain and cultivation | Bacterial cultures and growth conditions: CH34 from SCK-CEN, aerobic LB-Lennox overnight at 28 degrees C. |
| Biomass and batch setup | Platinum recovery experiments: 7000 g/7 min harvest, two 25 mL phosphate-buffer washes; buffer 8.5 g/L Na2HPO4.7H2O and 3 g/L KH2PO4; OD610=1; 50 mL in 120 mL bottles; 20 N2/vacuum cycles; 100% hydrogen headspace; 100 mg/L Pt as K2PtCl4 using 2.5 g/L Pt stock in 1 M HCl; initial pH adjusted 1.8-2.2; 28 degrees C, 100 rpm. |
| Pt removal screen | Table 1 CH34/Pt(II) row: 24% no-donor versus 99% H2; chemical reduction H2 row: 99%. n=1, 48 h. Not isolated-metal yield; no error bars/statistical enhancement inferred. |
| Product | Figure 1 CH34 red spectrum and S1 EXAFS/FT panels; authors interpret as consistent with metallic Pt(0). CH34 red and anaerobic Shewanella green spectra differ from the aqueous Pt(II) reference. Figure 3 CH34/Pt(II) panel shows particulate deposits, but cannot establish valence by itself. No new particle-size estimate or spectrum fit was performed. |
| Organism/condition specificity | Pt speciation section cautions that Pt removal and Pt(0) formation differ. Other organisms and Pt(IV) have different spectra. No borrowing of their phase conclusions. |
| Abiotic and inactive controls | Table 1 chemical hydrogen Pt(II)99%. Results additionally report heat-killed Shewanella Pt(II)99% and Pt(IV)13%, slower; those cells are not CH34, and the heat-killing protocol is not provided in inspected text. No matched CH34 killed-cell claim. |
| Biomass viability | Figure 5 CH34 triangle series and membrane-integrity text: counts decline and reach detection level by 27 h. Assay used SYBR Green I/propidium iodide, triplicate sampling/analysis; this does not change Table 1's n=1. No proof that cells remain metabolically active or grow during removal. |
| Complex dependence | Table 1 CH34 under H2: tetraamine preparation0%, carboplatin3%, unlike Pt(II) chloro-complex99%. The tetraamine compound has source nomenclature inconsistencies (bicarbonate starting salt in Methods vs chloride table/Discussion); no exact tetraamine identity is curated. |
| Donor-dependent counterevidence | S1 Table CH34/Pt(II): formate79%, acetate19%; chemical formate control12%; pH7 no-donor sorption18%. These are different donor/pH arms. No extrapolation of H2 phase assignment to the formate arm. S1 Table Pt(IV)/chemical formate95% also warns against generic biological causality. |

### Unresolved source reporting

The XAS Methods names the Pt L3 edge and gives **11919 eV** as the Pt-foil
calibration, while Figure 1's axis lies around **11560-11630 eV**; Results
calls the edge **K-edge**. These inconsistent assignments are preserved as a
limit in the record, without silently repairing the publication. The curated
claim is the authors' qualitative phase interpretation using both XANES and
EXAFS, not a claimed independent absolute-energy or oxidation-fraction fit.
No raw spectral arrays were acquired or refitted.

The 2017 ICP-OES paragraph sends experimental details to Maes et al. 2016,
DOI `10.1021/acs.est.5b05355`. Its publisher page offers purchase, and the
Ghent repository marks its full text UGent-only. Those routes were inspected;
the complete older method was not obtained. Consequently the 2017 reported
removal percentages are retained as the source's operational assay values;
this record does not invent a filter cutoff, centrifugation fraction, digestion,
or an absolute dissolved-versus-colloidal Pt mass balance.

The study did not establish industrial deployment, ore extraction, realistic
mixed-leachate performance for this selected CH34 assay, isolated pure-metal
yield, enzyme necessity, selectivity, repeated biomass reuse or sustained cell
growth. The percentages and mg/L dose do not fit the schema's native mg/kg
source-cell observations and stay in qualified prose.

## Acquisition and reuse

Raw artifacts are outside Git at
`/private/tmp/cmm-round3-platinum-evidence-20261011/`. The companion
`round3-platinum-20261011.json` preserves exact acquisition URLs, actual UTC
attempt times, HTTP outcomes, sizes, SHA256 hashes and local paths.

PLOS main article and its linked supplements are explicitly CC BY 4.0 in the
XML permissions; credit remains Maes et al. 2017. This commit contains authored
factual synthesis and provenance, not raw article copies. Authority pages were
read live via the web tool without a retained byte snapshot; source-specific
redistribution terms were not separately assessed. NIH author-manuscript
redistribution terms are not assumed from accessibility.

Acquisition failures: PMC browser opens returned a reCAPTCHA page for
PMC5207411 and PMC6101971. The first shell acquisition attempt lacked network
resolution; authorized network retry obtained PMC5207411 XML, but Europe PMC
returned HTTP500 for PMC6101971. Web image/supplement clicks failed internally;
ordinary publisher URLs extracted from the accessible HTML succeeded.
ChEBI:33400 was only an unverified lead and failed to open; it is not asserted.

## Deferred sources and next work

1. Simon-Pascual et al., [DOI 10.1002/jctb.5530](https://doi.org/10.1002/jctb.5530),
   PMC6101971: Pt(IV) reduction by anaerobic granular sludge; indexed primary
   text indicates ethanol-specific biological involvement versus substantial
   chemical H2/formate reduction and XRD product evidence. Acquire full Methods,
   Figure 4 and supplement before adding this separate consortium mechanism.
   Online publication is 2017; journal issue is June 2018, not two experiments.
2. Maes et al. 2016, [DOI 10.1021/acs.est.5b05355](https://doi.org/10.1021/acs.est.5b05355):
   prioritize legitimate complete method acquisition to resolve ICP preparation;
   halophilic-culture recovery is another mechanism context, not CH34 evidence.
3. [Recovery of platinum nanoparticles by the anaerobic mixed consortium](https://www.sciencedirect.com/science/article/abs/pii/S221471442401482X)
   is a newer follow-up lead; only indexed abstract-level evidence was seen.
   Do not import its taxonomic or functional-gene claims without primary methods.
4. [Hydrogenase-displaying yeast](https://pmc.ncbi.nlm.nih.gov/articles/PMC5050174/)
   offers a distinct engineering mechanism lead with XPS, but its full
   experimental contract was not inspected in this pass.

No schema or validator behavior change was needed. Parent handles independent
review, batch gates and authorized publication.
