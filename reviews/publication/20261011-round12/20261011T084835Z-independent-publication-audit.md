# Independent round 12 publication audit

Verdict: **pass with stated scientific and publication limits**. One new minor documentation finding was identified, corrected and independently rechecked during this audit. No unresolved blocker, major or minor publication finding remains in the inspected package.

- Reviewer: Codex agent `/root/round12_publication_adversary`, GPT-6, codex.
- Independence: this agent authored none of the 22 records, histories, source dossiers or per-record reviews. Root and other agents performed curation and correction; this agent made no Git/GitHub mutation or record edit.
- Audit finished: 2026-10-11T08:48:35.439940+00:00.
- Worktree: `/private/tmp/CMMMech-expansion-round12-20261011`.
- Branch: `curate/cmm-expansion-round12-20261011`.
- Trusted base: `1e52585c9019a32d37f959e0dafa00ae431f28c4`.
- Exact staged diff before adding this report: SHA-256 `e4c10deaf29bf1db57b3bd0f203c1412582e3e0be00ad1833e03a9af0d004fd3`.
- Scope: 109 staged paths: README, 22 commodity records, 25 histories, 11 research/frontier/publication files, and 50 files comprising 25 structured review pairs. This report is the anticipated 110th publication path.

This is a bounded publication audit, including independent scientific spot checks, rather than a replacement for the 22 per-record scientific observations linked in the [publication report](../../../research/ingests/round12-20261011-publication.md). It follows CLAUDE.md, docs/records.md, the local add-record/review-record skills and docs/record-review-profile.md.

## Scope, evidence and boundaries

All 22 new descriptions, kinds, designation scopes and sources were read. Their commodity identities distinguish ores, processing products, grade-qualified categories and economic groups from elements, mineral species and secondary resources. No new external material identifier is silently transferred from an element or mineral. Eighteen records make no microbial-mechanism claim. Four retain carefully bounded observations.

The following scientific checks were performed independently of the structural gates:

