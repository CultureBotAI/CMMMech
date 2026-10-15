# Round85 sulfides source investigation: wurtzite

Researcher: codex (GPT-6; codex), `/root/round68_iron_sulfides`. This is a curation handoff and source assessment, not independent acceptance of the authored record. Final assessment assembled 2026-10-15T01:20:45Z. Actual baseline PASS was verified before maintained writes; the final owner and canonical history are frozen below.

## Scope and deduplication

The selected material is the hexagonal ZnS mineral **wurtzite**, distinct from cubic sphalerite, elemental zinc, a zinc commodity and an unspecified ZnS nanoparticle. No criticality list was curated, so no jurisdictional designation is inherited.

The trusted base is `51adf4be6c544642f6bf54a4e7f514adb84aa34e`; owned worktree `/private/tmp/CMMMech-expansion-round85-20261015`, branch `curate/cmm-expansion-round85-20261015`. Both this tree and the original main tree were searched in `data/records`, `research`, `reviews` and `history` with `rg -n -i --hidden --no-ignore --follow`. Exact material spellings, the 2012/2016 DOIs and 2023 DOI suffix were included. The only maintained text hit was a natural-association mention in `cadmoindite.yaml`; `sphalerite.yaml` accepts different Fowler/Crundwell leaching experiments. There was no wurtzite owner or accepted experimental duplicate within this bounded search. Exact commands, output hashes and stderr are retained in `dedup-summary.json` and `dedup-root-{0,1}.txt`.

Relevant prior cited-download roots `cmm-round77-sulfides-research`, `cmm-round82-sulfides-research` and `cmm-round83-sulfides-research` were searched with hidden/ignored files and followed symlinks. Their text matches were contextual Handbook/search-result references, not accepted duplicates. Binary PDFs were not treated as searchable text without extraction; the retained searchable text and artifact inventories were checked. This is not a machine-wide or literature-wide absence claim. The current all-state issue snapshot contains 285 entries after flattening its paginated JSON; none matched the selected identity or verified studies. Root refreshes live issue deduplication before publication.

## Search and access

All searches occurred on 2026-10-15 UTC. The initial web queries were `microbial wurtzite zinc sulfide bacteria XRD nanoparticles primary`, `berzelianite microbial copper selenide bacteria XRD`, and `clausthalite biomineralization bacteria lead selenide`. Subsequent exact-title/DOI searches located the UNIA thesis, the MDPI official PDF and the PNNL Xu2016 institutional bibliography. Search-result captures are retained under `round85-search*.json` and `round85-wurtzite-fullweb.json`. The final bounded conflict/notice queries were:

- `"10.1016/j.scitotenv.2012.02.013" correction OR corrigendum OR retraction`
- `"10.3390/nano13050935" correction wurtzite`
- `"Castillo Hernández" "PROCESOS BIOGEOQUÍMICOS" 2013 tesis`
- `"wurtzite" "sulfate reducing" sterile control zinc`

The provider response is retained in `round85-correction.json`; no date filter or exhaustive pagination was applied. No resolving notice surfaced in those returned results. Both acquired Crossref responses have empty relation fields and no update-to/updated-by entry. This is bounded notice screening, not proof that no correction exists. The control-oriented query also returned a 2021 mine-community study and older comparative work as follow-ups; neither is adopted without a separate complete assessment.

The PMC browser route for the 2023 study returned a challenge, and the MDPI page open failed in the browser tool. Legitimate official `mdpi-res.com` PDF and Europe PMC XML routes then succeeded. These were route failures, not claims that the primary PDF was unavailable. No challenge was bypassed. Acquisition times, requested/final URLs, MIME types, sizes and SHA256s are in `acquisition-initial.json`; raw files and copyrighted original images remain outside Git.

## Accepted primary and identity sources

