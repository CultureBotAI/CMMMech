# BOF steelmaking dust: source investigation and curation handoff

- Investigation timestamp: 2026-10-11T16:11:19Z; Codex (GPT-6).
- Worktree: `/private/tmp/CMMMech-expansion-round27-20261011`, branch `curate/cmm-expansion-round27-20261011`, trusted base `3f1350b24b4f6248ed2e17caade936c15af9be93`.
- Selected identity: basic oxygen furnace steelmaking dust, a process-derived secondary resource distinct from BOF slag, EAF dust and blast-furnace cast-house dust. The primary experiment explicitly uses a historical Teesside stockpile sample. Its exact dust-collection fraction is not specified.
- Outcome: [new record prepared](../../data/records/basic-oxygen-furnace-steelmaking-dust.yaml), pending independent scientific review; this discovery report does not certify acceptance.

## Search boundaries and routes

Hidden and ignored files, with relevant symlinks followed, were searched in the original checkout's `data/records`, `research`, `reviews` and `history`, plus the referenced `/private/tmp/cmm-round26-root-raw`, `/private/tmp/cmm-round25-frontier-raw` and `/private/tmp/cmm-round25-button-raw`. The initial search used `PMC11200337`, the exact article title and BOF-dust variants; no prior match was found within those boundaries. Receipt: `/private/tmp/cmm-round27-bof-dust-dedup.txt`. This is not a machine-wide search. A preliminary general-lead search mistakenly named a nonexistent `cmm-round26-bof-raw` directory; the dossier was then read and its actual `cmm-round26-root-raw` boundary searched successfully. No completeness claim relies on that failed path.

Live web searches on 2026-10-11 used the first returned result sets, without pagination or date filters:

| Query | Outcome |
|---|---|
| `microbial bioleaching "mill scale" bacteria` | Broader steel-residue discovery; no mill-scale claim curated |
| `bioleaching "galvanic sludge" full text` | Existing automotive sludge overlap; BOF-dust primary paper found among results |
| `bioleaching "aluminium dross" fungi` | No dross assay accepted from this bounded set |
| `"Extracting metal ions from basic oxygen steelmaking dust" correction OR retraction OR supplementary` | Primary publisher/PMC and related representations; no applicable notice identified in returned set |
| `"Extracting metal ions from basic oxygen steelmaking dust" pdf` | Primary PMC and publisher matched; associated metadata representations deduplicated |
| `"10.1016/j.heliyon.2024.e32437" retraction correction erratum` | No applicable notice identified; not proof of universal absence |
| `"Unlocking the hidden value of industrial by-products"` | Related 2023 study verified as a follow-up lead, not independent validation of 2024 observations |

The first web open of PMC returned a browser challenge. A subsequent legitimate network request retrieved complete publisher-deposited HTML, and Europe PMC returned full JATS XML. All five original figure JPEGs were acquired from the asset URLs in that HTML and visually inspected. The old NCBI OA-helper URL returned 404; it was not treated as an article download. Exact URLs, UTC acquisition times, file sizes and SHA-256 values are in the paired JSON, backed by local raw receipts.

## Primary evidence and identity

