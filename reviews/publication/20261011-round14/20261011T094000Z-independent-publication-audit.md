# Independent round 14 publication audit

UTC audit timestamp: **2026-10-11T09:42:14Z**. The filename uses the 09:40 UTC time bucket;
this body records the actual completion time. The exact assessment start was not
separately clocked. Reviewer: **Codex /root/round14_publication_adversary (GPT-6)**.
I authored none of this batch's records, histories, source dossiers, or scientific
reviews. This is separation from those authors within the same team, not
organizational independence.

## Reviewed revision and working changes

Repository: `CultureBotAI/CMMMech`.
Worktree: `/private/tmp/CMMMech-expansion-round14-20261011`.
Branch: `curate/cmm-expansion-round14-20261011`.
Trusted base and current HEAD: `8f8abedfce68f932e4f6f333a5470ee5f3897ff4`.
The audited publication is an uncommitted working-tree package, not a claim that
these bytes have already been committed or merged. It comprises 18 new records,
18 CREATE histories and one EDIT, 19 new structured YAML/Markdown review pairs,
source/frontier dossiers, the publication report, README additions, and this audit.
The [publication report](../../../research/ingests/round14-20261011-publication.md)
links every new record and final scientific review.

## Scope and evidence checked

I read the applicable working guide, record contract, structured-review contract
and local review profile, the new publication report and README changes, all four
source dossiers and the frontier reconciliation, all new review identities and
verdicts, and the complete initial/successor FCC finding lineage. I independently
computed record/review hash coverage and prior-file preservation rather than
accepting the advertised counts.

Searches used `rg --files --hidden --no-ignore` and, for scientific-tree inventory,
`--follow`, covering the worktree and named round14 raw directories. Ignored and
hidden files were included. An unnecessarily broad `/private/tmp` inventory was
interrupted after a permission error in an unrelated daemon directory; no absence
or completeness claim relies on that attempt. This audit does not assert
machine-wide absence or exhaustive binary-PDF text coverage.

Primary-source challenge sampling was risk-based, not a new full scientific review
of all 119 records:

- **Hydrocracking catalyst:** read retained original methods and source context,
  visually inspected PDF pages 4 and 9 (filtrate preparation, pH treatment, controls,
  Table 5 loading units and Table 6 lack of fit). The record retains autoclaving,
  control-speed differences, incompatible loading units and the Al lack-of-fit
  limitation instead of adopting the abstract's optimized-yield claim.
- **Pyrolusite:** inspected retained original text and rendered PDF Figure 2/3 page.
  The initial 2.4 mM Fe(II) arm, approximately 0.6 mM aqueous Mn and later mixed
  iron phases support the bounded abiotic description. `microbial: false` is
  explicit; the mixed-ore microbial lead is context only.
- **Commercial products:** checked Albemarle's retained reader transcript for
  monohydrate formula and 55.0% LiOH assay basis, the Pan Chem/Ihumate reader
  evidence for manganese sulfate monohydrate, and SGL brochure excerpts for
  separate graphite anode, composite and additive products. Transcript hashes
  are not represented as original PDF/HTML hashes. The failed Walsun specification
  reacquisition is documented and its numerical table is excluded from records.
  Unseen standards tables are not cited as verified grade requirements.

These are independently read retained artifacts acquired by the curation agents,
not fresh downloads by this auditor. Source limitations, species-versus-strain
scope, laboratory-versus-industrial claims, reuse of one experiment across
material perspectives, measured-versus-modelled outcomes, and constituent versus
resource criticality were challenged. No new criticality designation is asserted
by this batch. Six commodities are identity-only, one mineral has an explicitly
abiotic mechanism, and eleven additions have scoped microbial-origin evidence.

Selected retained primary artifacts and transcripts:

| Artifact | SHA-256 |
|---|---|
| `hydro2026.pdf` | `5dceed6121da4c7b247e760ad90c0e7530d328ab9d313742247c62e19e310d94` |
| `pyrolusite-abiotic.pdf` | `d89993b072ec7eef6060bcb1fa7ecbf62b6ca4928ad3446804c0d80176e569ec` |
| `web-reader-1.txt` | `c241f106b9fdc7754b7cf85914af23a60a7994c1a01b722e00a5767869640300` |
| `manganese-primary-reader.txt` | `5b0e1ab940365f8fabf4c914db102a5120bef6cadd883a6cac771b81f78ead43` |
| `graphite-sgl.pdf` | `42e896b620617284885e047ba143af3a298272b4ddc9ce7a76ef12a50e3fd05c` |

## Findings by severity and corrections

**New findings from this publication audit: 0 blockers, 0 major, 0 minor.**
This is a bounded package verdict, not universal scientific clearance.

