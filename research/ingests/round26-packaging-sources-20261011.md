# Round 26 packaging source investigation

UTC investigation: 2026-10-11T15:35:42Z. Researcher: Codex, GPT-6. Worktree:
`/private/tmp/CMMMech-expansion-round26-20261011`, trusted base
`d20fc229fe61a08e36a2889d89e0f4ce7c06c4a9`. This is an author research handoff,
not scientific acceptance. Independent record reviews are separate artifacts.
Branch: `curate/cmm-expansion-round26-20261011`; working changes include these
two packaging records/history plus concurrent steel-resource author work.

The two supported additions are hospital-derived pharmaceutical blister waste
and the reject left after hydropulping beverage cartons. These identities follow
different manufactured feeds and processing histories. Neither is aluminium as
an element, a beverage can, the sulfur used to make acid, or an isolated polymer
product. No jurisdictional criticality claim is made or inherited.

## Coverage and search provenance

The starting corpus contained 165 records. An inventory during concurrent work
contained 166 records, including a teammate's new EAF-dust draft; its complete
ID/name list is retained outside Git. Searches used `rg --no-ignore --hidden
--follow` across `data/records`, `history`, `research`, `reviews` and the relevant
Round 25 raw frontier directory. Exact DOI and packaging-name searches found
six repository handoff/publication files and no pre-existing packaging record
root within those bounds. Adjacent aluminium, alumina, high-purity alumina and
biogas-desulfurization sulfur records were distinguished from the proposed feeds.
Hidden and ignored content and relevant symlinks were included. Unrelated home
directories, other worktrees and unrelated temporary downloads were excluded.
An accidentally overbroad, interrupted parent-directory search is not used as
completeness evidence. The companion JSON retains the bounded query inventory,
acquisition receipts and checksums; bulk papers and images stay outside Git.

Queries covered exact titles/DOIs, public PDFs, the author-upload route, the BOKU
and Genoa repositories, upstream acid-production methods, official DSMZ/NCBI
identifiers, and correction/corrigendum/retraction terms. Only returned first
result pages were inspected; no claim of comprehensive citation coverage or
global exhaustion follows. Crossref supplied no `update-to`, `updated-by` or
relation entries for the three original candidate DOIs at this check. The
bounded amendment queries did not identify a correction notice. This is an
observed search result, not proof that none exists.

## Primary-source decisions

