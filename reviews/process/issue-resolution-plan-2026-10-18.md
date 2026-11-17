# CMMMech issue resolution plan

Requested filename date: **2026-10-18**. Review performed **2026-10-19 UTC**.
Repository: [CultureBotAI/CMMMech](https://github.com/CultureBotAI/CMMMech).
Default branch inspected: `main` at `a272f29d32ad36fa0bb398ed866aeb0ab1b3cd8b`.
Skill: [.agents/skills/review-open-issues](../../.agents/skills/review-open-issues/SKILL.md).
This is backlog triage and a proposed implementation order, not a fresh scientific review of 183 sources.
The user explicitly requested this saved report; the skill's read-only restriction governs the triage, not that requested output.

## Inventory and evidence boundary

The paginated open-issue endpoint returned **183 actual issues and 0 PRs** across two pages.
A separate paginated open-PR query also returned **0 PRs**. All 183 full bodies and their state reasons
(all open, null state reason) were inspected, together with **all 29 issue comments**. Acquisition of
those discussions and 18 explicitly linked PRs completed at `2026-10-19T07:14:39.696459+00:00`.
All 18 linked PRs are merged; their relevant descriptions, discussion and review statements preserve
source gaps independently of completed curation. They do not cover the remaining tasks as open PRs.
The evidence JSON beside this report preserves exact body/comment hashes, timestamps, local owner
hashes, cited dossier hashes and the linked-PR state/merge commits.

Acquisition commands (read-only GitHub calls):

```sh
gh api repos/CultureBotAI/CMMMech
gh api --paginate --slurp 'repos/CultureBotAI/CMMMech/issues?state=open&per_page=100'
gh api --paginate --slurp 'repos/CultureBotAI/CMMMech/pulls?state=open&per_page=100'
gh api --paginate --slurp 'repos/CultureBotAI/CMMMech/issues/<number>/comments?per_page=100'
```

Linked PR metadata, issue comments and submitted reviews were read through their corresponding
paginated endpoints. Closed-issue history, every inline thread of every historical PR, remote runner
support, all historical raw downloads and the primary literature were **not exhaustively reassessed**.
No paid provider, author contact, remote content mutation or merge was performed for this review.

The isolated clone and branch leave the shared main checkout untouched. The current corpus has
**602 records**. Named owner files were read for identity, material kind, source inventory and
mechanism scope; this mapping is not a claim that every source discrepancy was independently
reproduced. A mapped file can be a comparison/candidate owner rather than a file that must change.
File discovery included hidden and ignored files with `rg --files --hidden --no-ignore`, excluding
Git internals and virtual environments. Cited repository evidence was resolved against this exact
base. An empty owner cell means ownership must be resolved; it does not assert global nonexistence.

README's current integration status describes fleet admission, 22 pinned governed artifacts,
canonical sidecar history and a configured native squash queue. The shepherd is manual/comment-only;
other unverified adapters remain disabled. This task authorizes neither queue admission nor merging.
Governed files must be updated through CLAW's supported synchronizer, never hand-edited.

## Current gate result and first issue

The premise of [#509](https://github.com/CultureBotAI/CMMMech/issues/509) does not reproduce in an
ordinary full clone at this revision. The fresh remote clone automatically acquired the annotated
`review-base/cmm-source-survey-20261009` tag. A live `git ls-remote` returned tag object
`fc4040c3abcd28f0a9cc52467e308100144ad1fd`, peeled to the full commit
`c0adc2c0763e1515ed07dc712b024974d98fb342`. The named test passed: **1 passed in 96.67 s**.
The complete baseline `uv run --no-sync just check` passed: **327 passed, 3 skipped**, **602 valid
records**, **730 valid history sessions**. The separate `bash scripts/check_vendored_sync.sh`
passed for **all 22 governed artifacts**. These results apply to the inspected base and local
environment, not to future PR CI or Ubuntu compatibility.
The three skips are the empty command-template parameter sets at
`tests/test_skill_frontmatter.py:190`, `:195` and `:201`; a focused `pytest -q -rs`
run passed 34 cases and reported exactly those three skips. No provenance case was skipped.
The same named provenance test **fails** in a separate full-history `--no-tags --single-branch`
clone because the exact retained commit is unavailable. That controlled comparison establishes
a clone-reference prerequisite; it does not establish that ordinary full clones fail.

Finish #509 first by distinguishing missing retained references from a missing remote object,
testing recovery in an intentionally tag-omitting clone, and documenting the supported setup.
Do not skip provenance validation, rewrite immutable reviews, manufacture a new evidence tag,
or change governed test behavior to hide unavailable provenance. No known-failure waiver was
needed for this baseline. If that exact test fails in another clone, diagnose its fetched refs;
no other failing test may be waived under the user's exception.

## Order, dependencies and stop rules

Visit **#509, then #479, then #456**. The first restores confidence in all gates; #479 has a
concrete acquired original ready for scientific assessment; #456 is bounded repository maintenance.
The remaining entries retain **unranked implementation priority**, because their missing primary
evidence or unresolved source contradictions do not establish a present corrective defect.
Their visit numbers are a deterministic investigation queue: identity/culture boundaries, reusable
datasets, assay/causal accounting, source acquisition, structural reproducibility, and embargo work,
with issue number as the tie-breaker. This is not an invented precision ranking of scientific severity.
Reconcile each item when reached; an actually demonstrated wrong accepted claim takes precedence.

Severity below describes the consequence of an unsupported expansion, unless explicitly marked
as a reproduced defect. **No current scientific-record defect is established by these source issues
alone.** Major prospective issues cannot be resolved by converting missing measurements into guesses.
Undetermined severity means the evidence is insufficient to judge it. Structural differences may
become major if they change material identity; reclassify only with inspected evidence.

The two-day window at acquisition begins `2026-10-17T07:14:39Z`. Forty-two record paths changed in
commit `e4e32f5e7dd8bca8e1cd86557db5bbb8c53dea34` (2026-10-18T07:18:01Z). Among the concrete owners
in this plan, **#226 (calcite) and #287 (zincite) must be skipped**. Merely mentioning an element
does not make its record an edit target. Recompute the rolling window and all open PR coverage
against freshly fetched `origin/main` before **every** issue. Skip any newly covered or recently
edited item, preserve it in the ledger, and move on; do not invent a no-op PR to bypass the rule.

Shared-owner references below are conflict checks, not claims that one paper resolves another.
In particular, #186/#377, #389/#390, #421/#422, #438/#439, #375/#376,
#130/#387/#388 and #396/#397/#405 overlap owners but retain separate evidence requirements.
If a new open PR covers an owner or issue, follow the user's skip rule rather than stacking branches.

For each eligible issue, follow [backlog-loop-goal sections 1–3](../../prompts/backlog-loop-goal.md):

1. Refresh all issue/PR pages, full selected discussions, current main and the two-day owner history.
   Reproduce the premise. Create one isolated branch/worktree from that fresh base before editing.
2. For source work, apply the discovery skill and preserve a bounded dated acquisition handoff.
   Reuse legitimate existing downloads after verifying hashes; retry denied endpoints only with a
   changed route/access condition. Document unavailability without claiming universal absence.
   A previous deferral, a new abstract, or successful schema validation does not complete an evidence task.
3. Only supported record changes receive actual new canonical history, independent exact-byte
   scientific reviews and required record/history/review/render checks. Preserve source versions,
   immutable observations, null results, jurisdiction/list/edition criticality, organism/strain and
   biomass state, substrate/controls, analytical fractions and laboratory scope. Aqueous depletion,
   fitted phase abundance and isolated-product recovery remain distinct. No automatic criticality inheritance.
4. For code defects, add the smallest meaningful regression and prove failure under old behavior.
   Run focused checks, `just check`, exact relevant CI commands, the pinned canonical check and
   `git diff --check`; inspect skips and nonempty targets. Stage only intended files.
5. Commit the cause and issue reference. Prepare an exact PR title/body and final diff, perform a
   separate read-only adversarial pass, and reproduce findings. Draft any required new finding issues
   locally. Publish only after the exact destination/content approval required by the user's working
   agreement. Push an explicit branch refspec, never force-push. Leave each PR open and move on.
6. Record done/open-PR, skipped, blocked-by-specific-evidence or failed-gate outcomes. Missing source
   evidence and a pending approval are not passing gates or successful fixes. Stop the batch when all
   entries are done or genuinely blocked, or three consecutive issue implementations fail their gates.
   Never merge, close an issue, request a bot review, mention a person with an at-sign, or invoke a paid provider.

An issue containing several sources is complete only when its full acceptance scope is met or an
explicitly reviewed disposition accounts for each subtask. Partial acquisitions stay partial.
The #469 embargo blocks only its named 2025-deposit subtask until 2026-11-21; investigate older
originals separately. No author outreach is implicitly authorized by an issue's request for clarification.

## Complete issue-by-issue queue

Each entry's linked issue and dated comments are the source of the reported evidence gap.
The acceptance text is an actionable summary; the full original issue criteria remain binding.
All scientific changes additionally require the common curation/validation checks above.


### Visit 001: [#509 — Structured review bundles pin provenance commit c0adc2c that no pushed ref reaches; just test fails on a fresh clone](https://github.com/CultureBotAI/CMMMech/issues/509)

- **Severity / status:** Reported blocker; not reproduced on full clone; priority 1; **ready for bounded assessment**.
- **Current evidence / owner:** [Provenance test](../../tests/test_record_review_contract.py), [native publication profile](../../docs/record-review-profile.md); exact remote tag and fresh-clone results above.
- **Dependencies:** Finish clone-mode diagnosis; no dependency on a scientific source.
- **Acceptance:** Full clone already has annotated provenance tag and the named test passes; verify complete gate and a tag-omitting clone, then document supported clone recovery without weakening governed validation.


### Visit 002: [#479 — Review newly acquired aluminium salt-slag recycling evidence and obtain complete HFC microbial methods](https://github.com/CultureBotAI/CMMMech/issues/479)

- **Severity / status:** Undetermined; scientific assessment pending; priority 2; **ready for bounded assessment**.
- **Current evidence / owner:** [aluminium-salt-slag](../../data/records/aluminium-salt-slag.yaml), [zinc-purification-hot-filter-cake](../../data/records/zinc-purification-hot-filter-cake.yaml)
- **Dependencies:** Inspect the already acquired salt-slag original; the independent HFC subtask still requires full primary methods.
- **Acceptance:** Assess the acquired Recycling2026 salt-slag original, balances and reuse trials; separately obtain the complete fungal HFC original. Keep both obligations explicit and review any supported extensions.


### Visit 003: [#456 — Assess Pages action runtime and Ubuntu 26 runner compatibility](https://github.com/CultureBotAI/CMMMech/issues/456)

- **Severity / status:** Minor maintenance; priority 3; **ready for bounded assessment**.
- **Current evidence / owner:** [Repository-owned Pages workflow](../../.github/workflows/pages.yaml); checkout v4, configure-pages v5, upload-pages-artifact v3, deploy-pages v4 and ubuntu-latest are still configured.
- **Dependencies:** Official action/runtime support and reproducible build/staging evidence; live deployment is outside this task.
- **Acceptance:** Assess the Pages action chain and live supported runtimes using official releases; reproduce staging/build and document runner compatibility. An annotation alone does not justify upgrading governed workflows or deploying the site.


### Visit 004: [#130 — Resolve yeast cerium-phosphate phase identity from full primary evidence](https://github.com/CultureBotAI/CMMMech/issues/130)

- **Severity / status:** Major prospective identity/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [monazite-ce](../../data/records/monazite-ce.yaml), [rhabdophane-ce](../../data/records/rhabdophane-ce.yaml)
- **Dependencies:** Authoritative specimen, phase or culture evidence is still required; source uncertainty prevents a defensible corrective implementation rank. Shared-owner checks: #387, #388.
- **Acceptance:** Obtain Jiang2010 diffraction/microscopy and reconcile the 2017 qualification; establish phase/hydration and biomass/control provenance before choosing a Ce-phosphate owner. No inferred species from CePO4 alone.


### Visit 005: [#134 — Complete original-figure and phase verification for manganese-ore oxalates](https://github.com/CultureBotAI/CMMMech/issues/134)

- **Severity / status:** Major prospective identity/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [manganese-ore](../../data/records/manganese-ore.yaml), [falottaite](../../data/records/falottaite.yaml), [lindbergite](../../data/records/lindbergite.yaml), [todorokite](../../data/records/todorokite.yaml), [kutnohorite](../../data/records/kutnohorite.yaml); [round40-manganese-ore-oxalates](../../research/sources/round40-manganese-ore-oxalates/20261012T005309Z-source-deferral.md); [round41-manganese-minerals](../../research/sources/round41-manganese-minerals/20261012T012222Z-source-investigation.md); [comment 1](https://github.com/CultureBotAI/CMMMech/issues/134#issuecomment-6116157338), [comment 2](https://github.com/CultureBotAI/CMMMech/issues/134#issuecomment-6116280005)
- **Dependencies:** Authoritative specimen, phase or culture evidence is still required; source uncertainty prevents a defensible corrective implementation rank.
- **Acceptance:** Recover original manganese-ore main PXRD/control series; reproduced SEM panels do not resolve it. Bind the 45-day crystal to feed arms and reconcile pH/table/CIF differences before curation.


### Visit 006: [#220 — Clarify Ma2024 anorthite feed composition before phase-specific leaching claims](https://github.com/CultureBotAI/CMMMech/issues/220)

- **Severity / status:** Major prospective identity/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [anorthite](../../data/records/anorthite.yaml); [round70-silicates](../../research/sources/round70-silicates/20261014T113302Z-source-investigation.md)
- **Dependencies:** Authoritative specimen, phase or culture evidence is still required; source uncertainty prevents a defensible corrective implementation rank.
- **Acceptance:** Obtain Ma2024 specimen-linked XRF/phase data or correction and final medium recipe; reconcile Mg/Fe-rich bulk feed with anorthite assignment before pure-phase Mg-release claims.


### Visit 007: [#233 — Resolve WMS2 accession identity and Han2022 carbonate run ambiguities](https://github.com/CultureBotAI/CMMMech/issues/233)

- **Severity / status:** Major prospective identity/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [monohydrocalcite](../../data/records/monohydrocalcite.yaml); [round72-carbonates](../../research/sources/round72-carbonates/20261014T131835Z.md)
- **Dependencies:** Authoritative specimen, phase or culture evidence is still required; source uncertainty prevents a defensible corrective implementation rank.
- **Acceptance:** Reconcile ON000249.1 environmental clone versus WMS2 culture, lowest Mg arm and ratio5/day140 phase assignment using original sequence/run data; require mineralization and preparation metadata.


### Visit 008: [#283 — Resolve metavivianite protocol and biological phase-identification gaps](https://github.com/CultureBotAI/CMMMech/issues/283)

- **Severity / status:** Major prospective identity/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [metavivianite](../../data/records/metavivianite.yaml); [round84-phosphates](../../research/sources/round84-phosphates/20261015T001048Z-source-investigation.md)
- **Dependencies:** Authoritative specimen, phase or culture evidence is still required; source uncertainty prevents a defensible corrective implementation rank.
- **Acceptance:** Resolve Chiba viv-S60/65, independently identify Erbs's provisional phase and acquire Miot SI; keep spectral areas distinct from phase fractions and historical assignments from modern species.


### Visit 009: [#286 — Clarify Segura2023 minor wurtzite indexing before accepting phase evidence](https://github.com/CultureBotAI/CMMMech/issues/286)

- **Severity / status:** Major prospective identity/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [wurtzite](../../data/records/wurtzite.yaml)
- **Dependencies:** Authoritative specimen, phase or culture evidence is still required; source uncertainty prevents a defensible corrective implementation rank.
- **Acceptance:** Obtain Segura2023 raw/indexed diffraction and authoritative reference-pattern mapping resolving cell, wavelength and hkl mismatch; predominant cubic ZnS does not prove the minor wurtzite claim.


### Visit 010: [#289 — Resolve azurite2016 strain, phase-sample lineage and copper-removal recipe](https://github.com/CultureBotAI/CMMMech/issues/289)

- **Severity / status:** Major prospective identity/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [azurite](../../data/records/azurite.yaml)
- **Dependencies:** Authoritative specimen, phase or culture evidence is still required; source uncertainty prevents a defensible corrective implementation rank.
- **Acceptance:** Bind Kang2016 B22/B7-22 accession and BPU phase sample to the YA removal assay; reconcile inoculum, 2mM/2M and time/concentration basis before any phase-specific Cu yield.


### Visit 011: [#290 — Clarify tenorite2021 thermal phase formation and mixed-product evidence](https://github.com/CultureBotAI/CMMMech/issues/290)

- **Severity / status:** Major prospective identity/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [tenorite](../../data/records/tenorite.yaml)
- **Dependencies:** Authoritative specimen, phase or culture evidence is still required; source uncertainty prevents a defensible corrective implementation rank.
- **Acceptance:** Obtain Badawy2021 pre/post-heating phase data, raw diffraction and matched heated controls; resolve sulfur/oxidation-state mixture without claiming direct living-cell CuO formation.


### Visit 012: [#296 — Resolve zinc-silicate phase and composition evidence gaps](https://github.com/CultureBotAI/CMMMech/issues/296)

- **Severity / status:** Major prospective identity/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [willemite](../../data/records/willemite.yaml), [hemimorphite](../../data/records/hemimorphite.yaml); [round86-zinc-minerals](../../research/sources/round86-zinc-minerals/20261015T023418Z-source-investigation.md)
- **Dependencies:** Authoritative specimen, phase or culture evidence is still required; source uncertainty prevents a defensible corrective implementation rank.
- **Acceptance:** Acquire Medas AM-18-56128 and 2017 aging original; independently reconcile Xu2022 synthetic-willemite composition/purity. Preserve low-order precursor and assayed-feed dissolution boundaries.


### Visit 013: [#333 — Clarify petroleum-coke feed identity, controls and sulfur balance in Tripathi2010 and its relationship to Tripathi2019](https://github.com/CultureBotAI/CMMMech/issues/333)

- **Severity / status:** Major prospective identity/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [petroleum-coke](../../data/records/petroleum-coke.yaml)
- **Dependencies:** Authoritative specimen, phase or culture evidence is still required; source uncertainty prevents a defensible corrective implementation rank.
- **Acceptance:** Authenticate Tripathi2010 feed origin and controls; recover recipe/sulfur balance and missing Figure1, then acquire 2019 original and resolve experiment lineage rather than treating concentration loss as recovery.


### Visit 014: [#334 — Clarify XN163 composition and phase attribution in the amblygonite–montebrasite heating study](https://github.com/CultureBotAI/CMMMech/issues/334)

- **Severity / status:** Major prospective identity/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [amblygonite](../../data/records/amblygonite.yaml), [montebrasite](../../data/records/montebrasite.yaml); [round94-minerals](../../research/sources/round94-minerals/20261015T114206Z-source-investigation.md)
- **Dependencies:** Authoritative specimen, phase or culture evidence is still required; source uncertainty prevents a defensible corrective implementation rank.
- **Acceptance:** Bind heated XN163 aliquot to XRD/EPMA F/OH composition and compare final 2018 article; preserve lacroixite and crossing species boundary before pure-species thermal claims.


### Visit 015: [#340 — Clarify HJ-2 identity and melanterite phase evidence in Peng et al.](https://github.com/CultureBotAI/CMMMech/issues/340)

- **Severity / status:** Major prospective identity/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [melanterite](../../data/records/melanterite.yaml); [round95-sulfates](../../research/sources/round95-sulfates/20261015T124816Z-source-investigation.md)
- **Dependencies:** Authoritative specimen, phase or culture evidence is still required; source uncertainty prevents a defensible corrective implementation rank.
- **Acceptance:** Reconcile HJ-2 culture/deposit with MZ701937.1 and comparator AB680720.1; obtain diffraction/preparation/quantification and control data before attributing melanterite necessity or phase yield.


### Visit 016: [#341 — Clarify Qin pickling-liquor culture provenance and experimental inconsistencies](https://github.com/CultureBotAI/CMMMech/issues/341)

- **Severity / status:** Major prospective identity/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [spent-steel-pickling-liquors](../../data/records/spent-steel-pickling-liquors.yaml)
- **Dependencies:** Authoritative specimen, phase or culture evidence is still required; source uncertainty prevents a defensible corrective implementation rank.
- **Acceptance:** Resolve Qin isolate versus KF378735.1 provenance, iron/reagent balances, CK controls and salt/phase maps; no guessed unit repair or combined operating optimum.


### Visit 017: [#342 — Clarify Zhong2019 potassium-calcium sulfate and spectral assignments](https://github.com/CultureBotAI/CMMMech/issues/342)

- **Severity / status:** Major prospective identity/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [alunite](../../data/records/alunite.yaml)
- **Dependencies:** Authoritative specimen, phase or culture evidence is still required; source uncertainty prevents a defensible corrective implementation rank.
- **Acceptance:** Resolve Zhong2019 K2Ca2(SO4)3/syngenite and coordination labels from phase/spectral data; map Figure6 arms and keep soluble-K metric separate from mixed evaporation product.


### Visit 018: [#412 — Resolve veatchite2012 specimen identity at the calcioveatchite boundary and recover its CIF deposit](https://github.com/CultureBotAI/CMMMech/issues/412)

- **Severity / status:** Major prospective identity/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [veatchite](../../data/records/veatchite.yaml), [calcioveatchite](../../data/records/calcioveatchite.yaml)
- **Dependencies:** Authoritative specimen, phase or culture evidence is still required; source uncertainty prevents a defensible corrective implementation rank. Shared-owner checks: #418.
- **Acceptance:** Acquire AM-12-015 CIF/reflections and specimen-linked reassessment of RG701/1; distinguish historical veatchite2M from a modern Ca-dominant determination and resolve table labels/cells.


### Visit 019: [#429 — Reconcile lanthanite-(La) historical specimen provenance with the IMA renamed-species row](https://github.com/CultureBotAI/CMMMech/issues/429)

- **Severity / status:** Major prospective identity/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [lanthanite-la](../../data/records/lanthanite-la.yaml)
- **Dependencies:** Authoritative specimen, phase or culture evidence is still required; source uncertainty prevents a defensible corrective implementation rank. Shared-owner checks: #428.
- **Acceptance:** Acquire IMA renaming/type documentation and natural La-dominant specimen analyses; distinguish B10531 from historical type references without inventing a unique approval number or locality correction.


### Visit 020: [#488 — Clarify ameghinite thermal-product identities and proposed polymorph conversion](https://github.com/CultureBotAI/CMMMech/issues/488)

- **Severity / status:** Major prospective identity/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [ameghinite](../../data/records/ameghinite.yaml)
- **Dependencies:** Authoritative specimen, phase or culture evidence is still required; source uncertainty prevents a defensible corrective implementation rank.
- **Acceptance:** Obtain primary heated-product identification and replication for distinct1967 arms; verify rather than assume proposed2017 polymorph conversion, preserving scarce/unidentified products.


### Visit 021: [#492 — Authenticate solder feed and Acetobacter preparation before mechanistic expansion](https://github.com/CultureBotAI/CMMMech/issues/492)

- **Severity / status:** Major prospective identity/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [tin-copper-solder](../../data/records/tin-copper-solder.yaml)
- **Dependencies:** Authoritative specimen, phase or culture evidence is still required; source uncertainty prevents a defensible corrective implementation rank.
- **Acceptance:** Authenticate Jadhav2017 feed composition and TISTR/BCRC culture link; resolve cells versus supernatant and acid-medium controls, then acquire Hocheng2014 before comparison.


### Visit 022: [#498 — Resolve caysichite-(Y) species and formula uncertainty using Canadian material and the 2025 deposit](https://github.com/CultureBotAI/CMMMech/issues/498)

- **Severity / status:** Major prospective identity/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [caysichite-y](../../data/records/caysichite-y.yaml); [round116-ree](../../research/sources/round116-ree/20261016T093140Z-source-investigation.md)
- **Dependencies:** Authoritative specimen, phase or culture evidence is still required; source uncertainty prevents a defensible corrective implementation rank.
- **Acceptance:** Acquire CSD2482225 and primary numerical corrections; require modern Canadian-material reassessment before species equivalence or split, preserving hypothetical sites and specimen-specific thermal evidence.


### Visit 023: [#213 — Complete maghemite primary-source and supplement assessment before curation](https://github.com/CultureBotAI/CMMMech/issues/213)

- **Severity / status:** Major prospective data/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [maghemite](../../data/records/maghemite.yaml); [round69-ironoxides](../../research/sources/round69-ironoxides/20261014T104949Z-source-investigation.md); [20261014T105449Z-maghemite-round69-independent](../../reviews/structured/20261014T105449Z-maghemite-round69-independent/review.md); [comment 1](https://github.com/CultureBotAI/CMMMech/issues/213#issuecomment-6167120913)
- **Dependencies:** Complete primary methods plus source-to-file/sample/unit mapping are required; acquired data alone cannot establish an accepted mechanism.
- **Acceptance:** Acquire Ohenhen SI and Zhou2019 complete original; map Mendeley specimen labels/masses/units beyond the eight-sheet sample. Existing Gao2020 evidence does not settle either source obligation.


### Visit 024: [#405 — Reconcile M. auratinigra La/Gd datasets and full primary evidence before mechanism admission](https://github.com/CultureBotAI/CMMMech/issues/405)

- **Severity / status:** Major prospective data/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [monazite-la](../../data/records/monazite-la.yaml), [monazite-gd](../../data/records/monazite-gd.yaml); [round105-ree](../../research/sources/round105-ree/20261015T230454Z-source-investigation.md)
- **Dependencies:** Complete primary methods plus source-to-file/sample/unit mapping are required; acquired data alone cannot establish an accepted mechanism. Shared-owner checks: #396, #397.
- **Acceptance:** Acquire 2026 primary/SI and reconcile two Mendeley releases and Figures(new); map actual paper figures to files beyond the two acquired XLSX, validate phases and measured/modelled columns.


### Visit 025: [#473 — Resolve eucrite experiment specimen provenance and acquire original supplementary data](https://github.com/CultureBotAI/CMMMech/issues/473)

- **Severity / status:** Major prospective data/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [eucrite-meteorite](../../data/records/eucrite-meteorite.yaml); [round112-resources](../../research/sources/round112-resources/20261016-source-investigation.md)
- **Dependencies:** Complete primary methods plus source-to-file/sample/unit mapping are required; acquired data alone cannot establish an accepted mechanism.
- **Acceptance:** Acquire authentic Tonietti2026 supplements and bind EU specimen/supplier; recompute EU-specific endpoints with censoring/uncertainty and retain one abiotic replicate without borrowing other rocks.


### Visit 026: [#165 — Resolve Li2025 clay sequencing supplement and extraction calculation evidence](https://github.com/CultureBotAI/CMMMech/issues/165)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [ion-adsorption-rare-earth-clay](../../data/records/ion-adsorption-rare-earth-clay.yaml)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Obtain Li2025 sequencing SI/data and reconcile Equation 2 and XRF/digestion inventories; verify taxonomic resolution and matched-medium controls before quantitative or organism-specific expansion.


### Visit 027: [#175 — Reconcile Hu2026 feed identity and bioleaching data before ingestion](https://github.com/CultureBotAI/CMMMech/issues/175)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [enargite-pyrite-concentrate](../../data/records/enargite-pyrite-concentrate.yaml), [chalcopyrite-enargite-concentrate](../../data/records/chalcopyrite-enargite-concentrate.yaml); [round57-enargite](../../research/sources/round57-enargite/20261012T120724Z-handoff.md); [round57-enargite](../../research/sources/round57-enargite/20261012T122955Z-disposition.md)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference. Shared-owner checks: #171.
- **Acceptance:** Obtain Hu2026 labelled raw/corrected Figures 5–6, Table 2 feed mineralogy and actual two-stage protocol. Resolve hours/days and dose-endpoint mapping before owner selection or ingestion.


### Visit 028: [#178 — Acquire Kordloo2024 supplement and reconcile electroplating experiment provenance](https://github.com/CultureBotAI/CMMMech/issues/178)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [electroplating-sludge](../../data/records/electroplating-sludge.yaml); [round58-electroplating](../../research/sources/round58-electroplating/20261012T132654Z-source-investigation.md); [round58-electroplating](../../research/sources/round58-electroplating/20261012T133101Z-independent-assessment-review.md)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Acquire Kordloo2024 SI and reconcile 2024/2026 batch lineage, reused percentages, rpm/temperature conflicts and extraction basis; no inference of independent replication or misconduct.


### Visit 029: [#210 — Acquire Choi 2023 supplement and reconcile asbestos assay controls](https://github.com/CultureBotAI/CMMMech/issues/210)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [chrysotile](../../data/records/chrysotile.yaml), [riebeckite](../../data/records/riebeckite.yaml)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Acquire Choi2023 SI Tables S1–S4/Figures S1–S11; reconcile Mg timepoints and inoculum/negative-control subtraction. Do not translate extractable Fe or liquid release into detoxification/recovery.


### Visit 030: [#215 — Reconcile original run metadata for wollastonite and diopside dissolution studies](https://github.com/CultureBotAI/CMMMech/issues/215)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [wollastonite](../../data/records/wollastonite.yaml), [diopside](../../data/records/diopside.yaml); [round68-new-frontier](../../research/sources/round68-new-frontier/20261014T100801Z-source-investigation.md)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Obtain Pokrovsky2009/2021 run-level metadata; reconcile loadings, silica units, pH, timing, steady state and live/dead/sterile images before importing exact rate effects.


### Visit 031: [#231 — Resolve Kato2022 hydrocerussite phosphate mapping and biomass units](https://github.com/CultureBotAI/CMMMech/issues/231)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [hydrocerussite](../../data/records/hydrocerussite.yaml), [pyromorphite](../../data/records/pyromorphite.yaml), [lead](../../data/records/lead.yaml)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Obtain Kato2022 A–D phosphate-to-phase map and experiment-specific biomass units; verify medium, preparation and sterile/killed controls before condition-specific mineral or intracellular claims.


### Visit 032: [#261 — Resolve contradictory MLCC leaching endpoints and sampling provenance in Masache-Romero 2025](https://github.com/CultureBotAI/CMMMech/issues/261)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [waste-multilayer-ceramic-capacitors](../../data/records/waste-multilayer-ceramic-capacitors.yaml)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Obtain Masache-Romero2025 raw/corrected Ni/Fe endpoints and timepoints, sampling correction and replicates; preserve estimated viscosity separately from measured extraction.


### Visit 033: [#262 — Resolve SmCo magnet-scrap peroxide recipe and supplementary samarium mass balance](https://github.com/CultureBotAI/CMMMech/issues/262)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [samarium-cobalt-magnet-scrap](../../data/records/samarium-cobalt-magnet-scrap.yaml)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Reconcile Nayak peroxide and precipitation/stripping recipes; obtain complete Sm feed, liquor, moisture/purity and product inventory explaining SI S3 before accepting overall yield.


### Visit 034: [#268 — Clarify Pethkar2003 fixer dilution, eluent recipe and recovery balance](https://github.com/CultureBotAI/CMMMech/issues/268)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [used-photographic-fixer-solutions](../../data/records/used-photographic-fixer-solutions.yaml); [round81-resources](../../research/sources/round81-resources/20261014T204929Z-source-investigation.md); [20261014T210002Z-used-photographic-fixer-solutions-round81-independent](../../reviews/structured/20261014T210002Z-used-photographic-fixer-solutions-round81-independent/review.md); [comment 1](https://github.com/CultureBotAI/CMMMech/issues/268#issuecomment-6178890319)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Reconcile Pethkar2003 dilution, sulfate, 1/10% ethanol and bead/biomass denominators using same-experiment data; require complete Ag/product balance, not merely a new PDF download.


### Visit 035: [#271 — Reconcile Ciani2026 effluent biosorption pretreatment, units and replicate handling](https://github.com/CultureBotAI/CMMMech/issues/271)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [electroplating-bath-effluents](../../data/records/electroplating-bath-effluents.yaml)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Obtain Ciani2026 arm-specific pretreatment, units and replicate accounting; reconcile PDF micromol versus XML mmol, zero/missing rows and threshold claims without deleting observations.


### Visit 036: [#275 — Clarify Robshaw2020 spent-potlining recipe and recovery denominators](https://github.com/CultureBotAI/CMMMech/issues/275)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [spent-potlining](../../data/records/spent-potlining.yaml)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Resolve Robshaw2020 acid/time/flow arms and model versus measured column inventories; account for wash/mixing losses before whole-feed fluoride recovery or product-purity claims.


### Visit 037: [#276 — Resolve Chen2022 parasymplesite experiment arm labels and reproducibility details](https://github.com/CultureBotAI/CMMMech/issues/276)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [parasymplesite](../../data/records/parasymplesite.yaml)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Obtain Chen2022 corrected curve-to-arm mapping, inoculum basis and XRD radiation metadata; Fe(II) percentages do not measure parasymplesite phase yield or As recovery.


### Visit 038: [#281 — Clarify Joseph copper-patina phase evidence and quantitative definitions](https://github.com/CultureBotAI/CMMMech/issues/281)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [brochantite](../../data/records/brochantite.yaml), [atacamite](../../data/records/atacamite.yaml); [round84-copper-patinas](../../research/sources/round84-copper-patinas/20261015T000916Z-source-investigation.md)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Acquire Joseph2011 graphics and reconcile 2012 loading, dry-product and oxalate-rate bases; map patina/coupon phases and shared experiments before quantitative or recovery claims.


### Visit 039: [#288 — Clarify titanogypsum2021 loading, fluoride balance and mixed phase assignments](https://github.com/CultureBotAI/CMMMech/issues/288)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [titanogypsum](../../data/records/titanogypsum.yaml)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Reconcile Chen2021 loading, fluorine compartment balance, TG assay/phase assignments and controls; retain null P, unmatched pH and separate phosphogypsum arms.


### Visit 040: [#294 — Clarify phosphorus accounting and endpoint inconsistencies in the municipal-sludge study](https://github.com/CultureBotAI/CMMMech/issues/294)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [municipal-sewage-sludge](../../data/records/municipal-sewage-sludge.yaml)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Obtain Pradhan2021 nutrient blanks, replacement/sampling volumes and raw P inventories; reconcile Figure1/Table5 and percentages over 100 before attributing sludge-derived recovery.


### Visit 041: [#299 — Clarify the Qu2023 simonkolleite run inventory, solution units and thermal protocol](https://github.com/CultureBotAI/CMMMech/issues/299)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [simonkolleite](../../data/records/simonkolleite.yaml)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Obtain Qu2023 run log resolving grams/mL, missing 2/10-day runs, 800/900C and sample/heating maps; distinguish purchased Zn from scrap and phase loss from recovery.


### Visit 042: [#300 — Clarify secondary aluminium dross roasting recipe and mass-balance basis in Lv et al. (2022)](https://github.com/CultureBotAI/CMMMech/issues/300)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [secondary-aluminium-dross](../../data/records/secondary-aluminium-dross.yaml)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Resolve Lv2022 roast/leach conditions and liquor recipe; reconstruct Mg-normalized equations and loss inventories before interpreting solid-balance Al/Na metrics as isolated product.


### Visit 043: [#303 — Clarify chromium partitioning and assay definitions in the IPS21 leather-shavings study](https://github.com/CultureBotAI/CMMMech/issues/303)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [chromium-tanned-leather-shavings](../../data/records/chromium-tanned-leather-shavings.yaml)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Reconcile IPS21 liquid/residue Cr bases, labels, degradation equation, recipe and sequence crosswalk from original data; retain censored Cr(VI) and avoid unsupported intracellular exclusion.


### Visit 044: [#304 — Clarify the gypsum dehydration control annotation, later inoculum loading, and missing supplementary evidence](https://github.com/CultureBotAI/CMMMech/issues/304)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [gypsum](../../data/records/gypsum.yaml), [anhydrite](../../data/records/anhydrite.yaml)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Acquire genuine Huang/Douchi SI and clarify control anhydrite marker, loading and radiation metadata; the coupon-size correction is already resolved and counterevidence remains explicit.


### Visit 045: [#309 — Resolve struvite-(K) battery-washwater recipe, mass-balance and fertilizer-table discrepancies](https://github.com/CultureBotAI/CMMMech/issues/309)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [struvite-k](../../data/records/struvite-k.yaml); [round89-minerals](../../research/sources/round89-minerals/20261015T061552Z-source-investigation.md)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Reconcile Abayie2025 reagent grades/doses, volume-dependent K removal, refinement basis and Cd table claim using raw/corrected evidence; no unverified fertilizer compliance conclusion.


### Visit 046: [#311 — Resolve Pan2024 coal-gasification-slag assay inconsistencies and metal mass balance](https://github.com/CultureBotAI/CMMMech/issues/311)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [coal-gasification-slag](../../data/records/coal-gasification-slag.yaml); [round90-resources](../../research/sources/round90-resources/20261015T071841Z-source-investigation.md)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Obtain Pan2024 raw turbidity, kinetic-arm and zeta maps and element balances; gravimetric feed loss and jar-test performance are not metal recovery.


### Visit 047: [#316 — Clarify Lambert2015 cable-residue copper accounting and inconsistent experiment labels](https://github.com/CultureBotAI/CMMMech/issues/316)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [electrical-cable-recycling-residues](../../data/records/electrical-cable-recycling-residues.yaml); [round91-resources](../../research/sources/round91-resources/20261015T083339Z-source-investigation.md)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Acquire Lambert2015 final version/raw data; reconcile figure test numbers, acid ratios, thymol and inoculum Cu, volumes and uncertainty; retain synthetic-feed nulls.


### Visit 048: [#317 — Resolve the synthetic florencite-(Ce) protocol and composition evidence in Li et al. (2022)](https://github.com/CultureBotAI/CMMMech/issues/317)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [florencite-ce](../../data/records/florencite-ce.yaml); [round91-minerals](../../research/sources/round91-minerals/20261015T083452Z-source-investigation.md)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Obtain Li2022 synthetic-Ce run protocol, reagent amounts and Figure6B cells/error definitions; distinguish local EDS ratios, coal-waste arms and phase-specific recovery.


### Visit 049: [#319 — Clarify Smeaton2009 plumbojarosite assay versions, microscopy preparation and lead accounting](https://github.com/CultureBotAI/CMMMech/issues/319)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [plumbojarosite](../../data/records/plumbojarosite.yaml); [round92-sulfates](../../research/sources/round92-sulfates/20261015T093131Z-source-investigation.md)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Compare Smeaton2009 final article/SI with thesis; resolve time/Fe/EDS/luminescence mappings and temperature, then require preparation controls before metabolic-phosphate or intracellular causation.


### Visit 050: [#320 — Clarify loellingite phase-recovery calculations and surface-component claims in Almojadah & Harmer 2025](https://github.com/CultureBotAI/CMMMech/issues/320)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [loellingite](../../data/records/loellingite.yaml)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Acquire Almojadah2025 QXRD patterns, fraction masses and recovery equation; reconcile XPS fitted trends and conditioning doses without assigning mixed-feed effects uniquely to loellingite.


### Visit 051: [#321 — Clarify metal normalization, control accounting and assay labels in the 2020 machining-burr bioleaching study](https://github.com/CultureBotAI/CMMMech/issues/321)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [metallic-machining-burrs](../../data/records/metallic-machining-burrs.yaml); [round92-resources](../../research/sources/round92-resources/20261015T093435Z-source-investigation.md)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Reconstruct Gomez-Ramirez2020 percentage normalization and control/inoculum terms, time units and sulfate method from original data; require liquid/solid/precipitate balances before extraction yield.


### Visit 052: [#324 — Clarify Tl-jarosite assay labels, sorption comparisons and thallium product accounting](https://github.com/CultureBotAI/CMMMech/issues/324)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [thallium](../../data/records/thallium.yaml)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Compare clean Smeaton2012 final source with thesis/SI; resolve formula, pH/significance, sample times and Tl/S/O maps, preserving distinct sorption/dissolution assays and product uncertainty.


### Visit 053: [#325 — Clarify assay bases and time-course metadata in Wei2018 pig-manure bioleaching study](https://github.com/CultureBotAI/CMMMech/issues/325)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [pig-manure](../../data/records/pig-manure.yaml)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Resolve Wei2018 sulfur/time/ORP maps, nutrient assays, mass basis and sampling correction; authenticate community accessions and preserve missing sterile/control limitations.


### Visit 054: [#335 — Clarify abiotic comparator temperatures in Wang2007 ammoniojarosite synthesis](https://github.com/CultureBotAI/CMMMech/issues/335)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [ammoniojarosite](../../data/records/ammoniojarosite.yaml)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Resolve Wang2007 sample6.6 and low-temperature comparator labels from primary run records; temperature clarification cannot make chemically unmatched abiotic arms matched biological controls.


### Visit 055: [#336 — Resolve argentojarosite thesis assay labels and acquire the complete2016 continuation](https://github.com/CultureBotAI/CMMMech/issues/336)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [argentojarosite](../../data/records/argentojarosite.yaml)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Acquire full Mukherjee2016 and crosswalk 2013 thesis arms; resolve Ag/time/Fe labels and analytical bases while preserving fourteen-day phases, negative arms and abiotic Ag stage.


### Visit 056: [#343 — Clarify Reich2024 loading denominators and censored lithium residuals](https://github.com/CultureBotAI/CMMMech/issues/343)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [heterosite](../../data/records/heterosite.yaml)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Obtain Reich2024 concentration/digestion masses, blanks and censoring thresholds; reproduce selected workbook loads on the correct basis without treating residual zeros/LOQ as exact zero or isolated yield.


### Visit 057: [#358 — Clarify poultry-manure phosphorus fractions and contradictory Gaind 2016 figures](https://github.com/CultureBotAI/CMMMech/issues/358)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** Source investigation; resolve material ownership before any CREATE.
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Resolve Gaind2016 poultry treatment/fraction maps, zeros, totals and mass inputs with primary data or a distinct complete controlled study; keep poultry manure separate from litter and pig manure.


### Visit 058: [#360 — Clarify Nejad2020 oily-sludge metal fractions, treatment recipe and mass accounting](https://github.com/CultureBotAI/CMMMech/issues/360)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [petroleum-oily-sludge](../../data/records/petroleum-oily-sludge.yaml)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Resolve Nejad2020 sampled fractions, wet/dry basis, recipe, analytical platform and metal controls; medium inputs and missing mass balance preclude biosorption/extraction attribution.


### Visit 059: [#365 — Clarify seawater uranium culture normalization and compartment mass accounting](https://github.com/CultureBotAI/CMMMech/issues/365)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [seawater](../../data/records/seawater.yaml)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Resolve Yuan2019 initial/final culture normalization, nutrient/compartment inventories and ratio arithmetic; require matched cell/nutrient/membrane controls before uranium binding or product claims.


### Visit 060: [#370 — Resolve acid mine drainage control, balance and sequence-sample gaps](https://github.com/CultureBotAI/CMMMech/issues/370)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [acid-mine-drainage](../../data/records/acid-mine-drainage.yaml), [covellite](../../data/records/covellite.yaml); [round101-amd](../../research/sources/round101-amd/20261015T193414Z-source-investigation.md)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Resolve Silva2019 Cu/S composition/product inventory and Akinpelu2021 control outputs, sampling/feed balance and Sa/Sb run mapping; one shared experiment is not independent replication.


### Visit 061: [#377 — Clarify zinc-leach-residue smelting temperatures and zinc accounting](https://github.com/CultureBotAI/CMMMech/issues/377)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [zinc-leach-residue](../../data/records/zinc-leach-residue.yaml); [round102-zinc](../../research/sources/round102-zinc/20261015T202456Z-source-investigation.md)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference. Shared-owner checks: #186.
- **Acceptance:** Resolve Wang2026 temperature labels, assay units and lower-temperature sequence with original runs; require collected vapor/dust/product balance before equating slag Zn loss to recovery. Separate from #186.


### Visit 062: [#378 — Reconcile uranium-tailings leach endpoints and downstream feed provenance](https://github.com/CultureBotAI/CMMMech/issues/378)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [uranium-mine-tailings](../../data/records/uranium-mine-tailings.yaml)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Resolve Reynier2021 U/Th endpoints, durations and resin-feed lineage; distinguish replicate types and require matched leach controls/element balances before microbial increment or recovered product.


### Visit 063: [#379 — Resolve carbonatite-ore pretreatment controls and interstage rare-earth accounting](https://github.com/CultureBotAI/CMMMech/issues/379)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [carbonatite-associated-rare-earth-ore](../../data/records/carbonatite-associated-rare-earth-ore.yaml)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Obtain matched pretreatment controls, pH and interstage inventories; resolve printed accession4TH0UUSC016 and unit conversion. Tmix membership does not establish a molecular cause.


### Visit 064: [#389 — Clarify spent vanadium electrolyte precipitation pH and material balance](https://github.com/CultureBotAI/CMMMech/issues/389)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [spent-vanadium-flow-battery-electrolyte](../../data/records/spent-vanadium-flow-battery-electrolyte.yaml)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference. Shared-owner checks: #390.
- **Acceptance:** Resolve Yang–Wang2016 pH, times and V2O5 concentration basis; obtain full liquid/product inventories and assay methods before pilot whole-feed recovery/purity claims.


### Visit 065: [#390 — Resolve spent electrolyte regeneration arm labels and charge accounting](https://github.com/CultureBotAI/CMMMech/issues/390)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [spent-vanadium-flow-battery-electrolyte](../../data/records/spent-vanadium-flow-battery-electrolyte.yaml)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference. Shared-owner checks: #389.
- **Acceptance:** Resolve Peng2024 electrolysis arm labels and charge arithmetic from cycling data; account for transferred/discarded material and replaced felt separately from capacity restoration.


### Visit 066: [#398 — Clarify Cu-Zn-alumina catalyst leaching recipe and zinc product balance](https://github.com/CultureBotAI/CMMMech/issues/398)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [spent-copper-zinc-alumina-catalyst](../../data/records/spent-copper-zinc-alumina-catalyst.yaml)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Resolve Malecki2018 liquid/solid units, peroxide dose and fine/dust inventory; keep measured alloys, liquor and retained Zn residue distinct from overall isolated-product yield.


### Visit 067: [#399 — Resolve iron-molybdate catalyst recovery ratios and assay denominators](https://github.com/CultureBotAI/CMMMech/issues/399)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [spent-iron-molybdate-oxidation-catalyst](../../data/records/spent-iron-molybdate-oxidation-catalyst.yaml)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Resolve Farhan2026 buffer/A:O arms, liquor depletion and product assay; compare Russo2023 final version and denominator/TGA with its separate feed before overall recovery claims.


### Visit 068: [#415 — Reconcile steam-reformer EDTA extraction plots, protocol and reuse evidence](https://github.com/CultureBotAI/CMMMech/issues/415)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [spent-nickel-steam-reforming-catalyst](../../data/records/spent-nickel-steam-reforming-catalyst.yaml)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Resolve Oza2011 plot/run conditions, acid/dechelation labels and calibration; require cycle-specific EDTA and Ni balances, then inspect complete comparators before quantitative expansion.


### Visit 069: [#419 — Clarify ludwigite2024 leaching calculation, grain-size and kinetic inconsistencies](https://github.com/CultureBotAI/CMMMech/issues/419)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [ludwigite-ore](../../data/records/ludwigite-ore.yaml)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Acquire Liang2017 inherited methods and 2024 run/assay metadata; reconcile low-temperature prose, exponential sign and grain size without importing another batch's roast recipe.


### Visit 070: [#420 — Resolve polymorph, treatment-time and figure-label ambiguities in the 2009 uranophane dissolution source](https://github.com/CultureBotAI/CMMMech/issues/420)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [uranophane](../../data/records/uranophane.yaml), [parauranophane](../../data/records/parauranophane.yaml)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Resolve Schindler2009 polymorph/reagent/time/image mappings from primary metadata; distinguish natural/synthetic arms and measured U release from dissolution rates under secondary-phase controls.


### Visit 071: [#423 — Clarify ferrochrome-slag magnesium extraction conditions, response plots and kinetic assignments](https://github.com/CultureBotAI/CMMMech/issues/423)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [ferrochrome-slag](../../data/records/ferrochrome-slag.yaml); [round107-resources](../../research/sources/round107-resources/20261016T003940Z-source-investigation.md)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Resolve Moyo2022 mixing/time/ratio/temperature curves and kinetic-energy labels; require Mg balance/uncertainty. Synthetic chromate study supplies no actual microbial slag evidence.


### Visit 072: [#442 — Resolve copper anode slime feed-to-liquid accounting before recovery claims](https://github.com/CultureBotAI/CMMMech/issues/442)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [copper-anode-slime](../../data/records/copper-anode-slime.yaml)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Acquire complete Zeng2023 Figures6–7 and raw feed/volume/product data; reconcile Table1/Table4 inventory and retain censored Sb before overall recovery or purity claims.


### Visit 073: [#450 — Clarify lead blast-furnace slag operational fractions and thesis method inconsistencies](https://github.com/CultureBotAI/CMMMech/issues/450)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [lead-blast-furnace-slag](../../data/records/lead-blast-furnace-slag.yaml); [round110-resources](../../research/sources/round110-resources/20261016-source-investigation.md)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Compare Yin2014 final journal with thesis and resolve filter units, pH, strain and Fe fraction arithmetic; operational associated metal includes precipitates and is not exclusive biosorption.


### Visit 074: [#461 — Resolve phosphate-tailings leaching controls, assay validation and conflicting protocols](https://github.com/CultureBotAI/CMMMech/issues/461)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [phosphate-ore-tailings](../../data/records/phosphate-ore-tailings.yaml); [round111-resources](../../research/sources/round111-resources/20261016-source-investigation.md)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Locate corrected/raw protocols and validated element assays with matched controls or a distinct controlled experiment; preserve source timing/inoculum/unit conflicts and compare IMPC2016 lineage.


### Visit 075: [#478 — Reconcile billietite and compreignacite primary-source reporting conflicts](https://github.com/CultureBotAI/CMMMech/issues/478)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [billietite](../../data/records/billietite.yaml), [compreignacite](../../data/records/compreignacite.yaml)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Resolve billietite salt/specimen captions and compare final compreignacite2017 data/model chemistry; retain separate measured column balances, fitted rates and final-solid inventories.


### Visit 076: [#497 — Resolve titanite processing feed, preparation and mass-balance ambiguities](https://github.com/CultureBotAI/CMMMech/issues/497)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [titanite](../../data/records/titanite.yaml); [round116-titanium](../../research/sources/round116-titanium/20261016-source-investigation.md)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference.
- **Acceptance:** Resolve Gerasimova2020 feed, preparation, methods and unit/size labels with source data; require stream balances before numeric extraction and separate pilot pigment from acid-route deployment.


### Visit 077: [#103 — Acquire tungsten mining-waste methods before record admission](https://github.com/CultureBotAI/CMMMech/issues/103)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** Source investigation; resolve material ownership before any CREATE.; [round31-tungsten-mining-waste](../../research/sources/round31-tungsten-mining-waste/20261011T190610Z-source-investigation.md); [comment 1](https://github.com/CultureBotAI/CMMMech/issues/103#issuecomment-6112846608)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire Han2023 full methods through a new legitimate route; reconcile waste-rock/tailings arms, +M controls, units and cumulative mass with retained figures/SI and Han2022/thesis lineage.


### Visit 078: [#104 — Acquire and reconcile full ilmenite bioleaching studies](https://github.com/CultureBotAI/CMMMech/issues/104)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [ilmenite](../../data/records/ilmenite.yaml); [round31-ilmenite](../../research/sources/round31-ilmenite/20261011T190712Z-source-investigation.md); [comment 1](https://github.com/CultureBotAI/CMMMech/issues/104#issuecomment-6112846768)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire both ilmenite journal originals; reconcile the preliminary enhancement versus journal null, ILC control label and spreadsheet err tokens. Keep basalt and tin-tailing feeds distinct.


### Visit 079: [#120 — Complete meta-autunite figure verification before record admission](https://github.com/CultureBotAI/CMMMech/issues/120)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** Source investigation; resolve material ownership before any CREATE.
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire original Smeaton2008 figures; verify calcium meta-autunite hydration, controls, transient U and tentative secondary phases before admitting a mineral owner or mechanism.


### Visit 080: [#129 — Complete vanadinite original-figure verification before admission](https://github.com/CultureBotAI/CMMMech/issues/129)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** Source investigation; resolve material ownership before any CREATE.
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire Ceci original Figures 1 and 5–10, Tables 2/4 and full Figure 3; distinguish natural chloride vanadinite from synthetic hydroxyl material and preserve null diffraction/control limits.


### Visit 081: [#133 — Verify original samarium biomineralization figures before record admission](https://github.com/CultureBotAI/CMMMech/issues/133)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [monazite-sm](../../data/records/monazite-sm.yaml); [round40-samarium-phosphate](../../research/sources/round40-samarium-phosphate/20261012T005055Z-source-deferral.md)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Inspect Jiang2018 Figures 1–8 and supplements; reconcile NaCl, temperature, biomass and time conflicts, Sm phase evidence and historical IAM1069 taxonomy without transferring unrelated viability assays.


### Visit 082: [#137 — Acquire complete Yu2012 biogenic-birnessite cobalt evidence before curation](https://github.com/CultureBotAI/CMMMech/issues/137)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [birnessite](../../data/records/birnessite.yaml); [round41-biogenic-birnessite](../../research/sources/round41-biogenic-birnessite/20261012T012315Z-source-investigation.md); [comment 1](https://github.com/CultureBotAI/CMMMech/issues/137#issuecomment-6116279640)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire complete Yu2012 main/SI; verify fungal preparation, cobalt loading/redox basis and overlap with Sasaki2008. Later metadata and author summaries do not complete the task.


### Visit 083: [#140 — Acquire and review complete Theisen sludge microbial mechanism evidence](https://github.com/CultureBotAI/CMMMech/issues/140)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [theisen-sludge](../../data/records/theisen-sludge.yaml); [round42-theisen-sludge](../../research/sources/round42-theisen-sludge/20261012T015742Z-source-investigation.md); [round45-theisen-sludge](../../research/sources/round45-theisen-sludge/20261012T035809Z-source-investigation.md); [20261012T040404Z-theisen-sludge-round45-independent](../../reviews/structured/20261012T040404Z-theisen-sludge-round45-independent/review.md); [comment 1](https://github.com/CultureBotAI/CMMMech/issues/140#issuecomment-6116588652), [comment 2](https://github.com/CultureBotAI/CMMMech/issues/140#issuecomment-6117778827)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire Klink2016 Tables 1–2, Figures 1–3 and full SI; verify strains, viable/inactivated controls and mass accounting. Existing identity-only Meschke record and synthetic membrane work are separate.


### Visit 084: [#153 — Acquire complete zircon-sand and concentrate microbial evidence before curation](https://github.com/CultureBotAI/CMMMech/issues/153)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [zircon](../../data/records/zircon.yaml); [ingests](../../research/ingests/round48-frontier-20261012.md); [round48-zirconium](../../research/sources/round48-zirconium/20261012T055936Z-source-investigation.md); [round49-resource-handoff](../../research/sources/round49-resource-handoff/20261012T064712Z-source-handoff.md); [comment 1](https://github.com/CultureBotAI/CMMMech/issues/153#issuecomment-6119028677), [comment 2](https://github.com/CultureBotAI/CMMMech/issues/153#issuecomment-6119623244), [comment 3](https://github.com/CultureBotAI/CMMMech/issues/153#issuecomment-6120276883), [comment 4](https://github.com/CultureBotAI/CMMMech/issues/153#issuecomment-6121037118)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Latest comments leave Bansal2007 Figures 1/4 and complete Hedrich2023 evidence outstanding; bind feed identity, controls and null comparisons. Already inspected ACS SI and Figures 2/3/5 need no repeat acquisition.


### Visit 085: [#169 — Acquire complete Han2026 clay-leachate recovery evidence before curation](https://github.com/CultureBotAI/CMMMech/issues/169)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** Source investigation; resolve material ownership before any CREATE.; [round55-clay-recovery](../../research/sources/round55-clay-recovery/20261012T111459Z-source-investigation.md); [comment 1](https://github.com/CultureBotAI/CMMMech/issues/169#issuecomment-6123424968)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire Han2026 main and bind its inspected SI; distinguish chemical gluconate leachate, engineered-host controls, fitted uptake and isolated recovery. Zhao2025 remains a separate source obligation.


### Visit 086: [#171 — Acquire Oyama2025 enargite main and reconcile supplementary fit statistics](https://github.com/CultureBotAI/CMMMech/issues/171)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [enargite-pyrite-concentrate](../../data/records/enargite-pyrite-concentrate.yaml); [round56-enargite-carbon](../../research/sources/round56-enargite-carbon/20261012T114658Z-source-investigation.md); [comment 1](https://github.com/CultureBotAI/CMMMech/issues/171#issuecomment-6124060090)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker. Shared-owner checks: #175.
- **Acceptance:** Acquire Oyama2025 main; reconcile Figure S4 caption R-squared threshold with displayed fits and verify carbon/feed/control arms. Hu2026 does not resolve this source.


### Visit 087: [#176 — Acquire complete Yang 2021 microbial uranium-mineral leaching evidence before extending coffinite](https://github.com/CultureBotAI/CMMMech/issues/176)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [coffinite](../../data/records/coffinite.yaml); [round57-mineral](../../research/sources/round57-mineral/20261012T124225Z-source-investigation.md)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire Yang2021 full main/SI and inspect phase-pure versus mixed synthetic U feeds, organisms, pyrite/chemical controls and denominators; existing abiotic coffinite evidence does not suffice.


### Visit 088: [#179 — Acquire complete earlier SCR microbial studies before extending mechanism claims](https://github.com/CultureBotAI/CMMMech/issues/179)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [spent-selective-catalytic-reduction-catalyst](../../data/records/spent-selective-catalytic-reduction-catalyst.yaml); [round58-scr](../../research/sources/round58-scr/20261012T132601Z-source-investigation.md)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire Wang2018 and Niu2021 originals, figures and SI; distinguish regenerated from spent feed and verify cultures/controls. Existing Niu2025/Su2020 mechanisms do not close either source gap.


### Visit 089: [#181 — Acquire complete Yao2022 tannery-sludge main before extending the record](https://github.com/CultureBotAI/CMMMech/issues/181)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [tannery-sludge](../../data/records/tannery-sludge.yaml); [round59-tannery](../../research/sources/round59-tannery/20261012T140358Z-source-investigation.md)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire Yao2022 main and assess it with the retained DOCX; verify feed, strain, controls and denominators against Wang2019 experiment lineage before extension.


### Visit 090: [#182 — Acquire and review complete Panda2017/2018 pyrite-ash multimetal evidence](https://github.com/CultureBotAI/CMMMech/issues/182)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [pyrite-roasting-cinder](../../data/records/pyrite-roasting-cinder.yaml); [round59-industrial](../../research/sources/round59-industrial/20261012T140606Z-source-investigation.md)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire Panda2017/2018 full originals/SI and compare feed, consortium and reactor lineage; separate metal mobilization from products and preserve existing limited-response evidence.


### Visit 091: [#186 — Acquire original zinc-leach-residue graphics, supplement and thesis evidence](https://github.com/CultureBotAI/CMMMech/issues/186)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [zinc-leach-residue](../../data/records/zinc-leach-residue.yaml); [round60-resource](../../research/sources/round60-resource/20261012T145058Z-source-investigation.md); [round61-zinc-residue](../../research/sources/round61-zinc-residue/20261013T020740Z-source-investigation.md); [comment 1](https://github.com/CultureBotAI/CMMMech/issues/186#issuecomment-6137087548)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker. Shared-owner checks: #377.
- **Acceptance:** Acquire Sethurajan Appendix S1 and thesis TH2015PESC1202; reconcile 5/50 g/L residue and 2.51/25.1 g/L sulfur, phases and downstream precipitation denominators. Separate from #377.


### Visit 092: [#187 — Resolve complete primary evidence for fluorite dissolution extensions](https://github.com/CultureBotAI/CMMMech/issues/187)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [fluorite](../../data/records/fluorite.yaml); [round60-mineral](../../research/sources/round60-mineral/20261012T144842Z-source-investigation.md); [round61-fluorite](../../research/sources/round61-fluorite/20261013T021048Z-source-investigation.md); [comment 1](https://github.com/CultureBotAI/CMMMech/issues/187#issuecomment-6137088069)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire Dai2019 and fungal natural-fluorite graphics; reconcile source dates, strains and dosing. The separately accepted synthetic-CaF2 fluorine assay does not establish natural-fluorite dissolution.


### Visit 093: [#191 — Acquire complete primary evidence for spent lead-acid battery paste conversion](https://github.com/CultureBotAI/CMMMech/issues/191)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** Source investigation; resolve material ownership before any CREATE.; [round61-lead-paste](../../research/sources/round61-lead-paste/20261013T020440Z.md); [comment 1](https://github.com/CultureBotAI/CMMMech/issues/191#issuecomment-6137088610)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire Weijma2002 original/SI; verify spent-paste feed and separate anglesite arms, communities, sulfur chemistry and whole-feed/product balances before new resource admission.


### Visit 094: [#194 — Acquire original diatom brucite study before mechanism curation](https://github.com/CultureBotAI/CMMMech/issues/194)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [brucite](../../data/records/brucite.yaml); [round62-uranium-vanadates](../../research/sources/round62-uranium-vanadates/20261014T044230Z-source-investigation.md); [round66-magnesium](../../research/sources/round66-magnesium/20261014T082237Z-source-investigation.md); [comment 1](https://github.com/CultureBotAI/CMMMech/issues/194#issuecomment-6161523707), [comment 2](https://github.com/CultureBotAI/CMMMech/issues/194#issuecomment-6164842056)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire Tesson2008 complete original and phase/control graphics; assess the diatom-specific formation claim independently of the accepted Prony Bay field evidence.


### Visit 095: [#197 — Acquire complete Cameron 2021 and COM 2017 methods before extending nickel-flotation-tailings](https://github.com/CultureBotAI/CMMMech/issues/197)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [nickel-flotation-tailings](../../data/records/nickel-flotation-tailings.yaml); [round63-nickel-resources](../../research/sources/round63-nickel-resources/20261014T053805Z-source-investigation.md); [comment 1](https://github.com/CultureBotAI/CMMMech/issues/197#issuecomment-6162176035)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire Cameron2021 and inherited COM2017 paper9704 methods/SI; verify magnetic upgrading, cultures and controls, and distinguish mixed-tailings extraction from pure-mineral yields.


### Visit 096: [#198 — Acquire Mavromatis 2012 original for nesquehonite phase and null-effect assessment](https://github.com/CultureBotAI/CMMMech/issues/198)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [nesquehonite](../../data/records/nesquehonite.yaml), [dypingite](../../data/records/dypingite.yaml); [round63-magnesium-carbonates](../../research/sources/round63-magnesium-carbonates/20261014T053338Z-source-investigation.md); [round65-magnesium-carbonates](../../research/sources/round65-magnesium-carbonates/20261014T072754Z-source-investigation.md); [round66-magnesium](../../research/sources/round66-magnesium/20261014T082237Z-source-investigation.md); [comment 1](https://github.com/CultureBotAI/CMMMech/issues/198#issuecomment-6162176328), [comment 2](https://github.com/CultureBotAI/CMMMech/issues/198#issuecomment-6163800237), [comment 3](https://github.com/CultureBotAI/CMMMech/issues/198#issuecomment-6164842597)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire Mavromatis2012 original; resolve phase/time assignments and preserve reported bulk-rate/isotope nulls. The 2019 carbonate and Atlin studies are separate experiments.


### Visit 097: [#202 — Acquire complete Kordloo2025 waste-aluminum-electrolyte bioleaching evidence](https://github.com/CultureBotAI/CMMMech/issues/202)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** Source investigation; resolve material ownership before any CREATE.; [round64-lithium](../../research/sources/round64-lithium/20261014T062345Z-source-investigation.md); [comment 1](https://github.com/CultureBotAI/CMMMech/issues/202#issuecomment-6162980881)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire Kordloo2025 full waste-aluminium-electrolyte evidence; establish process-derived feed identity, culture/medium controls, assays and denominators before new owner admission.


### Visit 098: [#207 — Acquire illustrated Daye 2019 dolomite main article and reconcile control/phase labels](https://github.com/CultureBotAI/CMMMech/issues/207)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [dolomite](../../data/records/dolomite.yaml); [ingests](../../research/ingests/round66-frontier-20261014.md); [round66-magnesium](../../research/sources/round66-magnesium/20261014T082237Z-source-investigation.md); [comment 1](https://github.com/CultureBotAI/CMMMech/issues/207#issuecomment-6164843144)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire Daye2019 illustrated main and reconcile gas recipe, dark-control Mn labels and reflection indices with inspected SI; retain the limited illuminated 1 mM Mn arm unless new evidence supports expansion.


### Visit 099: [#217 — Acquire the complete antigorite–Streptomyces primary study before mechanism curation](https://github.com/CultureBotAI/CMMMech/issues/217)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** Source investigation; resolve material ownership before any CREATE.; [round69-silicates](../../research/sources/round69-silicates/20261014T104745Z-source-investigation.md)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire Liu2022 antigorite/FXJ8.102 main and SI; verify feed phase, controls, glushinskite and release denominators. Antigorite in dunite does not establish a mineral-specific mechanism.


### Visit 100: [#219 — Acquire Lee and Fein 2000 primary evidence before microbial gibbsite curation](https://github.com/CultureBotAI/CMMMech/issues/219)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [gibbsite](../../data/records/gibbsite.yaml)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire Lee–Fein2000 full original; separate dissolution, adsorption and accumulation using strain, biomass, pH and sterile controls; preserve inhibitory/null outcomes.


### Visit 101: [#225 — Acquire and assess the complete orthoclase fungal-weathering experiment](https://github.com/CultureBotAI/CMMMech/issues/225)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [orthoclase](../../data/records/orthoclase.yaml); [round71-silicates](../../research/sources/round71-silicates/20261014T122302Z-source-investigation.md)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire Sun2014 full graphics/SI; resolve minor muscovite contribution and relation to Zhan2013 before choosing species versus mixed-feed scope and K/Si balance.


### Visit 102: [#232 — Acquire full direct-orpiment bioleaching studies and controls](https://github.com/CultureBotAI/CMMMech/issues/232)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [orpiment](../../data/records/orpiment.yaml); [round72-arsenic-sulfides](../../research/sources/round72-arsenic-sulfides/20261014T131236Z.md)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire both direct-orpiment bioleaching originals/SI; establish crystalline feed, Fe/Ag and abiotic controls, strains and denominator. Amorphous As2S3 and secondary-phase observations are insufficient.


### Visit 103: [#238 — Acquire complete antimonate-respiration polymorph evidence for Abin2014 and Yamamura2021](https://github.com/CultureBotAI/CMMMech/issues/238)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [senarmontite](../../data/records/senarmontite.yaml); [round73-antimony-minerals](../../research/sources/round73-antimony-minerals/20261014T135948Z.md)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire Abin2014 and Yamamura2021 complete phase/control evidence; bind dissertation versions and distinguish Sb2O3 polymorphs from EDS/morphology before mechanism expansion.


### Visit 104: [#240 — Acquire original CdTe manufacturing-scrap evidence before extending provenance or recovery claims](https://github.com/CultureBotAI/CMMMech/issues/240)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [cadmium-telluride-photovoltaic-module-scrap](../../data/records/cadmium-telluride-photovoltaic-module-scrap.yaml); [round74-cdte](../../research/sources/round74-cdte/20261014T145028Z-source-investigation.md)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire Fthenakis–Wang2006 full original and compare conference lineage; verify manufacturing-scrap provenance and Cd/Te product balance without relabelling 2021 laboratory fragments as postconsumer waste.


### Visit 105: [#244 — Acquire complete CRT microbial studies before adding glass or phosphor mechanisms](https://github.com/CultureBotAI/CMMMech/issues/244)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [cathode-ray-tube-glass](../../data/records/cathode-ray-tube-glass.yaml); [round75-crt](../../research/sources/round75-crt/20261014T154702Z.md)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire Pant2014 and Beolchini2012 complete originals; resolve glass versus CRT phosphor feeds, strains and EDTA/cell-free comparators. Keep fluorescent-lamp phosphor separate.


### Visit 106: [#247 — Acquire complete hectorite dissolution originals before mechanism curation](https://github.com/CultureBotAI/CMMMech/issues/247)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** Source investigation; resolve material ownership before any CREATE.; [round76-hectorite](../../research/sources/round76-hectorite/20261014T163029Z.md)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire Dong2026 and Van Rompaey2002 hectorite originals; verify F substitution, impurities, acid controls and measured/modelled Li balances before abiotic curation.


### Visit 107: [#248 — Acquire Lee 2011 originals and supplements before rambergite curation](https://github.com/CultureBotAI/CMMMech/issues/248)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** Source investigation; resolve material ownership before any CREATE.; [round76-sulfides](../../research/sources/round76-sulfides/20261014T163419Z-source-investigation.md)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire Lee2011 full main and actual SI; verify gamma-MnS diffraction, strains/mutants, donors and indirect-sulfide controls before assigning rambergite rather than generic/amorphous MnS.


### Visit 108: [#249 — Acquire phase-resolved microbial anilite originals before extending its abiotic record](https://github.com/CultureBotAI/CMMMech/issues/249)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [anilite](../../data/records/anilite.yaml); [round76-sulfides](../../research/sources/round76-sulfides/20261014T163419Z-source-investigation.md)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire Cheng2007/2008 full graphics/SI; verify grinding-induced phase changes, Fe-salt versus elemental doses and negative controls; deduplicate experiments and keep digenite leads distinct.


### Visit 109: [#253 — Acquire full hospital-incinerator bottom-ash bioleaching study](https://github.com/CultureBotAI/CMMMech/issues/253)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** Source investigation; resolve material ownership before any CREATE.; [round77-resources](../../research/sources/round77-resources/20261014T172009Z.md)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire Anjum2014 hospital-bottom-ash original/SI through a new route; isolate ultrasound-only, biological-only and combined arms and feed-specific metal balances before owner admission.


### Visit 110: [#256 — Acquire complete microbial sepiolite and phlogopite dissolution evidence](https://github.com/CultureBotAI/CMMMech/issues/256)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [sepiolite](../../data/records/sepiolite.yaml), [phlogopite](../../data/records/phlogopite.yaml); [round78-silicates](../../research/sources/round78-silicates/20261014T180444Z.md); [comment 1](https://github.com/CultureBotAI/CMMMech/issues/256#issuecomment-6176686094)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire 2021 sepiolite and 2019 phlogopite originals; compare the acquired 2010 thesis and retain Pinzari2024 null/control limitations. Complete one source does not complete both.


### Visit 111: [#265 — Acquire the complete ITO-etching wastewater recovery study and supplement (C5GC01244A)](https://github.com/CultureBotAI/CMMMech/issues/265)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** Source investigation; resolve material ownership before any CREATE.; [ingests](../../research/ingests/round80-frontier-20261014.md); [round80-resources](../../research/sources/round80-resources/20261014T194349Z.md); [comment 1](https://github.com/CultureBotAI/CMMMech/issues/265#issuecomment-6177888322)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire C5GC01244A main/SI; authenticate real ITO etchant feed and extraction/stripping/reduction balances. Synthetic indium solutions and solid LCD/ITO waste are different owners.


### Visit 112: [#267 — Acquire complete Garvie2022 ikaite slime-flux study before phase-specific curation](https://github.com/CultureBotAI/CMMMech/issues/267)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** Source investigation; resolve material ownership before any CREATE.; [round81-carbonates](../../research/sources/round81-carbonates/20261014T205040Z-source-investigation.md); [comment 1](https://github.com/CultureBotAI/CMMMech/issues/267#issuecomment-6178889693)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire Garvie2022 ikaite Figures 1–6 and full methods; verify specimen storage, phase mixtures, temperatures and microbial attribution against abiotic alternatives before owner admission.


### Visit 113: [#272 — Acquire complete Chang 2021 tiemannite methylation primary and official supplement](https://github.com/CultureBotAI/CMMMech/issues/272)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** Source investigation; resolve material ownership before any CREATE.
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire Chang2021 HgSe main/SI with original HRTEM/XRD and controls; distinguish abiotic tiemannite formation from subsequent ND132 methylation and verify carryover/aging.


### Visit 114: [#277 — Acquire complete microbial Bi2S3 originals before assigning bismuthinite mechanisms](https://github.com/CultureBotAI/CMMMech/issues/277)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [bismuthinite](../../data/records/bismuthinite.yaml)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire Barton2019, Kamaraj2014 and Yue2014 complete originals/SI; verify crystalline Bi2S3 assignment, biomass and abiotic controls. One acquired paper cannot close all three obligations.


### Visit 115: [#282 — Acquire the full silica-sand Shewanella journal study and clarify thesis assay provenance](https://github.com/CultureBotAI/CMMMech/issues/282)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [silica-sand](../../data/records/silica-sand.yaml); [round84-resources](../../research/sources/round84-resources/20261015T000755Z-source-investigation.md)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire Yahaya journal original and compare thesis versions; map Sand2/3, blanks and Figure5.4 and reconstruct percentage basis without equating HCl-extractable Fe with dissolved/recovered Fe.


### Visit 116: [#284 — Acquire Baldi 1987 original graphics and reassess the cinnabar-alone comparison](https://github.com/CultureBotAI/CMMMech/issues/284)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [cinnabar](../../data/records/cinnabar.yaml)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire Baldi1987 original graphics; compare washed SW9K1 cinnabar-only controls and Hg0/liquid fractions with Jew2014 before treating different conditions as contradictory experiments.


### Visit 117: [#295 — Acquire complete heterogenite bioleaching originals before adding microbial claims](https://github.com/CultureBotAI/CMMMech/issues/295)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [heterogenite](../../data/records/heterogenite.yaml)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire Zeka2015/2016 originals/SI and experimental lineage; verify mixed ore, culture and pyrite controls and Co-valence evidence before extending the abiotic owner.


### Visit 118: [#307 — Acquire complete microbial aluminium-hydroxysulfate evidence before extending felsobanyaite](https://github.com/CultureBotAI/CMMMech/issues/307)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [felsobanyaite](../../data/records/felsobanyaite.yaml); [round89-aluminium-sulfates](../../research/sources/round89-aluminium-sulfates/20261015T060953Z-source-investigation.md)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire Falagan2017/thesis and Carrero structural evidence; distinguish wet poorly ordered hydrobasaluminite from dried crystalline felsobanyaite and verify reactor controls/inventories.


### Visit 119: [#314 — Acquire and compare the complete 2001 heazlewoodite bioleaching original](https://github.com/CultureBotAI/CMMMech/issues/314)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [heazlewoodite](../../data/records/heazlewoodite.yaml); [round90-sulfides](../../research/sources/round90-sulfides/20261015T072634Z-source-investigation.md)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire Giaveno–Donati2001 original/SI and compare phase, cultures and controls with Huberts1986; retain thesis null and inspect 1988 study lineage before independent-replication claims.


### Visit 120: [#397 — Acquire primary La-phosphate biomineralization evidence for Micromonospora saelicesensis KLBMP 9669](https://github.com/CultureBotAI/CMMMech/issues/397)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [monazite-la](../../data/records/monazite-la.yaml)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker. Shared-owner checks: #396, #405.
- **Acceptance:** Acquire Zhang2024 KLBMP9669 full article/SI; verify biomass, P source, controls and SAED phase alternatives. The 2026 M. auratinigra dataset under #405 is separate.


### Visit 121: [#403 — Clarify platinum-reforming catalyst separation evidence and acquire the fungal primary study](https://github.com/CultureBotAI/CMMMech/issues/403)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [spent-platinum-petroleum-reforming-catalyst](../../data/records/spent-platinum-petroleum-reforming-catalyst.yaml); [round105-resources](../../research/sources/round105-resources/20261015T230306Z-source-investigation.md)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Resolve Sun2015 elution/purity/replicate/product definitions and acquire Malekian2019 full fungal-hybrid evidence; synthetic resin capacity cannot substitute for whole-feed Pt recovery.


### Visit 122: [#406 — Obtain original florencite-(Nd) characterization before mineral-owner admission](https://github.com/CultureBotAI/CMMMech/issues/406)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** Source investigation; resolve material ownership before any CREATE.
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire Milton–Bastron1971 and original diffraction evidence for florencite-(Nd); verify mixed chemistry and specimen, preserving the IMA placeholder as a non-unique field.


### Visit 123: [#411 — Clarify pinnoite spectroscopy water assignments and acquire original processing evidence](https://github.com/CultureBotAI/CMMMech/issues/411)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [pinnoite](../../data/records/pinnoite.yaml)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Compare Frost2014 final spectra/water assignments and acquire three processing originals; verify specimens, products and experimental versus empirical distances before adding mechanisms.


### Visit 124: [#413 — Acquire saléeite field-study figures and deposited diffraction data before mechanism expansion](https://github.com/CultureBotAI/CMMMech/issues/413)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [saleeite](../../data/records/saleeite.yaml)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire Siuda2016 complete field graphics and CSD430599; separate direct mixtures/structure from inferred pH/formation and model Fe from qualitative EDS.


### Visit 125: [#414 — Resolve later sabugalite synthesis and thermal evidence before extending the historical assay](https://github.com/CultureBotAI/CMMMech/issues/414)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [sabugalite](../../data/records/sabugalite.yaml)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire Vochten1983 and the full thermal original/erratum; resolve looping DOI metadata from actual documents before comparing natural/synthetic hydration and nonequilibrium heating.


### Visit 126: [#416 — Acquire the original xenotime-(Gd) CIF and verify AMCSD 0021444 provenance](https://github.com/CultureBotAI/CMMMech/issues/416)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [xenotime-gd](../../data/records/xenotime-gd.yaml); [round106-ree](../../research/sources/round106-ree/20261015T235305Z-source-investigation.md)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire authentic AMCSD0021444/publisher CIF; bind model to natural holotype and distinguish calculated powder pattern from measurement. Existing Raman corrigendum is already incorporated.


### Visit 127: [#421 — Source follow-up: reconcile lanthanite-(Nd) crystallization times and acquire Vallina 2015 SI](https://github.com/CultureBotAI/CMMMech/issues/421)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [lanthanite-nd](../../data/records/lanthanite-nd.yaml); [round107-ree](../../research/sources/round107-ree/20261016T004047Z-source-investigation.md)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker. Shared-owner checks: #422.
- **Acceptance:** Acquire Vallina2015 SI and authoritative time/sample maps; reconcile 4h/24h/60d phase labels and thermal symmetry before adding a bounded abiotic mechanism.


### Visit 128: [#422 — Source follow-up: acquire original lanthanite-(Nd) CIF and reflections for structural reproducibility](https://github.com/CultureBotAI/CMMMech/issues/422)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [lanthanite-nd](../../data/records/lanthanite-nd.yaml); [round107-ree](../../research/sources/round107-ree/20261016T004047Z-source-investigation.md)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker. Shared-owner checks: #421.
- **Acceptance:** Acquire authentic wm2719 CIF/HKL and match specimen/model to Morrison2013; separate mixed-REE chemistry, Nd proxy and excluded H from direct structural measurement.


### Visit 129: [#430 — Extend uranyl-silicate evidence only after resolving primary-source access and reporting limits](https://github.com/CultureBotAI/CMMMech/issues/430)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [soddyite](../../data/records/soddyite.yaml), [sklodowskite](../../data/records/sklodowskite.yaml); [round108-uranium](../../research/sources/round108-uranium/20261016T013528Z-source-investigation.md)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire Wall2010 and relevant primary clarification/deposits; resolve Giammar rates, CIF uncertainties and Vochten cycle/threshold gaps while preserving sample and mineral boundaries.


### Visit 130: [#431 — Extend tannery wastewater evidence with complete primary recovery studies](https://github.com/CultureBotAI/CMMMech/issues/431)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [tannery-wastewater](../../data/records/tannery-wastewater.yaml)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire Tobin1998, Reyes-Romero2021 and Ahmed2016 full originals/SI; verify actual feed, biomass and chemical/community arms and desorption/product accounting before existing-owner updates.


### Visit 131: [#439 — Acquire correctly attributed 2021 meyerhofferite pressure study and deposits](https://github.com/CultureBotAI/CMMMech/issues/439)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [meyerhofferite](../../data/records/meyerhofferite.yaml)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker. Shared-owner checks: #438.
- **Acceptance:** Acquire correctly attributed 2021 paper/CIF/HKL/SI; institutional filename currently supplies 2020 study. Bind specimens/phase brackets and H treatment before solved-structure expansion.


### Visit 132: [#440 — Extend boltwoodite stability evidence from complete primary experiments](https://github.com/CultureBotAI/CMMMech/issues/440)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [boltwoodite](../../data/records/boltwoodite.yaml)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire Chamberlain2025, Shvareva2011 and Burns reflection deposit; retain natural/synthetic hydration, K/Na species and filtered-U versus equilibrium/recovery distinctions.


### Visit 133: [#448 — Obtain specimen-linked synchysite-(Ce) diffraction files for reproducible refinement review](https://github.com/CultureBotAI/CMMMech/issues/448)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [synchysite-ce](../../data/records/synchysite-ce.yaml); [round110-ree](../../research/sources/round110-ree/20261016T034612Z-source-investigation.md)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Locate public or separately authorized FCF deposit and bind FCBN1–4 versus FCBN5/TF lamellae; examine proxy scattering/refinement limits. Request-only files do not authorize outreach.


### Visit 134: [#449 — Acquire gowerite refinement supplements and clarify the failed historical synthesis replication](https://github.com/CultureBotAI/CMMMech/issues/449)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [gowerite](../../data/records/gowerite.yaml)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire final Kyono2025 main and original SI/model; resolve H restraints and documented failed 1959 replication without inferring missing runs, purity or recovery.


### Visit 135: [#452 — Reconcile natroboltwoodite hydration and source-version evidence](https://github.com/CultureBotAI/CMMMech/issues/452)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [natroboltwoodite](../../data/records/natroboltwoodite.yaml)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire 2022 main/structural data and inspect retained workbooks; reconcile current one-water identity, synthetic1.5-water preparation and PNNL abstract version without inventing a correction.


### Visit 136: [#453 — Clarify metaschoepite humidity arms and acquire complete dissolution evidence](https://github.com/CultureBotAI/CMMMech/issues/453)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [metaschoepite](../../data/records/metaschoepite.yaml)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Resolve Kirkegaard2019 final RH/duration labels; acquire Stanley2019 main/Sup1 and bind EPA workbook cells to arms before dissolution expansion or kinetics.


### Visit 137: [#457 — Retrieve ginorite supplementary structure data and reconcile temperature labels](https://github.com/CultureBotAI/CMMMech/issues/457)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [ginorite](../../data/records/ginorite.yaml); [round111-borates](../../research/sources/round111-borates/20261016T042843Z-source-investigation.md)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire 2018 SI/CIF and reconcile temperature/distance fields with separate 2016 specimens; restraint-model differences do not establish a transformation.


### Visit 138: [#458 — Obtain the complete 2026 sulfoborite neutron study and reassess hydrogen bonding](https://github.com/CultureBotAI/CMMMech/issues/458)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [sulfoborite](../../data/records/sulfoborite.yaml); [round111-borates](../../research/sources/round111-borates/20261016T042843Z-source-investigation.md)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire verified 2026 neutron main/SI and compare chemistry, occupancy/H bonding to 1983 and current IMA OH/F notation; duplicated berborite DOI is not the target.


### Visit 139: [#460 — Resolve becquerelite coating identities and specimen mapping before stronger dissolution claims](https://github.com/CultureBotAI/CMMMech/issues/460)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [becquerelite](../../data/records/becquerelite.yaml); [round111-uranium](../../research/sources/round111-uranium/20261016T043005Z-source-investigation.md)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Obtain exact Schindler specimen/spectrum/time mapping and complete 2002 main; distinguish proposed mixed coatings and reused imaging from pure products or quantified inhibition.


### Visit 140: [#468 — Acquire probertite primary dissolution evidence and final crystallographic data before extending processing claims](https://github.com/CultureBotAI/CMMMech/issues/468)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [probertite](../../data/records/probertite.yaml); [round112-borates](../../research/sources/round112-borates/20261016T051609Z-source-investigation.md)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire complete 2009 dissolution original and final2022 structural/CIFs; bind feed impurities and conditions/denominator and compare H-site/extinction details before mechanism expansion.


### Visit 141: [#472 — Resolve studtite/metastudtite source discrepancies before structural or kinetic expansion](https://github.com/CultureBotAI/CMMMech/issues/472)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [studtite](../../data/records/studtite.yaml), [metastudtite](../../data/records/metastudtite.yaml); [round112-uranium](../../research/sources/round112-uranium/20261016T051818Z-source-investigation.md)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Compare final2020 rate/caption and workbook series; acquire 2026 main/SI, AM-03-036 factors and remaining SEM ZIP. Do not claim all2025 SI missing or infer universal reversibility.


### Visit 142: [#477 — Resolve borate synthesis and heated-product evidence gaps before expansion](https://github.com/CultureBotAI/CMMMech/issues/477)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [mcallisterite](../../data/records/mcallisterite.yaml), [tunellite](../../data/records/tunellite.yaml)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire 2014 recipe graphics and reconcile composition/formula basis; separately resolve tunellite heating rates and historical product assignments with phase evidence. Both mineral subscopes remain required.


### Visit 143: [#484 — Resolve curite assay conflicts and vandenbrandeite thermal evidence gaps](https://github.com/CultureBotAI/CMMMech/issues/484)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [curite](../../data/records/curite.yaml), [vandenbrandeite](../../data/records/vandenbrandeite.yaml)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire named structural/thermal supplements and newer originals; resolve curite time/pH/indices and vandenbrandeite heating/product evidence without inventing rates, pure products or unique hillocks.


### Visit 144: [#489 — Verify the 2024 calcioburbankite formation experiment and supplementary phase evidence](https://github.com/CultureBotAI/CMMMech/issues/489)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [calcioburbankite](../../data/records/calcioburbankite.yaml)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire Yuan2024 actual figure/SI files; independently review run8 and S2 phase/composition/conditions and cleaning effects, retaining unmeasured run8 REE concentration.


### Visit 145: [#491 — Acquire spent ITO target supplement and reconcile recovery and composition bases](https://github.com/CultureBotAI/CMMMech/issues/491)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [spent-ito-targets](../../data/records/spent-ito-targets.yaml)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire Gu2017 authentic SI; reconcile elemental/oxide/normalized bases, tin summaries and product masses/assays before yield/purity, scale or energy claims.


### Visit 146: [#495 — Acquire rivadavite primary structure note before extending atomic-model claims](https://github.com/CultureBotAI/CMMMech/issues/495)

- **Severity / status:** Undetermined until primary evidence is inspected; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [rivadavite](../../data/records/rivadavite.yaml)
- **Dependencies:** Missing complete originals, graphics or deposits prevent evidence-based implementation ranking; check new legitimate unpaid routes before declaring an execution blocker.
- **Acceptance:** Acquire Dal Negro1973 complete structure note and verify bibliography, specimen/cell/H model; preserve current IMA volume discrepancy and separate1967 thermal arms.


### Visit 147: [#329 — Source clarification: Lyalina2023 Supplement.xlsx Li2O weight-basis conversion](https://github.com/CultureBotAI/CMMMech/issues/329)

- **Severity / status:** Minor prospective reproducibility risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [triphylite](../../data/records/triphylite.yaml), [lithiophilite](../../data/records/lithiophilite.yaml)
- **Dependencies:** Versioned analytical/refinement/thermal evidence or authoritative clarification is required; preserve the existing qualified claims while unresolved.
- **Acceptance:** Verify Lyalina2023 Calculation B34 weight basis against B14 normalization and dependent quantities through authoritative clarification; diagnostic 3.008832 is not a replacement measured Li value.


### Visit 148: [#337 — Clarify formula and site-occupancy discrepancies in Basciano2007 hydroniumjarosite](https://github.com/CultureBotAI/CMMMech/issues/337)

- **Severity / status:** Minor prospective reproducibility risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [hydroniumjarosite](../../data/records/hydroniumjarosite.yaml)
- **Dependencies:** Versioned analytical/refinement/thermal evidence or authoritative clarification is required; preserve the existing qualified claims while unresolved.
- **Acceptance:** Resolve Basciano2007 specimen formula/site/normalization conflicts using original refinements; acquire Plasil2014 full evidence before stronger natural-endmember or H-site claims.


### Visit 149: [#366 — Resolve voltaite composition and structural-site normalization discrepancy](https://github.com/CultureBotAI/CMMMech/issues/366)

- **Severity / status:** Minor prospective reproducibility risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [voltaite](../../data/records/voltaite.yaml)
- **Dependencies:** Versioned analytical/refinement/thermal evidence or authoritative clarification is required; preserve the existing qualified claims while unresolved.
- **Acceptance:** Acquire CSD2303617/2303618 and authoritative Table4 normalization; distinguish measured chemistry from selected-crystal occupancies without doubling cations by inference.


### Visit 150: [#371 — Reconcile paramontroseite thermal product fractions and deposited models](https://github.com/CultureBotAI/CMMMech/issues/371)

- **Severity / status:** Minor prospective reproducibility risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [paramontroseite](../../data/records/paramontroseite.yaml); [round101-vanadium](../../research/sources/round101-vanadium/20261015T193316Z.md)
- **Dependencies:** Versioned analytical/refinement/thermal evidence or authoritative clarification is required; preserve the existing qualified claims while unresolved.
- **Acceptance:** Resolve Curetti2023 product fractions/calcite normalization and acquire CCDC2212426/2212427; keep powder, crystal and laser arms separate and distinguish chemistry from fitted models.


### Visit 151: [#372 — Resolve laueite composition and deposited diffraction-model qualifications](https://github.com/CultureBotAI/CMMMech/issues/372)

- **Severity / status:** Minor prospective reproducibility risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [laueite](../../data/records/laueite.yaml); [round101-phosphates](../../research/sources/round101-phosphates/20261015T193202Z-source-investigation.md)
- **Dependencies:** Versioned analytical/refinement/thermal evidence or authoritative clarification is required; preserve the existing qualified claims while unresolved.
- **Acceptance:** Obtain reflection data and defensible explanation/re-refinement of Grey2025 displacement/reporting alerts and chemistry/occupancy; alerts alone do not negate mineral identity.


### Visit 152: [#375 — Resolve borax thermal-program and borate humidity-endpoint ambiguities](https://github.com/CultureBotAI/CMMMech/issues/375)

- **Severity / status:** Minor prospective reproducibility risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [borax](../../data/records/borax.yaml), [tincalconite](../../data/records/tincalconite.yaml)
- **Dependencies:** Versioned analytical/refinement/thermal evidence or authoritative clarification is required; preserve the existing qualified claims while unresolved. Shared-owner checks: #376.
- **Acceptance:** Compare final Nishiyasu2024 and Liu–Bish2020 protocols/sequence with manuscripts; resolve DSC limit and 40%RH conflict without inventing sharper equilibrium boundaries.


### Visit 153: [#376 — Reconcile tincalconite 2002 formula table and deposited water-site model](https://github.com/CultureBotAI/CMMMech/issues/376)

- **Severity / status:** Minor prospective reproducibility risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [tincalconite](../../data/records/tincalconite.yaml)
- **Dependencies:** Versioned analytical/refinement/thermal evidence or authoritative clarification is required; preserve the existing qualified claims while unresolved. Shared-owner checks: #375.
- **Acceptance:** Obtain Luck–Wang2002 CIF/refinement and authoritative water-site clarification; reconcile Table1 formula/mass while preserving current IMA nomenclature versus model hydration.


### Visit 154: [#385 — Reconcile inyoite pressure-volume manuscript and supplement values](https://github.com/CultureBotAI/CMMMech/issues/385)

- **Severity / status:** Minor prospective reproducibility risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [inyoite](../../data/records/inyoite.yaml)
- **Dependencies:** Versioned analytical/refinement/thermal evidence or authoritative clarification is required; preserve the existing qualified claims while unresolved.
- **Acceptance:** Acquire Comboni2022 final source or corrected pressure-run table; map CIF pressure/volume and specimen provenance while retaining unsolved high-pressure phase limits.


### Visit 155: [#386 — Resolve szaibelyite thermal protocols and specimen provenance](https://github.com/CultureBotAI/CMMMech/issues/386)

- **Severity / status:** Minor prospective reproducibility risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [szaibelyite](../../data/records/szaibelyite.yaml)
- **Dependencies:** Versioned analytical/refinement/thermal evidence or authoritative clarification is required; preserve the existing qualified claims while unresolved.
- **Acceptance:** Resolve Marincea atmosphere, ramp, pretreatment and specimen labels from aliquot records; keep localities/thermal arms distinct and acquire Grice2008 deposits before structural expansion.


### Visit 156: [#387 — Clarify rhabdophane hydrothermal loading and low-conversion values](https://github.com/CultureBotAI/CMMMech/issues/387)

- **Severity / status:** Minor prospective reproducibility risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [rhabdophane-ce](../../data/records/rhabdophane-ce.yaml)
- **Dependencies:** Versioned analytical/refinement/thermal evidence or authoritative clarification is required; preserve the existing qualified claims while unresolved. Shared-owner checks: #130, #388.
- **Acceptance:** Resolve Bamforth2024 loadings and nominal-pH3 phase fractions from raw/corrected rows; preserve PXRD detection limits and distinguish crystalline conversion from Ce recovery.


### Visit 157: [#388 — Reconcile rhabdophane hydration and temperature trend wording](https://github.com/CultureBotAI/CMMMech/issues/388)

- **Severity / status:** Minor prospective reproducibility risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [rhabdophane-ce](../../data/records/rhabdophane-ce.yaml), [rhabdophane-la](../../data/records/rhabdophane-la.yaml)
- **Dependencies:** Versioned analytical/refinement/thermal evidence or authoritative clarification is required; preserve the existing qualified claims while unresolved. Shared-owner checks: #130, #387.
- **Acceptance:** Reconcile Shelyug2018 hydration/radius and separate temperature trends with primary corrections/data; sample water loss does not revise ideal IMA formulas.


### Visit 158: [#393 — Clarify hydroboracite pressure-arm summaries and deposited formula-unit metadata](https://github.com/CultureBotAI/CMMMech/issues/393)

- **Severity / status:** Minor prospective reproducibility risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [hydroboracite](../../data/records/hydroboracite.yaml); [round104-borates](../../research/sources/round104-borates/20261015T221506Z-source-investigation.md)
- **Dependencies:** Versioned analytical/refinement/thermal evidence or authoritative clarification is required; preserve the existing qualified claims while unresolved.
- **Acceptance:** Resolve Comboni2026 per-crystal transition summaries and CIF Z/density fields from versioned data; current CIFs do not establish a solved hydroboracite-II structure.


### Visit 159: [#394 — Resolve copper uranyl mineral thermal temperatures and specimen mapping](https://github.com/CultureBotAI/CMMMech/issues/394)

- **Severity / status:** Minor prospective reproducibility risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [metatorbernite](../../data/records/metatorbernite.yaml), [metazeunerite](../../data/records/metazeunerite.yaml); [round104-uranium](../../research/sources/round104-uranium/20261015T221713Z-source-investigation.md)
- **Dependencies:** Versioned analytical/refinement/thermal evidence or authoritative clarification is required; preserve the existing qualified claims while unresolved.
- **Acceptance:** Obtain source temperature-pattern and specimen maps plus deposits2307946/2307947; preserve separate natural air/vacuum/synthetic arms and sampled transition brackets.


### Visit 160: [#395 — Resolve florencite Raman specimen labels and incomplete F1 chemistry in Ghignone et al. (2024)](https://github.com/CultureBotAI/CMMMech/issues/395)

- **Severity / status:** Minor prospective reproducibility risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [florencite-la](../../data/records/florencite-la.yaml)
- **Dependencies:** Versioned analytical/refinement/thermal evidence or authoritative clarification is required; preserve the existing qualified claims while unresolved.
- **Acceptance:** Resolve Ghignone2024 F1/VS17/F2 Raman columns and peak labels using specimen-linked data; semiquantitative 35.6% oxide total is not complete bulk chemistry.


### Visit 161: [#396 — Resolve La-specific microwave recipe and Nd phase-label discrepancies in Zhoujin et al. (2025)](https://github.com/CultureBotAI/CMMMech/issues/396)

- **Severity / status:** Minor prospective reproducibility risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [monazite-la](../../data/records/monazite-la.yaml), [monazite-nd](../../data/records/monazite-nd.yaml)
- **Dependencies:** Versioned analytical/refinement/thermal evidence or authoritative clarification is required; preserve the existing qualified claims while unresolved. Shared-owner checks: #397, #405.
- **Acceptance:** Obtain Zhoujin2025 La precursor/direct-route run sheets and Nd pH/refinement maps; do not transfer Nd loading/onset/durability into La or infer yields from phase proportions.


### Visit 162: [#404 — Reconcile zeunerite neutron-study provenance and acquire competing structural evidence](https://github.com/CultureBotAI/CMMMech/issues/404)

- **Severity / status:** Minor prospective reproducibility risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [zeunerite](../../data/records/zeunerite.yaml); [round105-uranium](../../research/sources/round105-uranium/20261015T230406Z-source-investigation.md)
- **Dependencies:** Versioned analytical/refinement/thermal evidence or authoritative clarification is required; preserve the existing qualified claims while unresolved.
- **Acceptance:** Acquire Hennig2003, Locock structure factors and relevant ISIS runs; reconcile thesis year/container/occupancy and sample-temperature mapping without borrowing metatorbernite AIRSS validation.


### Visit 163: [#408 — Reconcile inderborite pressure/CIF inconsistencies before detailed structural reuse](https://github.com/CultureBotAI/CMMMech/issues/408)

- **Severity / status:** Minor prospective reproducibility risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [inderborite](../../data/records/inderborite.yaml); [round105-borates](../../research/sources/round105-borates/20261015T230558Z-source-investigation.md)
- **Dependencies:** Versioned analytical/refinement/thermal evidence or authoritative clarification is required; preserve the existing qualified claims while unresolved.
- **Acceptance:** Resolve Comboni2024 pressure/CIF, angle and quadratic-elongation conflicts; compare final neutron paper/SI for H-bond values. Preserve arms and unsolved high-pressure structure.


### Visit 164: [#409 — Obtain inderite pressure supplements and reconcile transition/modulus source conflicts](https://github.com/CultureBotAI/CMMMech/issues/409)

- **Severity / status:** Minor prospective reproducibility risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [inderite](../../data/records/inderite.yaml); [round105-borates](../../research/sources/round105-borates/20261015T230558Z-source-investigation.md)
- **Dependencies:** Versioned analytical/refinement/thermal evidence or authoritative clarification is required; preserve the existing qualified claims while unresolved.
- **Acceptance:** Acquire final pressure paper/S1/S2/CIFs and reconcile bracket/modulus/max pressure; bind neutron mislabeled blocks to actual inderite metadata without editing raw files.


### Visit 165: [#418 — Resolve calcioveatchite2024 measured SrO range and obtain deposited refinement data](https://github.com/CultureBotAI/CMMMech/issues/418)

- **Severity / status:** Minor prospective reproducibility risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [calcioveatchite](../../data/records/calcioveatchite.yaml)
- **Dependencies:** Versioned analytical/refinement/thermal evidence or authoritative clarification is required; preserve the existing qualified claims while unresolved. Shared-owner checks: #412.
- **Acceptance:** Resolve Pekov2024 measured SrO range versus ideal column and acquire CIF/reflections; keep separate water preparations and do not transfer holotype results to RG701/1 in #412.


### Visit 166: [#427 — Clarify larderellite thermal mass balance and product assignments in Fastelli 2020](https://github.com/CultureBotAI/CMMMech/issues/427)

- **Severity / status:** Minor prospective reproducibility risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [larderellite](../../data/records/larderellite.yaml)
- **Dependencies:** Versioned analytical/refinement/thermal evidence or authoritative clarification is required; preserve the existing qualified claims while unresolved.
- **Acceptance:** Obtain Fastelli2020 TG/DSC raw data and complete 1997 product source; reconcile total loss/step counting while distinguishing inferred gases, impurities and separately measured aliquots.


### Visit 167: [#428 — Clarify Terribili 2025 carbonate phase fractions, rehydration endpoint and time axes before broader ingestion](https://github.com/CultureBotAI/CMMMech/issues/428)

- **Severity / status:** Minor prospective reproducibility risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [lanthanite-la](../../data/records/lanthanite-la.yaml), [lanthanite-ce](../../data/records/lanthanite-ce.yaml), [kozoite-la](../../data/records/kozoite-la.yaml)
- **Dependencies:** Versioned analytical/refinement/thermal evidence or authoritative clarification is required; preserve the existing qualified claims while unresolved. Shared-owner checks: #429.
- **Acceptance:** Resolve Terribili2025 phase-fraction differences, time units and incomplete rehydration from raw/refined runs; preserve denominators and separate the Nd2015 task #421.


### Visit 168: [#437 — Clarify kurnakovite experiment duration and mixed-assemblage equilibrium calculation](https://github.com/CultureBotAI/CMMMech/issues/437)

- **Severity / status:** Minor prospective reproducibility risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [kurnakovite](../../data/records/kurnakovite.yaml)
- **Dependencies:** Versioned analytical/refinement/thermal evidence or authoritative clarification is required; preserve the existing qualified claims while unresolved.
- **Acceptance:** Resolve Xiong2020 duration/loading and reproduce model equations with documented activity basis; retain mixed assemblage and one-sided precipitation rather than pure-mineral equilibrium claims.


### Visit 169: [#438 — Resolve meyerhofferite B2O3 and analytical-total inconsistencies](https://github.com/CultureBotAI/CMMMech/issues/438)

- **Severity / status:** Minor prospective reproducibility risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [meyerhofferite](../../data/records/meyerhofferite.yaml)
- **Dependencies:** Versioned analytical/refinement/thermal evidence or authoritative clarification is required; preserve the existing qualified claims while unresolved. Shared-owner checks: #439.
- **Acceptance:** Resolve Gatta2022 B2O3, total and formula calculation from original analyses/correction; do not normalize or replace printed values and distinguish furnace loss from direct water assay.


### Visit 170: [#441 — Resolve kozoite-(Nd) volatile estimates and heated-residue identity](https://github.com/CultureBotAI/CMMMech/issues/441)

- **Severity / status:** Minor prospective reproducibility risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [kozoite-nd](../../data/records/kozoite-nd.yaml)
- **Dependencies:** Versioned analytical/refinement/thermal evidence or authoritative clarification is required; preserve the existing qualified claims while unresolved.
- **Acceptance:** Obtain Miyawaki2000 thermal/gas calibration and uncertainty; retain differing CO2/H2O estimates and require matched heated-residue characterization before product identity or recovery.


### Visit 171: [#447 — Reconcile burbankite analogue thermal reporting and normalization metadata](https://github.com/CultureBotAI/CMMMech/issues/447)

- **Severity / status:** Minor prospective reproducibility risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [burbankite](../../data/records/burbankite.yaml); [round110-ree](../../research/sources/round110-ree/20261016T034612Z-source-investigation.md)
- **Dependencies:** Versioned analytical/refinement/thermal evidence or authoritative clarification is required; preserve the existing qualified claims while unresolved.
- **Acceptance:** Resolve Milani2022 thermal fits, range and normalization from versioned sources; preserve measured/fitted distinctions, mixed synthetic analogue and natural-material boundary.


### Visit 172: [#459 — Reconcile schoepite CIF formula, density and second-crystal refinement metadata](https://github.com/CultureBotAI/CMMMech/issues/459)

- **Severity / status:** Minor prospective reproducibility risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [schoepite](../../data/records/schoepite.yaml); [round111-uranium](../../research/sources/round111-uranium/20261016T043005Z-source-investigation.md)
- **Dependencies:** Versioned analytical/refinement/thermal evidence or authoritative clarification is required; preserve the existing qualified claims while unresolved.
- **Acceptance:** Reconcile Plasil2018 CIF formula/density and second-crystal residuals using authoritative versions/specimen maps; no silent H repair or structural-complexity-to-kinetics inference.


### Visit 173: [#462 — Source follow-up: reconcile donnayite-(Y) refinement agreement metadata](https://github.com/CultureBotAI/CMMMech/issues/462)

- **Severity / status:** Minor prospective reproducibility risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [donnayite-y](../../data/records/donnayite-y.yaml); [round111-ree](../../research/sources/round111-ree/20261016T043038Z-source-investigation.md)
- **Dependencies:** Versioned analytical/refinement/thermal evidence or authoritative clarification is required; preserve the existing qualified claims while unresolved.
- **Acceptance:** Resolve Part1 Rint/table/CIF processing definitions and bind CSD2223388 to CMNMC90405, keeping the unsuccessful holotype refinement separate.


### Visit 174: [#463 — Source follow-up: reconcile alicewilsonite-(YCe) site occupancy and agreement fields](https://github.com/CultureBotAI/CMMMech/issues/463)

- **Severity / status:** Minor prospective reproducibility risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [alicewilsonite-yce](../../data/records/alicewilsonite-yce.yaml); [round111-ree](../../research/sources/round111-ree/20261016T043038Z-source-investigation.md)
- **Dependencies:** Versioned analytical/refinement/thermal evidence or authoritative clarification is required; preserve the existing qualified claims while unresolved.
- **Acceptance:** Resolve Part2 Sr1 occupancy, Rint/unique-reflection and comparative d fields from authoritative versions; retain rim/mixed-crystal, proxy and volatile limitations.


### Visit 175: [#470 — Source follow-up: reconcile bainbridgeite-(YCe) optical, powder and atom-label discrepancies](https://github.com/CultureBotAI/CMMMech/issues/470)

- **Severity / status:** Minor prospective reproducibility risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [bainbridgeite-yce](../../data/records/bainbridgeite-yce.yaml); [round112-ree](../../research/sources/round112-ree/20261016T051500Z-source-investigation.md)
- **Dependencies:** Versioned analytical/refinement/thermal evidence or authoritative clarification is required; preserve the existing qualified claims while unresolved.
- **Acceptance:** Resolve Part3 optical, powder and atom-label/version discrepancies with exact model/specimen mapping; retain the 2026 core/rim qualification and scattering limitations.


### Visit 176: [#471 — Source follow-up: clarify alicewilsonite-(YLa) deposited water labels and absorption geometry](https://github.com/CultureBotAI/CMMMech/issues/471)

- **Severity / status:** Minor prospective reproducibility risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [alicewilsonite-yla](../../data/records/alicewilsonite-yla.yaml); [round112-ree](../../research/sources/round112-ree/20261016T051500Z-source-investigation.md)
- **Dependencies:** Versioned analytical/refinement/thermal evidence or authoritative clarification is required; preserve the existing qualified claims while unresolved.
- **Acceptance:** Resolve Part4 water labels and absorption geometry from corrected/versioned deposits; changed labels are not changed coordinates, and proxy occupancies are not measured chemistry.


### Visit 177: [#482 — Reconcile borate primary-source thermal and hydrogen-model discrepancies](https://github.com/CultureBotAI/CMMMech/issues/482)

- **Severity / status:** Minor prospective reproducibility risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [kaliborite](../../data/records/kaliborite.yaml), [preobrazhenskite](../../data/records/preobrazhenskite.yaml)
- **Dependencies:** Versioned analytical/refinement/thermal evidence or authoritative clarification is required; preserve the existing qualified claims while unresolved.
- **Acceptance:** Obtain thermal/reflection data or authoritative clarification of kaliborite formulas/protocol and preobrazhenskite reflection/H labels; derivative coordinates do not supply measured reflections.


### Visit 178: [#483 — Reconcile calcioancylite-(La) chemistry and deposited refinement metadata](https://github.com/CultureBotAI/CMMMech/issues/483)

- **Severity / status:** Minor prospective reproducibility risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [calcioancylite-la](../../data/records/calcioancylite-la.yaml)
- **Dependencies:** Versioned analytical/refinement/thermal evidence or authoritative clarification is required; preserve the existing qualified claims while unresolved.
- **Acceptance:** Resolve Wang2023 F range/mean and table/CIF formula weight/refinement fields using original analyses/revised deposit; retain proxy model, calculated volatiles and missing factors.


### Visit 179: [#490 — Resolve andersonite diffraction wavelength and deposited hydration evidence](https://github.com/CultureBotAI/CMMMech/issues/490)

- **Severity / status:** Minor prospective reproducibility risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [andersonite](../../data/records/andersonite.yaml)
- **Dependencies:** Versioned analytical/refinement/thermal evidence or authoritative clarification is required; preserve the existing qualified claims while unresolved.
- **Acceptance:** Acquire authentic CSD1877782/SI for specimen1272 and resolve Co/Cu radiation with instrument/primary metadata; distinguish refined5.3-water occupancy from ideal six-water and bulk assays.


### Visit 180: [#496 — Reconcile the deposited uranopilite refinement with Plasil 2014 Tables 16–17](https://github.com/CultureBotAI/CMMMech/issues/496)

- **Severity / status:** Minor prospective reproducibility risk; unranked implementation priority; **needs source investigation**.
- **Current evidence / owner:** [uranopilite](../../data/records/uranopilite.yaml)
- **Dependencies:** Versioned analytical/refinement/thermal evidence or authoritative clarification is required; preserve the existing qualified claims while unresolved.
- **Acceptance:** Bind Plasil2014 Table16/17 and CIF metrics to model/reflection sets with authoritative provenance; retain conflicting parameters/R1/density and do not infer H occupancy from an H-free sum.


### Visit 181: [#469 — Resolve priceite powder-model direction discrepancy and reassess unavailable structure/thermal originals](https://github.com/CultureBotAI/CMMMech/issues/469)

- **Severity / status:** Undetermined; source access partly embargoed; unranked implementation priority; **partly blocked by dated embargo; other subtasks need source investigation**.
- **Current evidence / owner:** [priceite](../../data/records/priceite.yaml); [round112-borates](../../research/sources/round112-borates/20261016T051609Z-source-investigation.md)
- **Dependencies:** The 2025-deposit subtask is blocked until 2026-11-21 unless a distinct legitimate authorized source appears; earlier-source subtasks remain independently investigable.
- **Acceptance:** Resolve 2002 direction in a stated setting with 2011 structure/CIF; seek 2017 thermal original. Recheck the 2025 deposit after 2026-11-21 embargo; keep that subtask blocked until then.


### Visit 182: [#226 — Resolve DW018 sequence and raw-data provenance before stronger calcite claims](https://github.com/CultureBotAI/CMMMech/issues/226)

- **Severity / status:** Major prospective identity/causality risk; unranked implementation priority; **skip: owner changed within two days**.
- **Current evidence / owner:** [calcite](../../data/records/calcite.yaml); [round71-carbonates](../../research/sources/round71-carbonates/20261014T122206Z-source-investigation.md)
- **Dependencies:** Authoritative specimen, phase or culture evidence is still required; source uncertainty prevents a defensible corrective implementation rank. Recent owner bytes require skipping this issue in this batch.
- **Acceptance:** Locate authoritative DW018 sequence/raw-data deposit and bind it to the culture; preserve genus-only grounding, calcium-independent early removal and distinct two-hour calcite formation unless data resolve them.


### Visit 183: [#287 — Resolve zincite2020 dose and Zn balance inconsistencies before quantitative curation](https://github.com/CultureBotAI/CMMMech/issues/287)

- **Severity / status:** Major prospective quantitative/causality risk; unranked implementation priority; **skip: owner changed within two days**.
- **Current evidence / owner:** [zincite](../../data/records/zincite.yaml)
- **Dependencies:** Original run data, matched controls or attributable correction/clarification are required; current source contradictions cannot be fixed by inference. Recent owner bytes require skipping this issue in this batch.
- **Acceptance:** Resolve Sebesta2020 ZnO dose, Figure2 units/dilution and separate oxalate-consumption balance using primary data; mixed Figure4 phases do not establish conversion efficiency.


## Coverage and remaining work

All 183 acquired open issue numbers appear exactly once above and in the paired evidence JSON. All 29 acquired comments are represented. No issue is marked resolved merely because a narrower record was merged. No new scientific claim or source-access success is asserted by this plan. The implementation ledger begins with every item pending investigation except the two required recent-record skips and the explicit embargo subtask. Publication and Phase 2 remain separate work.
