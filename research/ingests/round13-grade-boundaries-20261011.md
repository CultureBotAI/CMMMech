# Round 13: deferred commodity boundaries

Prepared 2026-10-11 UTC by codex / GPT-6 / codex in
`/private/tmp/CMMMech-expansion-round13-20261011`, trusted base
`14ceff0da3e19d6d36426d33f4cf577b8e64760f`. The six proposals were carried
forward from the [round-12 frontier](round12-frontier-20261011.md).
The [JSON receipt](round13-grade-boundaries-20261011.json) records source
acquisitions, queries, hashes, decisions and validation. This dossier is separate
from the final independent scientific record review.

## Decisions and material identities

| Deferred proposal | Decision | Concrete next evidence or product scope |
|---|---|---|
| metallurgical-coal | Create a source-scoped commodity family. | EIA and IEA broader steelmaking categories; preserve the coking-coal subset and narrower USGS usage. |
| boron-metallurgy-grade | Keep deferred. | Ferroboron has its own product standards; that alloy is not the whole EU qualifier. Boric oxide, boric acid and refined borates require separate identity assessments. |
| lithium-battery-grade | Keep the umbrella deferred. | Investigate battery-grade lithium carbonate and lithium hydroxide monohydrate separately using dated product standards; anhydrous hydroxide is another form. |
| manganese-battery-grade | Keep the umbrella deferred. | Separate manganese sulfate, electrolytic manganese metal and electrolytic manganese dioxide; the JRC capacity grouping includes all three. |
| nickel-battery-grade | Keep the umbrella deferred. | Battery-use nickel sulfate is a specific product; upstream Class I metal and intermediate feedstocks are not synonyms. |
| graphite-battery-grade | Keep the umbrella deferred. | Natural purified/spherical and synthetic negative-electrode products need application-specific identity and qualification. Carbon purity alone is not a universal battery acceptance test. |

### Metallurgical coal: overlapping scopes can be represented honestly

