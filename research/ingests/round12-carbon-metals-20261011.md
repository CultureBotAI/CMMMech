# Round 12: carbon, metal commodities and battery-grade boundaries

Prepared on 2026-10-11 UTC by codex / GPT-6 / codex against trusted base
`1e52585c9019a32d37f959e0dafa00ae431f28c4`, for issue #48. This advances the
ten assigned proposals from [round 11](round11-frontier-20261011.json).
The [JSON receipt](round12-carbon-metals-20261011.json) contains per-proposal
decisions, exact queries, acquisitions, hashes, histories and reviewed locators.
Independent scientific review and whole-batch gates remain separate work.

## Decisions

| Proposal | This round | Identity and evidence boundary |
|---|---|---|
| magnesium-metal | Created, identity and designation only | Commercial metal; separate from element, compounds and every Mg-bearing alloy or scrap stream. |
| silicon-metal | Created, identity and designation only | Commercial silicon metal, including material refined further for solar/semiconductor use; separate from silica, ferrosilicon and silicones. |
| titanium-metal | Created, identity and designation only | Sponge and downstream metal forms; distinct from element, pigment and mineral concentrates. |
| coking-coal | Created with qualified laboratory evidence | Coke-making commodity, with a narrow culture-associated sulfur-content comparison in Tabas feed. |
| graphite | Created, identity and designation only | Natural-plus-synthetic commercial family; explicitly overlaps the existing natural-graphite subset. |
| graphite-battery-grade | Deferred | Resolve qualified product, morphology/impurity specification and performance evidence; origin alone is insufficient. |
| lithium-battery-grade | Deferred | Resolve carbonate, hydroxide or another qualified product; leached lithium is not automatically battery grade. |
| manganese-battery-grade | Deferred | Resolve sulfate/electrolytic or another product and its impurity specification; Mn ions/oxides are insufficient. |
| nickel-battery-grade | Deferred | Distinguish qualified nickel sulfate from Class I nickel/intermediates and verify product specifications. |
| metallurgical-coal | Deferred | Reconcile wider EIA steelmaking use with narrower USGS coke-making usage before mapping the US designation. |

