# Independent round 15 publication and contract audit

UTC completion: **2026-10-11T10:08:18Z**. Reviewer: **Codex /root/round15_publication_adversary (GPT-6)**.
The exact initial assessment start was not separately clocked. I authored none of
this batch's records, histories, source dossiers, scientific reviews, schema,
documentation changes or regression tests. Independence is separation from those
authors within the same team, not organizational independence.

## Record IDs, revision and working changes

Repository: `CultureBotAI/CMMMech`. Worktree:
`/private/tmp/CMMMech-expansion-round15-20261011`.
Branch: `curate/cmm-expansion-round15-20261011`.
Trusted base and current HEAD: `a2e2c82f11d97982f0cc1ae6be452a42b24a0ff0`.
This is an **uncommitted working-tree** assessment. The package comprises three
new records, three actual CREATE histories, five structured review pairs,
source/frontier/publication dossiers, the native `primary_resource` enum,
related guide/skill/README changes, one behavioral regression and this audit.
There are 31 proposed paths including this artifact: five modified tracked
owners and 26 additions.

The targets are `cmmmech:dittmarite`, `cmmmech:glushinskite` and
`cmmmech:lithium-bearing-geothermal-brine`, at their corresponding
`data/records/<slug>.yaml` paths. The
[publication report](../../../research/ingests/round15-20261011-publication.md)
links their final exact-state scientific reviews and source dossiers.

## Scope and evidence checked

I read the working guide, record and review contracts, applicable local review
skill, authoritative schema and validator, regression tests, all three new
records and CREATE sessions, all five new review observations, the two source
dossiers, frontier and publication report, and the complete tracked diff.
I independently measured current hashes, review coverage, original-file
preservation and local links. Structural gates were executed by root and the
record reviewers; I read their completed terminal receipts and logs rather than
claiming to have rerun them.

Inventory and text searches included hidden and ignored files, with relevant
links followed, across the worktree's `data`, `history`, `reviews`, `research`
and `.claude` trees and the named `/private/tmp/cmm-round15-brine-raw` evidence
directory. Searches used `rg --no-ignore --hidden --follow`. This is bounded
repository/source review, not machine-wide absence or exhaustive PDF indexing.

Primary-source challenge sampling focused on the brine's unusual resource kind
and outcome claims. I independently read retained original methods/results,
DSMZ and NCBI authority pages, and visually inspected main Figure 1, supplementary
Figure S5, Figure S7 and Table S7. The original paper supports natural,
unsterilized Cornish brine treated with prepared DSM 33 cells under laboratory
conditions. Hourly sampling, comparator Mn depletion, differing Figure 1/S5
trajectories and conflicting model signs prevent unqualified kinetic or yield
claims. The record retains these limitations, unspecified metal sample-fraction
handling and missing Li wavelength. Mixed carbonate identification is an author
assignment; lithium retained in solution is not isolated recovery. This is
risk-based sampling, not a second complete scientific review of all 122 records.
The per-record reviewers separately inspected the mineral primary methods,
figures, IMA identities and taxonomic scope.

Retained original brine paper SHA-256:
`3b1dd238e4fb9652d82846dcdb3d304edc667ff918977566d7da05522c6e6af8`.
Retained 27-page supplement SHA-256:
`d484e7bdfde39ed1e262a0095308a562c7ae971c724de2bc8a0c8564a2beff19`.
These were downloaded by the curator from legitimate institutional/EuropePMC
sources and independently read here. My direct RSC/PMC reader attempts met
403/challenge responses; I did not treat those responses or search snippets
as experimental evidence. Raw PDFs and figures remain outside Git.

## Findings by severity, corrections and disposition

**Final unresolved findings: 0 blocker, 0 major, 0 minor.** Two supported audit
findings were addressed before acceptance; this does not remove the scientific
limitations explicitly retained in the records.

### Major contract gap addressed: issue #60

