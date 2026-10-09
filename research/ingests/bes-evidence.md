# USGS BES ingest evidence

Prepared 2026-10-09 UTC by Codex (GPT-6), the U/V record curator. This is an
ingest dossier, not an independent scientific review. Base revision:
`905388523b6e9184783989484896e4cc20297832`, branch
`research/cmm-source-survey-20261008`; the records are working additions.

## Decision and claim boundary

Source E1 in the [discovery report](../sources/cmm-landscape/20261008T073140Z.md)
is now used in [uranium](../../data/records/uranium.yaml) and
[vanadium](../../data/records/vanadium.yaml). Each records an observed
laboratory separation in an MR-1-inoculated electrochemical system. The
mechanisms retain **partial** support for microbial attribution and substantial
abiotic separation. They do not assert enzyme identity, microbial necessity,
an improved yield, a named precipitated mineral, or industrial deployment.

The root records identify elements with neutral-atom ChEBI identifiers.
Experimental ions, reagent solutions and electrode-associated products are
explicitly distinct. The Federal Register designation concerns the named U/V
commodities; no host mineral or waste stream inherits it here.

## Acquisition and deduplication

The primary source is [Kane et al., USGS release 10.5066/P9ERLSM6](https://doi.org/10.5066/P9ERLSM6),
ScienceBase item `6398f05dd34e0de3a1f0d7e4`. Its FGDC citation is dated
2026-09-15, while the [USGS portal](https://www.usgs.gov/data/data-acquired-experiments-bioelectrochemical-systems-critical-mineral-recovery)
is dated 2026-09-17. Experiments date to 2024-2025. The metadata says complete,
no planned updates, and CC0-1.0; no semantic dataset version is supplied.
The portal's Campbell-Hay name and the metadata's Campbell name identify the
same release, not separate experiments.

`rg --no-ignore --hidden` searched `data`, `research`, `reviews`, `history`
and `.claude` for the DOI, U/V names and MR-1/MR1. Ignored and hidden files
were included within that repository boundary. Existing hits were the source
report and forward review; no earlier U/V record was present there. Previously
downloaded metadata/T1/T3/T6 were re-inspected from
`/private/tmp/cmm-source-discovery-downloads`; this is not described as a fresh
download. Their original receipts/hashes remain in the discovery evidence JSON.

On 2026-10-09 the four additional public attachments below were acquired via
the download links in the previously saved ScienceBase HTML. Bytes were saved
under `/private/tmp/cmm-bes-ingest/`, outside Git. Receipts are also retained in
that directory's `acquisition.json`. No repository dependency changed: a
temporary PyMuPDF environment rendered the PDF for read-only inspection.

| File | Acquisition UTC | Bytes | SHA-256 |
|---|---|---:|---|
| T2_pH.csv | 2026-10-09T04:44:48.344017Z | 2484 | `37b437d1194bc4d0b1906d6a5e63e0f347158ceef6e7621ec339fa3ece1911cf` |
| T7_UV_Vis.csv | 2026-10-09T04:44:48.620959Z | 138925 | `6249924fb62981dac1631d2eb377e5d41f2540dc5408111c70e7c0d1f8d525fa` |
| T9_SEM.pdf | 2026-10-09T04:44:49.948500Z | 4344277 | `50306bbd04006fc0b868204aab9159f8059f4c301d687c24b46e08c930e8129b` |
| T8_XRD.csv | 2026-10-09T04:44:50.202085Z | 48525 | `3ffb58083651002fb60de5d6fb19dc3d646f98aeee9270f17ab7dc3edbd6edc4` |

Exact attachment URLs:

- [T2 pH](https://www.sciencebase.gov/catalog/file/get/6398f05dd34e0de3a1f0d7e4?f=__disk__b3%2F05%2F9a%2Fb3059ab1d4e1d73e7706f8e249d15ef91bbe8569)
- [T7 UV-Vis](https://www.sciencebase.gov/catalog/file/get/6398f05dd34e0de3a1f0d7e4?f=__disk__36%2F56%2F9f%2F36569feaadeb989647dba2f16e32022c6b43f3f4)
- [T9 microscopy](https://www.sciencebase.gov/catalog/file/get/6398f05dd34e0de3a1f0d7e4?f=__disk__59%2F8b%2Fa6%2F598ba6c44f37d443a906f3cd9abbdec366b7c714)
- [T8 XRD](https://www.sciencebase.gov/catalog/file/get/6398f05dd34e0de3a1f0d7e4?f=__disk__ce%2F40%2Fb4%2Fce40b4bf6ee5ff76aa15b7b8ae3c777e8bbb92f6)

## Evidence inspection

FGDC process steps 1-8 were read in full; the source methods specify MR-1,
100 mL two-chamber cells, defined electrolyte, pre-equilibration samples,
inoculation immediately before applying -800 mV versus saturated Ag/AgCl,
solution ICP-OES, extraction methods and follow-up characterization. The
inoculum preparation/density, controlled assay temperature, and independent
replicate design are not resolved in those descriptions. Repeat/replicate
labels are not treated as a statistical sample size.

| Evidence | Observed scope and use |
|---|---|
| T1 | Dictionary: T3 ppm is mg/kg. Negative assay values encode below-detection limits; -9999 is documented missingness. Definitions do not identify all experimental sample-name conventions. |
| T2 | 43 sample rows. U/V rows join T3 by exact SampleID; T3 RunDate is analysis date, not sampling date. Original biotic U pH after inoculation spans 7.01-8.21; V from sample 0 to end spans 7.31-7.70. V control and biotic sample durations and initial concentrations differ. Cr informational pH is outside acceptance criteria and is not imported. |
| T3 | Original biotic U EQ 975 to endpoint -0.1 mg/kg (therefore <0.1, not zero); abiotic t0 914 to endpoint 0.819 mg/kg. Biotic V sample 0 44.1 to endpoint 34 mg/kg; abiotic 19.1 to 12.2 mg/kg. No assumed density conversion or percentage recovery. This table also contains digests, not just aqueous samples. |
| T6 | Positive U and V working-electrode acid-extract measurements establish association with extractable material. U original acid extractions use different concentrated acids in biotic versus abiotic conditions. Working electrode, PTFE holder, incidental filter and reference frit are distinct fractions; do not aggregate blindly. The biotic U carbonate entry is not imported as an exact positive amount because its T3 concentration is below detection. |
| T7 | 911 wavelength rows, 13 columns. One blank at 1100 nm for abiotic endpoint, despite metadata's general -9999 rule. Source step 5 says samples were stored anaerobically 67 biotic/76 abiotic days before analysis. No immediate endpoint speciation or fitted component proportions are inferred. Negative absorbances are not automatically converted with the ICP censoring rule. |
| T8 | 3001 rows at 5-65 degrees two theta, carbon-felt blank and U biotic/abiotic intensities. Raw diffraction counts have no curated reference-pattern match here; no named phase is assigned. |
| T9 | All seven pages rendered and visually inspected. Page 1 blank electrode; pages 2-4 abiotic U; pages 5-6 biotic U. Deposits and U-labelled EDS signals support electrode association in both conditions. Page 7 is expressly solids from **V phosphate-buffered culturing medium**, not a V BES working electrode: excluded from V electrode-product identification. |

The source's reported V(V) reagent formula `Na3V2O8` is preserved as reported
with an unresolved stoichiometry qualification. It is not normalized to a
guessed reagent or mapped to a mineral identifier. None of the records derive
electron-transfer causality from the metadata abstract alone.

## Identifier and authority checks

Live issuing-source checks on 2026-10-09:

- [ChEBI:27698](https://www.ebi.ac.uk/chebi/CHEBI:27698): vanadium atom, V,
  charge 0, `[V]`.
- [ChEBI:27214](https://www.ebi.ac.uk/chebi/CHEBI:27214): uranium atom, U,
  charge 0, `[U]`. Web-tool fetch failed; ordinary public HTTPS succeeded.
  Saved HTML `/private/tmp/cmm-bes-ingest/uranium-chebi.html`, 823052 bytes,
  SHA-256 `7cd4ba88cf6cc47e6985213c899003ac3f546a250ba88c64928273df1391a0e3`.
- [NCBI Taxonomy:211586](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=211586):
  current displayed name Shewanella oneidensis MR-1; resolves the reported
  strain name, not independent sequencing of the experimental inoculum.
- [Final 2025 U.S. list](https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm):
  uranium and vanadium explicitly named in summary and final table. The U
  addition is stated in the notice; the older assumption that U is excluded
  is not carried into the new record.

## Bounded correction and related-evidence search

Web searches on 2026-10-09, one returned result set each, no pagination:

1. `"10.5066/P9ERLSM6" correction retraction`
2. `"P9ERLSM6" uranium vanadium bioelectrochemical`
3. `"Data acquired in experiments on bioelectrochemical" correction`
4. `Kane Selvage Ciechanowicz Campbell Shewanella uranium vanadium 2026`

These searches returned the USGS release and other studies, but did not verify
a correction, retraction or companion interpretation paper for this release.
This is bounded coverage, not a claim that none exist. Recent, separate
uranium biofilm studies surfaced, including DOI `10.1016/j.jhazmat.2026.141485`
and PMID `42762932`; only their primary abstracts/metadata were encountered.
They are follow-up leads, not imported evidence for the USGS conditions.

## Next work and validation

Independent per-record review follows this curation. Quantitative comparison
would require sample/experiment mapping, inoculum details, matched durations,
pH and extraction bases, aliquot-volume/mass accounting, and a statistically
supported design. A phase or oxidation-state claim requires a reviewed
interpretation with appropriate standards. These are future analysis tasks,
not reasons to erase the accepted bounded observations. As/Sb/Cr ingests
remain separate decisions; the present U/V evidence does not certify them.

Both final U/V records passed individual strict validation after history
attachment on 2026-10-09. `cmmmech validate-history --base
905388523b6e9184783989484896e4cc20297832` checked 12 sidecars, zero errors.
The same curator then ran the complete batch gate while independently reviewing
other records: `UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache just check` passed
lint, 215 tests, with three existing optional-command skips; ten records and
12 histories validated. `uv run --locked cmmmech validate --require-records`
checked ten records, zero failures. Contract validation is separate from the
independent scientific acceptance reviews.
