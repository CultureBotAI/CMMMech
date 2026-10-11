# Antimony: source decision and curation dossier

Curated 2026-10-11 UTC by Codex (GPT-6; `/root/cmm3_platinum`) in
`/private/tmp/CMMMech-expansion-round4-20261011`, branch
`curate/cmm-expansion-round4-20261011`, trusted base
`c081a749cd63feafcc25414f5ad006d1f78f1e36`. This is a curator's evidence
assessment, not an independent scientific review.

## Decision

Add [antimony](../../data/records/antimony.yaml) as an element with its dated
U.S. 2025 designation and one bounded microbial transformation mechanism.
The original [USGS BES lead](bes-evidence.md) does not establish a microbial
Sb experiment at the resolution needed for a new mechanism. Its Sb cells
remain documented below, without copying U/V conclusions into Sb.

The accepted primary is [Johnson et al. (2021), Heliyon 7(2), e06275](https://doi.org/10.1016/j.heliyon.2021.e06275),
DOI `10.1016/j.heliyon.2021.e06275`, PMID `33681496`, PMC `7930292`.
Its defined sediment microcosms, uninoculated control, separate pasteurized
biogenic-material comparison, and X-ray absorption analyses provide a stronger
claim-specific basis than the BES metadata abstract. The mechanism is indirect
microbial sulfur/iron cycling coupled to chemical Sb reduction, without an
isolated Sb product, specific enzyme or industrial deployment claim.

## Identity and dated criticality

- Live [ChEBI:30513](https://www.ebi.ac.uk/chebi/CHEBI:30513) HTML resolves
  **antimony atom**, formula Sb, net charge zero; displayed modification date
  21 July 2017. The atom identifier grounds the element and does not identify
  antimonate, an Sb mineral or experimental neutral atoms.
- The [Final 2025 U.S. List of Critical Minerals](https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm),
  published 7 November 2025 in 90 FR 50494–50497, names antimony in the summary
  and commodity table on page 50496. The record explicitly maps this named
  commodity to the elemental root, without transferring designation to every
  compound, mineral or waste stream. This is an edition-specific claim.
- The inoculum is a wetland sediment community, not a pure strain. No taxon ID
  or individual organism's causal role is invented from relative-abundance
  sequencing. The record's `microbial: true` describes that community context.

## Rejected BES mechanism and quantitative-cell handoff

Re-read retained FGDC metadata, T1, T2, T3 and T6 from the earlier public
USGS release, [DOI 10.5066/P9ERLSM6](https://doi.org/10.5066/P9ERLSM6).
The release citation is dated 15 September 2026; the live USGS portal is
dated 17 September 2026. These are publication dates, not assay dates.
Original acquisition receipts remain in the [landscape evidence JSON](../sources/cmm-landscape/20261008T073140Z-evidence.json)
and [BES dossier](bes-evidence.md); this pass rehashed their actual retained
bytes and does not claim fresh table downloads. The release declares CC0-1.0.

| T3 SampleID | Exact Sb_ppm token | Analysis RunDate | Exact T2 sampling-date match |
|---|---:|---|---|
| `Sb.8V_PreEQ` | `191` | `06/12/2025` | None |
| `Sb.8V_0` | `32.2` | `06/12/2025` | None |
| `Sb.8V_1` | `12.4` | `06/12/2025` | None |
| `Sb.8V_2` | `15.3` | `06/12/2025` | None |

These are total-element ICP-OES concentrations in **mg/kg**, according to
T1, with Sb measured at 206.836 nm. All four selected tokens are positive
measurements. T1 defines negative analyte tokens as below the absolute-value
detection limit; metadata separately defines `-9999` as missing. No density
conversion, zero substitution, sampling date, duration or recovery fraction
is inferred. Metadata step 2 describes 0.22 micrometre filtration followed by
preservation in 1% HNO3 for working-solution samples. T3 as a whole also
contains digests, so its filename alone does not establish every row's fraction.

T1 explicitly defines `Sba_A` as **abiotic antimony** current; it has no
corresponding biotic Sb current definition. The four T3 Sb sample names lack
an explicit biotic/abiotic suffix, and the inspected dictionary does not supply
a complete run-to-sample mapping. T2 contains 43 rows with no exact match for
these four samples; T3 contains 87 rows; T6 contains 22 rows, none assigned to
Sb in its Element column. Metadata step 4 describes U/V/Cr extractions, not
Sb extractions. T8/T9 U/V characterizations do not establish Sb phase or valence.
The metadata also reports `Sb(V) as K2Sb2(C4H2O6)2·3H2O`; its stated valence
and antimony-tartrate formula warrant clarification, not silent chemical
normalization. The exploratory PubChem search did not independently certify
the stock reagent. No Sb redox assignment is derived from that formula here.

Thus the broad BES abstract cannot establish an Sb microbial benefit. These
cells are retained in the research JSON, not nested as observations under an
unrelated microbial mechanism. A later BES ingest needs explicit arm/sample
mapping, actual sample dates and pH, verified reagent identity/valence, and
Sb-specific biotic/control and product evidence. Absence statements here are
limited to the inspected tables and dictionary, not every possible experiment.

## Accepted experiment and analytical boundaries

Full primary XML was acquired from the official Europe PMC full-text API and
parsed, including Methods 2.1–2.11, Results 3.1–3.2, Discussion 4.1–4.4,
figure captions and reference list. PubMed and publisher records independently
confirmed bibliographic identity. The source declares CC BY-NC-ND 4.0;
full text and any raw media remain outside Git. The manuscript's own standard
fits are treated as interpretations, not newly fitted raw data.

- **System D:** duplicate 240 mL serum bottles, 200 mL final suspension;
  2 mM KSb(OH)6, 50 mM Fe(III) as ferrihydrite, reported 10 mM sulfate,
  lactate and defined medium. Medium pH was set to 7.2 before assembly;
  D's reported pH changed from 7.11 to 6.87 at day 3 and 7.44 at day 21.
  Argon sparging, dark incubation at 30 °C and roller mixing were specified.
  One mL inoculum came from 10 g surface wetland sediment in 150 mL medium.
- **Loading conflict:** abstract lactate is 10 mM; Methods 2.3 specifies
  2 mL of 2 M lactate in 200 mL, arithmetically 20 mM. Neither value is
  silently promoted to a resolved condition. The record preserves both.
- **Fractions:** dissolved Sb means the 0.2 micrometre nylon filtrate,
  total-element ICP-OES (5 micromolar detection limit). Filter-retained
  hydrated solids were stored anoxically for Sb/Fe K-edge XANES and EXAFS.
  This does not identify all aqueous species or purified solids.
- **Sorption versus redox:** D had >99% solution depletion within 5 days,
  yet day-5 EXAFS was similar to the uninoculated control. A likewise removed
  approximately 98% within 5 days without detected Sb reduction. Later D
  spectra showed Sb(III). No disappearance percentage is called a recovery
  yield or used as direct proof of Sb reduction.
- **Control definition conflict:** Methods 2.3 and the Sb results explicitly
  include Sb(V) in A; abbreviated Figure 3/4 captions omit it. The record
  discloses this omission and uses the explicit methods/results assignment.
  Figure 13's abbreviated D caption similarly omits Sb, whereas Methods,
  the Results paragraph and Figure 14/15 definitions include it.
- **Indirect route:** separate system B material (Fe/sulfate, no initial Sb)
  was collected at day 21, pasteurized 1 h at 70 °C and challenged with
  2 mM Sb(V) for a further 21 days. It reduced Sb, as did abiotic mackinawite.
  This supports reactive biogenic sulfide chemistry, not a matched killed-D
  experiment or proof that live cells have no role. Failed enrichment of
  direct Sb-reducing bacteria also does not prove their absence.
- **Phase limits:** O/S-coordinated Sb(III) fits do not uniquely identify
  a crystalline product. The authors explicitly could not distinguish the
  proposed combination of sorbed Sb(III)/amorphous Sb2S3 from alternatives
  such as a mixed O/S phase. No system D mineral species or exact fit
  percentage is imported. Color and community composition alone are not
  redox or causal proof. Acid Fe(II) extraction can overestimate in-situ
  reduction; its numerical values are not imported.
- **Scope:** the record accepts system D with its relevant comparisons,
  not all experiment arms, mineral-specific fits or broad taxon conclusions.
  It does not infer field operation, element-specific product purity or
  commercial recovery from a laboratory environmental-fate experiment.

## Bounded search, novelty and contrary evidence

On 2026-10-11, `rg --no-ignore --hidden` searched `data`, `research`,
`reviews`, `history` and local skills; relevant retained-source searches
included `/private/tmp/cmm-source-discovery-downloads`,
`/private/tmp/cmm-bes-ingest` and this task's raw directory. Queries covered
antimony, CHEBI:30513, P9ERLSM6, e06275, PMC7930292 and es404098z.
Ignored and hidden files were included. Existing antimony hits were source
inventories and deferred BES discussions; the selected Johnson primary and
antimony root were not present in that searched repository scope before
curation. No machine-wide or literature-wide absence is claimed.

Web searches used the web search provider on 2026-10-11, first returned set
per query, without pagination or date filters:

1. `site:ebi.ac.uk/chebi antimony atom`
2. `"P9ERLSM6" antimony`
3. `"10.5066/P9ERLSM6" correction retraction`
4. `antimony microbial reduction primary Desulfuribacillus stibiiarsenatis 2014 Abin Hollibaugh`
5. `antimony Shewanella microbial reduction antimonate MR-1 primary study`
6. `"Reduction of Sb(V) by coupled biotic-abiotic processes" PMC`
7. `"10.1021/es404098z" pdf`
8. `"10.1016/j.heliyon.2021.e06275" correction retraction erratum`
9. `"Reduction of Sb(V) by coupled biotic-abiotic processes" contradiction`
10. `site:pubchem.ncbi.nlm.nih.gov "K2Sb2" tartrate "III"`
11. `"Johnson" "e06275" "erratum"`
12. `"antimony" "biogenic sulfide" reduction contradictory magnetite`

No verified correction or retraction of either selected release/paper was
found in those returned sets. This is bounded coverage. The source itself
discusses differing magnetite/green-rust outcomes in earlier studies; no
universal absence of reduction by those minerals is asserted here.

Other primary leads remain separate:

- [Abin and Hollibaugh 2014](https://doi.org/10.1021/es404098z), PMID24319985:
  MLFW-2 respiration and Sb2O3 crystals. Publisher abstract/metadata were
  accessible but main content required access; full methods were not acquired.
- [New Mobilization Pathway of Antimonite](https://doi.org/10.1021/acs.est.1c05206),
  PMID34730937: abstract reports MR-1/S0-associated Sb mobilization under
  different substrate/pH conditions. This is a concrete boundary against
  assuming that biogenic sulfide always immobilizes Sb; full methods were
  not checked and its measurements are not imported.
- [Removal of antimony by dissimilatory and sulfate-reducing pathways in
  anaerobic packed bed bioreactors](https://doi.org/10.1002/jctb.7296):
  indexed primary lead for an engineered system, not an accepted deployment
  claim or validation of the current microcosm conditions.

## Acquisition and remaining limits

The adjacent [machine-readable dossier](round4-antimony-20261011.json)
records exact URLs, actual UTC acquisition/recheck times, byte sizes and
SHA-256 hashes. Raw files are under
`/private/tmp/cmm-round4-antimony-evidence-20261011`; prior BES files remain
at their documented original temporary paths. Publisher and PMC access
failures are preserved; HTTP success alone is not treated as usable evidence.
The PMC HTML response is a browser-check page, not scientific full text.
Publisher media requests returned 403. The first official Europe PMC
supplementary archive request timed out; a second request was manually stopped
while awaiting completion, without a complete retained archive. Therefore no
figure pixels or supplementary PDF tables were inspected in this pass. Main
text, methods and captions were read in full; the accepted qualitative redox
and control claims are explicit there. Exact supplementary fit fractions and
independent phase reassignment are excluded. A reviewer should retain this
access limitation rather than describe these figures as visually checked.

Scientific review must cover the final history-attached record and these
source limits. No schema or validator change is needed. Exact spectral fit
fractions, Sb mineral identity, direct respiratory enzyme, isolated recovery
yield, resolved lactate loading and the incomplete BES sample mapping remain
unclaimed.

## Local checks and final review target

After the actual CREATE sidecar and distinct inline event were attached,
`uv run --locked cmmmech validate data/records/antimony.yaml` passed
(1 record, 0 failed). `validate-history --base
c081a749cd63feafcc25414f5ad006d1f78f1e36` passed (36 histories, 0 errors)
at the concurrent batch snapshot. `git diff --check` passed. Commands used
`UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache`.

Final antimony SHA-256:
`3854163557ef588e4d570f71e6939b406bef24763d31332afe0741400cd91576`.
History: `history/records/antimony/2026-10-11T045740Z-codex-3839a3.yaml`.
Batch checks and independent scientific review follow; these structural checks
do not remove the documented source-access and mechanistic limitations.
