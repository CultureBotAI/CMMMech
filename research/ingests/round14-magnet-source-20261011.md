# Round 14 NdFeB magnet-resource assessment

Researcher: Codex (GPT-6; codex), 2026-10-11 UTC. The exact save/acquisition
timestamps and hashes are in the [JSON dossier](round14-magnet-source-20261011.json).
Worktree `/private/tmp/CMMMech-expansion-round14-20261011`, branch
`curate/cmm-expansion-round14-20261011`, trusted base
`8f8abedfce68f932e4f6f333a5470ee5f3897ff4`; acceptance [issue 56](https://github.com/CultureBotAI/CMMMech/issues/56).

## Scope and identity decision

The new [spent NdFeB magnet record](../../data/records/spent-ndfeb-magnets.yaml)
denotes discarded permanent-magnet material as a secondary resource. It is
distinct from neodymium, pure Nd2Fe14B, other magnet families and the existing
raw-material grouping for permanent magnets. Variable alloy additions,
coatings and contamination prevent a universal feed formula or inventory.
No criticality entry or external material ID is inferred from constituents.

[Riano and Binnemans 2015](https://doi.org/10.1039/C5GC00230C), printed
pp.2932–2933, explicitly studies an end-of-life NdFeB feed and describes its
University of Birmingham provenance. Table 1 reports one feed composition
with a 95.72 wt% total; this does not define every discarded magnet. Only
identity/feed context is used here. Its chemical extraction optimization also
uses a synthetic solution, and none of its product purities or recovery claims
is transferred into the separate microbial-origin biomass assay.

The [Kucuker 2017 experiment](https://doi.org/10.1371/journal.pone.0175255)
is already curated under [neodymium](../../data/records/neodymium.yaml).
Adding the feed/resource root is not a new experimental replication. The paper
describes real hard-disk magnets but not their precise collection/device
history. The record makes that transfer limit explicit rather than claiming
verified end-of-life provenance for the biosorption feed itself.

## Search and acquisition

The seven exact web queries, UTC date and first-result-page coverage are
recorded in JSON. Searches covered the exact PLOS DOI with correction/retraction
terms, its experimental system, the used-magnet identity paper, and potential
abiotic/precipitation limitations. No affecting correction notice was returned
in this bounded search; that is not an exhaustive clearance.

The local search used `rg --no-ignore --hidden --follow` across `data/records`,
`research`, `reviews` and `history` with the DOI, author and magnet aliases.
It produced 101 matching lines before this record was added. Existing neodymium
reviews and the broader permanent-magnet commodity boundary were read. The
older review's cited `/private/tmp/cmmmech-neodymium-s001.xlsx` is no longer at
that exact path; no machine-wide absence is claimed. The supplement was freshly
downloaded from the publisher, and its SHA-256 matches the value preserved in
the 2026-10-06 acquisition review.

Fresh public downloads retained outside Git in
`/private/tmp/cmm-round14-magnet-raw` comprise PLOS HTML, the complete 13-page
PDF, S1 XLSX, NCBI taxonomy XML, the SAG catalogue page and the Riano paper from
the originating research laboratory's public site. The RSC web reader returned
an internal error; the legitimate laboratory PDF supplied the material-context
evidence. Stable origin URLs and exact file hashes are retained. An expiring
publisher object-storage redirect for S1 is identified without preserving its
temporary signed query in the committed dossier.

PLOS states a Creative Commons Attribution license. The Riano PDF retains its
RSC copyright notice; reading the laboratory copy is not treated as permission
to redistribute it. Catalogue reuse rights are not assessed. No raw full text,
workbook, figure image or taxonomy export is committed.

## Primary evidence inspected

Kucuker Methods, Results, Table 1, Figures 1–3, Conclusion and the supporting
table were read. PDF pages 3, 6 and 8 were also visually inspected for the
workflow, Figure 2 response surfaces and Table 1. Other rendered pages are
marked as not visually inspected in JSON; no graph digitization was performed.

The feed is milled below 250 micrometres, roasted at 950 degrees C for seven
hours and selectively leached with nitric acid for 72 hours at 80 degrees C.
Prepared stock is separated and diluted before contacting algae. The
microbial-origin step is therefore biosorption from pretreated leachate,
not microbial attack on a magnet. The 90-degree-C, 24-hour drying establishes
inactive biomass. Outdoor pilot photobioreactor cultivation supplies that
biomass, whereas recovery tests are laboratory flask assays.

The scoped endpoint uses 0.2 L, 300 rpm, 90 minutes, pH 5, 35 degrees C,
250 mg Nd/L and 0.5 g dry biomass/L. ICP-OES assays filtered solutions;
the reported 157.40 mg/g is derived from their depletion using Eq.1.
Duplicate experiments are averaged. This is neither a direct solid-phase Nd
measurement nor an original-magnet-to-product recovery yield.

The source reports Fe, B, Dy and Co below detection after pretreatment without
numerical detection limits. These are not measured zeros or evidence of
selectivity for an untreated mixed waste. A matched biomass-free time-course
blank is not described in the inspected Methods or kinetic table. There are
no verified downstream regeneration or isolated-product yields in this assay.
Figure 1 includes a possible combustion route; that diagram does not establish
that a quantified metal-rich ash product was obtained.

Precipitation statements conflict: the text invokes its absence below pH 7
while discussing possible precipitation at 50 degrees C, and high-temperature
uptake wording differs between abstract and Results. The record preserves
these limits and avoids silently selecting a corrected high-temperature value.
Model fitting and pH trends do not identify a unique binding group or
rate-limiting chemical reaction.

## Supplement and identifiers

The original S1 workbook has `Tabelle1` (146 rows including two header rows,
11 columns), plus blank `Tabelle2` and `Tabelle3`. Merged condition cells must
be followed when reading lower rows. Source XML and openpyxl were inspected
without saving or recalculating the workbook; 40 formula cells remain original.

The A83:A86, B83:B86 and C83:C86 ranges give 35 degrees C, pH 5 and 0.5 g/L.
D86 is 250 mg Nd/L; E86's numeric token is 157.39840000000004 mg/g. Its rounding
agrees with the curated experimental endpoint. J86 is a different fitted
pseudo-second-order quantity, about 161.29 mg/g. The article's Table 1 gives
the separate Langmuir capacity, 188.68 mg/g. The source's broad R-squared
greater-than-0.99 claim has exceptions, including K100 and K121. Neither this
claim nor a causal kinetic mechanism is adopted.

These are uptake/model quantities with no source analysis date, not the native
`mg/kg` concentration-cell contract. No `observations` entries or schema change
is justified. JSON preserves selected raw tokens and exact cell locators.

Fresh NCBI XML resolves 3077 to *Chlorella vulgaris*, rank species. The SAG page
identifies 211-12 and reports catalogue axenity. Neither authority establishes
that the outdoor-grown experimental biomass was independently verified axenic.

## Curation handoff and remaining evidence

The canonical CREATE history is
`history/records/spent-ndfeb-magnets/2026-10-11T092622Z-codex-65cd7d.yaml`;
the record also contains a separate inline event. Initial named validation
passed one record with no failure. A subsequent relocation of the Langmuir
sentence to its article evidence entry preserves the quantitative claim while
making its source association more precise. Final batch gates and an
independent scientific review follow and are not claimed by this dossier.

Additional leads include primary characterization of end-of-life HDD magnets
(Muenchen and Veit 2017, DOI 10.1016/j.wasman.2017.01.032) and an older Kucuker
conference biosorption report with different apparent conditions. Only indexed
metadata/abstract material was inspected for those leads; their measurements
are not accepted as new experiments or contradictions here. Matched blanks,
feed history, complete mass balance, phase localization and regeneration remain
unresolved for the accepted assay. This bounded pass does not exhaust magnet
recycling or broader CMM evidence.
