# Round 61: fungal fluoride evidence and source follow-ups

UTC: 2026-10-13T02:23:53.231647+00:00. Worktree `/private/tmp/CMMMech-source-followups-round61-20261013`, branch `research/cmm-source-followups-round61-20261013`, trusted base `78ba2f4c84ff84be64b0da23e603f59c761905aa`. PR190's Pages deployment is included unchanged in that base.

## Curated outcome

Updated [fluorine](../../data/records/fluorine.yaml) with a separate conditional fungal inorganic-fluoride mechanism. The corpus remains **278 records**. The complete four-page 1984 original supports culture-associated release from supplier-precipitated CaF2, with control-subtracted endpoints and no positive CaF2 response in the separate soil assay. It does not establish natural-fluorite dissolution, an isolated fluorine product or industrial deployment. Loading, carbon-source and isolate-label conflicts remain explicit. Existing identity, Australian 2024 criticality and recombinant-culture evidence are unchanged.

This handoff was selected because the original methods and all four tables were acquired and inspected. The competing zinc-residue, Dai fluorite and lead-paste candidates still lack required original evidence. No unsupported new material owner was created and no schema change was needed.

The actual [EDIT history](../../history/records/fluorine/2026-10-13T021024Z-codex-6d1850.yaml) remains distinct from the inline event. Independent [scientific Markdown](../../reviews/structured/20261013T022022Z-fluorine-round61-independent/review.md) and [YAML](../../reviews/structured/20261013T022022Z-fluorine-round61-independent/review.yaml) cover the final record: **pass_with_limitations**, zero corrective scientific findings. The reviewer independently inspected all four new original pages and proved earlier fields unchanged, explicitly carrying forward their prior scientific review rather than claiming to have rechecked their literature live.

## Source investigations and remaining work

| Priority | Outcome and next action |
|---|---|
| [#186](https://github.com/CultureBotAI/CMMMech/issues/186) | [Zinc-residue assessment](../sources/round61-zinc-residue/20261013T020740Z-source-investigation.md) resolves the exact AppendixS1 deposit and thesis file/NNT/DOI. Original graphics and thesis phase evidence remain unavailable; retain loading and modeling questions before curation. |
| [#187](https://github.com/CultureBotAI/CMMMech/issues/187) | [Fluorite assessment](../sources/round61-fluorite/20261013T021048Z-source-investigation.md) verifies Dai's partial 16S accession and strengthens Alharbi's 2008 bibliography. Obtain their original graphics and resolve protocol discrepancies. The older synthetic-feed study does not close this natural-mineral gap. |
| [#191](https://github.com/CultureBotAI/CMMMech/issues/191) | [Lead-paste assessment](../sources/round61-lead-paste/20261013T020440Z.md) records the full-original gap. An OpenAlex OA label points to an abstract page; obtain and inspect the complete primary before accepting assay or recovery claims. |

All three source issues remain open. Earlier source priorities in the [round60 frontier](round60-frontier-20261012.md) also remain; this bounded pass does not claim source exhaustion. Retained raw artifacts stay outside Git with origin/access/checksum records; reading permission is not treated as redistribution permission.

## Review correction and validation

Adversarial publication review found one minor source-attribution error, saved in the immutable [initial finding](../../reviews/publication/20261013-round61/20261013T021411Z-publication-initial.md) and tracked as [#192](https://github.com/CultureBotAI/CMMMech/issues/192). The report now attributes author verification to Crossref and limits publisher-API corroboration to the fields actually present. Its manifest pin was refreshed with explicit correction provenance. The scientific reviewer re-inspected the corrected pair. The final publication disposition follows separately under [publication reviews](../../reviews/publication/20261013-round61/); closure of192 belongs to the eventual merged PR.

Baseline and final `just check` both passed: **317 tests, 3 skipped**. Final nonempty validation passed 278 records; trusted-base history passed 327 sessions. Rendering and render-check passed. Native review-check passed 338 bundles; separate exact-ID/path/hash coverage is **278/278**, with 62 available review bases. The [machine manifest](round61-frontier-20261013.json) pins actual commands, logs, hashes, scientific artifacts and declared scope. Validators do not establish scientific truth.

At this timestamp the local implementation and scientific review are complete. Final independent publication audit, commit, hosted checks and native SQUASH/ALLGREEN queue follow. Saved review bases must remain available after squash and branch deletion; fresh-checkout checks will verify that. Original main and the unrelated skill worktree were independently checked including hidden/ignored entries: 7,187 and 7,389 entries respectively preserved. No fleet/governance configuration was changed; future integration uses CLAW's supported process.
