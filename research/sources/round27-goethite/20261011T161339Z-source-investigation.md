# CMM source investigation: industrial goethite byproduct

## Scope and provenance

- UTC: 2026-10-11T16:13:39.477166+00:00. Researcher: Codex (GPT-6; round27_superalloy).
- Base `3f1350b24b4f6248ed2e17caade936c15af9be93`; branch `curate/cmm-expansion-round27-20261011`. Parent baseline passed: 308 tests, 3 skipped, 169 records and 191 histories. This report adds no record/history.
- Assess a potentially distinct industrial residue in [Tezyapar Kara et al. 2023](https://doi.org/10.1016/j.chemosphere.2023.140244). Existing mineral [goethite](../../../data/records/goethite.yaml) remains distinct; zinc-processing origin has **not** been established and is not accepted as a root identity.
- Hidden/ignored-inclusive, symlink-following deduplication covered worktree records/research/reviews/history, original-checkout records/research and relevant round26/27 raw directories. DOI, PII, PMID and byproduct terms found no existing accepted resource root in these boundaries. Exact command/output: `/private/tmp/cmm-round27-goethite-raw/dedup-receipt.json` and `dedup.txt`. Unrelated home/temp trees excluded.

## Search and acquisition log

Exact queries and receipts are in the paired JSON; first result sets only, no pagination. Most narrowly targeted methods queries returned irrelevant results and did not establish full-text inspection.

| Route | Result | Actual inspected content |
|---|---|---|
| [PubMed 37758076](https://pubmed.ncbi.nlm.nih.gov/37758076/) | Readable | Bibliography/abstract only |
| [Publisher](https://www.sciencedirect.com/science/article/pii/S0045653523025146) | Direct access 403; web open failed | Indexed selected Introduction/Results and Table 2, not complete Methods |
| [Elsevier metadata API](https://api.elsevier.com/content/article/pii/S0045653523025146?httpAccept=text/xml) | 200, 2068 bytes | Metadata only despite full-text wrapper; FULL request 401 |
| [Cranfield repository file](https://dspace.lib.cranfield.ac.uk/bitstreams/fc26b4f7-008c-42c1-bd0c-035f9d210fea/download) | 403; web displayed access denial | No PDF; no challenge bypass |
| [Original supplement](https://ars.els-cdn.com/content/image/1-s2.0-S0045653523025146-mmc1.docx) | 200, valid DOCX ZIP, 1035272 bytes | Tables S1–S4, all figure captions and original XRD image panels S2a/b |
| [Thesis lead](https://dspace.lib.cranfield.ac.uk/handle/1826/22526) | Located via Cranfield-contributed AGRIS record | Bibliographic route only, no thesis acquired |
| Browser | No available browser | No authenticated/browser content accessed |

The supplement PDF filename candidate returned 404; this does not imply absence of other supplements. OpenAlex's purported PDF URL is actually a graphical-abstract JPG, an acquisition metadata error; it was not counted as a full article. Its repository location resolved to the denied Cranfield bitstream. The supplementary file is the substantive new evidence obtained here.

## Candidate inventory

| Candidate | Stable identifier/version | Role and access | Decision |
|---|---|---|---|
| Tezyapar Kara, Simmons, Wagland and Coulon, 2023 | [10.1016/j.chemosphere.2023.140244](https://doi.org/10.1016/j.chemosphere.2023.140244), Chemosphere 343, 140244; online 25 September, December issue | Primary experiment; original supplement acquired, main incomplete | Defer goethite-resource curation pending identity and control checks |
| Tezyapar Kara PhD, Assessing resource recovery potentials of industrial metal-bearing by-products using bioleaching | [Cranfield handle 1826/22526](https://dspace.lib.cranfield.ac.uk/handle/1826/22526), 2023 | Potential expanded methods for same research programme | Acquire, then check study overlap; not independent replication |

## Source assessments

The publisher metadata API verifies DOI/title, open-access status and CC BY 4.0; PubMed verifies authors and date. OpenAlex describes the Cranfield item as submittedVersion, which must be checked against the actual PDF before treating it as the VoR. Crossref/Elsevier metadata and the article supplement describe one experiment, not independent confirmations.

The original supplement materially sharpens the evidence gaps:

- Table S1 gives non-autoclaved goethite copper as 23600 mg/kg and a -16% autoclaving difference. Indexed main Table 2 gives 203667 mg/kg for autoclaved goethite. These do not reconcile. A decimal/extra-zero error is possible, but no value is corrected here; original main table layout and author data are needed.
- Table S3 says n=3 for goethite extraction, whereas Figures S4/S5 captions say n=2. Replication basis remains unresolved.
- Original Figure S2b legend lists magnetite, lautite, zinc titanium oxide, corkite, ammonium hydrogen aluminium phosphate hydrate and adamantyl methanol; it does not label goethite. This does not identify the byproduct as a pure mineral or verify those phase assignments. The source name, process provenance and mixed phase identity require adjudication together.
- Tables S3/S4 and captions define the selected condition as 1% solid, 4% energy source, 10% inoculum and pH 2. Reported extraction percentages, including ceiling values, are unaccepted until the full methods, denominator, sterile controls, acid additions, sampling and source conflicts are checked. Acid-consumption Figure S3 is present; it is not a complete acid-matched causal control.

No original main figures, complete methods, full experiment-specific culture accession or substrate origin were obtained. No strain identifier, criticality designation, measured observation, isolated-product yield or industrial deployment claim enters the corpus. Chemical headings such as “critical metals” in an experimental table lack jurisdiction/list/edition. The narrow DOI correction search found no relevant notice in first results, but the full version/correction inventory remains unchecked.

The supplement text/tables and the two embedded XRD image panels were inspected. Other figures are embedded charts: their captions were read, but charts were not fully rendered/adjudicated. No raw replicate dataset or complete data dictionary was verified. Zero, dash and below-LOD cells must remain distinct; no conversions or censoring interpretation were entered as observations. Article CC BY 4.0 is verified by the publisher API; detailed supplement-specific license text was not separately established. Bulk source artifacts remain outside Git.

Retained supplement: `/private/tmp/cmm-round27-goethite-raw/supplement.docx`, acquired 2026-10-11T16:11:36.921888+00:00, SHA256 `da1022aa0345428a306c80cfb4819bddd4bb68b08e1e3a4302033982b004212b`. All metadata, extracted text/images and receipts have checksums in the paired JSON.

## Priorities and handoff

1. Obtain the Cranfield manuscript or primary main PDF through a functioning public route; use the thesis as a possible methods source after checking experiment overlap.
2. Establish the industrial feed's process/site identity, distinguish it from goethite mineral, and resolve composition/replicate conflicts with original tables and controls.
3. Inspect all supplementary charts and the primary experiment's acid additions, sterile comparisons, analytical recovery, limits and statistical model. Curate only supported resource-specific claims, preserving source uncertainty; independent review is still required.

## Limits and unresolved questions

The new supplementary acquisition is progress, but it does not close the main-paper and material-identity gaps. No speculative root or canonical history was created. JSON parsing, raw checksums and relative links were checked; this is a research deferral, not an accepted scientific record review. Source discovery remains open.