[Tezyapar Kara et al. (2024)](https://doi.org/10.1016/j.heliyon.2024.e32437), *Heliyon* 10(11), e32437, is the accepted primary study, deposited as [PMC11200337](https://pmc.ncbi.nlm.nih.gov/articles/PMC11200337/). Crossref, the deposited article and PubMed agree on DOI, title and five authors. The article was accepted/published online on 4 June 2024 and collected in the 15 June issue. Crossref's month-level date is not a new experimental edition. Crossref has no `update-to` entry and an empty relation object at this inspection; those metadata limits do not exclude undiscovered notices.

The article's permissions and version-of-record license state [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Full text, metadata and figures remain outside Git under `/private/tmp/cmm-round27-root-raw`; the repository retains curator paraphrases and provenance. All-data-in-article is the authors' availability statement, not confirmation that individual replicate measurements are downloadable. The inspected full XML/HTML has no supplementary-material attachment. The complete deposited text, Tables 1-3, Equation 1 and Figures 1-5 were checked; no separate raw replicate dataset was acquired.

[DSMZ DSM 583](https://www.dsmz.de/collection/catalogue/details/culture/DSM-583) lists *Acidithiobacillus ferrooxidans*, agreeing with this paper. [NCBI Taxonomy 920](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=920&mode=Info) resolves the species. Neither authenticates the adapted experimental stock. No external identifier was assigned to the mixed dust resource, and no constituent criticality designation was inherited.

## Claim-level assessment

Methods 2.1 identifies bulk Teesside stockpile dust, air drying, grinding, a 2 mm sieve, and 121 °C/15 min autoclaving. Aqua-regia/microwave digestion and ICP-MS establish an operational initial inventory, not exhaustive phase identification. Table 1 contrasts autoclaved and non-autoclaved concentrations; mixed higher, equal and lower values do not establish a causal loss solely from autoclaving.

Methods 2.2-2.3 describe culture adaptation, iron-containing medium, acid additions, two-day precultivation, 1% solids and duplicate batch arms. The article's `1% w/v inoculum` and energy-source shorthand are not silently converted to a different recipe. The medium preparation states 11.1 g/L ferrous sulfate heptahydrate and about 2.22 g/L Fe(II). Culture maintenance is at 30 °C/150 rpm; exact batch temperature should not be inferred beyond the source wording. Reagent acid at 5 M is used for pH adjustment, not a 5 M final leachate. Acid-only and uninoculated iron-containing comparisons exist, but a sterile ferric-matched comparison and acid-demand balance are not reported in the inspected experiment.

Figures 1-2 support culture-associated iron oxidation and faster early release. Figure 2's day zero is dust addition on culture day 2. Controls later approach or exceed inoculated values for multiple metals; the record retains Cu/Zn/Mn examples and does not claim a universal endpoint advantage. Equations for metallic Cu/Zn are explanatory chemistry, not proof of these phases in the feed. ORP and iron depletion are proxies; they do not measure cell proliferation or independently establish a molecular pathway.

Figure 3 compares a three-day biological assay with a two-hour choline chloride/ethylene glycol stage followed by fourteen-day residue bioleaching. The chemical stage uses 12.5% solids versus 1% for direct bioleaching, different temperature wording and different residence time. Stacked bars separate the chemical contribution from subsequent dissolution. The Y hybrid total is slightly below direct bioleaching, and the Cu stack has no visible additional biological component. Claims about greater extraction or significance must be element- and comparison-specific; the paper reports approach differences at its stated significance threshold only for Zn and Mn.

Methods 2.4, Figures 4-5 and Table 3 support 10 g/1 L, aerated, recirculating laboratory column observations. Similar outcomes at 40 and 80 mL/min do not demonstrate flow-rate equivalence generally. A matched abiotic column time course is not displayed. The source distinguishes culture days from 21 days of dust contact. Higher-loading clogging, including a failed 5% assay, is retained; a 20% water-flow test does not show successful culture leaching at that loading. Proposed viscosity, precipitation and permeability explanations remain hypotheses.

Table 3's source-reported percentages are retained with explicit initial-inventory qualification. Its initial Zn is 18,300 mg/kg versus Table 1's 18,000 mg/kg; prose rounds Li/Co differently, and the extracted-mass paragraph is duplicated. Summed day-21 dissolved amount is lower than day 11 while REE amounts continue to increase. Thus a generic 11-day optimum or the abstract's aggregate 39% cannot replace element-specific outcomes. No closed sampling-adjusted mass balance or isolated-metal product is established. Modeled economic discussion is not industrial deployment. No native `observations` were created because the record contract requires analysis dates that the paper does not supply.

## Other leads and next actions

1. Complete independent review of the exact new record/history bytes and correct supported findings.
2. Inspect the related 2023 [BOF dust/goethite study](https://doi.org/10.1016/j.chemosphere.2023.140244). The process-defined goethite residue may be distinct from the existing mineral record, but feed provenance and complete experimental evidence must establish that identity first. This investigation checked metadata/abstract only; no measurements from that study are accepted here.
3. The source's 2022 [UK site study](https://doi.org/10.31025/2611-4135/2022.17232) may clarify stock and adaptation history. Separate its experiments from this study before extending claims.
4. Resolve Table 1/3 inventories, missing replicate files and acid/sampling balances if further primary material becomes available.

Baseline `just check` returned zero: 308 passed, 3 skipped in 165.15 s; 169 records and 191 histories valid. The initial dependency-setup invocation failed sandbox DNS and the network-enabled retry passed. This is baseline evidence, not validation of the new record. The independent review and batch publication report will record final gates. Bounded discovery leaves many open source families; exhaustion is not established.
