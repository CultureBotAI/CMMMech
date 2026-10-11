# Round 27 packaging and layered-metal source investigation

UTC investigation: 2026-10-11T16:15:07.492579Z. Researcher: Codex (GPT-6). Worktree
`/private/tmp/CMMMech-expansion-round27-20261011`, branch
`curate/cmm-expansion-round27-20261011`, trusted base
`3f1350b24b4f6248ed2e17caade936c15af9be93`. This report records author research
and a curation handoff; independent scientific review is a separate artifact.
Concurrent work concerns other steel and industrial resources.

## Scope and novelty

The starting corpus contained 169 records. This pass resumed the Round 26
beverage-can access gap, then followed the layered-material recycling literature
to defective electroformed Cu/Ag tubes. The latter is a manufacturing-derived
secondary resource with a defined production route, not a synonym for copper,
silver, printed circuit boards, electroplating sludge or multilayer packaging.
No criticality claim is asserted: a source calling metals valuable does not
establish jurisdiction, list or edition for their host waste.

Before curation, exact DOI and electroform/electrodeposition searches using
`rg --no-ignore --hidden --follow` covered this worktree's records, research
and reviews, the original checkout's records, and the referenced Round 26
packaging raw directory. A subsequent expanded search covered records,
history, research and reviews in both checkouts plus that raw directory; its
only hits were this newly created record and history. The hit-path receipt is
`/private/tmp/cmm-round27-packaging-dedup-paths.txt`. Hidden and ignored files
and relevant symlinks were included. Other worktrees, unrelated home directories
and unrelated temporary downloads were not searched. This establishes novelty
within those curated-source bounds, not absence everywhere.

## Search and acquisition

The companion JSON lists exact search queries, public-route attempts, UTC times,
content checks and hashes. Web queries covered exact beverage-can title/DOI,
author thesis/repository routes, full text and supplements, the newly discovered
electroformed-tube DOI, controls, CF3 taxonomy and corrections/retractions. Only
returned first result pages were examined; references were screened for relevant
scope, not exhaustively followed. No author was contacted or authentication used.

