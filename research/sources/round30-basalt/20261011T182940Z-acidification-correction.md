# Basalt analytical acidification correction

UTC: 2026-10-11T18:29:40.928688+00:00

Author: codex (GPT-6; codex), original curator. Base `930ce995269f0ded5df009eb5916162971eb1f58`. This is a correction handoff, not independent scientific acceptance.

Independent root review found a minor source-interpretation defect, tracked in [issue 107](https://github.com/CultureBotAI/CMMMech/issues/107) and [the immutable initial native review](../../../reviews/structured/20261011T182728Z-basalt-round30-independent-initial/review.md), finding `acid-concentration`, issue key `cmmmech-basalt-acidification-concentration`.

The original [source assessment](20261011T182352Z-source-investigation.md) and record described acidification **to** 0.3 M HNO3. Chemical Analysis on PDF p6 instead states that 4.5 mL filtered solutions were acidified **with** 0.3 M HNO3. It provides neither added acid volume nor final acid concentration. The value is therefore a reagent specification. This correction supersedes that specific statement in the original assessment; the original dossier, CREATE history and initial review are preserved unchanged.

The [record](../../../data/records/basalt.yaml) now uses reagent wording and explicitly leaves final sample acid concentration unspecified. The [canonical EDIT sidecar](../../../history/records/basalt/2026-10-11T182847Z-codex-c03537.yaml) links issue 107 and the independent finding; a separate inline EDIT event records the correction. No organism, feed, outcome, mechanism or deployment claim changed.

Named validation completed with exit 0: `Checked 1 record(s); 0 failed.` Receipt `/private/tmp/cmm-round30-basalt-research/corrected-named-validation.json`. Corrected record SHA-256 `e7f999badce7c3ebca3fe28a56827f602d4162b5b6e4b00729b06b019001e1e5`. EDIT sidecar SHA-256 `07ae8c7a21f53c93de4e4363d68980ffdcdf14c36b83d16da62adb000305808d`. Parent final batch gates and an independent successor disposition remain pending.

Complete source PDF retained at `/private/tmp/cmm-round30-basalt-research/raw/primary.pdf`, SHA-256 `cf5067359aaf42d8696ab61fe6b50f3d3000774cdc62dd250cc48cbff6ab9b2f`. The [paired JSON](20261011T182940Z-acidification-correction.json) pins prior artifact hashes and exact correction provenance. No historical source assessment or review was overwritten.
