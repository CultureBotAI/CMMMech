# Independent bounded review: expansion authority inventory

## Reviewed artifacts, revision and time

- Reviewer: Codex (GPT-6), delegated agent `cmm_curate_tellurium`; independent of the authority-inventory author. This agent authored tellurium, but no tellurium scientific acceptance is part of this review.
- Review started UTC: 2026-10-11T04:05:09Z.
- Review completed UTC: 2026-10-11T04:08:31Z.
- Reviewed repository HEAD and accepted inventory base: `76cd81d310a6ccb4cf7bdebcc61be050d0863222`.
- Worktree: `/private/tmp/CMMMech-expansion-20261011`; branch `curate/cmm-expansion-20261011`.
- JSON: `research/sources/expansion-authorities/20261011T040103Z.json`; SHA-256 `fb5cc04b2a937a82571511a712eeb646b577f2bae9ec3f0c2837852d00e69e69`.
- Markdown: `research/sources/expansion-authorities/20261011T040103Z.md`; SHA-256 `cddba86921200d2f9c1227f5001a1c055409082a830ac0fffcc515856a665b27`.
- Both reviewed artifacts are untracked working additions at this revision. Final Markdown readability changes and the explicit chalcopyrite deferral were reread before these hashes were captured. Other concurrent changes (new copper/nickel/tellurium records, dossiers, histories and structured reviews; README, packaging/lockfile and recipe-test changes) are outside this audit. No reviewed inventory bytes were edited by this reviewer.

## Scope and method

This is a bounded authority-discovery audit, not a fresh exhaustive review of all nine list roles or acceptance of 94 scientific records. Programmatic checks cover the complete JSON and Markdown candidate table. Primary-source spot-checks cover the requested EU, Australian and UK distinctions. No new record identity, microbial mechanism, industrial deployment, or worldwide completeness claim is certified.

Repository/cache searches used `rg --no-ignore --hidden`; ignored files were included. The ten-record accepted-base set was established independently with `git ls-tree` and `git show`, so concurrent untracked records cannot alter that historical coverage calculation. No absence claim is made about unrelated home or temporary directories.

## Evidence checked and results

1. **Counts and referential integrity:** all authority keys, designation IDs and candidate keys are unique; all 268 designations resolve to authorities and candidate keys; every candidate support link resolves to the same authority/designation and has a matching reverse link. Within-designation candidate links are unique. Classifications match their list role. Per-list counts are 60/34/17/34/31/5/34/23/30, totaling 268 across nine roles and six jurisdictions. All 94 candidates have support links. The Markdown table matches every JSON key, proposed kind and base status.
2. **Accepted-base identity:** independently recomputed all ten record hashes from Git; every stored hash and the complete base path set match. Seven represented element candidates link to those base records; 87 are unrepresented at that base. Mineral species and the secondary resource are not equated with authority commodities. Copper, nickel and tellurium correctly remain unrepresented in this historical snapshot despite their concurrent additions.
3. **Qualification and priority clarity:** generic nickel and battery-grade nickel remain separate proposed scopes; broad/qualified graphite and coal keys are explicitly provisional. Group concepts use proposed commodity scope, not mineral groups. All 94 candidates explicitly defer identifier verification and microbial evidence. Priority classes total 39 general evidence searches, 30 identity-resolution candidates, 15 next primary-evidence searches, seven existing-record enrichments and three current-batch curations. The prose describes a coverage/workflow judgment, not evidence of experimental readiness or 87 necessary new roots.
4. **EU original 2024 act:** independently extracted retained authentic PDF pages 55, 57 and 58. Both annexes qualify nickel as battery grade; Annex II lists graphite without a natural-only restriction. The combined bauxite/alumina/aluminium scope and strategic qualifiers are preserved. A fresh [official PDF request](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202401252) returned no usable document. This review therefore supports only the stated original edition, not current consolidated law. Retained PDF SHA-256: `eb89f374a725ebde267c90f237898cd1d0bdfa65a1d4a118511e225bde60283e`.
5. **Australia:** freshly read the [department's complete list page](https://www.industry.gov.au/publications/australias-critical-minerals-list-and-strategic-materials-list), including the revision statement, Table 1 and footnotes 16–17. The REE footnote enumerates 16 members, includes promethium and excludes separately listed scandium. The PGE footnote enumerates six including osmium. Nickel is critical; copper belongs to the five strategic materials. These source-specific distinctions match the mappings. Foreign-list comparison columns were not used to establish other jurisdictions' current status.
6. **UK:** freshly read [government Annex 1](https://www.gov.uk/government/publications/uk-critical-minerals-strategy/critical-minerals-technical-annex). Copper and uranium are growth materials, and the growth PGM subset is Ir/Pt/Rh/Ru. Growth remains outside the current critical/strategic schema classification. Independently extracted retained [BGS OR/24/047](https://nora.nerc.ac.uk/id/eprint/538471/1/OR24047_report.pdf) PDF pages 11, 48 and 228 using an isolated PyMuPDF environment, and visually inspected rendered page 11. The source supports palladium below the threshold, sodium compounds, and the 17-member REE definition. PDF SHA-256: `1a72206ff4e1b8d6cbc2a350e28338f192e264a3ba6c31a5d8dbb28262e35dc5`. Fresh web PDF access exceeded the provider's size limit; retained bytes were used honestly.
7. **Acquisition provenance:** every receipt with a stored SHA-256 matches its retained file (nine files, including empty EU failure responses and two prior EU acquisitions). The Australian timeout has no invented checksum. All nine authority entries retain jurisdiction, edition, URL, locator and acquisition state. Failed acquisition and prior acquisition are distinguished.

## Findings by severity

- Blocking/high: none found in this scope.
- Medium: none found in this scope.
- Low: none requiring correction found in this scope.

These are bounded findings, not proof that all 268 source labels and every membership mapping were independently reread from all nine primary lists.

## Corrections

None requested or applied. The inventory author's readability cleanup was not treated as a scientific correction; final bytes were reread and hashed.

## Unresolved questions and limitations

Current consolidated EU legal status remains unverified; Canadian group membership and provisional commodity/grade identities require follow-up before curation. US, Canada and India source membership was not independently re-audited exhaustively in this review. Source-reuse licensing statements were not independently certified. A local raw-file hash proves byte consistency, not source truth. Primary microbial experiments and exact chemical/mineral identities must still be checked for each future candidate. The inventory explicitly retains these boundaries and makes no exhaustion claim.

## Verdict

**Pass with limitations for the authority-discovery handoff.** Counts, links, historical representation, stated provenance and the sampled nonobvious authority distinctions are supported. This verdict does not accept future records or imply a complete global CMM inventory.