[Issue #60](https://github.com/CultureBotAI/CMMMech/issues/60) arose from the real
natural-brine pilot. The former enum lacked a truthful primary-resource kind;
forcing this feed into a secondary-resource, commodity or mineral category would
misrepresent its identity. The native schema now defines `primary_resource`,
with matching guidance in `docs/records.md`, README and the add-record skill.
No existing record is reclassified or given inherited lithium criticality.

I reviewed the regression: it accepts a synthetic primary-resource fixture with
scoped microbial separation evidence and no criticality, then accepts its
identity-only form, and rejects the unsupported `primary-resource` spelling.
The validator still derives a closed schema; no validator implementation,
dependency, workflow or governed CLAW artifact was changed. The full native
gate includes the new regression. The substantive correction is accepted locally;
GitHub closure and publication are subsequent operations.

### Minor review-context error corrected: issue #61

[Issue #61](https://github.com/CultureBotAI/CMMMech/issues/61) concerns the two
initial mineral reviews, not their maintained scientific targets. Their search
scope and limitations mistakenly said both existing magnesium and struvite
records reused Suyamud 2020. I read the actual source lists: **magnesium,
dittmarite and glushinskite use Suyamud 2020, DOI 10.1111/1462-2920.14949;
the existing struvite record uses separate Kang 2022 evidence, DOI
10.1007/s00253-021-11721-0.** Shared mineral/organism context does not make these
papers one experiment.

The correction is explicitly retained in these successors:

- Dittmarite: [initial review](../../structured/20261011T100137Z-dittmarite-round15-independent/review.yaml)
  and [corrected successor](../../structured/20261011T100535Z-dittmarite-round15-successor/review.yaml).
- Glushinskite: [initial review](../../structured/20261011T100137Z-glushinskite-round15-independent/review.yaml)
  and [corrected successor](../../structured/20261011T100535Z-glushinskite-round15-successor/review.yaml).

Both successors capture the contextual magnesium/struvite inputs, explicitly
link their predecessors, retain actual earlier evidence-access/check times,
and preserve the unchanged target hashes. Their empty findings lists do not
invent a resolved finding ID in an original observation that had no finding.
No fictitious scientific edit or history session was created. I independently
verified both original YAML/Markdown pairs remain unchanged, and the final
publication report points at the successors. Original YAML hashes are:

- Dittmarite: `f0572d369bebe1bef5f00d074a3048092d67fa46d96af0c2bd7f4094244791d0`.
- Glushinskite: `87c39aa66a11f8d13c7a4d30c774d403d3c78fde4d368a5d84b360284be51d00`.

The review-provenance correction is accepted. The original observations remain
historical; their two erroneous source-lineage statements are superseded by the
linked successors and this explicit correction. GitHub issue closure is not
claimed at this timestamp.

## Independent package verification

- **122 records:** 64 elements, 30 commodities, 16 minerals, 11 secondary
  resources and one primary resource; these are identities, not independent
  experiments or a disjoint resource inventory.
- **138 history sidecars; 137 structured YAML/Markdown review pairs.** Five pairs
  are new because both initial mineral reviews and their successors are retained.
- **122/122 exact current independent scientific-review coverage.** Each record
  has a completed independent passing or qualified-passing review with the exact
  record SHA and matching actually reviewed target ID. All three final addition
  reviews pass with limitations. Old mineral observations do not replace the
  corrected final successors linked above.
- All **747 prior tracked scientific-tree files** under `data`, `history`,
  `reviews` and `research` are byte-identical to the trusted base, checked against
  `git archive`. Existing records, histories and committed reviews were not edited.
- All **122 gated record hashes** still match. All **13 available path/SHA
  assertions** traversed in the new JSON source/frontier dossiers match their
  local files; repeated representations are not independent sources.
- Before this audit was added, **186 local Markdown links** in README and new
  documents resolved. The artifact's added relative links were checked when saved.
  Proposed additions contain only Markdown, YAML and JSON; no raw PDF, ZIP or
  other binary source is proposed for Git. A targeted credential-pattern scan of
  new visible text files found no matches; this is not a whole-machine audit.
- The only previously tracked modified owners are README, the record guide,
  add-record skill, native schema and validation test file. The two earlier
  mineral review pairs are also preserved against their pre-correction hashes.

My independent measurement receipt is
`/private/tmp/cmm-round15-publication-adversary-checks.json`; the core results
are retained here so this verdict does not depend on that temporary path.

## Actual validation evidence

I read the terminal receipts and actual logs below. Passing output was not
inferred while a parent or child process was still running.

| Gate | Observed terminal result |
|---|---|
| `UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache just check` | Root session 53914 exit 0; 308 passed, 3 skipped in 99.07 s; 122 records and 138 histories valid |
| `uv run --locked cmmmech validate --require-records` | Exit 0; 122 checked, 0 failed |
| `uv run --locked cmmmech validate-history --base a2e2c82f11d97982f0cc1ae6be452a42b24a0ff0` | Exit 0; 138 histories, 0 errors |
| `just review-check --require-reviews --base a2e2c82f11d97982f0cc1ae6be452a42b24a0ff0` | Root session 30744 exit 0; 137 valid reviews, `declared_scopes_only` |
| `bash scripts/check_vendored_sync.sh` | Root session 59811 exit 0; all 22 governed artifacts match the pin |

The authoritative temporary receipts read were
`/private/tmp/cmm-round15-native-terminal-receipt.json`,
`/private/tmp/cmm-round15-gate-receipts.json` and
`/private/tmp/cmm-round15-package-terminal-receipt.json`, with the named native,
nonempty-corpus, history, review and vendored-sync logs. Independent manual hash
coverage supplements the checker's declared-scope gate. Validation does not
establish scientific causality or product recovery.

## Review-base retention and governance

All **16 distinct review bases** resolve. Fifteen are in the trusted main ancestry.
The remaining revision, `c0adc2c0763e1515ed07dc712b024974d98fb342`, is retained
by annotated tag `review-base/cmm-source-survey-20261009`. My independent remote
read returned tag object `fc4040c3abcd28f0a9cc52467e308100144ad1fd` and that exact
peeled commit; remote main was the trusted base. Every new round 15 review uses
that already merged main base, so no new review depends only on the topic branch.

A live ruleset read confirmed **24692449** active, native **SQUASH / ALLGREEN**,
required `validate-strict` from integration **15368**, and no bypass actors.
CLAW pin is `a5d562962c75a2ad9efd8160b548df5944315422`; the 22-file sync gate
passed. Existing fleet admission and shared history remain installed. The
checked PR shepherd is manual and comment-only. Any future governance change
must use CLAW's supported admission/synchronization process.

## Unresolved questions and verdict

**Pass with limitations for publication of these inspected bytes.** The two
supported audit findings have concrete local corrections. Remaining source
conflicts, incomplete purity/recovery evidence, unresolved comparator accession,
future mineral/feed leads and five grade umbrellas remain openly documented.
No global discovery-exhaustion or industrial-deployment conclusion is justified.

Commit/push, PR CI, isolated squash-shaped checkout verification, native queue
admission, actual merge, branch deletion, fresh remote-main validation, original
ignored/untracked-file preservation, and installed skill synchronization are
**not yet claimed complete**. Root must record those actual outcomes in the PR
completion receipt. The squash preflight must exclude the topic commit, fetch
retained tags explicitly, and check records, trusted-base history and structured
reviews; the fresh post-merge clone must repeat the required gates. Original
checkout advancement requires collision checks and matching ignored-inclusive
before/after snapshots. Installed skill synchronization requires checking its
existing bytes before replacing only the authorized skill content. Later record,
schema or evidence changes require affected reassessment, not just a hash update.

## Exact reviewed bytes

| Record path | SHA-256 |
|---|---|
| `data/records/dittmarite.yaml` | `cdd67254dea22a44812ebfcf71ebb5aef3db97b77e77f2eb29099ddbb8e9a797` |
| `data/records/glushinskite.yaml` | `5ccb9078ddb4c0c2910d827f1afd426d489c78656aa8c5fa8ebc40b303e11a67` |
| `data/records/lithium-bearing-geothermal-brine.yaml` | `e82a067575e5ea6c26e43962f9478f34fa5c330d0a64e6869bb35e43dcf0b0cf` |

| Other final input | SHA-256 |
|---|---|
| `README.md` | `57dde9b0b70453f121bd1a3f2e251e92007e751f3e65f27c6b3cea9998642919` |
| `.claude/skills/cmmmech-add-record/SKILL.md` | `cdbdc03c1aa9bdfc4088a2df1c01229419f88a58677a01edf07d732855f200c2` |
| `docs/records.md` | `381bbb73b78607fe4729512f0c30e1f0f3cf010344c88104e84d495639f69c9b` |
| `src/cmmmech/schema/cmmmech.yaml` | `f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c` |
| `tests/test_validation.py` | `dc2e9997a923344de42d058a6f4e07440c652a61ae01c1f614f0628af6e34a80` |
| `research/ingests/round15-20261011-publication.md` | `cbe01f7eb12a4df9b57f0413af1d0af6f98fe46e254c0be3bd5d61c6b0f2a188` |
| `research/ingests/round15-frontier-20261011.md` | `9d3e5439e4de4efcb98d26baf85e009e4004d15795fcf42f5a3573cefbe53b7c` |
| `research/ingests/round15-frontier-20261011.json` | `10c94159a6cea99d4b233ff63213786e866b248878e257c8474d98baf6665b87` |
| `research/ingests/round15-mineral-sources-20261011.json` | `d7d23df153075bb76a761577c0c13b94a05628e28c13109723cb7c95ccdf3948` |
| `research/ingests/round15-brine-sources-20261011.json` | `32d445e3696f062dbbf08dc22bf4c5fd10ef7ff5c599064e5e17d3b538544ec4` |
