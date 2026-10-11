# Round22 reviewed resource additions and evidence extensions

Worktree: `/private/tmp/CMMMech-expansion-round22-20261011`.
Branch: `curate/cmm-expansion-round22-20261011`.
Trusted base: `b19103bb393096e405bbecd2808a1aa0e01bb200`.
Acceptance: [issue 80](https://github.com/CultureBotAI/CMMMech/issues/80).

Two new resources and two updates bring the corpus to **154 records**. Seafloor massive sulfides have a narrowly scoped thermophilic laboratory leaching study. End-of-life crystalline-silicon photovoltaic modules have evidence for silver-bearing cathode deposition from chemically prepared real-module leachate using a living bioanode. Existing nodules gain separate Baltic growth and partitioning experiments; PCBs gain stage-specific ferric-regeneration evidence and a paired dataset. No resource inherits constituent criticality, and no industrial or closed-process recovery claim is inferred.

## Independent scientific reviews

| Change | Record | Kind | Final exact-state review |
|---|---|---|---|
| New | [End-of-life crystalline-silicon photovoltaic modules](../../data/records/end-of-life-crystalline-silicon-photovoltaic-modules.yaml) | secondary_resource | [YAML](../../reviews/structured/20261011T132124Z-pv-modules-round22-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T132124Z-pv-modules-round22-independent/review.md) |
| New | [Seafloor massive sulfides](../../data/records/seafloor-massive-sulfides.yaml) | primary_resource | [YAML](../../reviews/structured/20261011T132327Z-seafloor-massive-sulfides-round22-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T132327Z-seafloor-massive-sulfides-round22-independent/review.md) |
| Updated | [Polymetallic nodules](../../data/records/polymetallic-nodules.yaml) | primary_resource | [YAML](../../reviews/structured/20261011T132229Z-polymetallic-nodules-round22-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T132229Z-polymetallic-nodules-round22-independent/review.md) |
| Updated | [Waste printed circuit boards](../../data/records/waste-printed-circuit-boards.yaml) | secondary_resource | [YAML](../../reviews/structured/20261011T132452Z-waste-printed-circuit-boards-round22-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T132452Z-waste-printed-circuit-boards-round22-independent/review.md) |

All four changed records have actual CREATE/EDIT sidecars, distinct inline events and independent scientific reviews matching final hashes. Prior unchanged mechanism fields in the two extended records retain their earlier independent scientific coverage; the new reviews disclose that boundary. The [manifest](round22-frontier-20261011.json) lists record/history/review paths and before/after hashes.

The PCB independent reviewer identified joined words and quantities in its source dossier. [Issue 81](https://github.com/CultureBotAI/CMMMech/issues/81) tracks the minor readability correction, independently verified before the final review was saved. Context hashes were refreshed; record bytes, source measurements and immutable prior reviews were unchanged. No fictitious predecessor finding is created.

## Evidence limits and remaining work

Sulfide source inconsistencies include gallium inventory, salt units and endpoint wording. The PV study separates living bioanode activity from an abiotic cathode and chemical module pretreatment; its blank XRD trace and missing matched controls remain explicit. Nodule experiments distinguish local CT patches from whole-nodule growth, azide controls from matched biological controls, and bottle-wall material from nodule accumulation; supplementary tables remain unavailable. The PCB study retains synthetic electrowinning, acid-washed residue, particle-size and workbook discrepancies. None establishes a universal yield or particular consortium member's causality.

See the [prioritized next ingests](round22-frontier-20261011.md) and paired dossiers. Primary sources and raw datasets remain outside Git. No schema, validator, skill or governed-artifact change was needed.

## Checks and preservation

Baseline: 308 tests passed, 3 skipped in 120.45 seconds; 152 records and 169 histories. Final `just check`: **308 passed, 3 skipped in 124.01s (0:02:04)**. All **154 records and 173 history sessions** validate. Separate `validate --require-records`, trusted-base history and structured-review checks passed; **173 review pairs** are valid. All 154 current records have independent scientific coverage matching current hashes.

Of 986 prior scientific files under data/history/reviews/research, **984 are byte-identical**; only the two explicitly named maintained records changed. All earlier sidecars, review bundles and source dossiers are preserved. All 23 review bases resolve; the annotated source-survey provenance tag is retained, and new reviews use the merged trusted base.

The 22 governed artifacts match CLAW pin `a5d562962c75a2ad9efd8160b548df5944315422`. Live ruleset 24692449 remains active with SQUASH/ALLGREEN queue, required validate-strict from App 15368 and no bypass actors. Admission and shared history are installed; the documented PR shepherd is manual/comment-only. This curation batch does not configure fleet capabilities. Future integration must use CLAW's supported admission and synchronization process.

Publication audit, exact-tree squash-shaped validation, native queue admission, actual merge verification, topic-branch deletion and fresh remote-main checks remain pending at preparation of this report. Terminal publication receipts belong on the PR. Original-main advancement requires clean-state, new-path/symlink collision and ignored/untracked preservation checks; unrelated worktrees remain intact.