- Reopened the [original EU 2024 act](https://eur-lex.europa.eu/eli/reg/2024/1252/oj/eng), including recital 8 and list context. The combined aluminium value chain, graphite qualifications, and explicitly dated record mappings are defensible. This is not a consolidated-amendment audit.
- Reopened the [Australian official list](https://www.industry.gov.au/publications/australias-critical-minerals-list-and-strategic-materials-list), confirming footnotes 16–17 explicitly enumerate six PGMs and sixteen rare-earth members. The corrected PGM record retains this enumerated Australian designation. The Australian rare-earth record preserves promethium and treats separately listed scandium distinctly.
- Reopened the [Canadian 2024 announcement](https://www.canada.ca/en/natural-resources-canada/news/2024/06/government-of-canada-releases-updated-critical-minerals-list.html), confirming high-purity iron ore in the green-steel context. The record does not promote a project-specific concentrate specification to a universal federal purity definition.
- Read retained BGS OR/24/059 text at section 2.6.3, Table 11 and commodity context. The sodium category explicitly includes sodium carbonate, nitrate and minor metal; the record explains the category name rather than making metallic sodium a chemical compound. Borates and magnesite preserve the assessment's status and policy disclaimer.
- Read retained EU 2020 factsheet pages 547 and 399. The named five-light/ten-heavy REE convention and processing stages support the qualified subgroup records. Six chemical PGMs do not by themselves verify the membership of a later unenumerated legal designation; the PGM correction conservatively removes the contested EU entries without inventing an osmium exclusion.
- Read primary colemanite methods and Table 1/3 text. The twelve composition cells total 126.8%; corrected borates qualifies the reported 28.05 wt% cell and declines normalized recovery claims. Temperature/pH discrepancies, absent corresponding abiotic boron series and lack of isolated product remain explicit.
- Read the Tabas coal methods/results and visually inspected printed page 589/Table 3. The PE concentration comparison is supported, while thymol controls, acid washing, uncertain replication and no demonstrated retained coking performance limit causation and deployment. No whole-feed sulfur mass balance is claimed.
- Inspected the phosphate record against retained primary source and Figure 1 pixels: about 80 mg/L soluble P at 60 hours and later non-monotonic concentrations are consistent. The record distinguishes rock and soluble-phosphate assay arms, preserves control and supplement limits, and does not turn filtrate P into product recovery.
- Visually inspected Mattocks Figure 4 and independently extracted the XLSX formulas. Fig4d O33 uses the summed tabulated Dy eluate denominator, N45 uses the summed Nd eluate denominator, and purity is within the Nd/Dy pair. The workbook gives O33 = 99.396415% and K56 = 15.194194; the record explicitly preserves source differences and avoids a whole-feed recovery or living-cell claim.

The four source dossiers were inspected for accepted/deferred distinctions, acquisition successes and failures, raw-file provenance, reuse terms, and initial/corrected state semantics. Nine retained primary artifacts were independently rehashed against their receipts: colemanite PDF, coal PDF, phosphate HTML, Nature main PDF, supplementary PDF, Figure 4 workbook, EU 2020 factsheets PDF, USGS MCS2026 PDF and BGS OR/24/059 PDF. All nine matched. Historical acquisition and pre-correction hashes are not incorrectly treated as current-file assertions. Raw articles and bulk source data are outside the staged package.

## Deduplication and frontier

Bounded searches used `rg --no-ignore --hidden --follow` over `data/records`, `research`, `reviews` and `history`; relevant raw roots were enumerated with ignored/hidden inclusion. The four accepted experiment DOIs occur in the new records and corresponding dossiers/reviews, with no earlier record occurrence in this searched boundary. The named repository roots contain no symlinks. This is not a machine-wide or literature-wide absence claim; PDF text and selected figure pixels were inspected separately.

Actual corpus counts are 93 records: 64 elements, 23 commodities, 4 minerals and 2 secondary resources. The unchanged historical inventory contains 94 proposed roots. All 29 remaining commodity proposals have decisions: 22 new roots, the designation-specific phosphate-to-phosphate-rock alias and six deferrals. The frontier's 87 exact represented roots and record count use distinct denominators. Natural graphite remains the narrower subset of the new broad graphite family; REE groups explicitly overlap under named conventions.

All current-record, context-input, prior-frontier and historical-inventory hashes in the new frontier matched the cited files. Relative links in README and all new round12 Markdown files resolve. Root's separately inspected packaging receipt reports 243 checked links and 93 contiguous README rows.

## Finding and disposition

**F1 — minor, resolved: stale broad-graphite frontier limitation.** The initial round12 JSON inherited a sentence saying broad graphite remained unrepresented, despite creating and counting that root. Reported immediately to root; tracked as [issue 52](https://github.com/CultureBotAI/CMMMech/issues/52). Root replaced the new frontier limitation with explicit broad/natural representation and battery-grade deferral, while distinguishing new borates/fluorspar from their elemental records. I independently reread the corrected JSON and staged package. The unchanged historical inventory and earlier frontiers preserve their original dated statements. No record or scientific review needed rewriting for this documentation correction.

The three earlier scientific-review findings also have explicit resolved successors, retaining stable issue keys and exact predecessor review/F1 identities:

| Issue | Initial observation | Current disposition |
|---|---|---|
| [49](https://github.com/CultureBotAI/CMMMech/issues/49), borates composition | `20261011T083609Z-borates-round12-independent` | `20261011T084336Z-borates-round12-resolution`: qualified source composition and denominator |
| [50](https://github.com/CultureBotAI/CMMMech/issues/50), magnesite locator | `20261011T083659Z-magnesite-round12-independent` | `20261011T084348Z-magnesite-round12-final-independent`: Magnesium Compounds printed 120–121/PDF 124–125 |
| [51](https://github.com/CultureBotAI/CMMMech/issues/51), PGM scope | `20261011T084025Z-platinum-group-commodities-round12-independent` | `20261011T084341Z-platinum-group-commodities-round12-resolution`: unverified EU entries removed, Australian six-member designation retained |

Initial partial observations remain immutable; their pre-correction working-tree hashes are intentional historical attestations. Current record hashes and their corrective EDIT histories were checked rather than demanding that those earlier reviewed bytes equal the corrected files.

## Validation and preservation

Independently executed `.venv/bin/python scripts/record_review.py check --require-reviews --base 1e52585c9019a32d37f959e0dafa00ae431f28c4`: exit 0, **105 valid review pairs**, declared scopes only. An initial `uv run` read attempt was blocked by sandbox access to the global uv cache; direct use of the existing project environment succeeded. No validator exception was bypassed.

Independent byte and scope inspection confirms:

- 80 prior pairs plus 25 new pairs: 22 completed independent scientific `pass_with_limitations` observations and 3 initial partial `needs_curation` observations.
- Every one of the 22 new records has a completed current scientific review matching its exact path/hash. All local input hashes in those 22 final reviews match current bytes.
- All 93 corpus records have current completed scientific review coverage; this finding is separate from the checker's nonempty gate.
- 108 canonical history sidecars, including 22 new CREATE and 3 corrective EDIT sessions.
- All 509 prior tracked paths under data/records, history, reviews and research remain byte-identical to the trusted base. The narrower record/history/review preservation count is 383. The two counts have different explicit search boundaries.
- `git diff --cached --check` exits 0. No unstaged tracked-byte changes separate the inspected working files from the 109 staged paths. No schema, validator, dependency, test, governed copy or bulk primary-source file is part of the staged change.

Root's actual final command receipts and logs were read, rather than inferred from prior reports:

| Command | Result |
|---|---|
| `just check` | Exit 0; 307 passed, 3 skipped in 70.99 s; 93 records/0 failed; 108 histories/0 errors |
| `uv run --locked cmmmech validate --require-records` | Exit 0; 93 checked, 0 failed |
| `uv run --locked cmmmech validate-history --base 1e52585c9019a32d37f959e0dafa00ae431f28c4` | Exit 0; 108 checked, 0 errors |
| `bash scripts/check_vendored_sync.sh` | Log confirms 22 governed artifacts match pinned CLAW revision |

The tests, history check and vendored check above were run by root; this auditor inspected their receipts/logs and independently ran the structured checker, preservation/hash checks and staged-package checks. Structural success is not used as scientific proof.

## Review-base retention and remaining publication actions

Enumerated all 13 distinct review bases. Twelve, including the new reviews' base, are ancestors of the trusted main base. The only non-ancestor is `c0adc2c0763e1515ed07dc712b024974d98fb342`, retained under annotated tag `review-base/cmm-source-survey-20261009`. Local ancestry/tag checks agree with the root's live remote receipt: tag object `fc4040c3abcd28f0a9cc52467e308100144ad1fd`, peeled commit `c0adc2c0763e1515ed07dc712b024974d98fb342`. No new review base depends only on the disposable topic branch.

The inspected live integration receipt records active ruleset 24692449, SQUASH/ALLGREEN queue, required `validate-strict`, and no bypass actors; admission PR 581 is merged. This audit did not alter governance or make an independent live GitHub API request.

Commit, push, PR creation, isolated squash-shaped verification, queue admission, actual merge, topic-branch deletion and fresh remote-main validation remain root's publication steps at the time of this report. This pre-publication pass does not claim they already happened. Run the required queue and fresh-checkout checks without relaxing the provenance validator, fetch tags explicitly, and preserve the annotated provenance tag.

Scientific limits remain exactly those in the records/reviews: no global source exhaustion, no universally certified product grades, no inference of industrial deployment, and no generic commodity-wide recovery from four narrow assays. Further methods acquisition and independent controls remain research priorities, not hidden unresolved curation defects in the accepted scope.
