# Electroplating sludge: source investigation

Investigator: Codex /root/round27_packaging (GPT-6; codex). This is author research and curation, not an independent scientific review.

## Decision and material boundary

Create `electroplating-sludge` as a secondary resource: solids from treatment of electroplating wastewater. The Chennai sludge examined by Prabhu and Baskar (2015) and compositionally different sludge examined by Kordloo et al. (2026) provide two separately scoped experimental arms. The latter does not name its sludge supplier or sampling site. Do not pool feeds, claim replication, or infer a pure mineral species. No inherited criticality or recovered-product claim is added.

This owner differs from metallic electroformed copper/silver manufacturing scrap and GaAs-production hydroxide sludge. The existing automotive wastewater-treatment sludge record is grounded in an automotive factory whose contributing process is unresolved; it cannot be renamed electroplating sludge from that information. Its 2009 experiment and the round19 assessment were read. Existing nickel-sulfate application mentions and generic galvanic-sludge research leads do not represent the selected experiments.

## Acquisition, rights and inspection

Both selected full primary papers were freshly acquired from their official publishers on 2026-10-12, together with current Crossref metadata and NCBI Taxonomy 920 XML. Initial sandbox DNS failures remain in acquisition-1.json; successful authorized public GETs are independently recorded in acquisition-2.json. These are new acquisitions, not reused prior-round originals. Complete source bytes, rendered originals and acquisition receipts remain outside Git in the raw directory. Publisher rights are retained: the 2015 PDF bears publisher copyright; the 2026 paper identifies CC BY-NC-ND 4.0. No bulk original article or image redistribution is included in the repository.

Prabhu and Baskar, DOI 10.15244/pjoes/30931: official complete PDF has nine scientific pages, printed 1249–1257, plus a blank tenth page. All ten rendered pages were personally viewed, including Figures 1–10 and Tables 1–4. The official landing page and complete paper exposed no article-specific supplement in the bounded inventory. This is not a claim that no unlinked supplement exists.

Kordloo et al., DOI 10.1038/s41598-026-37924-x: the final publisher PDF has thirteen pages; all pages, Figures 1–5 and Tables 1–4 were personally viewed. The complete official HTML identifies one supplement, `41598_2026_37924_MOESM1_ESM.docx`, acquired from the exact observed Springer Nature MediaObjects URL in acquisition-si.json. All ten original embedded image files covering Figures S1–S6 were personally viewed; Tables S1–S3 were read from their original DOCX XML cell grids. The extracted `original-order.json` binds captions and media order. No claim is made to a rendered DOCX page count or pagination inspection.

## Prabhu and Baskar 2015: accepted scope and limits

The sludge originated in an electroplating-sector effluent-treatment bed in Chennai, sampled 2–5 cm below the top, refrigerated and air-dried overnight. Table 2 reports dry-feed Zn 42,180±685 mg/kg and Ni 20,160±430 mg/kg for five samples. A Chitradurga copper-mine drainage isolate was assigned to Acidithiobacillus ferrooxidans through reported phenotypic/morphological traits; there is no strain deposit or sequence accession. Sulfur medium and acclimation through 0.25–1% sludge precede triplicate 250 mL flask experiments with 90 mL medium, 10 mL inoculum, 1–5% (w/v) solids, initial pH 3, 28 °C, 150 rpm and 480 h.

Only the 1% loading has an uninoculated comparator; it additionally received 5% (v/v) alcoholic thymol solution, whose thymol concentration is 1% (w/v). It is neither chemically nor longitudinally pH matched. Five-millilitre samples were withdrawn every 48 h, centrifuged, filtered and measured by AAS; sulfur-free medium replaced sampling and evaporation losses. The source does not resolve a complete cumulative sampling correction.

