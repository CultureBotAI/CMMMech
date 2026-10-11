# Independent round 13 publication audit

Verdict: **pass with stated scientific and publication limits**. No unresolved blocker, major or minor publication finding remains in the inspected package.

Audit timestamp (UTC): 2026-10-11T09:14:34.239104+00:00.

Reviewer: Codex agent `/root/round13_publication_adversary`, GPT-6, codex. This agent authored none of the eight records, histories, source dossiers, per-record reviews or publication report. It inspected the package, scientific spot checks and live read-only publication configuration; it made no record, Git or GitHub mutation.

Worktree: `/private/tmp/CMMMech-expansion-round13-20261011`; branch `curate/cmm-expansion-round13-20261011`; trusted base `14ceff0da3e19d6d36426d33f4cf577b8e64760f`. The scope is eight records (pentlandite, jadarite, spodumene, colemanite, battery-black-mass, bauxite-residue, phosphogypsum and metallurgical-coal), their CREATE histories, README, three cohort dossiers, the dated frontier, saved scientific reviews, and publication documentation. This is a bounded independent publication audit with scientific spot checks, not a replacement for the complete per-record observations.

The reviewed working changes comprise 42 paths before adding this report: eight records, eight CREATE histories, nine research/frontier/publication files, 16 files forming eight review pairs, and README. The exact sorted file/hash manifest has SHA-256 `b11ebe99dcc73a5fd8ff409131692c55fc976f74051dc4e1ba92e3c1f3c51c33`. It is reproducible by serializing a path-sorted list of objects with `path` and `sha256` keys using `json.dumps(manifest, sort_keys=True, separators=(',', ':')).encode()` and hashing the result. The separate audit is the 43rd path. This is an attestation of uncommitted working bytes against the trusted base, not a claim that a topic commit already exists. The full external receipt is `/private/tmp/cmm-round13-adversary-package-manifest.json`.

The [publication report](../../../research/ingests/round13-20261011-publication.md) links every exact-state YAML/Markdown scientific observation.

## Evidence checked

All eight records were read against the repository contract and local skills. Mineral species, elements, commodity families and heterogeneous resource streams remain distinct. No new criticality designation is inherited from a constituent element, ore or narrower coal category. Seven records have scoped microbial evidence; metallurgical coal has identity evidence only. Reused experiments are not counted as independent replications.

