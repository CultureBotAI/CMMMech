# Jarosite source investigation — round35

- UTC: 2026-10-11T21:43:23.749652+00:00
- Worktree: `/private/tmp/CMMMech-expansion-round35-20261011`; trusted base `f83cf867a38c470b4347f721d9ea9370c3019eaf`.
- Baseline: exact freshly checked prior-main base reused through `/private/tmp/cmm-round35-baseline-reuse.json`; no new baseline execution claimed.
- Curator: codex / GPT-6 / codex. This is a source dossier, **not** the independent scientific review.
- Decision: one K-jarosite mineral record, one culture-associated reduction/dissolution mechanism; no criticality or isolated recovery claim.
- Frozen record: `data/records/jarosite.yaml`, SHA256 `5642b5560b9d351f581fab9725486c440b4a3a0e6e4978c78478898e172b011b`.
- CREATE: `history/records/jarosite/2026-10-11T214126Z-codex-bd6b8a.yaml`, SHA256 `a9c21ce2f60f66f3e5f25d2be7be21062b31ec7bdacc2fcc48a90c8890e5ef95`; distinct actual-time inline event attached.

## Selection, identity and novelty

Chen et al. (2022) supplies complete methods, initial mineral characterization, three sulfur-donor culture/control comparisons, solution chemistry, spectroscopy and supplementary controls. This supports one mineral record without assuming that every jarosite-bearing residue behaves similarly. The IMA September 2026 list, original PDF page 104, identifies Jarosite as KFe3+3(SO4)2(OH)6, status Rd, 1987 s.p. The redefinition entry is not a fabricated approval identifier. The potassium species, broader jarosite family, sodium/ammonium/hydronium endmembers, elemental iron and industrial residues remain distinct.

The hidden/ignored-inclusive, symlink-following search covered 113 declared roots: current and original checkout records/research/reviews/history plus existing cited research/raw directories. It returned 626 matching lines, exit 0, without errors. Binary PDF, images, Office and ZIP files were excluded from text matching; retained extracted text and metadata were included. Exact commands, roots and results are retained in the paired JSON and raw dedup receipts. Existing records contain contextual jarosite observations, and prior copper-slag/zinc-ore literature cites Chen (2022), but the declared boundary contained no jarosite root or accepted claim from this experiment. The concurrent anglesite record also contains a contextual mention. This is not a machine-wide absence claim.

## Acquired and inspected evidence

