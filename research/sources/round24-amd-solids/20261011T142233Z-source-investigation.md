# CMM source investigation: AMD solids and remaining identity frontier

## Scope and provenance

UTC 2026-10-11T14:22:33.131628+00:00; codex (GPT-6), source investigator and curator `round24_identity_frontier`. Checkout `/private/tmp/CMMMech-expansion-round24-20261011`, branch `curate/cmm-expansion-round24-20261011`, base `d7183efeb2e528d6d88f0b69da41323642b8fa85`. All 156 baseline records were inventoried. Curation began after the baseline passed (308 tests, 3 skipped). Other agents own catalyst, slag and NiMH files. This bounded survey seeks distinct material identities beyond those assignments. It is not a global exhaustion test, comprehensive mineral nomenclature survey or criticality-list refresh.

## Search and acquisition log

Provider `web.run`, 2026-10-11 UTC, first returned result sets only; no date/domain filters or pagination. Exact queries:

- `bioleaching "acid mine drainage sludge" rare earth full text`
- `bioleaching "steel slag" bacteria full text`
- `bioleaching "electric arc furnace dust" full text`
- `bioleaching "oil fly ash" vanadium nickel full text`
- `"bioleaching" "mine drainage sludge" rare earth`
- `"bioleaching" "acid mine drainage" "precipitates" rare earth`
- `"bioleaching" "oil fly ash" Rastegar`
- `"bioleaching" "samarium cobalt" magnets`
- `"Bioleaching Rare Earth Elements from Abandoned Coal Mine Drainage" correction retraction`
- `"Bioleaching of an oil-fired residual" optimization`
- `"fuel oil ash" "Penicillium simplicissimum" 2016`
- `"bioleaching" "steel slag" "10.1016/j.chemosphere.2014.09.089" pdf`
- `site:mdpi.com/2075-163X/16/9/930 "2. Materials" "Al"`
- `"Bioleaching Rare Earth Elements from Abandoned" pdf`
- `"Low residual dissolved phosphate" bioleaching batteries pdf`
- `"Bioleaching" "casthouse dust" Frueholz 109859`
- `"Bioleaching Rare Earth Elements from Abandoned Coal Mine Drainage" "2.1"`
- `"Bioleaching Rare Earth Elements from Abandoned Coal Mine Drainage" "Methods"`
- `"Bioleaching" "casthouse dust" "2025"`
- `"spent nickel-metal-hydride" bioleaching "10.1016/j.mineng.2021.107361" correction`
- `"Bioleaching" "spent NiMH" "2026" "Comprehensive characterization"`
- `"Bioleaching" "blast furnace casthouse dust"`
- `"Bioleaching Rare Earth Elements from Abandoned" Vietmeier "930" doi`
- `"Bacillus mycoides" "JR07" genome`
- `"Bacillus pseudomycoides" "KB7" genome`
- `"10.3390/min16090930" correction retraction`
- `"10.21203/rs.3.rs-9065662"`
- `site:ncbi.nlm.nih.gov Taxonomy "Bacillus mycoides" "1405"`
- `site:ncbi.nlm.nih.gov Taxonomy "Bacillus pseudomycoides" "614"`
- `"Bioleaching Rare Earth Elements from Abandoned Coal Mine Drainage" correction retraction erratum`
- `site:ncbi.nlm.nih.gov/Taxonomy "Bacillus pseudomycoides" "Taxonomy ID"`


Acquisition URLs, UTC timestamps, file types, sizes, SHA256 values and failed routes are in the [paired JSON](../../../research/ingests/round24-amd-solids-sources-20261011.json). Initial network-sandbox DNS failures differ from actual publisher 403/429 responses. Public downloads acquired the AMD main PDF, supplement and institutional cast-house-dust PDF. The NiMH institutional route returned an HTTP 200 HTML challenge, not a PDF. After the linked supplement landing failed, three conventional publisher file-extension routes were checked: ZIP succeeded; PDF and DOCX returned 404. No access control was bypassed and no author was contacted.

## Selected primary study