| Candidate and canonical version | Evidence inspected | Decision |
|---|---|---|
| [Kremser et al., Waste Management 120:16-24, DOI 10.1016/j.wasman.2020.11.012](https://doi.org/10.1016/j.wasman.2020.11.012), 2021 issue | Prior abstract/metadata dossier, current Genoa repository page and Elsevier API response | Continue to defer beverage cans: repository labels its PDF closed access; API returns metadata only with `openaccess=0` |
| [Pakostova and Herath, Sustainability 15:14068, DOI 10.3390/su151914068](https://doi.org/10.3390/su151914068), published 22 September 2023 | Complete 18-page publisher PDF text, rendered main Figures 1-8, Table 1 and equations; Crossref metadata | Curate scoped manufacturing-scrap record; missing supplementary images remain explicit |
| [NCBI Taxonomy 3063951](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=3063951&mode=Info) and [BioSample SAMN14556242](https://www.ncbi.nlm.nih.gov/biosample/SAMN14556242) | Current names, species rank, CF3/type-strain links and sample attributes | Taxonomic context; not authentication of the experimental stock or consortium sequencing |

Publisher landing/XML and Coventry direct downloads failed with 403/429, but the
public MDPI CDN supplied a real 10,875,623-byte PDF with matching title, authors,
DOI and 18 pages. No binary from a challenge page was accepted as full text.
The main PDF states CC BY 4.0, corroborated by Crossref's version-of-record
licence. It remains outside Git despite that licence. The repository PDF mirror
was not substituted with ResearchGate's indexed pre-publication rendering.
The public supplement landing route failed and bounded plausible CDN filename
routes returned 403/404; these guessed filenames do not establish which binary
format exists. Figures S1-S4 were not acquired or visually inspected. Their
captions in the main PDF identify the missing material: fabrication/apparatus
photos and abiotic-residue microscopy. No required claim is based solely on an
unseen figure. Initial sandbox DNS failures are distinguished from actual
network responses in the receipts.

Crossref's live record has no `update-to` or `updated-by` value and an empty
relation object. Exact-DOI amendment searches did not return a correction or
retraction notice on the inspected result pages. This bounded negative result
is not a universal absence claim. The broader electroformed-bioleaching-control
query returned this original study and contextual literature, without a
verified independent replication for this precise scrap. Unsearched citations
may contain additional evidence.

## Primary evidence and scientific boundaries

Methods 2.1 and Figure 1 establish defective manufactured tubes, approximately
500 micrometre Cu walls and 24-30 micrometre inner Ag coating from painted wax
mandrels. The Discussion's 94.4/5.6 wt.% feed composition is retained as reported,
not treated as an independently reconstructed bulk digest. Material identity
supports `secondary_resource` without a waste-specific external ontology ID.

Methods 2.2-2.3 and Table 1 define a CF3 pure culture, ten-member starting
consortium and adapted mixed inoculum in different vessels. Acid and Fe(II)
medium, pre-growth, ethanol treatment, loading, pH control, leachate replacement
and temperature are retained in the record. Section 2.3 and the S2 caption give
220 rpm for flasks, while Figures 2-3 captions say 130 rpm; the abstract's 22°C
and Methods' approximately 23°C also differ. These discrepancies are not
silently reconciled. The abiotic control was 25-28°C and not a matched reactor
or maintained-ferric comparator. No independent vessel replication or formal
statistical comparison is described; time-course samples and redox-reading
n values cannot establish biological replicate counts.

Results 3.1-3.3 and Figures 2-4 support culture-associated solubilization and
Fe cycling. CF3's plateau near 42% and response to fresh medium are observations;
specific Cu inhibition is the authors' inference. The CF3 endpoint is 94.7% in
the abstract and 95.2% in Results. The mixed flask reports 99.2% over 59 leaching
days and the adapted reactor 99.6% over 12 leaching days; pre-growth occurs
before those intervals. Changes in temperature, air supply and inoculum history
co-occur, so faster kinetics do not isolate any one cause. Main-text assays and
Figure 2 contain the 5.3% abiotic Cu result over 75 days, independently of inaccessible
S4 microscopy.

CF3 is called A. ferrooxidans and parenthetically ferruginosis by the leaching
paper. Current NCBI assigns species 3063951 and CF3 BioSample SAMN14556242 to
A. ferruginosus (an effective name). The record gives the current species CURIE
as context for CF3, preserves historical paper naming and does not infer that
a deposited genome authenticates this laboratory stock. Genus-level sequence
proportions and culture isolates do not identify the causal contribution of
individual community members. Results 3.3's final Leptospirillum 50.0% differs
from the abstract's 59%; the discrepancy remains unresolved and no exact
independent percentage is extracted from Figure 5. Raw amplicon accessions are not stated in the
inspected main article; its data statement says sharing is not applicable.

Chemical Fe precipitation and electrochemical Cu deposition form a second,
nonmicrobial mechanism. Methods 2.4, Results 3.4 and Figure 6 directly document
unamended versus pH-raised/filtered liquors. The crucial 6-19% Cu co-precipitation
loss occurs before the reported near-complete electrowinning step. The latter
is measured from remaining solution and is not a whole-scrap recovery yield.
Current efficiency is a separate metric. Results alternate thresholds above 99,
99.9 and 99.99%; this record uses approximate near-complete recovery without
inventing precision or a complete mass balance. Figure 8's deposition on an
existing Cu foil and local EDS 98.5-99.9% do not establish net recovered bulk
mass, certified purity or return-to-manufacture performance. The Ag-rich residue
has local EDS 92.6% Ag, 7.2% Cu, 0.2% Fe and lacks a whole-feed Ag-yield balance.
No claim of microbial Ag reduction follows. No industrial operation, complete
process life-cycle assessment or demonstrated economic advantage is established.

There is no reusable numeric source-cell dataset within the current observation
contract: reported percentages, mg/L or g/L and graph time series are not
source-table mg/kg cells with analysis dates. Qualified prose uses existing
schema fields; no schema/validator/importer change is proposed.

## Handoff and remaining priorities

The new [electroformed copper-silver manufacturing scrap record](../../data/records/electroformed-copper-silver-manufacturing-scrap.yaml)
contains the bounded observations above and native CREATE and corrective EDIT
history sidecars.
Named-record validation, trusted-base history checks and final batch results
are recorded in the companion JSON. Independent acceptance is saved in the
successor review linked below; this author report is not that verdict.

1. Obtain the exact publisher supplement to inspect S1-S4. It may refine
   apparatus/abiotic-residue interpretation; do not infer its contents now.
2. Obtain complete primary beverage-can methods, controls, figures and supplement
   before importing its abstract's high leaching/precipitation claims.
3. Existing [carton hydropulping reject](../../data/records/beverage-carton-hydropulping-reject.yaml)
   remains a same-resource follow-up for DOI 10.1016/j.wasman.2025.114913, not
   a new material merely because the acid differs. That full paper was not
   acquired in this pass. The electroformed-paper references to PCB recovery
   are further evidence leads for already represented feed families, not
   automatically distinct records.

The search frontier remains open. Missing full text and uninspected source
families prevent any claim that no further CMM identities exist.

## Independent-review correction

At 2026-10-11T16:22:11.028471Z, independent review F1 (`CMMMech.electroformed-scrap-leptospirillum-figure-direction`) identified that the record incorrectly called Figure 5 consistent with Results 50.0%. The final Leptospirillum segment is visually closer to the abstract's 59%, but it does not supply an independent exact percentage. The corrected record retains the 59% versus 50.0% discrepancy without adjudicating it from the graph. The initial native review is `reviews/structured/20261011T161956Z-electroformed-copper-silver-manufacturing-scrap-round27-independent-initial/review.yaml`; the appended EDIT is `history/records/electroformed-copper-silver-manufacturing-scrap/2026-10-11T162139Z-codex-98721d.yaml`. Initial record SHA256 `5f2c0602ef2d7d079d467e130cbc8c43e6b38a882b2071c6a69ac4306ac2c239`; corrected record SHA256 `cd4c7e284b4ad47079d0c609db007795f1aeeb28dcdf7cf359d2a32b52b1ea62`. At correction time, successor independent review and final batch checks remained pending; their completed results are recorded below.

Corrected-record validation completed with exit 0 (1 checked, 0 failed); trusted-base history validation completed with exit 0 (195 checked, 0 errors). These structural checks are separate from scientific acceptance.

The final corrected batch completed successfully: `just check` passed 308 tests (3 skipped), 171 records and 195 histories; `validate --require-records` checked 171 with 0 failed; trusted-base history validation checked 195 with 0 errors. The coordinator receipt `/private/tmp/cmm-round27-final-terminal.json` and all three logs were independently read and checksummed. The corrected record hash remained unchanged. Scientific acceptance is recorded separately by the independent reviewer.

Independent successor review completed as `pass_with_limitations`: `reviews/structured/20261011T162619Z-electroformed-copper-silver-manufacturing-scrap-round27-independent-resolution/review.yaml` (with generated `review.md`). It explicitly resolves the previous F1 occurrence against the corrected frozen record hash. The retained limitations, including inaccessible supplementary figures, confounded comparisons, stage losses and local EDS, remain part of acceptance.