The [USGS 2026 commodity chapters](https://pubs.usgs.gov/periodicals/mcs2026/mcs2026.pdf)
support the three metal-product boundaries: printed pp. 122–123, 170–171 and
196–197 (PDF pp. 126–127, 174–175 and 200–201). Text was inspected for both
pages of each chapter; the first page of each was also rendered and viewed.
The PDF was reused from the round-9 acquisition and rehashed, not claimed as a
fresh download. No production estimate, tariff or inferred purity cutoff was
imported. The [USGS 2025 outlook](https://pubs.usgs.gov/publication/sir20255021/full)
independently separates magnesium metal from compounds and titanium sponge
from the other titanium markets.

## Exact dated designations

The full Annex I and II lists in the
[original Regulation (EU) 2024/1252](https://eur-lex.europa.eu/eli/reg/2024/1252/oj/eng)
were inspected. The record editions are the act of 11 April 2024, published
3 May 2024; this is not a consolidated-amendment audit or timeless claim.

| Scope | Original locator | Classification |
|---|---|---|
| magnesium metal | Annex I, Section 1(i) | strategic |
| silicon metal | Annex I 1(o); Annex II 1(ac) | strategic; critical |
| titanium metal | Annex I 1(p); Annex II 1(af) | strategic; critical |
| coking coal | Annex II 1(i) | critical |
| graphite | Annex II 1(v) | critical |
| graphite — battery grade | Annex I 1(k) | strategic; deferred root |
| lithium — battery grade | Annex I 1(h) | strategic; deferred root |
| manganese — battery grade | Annex I 1(j) | strategic; deferred root |
| nickel — battery grade | Annex I 1(l); Annex II 1(w) | strategic; critical; deferred root |

Broader element wording does not establish a finished product grade. Article
3(3) explicitly discusses synthetic graphite in the first strategic-list update;
the battery-grade qualifier remains material. Other inventory jurisdictions were
not automatically copied. The [US final 2025 list](https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm)
was inspected at its metallurgical-coal row, printed p. 50497, but that designation
was not silently transferred to the narrower coking-coal record.

## Coal identity and the accepted experiment

The EIA defines [coking coal](https://www.eia.gov/tools/glossary/index.php?id=Coking+coal)
by its suitability for making coke. Its
[metallurgical-coal entry](https://www.eia.gov/tools/glossary/index.php?id=Metallurgical+coal)
also encompasses pulverized coal used in steelmaking. In contrast,
[USGS Fact Sheet 2026-3061](https://pubs.usgs.gov/fs/2026/3061/fs20263061.pdf),
version 1.1, August 2026, pp. 1–2, uses coking/metallurgical terminology
interchangeably within coke production. Both source usages are preserved;
neither synonymy nor a universally disjoint split is asserted.

[Shahbazi et al.](https://doi.org/10.22044/jme.2023.13127.2387), JME 15(2):581–595
(2024; online 7 October 2023), is the accepted primary experiment. The full
15-page publisher PDF was acquired, its English text read, and Methods 2.4,
Tables 3–5 and Figures 4–5 visually inspected. The PE feed and mixed culture
were investigated in acidic shaken flasks; post-treatment HCl washing precedes
the reported analysis. The internally consistent PE sulfur comparison supports
a narrow association with inoculation. Thymol-containing uninoculated controls
also change sulfur content. Culture chemistry and washing were not separately
isolated. Replicate counts and error-bar meanings remain unspecified.

The record preserves the source's conflicting ash assignments and non-PE
percentages; it accepts no cross-method ranking. Its percentages concern residue
concentrations, not a sulfur mass balance or recovered product. Neither retained
coking performance nor industrial operation was demonstrated. Exact substrate,
conditions, observations and limitations are in [coking-coal.yaml](../../data/records/coking-coal.yaml).
The journal landing identifies CC BY 4.0; the raw PDF remains outside Git.

## Graphite family and battery products

The newly acquired [USGS Graphite 2021 yearbook](https://pubs.usgs.gov/myb/vol1/2021/myb1-2021-graphite.pdf)
(advance release December 2024), pp. 32.1–32.2 / PDF pp. 2–3, provides the
additional grounding needed since the round-10 deferral: it treats natural and
synthetic graphite together as commercial streams while accounting for each
separately. Both pages were read and viewed. The new family record explicitly
overlaps [natural graphite](../../data/records/natural-graphite.yaml); it does
not rename that record or imply a second disjoint natural-graphite commodity.
The yearbook's natural-graphite battery-purification example does not define
every battery product.

The [JRC 2023 foresight report](https://rmis.jrc.ec.europa.eu/uploads/CRMs_for_Strategic_Technologies_and_Sectors_in_the_EU_2023.pdf),
Table 16 continued on printed p. 243 / PDF p. 246, explicitly distinguishes
precursors and intermediates. It lists lithium carbonate/hydroxide, manganese
sulfate/electrolytic manganese, nickel sulfate with upstream nickel materials,
and natural/synthetic graphite paths. This is evidence for separate product
forms, not one universal grade threshold. The inspected 2025 Commission
[lithium](https://webgate.ec.europa.eu/circabc-ewpp/d/d/workspace/SpacesStore/760da134-e3de-4421-a3d4-751cbea62e9a/download)
and [manganese](https://webgate.ec.europa.eu/circabc-ewpp/d/d/workspace/SpacesStore/41471143-52cd-429f-9c76-c6359286d3aa/download)
single-page factsheets name strategic uses without supplying a qualification
specification; their placeholder ISBN/DOI strings are not accepted identifiers.

Roy 2023 (`10.1021/acssuschemeng.2c07262`) remains a deferred primary lead under
the [round-10 access and evidence limits](round10-graphite-20261011.json);
no fresh full-text acquisition is claimed. The new
[Recycling 2026 lead](https://www.mdpi.com/2313-4321/11/8/142) explicitly limits
its graphite result to a non-battery use. Direct access returned 403, so its
methods and measurements are not curated. Generic metal solubilization does not
demonstrate a qualified battery precursor.

## Search, acquisition and review handoff

The local search included ignored and hidden files, following links, across
`data/records`, `research`, `reviews`, `history` and cited round-9/10 graphite
and titanium raw directories. The bounded inventory enumerated 586 paths with
no symlinks found. An exact new-source DOI/title search returned no prior
matching references within that boundary before the records were written.
This is not a machine-wide or literature-wide absence claim. Existing titanium,
silicon, magnesium, lithium, manganese, nickel and natural-graphite records were
treated as related material scopes, not missing records.

The JSON records 32 web queries and the primary-page follow-ups. Searches
included controls, null effects, product specifications, and exact-title
correction/retraction terms. No matching correction/retraction notice was found
in returned results; this was neither exhaustive nor a Crossmark audit.
Magnesium antibacterial/abiotic-corrosion and alloy-metabolite leads were not
recast as microbial magnesium-metal recovery. Quartz purification was not
recast as silicon-metal production. Existing titanium passive-film evidence
was not duplicated as metal recovery.

Raw materials and tool receipts are retained in
`/private/tmp/cmm-round12-carbon-metals-raw`. Initial sandbox DNS failures were
retried as authorized public read-only acquisitions. The purported JRC141715
2025 PDF returned HTTP 200 but only a 245-byte HTML rejection page: it was
rejected as a PDF and supports no claim. RMIS battery HTML contained navigation
without its dynamic article; indexed content was only a discovery lead.
Other access failures, file types, times and SHA-256 values are in the JSON.

Named validation passed: **5 records checked, 0 failed**. Each record has a
canonical CREATE sidecar authored through `just new-history` with actual
codex / GPT-6 / codex metadata and issue #48, plus a distinct inline event.
The exact frozen record hashes and sidecar paths are in the JSON for independent
review. No README, prior record, Git or external publication mutation was made
by this workstream.