The [AMD solids dossier](../../../research/ingests/round24-amd-solids-sources-20261011.md) grounds the resource's treatment origin and records Methods 2.1–2.5, Figures 1–7, Table S1 control comparisons, source contradictions, taxon resolution and quantitative-import limits. Main article and supplement belong to one experiment family. Every figure and both supplementary tables were visually checked. The resource fits the existing `secondary_resource` and `bioleaching` contract with qualified prose. No criticality claim or schema change is needed. The dossier is separate from the required independent scientific review.

## Ranked remaining material identities

1. **Blast-furnace cast-house dust**, DOI [10.1016/j.bej.2025.109859](https://doi.org/10.1016/j.bej.2025.109859), Frueholz et al., *Biochemical Engineering Journal* 222:109859, available 8 July 2025. The fresh 10-page primary PDF from [K1-MET](https://www.k1-met.com/fileadmin/user_upload/Publications/Journal_articles_open_access/Frueholz_et_al__2025__Bioleaching_BF_casthouse_dust_BiochemEngJ_paper_109859.pdf) is 2,962,264 bytes, SHA256 `569ccc49d1455b33e335e32623a88f8ab2fa5c42cde446efaa7ba12f395e2d25`. Title, introduction and Methods 2.1–2.5 were inspected: iron-tapping dust supplied by an Austrian steelmaker, 3 L fed-batch *A. thiooxidans* experiments, an abiotic-medium test, partial inoculum retention and feed increments. Dust differs from slag and flotation tailings. Next inspect all figures, assay comparability, reference 9 feed characterization, cycle inventories and supplement. No abstract yield is accepted here. Reuse terms remain to be checked; the raw PDF stays outside Git.
2. **Heavy-fuel-oil fly ash**, DOI [10.1039/C5RA00128E](https://pubs.rsc.org/en/content/articlelanding/2015/ra/c5ra00128e), plus 10.1016/j.wasman.2016.04.004 and 10.1039/C5RA24870A. The RSC primary title and abstract were verified; other citations were traced from a review. Full primary methods and figures have not been acquired. The combustion feed differs from coal ash and spent refinery catalysts. Next acquire full evidence and validate proposed downstream product accounting, beyond solution release alone.
3. **Electric-arc-furnace steel slag**, DOI [10.1016/j.chemosphere.2014.09.089](https://doi.org/10.1016/j.chemosphere.2014.09.089), Hocheng, Su and Jadhav (2014). PubMed metadata, abstract and publisher preview were inspected; the author page offers a PDF request only. Water washing and supernatant leaching remain leads, requiring full methods, controls and serial-cycle evidence. Other steel/EAF studies use wastes as neutralizers during gold biooxidation; that role does not prove recovery from the neutralizers.
4. **Spent NiMH batteries**, DOI 10.1016/j.mineng.2021.107361, is an existing deferred source with no baseline material root. Indexed institutional methods and the 2026 primary PMC study, DOI 10.1039/d6ra03345h, were found and handed to the root author for round24 curation. This agent did not duplicate that work. The local institutional download was an HTML challenge.
5. **SmCo magnets and EAF dust** remain bounded leads. Searches returned chemical processes, secondary references or a neutralization role, without a fully assessed microbial extraction experiment. No absence-of-evidence claim is made.

## Duplicates, limitations and handoff

Municipal-waste incineration ash, sewage-sludge incineration ash and coal fly ash already have distinct accepted roots. Further assays belong in the applicable root unless a different material identity is scientifically grounded; locality alone is insufficient. Baseline absence searches included hidden and ignored files and followed links in `data`, `research`, `reviews` and `history`. Initial/final duplicate logs and the 156-record hash inventory remain outside Git. No matching cast-house-dust, fuel-oil-ash or EAF-slag root or cited DOI was found within those boundaries before writing this report.

Cast-house dust has accessible primary full text, so the active goal is not exhausted. This report is a discovery handoff, not acceptance or an independent record review. Access does not replace causal assessment, native validation or review of final hashes. Unsearched scope includes complete citation networks, every ore and mineral species, all jurisdictional commodity lists and global industrial waste streams. Bulk reuse requires its own terms check. Earlier source frontiers remain live.
