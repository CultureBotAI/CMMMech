# Magnesium-carbonate source investigation, round 63

## Scope and provenance

- UTC: 2026-10-14T05:33:38.518153+00:00; curator codex (GPT-6; codex), agent `/root/round61_zinc_sources`.
- Worktree `/private/tmp/CMMMech-expansion-round63-20261014`, branch `curate/cmm-expansion-round63-20261014`, trusted base `1e3d834112099855c0398459415d0022336055f5`. Parent selected a bounded four-record publication batch; this investigator owns only dypingite and this source assessment.
- Question: which of dypingite, hydromagnesite and nesquehonite supports a new, distinct mineral owner with defensible microbial phase evidence? No criticality-list assessment was requested for these minerals, and no magnesium-element or magnesite-commodity criticality is inherited.
- Read local add-record/discover-sources workflows and source guide/template, CLAUDE, README, record contract, schema, validator, representative validation tests, nearby magnesite/glushinskite owners and the round17 saline source assessment. Existing `magnesite` is a commodity record; neither it nor elemental magnesium is a substitute for a hydrated carbonate species.

## Search and acquisition log

All 14 exact web queries are in the paired machine manifest. They were run on 14 October 2026 UTC, with first returned result sets only, no pagination or domain filter. Individual query seconds were not retained; this is explicitly date-level logging. Direct opening of the publisher Power2007 article succeeded; Open University, Southampton, UCL, CiteSeer and Granada full-text routes failed as detailed in the request receipts. Search-engine indexing of a PDF is not acquisition or inspection of its original figures.

Shell acquisitions preserve requested/final URLs, start/finish UTC, HTTP status or transport error, MIME/signature, bytes and SHA256. The first seven requests failed DNS in the restricted shell; a permitted read-only network retry succeeded. Those initial zero-byte target files were replaced by the successful retry, so initial response hashes are historical request receipts, not the current retained file hashes. Current retained-file checksums are listed separately. No authentication, payment, access-control bypass or author contact was attempted. Failed files ending `.pdf` are HTML, explicitly identified by signature.

The bounded local deduplication used `rg --no-ignore --hidden --follow` over `data`, `research`, `reviews` and `history` and then 379 existing raw directories cited by those materials. Text formats were YAML/JSON/Markdown/text plus HTML/XML in raw roots, with an 8 MB per-file bound. Binary semantics without extracted text were not searched. Only two repository reports matched before creation: the round17 saline assessment and ingest handoff. Raw matches included prior reference-list mentions of the 2011 and 2012 studies in round12 and round16 artifacts; these are known leads revisited, not first literature discovery. There was no pre-existing owner among the three target names in the searched record text. This is neither a machine-wide nor literature-exhaustive claim. A cleaned dedup receipt explicitly separates non-directory reference tokens from genuine searched directories; the initial regex's 1,430 excluded tokens are not claimed to be missing raw directories.

## Candidate inventory

