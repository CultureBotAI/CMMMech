# Source routes and query examples

These are discovery routes, not an exhaustive catalogue or imported datasets.
Choose the routes relevant to the research question and recheck availability,
editions, terms and scope during each investigation. An entry point's existence
does not establish that its underlying files have been acquired or reviewed.

## Official entry points

| Research need | Entry point | What to inspect and what it cannot establish |
|---|---|---|
| US criticality | [GovInfo example: 2025 final list](https://www.govinfo.gov/app/details/FR-2025-11-07/2025-19813) | Resolve the requested edition and check for later notices when making a current-status claim. This dated example is not a permanently current list. |
| Commodity/resource statistics | [USGS Mineral Commodity Summaries](https://www.usgs.gov/centers/national-minerals-information-center/mineral-commodity-summaries) | Annual chapters, data releases, units and reporting revisions. A chapter is resource/commodity context, not proof of criticality or microbial recovery. |
| EU criticality | [EUR-Lex Regulation 2024/1252](https://eur-lex.europa.eu/eli/reg/2024/1252/oj/eng) | Original Annex I strategic and Annex II critical materials; inspect amendments/consolidated versions as the task requires. Preserve material groups and grade qualifiers. A search snippet is not inspection of the complete annex. |
| Element/chemical identity | [ChEBI](https://www.ebi.ac.uk/chebi/) | Resolve labels and the exact chemical entity. Atoms, ions and substances are distinct; an element identifier does not identify its ore or waste stream. |
| Mineral identity and analytical data | [RRUFF](https://www.rruff.net/) | Mineral names/IMA information, specimen chemistry, spectra, diffraction and primary references. Keep mineral species, sample identifier and measured composition distinct. |
| Primary mechanism literature | [PubMed](https://pubmed.ncbi.nlm.nih.gov/) and the primary publisher | Follow full text, associated datasets and supplements. PubMed has a life-sciences focus; also search materials, mining and hydrometallurgy literature through web/publisher searches. Indexing is not verification of experimental claims. |
| Taxon/sample/genome context | [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/datasets/taxonomy/), [BioSample](https://www.ncbi.nlm.nih.gov/biosample/), [Datasets documentation](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/) | Inspect rank, sample provenance and accession-versioned genomes/linked sequence archives. These identify different objects; annotations or sequence similarity alone do not demonstrate recovery. |
| Strain context | [BacDive](https://bacdive.dsmz.de/) and the cited culture collection | Follow strain identifiers and observation provenance. Separate measured, predicted and species-level properties; verify the exact experimental strain. |
| Study datasets and supplements | [BioStudies](https://www.ebi.ac.uk/biostudies/about) and repositories linked by the original paper | Inspect study accession, file identity, release/version, license and representative rows. Deposited files may reuse published observations rather than add independent experiments. |

The list is not restricted to the US or EU. For another jurisdiction, locate its
issuing ministry/geological survey and the actual designated list or legal
instrument. For waste inventories, geological occurrences, tailings, process
data or broader repositories, start from the originating agency or primary
study's data-availability statement. Verify the particular dataset rather than
treating a generic portal as evidence.

Entry-point check: 2026-10-07 session. ChEBI, current RRUFF, PubMed, the listed
NCBI routes, BacDive, BioStudies and the GovInfo example were opened. USGS content
and the EUR-Lex document identity were checked through official indexed results
after timeout/JavaScript access limits. Their complete data/annex contents were
not assessed in that check. Legacy `rruff.info/ima/` returned a redirect loop;
use the current entry point and verify any redirected target.

## Build queries around claims

Substitute verified names/synonyms; adapt syntax to the search provider. These
are examples, not searches already performed or evidence that a source exists.

- Criticality: material/group + jurisdiction + `critical minerals` or
  `critical raw materials` + requested edition + official authority domain.
- Extraction: material/mineral + `bioleaching` or `microbial dissolution` +
  ore, tailings, black mass, slag or the exact resource.
- Transformation/recovery: material/ion + `biosorption`, `biomineralization`,
  `bioprecipitation`, `reduction`, `oxidation` or `bioaccumulation` + strain,
  biomass state or substrate. Classify actual microbial involvement separately.
- Data acquisition: exact paper title or DOI + `supplementary`, `dataset`,
  `data availability`, `correction` or `retraction`; follow deposited accessions.
- Counterevidence: exact system/material + `abiotic control`, `precipitation`,
  `inhibition`, `no effect`, `selectivity` or `mass balance`, chosen to challenge
  the proposed claim. Search broader conflicting studies as appropriate.

Include relevant organism and material synonyms without silently merging their
identities. Search backwards through references and forwards through citing
experiments when it can close a specific evidence gap. A lack of hits for one
spelling or provider is a search limit, not evidence that a mechanism is absent.
