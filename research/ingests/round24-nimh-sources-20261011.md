# NiMH battery source assessment

The accepted candidate is a process-defined **secondary resource**, spent nickel-metal-hydride batteries represented by mixed recycler powder. It is distinct from the existing lithium-ion battery black-mass record and from constituent elements or pure electrodes. No resource-level criticality is asserted.

The [machine-readable dossier](round24-nimh-sources-20261011.json) records actual acquisition times, hashes, exact search queries and limits. The principal source is [Rasoulnia et al. 2021](https://doi.org/10.1007/s12649-021-01398-x), with the [publisher-linked supplement](https://media.springernature.com/original/springer-static/esm/art%3A10.1007%2Fs12649-021-01398-x/MediaObjects/12649_2021_1398_MOESM1_ESM.docx). The full primary PDF was acquired from the German National Library (SHA256 `fde0cdd23acd519b7740891655e3bfcc360bca33017c53366333df2af0474986`). Its main figures and tables were visually inspected. Supplement text and all native chart series/error caches were inspected; an original Word rendering was unavailable. Supplementary medium selection plots do not establish another battery-leaching experiment.

## Selection, identity and duplicate checks

Hidden/ignored files and relevant symlinks were included within data/records, research, reviews and history. The expanded NiMH/DOI search found the known 2022 phosphate source lead in the original landscape report, so this is not a claim that NiMH literature was newly discovered. No NiMH resource root existed in the searched pre-curation corpus. The full 2021 paper provides a more immediately reviewable bounded ingest than abstract-only or incompletely inspected follow-ups.

[DSMZ 3503](https://www.dsmz.de/collection/catalogue/details/culture/DSM-3503) resolves Gluconobacter oxydans strain I; [DSMZ 40097](https://www.dsmz.de/collection/catalogue/details/culture/DSM-40097) resolves Streptomyces pilosus ISP 5097. [NCBI 442](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=442&mode=Info) and [NCBI 28893](https://www.ncbi.nlm.nih.gov/taxonomy/28893) are species identities, not proof of experimental-stock authentication.

## Evidence and interpretation

Methods and Figure 1 distinguish simultaneous addition, delayed powder addition and centrifuged six-day culture supernatants. Actual spent powder was screened at 630 micrometres and autoclaved under nitrogen. Triplicate experiments used 1% w/v powder, 27 +/- 1 degrees C and 150 rpm. Gluconobacter and Streptomyces were tested in different phosphate concentrations. The former's delayed and spent-medium treatments produced filtered-liquid metal extraction, whereas its simultaneous treatment and all tested Streptomyces modes lacked appreciable leaching. These null results remain explicit; they are not recast as universal biological incapability.

Figure 4 and main Results retain source-reported extraction percentages and triplicate standard-deviation error bars. The abstract's two-step total REE value 6.0% disagrees with main Results/Table 3 value 6.5%. Methods/Figure 3 indicate one-day Gluconobacter pregrowth, whereas Table 3 gives two days; the timeline is not silently repaired. Table 2 and Results also disagree over higher-phosphate initial pH; no optimization recommendation is imported from that discrepancy. Main Table 1 is feed-specific and reported in mg/g, so it was not transformed into native mg/kg source-cell observations.

Measured gluconate and pH support culture-liquid activity but do not isolate a unique pathway or partition cells, dissolved ions and precipitates. Cell adsorption and phosphate precipitation remain proposed explanations within this paper. SEM/EDS shows selected particles, not a closed phase-specific balance. No isolated product, process economics or commercial operation was demonstrated.

## Access and conflicting evidence frontier

The DOI/title correction search inspected first returned sets without date filters; no relevant correction notice returned in that bounded search. No exhaustive absence claim is made.

- [Rasoulnia et al. 2022](https://doi.org/10.1016/j.mineng.2021.107361) is an existing-resource extension concerning phosphate reduction. A direct institutional download returned HTML challenge, not a PDF; indexed primary Methods and publisher abstract are available. Full figures and model supplements require review before adding yields.
- [Heidarinejad et al. 2026](https://doi.org/10.1039/d6ra03345h) has a retrieved PMC HTML and unreviewed figures/supplements. Indexed abstract/conclusion metal-percentage assignments disagree. No 2026 yield was imported.
- Alkaline button-cell batteries and discarded LED lamps are additional feed-identity leads, not accepted records. Their full primary evidence and overlap with existing resources require assessment.

Raw full text and supplementary chart data remain outside Git. Independent exact-state review and final batch checks are separate acceptance gates.
