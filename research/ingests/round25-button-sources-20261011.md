# Round25 source investigation: spent zinc-manganese button cells

- UTC: 2026-10-11T14:55:59.780709+00:00; Codex (GPT-6; Codex), root curator.
- Base `baedff25eafad1516270916a651af6754ffa5996`; branch `curate/cmm-expansion-round25-20261011`; [batch issue 90](https://github.com/CultureBotAI/CMMMech/issues/90).
- Scope: a distinct used-battery resource, its primary microbial leaching evidence, and unresolved related resource leads. No criticality-list claim is made for the waste.
- Exact queries, access results, dedup boundaries and raw provenance are in [the paired manifest](round25-button-sources-20261011.json). Search included ignored/hidden files and relevant symlinks in records, research, reviews, history and the specified round24/25 raw directories. Existing mentions were leads and references; no record matched this material in that scope. Binary/HTML exclusions from text grep are explicit, and the selected PDF was separately read in full. This is not a machine-wide or exhaustive literature search.

## Sources and acquisition

The [KIChE primary paper](https://doi.org/10.1007/s11814-022-1160-x), Pourhossein, Sadeghi and Mousavi (2022), is an experimental report despite its PDF's repeated “INVITED REVIEW PAPER” header. Springer confirms the version-of-record date of 25 June 2022 and September issue, pages 2444–2454. The [publisher PDF](https://www.kiche.or.kr/journal/kjche/fulltext/39/9/2444/47643892) was acquired at 2026-10-11T14:51:22.726551+00:00; 3485854 bytes, SHA256 `683278a4eb68599f096eec35869fdabd51248507127991e44bda53e4558bf350`. Its eleven pages, Table 1 and all Figures 1–6 were inspected; figure/table pages 4, 5, 6, 8, 9, 10 were rendered and visually checked. Local artifact: `/private/tmp/cmm-round25-button-raw/pourhossein2022.pdf`. KIChE's landing page declares CC BY-NC 3.0, the PDF carries KIChE copyright, and Springer restricts its own access route. Raw files remain outside Git; this assessment does not redistribute the paper.

The [2019 predecessor](https://doi.org/10.1016/j.hydromet.2019.06.003) remains abstract/preview level in this investigation. Direct publisher requests failed and exact-title/DOI searches did not acquire full methods. Its reported Zn/Mn yields and detoxification claims are not transferred to the record. It is related earlier work, not an independent confirmation of the 2022 treated feed.

## Claim assessment

Methods 1–8 support an actual mixed powder from approximately 1 kg of spent watch-store button cells, manually dismantled, dried at 100 degrees C, crushed and screened. The study identifies its feed as Zn-Mn but does not authenticate each manufacturer's cell chemistry. Thermal treatment is a separate four-hour furnace step at 200 or 600 degrees C; the air atmosphere of the TGA cannot establish the furnace atmosphere. The number-200 sieve and stated below 70 micrometre size are preserved as source descriptions, not a measured distribution.

Results 2–3 and Figures 3–5 support culture-associated solubilization, source-reported 95% Zn/91% Mn after 21 days at 20 g/L of 600-degree-treated feed. Untreated-feed outcomes are 21% Zn/16% Mn. Figure 3's activity comparison is at 1 g/L, not the 20 g/L extraction assay. The serially adapted culture did not grow at 25 g/L, and untreated/200-degree-treated samples inhibited the culture in the selected assay. No isolated product or full-battery yield is shown.

The comparators are spent culture liquid (centrifugation does not establish sterility) and chemical ferric sulfate in distilled water. Their pH/iron histories and medium composition differ, so greater extraction does not uniquely establish a microbial molecular cause. Methods give spent-medium ferric iron 6 g/L, Results approximately 6.7 g/L. Methods alternate ICP-OES and ICP-MS for the Vista-pro analysis, do not state the Millipore pore size, and do not close cumulative sampling losses. Triplicate means are stated; error bar definitions are not supplied. Table 1 supplies feed composition, but source prose swaps original Zn/Mn percentages. No absolute-feed inventory was imported.

The chemical-Mn text value 55% is not visually identical to its Figure 4 bar near 60%. Abstract pretreatment improvements and conclusion 33% Zn/31% Mn statements do not transparently reconcile with the endpoints. Figure 5's first sampled Mn fraction is below 50%, despite prose describing more than 50% of both metals on the first day; that early fraction is not imported. EPS, siderophores, reductase respiration and protein adaptation were not directly tested; printed reaction equations include atom/charge balance defects. Figure 6 indicates a mixed residual solid with jarosite and remaining ZnMn2O4, not proof of complete detoxification or recovered-pure-metal yield.

## Experimental culture identity

Methods 4 names A. ferrooxidans PTCC 1664. The [NCBI species page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=920&mode=Info) verifies the species label only. Exact-number searches surface a 2006 paper indexed as Pseudomonas putida PTCC 1664; its full PDF was inaccessible in this pass, so no reassignment is made. The [official collection entrypoint](https://irost.org/ptcc/) was opened, but its database link returned 404. The record preserves the reported name and unresolved strain, with no organism CURIE. Sequence/collection authentication remains a concrete follow-up.

## Corrections, supplements and limits

Exact-title/DOI correction, retraction and supplementary queries, the publisher landing pages and full PDF were inspected. No applicable correction or separate supplement was located in that bounded coverage; broader absence is not claimed. Primary facts are not accepted merely because the offline validator passes. The source has useful controlled comparisons but substantial interpretive limitations, which remain in the record. Quantitative concentration-cell storage does not apply to these extraction percentages; no schema change is needed.

## Handoff

Curate `data/records/spent-zinc-manganese-button-cell-batteries.yaml` with canonical CREATE history and independent exact-state scientific review. Record creation is the next curation step, not acceptance by this dossier alone. Further evidence priorities: resolve PTCC 1664, acquire 2019 full methods, audit whole-feed inventory and thermal emissions, then investigate silver-oxide/zinc button cells, Ni-superalloy residues (10.3390/pr13072157) and brake-pad waste (reference 25). These leads prevent an exhaustion claim.
