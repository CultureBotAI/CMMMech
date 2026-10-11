# Round22 PCB staged-process evidence

The existing [waste printed circuit board record](../../data/records/waste-printed-circuit-boards.yaml) is extended with one stage-specific mechanism. This is a known round21 frontier lead, not a new resource identity. The 2024 paper and its paired workbook are one experiment; repository mirrors do not provide independent replication. Earlier 2021/2022 mechanisms and history remain unchanged.

## Sources and access

- [Iglesias-González et al., Minerals Engineering 205 (2024), 108459](https://doi.org/10.1016/j.mineng.2023.108459). Crossref and repository metadata support the title, authors and 2024 issue year; the Seville accepted-manuscript cover says 2003 and is not followed for citation dating.
- [Experimental dataset, DOI 10.12795/11441/161670](https://doi.org/10.12795/11441/161670), deposited 25 July 2024. The original repository bundle provided Data.xlsx and README; API provenance and actual download hashes are in the paired JSON.
- [Seville accepted manuscript](https://idus.us.es/server/api/core/bitstreams/bf5e6054-a962-47b4-bee1-1720300fb1db/content), 31 PDF pages including repository cover. Full Methods 2.1–2.2 and Results 3.1–3.5, relevant introduction/conclusions, Tables 2–6 and rendered Figures 2–8 inspected. Figure 1 caption/conceptual description was read; no claim of inspecting its graphic. [UPC manuscript](https://upcommons.upc.edu/server/api/core/bitstreams/f07097b6-b4de-47bc-9520-3c20147e472a/content) is a same-paper mirror, acquired and text-extracted, not a second independent full assessment.

Publisher and repository page opens through the web tool returned internal errors, while official direct bitstream/API downloads succeeded. The precise two discovery/status queries are retained in JSON: first returned sets, no filters or pagination, no complete correction-registry or literature exhaustion claim. Crossref supplied no update-to relation in the inspected response; this is bounded evidence, not a guarantee of no corrections. No unverified publisher supplement is claimed absent.

## Accepted evidence and limiting contradictions

Methods 2.1 describe ground mobile-phone material after casing/battery removal, targeting 0.8–2 mm with 2/7 mm recirculation screens. The README instead says 2–7 mm. Table 2 nine Cu assays give 35.71 wt% mean and 4.16 percentage-point SD; this heterogeneous feed is not every PCB. No material or organism CURIE is invented, and no criticality designation is inherited.

The 96-hour 60-degree C stirred chemical leach used biogenic Fe(III), with commercial Cu sulfate added to simulate recycle. Effluent was collected for later filtration and biooxidation. Table 6 is the narrow biological-stage evidence: living Riotinto community, reported mainly A. ferrooxidans and L. ferrooxidans, 31 degrees C, 0.55 L column. At 100 mL/h, raising inlet Fe(II) to 9.29 g/L with Cu 10.45 g/L left 2.37 g/L Fe(II); the later zero outlet required 37 mL/h. This does not establish universal absence of inhibition, member-specific activity, a sterile-control effect, or simultaneously closed operation. No matched sterile column or replicated full train is reported in inspected Methods/Results.

Table 5 reports 135.01 g feed and 74.93 g combined residual solids with 0.41% Cu, yielding the paper's approximate 99% extraction claim. Workbook composition B21/D23:D24 explicitly identifies 1.5% HCl washing and 62.03→53 g retained-solid mass. Wash loss, sampled fractions, copper-spiked inlet and heterogeneous starting grade prevent adoption as an independently reproduced reactor-only mass balance. Native records therefore attribute the figure to the paper and qualify it.

Actual column liquor underwent LIX 973 solvent extraction, with aqueous analysis and calculated organic concentrations (Methods 2.2/Results 3.4/Figure 5). Stripping used simulated electrolytes. Methods 2.2 and Results 3.5 explicitly say synthetic 15 g/L Cu plus 155 g/L acid for electrowinning, in tension with Table 4's AP SX origin and 150 g/L acid. Figure 7 solution decline and Figure 8 Cu-rich local EDS therefore do not establish actual-board metal recovery, certified purity, or closed-loop zero-reagent/zero-effluent performance. The reported 99.2% is current efficiency, not product purity or board yield.

## Dataset inspection and import decision

The XLSX ZIP/XML was parsed with original sheet names, cell values and formulas retained locally. Six sheets contain 1,435 nonempty cells: composition 170, Batch 895, CSTR 20, biooxidation 83, SX 213, EW 54. This is full parsing, not independent numerical reproduction of every model/formula. Focused displayed checks covered composition Cu mean/SD and wash rows; Batch volume/normalization/model cells; every nonempty CSTR and biooxidation cell; selected SX aqueous/iron cells; every nonempty EW cell.

Important unresolved items: Batch C2 says 1.2 L versus 1 L in Methods; B9 normalizes batch conversion to measured maximum 3.447 g/L, while B11:B13 retain model settings differing from the paper's continuous-stage retention time. CSTR productivity/loading cells use decimal-comma strings. Biooxidation H2 uses g/h rather than paper mL/h, and A4:A10 mix 2023 dates with 16/02/24 despite README collection date 10-01-2022. No density conversion or analysis dates are inferred. EW C16 = 1.02 under CE (%) differs from manuscript 99.2%; additional 50-degree series lacks a demonstrated one-to-one manuscript mapping. Composition T8 Au mean differs from paper Table 3, and SX H3 iron 43.4 g/L exceeds initial G3 = 38.8; neither is silently reconciled. These checks support contextual limitations, not a workbook-wide import. Rates, percentages and uncertain dates fall outside the native exact-mg/kg concentration contract.

## Reuse and follow-up

Dataset metadata identifies CC BY 4.0 (README says CC-BY); metadata itself is CC0. UPC manuscript terms indicate CC BY-NC-ND 4.0. Raw PDFs, workbook, rendered figures and extracted text stay outside Git; committed content is original curation/provenance. No license is inferred for a different publisher artifact.

The paired data are valuable for a later reconciled mass-balance audit, but exact links among sampled/wash fractions and copper-spiked liquid inventory remain unresolved. Do not manufacture author clarification. Other round21 PCB leads (DOI 10.1007/s12649-020-01036-y, DOI 10.3389/fmicb.2021.669738 and PMC10079379) remain distinct follow-ups. This bounded search does not establish literature exhaustion.

## Validation and review handoff

Single-record validation passed: `uv run --locked cmmmech validate data/records/waste-printed-circuit-boards.yaml` (one checked, zero failed). A real EDIT sidecar and separate inline event are attached; earlier scientific mechanisms, source entries and provenance prefixes were programmatically checked unchanged. Independent scientific review and full batch gates are pending at this source-report freeze. Final publication evidence belongs in the batch frontier and saved canonical review, not retroactive edits to this report.