| Source and version | Material and inspected evidence | Decision |
|---|---|---|
| [Kremser et al. 2023, DOI 10.1016/j.hydromet.2023.106124](https://doi.org/10.1016/j.hydromet.2023.106124), published journal version | All nine pages of PDF text through the author-uploaded copy, main Figures 1–5 from publisher JPEGs, complete native DOCX supplement and Figures S1–S4 | Curate [pharmaceutical blister packaging waste](../../data/records/pharmaceutical-blister-packaging-waste.yaml), with conditional acid-leaching evidence |
| [Kremser et al. 2022, DOI 10.1016/j.resconrec.2022.106444](https://doi.org/10.1016/j.resconrec.2022.106444), published journal version | Full ten-page project-hosted PDF, all six main figures, five-page publisher supplement, Table S1, acid methods and Figures S1–S2 | Curate [beverage-carton hydropulping reject](../../data/records/beverage-carton-hydropulping-reject.yaml), separating every processing stage |
| [Kremser et al. 2021, DOI 10.1016/j.wasman.2020.11.012](https://doi.org/10.1016/j.wasman.2020.11.012) | DOI metadata, abstract and repository deposit status; Genoa lists a 1.91 MB published PDF as closed | Defer beverage cans until full methods, controls, figures and supplement are obtained |
| [Kremser et al. 2022, DOI 10.1016/j.wasman.2022.03.025](https://doi.org/10.1016/j.wasman.2022.03.025) | Published author-uploaded text, specifically Methods 2.2–2.4 cited by the blister paper | Context only for microbial acid origin and filtration; no incineration-residue measurements imported |

The blister DOI resolves to the August 2023 volume; its PDF says available online
22 July 2023. The author upload is dated 25 July. SSRN 4401507 is an earlier
23-page preprint posted 30 March 2023; direct acquisition failed and its data
were not substituted for the journal version. For beverage cans, online December
2020 and February 2021 issue dates refer to the same DOI, not two experiments.

## Pharmaceutical blister waste: claim audit

Methods 2.1 and Supplement S1–S2 establish real hospital-collected waste sorted
by packaging construction. The three colour groups stay within one resource
record. Polymer labels differ by layer; the S2 label `PVDC/PCTFE` and the main
text's `PVDF or PCTFE` are not harmonized into a fabricated pure composition.
Section 3.1's Al estimates are batch-specific; the silver fraction later changes
from 67.6% to 63% in the prose. The record preserves the discrepancy.

Methods 2.5 uses pre-produced liquor with 0.85 M sulfate, pH about 0.2 and
source-described 0.86 M acid. The 2023 sulfur-source experiments in Figure 1 and
S3 have different concentrations and reactors. They do not document that the
blister lixiviant came from that particular biogas-sulfur batch. The upstream
referenced 2022 protocol names DSM 504/9466 and filters withdrawn acid at 0.2 µm;
this is method context, not independent authentication of the later liquor.

Methods 2.5–2.6 and Figures 2–4 support filtered-liquid Al release at specified
loadings, temperature and duration. Figure 2 has separate reagent-acid and
biogenic-acid bars, including values slightly above 100%. Poor silver-fraction
performance, the disappearance of the acid-type advantage at 50 °C, similar
outcomes after finer shredding and lower 1 L performance all limit generality.
The accessible Equation 2 text places solid inventory over liquid inventory;
its calculation is not independently reconstructed. PDF screenshots returned
text placeholders rather than inspectable image bytes through the available
tool, so no visual equation-layout verification is claimed. All five scientific
figure images were instead downloaded from the publisher CDN and actually
viewed, along with all four native supplement figures.

Biosurfactants and redox/foam explanations remain hypotheses. The reagent acid
does not match all culture-medium constituents. Section 3.3.3 discusses later
hydroxide precipitation by reference to other studies, without a blister-specific
isolated Al-product mass or purity. Figure 5 and Section 4 include solvent,
temperature and stabilizer interventions in polymer reprocessing, with residual
discoloration. Neither a commercial recovery operation nor a complete economic
or environmental assessment is established.

## Carton hydropulping reject: claim audit

Methods 2.1 establishes the source as industrial hydropulping reject, then dried,
cap-sorted, shredded and homogenized. Figures 1–2 show mixed plastics, Al and
remaining fibres. The original component labels 79/11/11 sum to 101; they are
approximate characterization, not a reconciled bulk mass balance. The cellulase
mixture's producing strain is not identified. Enzyme-mediated fibre removal is
a separate pretreatment, not a live-cell Al recovery mechanism.

The supplement directly names A. thiooxidans DSM 504 and A. caldus DSM 9466 in
the acid-production mixture, including medium, reactor, aeration, replenishment
and centrifugation. It estimates total acidity from pH and sulfate; the nominal
1.4 M label is not an independent acid-purity assay. Main Methods 2.5, Results
3.3 and Figure 4a compare spent acid with commercial acid at the highest loading.
Comparable performance supports an alternative source of acid, without proving
live-cell necessity during dissolution or an extra metabolite effect.

The direct-culture arm is less effective, especially at higher feed loading,
and shows a nonzero reagent-medium blank, polymer discoloration and altered
FTIR bands. These results do not prove the proposed persulfate pathway. Its
DSM 583 label is described as newly reclassified to A. ferridurans in the paper,
whereas the live DSMZ catalogue retains A. ferrooxidans. The record preserves
the conflict and leaves that arm without a species CURIE rather than identifying
the actual stock from assumption. Upstream species CURIEs 930 and 33059 were
resolved at NCBI and kept distinct from collection accession identity.

Methods 2.6/2.8 specifies NaOH precipitation at pH 6.5, compared with 6.4 in the
abstract. Near-complete solution removal is based on Al non-detection without
a stated detection limit; the pictured solid is not a phase/purity-validated
isolated-metal yield. The integrated experiment is described as a shaken 2 L
bottle with 1 L acid; the abstract's stirred-tank wording is not silently adopted.
Figure 6 retains polymer impurities. Feed origin does not establish industrial
deployment of the laboratory process.

## Access, reuse and remaining leads

Both main curated papers explicitly state CC BY 4.0 in their published PDFs.
The supplements are linked publication artifacts, not independent experiments;
no separate supplement-specific licence was observed. Raw articles, source
images and catalogue HTML remain outside Git at
`/private/tmp/cmm-round26-packaging-raw`. The JSON distinguishes actual binary
downloads from web-extracted text and derived renders. Local copies of web text
are not represented as downloaded PDF bytes. Direct publisher/ResearchGate
downloads sometimes returned 403; the first Genoa hostname had an expired
certificate, and the functioning alternative repository page confirmed closed
access. Certificate checks were not disabled, no login was attempted and no
author was contacted. A speculative SSRN delivery-code URL was unsuccessful
and supplies no evidence.

The related [2025 PolyAl study, DOI 10.1016/j.wasman.2025.114913](https://doi.org/10.1016/j.wasman.2025.114913)
is a priority follow-up for the same carton-reject identity, not a new resource
merely because the acid changes. Its abstract suggests organic-acid comparisons;
full methods are needed to distinguish purchased reagents from experimentally
microbial preparations. The [2026 adhesive study, DOI 10.1039/D6GC00733C](https://doi.org/10.1039/D6GC00733C)
describes designed packaging adhesive; it is an uncurated lead, not evidence that
the existing hospital waste uses that formulation. Beverage cans remain the
strongest distinct packaging identity awaiting full primary access. These
bounded outcomes do not exhaust material identities or microbial mechanisms.

## Handoff and validation

The two record drafts and native CREATE sidecars reference issue 93. Named
validation completed successfully for both records; the final batch gates and
independent scientific reviews are controlled separately. An independent reviewer
has raised a minor ambiguity in the blister description; the original state is
being preserved before correction. This report does not assert acceptance of
that state. Current schema fields express the two resources and scoped evidence
without changes. No importer, governance file, historical record or shared
documentation was changed by this author task.
