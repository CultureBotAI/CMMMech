# Independent review: CMM source-discovery skill and landscape report

## Reviewed state and scope

UTC: **2026-10-08T07:44:26Z**. Reviewer: `/root/claw_register_cmm` (Codex, GPT-6), separate from the coordinating report author and its three source investigators.

Checkout `/private/tmp/CMMMech-source-survey-20261008`, branch `research/cmm-source-survey-20261008`, base `905388523b6e9184783989484896e4cc20297832`. Reviewed working changes comprise the discovery skill and two references, the three-file landscape assessment, and the copied independent forward test. The file hashes below identify this uncommitted reviewed state. Scientific records, schema, sidecars and governed artifacts are outside the change.

Scope: skill usability; evidence and acquisition boundaries; source dates, licensing and identities; quantitative wording; reproducible source handoff; local links; and separation of discovery from scientific acceptance. This is not a new per-record review or exhaustive reanalysis of all sources.

## Evidence checked

- Read the full skill, references, consolidated report/search log/evidence JSON, source investigators' fragments, repository guide and schema. The independent [forward test](20261008T073611Z-source-discovery-forward-test.md) began from supplied raw BES files without reading the coordinator's derived analysis. Its acquisition limits and exact observations remain in that immutable artifact.
- Independently reproduced BES dictionary/assay counts, negative-value coding, the blank potassium value, nonunique experimental grouping and 22/22 normalized date/sample joins. Directly read the metadata's laboratory methods, controls, units, CC0 statement and update policy.
- Independently reproduced MCS counts: 8,886 rows, 12 columns, 127 commodity labels, 102 cobalt rows, 15 blank units, 720 interval-year entries and 20 duplicate groups for the stated candidate key. These justify the skill's added dictionary/key/date checks.
- Independently opened the retained RRUFF ZIP: 25 files, five specimen IDs and 1,238 numerical pairs in the named processed R060020 spectrum. This is a bounded format sample, not a mineral-recovery dataset.
- Spot-checked the retained primary HTML against M1/M2 laboratory conditions and total-REE versus relative-improvement wording; M3's ore-derived culture, loading discrepancy and substrate-specific null results; and M4's culture conditions, abiotic comparison and qualified Mn-speciation interpretation. Remaining source assessments were checked against the investigators' source-specific evidence and declared limits, without claiming all remote authorities or supplements were reacquired by this reviewer.
- All **23 retained-file receipts** containing a path/file and SHA-256 match the currently retained bytes. Successful IMA/RRUFF and BES metadata receipts now contain local paths; initial primary HTML receipts retain original acquisition timestamps recovered by the coordinator from the source investigator's tool history. This reviewer verified those files/hashes and the explicit recovery annotation, not the original network transactions. No fresh download is implied. The Nature redirect's transient code is explicitly omitted, with original source URLs retained.
- All **eight relative Markdown links** in the reviewed report, skill and forward-test files resolve. The evidence JSON parses. `git diff --check` passes.

## Findings by severity and corrections

- **Critical:** none identified.
- **Major:** none identified within the assessment scope.
- **Minor, corrected — assay identity:** E1 initially described all 87 T3 rows as aqueous analyses. The file includes solution and digest samples. The final text calls these ICP-OES assay rows and distinguishes electrode, holder/filter and reference-frit fractions. It now also states the inspected recovery table has no Sb row and only an initial-abiotic As row. The landing's five-element scope is not treated as five equivalent biological recovery experiments.
- **Minor, corrected — retained provenance:** four successful acquisition receipts lacked local paths, and three retained primary HTML files lacked receipts in the checked-in evidence manifest. Final receipts supply paths, original acquisition provenance, hashes and sizes. These corrections preserve original times rather than presenting rechecks as new downloads.
- **Minor, corrected — organism spelling:** the report now describes M3's organism as the culture reported as *At. ferrooxidans*, with genus spelling unresolved. The article's title/abstract spelling is not silently normalized into an independently verified taxonomic identity.
- **Informational:** the 12 entries deliberately include known authorities, related studies and sampled datasets; they are not claimed as 12 novel independent experiments. Unavailable EU annexes, occurrence rows, Mendeley files, and unsampled supplements remain explicit gaps. Criticality editions, chemical forms, mineral species and specimens remain distinct. No new curated record, validated microbial effect size, isolated-product yield or industrial deployment is claimed.

## Validation and limits

The coordinator reports successful skill `quick_validate` and `just check`: lint passed, **215 tests passed with three empty optional-command cases skipped**, and the unchanged three records and three histories validated. This reviewer did not rerun the full gate; independent checks are enumerated above. Repository validation establishes existing contracts, not acceptance of the new scientific source claims.

The corrected source assessment retains dataset-specific terms or explicit unknown licensing, separates catalogue dates from release/version dates, and logs failed acquisition attempts as failures. The scoped search cannot establish universal absence of sources or corrections. Future curation still requires resolved identifiers, exact claim-level evidence and independent timestamped record reviews.

## Verdict

**Accept the reviewed local skill/report state.** The skill passed a realistic raw-data forward test, the three minor review findings are resolved, and no outstanding required correction remains. This approval does not authorize a publication or record import and does not substitute for future scientific record acceptance.

## Reviewed file SHA-256

| Path | SHA-256 |
| --- | --- |
| `.claude/skills/cmmmech-discover-sources/SKILL.md` | `52bfb4803adbf394c82c3b47b1eb8c1928ddf7cb35aa81ed8ff50de9cd569e21` |
| `.claude/skills/cmmmech-discover-sources/references/source-guide.md` | `893e38956eaaca8430a0957b8ecbe5539d23d01a363c9f7fbbc029de2b057090` |
| `.claude/skills/cmmmech-discover-sources/references/report-template.md` | `79e2494b02e49fda12724b47221ff3c282893e70a5bf96d772dcfd04b0633e41` |
| `research/sources/cmm-landscape/20261008T073140Z.md` | `176b6b8c824f8c761fb1a62f0c7656f70b667f6eb46ee57b3ec0ea4e8ac4c890` |
| `research/sources/cmm-landscape/20261008T073140Z-search-log.md` | `06205d82969b9590eb8d22d20c6db460348dcce3f135aa4221571264badff450` |
| `research/sources/cmm-landscape/20261008T073140Z-evidence.json` | `35e5447248fdfd303a27308b837c217577b69f88d1f48353707283573d4c4e0e` |
| `reviews/process/20261008T073611Z-source-discovery-forward-test.md` | `395cd5b7b09e805637fa0f0852aac0e7299bff8213d300552928862893a727d2` |