The [EIA glossary](https://www.eia.gov/tools/glossary/index.php?id=Metallurgical+coal)
includes both coking and pulverized steelmaking coal. The newly inspected
[IEA Coal 2020 glossary](https://www.iea.org/reports/coal-2020/annex) separately
identifies coking coal, semi-soft blending coal and PCI coal within that report's
metallurgical category, while assigning anthracite to thermal coal even when
used in metallurgy. Its explicit scope resolves the earlier need for an
independent definition of the broader family.

The [new record](../../data/records/metallurgical-coal.yaml) makes its overlap
with [coking coal](../../data/records/coking-coal.yaml) explicit. The reused and
rehashed [USGS Fact Sheet 2026-3061](https://pubs.usgs.gov/fs/2026/3061/fs20263061.pdf),
version 1.1, August 2026, pp. 1–2, instead uses the terms interchangeably in
coke production. That usage is preserved. The family has no transferred EU
coking-coal or US metallurgical-coal designation, no invented numerical grade
boundary, and no duplicated coal experiment. It is an identity-only record.

### Battery and metallurgy labels are not single chemical identities

The original [EU 2024/1252](https://eur-lex.europa.eu/eli/reg/2024/1252/oj/eng),
Annex I 1(c), 1(h), 1(j)–1(l), names the five qualified materials; Annex II
1(w) also names battery-grade nickel. These original designations remain valid
historical evidence. Article 3 permits updates and requires a review by
24 May 2027; the date does not prove that no earlier update exists. The bounded
delegated/implementing-act queries found no grade specification that resolves
these roots. The EUR-Lex all-information route yielded no usable relation graph,
so this is not a complete amendment audit or a claim about the latest list.

The [Commission's 2025 boron factsheet](https://single-market-economy.ec.europa.eu/document/download/d6fb1296-b08c-4f80-b735-0f9f1fc36603_en?filename=RMSP_Boron_Factsheet_V2.pdf)
was acquired as a real one-page PDF and visually inspected. It describes uses
under the metallurgy-grade heading but supplies neither product composition
nor an impurity limit. Its placeholder ISBN/DOI strings are not identifiers.
The primary standards catalogues identify ferroboron as a separate product:
[SAMR GB/T 5682-2015](https://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D80975D3A7E05397BE0A0AB82A)
and [ASTM A323-05(2025)](https://store.astm.org/a0323-05r25.html).
Only catalogue/scope information was inspected; the current complete grade
tables were not acquired. No ferroboron percentage is substituted for the
undefined EU grade, and a withdrawn ASTM analytical-method range is not adopted
as a current product definition.

The [DOE January 2022 workshop report](https://www.energy.gov/sites/default/files/2022-01/Battery%20Critical%20Materials%20Workshop%20Report%20-%20FINAL.pdf),
printed pp. 11 and 23 / PDF pp. 23 and 35, records differing participant
descriptions of lithium purity requirements and a lack of a common testing
standard. These are workshop observations, not present-day universal standards.
The [Fastmarkets methodology FAQ](https://www.fastmarkets.com/methodology/lithium-methodology-faqs/)
describes September 2026 changes emphasizing destination-market buyer
qualification for distinct carbonate and hydroxide-monohydrate assessments.
Neither source defines all lithium-bearing battery materials.

The rechecked [JRC 2023 methodological notes](https://rmis.jrc.ec.europa.eu/uploads/rmprofiles/info-production.pdf),
p. 143, Section 47.4, aggregate EMD, high-purity EMM and high-purity MSM for
battery-grade manganese capacity. This corroborates the need to distinguish
products rather than equate the umbrella with manganese sulfate. The prior
[JRC foresight Table 16](https://rmis.jrc.ec.europa.eu/uploads/CRMs_for_Strategic_Technologies_and_Sectors_in_the_EU_2023.pdf),
printed p. 243 / PDF p. 246, independently distinguishes precursor and upstream
intermediate forms; its retained PDF was rehashed and that page re-read.

## Product-standard handoff

The official SAMR registry establishes these specific standards and their
edition/status metadata. It does not expose the complete technical tables in
the inspected textual pages. Numeric qualification remains unverified.

| Product to investigate | Verified registry edition | Date and limit |
|---|---|---|
| Battery-grade lithium carbonate | [YS/T 582-2023](https://std.samr.gov.cn/hb/search/stdHBDetailed?id=1C51E7879EF6D54EE06397BE0A0A1DC6) | Effective 1 July 2024; replaces 2013. A previous raw search already mentioned this standard; this pass verifies the issuing registry. |
| Battery-grade lithium hydroxide monohydrate | [GB/T 26008-2020](https://std.samr.gov.cn/gb/search/gbDetailed?id=A73D6262FE9172E3E05397BE0A0A6CEB) | Effective 1 April 2021; replaces 2010. Preserve hydration state. |
| Manganese sulfate for batteries | [HG/T 4823-2023](https://std.samr.gov.cn/hb/search/stdHBDetailedCNF?id=037FCC3702C04EF6E06397BE0A0A09CA) | Effective 1 February 2024; replaces 2015. Chinese title translated here; hydration/composition table not checked. |
| Nickel sulfate for batteries | [HG/T 5919-2021](https://std.samr.gov.cn/hb/search/stdHBDetailedCNF?id=D7B6988FD9BCAABEE05397BE0A0A1B36) | Effective 1 April 2022. Chinese title translated here; distinguish anhydrous, hydrated and solution products during curation. |
| Graphite negative-electrode materials | [GB/T 24533-2019](https://std.samr.gov.cn/gb/search/gbDetailed?id=8531C702DBA16551E05397BE0A0ACD16) | Effective 1 February 2020; registry shows current status. An ongoing revision is not an enacted replacement. |

Priority is to acquire legitimate full product specifications and verify chemical
and commodity scope before deciding between new narrow records and a defined
umbrella. Then search primary microbial studies for the exact feed or achieved
product. A metal-solubilization assay does not demonstrate a qualified battery
precursor. No mechanism research or new chemical identifier validation was
performed for these five deferred roots in this pass.

## Additional authority lead and access limits

[Commission Implementing Regulation (EU) 2026/1116](https://eur-lex.europa.eu/eli/reg_impl/2026/1116/oj/eng),
published 27 May 2026, was acquired and its Article 1, recitals and complete annex
read. It identifies products/components/waste streams with CRM recovery
potential under Article 26, including battery materials, industrial catalysts,
digestate and sludge/ash streams. Extractive waste is handled separately. This
is a useful secondary-resource discovery authority, not a grade definition,
new criticality designation for each waste, or evidence of microbial recovery.
The parent workstream received the lead for its resource assessment.

Local deduplication used hidden/ignored-aware, symlink-following searches across
`data/records`, `research`, `reviews`, `history`, and the cited round-12 carbon/
metals and aluminium/boron raw directories. The new record ID was absent there
before creation; prior proposals and source references were retained as prior
work. Binary PDFs were explicitly opened rather than presumed searchable. This
is a bounded repository/source check, not machine-wide or scientific exhaustion.

Twenty-nine exact web queries and linked official pages were inspected without
pagination. Raw files remain outside Git in `/private/tmp/cmm-round13-grade-raw`.
The Commission PDF first returned 429 through the web reader but the ordinary
public URL subsequently downloaded through its official redirect. SAMR full-text
entry pages exposed preview/download buttons and a browser-support message;
the standards' full technical content was not retrieved. ASTM catalogue access
was not full-text access. Rights for those standards remain reserved; no raw
documents are committed. No access restrictions were bypassed.

The CREATE sidecar is
`history/records/metallurgical-coal/2026-10-11T090113Z-codex-5e05f9.yaml`.
Its creation preceded receipt of issue #54, so its optional issue field is absent.
Named validation passed: one record, zero failures; one history against the
trusted base, zero errors. The parent baseline passed 307 tests with three skips
and 93 pre-existing records. Full batch gates and independent review are
parent-owned and are not claimed completed by this dossier.
