# Isolated verification and report audit

UTC: 2026-10-16T03:59:55.031684Z. Reviewer: codex /root/round104_ree (GPT-6). Trusted base `0482e7b0af9b18685dabe310dbe86487b6ac4226`; working tree `/private/tmp/CMMMech-expansion-round110-20261016`.

Scope: bounded static review of the two isolated-verification helpers, measured configuration and round110 report. No cloning, mutations or additional project tests. I did not author these helpers or the report; I authored the two REE owners, borate scientific reviews and separate dossier-locator disposition, which are disclosed rather than self-reviewed as independent science.

## Evidence and assessment

- Main-only clone uses explicit --single-branch main --no-tags, then fetches tags and checks the main-only fetch refspec. Topic commit absence is checked before and after shape construction and after validation.
- Preflight requires clean exact topic HEAD/tree in the retained worktree and remote main at trusted base; archive contents form a new synthetic commit parented by the base. Postmerge requires both topic refs absent, clone HEAD equal the supplied merge SHA, and exactly the trusted base as sole parent. Both paths require the exact reviewed tree.
- Strict nonempty record validation, history validation against the trusted base, canonical review-check --require-reviews, and exact-hash coverage execute in the isolated clone. Each subprocess row records actual cwd, timestamps, exit and allowed exits. The terminal receipt binds log, config, verification helper, coverage helper and coverage output digests, with helper/config rechecks before success.
- Coverage enumerates filesystem YAML including hidden/ignored paths and follows symlinks with directory-cycle prevention. Completed positive scientific reviews must match record ID, target path, reviewed scope and exact current owner hash; all referenced review bases must be available commits. Counts must equal the measured configuration.
- Report seven owner/review hashes, all eight dossier sizes/hashes, final batch receipt/log digest and successful command rows independently matched. Local coverage receipt reports 555 records, 631 histories, 648 native reviews, 111 bases and 555 covered records; all listed owner and matching-review digests were reread and matched.
- Report retains the initial natroboltwoodite finding and successor, dossier-only issue451 correction chain, skill-only issue445 process correction and six open evidence followups. README rows preserve synthetic/natural, laboratory/industrial, phase identity/recovery and operational-fraction boundaries.
- Both scripts parse as Python. Review was static and read-only; no clone, publication helper or project test was executed by this auditor. Initial question about coverage-helper attribution was addressed before this final audit by adding its digest and final recheck.

Exact reviewed input paths, sizes and hashes are recorded in the paired JSON. Verification helper SHA256 `0d9211b663de4edb2319355e4f5a61541eb2b25f2e0810d94844e6d9c3737ea5`; coverage helper SHA256 `7afaef22c3c4967d262a95f36f0eff9aa825db2dc8c873c4d719f7c2386b2d44`.

## Findings and verdict

No supported corrective defect in this bounded static scope. **Pass with limitations.** The later canonical corpus review gate, committed-head review, real isolated checks and hosted publication still need their actual successful receipts. This audit is not queue or merge approval by itself.
