# Uramphite source investigation

UTC: 2026-10-11T22:23:03.523877+00:00

Researcher: Codex `/root/round27_eaf_slag` (GPT-6; codex). Worktree `/private/tmp/CMMMech-expansion-round36-20261011`, branch `curate/cmm-expansion-round36-20261011`, trusted base `1ef6fdde620a4053fbfff99c51065082dce32d39`. This is a curation dossier, not the required independent scientific review.

## Selection and identity

The [new uramphite record](../../../data/records/uramphite.yaml) has SHA-256 `9a75ded70935425b4d938cb62081a28b767a9df66b7c22a8734df54912a014eb` and [CREATE history](../../../history/records/uramphite/2026-10-11T221946Z-codex-45fbfb.yaml) SHA-256 `7cd7271813793147abfbf3a59b8737ba7e3975302392e028ae652528e842edbd`. The current official [IMA September 2026 list](https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf), original PDF page 224, identifies uramphite as (NH4)(UO2)(PO4)·3H2O. Pages 1–2 distinguish status G, grandfathered, from approval status A; 1957 is the original-description year, not an approval ID. The mineral is not elemental uranium, a dissolved uranyl reagent or the U(IV) product ningyoite. No criticality is inferred from uranium and no unsupported mineral CURIE is invented.

