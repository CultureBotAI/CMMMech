# Fluorite and inorganic-fluoride source investigation, round 61

## Scope and provenance

UTC: 2026-10-13T02:10:48.122455Z. Researcher: Codex (GPT-6; Codex), delegated source investigator. Repository base: `78ba2f4c84ff84be64b0da23e603f59c761905aa` in `/private/tmp/CMMMech-source-followups-round61-20261013`. This investigator changed no material record, history, schema, review, or Git state. After the source handoff, the coordinator began a qualified fluorine-record extension; its acceptance remains subject to a new history, validation and independent scientific review. It follows issue [187](https://github.com/CultureBotAI/CMMMech/issues/187), the round-60 mineral dossier, and the existing fluorite and fluorine records. The paired JSON pins the pre-edit source inputs at the stated base, exact searches, acquisition receipts and every retained raw artifact. It does not claim inspection of a later final record state.

**Decision:** retain the direct natural-fluorite dissolution leads as deferred. A newly acquired complete 1984 primary study supports a separate, carefully limited handoff for the **fluorine element owner**, using synthetic precipitated calcium fluoride. It must not become evidence for natural-fluorite dissolution, elemental-fluorine production, mineral-grade recovery or industrial deployment. No new criticality claim is proposed.

## Search, acquisition and deduplication

Live searches used `web.run` on 2026-10-13 UTC: exact DOI/title queries, author/institution routes, notice queries, backward references, and three image searches. Exact queries and retained returned sets are in the paired JSON; default returned result sets only, without pagination or exhaustive citation coverage. Web receipt save timestamps are actual save times, not reconstructed query times. Broad queries sometimes returned irrelevant items; those were not accepted as evidence.

Hidden and ignored files were included, with symlinks followed, in `data/records`, `research`, `reviews`, and `history` in the original checkout, the explicitly cited `/private/tmp/cmm-round60-mineral-research` downloads, and this task directory. The main text search had an 8 MB/file bound and explicit text extensions. The subsequent historical-study search included all file types recognized as text by ripgrep, with the same size bound. This is a bounded deduplication, not a machine-wide absence claim. `dedup.json` and `dedup-wainwright.json` retain commands and results. The latter found no prior match for the historical DOI/title/author in those pre-existing scientific trees or the prior cited download directory.

| Route | Evidence returned | Access conclusion |
|---|---|---|
| Muroran repository API, `q=Fluorite`, size 20 | Seven results inspected; none was the Dai study | Supported API succeeds, unlike the previous HTML query; no matching source in returned seven |
| Muroran API, `q=1654042`, size 20 | Zero hits | Bounded DOI-suffix query only |
| OpenAlex and Semantic Scholar exact DOI | Matching metadata, no full-text file link | A current index result, not proof that an author copy cannot exist elsewhere |
| ResearchGate author upload and separate figure/table pages | Original text and captions; two figures and one table identified | Local article/figure/PDF requests returned 403; graphic links failed or led to actions/login routes |
| Academic Journals original PDF via web | Three-page indexed text | Three screenshot attempts supplied no viewable image; local download was 403 HTML |
| KSU author CV | Original PDF acquired; citation visible in indexed text | Bibliographic support only; CV page layout not inspected |
| Cyberliber BMS-authorized archive | Complete original 1984 pages 289–292 as JPEG scans | HTTP works; HTTPS timed out. One partial JPEG and one timed-out wrapper retained; a single bounded retry completed them |
| Elsevier article API | Historical title, DOI, journal and date | HTTP 200 XML is metadata only, not a full article |

Raw files remain outside Git under `/private/tmp/cmm-round61-fluorite-research`. Receipt HTTP status is not an acceptance test: `.pdf` filenames containing denied HTML and the incomplete first page-290 JPEG are explicitly failed acquisitions. Complete source-page images were personally viewed; no reconstructed figures were substituted.

## Dai et al. 2019: direct natural-fluorite lead, still deferred

[DOI 10.1080/01490451.2019.1654042](https://doi.org/10.1080/01490451.2019.1654042), Geomicrobiology Journal 36, 933–939, matches Crossref. The author-upload text specifies supplier natural fluorite, ground to 0.12–0.38 mm, washed, dried and added at 20 g/L; 100 mL assays ran at 30 degrees C/120 rpm in duplicate with 2/20/200 mg/L glucose. Reported EDS Ca/F/C percentages are data-not-shown, not verified phase purity.

The cell-free comparison uses 200 mg/L glucose, so the lower-glucose arms lack matched counterparts. Abstract pH 4.8 conflicts with Results/Discussion 4.3 for the high-glucose arm. HPLC peak correlations do not identify particular acids or prove a causal enzyme. Observed solution release is not recovered product or a demonstrated groundwater flux. The original figure/table graphics remain uninspected, so these are curation questions rather than accepted measurements.

The [NCBI deposit MK691476.1](https://www.ncbi.nlm.nih.gov/nuccore/MK691476.1), freshly acquired via EFetch, independently identifies a 1,404-base partial 16S sequence from groundwater, Pseudomonas sp. strain PSB, submitted by Dai; taxon 306 is unresolved Pseudomonas sp. It is not the cited comparator P. fluorescens P35. A species or authenticated collection strain must not be substituted.

## Alharbi: 2008 bibliography strengthened, science still deferred

The [official original PDF](https://academicjournals.org/journal/AJMR/article-full-text-pdf/443D4B411559) indexed first page states November 2008, pages 319–321, accepted 15 October 2008. The author CV and official OAI listing agree with 2008. The landing's 2013 acceptance and another host's 2013 journal wrapper/2012 acceptance conflict with that original header; the derivative is not accepted as another experiment. Landing-claimed DOI `10.5897/AJMR.9000403` still returns Crossref 404, so DOI registration remains unverified.

The indexed methods name unresolved Penicillium isolates and departmental F. solani FS1/2006, use shaken 50 mL cultures at 25 degrees C for seven days, and mention uninoculated controls. Natural specimen provenance is not demonstrated. The text's subtraction direction is reversed relative to its positive-release interpretation; formula strings and a 15% Table-4 caption conflict with other loading/growth descriptions. Sporulation concentration differs between abstract and figure caption. No 2-/5-ketogluconic acid was detected, which does not exclude every acid or identify the operative mechanism. Original graphics and table typography remain uninspected; no numerical result is accepted.

## Wainwright and Supharungsun 1984: complete original, distinct synthetic-feed handoff

[Release by fungi of F− from insoluble fluorides](https://doi.org/10.1016/S0007-1536(84)80071-6), Transactions of the British Mycological Society 82(2), 289–292. Crossref verifies the title, author names and DOI; the publisher API separately corroborates the title, DOI, journal and March 1984 publication date. The retained publisher XML has no author list. All four original pages and all four tables were personally inspected from [Cyberliber page 289](http://www.cybertruffle.org.uk/cyberliber/59351/0082/002/0289.htm), following next-page links. The archive wrappers state British Mycological Society permission. Reading access does not establish redistribution rights; no raw scans should be committed. Complete article inspection found no supplement reference, but a separate exhaustive publisher supplement inventory was not available.

### Material and organism scope

Page 289 explicitly identifies the calcium-fluoride reagent as precipitated B.D.H. material. The authors call it fluorspar, but there is no natural specimen, XRD characterization or proof of an isolated fluorite mineral phase. The separately tested cryolite is also supplier material. Do not merge these with natural mineral specimens or commodity-grade products.

Fungi came from fluoride-polluted brown-earth/grassland soils near an aluminium smelter and glassworks. The named cultures include unresolved Penicillium sp. I–III and source-labeled Fusarium culmorum and F. merismoides. These labels do not authenticate an accessioned strain. Table 2 labels F. culmorum, while its nearby narrative names F. solani for the carbon comparison; retain that discrepancy rather than silently changing the organism. Use optional organism omission if no reliable experimental-stock mapping can be supplied.

### Methods, controls and observable outcome

Pages 289–290 describe Czapek Dox medium, mycelial disks from colony margins (or a yeast starter), reciprocal shaking at 100 throws/min, 25 degrees C and 14 days. Filtered culture/soil extracts were mixed 1:1 with TISAB at pH 5.8 and analyzed by a fluoride electrode. Non-inoculated controls were incubated under the same stated conditions; reported solubilization is fluoride in excess of their values. These are net aqueous-fluoride differences, not a mineral-mass dissolution yield. Biomass-associated fluoride, total mass balance and isolated-product purity were not measured.

Table 1 reports triplicate means/SD for culture-filtrate fluoride and final pH. Calcium-fluoride differences are positive for the listed fungi, while endpoint pH differs substantially from the no-inoculum control. The paper lacks matched endpoint-pH, killed-cell and spent-medium controls. It supports culture-associated mobilization but cannot establish a unique biochemical cause. Carbon and pH experiments in Table 2 show conditional effects and no-growth cells; avoid a universal optimized loading or organism-wide performance claim.

The source has unresolved dosing inconsistencies: the general Methods describe 100 mg/cm3 substrate, whereas Table 2 reports no growth at 5% and 10% CaF2 and positive activity at lower doses. Table 2's carbon series is labeled 0.3% w/v; Methods specify malt extract at 1 g/L, and the table's default glucose note is 0.1% w/v. These descriptions cannot be forced into one clean protocol. Preserve the original assay-specific statements and do not normalize yields across them.

### Soil counterevidence and mechanism limits

Pages 290–292 describe a separate triplicate autoclaved-soil experiment: 5 g initially unpolluted soil, calcium fluoride or cryolite at 50 mg/g soil, glucose addition, inoculation, approximately 45% water content and 25 degrees C incubation. Water-extractable fluoride was followed through seven weeks. Table 4 shows no positive CaF2 effect for the tested F. merismoides or Penicillium sp. I arms; inoculated means are generally below the controls. The distinct cryolite/Penicillium arm eventually exceeds its control. A culture-liquid positive result therefore does not establish mobilization in soil.

The authors discuss adsorption masking release; the study measures water-extractable fluoride, so the soil null is not proof of zero mineral reaction. Industrial use is proposed, not deployed. No gene/enzyme mechanism, mineral selectivity or usable fluorine recovery is demonstrated.

## Ranked curation handoff

1. **Handoff taken up by coordinator, acceptance pending:** add a separate fungal inorganic-fluoride-mobilization mechanism to `data/records/fluorine.yaml`, using the complete 1984 original. The coordinator chose a CaF2-only mechanism after directly viewing all four scans and reported that its baseline passed (317 tests passed, 3 skipped); that report is not an independently rerun check by this investigator. Keep the synthetic feed, unresolved stock identity, net-control denominator, dosing/organism conflicts and soil counterevidence explicit. This differs from the existing recombinant C–F cleavage mechanism. Existing fluorine identity and historical Australian criticality should remain independently sourced. Proposed fields: `sources`, `mechanisms[].context`, `mechanisms[].evidence` with support and partial entries; new actual history and independent whole-record review are mandatory before acceptance. This source assessment is not acceptance or a record review.
2. **Deferred:** obtain Dai's Figures 1–2 and Table 1 originals, then compare them with the complete indexed methods and verified deposit. Preserve its pH conflict, unmatched lower-glucose controls, unspecified mineral phase purity and laboratory-only scope. Do not close issue 187 on the strength of the older synthetic-feed study.
3. **Deferred:** obtain Alharbi's actual page images and resolve table/formula typography, controls and material provenance. Prefer the 2008 original header over the derivative wrapper while retaining the landing discrepancy and unverified DOI status.

## Limits and checks

No affecting correction/retraction notice appeared in the bounded returned title-query sets or Dai/historical-study Crossref update metadata. This is not exhaustive notice clearance; Alharbi's missing Crossref record prevents that metadata check. No author contact, purchase, login or access-control bypass occurred. No record/schema validation is claimed, because this investigator did not alter records. The JSON was parsed and every pinned local artifact was rehashed when finalized. Parent-coordinated curation, validation, scientific review and publication are separate subsequent actions.
