# Round 18: manganese product source assessment

## Scope and provenance

UTC 2026-10-11T11:17:09.078802+00:00; codex/GPT-6. Base `26cb0688effb2f71e4a570c416f6f43ff858c5ab`, branch
`curate/cmm-expansion-round18-20261011`; two new identity-only commodity records
and CREATE sidecars. This assesses manufactured electrolytic manganese metal
(EMM) and dioxide (EMD); it does not settle a universal battery-grade designation.
Existing manganese, pyrolusite, manganese-sulfate-monohydrate and round13/14 grade
reports were checked. Hidden and ignored files and relevant symlinks were included
in the bounded repository/raw paths recorded in the paired JSON's dedup receipt.
No existing record matched the product names in that pre-write inventory;
prior research proposals did. Binary sources were separately inspected.

## Search and acquisition log

The paired JSON retains the ten exact web queries, first-result-set limits,
actual acquisition UTC times, successful HTTP/file-type checks, raw paths and
SHA-256 hashes. No exact query time is invented. Complete manufacturer HTML,
both one-page grade PDFs and the relevant USGS/JRC pages were inspected.
PDF pages visually checked: MMC LO/LH p1; USGS PDF2 and7 (printed47.1,47.6);
new JRC PDF67 (printed53). The retained older JRC version was reopened and hashed,
not represented as a fresh download. Sources are reading evidence, not an import
dataset; raw copyrighted files remain outside Git. Source-specific reuse limits
are recorded in JSON. Source versions have no guaranteed update API.

## Candidate inventory and source assessments

1. **EMM — curate commodity identity.** [MMC refinery](https://www.mmc.co.za/what-we-do/electrolytic-manganese-metal-emm-refinery)
   describes cathode deposition and product preparation. Its
   [product page](https://www.mmc.co.za/products/electrolytic-manganese-metal-emm)
   distinguishes flake and powder; mixed Mn-Al briquettes are excluded from this
   root. [Tosoh](https://www.tosoh.co.jp/product/functionality/mangan_electrolytic_metal.html)
   supplies alloy-use context. These support `description`/`sources`, not a
   microbial mechanism or inherited criticality.
2. **EMD — curate commodity identity.** [Tosoh](https://www.tosoh.co.jp/product/functionality/electrolytic_manganese_dioxide.html)
   describes electrolytic manufacture, alkaline-battery use and lithium-manganate
   precursor context. Its representative active-oxygen assay expressed as MnO2
   is not a universal phase-purity measurement. No mineral species is assigned.
   [USGS 2020 chapter](https://pubs.usgs.gov/myb/vol1/2020/myb1-2020-manga.pdf),
   published September2024, Table3 printed47.6 distinguishes chemical/electrolytic
   synthetic MnO2 manufacture. Historical data are not current market statistics.
3. **Manufacturer grade limits — preserve disagreement.** The MMC LO specification,
   Grade40 revision000 dated21August2017, distinguishes total Mn minimum99.6%
   from Mn(Met)99.9% excluding nonmetallic components. LH Grade01 similarly
   separates total Mn99.7% and metallic99.9%; no visible LH date is inferred from
   the other sheet. The LO sheet oxygen maximum0.15% conflicts with webpage0.1%.
   No numeric qualification is curated; resolution needs producer clarification
   and an explicitly dated applicable grade. The page's certification link is
   not evidence of current validity. This source discrepancy does not undermine
   the process/product identity.
4. **JRC source delta — context only.** The newly downloaded `/rmp/` artifact has
   134pages and an unresolved overall edition; the retained `/rmprofiles/` version
   has282pages and cover date14September2023. Both group EMD+HPEMM+HPMSM for a
   historical battery-grade capacity account. This grouping is not a technical
   qualification or direct legal designation. Keep URLs, hashes and page locators
   distinct; neither changes the five deferred grade boundaries from round13.

## Priorities and handoff

The two product identities have genuine CREATE histories and individual validation
exit0. Their independent scientific reviews remain a separate acceptance step.
Prioritize the open2026 iron-reductant paper for assay reassessment, then obtain
complete Xin2011 electrolytic-manganese-residue methods for a potentially distinct
secondary feed. Resolve BCTOM2016 full methods/product endpoint before extending
existing ore records or asserting final EMM. The ACS2018 full-main gap remains.
The 2024 ACS bioleachate/MnO2 lead requires an original DOI and legitimate access;
an institutional-proxy search hit was not used. Chemical precipitation does not
establish electrolytic manufacture. Exact DOI/title/access requirements are in JSON.

## Limits and unresolved questions

This bounded search is not exhaustive. Correction/conflict coverage includes the
logged EMD query and explicit manufacturer document comparison; it is not a full
review of the newly discovered mechanism papers. No snippet percentages were
accepted. Product identity does not qualify every member for a battery end use.
No new organism CURIE, material CURIE, criticality claim, measurements or microbial
mechanism were added. No schema change is demonstrated. Unknown grade limits,
source inconsistencies and missing primary methods remain research questions.
