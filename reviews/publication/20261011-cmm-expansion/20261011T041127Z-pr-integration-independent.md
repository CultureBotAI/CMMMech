# Independent final PR integration review

## Revision, scope and independence

- Review timestamp UTC: 2026-10-11T04:11:27Z.
- Accepted base and current HEAD: `76cd81d310a6ccb4cf7bdebcc61be050d0863222`.
- Branch: `curate/cmm-expansion-20261011`.
- Worktree: `/private/tmp/CMMMech-expansion-20261011`.
- Reviewer: Codex (GPT-6), delegated agent `cmm_curate_tellurium`.
- Scope: current full working diff and untracked publication additions relative to the accepted base; integration consistency, exact review coverage, workflow correction and handoff inclusion. The hash manifest below records 29 files present at capture; this new review excludes itself to avoid a circular digest.
- Independence: reviewer did not author README, the justfile correction, its regression tests or dependency changes, the authority inventory, copper, or nickel. Reviewer authored tellurium and therefore performs **no fresh scientific acceptance of tellurium here**; the separate independent parent review supplies that acceptance. The reviewer's own nickel and authority reviews are checked for file coverage, not represented as new independent reassessments of those review artifacts.

## Evidence checked

1. **README and corpus integration.** All repository-local README links resolve. Its 13 material rows match the 13 record paths exactly, without duplicate or missing records. The three added summaries remain within their record boundaries: copper includes dissolved/precipitated release; nickel notes matched-pH controls and ore-dependent null results; tellurium distinguishes product-phase evidence from isolated yield. All ten accepted-base record files remain byte-identical to Git. No new mineral-species root is inferred from the chalcopyrite substrate or copper authority designation.
2. **Scope and governance.** Tracked changes are confined to README, justfile, pyproject.toml and uv.lock. The maintained schema, validator, CI workflow, vendored/governed helpers, local skills and prior corpus records are unchanged. Hidden and ignored files were included in scoped status/inventory checks of governance, code and test roots; only ignored Python build/cache products accompany the new recipe test there. New scientific additions consist of three records, three CREATE sidecars, source dossiers, inventory and saved review artifacts. Raw literature files remain outside this proposed Git change.
3. **Argument-forwarding correction.** All three variadic recipes use recipe-level positional forwarding with quoted `$@`. Nine maintained regression cases execute real just against a fake receiver, covering no arguments, multiword values, command substitution syntax, environment/glob literals, empty arguments, quotes, newlines and tabs. Sentinel checks detect evaluated substitutions. This verifies caller-text preservation without writing real history or records. Regression tests are not skipped if just is missing.
4. **Dependency and CI path.** `rust-just==1.58.0` is declared in the development extra and represented by one matching locked package with 16 platform wheels, including Linux x86_64. The strict CI workflow installs `uv sync --locked --extra dev`, then runs the local gate through `uv run --no-sync`; pytest discovers the new test. The existing check recipe also requests the development extra. README supplies `uv run just check` for an installed locked environment. No CI or governed artifact edits are required for this integration.
5. **Exact scientific-review coverage.** Independently recomputed every recorded input digest in the three new scientific bundles; all match current bytes, including records and their history context. Every bundle declares independent scientific review, uses the accepted base, has verdict `pass_with_limitations`, and has no findings. Copper: `20261011T040915Z-copper-expansion-science`; nickel: `20261011T040430Z-nickel-expansion-independent`; tellurium: `20261011T040423Z-tellurium-expansion-science`. This coverage check does not replace those scientific reviews.
6. **Issue #21 review lineage.** The initial `20261011T040637Z-variadic-wrapper-review/F1` remains intact with its historical open finding. The independent `20261011T041005Z-variadic-wrapper-resolution/F1` records a resolved disposition under the same issue key, `CMMMech.just-variadic-argument-preservation`, and explicitly links that exact predecessor. Its ten captured target/context input hashes all match current bytes. The successor documents nine passing regressions and three downstream CLI-help checks. This establishes a saved local disposition, not remote issue closure.
7. **Source handoff inclusion.** README links the authority inventory; JSON and Markdown are present. Its independent bounded review is saved alongside this review. Inventory hashes still match that audit. The inventory preserves 268 designations, 94 proposed concepts and accepted-base representation, without asserting 87 mandatory records or saturation. Source dossiers and review bundles accompany all three additions.
8. **Publication coverage report.** Read `review-coverage-and-bases.json`; independently checked its three current record hashes and issue #21 predecessor/disposition against the saved bundles. The parent owns its remote provenance-tag check. All new review bases point to the accepted base; no new review-source revision is introduced by this Markdown audit.

