# Fluorite source investigation, round 60

UTC: 2026-10-12T14:48:42.878957Z
Actor: codex / GPT-6 / codex. Trusted base: `3ac02ecf15ba53e28b15b2f4afcdcb083d0a226c`.

## Decision and owner

Accept `data/records/fluorite.yaml` (mineral) for authority-grounded CaF2 identity and washed-cell-associated aggregation/settling. This is distinct from the existing fluorspar commodity and fluorine element. No designation is inherited and no dissolution, isolated-product recovery or deployment is claimed. Record SHA-256 `5c4e6129dd9b54b5236ea6baa7bf306b4dec037fb69a3b96d03d113dadbe5f6e`. Actual CREATE sidecar: `history/records/fluorite/2026-10-12T144633Z-codex-8f4754.yaml`; SHA-256 `8fb506a0acb5e3003d6574bd364e5db9fb62395b76716400f8e886d267dc4873`. The inline event is separately timestamped.

## Primary sources and inspection

- **Haas et al. 1999**, DOI10.1590/S0001-37141999000300007, Revista de Microbiologia30,225–230. Complete six-page original from indexed Semantic Scholar mirror, official SciELO full text and Crossref independently matched. All six original figures, Table1, equation and methods/results/discussion visually inspected. Natural source-stated99%CaF2 crystals from Criciuma, Brazil; washed C.xerosis cells; 1L jars,10g/L mineral, specified stirring and sampling depth. This closes the round12 original-access gap for this narrowly scoped experiment, not a commodity-recovery gap.
- **Rigo et al. 2002**, DOI10.1590/S1517-83822002000400010, Brazilian Journal of Microbiology33,331–332. Complete official HTML and original Table1 GIF inspected. PDF route returned502 HTML; page-layout inspection is not claimed. One scientific table, duplicated as thumbnail/full graphic in HTML; no further scientific figure/SI identified. It supplies a separate triplicate no-cell/polymer comparison, with source-related laboratory lineage. The initial local filename `haas2002.html` is a shorthand error in artifact naming, not source attribution.
- **IMA-CNMNC September2026**, fresh issuing PDF/landing: definitions page1, fluorite row page75, CaF2/G and unresolved original year. No approval accession invented. Complete Handbook fluorite datasheet inspected, with natural occurrences kept separate from its synthetic reference diffraction pattern.
- **NCBI1725**, current species Corynebacterium xerosis verified live. It does not authenticate either unnumbered experimental commercial stock.

## Controls, denominators and source conflicts

- Natural crystals source-stated99%CaF2, no experimental XRD, specimen accession or impurity assay. Not a mixed-ore beneficiation trial or fluorite grade certification.
- Commercial C.xerosis cultures have no strain/genome authentication. Washed-cell assay lacks killed-cell/supernatant controls or viability measurements; physical microbial association not demonstrated metabolism.
- 1999 solids removal denominator is loss of sampled suspension concentration relative to initial concentration; not dissolved fluoride or isolated product. Jar temperature/replication unavailable; electrophoresis20readings not jarreplicates.
- 1999 prose40mg/L96% optimum conflicts with visibly continued Figure4 increase; Figure3 plotted baselines differ. Exact optimum/turbidity baseline reduction not adopted.
- 2002 Table1 triplicate means/SD retained; bacteria40mg/L versus polymers2mg/L and none; pH at endpoints differs, including7.30 versus6.85 for cells/none. Polymer effects contradict microbial necessity or superiority.
- 2002 HTML grinding unit37mm versus400#Tyler unresolved; no silently repaired size. Complete HTML+original Table1 used without claiming acquired print PDF.
- No criticality transfer from fluorspar commodity/fluorine element; no industrial deployment, metal dissolution or mineral-isolation yield.
- No affecting correction/retraction identified in bounded returned web sets or Crossref update-to metadata; this is not exhaustive notice clearance.

Table1 of Rigo2002 was read from the original graphic, not reconstructed from prose: cells40mg/L give97.3±0.2%solids removal; none12.2±2.1%; anionic/cationic/nonionic polymers at2mg/L give99.2±0.7%,96.6±1.6%,50.3±3.8%. These are reported suspended-solids endpoints, not percentages of calcium or fluoride recovered. Cell residual turbidity33±16.2NTU is more variable than anionic polymer31±1.7NTU. Stated initialpH6±0.5 differs from measured equilibrium values; matched-pH causality is not established. Detailed values and source locators are preserved in the record.

## Deduplication and search boundary

`rg --no-ignore --hidden -L` searched current and original `data/records`, `research`, `reviews`, `history` for material, organism and exact primary DOIs. Both yielded12 matching files; only maintained fluorine/fluorspar identities matched. Referenced local roots from matching documents were searched with hidden/ignored inclusion and followed symlinks, text extensions,8MB/file and20s/root bounds. Binary PDFs/images were not machine-searched; selected originals were personally inspected. The receipt includes literal references that are files or punctuation-bearing tokens and clearly marks them non-directory, rather than silently claiming their contents absent. Detailed roots/commands/results are in the paired JSON and `/private/tmp/cmm-round60-mineral-research/dedup.json`. No machine-wide novelty or source-exhaustion claim is made.

Live web searches included exact DOI/title and correction/retraction/control queries; default returned sets only. Crossref supplied no update-to notice. No affecting notice identified within this bound. The complete primary observations and explicit controls take precedence over favorable abstract wording.

## Deferred dissolution leads and next actions

1. **Dai et al. 2019**, DOI10.1080/01490451.2019.1654042, Geomicrobiology Journal36,933–939: direct fluorite dissolution is relevant, but full original graphics remain unavailable. Fresh ResearchGate and publisher PDF responses were403; institutional search endpoint400. Indexed methods are only a handoff. Acquire full seven-page original and figures/tables; resolve isolate identity, natural specimen characterization, glucose/acid arms and reported pH discrepancies before accepting any measurements.
2. **Alharbi2008**, landing-claimed DOI10.5897/AJMR.9000403: official PDF text visible through web, but no viewable original graphics locally; directPDF403 and alternate mirror timeout. Crossref404 and landing acceptance/publication-year disagreement, plus mirror2013 attribution, prevent unqualified source merging. Obtain authoritative original graphics and bibliographic resolution first.

Exact URLs, UTC acquisition events, HTTP/file-type failures, byte counts and SHA-256s are retained in the acquisition receipts. No identical denied endpoint was repeatedly retried. Raw literature remains outside Git at `/private/tmp/cmm-round60-mineral-research/raw`; the paired JSON inventories all 30 raw artifacts and 11 receipt files. Failed HTML payloads are retained for provenance and are not treated as PDFs.

## Validation and handoff

Actual named validation: `uv run --locked cmmmech validate data/records/fluorite.yaml` from `/private/tmp/CMMMech-expansion-round60-20261012`, terminal exit0; one record checked, zero failed. Exact log SHA-256 `6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e`. Baseline reused coordinator's exact-base initialization; full cohort gates and independent scientific review remain coordinator tasks. No test/schema changes needed for this data-only addition. This dossier is author research, not its own independent scientific approval.