One earlier **minor** scientific finding was supported, corrected and explicitly
resolved: [issue #57](https://github.com/CultureBotAI/CMMMech/issues/57), stable key
`round14-fcc-pkmt-growth-temperature`. The original FCC record omitted unequal
culture-growth temperatures from the Pkm/PkmT comparison. The current record
retains the endpoints while stating 30°C Pkm versus 20°C PkmT growth and common
30°C leaching, so it does not isolate a tryptone effect. The actual EDIT sidecar
is linked, the CREATE and initial observation remain immutable, and the
[successor](../../structured/20261011T093831Z-spent-fluid-catalytic-cracking-catalyst-round14-successor/review.yaml)
cites the exact prior review/finding occurrence and corrected target hash. It also
clarifies the original review's imprecise methods locator as Section 2.4, with
Section 3.2 independently supporting the temperatures. The issue remains open
pending publication/closure; resolution of the scientific finding is not claimed
as GitHub closure. No unresolved round14 finding head remains.

No source weakness already correctly qualified was converted into an invented
issue. I made no record, history, scientific-review or governance edits.

## Independent package verification

- **119 records:** 64 elements, 30 commodities, 14 minerals, 11 secondary resources.
- **135 history sidecars** and **132 structured review pairs**; 19 pairs belong to
  this round because the FCC initial observation and successor are both retained.
- **119/119 exact current independent scientific-review coverage.** Each current
  record hash has a completed independent passing or qualified-passing review
  targeting that record. All 18 additions have `pass_with_limitations` final
  reviews. This coverage check supplements the structured checker's declared-scope
  validation; it does not convert structural validity into scientific proof.
- **660 prior tracked scientific-tree files preserved byte-for-byte** against the
  trusted base using `git archive` and direct byte comparison of `data`, `history`,
  `reviews` and `research`. No prior record or review was rewritten.
- All **280 available path/SHA-256 assertions** traversed in round14 JSON dossiers
  matched the corresponding local files. All **119** final gated record hashes
  still match current bytes. These checks include repeated assertions where a
  source appears in multiple dossiers; 280 is not a count of independent sources.
- The historical authority inventory remains 94 candidates: **88 exact roots,
  one designation-specific alias, five deferred grade umbrellas**. The 18 new roots
  lie outside that fixed inventory. Product definitions do not retire universal
  grade questions. The frontier explicitly declines to claim exhaustion.
- README and round14 Markdown relative links were checked; 253 links resolved
  after this audit artifact was written. No raw PDF, binary archive or workbook is
  among the proposed Git-visible additions. A targeted credential-pattern scan of
  those additions found no matches; this is not a whole-machine secret audit.
- Schema, validators, tests, dependencies, workflow and governed files are unchanged.
  Only README is modified among previously tracked paths.

The terminal receipts and logs supplied by the executing root were read. I did
not rerun or claim authorship of those native checks:

| Check | Observed result |
|---|---|
| Final `UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache just check` | Exit 0; 307 passed, 3 skipped; 119 records and 135 histories valid; 100.41 seconds |
| `uv run --locked cmmmech validate --require-records` | Exit 0; 119 checked, 0 failed |
| `uv run --locked cmmmech validate-history --base 8f8abedfce68f932e4f6f333a5470ee5f3897ff4` | Exit 0; 135 histories, 0 errors |
| Corrected FCC named validator | Exit 0; 1 checked, 0 failed, as recorded in the successor |
| `just review-check --require-reviews --base 8f8abedfce68f932e4f6f333a5470ee5f3897ff4` | Root terminal session 48135 exited 0; 132 valid reviews, `declared_scopes_only` |
| `bash scripts/check_vendored_sync.sh` | Root terminal session 69928 exited 0; 22 governed artifacts match the pin |

The final native receipts are `/private/tmp/cmm-round14-gate-receipts.json` and
`/private/tmp/cmm-round14-package-terminal-receipt.json`; logs were read, not
inferred to be successful from running output. My independent measurements are
in `/private/tmp/cmm-round14-publication-adversary-checks.json`. The core results
are retained above so temporary-file availability is not required to understand
the verdict.

## Provenance retention and current governance

All **15 distinct review source revisions** resolve locally. Fourteen are in the
trusted main ancestry. The remaining revision,
`c0adc2c0763e1515ed07dc712b024974d98fb342`, is retained by annotated tag
`review-base/cmm-source-survey-20261009`. Independent remote `git ls-remote`
verification returned tag object `fc4040c3abcd28f0a9cc52467e308100144ad1fd` and that
exact peeled commit. Remote main was the trusted base at inspection. No new
round14 review base depends on the soon-to-be-deleted topic branch.

A live read of GitHub ruleset **24692449** confirmed active enforcement, native
**SQUASH** merge queue with **ALLGREEN** grouping, required `validate-strict`
from integration **15368**, and no bypass actors. Local CLAW pin remains
`a5d562962c75a2ad9efd8160b548df5944315422`; the synchronization receipt verifies
all 22 governed files. Existing fleet admission/history integration is preserved.
The checked PR-shepherd workflow is manual and comment-only; deterministic queue
admission is separate. Future integration follows CLAW's supported process.

## Unresolved questions and verdict

**Pass with limitations for publication of the inspected package.** Scientific
source conflicts and five unresolved grade umbrellas remain openly described.
The package supplies concrete next-source leads; global material discovery is
still open.

At this audit timestamp, commit/push, PR CI, isolated squash-shaped verification,
queue admission, actual merge, branch deletion, fresh remote-main verification,
and original-checkout ignored/untracked preservation are not claimed complete.
The root must record their actual results in the PR completion receipt. Review
bases and the retained tag must survive those steps. Any later record or evidence
change requires affected reassessment; this audit does not silently cover new bytes.

## Exact reviewed working-state hashes

The following eighteen SHA-256 values identify the new record bytes. Full current
record inventory is retained in the linked frontier JSON.

| Record ID | SHA-256 |
|---|---|
| `cmmmech:scheelite` | `a8fd85cedb9100cb6a3b1ec8e5bafe5be2d5a4fe1ea740abf33acee44a1c7425` |
| `cmmmech:pyromorphite` | `87973d0a231986d00bf9883c4c6f941657b8abfd9d83ee418d61ac7d8faf88e5` |
| `cmmmech:struvite` | `02d68b2c3524462ac21f614c70ded7263156f713481c732264b9849567f6e945` |
| `cmmmech:ferrihydrite` | `2de9e5fdbd96b7d9ec8b74c7b09ffd04951e1351288c88a37872fd4a0c22791c` |
| `cmmmech:magnetite` | `d2781c4c48ee85c9bea32e3caaa2795ee362a0b3c69108d1c925428df8203020` |
| `cmmmech:pyrolusite` | `47ce73b2f3c987208bee82bbd91109870d1866a90fbc580172f1907269f44831` |
| `cmmmech:lithium-carbonate` | `78c7773d6bf0764a6bbb51bf4fa50f6468638ba1312d5f93ba324d6c6b99c2f5` |
| `cmmmech:lithium-hydroxide-monohydrate` | `682207c7f5d201d066b3a79c7d64c49360f867500c9ce4ca162f1a236acd1c49` |
| `cmmmech:nickel-sulfate-hexahydrate` | `468df9c5da237f38f0263ce32bb06275e7572999d73387a96456d9892a053c9d` |
| `cmmmech:manganese-sulfate-monohydrate` | `22a095812cd5f0add14f5c2007f47defd68ea263334690ecc946784da3e9f2dc` |
| `cmmmech:ferroboron` | `3b9d4fa94eee8f3f6b443e7d73af93d2dafaa58e7e2f1b58621c6afb1611df0d` |
| `cmmmech:graphite-anode-material` | `608c23661e1f2b5cbffef9cd391b9c7ecc36d20815533f8dcb34c2b17b4afe1b` |
| `cmmmech:spent-fluid-catalytic-cracking-catalyst` | `1fdf0137fd53339f7acd6b1b87d9537ddcb911255e91834bf8dc0c1471796401` |
| `cmmmech:coal-fly-ash` | `cf34e4290d857ff173b845ab1ea3e77a37c54c289e5326bf40cb015110b2901d` |
| `cmmmech:municipal-waste-incineration-ash` | `3677ebff576d161d1ad015d57f7ca27c810a17bc81a4166feb7efbdf8d154d52` |
| `cmmmech:sewage-sludge-incineration-ash` | `2c63142c818ba0e3309df50b45f614b0a6ff2c0d39e370a9e0651d3b5d999a0a` |
| `cmmmech:spent-hydrocracking-catalyst` | `8bb94dfd26a8e4ad935a3337314ca4d7b96dbb50f857d8ca7405140b7df82e95` |
| `cmmmech:spent-ndfeb-magnets` | `9a55438ef82ebcb1a7568878377e0ccb9c5762e2370f154b2c76902ad8c34697` |

Publication inputs at final assessment:

| Path | SHA-256 |
|---|---|
| `README.md` | `c990b4003b182d08ebeebbb08592bb859a4be9be08ec18f726c7ae5b7067c5f2` |
| `research/ingests/round14-20261011-publication.md` | `bad568c6c068a5b48ed15d521b8da5c0eb8d41682c796e4faec9f260f4e76fd8` |
| `research/ingests/round14-frontier-20261011.json` | `2760d7b7b5595ebac7fa587d1f9d7828287860eabef4ae31b45743a402fbd3da` |
| `research/ingests/round14-magnet-source-20261011.json` | `cdcfce1cb9340b23b9a276b55addfacde8decc9bdb85d8471024bb0b8294f1e9` |
| `research/ingests/round14-mineral-sources-20261011.json` | `09808fc24ed1e022c5412e73257987a586ffa4728b40b03b9e740fc92e025d46` |
| `research/ingests/round14-product-boundaries-20261011.json` | `52bcd20b6f1ff6a4ea1c83b05c14b9cf7a74713bea06fd7bc9fa2e45d5bc4a2a` |
| `research/ingests/round14-secondary-sources-20261011.json` | `946e3c44bc55371cf8f623fbbe85ace38a8c48162be4ed55a04a9a0973eabd36` |