**Castillo Hernández2013 thesis.** [Institutional handle](https://hdl.handle.net/10334/2563), complete143-page original, electronic2013 edition, ISBN978-84-7993-915-1. Actual file `castillo-unia-thesis.pdf`, SHA256 `088266e2a2a87aad68c73ceb55620f328c03618b89fe1b48f96f2f8a54be8d20`, acquired2026-10-15T01:07:26.218693Z via the UNIA bitstream. The accepted experiment is complete Chapter2, printed18–39/PDF42–63; all text and all original Figures2.1–2.7 were inspected. Chapter2 cites Castillo et al.2012, DOI[10.1016/j.scitotenv.2012.02.013](https://doi.org/10.1016/j.scitotenv.2012.02.013), as its basis. This is one experimental lineage, not independent replication. Appendix PDF139 contains only the journal first page. The complete nine-page journal article and its independent supplement state were not verified; the accepted source is explicitly the thesis chapter. No separate supplement is referenced for the chapter. Whole-thesis chapters3/4 are outside accepted experimental scope. The institutional license is attribution/noncommercial/no-derivatives; complete text and page images are not redistributed in the corpus.

**IMA September2026.** Complete previously acquired original `/private/tmp/cmm-round80-carbonates-research/ima2026-09.pdf`, SHA256 `2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973`, rechecked this round rather than freshly downloaded. The original page236 row and page1 field definitions establish name Wurtzite, ideal ZnS, statusG and original-description year1861. No approval accession is minted from that year. Current raw contains the original-page236 render and extracted row. This is a dated mineral identity list, not a criticality authority.

**Handbook of Mineralogy.** [Complete one-page entry](https://www.handbookofmineralogy.org/pdfs/wurtzite.pdf), actual `wurtzite-handbook.pdf`, SHA256 `16d58b02258e3b151b5ddcd8ba0d78154a1e168946bed29d5674d8246a0eb4b6`, freshly acquired and visually inspected. It describes hexagonal (Zn,Fe)S and synthetic2H P63mc. Its Fe-bearing formula is compatible with substitution; it is not a reason to replace the IMA ideal ZnS formula. Older polymorph terminology beyond sphalerite is not adopted without current authority checks. Handbook copyright remains with its publisher; raw stays external.

## Claim map and adversarial limits

| Claim | Exact original locator | Accepted scope / limit |
|---|---|---|
| Three unresolved SRB consortia | Chapter2§2.1, printed25–26/PDF49–50, Fig2.1 | Mine sediment CM/ME and prior sludge-derived SS culture; no strain/sequence IDs or taxon-level causal role. |
| Living enrichment and Zn assay | §2.1–2.3, printed25–28/PDF49–52 | Separate35-day enrichment;42-day200mL synthetic Zn/lactate/sulfate assay under nitrogen/paraffin at room temperature. Five-percent dose belongs to enrichment only. Final Zn-assay inoculum dose is absent. |
| Mixed-phase wurtzite assignment | §3.2, PDF55–57, Fig2.6 | All three final solid patterns, W(103) near14.5°2θ atλ0.443Å; SS example decomposes overlapping reflections. This supports source-assigned mixed sphalerite/wurtzite, not phase-pure product or quantitative wurtzite fraction. |
| Filtered Zn depletion | §3.1, PDF53–54, Fig2.3d | Approx260mg/L to below unreported detection threshold at14/35/42days forSS/ME/CM. Never substitute zero or a recovered-product yield. |
| ZnS/cell/EPS association | Figs2.4,2.5,2.7, PDF55–58 | Microscopy/EDS association; individual images do not identify every particle's polymorph or establish exclusive biological nucleation. |
| Sulfate reduction interpretation | §3.1 and§4, PDF52–54/59–62 | Coupled solution chemistry and community MPN support the interpretation; direct dissolved-sulfide speciation, volatile-S assay and taxon-specific causality are unreported. |

The chapter gives no matched uninoculated, killed-biomass or chemically sulfided precipitation control. Duplicate-mean captions do not define independent reactor replication; MPNn=3 is a separate count. The initially larger SS community confounds comparative intrinsic tolerance. The source itself discusses biosorption and organic complexation as alternative contributions to Zn depletion. Washing in culture medium leaves carryover unresolved, and solids were centrifuged, frozen and lyophilized; final dried diffraction does not establish wet-culture phase history.

Source inconsistencies are retained rather than reconciled silently: Methods approximately3000mg/L sulfate versus Results/Fig2.3c approximately1400mg/L; pH7 nominal adjustment versus plotted starting pHapproximately6.3; Fig2.3 caption calls(c) zinc while zinc is in(d); Spanish summary prints<2.5nm aggregates whereas microscopy/Results describe micrometre spheroids. The3–6nm Scherrer estimate refers to the mixed ZnS crystallites, not a measured wurtzite-only size distribution. No criticality, purified-product yield, mass-balance recovery, long-term stability or industrial deployment is asserted.

## Screened and deferred sources

1. **Segura et al.2023**, DOI[10.3390/nano13050935](https://doi.org/10.3390/nano13050935): complete official14-pagePDF and fullXML acquired; pages1–3 and6–7, particularly originalFigure4, were assessed for phase fitness. The remaining antimicrobial/photocatalysis experiments were not independently assessed and are not curated. The phase paragraph assigns34°,36.2°,47.6° to hexagonal002/101/102 while its reported a,c,λ imply approximately27.98°,30.41°,39.22°. The reproducible calculation and original pixels are retained; this is an internal consistency concern, not a new alternative-phase identification. Figure4 labels major cubic peaks only. No supplementary-material element appears in the completeXML. This study is **deferred as wurtzite corroboration**, not counted as a second accepted experiment. A concrete clarification draft is `source-issue-draft.md`.
2. **Xu et al.2016**, DOI[10.1016/j.gca.2016.02.007](https://doi.org/10.1016/j.gca.2016.02.007), officialPNNL-SA-120162 bibliography: metadata describes biogenic/abiogenic mixed-ZnS comparison, potentially valuable controls. Complete original/graphics/SI were not acquired or verified in this bounded round; pursue legitimate institutional manuscript routes later. No measurements imported.
3. **Moreau et al.2004**, *Ultrastructure, aggregation-state, and crystal growth of biogenic nanocrystalline sphalerite and wurtzite*: institutional metadata and thesis citation only. Its stacking-fault interpretation is not transferred as a direct observation from Castillo's experiment.
4. Berzelianite and clausthalite were briefly screened against prior round77/82/83 leads. No new complete phase-specific microbial experiment was accepted. These names do not justify additional identity-only filler this round.

## Handoff and priorities

First curate/review the single thesis-supported wurtzite owner, preserving the narrower phase and control scope. Second resolve the2023 indexing question before treating that article as independent corroboration. Third inspect complete comparative ZnS controls from Xu2016 or other accessible primary work when a future update is warranted. Improving phase fractions, in-situ preparation controls and isolated-product balances would be more useful than adding nominal ZnS identities.

The raw acquisition receipt, exact dedup outputs, search captures, allChapter2 original-page renders, authority files, phase calculation and draft issue remain in `/private/tmp/cmm-round85-sulfides-research`. The paired JSON inventories exact hashes. No schema/validator change is justified. Named validation passed1/0; canonical CREATE history and a distinct actual-time inline event are attached. Independent scientific review and root batch gates remain pending and are not claimed by this source assessment.

## Frozen curation handoff

- Owner: `data/records/wurtzite.yaml`, SHA256 `3023a9fa6aa8f6f82b2284252f7245ad85ab1ff297f5cddaee53e61f2f4590a3`.
- Canonical CREATE: `history/records/wurtzite/2026-10-15T011942Z-codex-2cd232.yaml`, SHA256 `0134924e4afe1e980457c802a12753e7452f59da7c3279808e16b733eba770ea`.
- Named validation: one record checked, zero failures; `/private/tmp/cmm-round85-sulfides-research/named-validation.json` and `.log`.
- Baseline receipt: `/private/tmp/cmm-round85-baseline.json`, actual PASS01:18:29Z, trusted base as above.
- Independent reviewer must inspect the final owner/history before judgment; no self-acceptance is asserted.