- The [September 2026 IMA list](https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf)'s exact rows on PDF pages 48, 103, 168 and 203 confirm colemanite, jadarite, pentlandite and spodumene formulas and status. Grandfathering dates and the special-procedure entry are distinguished from sequential approval identifiers.
- [Sun 2020](https://doi.org/10.3390/min10030289) Methods 2.1–2.3 and the pH-stat/ferric-assay distinction support the pentlandite scope. One 8-day and one 16-day run cannot establish independent replication at the terminal 16-day endpoint. Surface assignments and community profiles do not identify unique causal enzymes or responsible community members. The record retains those limits.
- [Kirk's version 1 source workbooks](https://doi.org/10.17632/djkf7tkm8d.1) were independently inspected through their actual XLSX sheet XML. Jadarite F5 and F7 differ from arithmetic means of the labelled C:E replicates; the spodumene and lepidolite C3:E12 blocks contain the same 30 Li values. The source loading and unit discrepancies prevent a reliable normalized-yield comparison. The records preserve qualitative transient/null outcomes without silently repairing deposited data.
- The colemanite record, checked against [Bayat 2011](https://www.scielo.cl/pdf/ejb/v14n3/a07.pdf), retains the already documented nonclosing 126.8 wt% source composition, protocol inconsistencies and missing corresponding abiotic boron series. The reported B2O3 cell is not promoted to a valid recovery denominator. The mineral record is not an independent replication of the borates study.
- [Lalropuia 2024](https://doi.org/10.3389/fmicb.2024.1347072) PDF Methods 2.5–2.6, Tables 1–2 and visually inspected Figure 5 support the black-mass observation and withheld complete-recovery claim. At 1% w/v feed, the stated 145 g Co/kg implies 1.45 g/L Co inventory, while adapted-Co bars are near 2 g/L. Adaptation amounts and unmatched pH/iron chemistry are additional retained limits. No corrected mass balance or isolated product is claimed.
- The red-mud record, checked against [Urik 2015](https://doi.org/10.1016/j.jinorgbio.2015.08.022) in the retained official thesis copy, keeps the source-defined Ajka feed, unresolved aluminium host phases and unlike synthetic-acid controls. Its filtered aluminium endpoint is a mobilization measurement, not recovered aluminium metal or alumina.
- [Antonick's OSTI manuscript](https://www.osti.gov/servlets/purl/1862749) Methods 2.1–2.4 and visually inspected Table 2 support separate synthetic single-REE models, the 20 mg/mL loading and distinct equal-pH/equal-molarity comparisons. Ce concentration and dissolved-fraction order reverse between the organic lixiviants; Table 2 errors are 95% confidence intervals from triplicates. These are not universal industrial-feed or whole-process recovery results.
- [Zhang 2025](https://doi.org/10.3390/molecules30030674) and visually inspected Figure 7 retain a micrograms/kg axis against micrograms/L in the text and a plotted maximum around day 24 against the approximately day-21 conclusion. Liquid/solid accounting and feed inventory do not establish the reported 24.67% denominator. The record keeps qualitative culture-associated release and declines unverifiable yield or matched microbial-advantage claims.
- The live [EIA glossary](https://www.eia.gov/tools/glossary/index.php?id=Metallurgical+coal) and [IEA Coal 2020 Annex](https://www.iea.org/reports/coal-2020/annex) corroborate the broader metallurgical-coal family, while the retained USGS 2026 fact sheet uses a narrower coke-making scope. Explicit overlap with coking coal and source-dependent anthracite treatment make this an overlapping family, not a duplicate disjoint identity.

Source acquisition failures, reused copies, missing supplements, version dates and raw-file reuse limitations remain visible in the dossiers. Independent live opening of the MDPI pentlandite page returned an error and the PMC phosphogypsum page returned a browser challenge; retained publisher PDF/primary article artifacts were used for those checks. The live EIA and IEA pages were readable. No raw full text or workbook is added to the publication package.

## Frontier and preservation

Bounded identity searches used `rg --no-ignore --hidden --follow` over data/records, research, reviews and history. Those roots contain no symlinks. Binary PDFs and selected figure pixels/XLSX cells were inspected separately. These are bounded local searches, not machine-wide or literature-wide absence assertions.

The historical authority inventory remains exactly 94 candidate roots. Independent set comparison with actual record slugs gives 88 exact represented roots, one designation-specific phosphate alias and five deferred grade proposals. The corpus contains 101 records: 64 elements, 24 commodities, eight minerals and five secondary resources. Seven new mineral/resource roots lie outside that historical authority inventory. Record totals are not disjoint material counts or independent-experiment totals.

Independent byte comparisons confirmed all 618 prior tracked paths under data, history, reviews and research are unchanged from the trusted base. Recursive checks verified 210 referenced dossier/frontier/raw-artifact hashes with no mismatch or missing hashed file. README has 101 distinct record rows, all resolving to actual records. All 191 relative links inspected across README and the five new Markdown research/publication reports resolve. The frontier explicitly leaves the wider goal active and identifies mineral, resource, grade-specification and primary-literature priorities.

## Exact-state scientific coverage

Independently inspected all 113 saved pairs and matched maintained target ID, path, declared reviewed scope and current target SHA. All 101 corpus records have current completed scientific coverage. The eight new pairs are completed, independent, `pass_with_limitations` and contain no findings. Every new review input hash matches its actual file. Independence is disclosed record-author separation within a shared agent/model workspace, not institutional independence.

| Record ID and path | Final scientific observation |
|---|---|
| [cmmmech:pentlandite](../../../data/records/pentlandite.yaml) | `20261011T091034Z-pentlandite-round13-independent` |
| [cmmmech:jadarite](../../../data/records/jadarite.yaml) | `20261011T091034Z-jadarite-round13-independent` |
| [cmmmech:spodumene](../../../data/records/spodumene.yaml) | `20261011T091034Z-spodumene-round13-independent` |
| [cmmmech:colemanite](../../../data/records/colemanite.yaml) | `20261011T091034Z-colemanite-round13-independent` |
| [cmmmech:battery-black-mass](../../../data/records/battery-black-mass.yaml) | `20261011T090808Z-battery-black-mass-round13-independent` |
| [cmmmech:bauxite-residue](../../../data/records/bauxite-residue.yaml) | `20261011T090808Z-bauxite-residue-round13-independent` |
| [cmmmech:phosphogypsum](../../../data/records/phosphogypsum.yaml) | `20261011T090808Z-phosphogypsum-round13-independent` |
| [cmmmech:metallurgical-coal](../../../data/records/metallurgical-coal.yaml) | `20261011T090808Z-metallurgical-coal-round13-independent` |

## Findings and corrections

No supported new blocker, major or minor scientific/publication defect was identified in the inspected record scope. Preserved source inconsistencies are explicitly limited scientific claims rather than hidden acceptance failures. No corrective record edit or invented review issue was needed for this audit.

## Unresolved scientific questions

Five qualified grade umbrellas remain deferred for complete product specifications and defensible list mapping. Mineral phase characterization, missing supplements, revised datasets, quantitative source denominators and matched controls remain concrete research priorities. The accepted scope does not certify inaccessible supplements, all literature, whole-process recovery or industrial deployment. No further correction is required to preserve those limits in this publication package.

## Validation and publication boundary

Root's actual logs and terminal command receipts were inspected: `just check` exited 0 with 307 passed and 3 skipped in 76.91 s, 101 records/0 failed, and 116 histories/0 errors; required-record validation and trusted-base history validation each exited 0. This auditor did not repeat the full tests. Root's final structured-check terminal receipt separately confirms exit 0 and 113 valid review pairs; governed synchronization confirms all 22 artifacts match the pinned CLAW revision. This auditor independently performed coverage, source, byte-preservation, hash, link and live-ref/ruleset checks; it inspected root's terminal gate receipts instead of claiming to have run those gates. Structural gates are not used as scientific proof.

All 14 distinct review bases were enumerated. Thirteen are ancestors of, or equal to, the trusted main base; the remaining source-survey base has the retained annotated tag below. None of the new reviews relies on a disposable topic-only revision.

Live read-only checks independently confirmed remote main at the trusted base and ruleset 24692449 active: SQUASH/ALLGREEN queue, required `validate-strict` from integration 15368 and no bypass actors. The annotated `review-base/cmm-source-survey-20261009` tag still has object `fc4040c3abcd28f0a9cc52467e308100144ad1fd` and peels to `c0adc2c0763e1515ed07dc712b024974d98fb342`. An initial sandbox DNS failure was resolved by authorized read-only network escalation; no publication check was bypassed.

Commit, push, PR, squash-shaped verification, queue admission, actual merge, branch deletion and fresh remote-main validation remain root-owned publication steps. This pre-publication observation does not assert that they have occurred. Fetch tags explicitly and retain all source revisions. No global new-material or source-exhaustion claim is supported.