| Candidate/source | Actual inspected evidence | Decision |
|---|---|---|
| Dypingite; [Power et al.2007, DOI10.1186/1467-4866-8-13](https://doi.org/10.1186/1467-4866-8-13) | Complete publisher 16-page original; methods/results/discussion text, all seven main figures and both tables visually inspected | Curate laboratory biofilm-associated phase formation with explicit limits |
| All three identities; [IMA September2026 list](https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf) | Fresh issuing-authority PDF and home page; definition page1 and rows on pages60/98/154 visually inspected, terms page2 read | Dypingite A,1970-011; hydromagnesite G,1828; nesquehonite G,1890. Years for G rows are not approval numbers |
| Nesquehonite/dypingite; [Mavromatis et al.2012](https://doi.org/10.1016/j.gca.2011.10.019) | Crossref/OpenAlex metadata and indexed abstract; complete originals not acquired | Defer additional mechanism/phase attribution; preserve reported null-effect lead |
| Hydromagnesite; [Sánchez-Román et al.2011](https://doi.org/10.1016/j.chemgeo.2010.11.020) | OpenAlex and institutional bibliographic metadata; Granada returned504 twice, CSIC links a restricted-access notice | Defer culture claim pending complete methods, phase table and controls |
| Mg-carbonate cultures; [Balci et al.2016](https://doi.org/10.1080/01490451.2015.1099763) | Institutional/indexed abstract and OpenAlex locations only | Secondary full-text handoff, no claim accepted |
| Atlin landscape; [Power et al.2009](https://doi.org/10.1016/j.chemgeo.2009.01.012) | Complete author-hosted15-page PDF acquired/rendered; only title, abstract and DOI screened this pass | Context lead, not a newly verified hydromagnesite mechanism |

## Dypingite source assessment

The current publisher PDF and Crossref establish the 2007 paper identity. Its title-page author rendering is Sasha Wilson; an indexed older copy uses Siobhan A Wilson. The record uses surname-only citation and makes no inference about this metadata difference. The publication date is 5 December 2007, distinct from this round's access date. IMA's September2026 page60 lists dypingite as approved, IMA1970-011, formula Mg5(CO3)4(OH)2·5H2O. Hydromagnesite differs by hydration, and nesquehonite's current IMA formula is Mg(CO3)(H2O)2·H2O. The dypingite row's more recent structural reference is not an experimental mechanism source.

The curated claim concerns the **laboratory** experiment, not proof of industrial recovery or pure-species causality. Sections3.2–3.5 describe three successive enrichments over three months to obtain carbonate-free filamentous cyanobacterial biomass. Ten-milliliter filtered natural groundwater and wetland-water systems were incubated for six weeks at room temperature in sunlight. The wetland biological arm received nitrate and phosphate, whereas described abiotic controls contained filtered water alone. The field Lyngbya label is not a strain-resolved identification of the enrichment, so no taxon CURIE is assigned.

Figures5A–B and6 identify the products as predominantly dypingite using morphology, EDS and micro-XRD. Figure5C and Table2 show nesquehonite in the unadjusted wetland abiotic system; the groundwater abiotic system had no precipitate. Table2 is an endpoint water-chemistry comparison, not an isolated-product yield. Its mg/L values are not converted to the schema's mg/kg concentration observations. Source-reported bulk pH and magnesium changes do not directly measure biofilm microniche pH or establish a uniform precipitation-rate enhancement.

Directly preserved limiting evidence:

- Figure5D and Sections4.3/5.1 show dypingite also in a NaOH-only control at pH10.3, alongside nesquehonite and an unidentified magnesium carbonate. Thus phase occurrence is not a unique biosignature or proof of biological necessity.
- Section3.2 specifies **0.5 M NaOH**, Section4.3 **0.1 M**. Section4.3 describes approximately equal parts of three phases; Section5.1 calls nesquehonite dominant. These internal discrepancies are retained, without choosing a dose or inventing phase fractions.
- Nutrient matching is not demonstrated for the wetland comparison. Axenic species-level causality, a direct microsite-pH measurement and replicate-level precision for the phase comparison are not established by the reported protocol.
- The separate field microcosms contained pre-existing carbonate that prevented identifying newly precipitated phases (Sections4.2/5.1). Field solution depletion is therefore not a dypingite-specific yield. Minor dypingite in the field abiotic precipitate may reflect post-collection nesquehonite decomposition.
- Figures1/3 and their text acknowledge minor nesquehonite potentially due to evaporation after collection. Morphology alone does not substitute for phase identification.
- Thermodynamic discussion uses hydromagnesite as a proxy because dypingite thermodynamic data were unavailable; that calculation is not an experimental hydromagnesite product identification.

Original figure coverage: pages3,4,7,9,10,11 and13 contain Figures1–7; pages7/11 contain Tables1/2. All were viewed as rendered originals. Page15 (supplement description) was also viewed. Remaining claim-relevant methods and discussion were read as extracted text. The additional video is an acid-carbonate screening demonstration, not phase-specific XRD. A guessed publisher supplement path failed DNS and the video was **not inspected**; no inference from it is accepted.

## Counterevidence, terms and acquisition limits

Exact-DOI correction/retraction searches returned no relevant notice in the examined sets. Fresh Crossref Power2007 and Mavromatis2012 metadata have no `update-to` and empty relations; this bounded check is not proof that no notice exists. The 2012 abstract reports that Gloeocapsa presence did not affect bulk hydrous-Mg-carbonate precipitation rates or Mg isotope fractionation within the reported uncertainty. This is a relevant warning against extrapolating the Atlin result, but its unavailable methods/tables/figures prevent accepting detailed phase-specific claims or treating it as a direct replication. No 2012 measurements are curated.

Power2007 is labeled CC BY2.0 on page1. The IMA list states CC BY-SA3.0 on page2. Power2009 is an author-hosted copyrighted Elsevier article; general redistribution rights were not established. The failed-access 2011/2012 originals remain unverified, regardless of search-index snippets. Full text and rendered images remain outside Git; committed material contains curation and provenance only. This cohort is not a bulk reusable dataset: no schema importer, accession join or general measurement extraction was justified.

Key retained originals:

- Power2007: `4adde86fabe8e1aa0709b0454c884d5e5434616a923a94f1ade21dd7cd96e8be`.
- IMA2026-09: `2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973`.
- Power2009, acquired but only screened: `92d52beae6ab9818bc868a775a0a86efdccb43831b599260a74e7f834ba9d01c`.

## Priorities and handoff

1. Independently assess `data/records/dypingite.yaml` and its final attached CREATE history; the source curator is not its scientific reviewer. Named validation passed at 2026-10-14T05:32:00.419209+00:00: `Checked 1 record(s); 0 failed.`. Parent baseline passed before accepted record writing; final batch/history/review gates remain the coordinator's responsibility and are not claimed here.
2. Focused proposed source-gap issue: acquire a legitimate complete Mavromatis2012 original and inspect its phase/time/biotic-control assignments before adding a nesquehonite mechanism or extending dypingite's quantitative claims. Preserve the null-rate result and avoid pooling it with the Atlin experiment.
3. Separate focused source-gap issue: acquire Sánchez-Román2011 (Granada or another authorized institutional copy) or Balci2016 complete primary, then verify hydromagnesite phase patterns and matched controls. Power2009 can be fully assessed as a field-context fallback, with weaker causal scope made explicit.

Final record SHA256 `dda0701dc49edb424e05e386bc8bfcd7859e9999b1c376949272c9e6979907c3`. CREATE history `history/records/dypingite/2026-10-14T053128Z-codex-2f510c.yaml` SHA256 `e3f20a1ce49d303c65f90884e15179e1f4d1eeef621d3b202c39c0eba53f7523`. No accepted nesquehonite/hydromagnesite record was created. No schema/validator change was needed. No issue was posted by this investigator. No claim of source exhaustion is made.