The accepted microbial observation uses the complete original [Khijniak et al. 2005 article](https://doi.org/10.1128/AEM.71.10.6423-6426.2005), pp. 6423–6426. It is exactly the same experiment already represented from its product perspective in [ningyoite](../../../data/records/ningyoite.yaml), not independent replication. Here the material owner is the starting uramphite phase. This distinction and the original source deficiency boundaries are explicit in the record.

## De-duplication and access

Before record creation, `rg --no-ignore --hidden --follow` searched material names, the accepted DOI and selected lead DOIs in `data`, `research`, `reviews` and `history` under both the round36 worktree and original checkout. Ignored and hidden files were included. The relevant cited download roots were round35 ningyoite research/review, round34 uraninite research and round33 pyrite research. Seven PDFs in those four roots were independently text-extracted; symlinks were followed with cycle prevention, with no symlinks or extraction errors encountered. The matches confirmed existing study reuse and the earlier frontier handoff, with no separate maintained uramphite record before this addition. This is a bounded search, excluding unrelated home/temp trees, environment packages and Git internals, not a machine-wide absence claim.

The original Khijniak repository PDF was downloaded in round35 at 21:38 UTC on the same date and rechecked here, not represented as a fresh download. Its five PDF pages include the repository cover and four complete article pages. I read the full text and visually inspected every article page, all Figure 1A–F panels, all four Figure 2 loading arms and both Figure 3 panels. There are no tables in those article pages. No supplement is cited in the inspected article. The external basal-medium recipe in the cited 1997 paper remains outside the acquired full methods: its publisher HTML contains abstract/metadata, not the full recipe.

Fresh NCBI API and Crossref requests returned verified public metadata. The historical taxon spelling resolves to **Carboxydothermus ferrireducens, NCBITaxon:54265, species**, without proving a strain. Sandbox DNS failure on the first public requests is retained separately from the successful permitted retry. Direct PMC web access challenged the browser; the complete repository original supplies the primary evidence. A mistaken initial PMC identifier is explicitly excluded in the paired JSON. Raw papers and images remain outside Git.

## Evidence and adversarial limits

The initial yellow solid formed abiotically when uranyl acetate was injected into medium containing 2.4 mM phosphate. Page 6423 and Figure 1A assign this precipitate to uramphite by characteristic XRD lines, including material sampled immediately and after 68 h in uninoculated medium. This is stronger than formula matching, but Figure 1D describes a mixture of crystals and no quantitative purity is reported. It is a precipitated laboratory analogue, not a natural ore feed.

The standard assay used a 5% fumarate-grown inoculum, anaerobic bicarbonate medium at initial pH 7, 2.5 mM U(VI), 0.2 g/L yeast extract, 10 mL liquid in 27 mL tubes, 65 degrees C, darkness and no agitation. Methods say 3 mL/L glycerol while Figure 3 says 30 mmol/L; these are not silently converted or equated. The base assay had no added reducing agent; separate growth comparisons included sulfide. U(VI) was measured separately in supernatant and acid-dissolved centrifuged solids. Duplicate sample preparations are reported, but independent culture replication is not clearly distinguished. The experimental strain accession is not expressly identified in this article.

The cultures reduced predominantly solid-phase U(VI), with a product assigned by XRD to ningyoite and accompanying U(IV)/phosphate XAS evidence. The source reports approximately 80–90% U(VI) reduction within 68 h at 1 or 2.5 mM in Figure 2; this is not a mineral-specific mass yield, phase fraction or recovered uranium product. Figure 3 is a separate growth comparison, not an interchangeable percentage endpoint. No reduction or growth occurred at 5 or 10 mM. Uninoculated controls retained the starting precipitate and U(VI). The observed dissolved pool means a dissolved-intermediate pathway remains possible; neither a direct-contact mechanism nor an electron-transfer protein is established. Long-term stability, natural-ore treatment and industrial recovery are untested.

Exact-DOI searches for correction, erratum and retraction returned no relevant notice in their first result sets; fetched Crossref relation/update fields provide no such link. These limited searches do not prove absence of notices. The full article itself discusses earlier resistant solid-phase sediment U(VI); its cited field system is not silently treated as an uramphite-specific refutation or a new independently inspected experiment.

## Candidate inventory and follow-up

| Source | Evidence inspected | Decision |
|---|---|---|
| IMA September 2026, uramphite row | Original PDF pages 1, 2 and 224; live official URL | Accepted mineral identity |
| Khijniak 2005, DOI 10.1128/AEM.71.10.6423-6426.2005 | Complete original article and all three figures; fresh Crossref | Accepted scoped reduction observation; explicit existing-study reuse |
| NCBI taxon 54265 | Fresh original-name API response | Accepted species ID only |
| Slobodkin 1997, DOI 10.1099/00207713-47-2-541 | Publisher abstract/metadata HTML | External medium detail deferred; no strain inference for the 2005 assay |
| Pan 2015, DOI 10.1016/j.jhazmat.2015.05.019 | Publisher preview and EPA metadata | Acquire complete primary, figures and SI before any formation extension |
| Caulobacter 2014, DOI 10.1128/AEM.01050-14 | Source phase-assignment passage supplied by sibling researcher | Deferred: uramphite and K/Na uranyl-phosphate candidates are alternatives; no definitive owner inferred |
| X-27 study, DOI 10.1016/j.jenvrad.2023.107126 | Publisher abstract discovery | Deferred; no abstract measurements curated |
| Gurzhiy 2025, DOI 10.2138/am-2024-9313 | IMA reference and discovery metadata | Natural-material crystallography follow-up; no secondary-source space group claim |

First priority is independent review of this frozen record and the cohort gates. Subsequent formation extensions require complete original evidence and mineral-specific phase/control checks. The Caulobacter alternatives need resolution before genetic phosphatase evidence can support a particular mineral owner. No additional mechanism was inserted merely to broaden the record.

## Checks and provenance

Named validation completed with exit 0: **1 record checked, 0 failed**. The new canonical CREATE was generated by `just new-history` using actual codex/GPT-6/codex metadata and attached separately from the inline creation event. Full batch history/review checks and independent review are delegated to the cohort coordinator and are not claimed complete here. Baseline evidence explicitly reuses the already completed fresh checks on the exact unchanged base; it was not rerun by this curation task. No schema, validator, tests, existing record, governance or shared document was changed by this task.

The [paired JSON](20261011T222303Z-source-investigation.json) records exact search strings and bounds, source roles, original versus fresh acquisition states, URLs, timestamps, all retained artifact SHA-256 values, record/history hashes and the actual validation receipt. Raw material is retained outside Git at `/private/tmp/cmm-round36-uramphite-research` and the cited existing download paths. The IMA original declares CC BY-SA 3.0; the article declares ASM copyright. Public access is not taken as permission to redistribute full text. No measurement dataset import or schema extension was needed.