## Validation evidence and limits

The publisher and copper reviewer each report the final local gate passing with **307 tests passed, three skipped, 13 valid records and 22 valid histories**. The parent also reports 22 canonical artifact checks passed. These broader checks are attributed evidence, not a full-suite rerun by this integration reviewer. Independently inspected current diff, dependency/lock/CI agreement, all README local paths, unchanged baseline records and exact saved input hashes. `git diff --check` passed during this review. Remote PR CI, provenance publication, merge-queue result and issue closure remain the publisher's subsequent actions.

## Findings by severity

- Blocking/high: none found within scope.
- Medium: none found within scope.
- Low: none requiring correction found within scope.

## Corrections and unresolved questions

No new correction requested or applied. Issue #21 has an independent saved resolution. The scientific limits documented in each record and the authority inventory remain intentional; none is upgraded to industrial deployment, isolated recovery yield, global completeness or current-law certification by this review.

## Verdict

**Pass with limitations for local PR integration.** The three additions, review artifacts, discovery handoff and narrowly scoped workflow fix are consistent at the captured bytes. Proceed with the authorized publication workflow and its remote gates.

## Current working-file SHA-256 manifest

| Path | SHA-256 |
|---|---|
| `README.md` | `78c70cac10a21bebc09b2bb5f3ddb402e174e71673b96c4bfbd779ea4607f70a` |
| `data/records/copper.yaml` | `357e81e48e5a480359f485e380a26eecf8d5a125100f328d99b06c0dacaabbfc` |
| `data/records/nickel.yaml` | `b87ef9b7ab31d74980b5d6c57d7e74ba85a3d7860ca257cd30c0886c85aa47dc` |
| `data/records/tellurium.yaml` | `8de03e4ddd334be7f6adf1813384529600bdbab2b9b0dec6f0f394fdbab81f38` |
| `history/records/copper/2026-10-11T040209Z-codex-558c98.yaml` | `f53837b64ae6c21addafff734b117280869fa830a7cc4739feee4f7b2e2d483d` |
| `history/records/nickel/2026-10-11T040136Z-codex-dc4fc2.yaml` | `2e6d8bee0f9f1af9cd3697032ba0320ee19979feb22a01f3b4ced091d4e26163` |
| `history/records/tellurium/2026-10-11T040057Z-codex-bc6ab1.yaml` | `565ba88f23db358c418968066f3ae52de7250318493e44ddf3537a49525768cb` |
| `justfile` | `ab372446900aadfbbca2f1195c085cf100ef69cddb10a9ea52f74ecb441a8a4c` |
| `pyproject.toml` | `e6d0c71251d97a1b5f8b65ef9a0f6f8c04848e4de50bf4c3e46d96b9edc02eed` |
| `research/ingests/expansion-copper-20261011-acquisition.json` | `ef3544a05273dcabee2ed7de5a7238700873e26aedfd13e86052cef1f40ef436` |
| `research/ingests/expansion-copper-20261011.md` | `2e9e0eba0928cab04889a4359734573a6cd80bc9e1f05f84306e4dc1e54dfdc2` |
| `research/ingests/expansion-nickel-20261011.md` | `82dcab872ac2badf20c793155299e919185c7a9be4138633559505690b1913a0` |
| `research/ingests/expansion-tellurium-20261011.md` | `72727c1fd8d47f38134d3f88eecbd63106b9f77ebe137f6c21ac45de98dfb8a3` |
| `research/sources/expansion-authorities/20261011T040103Z.json` | `fb5cc04b2a937a82571511a712eeb646b577f2bae9ec3f0c2837852d00e69e69` |
| `research/sources/expansion-authorities/20261011T040103Z.md` | `cddba86921200d2f9c1227f5001a1c055409082a830ac0fffcc515856a665b27` |
| `reviews/publication/20261011-cmm-expansion/20261011T040831Z-authority-inventory-independent.md` | `b8a4df0a53bef502fc449abce49ef51bff95b951369d880d3e3ff9e2bca99e49` |
| `reviews/publication/20261011-cmm-expansion/review-coverage-and-bases.json` | `0951fe2d11133a37be55730d8db94e5fe40b29f277f0fed90d769a2cbdf4012d` |
| `reviews/structured/20261011T040423Z-tellurium-expansion-science/review.md` | `6146c9975faec75d6a4a92a4304bf7e20db3cbbb1ba7afe5158079fc47375bd6` |
| `reviews/structured/20261011T040423Z-tellurium-expansion-science/review.yaml` | `5f823d535773165b789e0aeb7a4a721a98fb969c9c3a3ad7bd41df33caa6af24` |
| `reviews/structured/20261011T040430Z-nickel-expansion-independent/review.md` | `a01c6a90a289c1ec2635bc4fae9e9acf5783734f9f926860d73768fc8cb092dc` |
| `reviews/structured/20261011T040430Z-nickel-expansion-independent/review.yaml` | `0a8bbf99b5fd1446b137d64b8fa9c159373e94ceae6947e30dd21b217e32a682` |
| `reviews/structured/20261011T040637Z-variadic-wrapper-review/review.md` | `038e0a07894d20c47758e8859ccbcdcf38467b9594eb3650637fc326ef94b6f6` |
| `reviews/structured/20261011T040637Z-variadic-wrapper-review/review.yaml` | `1c6b03b45836f19e4fe601e6def2025fa5f86b8bb742c6d07d07e8d3c8882fc2` |
| `reviews/structured/20261011T040915Z-copper-expansion-science/review.md` | `305081d80e3a9b31b3eede049a88552a1bde3ce7353ffbe5eafc55e9e4018c04` |
| `reviews/structured/20261011T040915Z-copper-expansion-science/review.yaml` | `f41c99ec214a7f774c6fd7302848ce14a929ed29025873378307266f771f1710` |
| `reviews/structured/20261011T041005Z-variadic-wrapper-resolution/review.md` | `828113c378f91649394cb7b9a179c4e7b86d9d0bfc99a2f945ceaf92903bc007` |
| `reviews/structured/20261011T041005Z-variadic-wrapper-resolution/review.yaml` | `4faf65b99764d80e83688da4db1a66a120f8d9ec051c9835180a0be5bf158023` |
| `tests/test_just_recipes.py` | `d458a511cb46d66c77ee02057a70b9fd30b2cef40275c22f21331e7252739bd2` |
| `uv.lock` | `473bfdb18b56d16f4b87672a4cd975b572c9f56db367db3d43cabaeeb2b055a7` |

## Unchanged contextual inputs

| Path | SHA-256 |
|---|---|
| `.github/workflows/validate-strict.yaml` | `3a00e7becf969a181f71bbc1b12875929400a6cedfdf56f287cdbfcf1c3ff134` |
| `scripts/check.py` | `69894bbe6480c4dbec56b8e15cf97e3ed6273078dd6ac1b929d73aab3a87301a` |
| `src/cmmmech/schema/cmmmech.yaml` | `861e6299240364ebddc53f7fb238b11014a5c2d48d2a211a80fcb18a5cc2170c` |
| `docs/records.md` | `212cdbb723eb1ad9eb76ea1b7dad066914659b1f85eb2cdb51ee67466cfcc8ee` |
| `.claude/skills/cmmmech-add-record/SKILL.md` | `c9b05bae67a8d30fe27f1f501f4240a36c599d14cfefac0175e79d71ef0ac889` |
