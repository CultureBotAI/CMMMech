# Round14 product boundaries and curation handoff

UTC: 2026-10-11T09:28:17Z. Trusted base: `8f8abedfce68f932e4f6f333a5470ee5f3897ff4`.
Worktree: `/private/tmp/CMMMech-expansion-round14-20261011`. Acceptance issue: [#56](https://github.com/CultureBotAI/CMMMech/issues/56).

Six narrow commodity records were created from the round13 product-standard
handoff. Their evidence establishes traded product identities, without assigning
the five unresolved EU grade umbrellas to those products. These records carry no
criticality designation, chemical-entity identifier or microbial mechanism.
They preserve hydration states and distinguish producer specifications from
universal qualification rules. A chemical formula describes nominal product
composition; it is not an assertion of an impurity-free chemical entity.

| New root | Primary identity/specification evidence | Qualification limit |
|---|---|---|
| lithium-carbonate | Albemarle product-family page and complete 2018 product 401125 sheet; SAMR YS/T582-2023 identity | Technical, battery and pharmaceutical grades differ. A stated cathode application of the technical product is not proof of universal battery qualification. |
| lithium-hydroxide-monohydrate | Complete Albemarle product 401106 sheet, issued 6 July 2018, LiOH.H2O formula; SAMR GB/T26008-2020 title | The sheet's minimum 55% is LiOH assay, not 55% monohydrate purity. Anhydrous LiOH remains distinct. |
| nickel-sulfate-hexahydrate | Primobius hexahydrate formula/use; complete Coremax version 8 one-page specification dated 2 July 2024 | Primobius publishes at least 22.0 wt% Ni; Coremax more than 22.3 wt% Ni and customer-specific options. These are different producer criteria, not contradictory measurements. |
| manganese-sulfate-monohydrate | Pan Chem complete monohydrate powder sheet and Ihumate formula/specification; Walsun homepage battery-use context and SAMR HG/T4823-2023 registry | Initial Walsun table access could not be reproduced, so its precision claims were excluded. Independently verified agricultural products establish the monohydrate identity, not battery qualification. |
| ferroboron | ISO10386:1994 catalogue scope; Bomet BMTQB2016 No.BMT16-204 enterprise table | Alloy family with several grades, not pure boron or stoichiometric FeB. Full ISO standard not acquired. |
| graphite-anode-material | SGL Carbon February 2020 brochure pp.7–9,20–21; SAMR GB/T24533-2019 product title | End-use subset of graphite, overlapping the broader record. Excludes complete/furnace electrodes, spent waste and separately described C/Si composites. Customer testing is not one universal purity standard. |

The records link the exact producer and issuing-registry URLs. All six public
record paths and actual CREATE history paths/hashes are recorded in the
[companion JSON](round14-product-boundaries-20261011.json). Standards catalogues
were used only for their visible product identity, scope and edition metadata.
They were not represented as having supplied unavailable technical tables.

## Sources inspected and access boundaries

The complete three-page Albemarle sheets were read through the web reader,
including their formulas, application/specification sections and dated imprints.
Direct downloads returned 403. Reader exports are retained as transcripts with
their own hashes; they are not falsely labelled original PDF checksums.
The Coremax sheet and 24-page SGL brochure were acquired as actual PDFs and their
relevant sections read. SGL's final-page imprint is `02 2020/1 2N`, and its
disclaimer states that general product information does not guarantee particular
application suitability. The record does not transfer its marketing comparisons
or production-volume claims into scientific evidence.

Primobius's original HTML supplies the hexahydrate formula and nickel-content
table. Bomet's original HTML labels its table as enterprise technical conditions,
with steel/foundry, permanent-magnet and amorphous-material uses. This does not
define every jurisdiction's metallurgy-grade boron. Its table contains header
and transliteration ambiguities, so no numerical impurity table was imported.

Walsun's first opened primary page displayed its Basic information, Application
and entire Specifications table. A subsequent direct download and repeated
reader opens returned the manufacturer homepage, although the indexed primary
page still returned the complete table. The retained downloaded HTML is therefore
explicitly classified as a homepage, not a captured specification. The initially observed table is retained only as an access finding; no Walsun
numeric specification is present in the final record. Complete independent
[Pan Chem product sheet](https://www.panchemcorp.com/pdf/product/Manganese-Sulfate-Monohydrate-Spec-Sheet.pdf)
and [Ihumate manufacturer page](https://www.ihumate.com/manganese-sulfate-monohydrate)
were then read through the web reader. Their monohydrate powder/formula and
agricultural end-use descriptions independently establish the commodity. Pan
Chem direct acquisition returned406 and Ihumate returned403; the retained
combined reader transcript is explicitly not an original PDF/HTML checksum.
The accessible Walsun homepage is used only for its broader sulfate battery-use
context, without asserting that its unavailable detailed table was verified.

SAMR registry pages for all six previously proposed standards were acquired and
their title/version metadata read. Three linked official openstd entries
(graphite, hydroxide monohydrate and ferroboron) exposed preview/download controls
but yielded a browser-support message through the reader; complete standard
contents were not obtained. Vendor sales previews and unauthenticated third-party
uploads were not treated as complete authoritative standards. The old Arcadium
hydroxide-sheet link redirected to Rio Tinto's homepage and supplied no evidence.
Raw files remain in `/private/tmp/cmm-round14-product-raw`; exact origins, checksums and failures are in JSON.
No raw producer document or copyrighted standard is committed.

## Preserved source conflict

The [SAMR registry](https://std.samr.gov.cn/gb/search/gbDetailed?id=A73D6262FE9172E3E05397BE0A0A6CEB)
reports 1 April 2021 for GB/T26008-2020 implementation, whereas its
[linked official openstd entry](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=EDE35159DCEFEE4EBD50689B422430DD)
reports 1 May 2021. This conflict remains unresolved. The new hydroxide record
cites the edition without choosing an implementation date. The round13 report
is retained as the earlier observation; its stated date is not promoted to a
resolved current fact. Neither metadata value changes the hydrate identity.

## Five umbrellas still deferred

`boron-metallurgy-grade`, `graphite-battery-grade`, `lithium-battery-grade`,
`manganese-battery-grade` and `nickel-battery-grade` remain in research.
The newly read producer specifications improve narrower product coverage but
do not prove an exhaustive mapping of those authority designations. Complete
product standards, their original technical tables/test methods and explicit
authority interpretation are still needed before claiming a general boundary.
The new roots do not change the old 94-candidate authority inventory's five
deferrals or constitute five new exact-key matches.

## Microbial leads and excluded inference

Targeted searches tested the exact product/hydrate names with microbial recovery,
bioleaching, bioprecipitation and crystallization terms. No mechanism was curated
without verified methods and final product identity. This is a bounded access
result, not a claim that microbial routes do not exist.

1. [Biswal et al. 2018](https://doi.org/10.1021/acssuschemeng.8b02810)
   is the strongest lithium-carbonate follow-up: the institutional abstract
   describes fungal leaching followed by chemical precipitation. ACS full text
   returned 403; author NTU bibliography and HKUST institutional metadata identify
   the paper, but full methods/supplements were not acquired. Do not turn its
   abstract recovery number into a curated yield or call chemical precipitation
   direct microbial Li2CO3 synthesis. Acquire controls, reagent additions,
   product characterization, purity and denominator first.
2. [Rehmanji et al. 2025](https://doi.org/10.1039/d5ra06824j)
   is a geothermal-brine follow-up. Publisher abstract/indexed discussion describe
   microbial impurity-carbonate removal with Li retained in solution. It is not
   proof of lithium carbonate recovery. Full methods, supplements and controls
   were not investigated in this product lane.
3. [Graphite oxidation study](https://pmc.ncbi.nlm.nih.gov/articles/PMC4647224/)
   is a possible existing-graphite mechanism update; the primary search excerpt
   concerns bioelectrochemical graphite oxidation to graphene oxide. Verify
   actual electrode substrate and controls before curating; it does not establish
   recovery of qualified Li-ion anode powder.

Exact DOI correction/retraction searches for the two lithium leads returned no
applicable notice in the first result sets. No comprehensive notice audit or
full scientific review is claimed, and no unseen paper was used to fill a record.
The nonmicrobial nickel-sulfate crystallization and LiOH recovery papers found
during searching remain outside this microbial curation pass.

## Novelty and validation

Hidden and ignored files, with relevant symlinks followed, were included in
searches of records, research, reviews, histories and the cited round12/13 raw
directories. The108-line match log includes previous product proposals and
authority mentions. These six exact product roots were not present among the 101
baseline records. Binary PDFs are not claimed exhaustively searched by `rg`;
this is a bounded repository and cited-source check, not machine-wide novelty
or an exhaustive world-material search. The JSON lists all exact queries and
first-result-set coverage without pretending the searches were paginated.

Root baseline: 307 tests passed, 3 skipped, 101 records and 116 histories valid.
Named product validation: `Checked 6 record(s); 0 failed.`.
Actual CREATE events were generated through `just new-history` with issue 56,
GPT-6/codex provenance and separate inline events. Independent scientific reviews
and full batch gates are parent-owned and were pending when this source dossier
was created; this dossier is not a substitute for those review artifacts.
