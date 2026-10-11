# Indium curation dossier

Added [elemental indium](../../data/records/indium.yaml), based on the
Nicomel et al. primary experiment rather than a review or abstract. Exact
searches, acquisition timestamps, SHA-256 hashes, access failures and terms
are in the [machine-readable receipt](round6-indium-20261011.json). Baseline
`d09a5611767d94fd196393b31d44cb8cf6657f7f`; the parent reported the unchanged
baseline gate passed before corpus writes. This dossier is not a scientific
review.

The [ChEBI authority](https://www.ebi.ac.uk/chebi/CHEBI:30430) resolves
CHEBI:30430 to indium atom, formula In and charge zero. The
[US2025 notice](https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm)
has the exact Indium row on page 50496. Its named commodity maps to the
elemental record; it does not make every In salt, mineral or ITO stream a
synonym or confer inherited criticality.

## Selected experiment and bounds

[Nicomel et al. 2020](https://doi.org/10.1039/C9GC03073E), Green Chemistry
22:1985–1995, was inspected through its
[UPC accepted manuscript](https://upcommons.upc.edu/server/api/core/bitstreams/e2c160fc-f3c7-4279-8931-d298426d9b78/content).
The manuscript has 35 numbered pages plus its cover; PDF page numbers are one
higher. Its main Figures 2, 5 and 9 were also rendered and inspected visually.
The final published full text was not acquired. The publisher abstract and
[UGent metadata](https://biblio.ugent.be/publication/8655193) confirm identity;
the UGent published-version file is restricted to UGent and marked in copyright.
Raw PDF, HTML and derived renders remain outside Git.

| Claim | Evidence and interpretation |
|---|---|
| Biomass | Section 2.2, manuscript pp5–6: municipal-wastewater pond biomass harvested June 2017, dominated by Chlorella sp. and diatoms (mostly Nitzschia/Navicula), with grazers. Thickened, centrifuged, frozen, lyophilized, washed, dried and ground. Inactive mixed biomass; no taxon identifier or causal member assignment is invented. |
| Assay | Sections 2.1 and 2.6–2.8, pp5 and 8–9: synthetic InCl3, 100 mg biomass/10 mL, duplicate tubes, 115 rpm, room temperature. ICP-MS of 0.45 µm filtrate establishes apparent aqueous removal; percentages are relative to initial In. |
| pH response | Section 3.4/Figure 2, pp13–15: 94.7% removal at initial pH 2 after 24 h, 0.15 mM In and 100 mL/g; final pH about 2.4. Separate Figure 3 kinetics reports about 80% by 30 min. |
| Controls | Section 2.6 reports precipitation controls showing onset near pH 2.7 and refers to Figure S2. Publisher-link and two ordinary candidate supplementary-PDF routes failed; the control plot and exact protocol were not independently inspected. This is explicitly retained as a limit. |
| Capacity | Section 3.6/Table 2: 0.14 mmol/g is fitted Langmuir qmax from the 0.05–10 mM series; Freundlich gives the better fit. It is not a measured maximum or a product yield. |
| Counterevidence | Section 3.7/Figure 5, pp20–22: 1 mM In plus 10 mM Fe(III) reduced In removal from 67% to 5% at initial pH 2, 100 mL/g and 24 h. Tin loss in the separate binary condition was predominantly precipitation, not proof of adsorption. |
| Regeneration | Sections 3.8–3.9/Figures 6–9: the desorbent screen gave about 80% release of adsorbed In with 0.1 M HCl, 100 mL/g and 24 h. The different reuse protocol used 60 mL/g and 30 min. Adsorption declined 91.3→60.7% over five cycles. Acid release is not isolated-metal recovery. |

Surface-group titration and marginal FTIR shifts are insufficient to assign
one molecular interaction. Biomass was grown in a pilot pond, but the indium
tests were laboratory batches with synthetic feeds. The authors propose
burning the loaded biomass to obtain In-rich ash; that proposal is not a
demonstrated process. The reported concentration ratio of about 1.5 also
limits the practical recovery claim.

## Deduplication, deferred leads and follow-up

Hidden/ignored-inclusive searches covered records, research, reviews and
history, then the eight named prior task-download scopes in the JSON receipt.
Existing matches were authority/frontier proposals and authority copies;
there was no previously curated indium root or Nicomel assay within those
boundaries. Binary contents not already text-extracted, unrelated home/temp
trees and all possible literature are outside this absence claim.

Ogi et al. (2012), *Recovery of indium from aqueous solutions by the
Gram-negative bacterium Shewanella algae*, is a useful next primary assay to
acquire. The Aspergillus LCD-panel experiment and 2018 indium/tin bioleaching
PDF are deferred leads, not accepted evidence. The readily accessible
Ascophyllum paper was not selected as microbial evidence because it uses a
macroscopic seaweed. An exact-DOI correction/retraction/erratum query returned
no relevant notice in this bounded search; this is not an exhaustive absence
assurance.

The next useful evidence is the actual supplementary control protocol and
Figure S2, followed by a comparison with the final published full text. New
organism-specific experiments would be required to assign mixed-biomass
activity to an individual taxon.

## Local provenance and checks

Canonical CREATE sidecar:
`history/records/indium/2026-10-11T053922Z-codex-ce07d4.yaml`, generated by
`just new-history` with actual codex / GPT-6 / codex metadata and issue 32.
Its path and a distinct actual inline event were attached before hash capture.
The named-record validation passed: `Checked 1 record(s); 0 failed.`
Final pre-review SHA-256:
`92414434d8f03130dcd8fc225659752c66f9b3b726f9c3598f1dcc2b4aa09aed`.
The parent coordinates the independent review and full batch gates; no
self-review is asserted here.
