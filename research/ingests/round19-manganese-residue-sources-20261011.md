# Round 19: electrolytic manganese residue source assessment

## Scope and provenance

UTC 2026-10-11T11:41:57.645062+00:00; codex, GPT-6, Codex. Trusted base
`c4b2a6c21a2ff54d1fdd3965ac98a6d90effba7a`, branch
`curate/cmm-expansion-round19-20261011`. This lane follows the round18 Xin2011
handoff and curates one process-defined secondary resource. It does not inherit
criticality from manganese or duplicate manufactured EMM/EMD commodities.

The pre-write search included hidden and ignored files and followed symlinks in
`data/records`, `research`, `reviews`, `history`, and the named round18 product and
catalyst raw directories. Five matches were prior Xin research proposals; no
existing record matched in these boundaries. Binary PDFs were separately read.
The exact command, result checksum, inventory, queries and acquisition ledger are
in the paired JSON. No wider absence claim is made.

## Search and acquisition log

Twenty exact queries used web search on 2026-10-11, first returned sets only.
Queries pursued original full text, author repositories, identifiers, supplements,
corrections and conflicting/abiotic outcomes. Direct downloads have actual UTC
acquisition times and SHA-256 values in JSON. Two initial local script attempts
failed before networking because `requests` was unavailable; standard-library
networking then completed. HTTP200 was not equated with full-text access.

## Candidate inventory and evidence checked

- **Cao2012, curate with limits:** [original DOI](https://doi.org/10.1080/09593330.2011.624125),
  complete seven-page publisher PDF from the authors' [Hunan University site](https://ee.hnu.edu.cn/__local/D/CA/5B/3875F1EB59A4CC26685E4ABB867_ABC9F11B_6B8C6.pdf?e=.pdf).
  All six article pages read; PDF3-6 visually checked, including all six figures.
  Section2.1 grounds the disposal-dam feed; Sections2.4/3.2 and Figures2-4 establish
  culture-associated solution Mn with a lower, nonzero no-inoculum comparator.
  Reported percent is a medium/feed mass ratio, not an isolated-product yield.
  Late decline and pH changes matter; no pH-trajectory-matched abiotic comparison
  supports a stronger acid-specific causal claim. Organic acids are an explicit
  untested hypothesis. Loading and pretreatment remain insufficiently described.
  Operational BCR fractions are not mineral species or proof of complete mass
  balance. Source economic/environmental assertions are not measured deployment.
- **Identity conflict, preserve:** [FJ532369.1](https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=FJ532369.1&db=nuccore&report=genbank&retmode=text)
  actually names CJB1/partial28S; the paper calls J62/26S and later16S. The root
  uses [Fusarium genus5506](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=5506&mode=Info)
  only. No inferred species or J62=CJB1 equivalence is accepted. The paper also
  has an ambiguous inoculum mass basis and a pH-range prose/figure disagreement.
- **Xin2011, still deferred:** [original DOI](https://doi.org/10.1016/j.biortech.2010.09.107).
  Publisher snippets and bibliographic identity checked, but the direct publisher
  request failed403. OpenAlex supplied no OA route. The public publisher API
  returned core metadata only. Its sulfur/pyrite/serial-treatment outcomes cannot
  enter a mechanism without the missing methods, figures and controls.
- **Lan2019, deferred:** [original DOI](https://doi.org/10.1016/j.jclepro.2019.03.098),
  [HKU metadata](https://hub.hku.hk/handle/10722/365597). The repository explicitly
  links subscribed full text; publisher API metadata is not a manuscript. Obtain
  Y1 identity and assay/product evidence before accepting the abstract's recovery
  or double-salt claims.
- **Zhao2023, high-priority follow-up:** [original DOI](https://doi.org/10.1016/j.jhazmat.2022.130662),
  [PubMed36587595](https://pubmed.ncbi.nlm.nih.gov/36587595/). Full paper and SI are
  needed for strain Z6-5-1, acid/biosorption tests and PoxCxrE perturbation claims.
  A university-domain PDF search returned a citing paper; it did not close access.

## Known-source changes, reuse and mapping

The original Xin access gap persists; Cao is an additional primary study on the
same material family, not a new identity per treatment. No bulk dataset was
acquired. Figure-derived or undated concentrations do not meet the numeric-table
observation contract, so no structured concentration cells were generated.
Accepted fields are `description`, `sources`, and a qualified `bioleaching`
mechanism with verified genus context. Existing schema suffices.

Cao's PDF cover restricts redistribution; raw full text and renderings remain in
`/private/tmp/cmm-round19-manganese-residue-raw`, outside Git. NCBI metadata and
source-specific license uncertainties are identified in JSON. Reading access is
not treated as permission for bulk reuse. The accepted-version online date,
version-of-record date, issue date and this download date remain separate.

## Priorities and handoff

1. Independently review `data/records/electrolytic-manganese-residue.yaml`, checking
   the controls, taxonomy conflict and missing loading against the retained PDF.
2. Acquire Zhao2023 main/SI to test the acid hypothesis and possible regulatory
   evidence using an independently characterized strain.
3. Acquire Xin2011 main/figures and Lan2019 main/SI to assess serial leaching and
   actual downstream product recovery, respectively; extend this root if supported.

## Limits and unresolved questions

Exact DOI/title correction searches and Crossref updates returned no specific
notice in inspected results, which is a bounded negative. No supplement was
located for Cao in the inspected article/indexed publisher material and query;
blocked live publisher access prevents a comprehensive supplement absence claim.
No author contact or access-control bypass was used. This lane is not an
exhaustive manganese or CMM survey. Independent scientific review remains a
separate acceptance step. Individual validation is recorded in the paired JSON
when its actual terminal result is available.
