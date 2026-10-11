# Schwertmannite primary-source investigation

UTC: 2026-10-11T21:47:56Z

Revision: `f83cf867a38c470b4347f721d9ea9370c3019eaf` with the new schwertmannite record/history and this dossier as working changes. Curator: codex (GPT-6; codex). This is an author handoff, not independent scientific approval.

## Decision and scope

Accept `data/records/schwertmannite.yaml` as a mineral species record, grounded in the current IMA list and Song, Liu and Wang (2018), DOI [10.3390/ma11091739](https://doi.org/10.3390/ma11091739). The complete 13-page publisher PDF, complete Europe PMC JATS, all seven original figures and Table 1 were inspected. The biological process is laboratory formation from ferrous sulfate reagents by washed resting A. ferrooxidans LX5, with a chemical H2O2 comparator. The record preserves the lower biological Fe precipitation, a separate extracellular-material perturbation, and the nonmicrobial downstream adsorption-stage boundary. No inherited criticality, natural-feed extraction, industrial deployment or isolated elemental recovery is claimed.

The exact current base had already passed fresh main checks; this session reuses the parent receipt `/private/tmp/cmm-round35-baseline-reuse.json`, rather than claiming another baseline execution. Named validation of the final record returned terminal 0, one record checked and zero failed. Parent handles final cohort checks; independent review is pending at this handoff.

## Deduplication and instructions

Read current CLAUDE/README, docs/records, schema, relevant validator/tests and local add-record/discovery contracts. Bounded searches used hidden/ignored-inclusive `rg --hidden --no-ignore --follow` over records, research, reviews and history in both the new worktree and original checkout. Referenced downloads searched were `/private/tmp/cmm-round13-mineral-raw`, `/private/tmp/cmm-next-li`, `/private/tmp/cmm-round12-aluminium-boron-raw`, `/private/tmp/cmm-round28-black-shale-research`, and `/private/tmp/cmm-round30-pyrrhotite-research`. Receipt `raw/dedup.json` retains exact boundaries, queries, outputs and errors. Binary images/PDF/ZIP were excluded from text matching; retained extracted text and metadata were included. This is a bounded material/DOI/experiment search, not a machine-wide absence claim.

The existing pyrrhotite record mentions schwertmannite as a secondary product in a different 1993 experiment. It does not identify the new material record or represent the controlled 2018 LX5 comparison. No duplicate schwertmannite identity or DOI/experiment was found in those scopes. Existing records and history were preserved.

## Sources, access and authority

- IMA-CNMNC September 2026 master list, official PDF page 195: Schwertmannite, approved, 1990-006. The displayed formula is Fe(III)16O16(OH)9.6(SO4)3.2·10H2O. The record does not equate the study's calculated formulas with authoritative mineral identity. IMA row image was visually inspected.
- Song et al. Materials 11(9):1739, publication 15 September 2018, DOI verified against publisher PDF, JATS and fresh Crossref metadata. Publisher PDF URL: `https://mdpi-res.com/d_attachment/materials/materials-11-01739/article_deploy/materials-11-01739.pdf`.
- Complete JATS: `https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6164185/fullTextXML`; retained filename `liu2018.xml` is an early shorthand, not an authorship assertion. Actual first author is Yongwei Song. Media ZIP from the matching Europe PMC supplementaryFiles endpoint contains 14 members: seven original figures in JPG and GIF. The JATS has zero supplementary-material nodes. No unseen supplement is used as evidence; this describes the inspected package, not a universal assertion that no additional material could exist.
- NCBI Taxonomy 920 was accessed at its authority and resolves Acidithiobacillus ferrooxidans. LX5/CGMCC No.0727 are source-reported strain labels. No independent CGMCC catalogue entry was verified and no strain CURIE is invented.
- Fresh Crossref metadata has no update-to/updated-by notice and empty relation map. Exact DOI/title searches with correction/retraction/erratum did not locate a relevant notice. The MDPI notes URL returned 403, limiting a publisher-version audit. No comprehensive no-correction guarantee is made.
- The primary article is CC BY 4.0 according to the article/Crossref licence. Full text and bulk media remain outside Git regardless; only summaries, locators and hashes are maintained.

## Verified assays and boundaries

### Formation versus chemical oxidation

Sections 2.1-2.3 describe growth to the end of exponential phase in modified 9K with 44.48 g/L FeSO4·7H2O, filtration, centrifugation, three pH1.5 acid washes and resuspension at pH2.5. Resting cells are not killed biomass. The assay uses 225 mL containing 11.12 g FeSO4·7H2O, 10% v/v inoculum, reported density 6.0×10^6 cells/mL, initial pH3.0, 28°C, 180 rpm and triplicate treatments. The wording does not unambiguously distinguish inoculum from final density in the first assay; the record reports the source density rather than recalculating it. Chemical assays use 250 mL effective volume and approximately 6 mL 30% H2O2 delivered at a constant rate approximating average biological oxidation.

Figure 1 and Section3.1 explicitly report 35.0% biological versus47.9% chemical total-Fe precipitation at60h. These fractions are loss of initial dissolved total Fe, not purified product recovery. Early oxidation is not matched:11.0% biological versus18.4% chemical at12h. Figure1b also extends to72h. Collection follows complete oxidation in Methods, reported complete at60h, while Figures1-3 captions state72h. The record retains that timing discrepancy and labels the numerical solution comparison60h.

Figure2 broad XRD features are assigned to schwertmannite reference47-1775; authors report no other characteristic peaks. This supports phase assignment, not quantified absence of amorphous impurities. Figure3 compares rough/spiny biological aggregates with smoother chemical material. Laser-dispersion sizes are aggregate measurements, not crystallite sizes. No greater biological mass yield is claimed.

### Extracellular-material perturbation

Section2.2.3 compares conventional resting cells; cells centrifuged20,000g for20min at4°C and resuspended with detached material; and cells treated similarly but with supernatant removed and replaced by equal-volume deionized water. Reported assay density is~6×10^6 cells/mL, with25mL suspension plus225mL reagent solution, initialpH3.0,28°C,180rpm,72h. Filtered solids were washed once and dried60°C to constant mass.

Figure7 gives0.89,0.96,1.29g respectively; Figure5b shows similar FeII oxidation trajectories; Figure6 gives microscopy comparisons. Table1 BET values68.23,56.76,86.43m²/g belong to this72h experiment, not the earlier comparison's58.79m²/g biological value. Collected mass is not purity-corrected mineral yield. Supernatant removal changes other solutes/handling and lacks purified-polymer add-back or independent viability testing. Proposed EPS inhibition is not an isolated molecular mechanism.

The Figure5a original axis is mg/L but Section3.4 prints mg/mL for the same0.16/1.67/0.08 values; organic carbon is an EPS proxy, not pure polymer mass. No reconciled concentration is adopted. Table1 formulas with x1.30/1.35/1.64 have OH5.24/5.19/4.23 instead of5.40/5.30/4.72 under the source's own8−2x rule. These unresolved calculations are not copied as identity/stoichiometry.

### Downstream arsenic assay

Sections2.2.2/3.3 and Figure4 use25mg collected material per100mL, initialAs(III)0–30mg/L, adjustedpH7.5,28°C,180rpm,4h, triplicates,0.22µm filtration. The source reports saturation uptake117mg/g biological and87mg/g chemical material. The record treats these as assay-specific source-reported uptake values, not a universal fitted constant. Although labeled As(III), analytical Section2.3 specifies total-As measurement. No independent redox speciation, living-cell adsorption or isolated-As recovery is demonstrated. Sulfate release is consistent with proposed exchange but does not prove an exclusive molecular mechanism.

## Deferred leads and counterevidence coverage

1. Cutting et al.2012 DOI10.1021/es204596z, PMID23043215: fresh Crossref/OpenAlex and Manchester institutional metadata were obtained; ACS fullPDF403 and no institutional download identified. Complete methods/figures/SI were not acquired, so no abstract-derived reduction/arsenic-retention measurements enter the record.
2. DOI10.1016/j.scitotenv.2020.144279: Crossref/OpenAlex and institutional metadata do not provide accessible fullprimary evidence in the bounded routes inspected. Deferred.
3. Li et al.2024 DOI10.3389/fenvs.2024.1482113: complete11-page PDF/XML/HTML and all8 mainfigures inspected. Original JATS names `DataSheet1.docx`; bounded legacy/publicpages/API paths returned404, so SI methods/FigS6 remain uninspected. Root is independently checking current public file links. Abstract M/Y capacity ordering conflicts with results; pH prose assigns values to SRB that Figure6 places under MR1. Phase claims rely on weak/shifted features. This extension remains deferred even though main text is available; no SI-dependent measurements enter the record.
4. Exact source/strain searches surfaced distinct comparator studies (e.g. DOI10.1021/acsomega.0c05606 and DOI10.3390/min7040064) and an older structural interpretation questioning phase homogeneity. These are leads, not accepted experiments or independently reviewed refutations. Current IMA identity is authoritative; the accepted2018 record already limits its phase-purity claim. Further expansion requires full source-specific assessment.

Acquisition receipts preserve initial sandbox-DNS failures separately from network-enabled attempts; they must not be described as publisher access denial. Actual403/404 outcomes are retained individually. No blocked route was treated as fulltext access.

## Handoff and reproducibility

Frozen record SHA256: `d4fb683c9253e73339d001453c808d6ea5aab0dc108cf2ea0788ce23fe5b7978`.

CREATE sidecar: `history/records/schwertmannite/2026-10-11T214621Z-codex-af894f.yaml`, SHA256 `8e34ba46322ac995d502f3adbea241d3dd885d8ecabbdd59fe8693b2cc2235df`. A distinct actual-UTC inline CREATE event is present. Named validation passed1/0. This dossier does not claim independent acceptance or completed cohort gates.

The accompanying JSON lists every retained raw artifact, byte count and SHA256, plus acquisition URLs/statuses. Complete PDF pages and original figure files are directly available for the independent reviewer. No schema change was needed. Remaining work is independent review, parent cohort gates, and future fulltext/SI investigation of the deferred reductions/2024 extension.