Figures 2–4 support culture-associated acidification and greater Zn/Ni mobilization: the 1% treatment ends at pH 1.17 versus control 2.63; source-reported 20-day Zn/Ni percentages are 96.31/84.40 at 1% and 79.03/66.14 at 5%. These are reported assay percentages, not independently reconstructed mass recoveries. Printed Equation 4 has (M0−Msoln)/MT while its definitions describe aqueous initial and later concentrations; the sign and solid/liquid normalization are unresolved. No unique biological contribution beyond acid-mediated leaching follows from the mismatched control.

Figures 5–6 show EDX/FTIR of 5% residue, not a quantitative phase-resolved balance. Figures 7–10 and Tables 3–4 are model fits. Several Ni coefficients differ between Table 4 and plotted labels; Table 4 gives higher liquid-film than chemical-reaction R² for 2–4% solids. The universal chemical-reaction-control conclusion is not imported. Table 2 organic matter is 4.1±0.11%, whereas prose says 4.1 mg/kg; the medium prints Ca(CO3)2. Neither inconsistency is silently repaired into a recipe or mechanistic inference. No purified product, complete recovery mass balance or industrial deployment is demonstrated.

## Kordloo et al. 2026: accepted scope and limits

The heterogeneous feed is source-labelled electroplating sludge; its supplier/site and detailed generation process are not given. Prose gives 8.23% Cr, 5.97% Cu and 10.92% Ni; Table 2 uses 12.03% Cr2O3, consistent with the elemental-Cr conversion. This does not identify a pure metal compound. Figure S2 reports d80 about 97.9 µm.

An unnamed A. ferrooxidans culture came from the Soil and Water Research Institute, Karaj. Culture preparation used sulfur/ferrous medium initially adjusted to pH 1.8, 100 mL with 10% inoculum, one week at 34 °C and 140 rpm. The final liquor is reported at pH 1.2, 650 mV ORP and 9 g/L ferric iron. Centrifugation at 5000 rpm for 15 min is the reported cell-removal operation; no filtration or sterility assay is stated. The microbial role is upstream reagent generation, not demonstrated living-cell contact during sludge leaching. Initial added acid and culture-derived iron remain components of this liquor.

The downstream assay used 100 mL reagent in 250 mL three-neck flasks and a 37 kHz, 150 W ultrasonic bath, with triplicate OFAT comparisons across 300–500 rpm, 10–50 g/L solids and ambient to 75 °C. Figure 1 supports an early ultrasound benefit for Ni/Cr at ambient temperature, 10 g/L and 400 rpm, while Cu differences are small and prose reports no significant Cu effect. Longer-time differences narrow. There is no acid/ferric-iron matched synthetic-reagent control; the paper explicitly proposes this on page 11.

Figure 4 and pages 7–8 report 92.51% Cr, 86.91% Cu and 91.25% Ni at 8 min, 45 °C, 400 rpm and 10 g/L. Later/hotter arms decline and ambient late endpoints can exceed those 8 min values. Thus the reported optimum is conditional. No explicit extraction formula or full sampling/mass balance allows independent reconstruction. Table S2 final-PLS concentrations are in ppm and are not silently converted to mass yields or mg/L without sufficient assay linkage.

Figures 5/S5 support source-assigned hydronium-jarosite-containing residues and Fe/S surface enrichment, but do not directly measure Cr/Cu/Ni incorporation or establish a passivation rate-controlling pathway. Medium descriptions differ on 44.22 versus 44.7 g/L and Fe2SO4·7H2O versus FeSO4·7H2O. Table 4 has six solids levels including 25 g/L; Figure 3 has five, omitting 25 g/L. These differences remain explicit.

The broad abstract detoxification claim is not adopted. Page 10/Figure S6a give residue Ni 13.9 mg/L, above the source's 5 mg/L TCLP comparator. Figure S6a feed Cr is 11.6 against a 12 comparator, also limiting the prose claim that both initial values exceed thresholds. Figure S6b gives Ni 17.8 to 4.1 but labels its SPLP threshold n.s.; Cr is 5.82 to 1.6 against 5. This does not establish that Ni meets a stated SPLP threshold or that the material is generally safe for landfill. Comparator values are source observations, not independently verified regulatory advice. No isolated saleable product or plant-scale performance is shown.