The [official Coventry accepted manuscript](https://pure.coventry.ac.uk/ws/files/65409385/Post_Print.pdf), [DOI 10.1016/j.hydromet.2022.105908](https://doi.org/10.1016/j.hydromet.2022.105908), was downloaded with HTTP 200 at 21:37:36–38 UTC. Its 28 pages contain the repository cover, 22 manuscript pages, supplementary cover and Figures S1–S4. All text was read. Original Table 1 and Figures 1–8 on PDF pages 9, 10, 13–17 and 19, and Figures S1–S4 on pages 25–28, were rendered and visually inspected. All 28 pages were rendered for independent review.

The primary PDF SHA256 is `f458a0d2e86fd8a19c41575aa78029006783e844ec52a0c662c9b510598a2ce2`. Its cover identifies CC BY-NC-ND 4.0 terms and the accepted version, which may differ from the version of record. Full text and figures remain outside Git under `/private/tmp/cmm-round35-jarosite-research/raw`. Provisional Vera-prefixed filenames were corrected to Chen after author verification; immutable acquisition receipts and `filename-correction.json` document byte-identical renames.

The IMA original jarosite row was inspected from the retained September 2026 PDF, SHA256 `2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973`. This was reuse, not a fresh download; the current CNMNC landing page was checked separately. Live NCBI Taxonomy 930 confirms *Acidithiobacillus thiooxidans* at species rank. The [DSMZ DSM 504 catalogue](https://www.dsmz.de/collection/catalogue/details/culture/DSM-504) confirms the named strain and collection equivalents. No strain-specific TaxID, genome or Acidianus strain accession is invented.

## Experimental boundary

The authors prepared the feed using *Acidianus manzaensis* at 65°C and 180 rpm, with 100 mL medium in 250 mL flasks, initial pH 2.0 ± 0.05, 0.2 M FeSO4 and 0.067 M K2SO4. After approximately six days the precipitate was filtered, washed with deoxygenated water and vacuum dried at 30°C. Table 1 reports Fe 31.23%, K 5.33% and S 12.11%, versus ideal reference values 33.45%, 7.78% and 12.81%. XRD supports potassium jarosite; lower K and incomplete compositional/phase quantification prevent asserting a pure ideal endmember. No separate synthesis-causality mechanism is curated.

Dissolution used 0.5 g feed in 50 mL sterile basal medium in 150 mL bottles, initial pH 1.94 ± 0.05, and S0, Na2S2O3 or Na2SO3 at sulfur-equivalent 10 g/L. Cultures began at 4 × 10^8 cells/mL; each donor had an uninoculated control. Bottles were flushed with N2/CO2 (80/20) for approximately 20 minutes and incubated at 30°C, 180 rpm, for 34 days. Assays were in duplicate. Total and ferric iron were measured colorimetrically; Fe(II) was calculated by subtraction. Counts concern planktonic cells.

No dissolved-oxygen time course, killed-cell or culture-filtrate control, pH-clamped comparison, respiratory mutant/enzyme test, electron balance or isolated-product mass balance is reported. Enhanced release relative to controls supports a culture association under these conditions, without proving an exclusive molecular pathway or industrial performance.

## Source tensions and preserved limits

- The final sulfite extent is 96.4% in Results, manuscript line 246, but 98.4% in the abstract and conclusion. Neither is selected as an accepted recovery measurement. Figure 2c shows a near-complete extent without resolving the discrepancy.
- Supplementary Figure S2 gives day-34 abiotic extents of 1.3%, 6.3% and 8.5%, versus across-time maxima of 1.5%, 6.3% and 8.7%. Abiotic dissolution is not zero.
- Supplementary Figure S4 shows thiosulfate-control pH rising toward 2.8, qualifying the main text's blanket statement that abiotic pH and redox did not change significantly. S4 also includes a sodium-sulfate control without a complete corresponding dissolution protocol; no fourth equivalently specified assay is inferred.
- The near-ideal Fe/S ratio and XRD assignment do not erase the lower K content or establish quantitative phase purity.
- Complete-dissolution language exceeds unquantified detection limits and residual Fe(II)-bearing solids. No whole-feed iron balance or isolated product is provided.
- Fe(II) is calculated from total minus ferric iron. Its decline at some later times, together with solid Fe(II) spectra, is compatible with repartitioning; dissolved iron alone does not close the inventory.
- Nominal anaerobic preparation is documented, but persistent anoxia and an exclusive respiratory mechanism are not independently demonstrated. The largest dissolution response has no significant planktonic-count increase.
- Main manuscript line 216 points to Figure 8 for solid Fe(II), whereas the actual Fe L-edge spectra are Figure 7. The record uses Figure 7. Line 300 says four sulfur compounds, but Figure 4 displays the three methods-defined donors.
- Sulfur intermediates, pH changes and cell-derived chemistry remain possible contributions. Different-strain literature on indirect iron reduction is a useful follow-up, not a direct replication or refutation of this DSM 504 jarosite assay.

## Notice searches and deferred comparisons

Exact DOI/title queries with correction, retraction and corrigendum found no specific notice in the inspected results. Crossref's live original DOI record has an empty relation field and no update-to/updated-by entry. These are bounded checks, not proof that no notice exists anywhere. Direct DOI opening failed at an Elsevier redirect while the indexed publisher preview was readable; no repeated blocked acquisition loop was used.

1. First complete the independent native scientific review and cohort gates for the frozen jarosite record.
2. Ouyang et al. (2014), DOI `10.1016/j.gca.2013.09.020`, is a promising MR-1 comparison. Primary preview and DOI metadata were inspected; complete methods, original figures and supplements were not acquired in this round. No measurements were imported.
3. DOI `10.1016/j.cejgas.2026.100108` may support a jarosite-formation comparison. Publisher preview and metadata were inspected, but the direct publisher page returned 403. Full primary evidence and species/group identity remain unresolved.
4. DOI `10.1016/j.resmic.2023.104110` and DOI `10.3389/fmicb.2017.00211` provide primary-literature leads on indirect iron reduction in different conditions or strains. Only abstracts/search excerpts were assessed in this pass; figures and complete methods need a separate investigation before transferring measurements or claiming contradiction. The current record already avoids asserting direct respiration.

## Checks and handoff

Named validation actually completed with exit 0: one record checked, zero failed. Its post-completion receipt is `raw/named-validation.json`. The existing schema expresses the supported scope; no validator, test or shared file changes were needed. Percentages remain qualified source prose, not concentration observations.

The paired JSON records queries, acquisition state, detailed source roles, dedup boundaries and all 47 raw artifact checksums. An independent reviewer must evaluate the exact frozen record and linked CREATE history against the complete primary, followed by parent-owned corpus gates. This investigation performed no external posting, Git mutation or integration configuration.