## Taxonomy, overlap and notice checks

Fresh official NCBI XML verifies TaxId 920 as Acidithiobacillus ferrooxidans at species rank. This validates the label/identifier, not the experimental cultures, strain identity or purity. No type-strain identity is inherited.

Crossref identity checks match both selected papers; returned works objects have no update-to notice and empty relation objects. Bounded live DOI-specific erratum/correction/retraction searches, the complete publisher pages and the current PDFs identified no article-specific notice in the inspected results. The exact search output is retained in raw/notice-search.json. This is not an exhaustive absence assertion or an independent Crossmark-status response.

The two accepted papers have distinct compositions, preparation and assay roles and are represented separately. Within the 2026 supplement's literature table, Kordloo 2024 Environmental Technology & Innovation 36:103826 has the same Ni/Cu/Cr percentage triple repeated in the 2026 ambient prose (89.59/89.49/92.33). The 2024 original is not acquired or independently assessed; reuse, derivation and independent replication remain unresolved. Only the separately qualified 8 min 2026 values are curated. Do not infer misconduct from this similarity.

## Deduplication scope

Before record creation, hidden and ignored files were included with symlinks followed and resolved-path cycle prevention in data/records, research, reviews and history of both the round57 worktree and the exact published-base source clone. Relevant cited raw/download roots were then scanned. The original Documents checkout is unavailable with EPERM, so it was not touched or claimed searched. No unrelated home or temporary-directory sweep was performed.

The normalized receipt covers 8,490 eligible text files, 197 cited directories, and thirteen unavailable cited prefixes; 32 cited standalone files were distinguished from directories. A separate receipt searches all 29 eligible standalone text files (three binary files excluded), giving 8,519 text files across the combined bounded scope. Exclusions are .git, .venv, __pycache__ and node_modules; raw text size cap is 30 MB. Binary PDFs/images are not claimed semantically searched; selected originals were separately inspected. The exact root list, unavailable prefixes, regex, matched context and errors are retained. The initial dedup.json used a less accurate cited-prefix classifier and remains historical; dedup-normalized.json plus dedup-standalone.json define the final scope. No selected experiment or equivalent accepted owner was identified within that accessible bounded search, including ignored files; inaccessible and binary-only collections limit this conclusion.

## Deferred work

The 2026 consortium lead DOI 10.1016/j.rineng.2026.112512, 2021 DOI 10.1016/j.jenvman.2021.112133, pilot-scale DOI 10.1016/j.chemosphere.2019.05.185, fungal DOI 10.1016/j.jclepro.2020.121622 and the 2024 overlap lead require complete primary methods/original graphics and any supplements before extensions. None supplies accepted measurements here. The electroplating review DOI 10.3390/ma17071707 was only a discovery aid. No new frontier acquisition is required to publish the two supported, qualified arms.

## Validation and provenance

The exact baseline is the parent's already completed fresh postmerge validation of the unchanged trusted base: 317 passed, 3 skipped, 264 records and 312 histories. This is reuse, not a fresh author-run whole-corpus check. The final named command was `PYTHONDONTWRITEBYTECODE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache UV_OFFLINE=1 uv run --locked cmmmech validate data/records/electroplating-sludge.yaml`, run in the round57 worktree; terminal exit 0 and log report 1 checked, 0 failed. Full new-cohort gates and independent scientific review are parent-owned and were pending when this dossier was saved. The real CREATE sidecar and distinct inline event record actual UTC activity. The JSON companion binds current record/history bytes, every retained raw artifact, acquisition/search receipts and the final validation log.

Dossier saved: 2026-10-12T12:41:15.347537Z. Trusted base: `76509ff65c70edb5f212b6b4217febe5493bb0f3`.
