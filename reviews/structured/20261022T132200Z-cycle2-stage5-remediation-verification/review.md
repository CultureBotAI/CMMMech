# Cycle 2 Stage 5 Post-Remediation Verification Review: 33 Remediated CMMMech Records

- Review: 20261022T132200Z-cycle2-stage5-remediation-verification
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-22T13:20:00Z
- Finished UTC: 2026-10-22T13:22:00Z
- Reviewer: antigravity / cmmmech-cycle2-stage5-remediation-reviewer (self_review)
- Completion: completed
- Verdict: pass
- Scientific review: true

## Summary

Post-remediation scientific and structural verification of all 33 CMMMech records remediated in Cycle 2 Stage 5 (run mech-goal-sequence-20261019, cycle 2, stage 5) across GitHub issues #817 (GRP-C2S5-001: cmmmech-cycle2-stage4-finding-0001, 30 mineral records normalized from ima2026/ima202609/ima_202609 to canonical ima_2026_09), #818 (GRP-C2S5-002: cmmmech-cycle2-stage4-finding-0002, causal-graph node protein_examples evidence explanations synchronized with mechanism protein_examples in allanite-concentrate and thulium), and #819 (GRP-C2S5-003: cmmmech-cycle2-stage4-finding-0003, dissolution edge predicate updated from chelates to solubilizes in katsarosite). All 3 carried-forward Cycle 2 Stage 4 findings are verified as resolved with append-only EDIT history sidecars.

## Scope And Provenance

All 33 CMMMech records affected by the 3 Cycle 2 Stage 4 findings carried into Stage 5 (30 mineral records in GRP-C2S5-001 / #817, 2 records in GRP-C2S5-002 / #818, and 1 mineral record in GRP-C2S5-003 / #819).

Selection: cycle2_stage4_open_finding_targets
Coverage: full; 33 reviewed / 33 in the declared population.
Source: working_tree at Git base e16fd0f59192b2bbc20e9baa943fb67085950171.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:alicewilsonite-yce | data/records/alicewilsonite-yce.yaml | maintained | Alicewilsonite-(YCe) |
| cmmmech:alicewilsonite-yla | data/records/alicewilsonite-yla.yaml | maintained | Alicewilsonite-(YLa) |
| cmmmech:allanite-concentrate | data/records/allanite-concentrate.yaml | maintained | Allanite concentrate |
| cmmmech:ancylite-ce | data/records/ancylite-ce.yaml | maintained | Ancylite-(Ce) |
| cmmmech:azurite | data/records/azurite.yaml | maintained | Azurite |
| cmmmech:bainbridgeite-yce | data/records/bainbridgeite-yce.yaml | maintained | Bainbridgeite-(YCe) |
| cmmmech:brucite | data/records/brucite.yaml | maintained | Brucite |
| cmmmech:burbankite | data/records/burbankite.yaml | maintained | Burbankite |
| cmmmech:calcioancylite-la | data/records/calcioancylite-la.yaml | maintained | Calcioancylite-(La) |
| cmmmech:calcioburbankite | data/records/calcioburbankite.yaml | maintained | Calcioburbankite |
| cmmmech:caysichite-y | data/records/caysichite-y.yaml | maintained | Caysichite-(Y) |
| cmmmech:cerianite-ce | data/records/cerianite-ce.yaml | maintained | Cerianite-(Ce) |
| cmmmech:cordylite-ce | data/records/cordylite-ce.yaml | maintained | Cordylite-(Ce) |
| cmmmech:dolomite | data/records/dolomite.yaml | maintained | Dolomite |
| cmmmech:donnayite-y | data/records/donnayite-y.yaml | maintained | Donnayite-(Y) |
| cmmmech:greenockite | data/records/greenockite.yaml | maintained | Greenockite |
| cmmmech:gysinite-nd | data/records/gysinite-nd.yaml | maintained | Gysinite-(Nd) |
| cmmmech:hawleyite | data/records/hawleyite.yaml | maintained | Hawleyite |
| cmmmech:hydrotalcite | data/records/hydrotalcite.yaml | maintained | Hydrotalcite |
| cmmmech:ilmenite | data/records/ilmenite.yaml | maintained | Ilmenite |
| cmmmech:katsarosite | data/records/katsarosite.yaml | maintained | Katsarosite |
| cmmmech:kukharenkoite-ce | data/records/kukharenkoite-ce.yaml | maintained | Kukharenkoite-(Ce) |
| cmmmech:kuliokite-y | data/records/kuliokite-y.yaml | maintained | Kuliokite-(Y) |
| cmmmech:lorenzenite | data/records/lorenzenite.yaml | maintained | Lorenzenite |
| cmmmech:millerite | data/records/millerite.yaml | maintained | Millerite |
| cmmmech:perovskite | data/records/perovskite.yaml | maintained | Perovskite |
| cmmmech:polydymite | data/records/polydymite.yaml | maintained | Polydymite |
| cmmmech:pyroaurite | data/records/pyroaurite.yaml | maintained | Pyroaurite |
| cmmmech:synchysite-ce | data/records/synchysite-ce.yaml | maintained | Synchysite-(Ce) |
| cmmmech:tenorite | data/records/tenorite.yaml | maintained | Tenorite |
| cmmmech:thulium | data/records/thulium.yaml | maintained | Thulium |
| cmmmech:titanite | data/records/titanite.yaml | maintained | Titanite |
| cmmmech:vaesite | data/records/vaesite.yaml | maintained | Vaesite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Schema and semantic record validation | passed | True | cmmmech:alicewilsonite-yce, cmmmech:alicewilsonite-yla, cmmmech:allanite-concentrate, cmmmech:ancylite-ce, cmmmech:azurite, cmmmech:bainbridgeite-yce, cmmmech:brucite, cmmmech:burbankite, cmmmech:calcioancylite-la, cmmmech:calcioburbankite, cmmmech:caysichite-y, cmmmech:cerianite-ce, cmmmech:cordylite-ce, cmmmech:dolomite, cmmmech:donnayite-y, cmmmech:greenockite, cmmmech:gysinite-nd, cmmmech:hawleyite, cmmmech:hydrotalcite, cmmmech:ilmenite, cmmmech:katsarosite, cmmmech:kukharenkoite-ce, cmmmech:kuliokite-y, cmmmech:lorenzenite, cmmmech:millerite, cmmmech:perovskite, cmmmech:polydymite, cmmmech:pyroaurite, cmmmech:synchysite-ce, cmmmech:tenorite, cmmmech:thulium, cmmmech:titanite, cmmmech:vaesite | All 631 records (including all 33 remediated records) pass .venv/bin/python -m cmmmech validate --require-records with 0 errors and 0 warnings. |
| Append-only history sidecar validation | passed | True | cmmmech:alicewilsonite-yce, cmmmech:alicewilsonite-yla, cmmmech:allanite-concentrate, cmmmech:ancylite-ce, cmmmech:azurite, cmmmech:bainbridgeite-yce, cmmmech:brucite, cmmmech:burbankite, cmmmech:calcioancylite-la, cmmmech:calcioburbankite, cmmmech:caysichite-y, cmmmech:cerianite-ce, cmmmech:cordylite-ce, cmmmech:dolomite, cmmmech:donnayite-y, cmmmech:greenockite, cmmmech:gysinite-nd, cmmmech:hawleyite, cmmmech:hydrotalcite, cmmmech:ilmenite, cmmmech:katsarosite, cmmmech:kukharenkoite-ce, cmmmech:kuliokite-y, cmmmech:lorenzenite, cmmmech:millerite, cmmmech:perovskite, cmmmech:polydymite, cmmmech:pyroaurite, cmmmech:synchysite-ce, cmmmech:tenorite, cmmmech:thulium, cmmmech:titanite, cmmmech:vaesite | All 33 new EDIT history sidecars and existing history sidecars pass .venv/bin/python -m cmmmech validate-history --base origin/main. |
| Canonical ima_2026_09 source key across all 30 remediated mineral records | passed | True | cmmmech:alicewilsonite-yce, cmmmech:alicewilsonite-yla, cmmmech:ancylite-ce, cmmmech:azurite, cmmmech:bainbridgeite-yce, cmmmech:brucite, cmmmech:burbankite, cmmmech:calcioancylite-la, cmmmech:calcioburbankite, cmmmech:caysichite-y, cmmmech:cerianite-ce, cmmmech:cordylite-ce, cmmmech:dolomite, cmmmech:donnayite-y, cmmmech:greenockite, cmmmech:gysinite-nd, cmmmech:hawleyite, cmmmech:hydrotalcite, cmmmech:ilmenite, cmmmech:kukharenkoite-ce, cmmmech:kuliokite-y, cmmmech:lorenzenite, cmmmech:millerite, cmmmech:perovskite, cmmmech:polydymite, cmmmech:pyroaurite, cmmmech:synchysite-ce, cmmmech:tenorite, cmmmech:titanite, cmmmech:vaesite | All 30 mineral records in GRP-C2S5-001 (#817) now key the September 2026 IMA-CNMNC Master List under canonical ima_2026_09, achieving 100% (380/380) uniformity across all mineral records in CMMMech. |
| Causal-graph protein_examples evidence parity (#818) and dissolution predicate alignment (#819) | passed | True | cmmmech:allanite-concentrate, cmmmech:katsarosite, cmmmech:thulium | allanite-concentrate (UniProtKB:Q5FT13, UniProtKB:Q5FTI1) and thulium (UniProtKB:O34952, UniProtKB:Q797B3, UniProtKB:P54496, UniProtKB:O32206) have identical evidence[].explanation strings between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples, and katsarosite uses predicate: solubilizes on its secreted_organic_acids -&gt; znso4_hopeite_culture_substrate dissolution edge. |

## Scientific And Domain Assessments

### Canonical ima_2026_09 source key across 30 mineral records (#817)

consistency: supported. Targets: cmmmech:alicewilsonite-yce, cmmmech:alicewilsonite-yla, cmmmech:ancylite-ce, cmmmech:azurite, cmmmech:bainbridgeite-yce, cmmmech:brucite, cmmmech:burbankite, cmmmech:calcioancylite-la, cmmmech:calcioburbankite, cmmmech:caysichite-y, cmmmech:cerianite-ce, cmmmech:cordylite-ce, cmmmech:dolomite, cmmmech:donnayite-y, cmmmech:greenockite, cmmmech:gysinite-nd, cmmmech:hawleyite, cmmmech:hydrotalcite, cmmmech:ilmenite, cmmmech:kukharenkoite-ce, cmmmech:kuliokite-y, cmmmech:lorenzenite, cmmmech:millerite, cmmmech:perovskite, cmmmech:polydymite, cmmmech:pyroaurite, cmmmech:synchysite-ce, cmmmech:tenorite, cmmmech:titanite, cmmmech:vaesite.

All 30 mineral records previously using ima2026 (14), ima202609 (9), or ima_202609 (7) now use canonical ima_2026_09.

### Parity of protein_examples evidence explanations between mechanisms and causal_graphs (#818)

consistency: supported. Targets: cmmmech:allanite-concentrate, cmmmech:thulium.

Both allanite-concentrate (UniProtKB:Q5FT13, UniProtKB:Q5FTI1) and thulium (UniProtKB:O34952, UniProtKB:Q797B3, UniProtKB:P54496, UniProtKB:O32206) now carry identical full evidence[].explanation strings on causal_graphs[].nodes[].protein_examples and mechanisms[].protein_examples.

### Dissolution edge predicate solubilizes on katsarosite causal graph (#819)

consistency: supported. Targets: cmmmech:katsarosite.

data/records/katsarosite.yaml (niger_associated_zinc_oxalate_formation_graph) now uses predicate: solubilizes on its secreted_organic_acids -&gt; znso4_hopeite_culture_substrate dissolution edge, matching the sibling Aspergillus niger oxalate biomineralization cohort.

## Findings

### cmmmech-cycle2-stage4-finding-0001: 30 mineral records now use canonical ima_2026_09 source key for the September 2026 IMA Master List

minor / resolved / confirmed; issue key: cmmmech.mineral.noncanonical-ima-master-list-source-ids.

Normalized sources[].id from ima2026 (14 records), ima202609 (9 records), and ima_202609 (7 records) to canonical ima_2026_09 across all 30 mineral records and recorded 30 append-only EDIT history sidecars.

Disposition: Resolved under GitHub issue #817 (group GRP-C2S5-001) by normalizing sources[].id to ima_2026_09 with append-only EDIT history sidecars on all 30 records.

### cmmmech-cycle2-stage4-finding-0002: allanite-concentrate and thulium causal-graph node protein_examples evidence explanations now match mechanisms[].protein_examples

minor / resolved / confirmed; issue key: cmmmech.protein_examples.mechanism-node-evidence-explanation-drift.

Synchronized causal_graphs[].nodes[].protein_examples[].evidence[].explanation with mechanisms[].protein_examples[].evidence[].explanation for UniProtKB:Q5FT13 and UniProtKB:Q5FTI1 in allanite-concentrate.yaml and UniProtKB:O34952, UniProtKB:Q797B3, UniProtKB:P54496, and UniProtKB:O32206 in thulium.yaml with append-only EDIT history sidecars.

Disposition: Resolved under GitHub issue #818 (group GRP-C2S5-002) via scripts/curate_causal_graphs.py with append-only EDIT history sidecars on both records.

### cmmmech-cycle2-stage4-finding-0003: katsarosite causal graph now uses predicate: solubilizes on its substrate dissolution edge

minor / resolved / confirmed; issue key: cmmmech.katsarosite.legacy-chelates-predicate-on-hopeite-solubilization.

Updated predicate: chelates to predicate: solubilizes on the secreted_organic_acids -&gt; znso4_hopeite_culture_substrate edge in data/records/katsarosite.yaml (niger_associated_zinc_oxalate_formation_graph) with an append-only EDIT history sidecar.

Disposition: Resolved under GitHub issue #819 (group GRP-C2S5-003) via scripts/curate_causal_graphs.py with an append-only EDIT history sidecar.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: cmmmech:alicewilsonite-yce, cmmmech:alicewilsonite-yla, cmmmech:allanite-concentrate, cmmmech:ancylite-ce, cmmmech:azurite, cmmmech:bainbridgeite-yce, cmmmech:brucite, cmmmech:burbankite, cmmmech:calcioancylite-la, cmmmech:calcioburbankite, cmmmech:caysichite-y, cmmmech:cerianite-ce, cmmmech:cordylite-ce, cmmmech:dolomite, cmmmech:donnayite-y, cmmmech:greenockite, cmmmech:gysinite-nd, cmmmech:hawleyite, cmmmech:hydrotalcite, cmmmech:ilmenite, cmmmech:katsarosite, cmmmech:kukharenkoite-ce, cmmmech:kuliokite-y, cmmmech:lorenzenite, cmmmech:millerite, cmmmech:perovskite, cmmmech:polydymite, cmmmech:pyroaurite, cmmmech:synchysite-ce, cmmmech:tenorite, cmmmech:thulium, cmmmech:titanite, cmmmech:vaesite. All 33 remediated records represent distinct mineral species (31 records), elements (1 record: thulium), or primary resources (1 record: allanite-concentrate) with disjoint identifiers and provenance; cohort boundaries from Cycle 2 Stage 4 are retained unchanged.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-ima-2026-09 | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; IMA-CNMNC List of Mineral Names (September 2026) | supports | Official IMA-CNMNC Master List (September 2026) cited across all 380 mineral records under canonical source key ima_2026_09. |
| ev-cycle2-stage4-findings | reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-04/revision-0001/review_findings.yaml; findings[0..2] | supports | Frozen Cycle 2 Stage 4 review findings ledger defining cmmmech-cycle2-stage4-finding-0001, cmmmech-cycle2-stage4-finding-0002, and cmmmech-cycle2-stage4-finding-0003 across the 33 target records. |
| ev-schema | src/cmmmech/schema/cmmmech.yaml; classes.CriticalMineralRecord, enums.CausalPredicateEnum | supports | Canonical LinkML schema defining CriticalMineralRecord, ProteinExample, and CausalPredicateEnum (including solubilizes). |

## Limits And Additional Notes

- This verification review is scoped to the 33 records remediated in Cycle 2 Stage 5; the remaining 598 records were verified with 0 open findings in the immutable Cycle 2 Stage 4 review bundles.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T132200Z-cycle2-stage5-remediation-verification
title: 'Cycle 2 Stage 5 Post-Remediation Verification Review: 33 Remediated CMMMech
  Records'
repository: CultureBotAI/CMMMech
kind: category
started_at: '2026-10-22T13:20:00Z'
finished_at: '2026-10-22T13:22:00Z'
skill: .claude/skills/review-yaml-category/SKILL.md
completion: completed
verdict: pass
scientific_review: true
summary: 'Post-remediation scientific and structural verification of all 33 CMMMech
  records remediated in Cycle 2 Stage 5 (run mech-goal-sequence-20261019, cycle 2,
  stage 5) across GitHub issues #817 (GRP-C2S5-001: cmmmech-cycle2-stage4-finding-0001,
  30 mineral records normalized from ima2026/ima202609/ima_202609 to canonical ima_2026_09),
  #818 (GRP-C2S5-002: cmmmech-cycle2-stage4-finding-0002, causal-graph node protein_examples
  evidence explanations synchronized with mechanism protein_examples in allanite-concentrate
  and thulium), and #819 (GRP-C2S5-003: cmmmech-cycle2-stage4-finding-0003, dissolution
  edge predicate updated from chelates to solubilizes in katsarosite). All 3 carried-forward
  Cycle 2 Stage 4 findings are verified as resolved with append-only EDIT history
  sidecars.'
reviewer:
  identity: antigravity / cmmmech-cycle2-stage5-remediation-reviewer
  kind: agent
  independence: self_review
  independence_basis: Cycle 2 Stage 5 post-remediation verification review (.claude/skills/review-yaml-category/SKILL.md)
    of the 33 remediated records against the immutable Cycle 2 Stage 4 review bundles.
  model: claude-opus-4-6
source:
  git_revision: e16fd0f59192b2bbc20e9baa943fb67085950171
  state: working_tree
  inputs:
  - path: data/records/alicewilsonite-yce.yaml
    sha256: a7f9126688bb2e2af56d6fa2ea18924c66ee48332a0b671063f5b60a993cac71
    role: target
  - path: data/records/alicewilsonite-yla.yaml
    sha256: f183f98843ba2a5e2a80b284a3e2b6bff9c26508306742d260bc6f2140b9d399
    role: target
  - path: data/records/allanite-concentrate.yaml
    sha256: 7c463c39890290cf837fc3677c078cfbc1f9c6c5acb415ecad2eb83842bf029c
    role: target
  - path: data/records/ancylite-ce.yaml
    sha256: 24f1f7a4773025ce26cf266f129f160418eca01a774b6f5cbbb8483e1db7e45f
    role: target
  - path: data/records/azurite.yaml
    sha256: 35c6bcb553d588c0c0d1a495e033af3b727701f817428517ecbee85ce942530d
    role: target
  - path: data/records/bainbridgeite-yce.yaml
    sha256: 8b24d2a4bb879b83596afbbee0d573543a90c5350c25ebabf5c669d9d89f4853
    role: target
  - path: data/records/brucite.yaml
    sha256: 0c7cb57a9010418b09cfc4e6c519f3eb463e254d1c226376d856c7484d4fda88
    role: target
  - path: data/records/burbankite.yaml
    sha256: 31566556e071a04453a56136cfb7646a8fbbc534d3c4432c7261653cf616e147
    role: target
  - path: data/records/calcioancylite-la.yaml
    sha256: ff97583841381fa47f6e2ffcef9dcd764aa63242a52119f33b4eb0014b1b6bff
    role: target
  - path: data/records/calcioburbankite.yaml
    sha256: 1363b6854e85852e33a19976dcc81befbed74634ecf2792c7a8b712c59ebab75
    role: target
  - path: data/records/caysichite-y.yaml
    sha256: 4b42b2d84149a4593eabdf737902cc5da218ed105c88fced2a6abdf09e3e8d25
    role: target
  - path: data/records/cerianite-ce.yaml
    sha256: a35f7c93c7e699c5b1ea542765e357e8eb92f305fbbb5abb7dcb13637c6ce7b8
    role: target
  - path: data/records/cordylite-ce.yaml
    sha256: 3c56646d4465371827f38abbc30840295bcaec580037579c9ec8e40da7ff868f
    role: target
  - path: data/records/dolomite.yaml
    sha256: ed967c3edf5d1339e4062a6ea8f35dc51b86d111ebbb75a1c2bd1a5820668c5f
    role: target
  - path: data/records/donnayite-y.yaml
    sha256: febbc17fa3c5b648cb55b7a10070716aa896bae1b7ee8affe643545ba5860339
    role: target
  - path: data/records/greenockite.yaml
    sha256: 0b09b3537e9d8ede0a17972cd9b689a161dcfa7d6fd52dff02584f58972da349
    role: target
  - path: data/records/gysinite-nd.yaml
    sha256: 83cba20f5c33ae0b958a557e386cf94788d2f782945f9d467121ef904027a8d9
    role: target
  - path: data/records/hawleyite.yaml
    sha256: 01e3418f24cf42feed7665f84fb93e4fa45a9f619b4f35373116e233cbc8f5dd
    role: target
  - path: data/records/hydrotalcite.yaml
    sha256: de5f9d1cbc5ee012c96025c2aa42060d72a79ddd0b577878528cecb637190a4c
    role: target
  - path: data/records/ilmenite.yaml
    sha256: 6fcc33648fdeb7352757cdb639b87cecc3ac7fedf8481d803069bb5eec2a3544
    role: target
  - path: data/records/katsarosite.yaml
    sha256: 70f5c37f86e33265051032055fe64e6bf44e9a0f3ef055f4d3b605aa4f70a9c7
    role: target
  - path: data/records/kukharenkoite-ce.yaml
    sha256: 948da61159206ffd7d157e396af38387e0bc4f38cc4cbb4665815cdaa645081c
    role: target
  - path: data/records/kuliokite-y.yaml
    sha256: 0ff16d6a8cab92d0f306d4b4c895c7a8f1367486730c4676fa438e80729ba1b9
    role: target
  - path: data/records/lorenzenite.yaml
    sha256: 63921cf8ea515a24a9413cfad2cbfe7c7eefc27ed2d9864de6937642bbbfc151
    role: target
  - path: data/records/millerite.yaml
    sha256: cf4ea1827b9e503424920152ab7d175f5fe16db4740125d641df1dfac6a43373
    role: target
  - path: data/records/perovskite.yaml
    sha256: 45104b07f2cf3bbdd3a5aede5c14ee2c3e5ae35dbc3c482aa2cc144323921180
    role: target
  - path: data/records/polydymite.yaml
    sha256: 8cc946a28b9e26a5799f7f27d327b35fe6798a7ba6163d5ad3d7085ab6a8220e
    role: target
  - path: data/records/pyroaurite.yaml
    sha256: 1f48e4057dbd0b3917b294b6bd63a0f7bfddf9f34dd1a3972efa525fc2e6fadb
    role: target
  - path: data/records/synchysite-ce.yaml
    sha256: 7f2b86d15f0c3e5660b792a1acdb0dfe683ccc9c53d9c01f50a77656e181781b
    role: target
  - path: data/records/tenorite.yaml
    sha256: 8a246bb230b7bc77ae4ccea675c93395c334dee72f68dcb49ef1a3a4b045df82
    role: target
  - path: data/records/thulium.yaml
    sha256: 24456f05fb24d477fbea1aa1584f763bf61506fcdab6837713b105f020730a34
    role: target
  - path: data/records/titanite.yaml
    sha256: 42e0d9a8c2c5e5bb6cc8a92764d92525e4ffcddb6569450361842092711b807c
    role: target
  - path: data/records/vaesite.yaml
    sha256: 8578b291bb5b6ef240b0e5ddf288a38c60bbf9f94e0b687b5e7121674a0b6914
    role: target
  - path: reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-04/revision-0001/evidence.yaml
    sha256: ed3f293d67647ec6046bea289201746c85e0439da5bd3c205379e9ce16dc7306
    role: context
  - path: reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-04/revision-0001/review_findings.yaml
    sha256: d6eeece41ce9a8d4ca3ea11f52e2018a0b268c9b6ee5bcc6c93ff09c4348cd37
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
  - path: src/cmmmech/validation.py
    sha256: 63ff33d51b753dd715e6bd1c3e5f60a99e4fcb41b3aee68d536306a862d922e2
    role: context
targets:
- target_id: cmmmech:alicewilsonite-yce
  path: data/records/alicewilsonite-yce.yaml
  label: Alicewilsonite-(YCe)
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 036c8e2e81a1ea9f0f20c1036198da8af3585420e49c613f94e0d4e283611ac4
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/alicewilsonite-yce.yaml
    role: maintained_record
- target_id: cmmmech:alicewilsonite-yla
  path: data/records/alicewilsonite-yla.yaml
  label: Alicewilsonite-(YLa)
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 812fc5df06a6e2805b66e1cbb7a1c8ea4413bb3b5e9802728e5d0c9ff52de404
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/alicewilsonite-yla.yaml
    role: maintained_record
- target_id: cmmmech:allanite-concentrate
  path: data/records/allanite-concentrate.yaml
  label: Allanite concentrate
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: a3d7846b20719725fe22bf36dd604f3d65d86ad6dc219f4ef3fe4f9935259af1
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/allanite-concentrate.yaml
    role: maintained_record
- target_id: cmmmech:ancylite-ce
  path: data/records/ancylite-ce.yaml
  label: Ancylite-(Ce)
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: c9c05bcfa4881d3e8ace1d8a133e35add11a6b459ef4bd04c57091e48410a76f
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ancylite-ce.yaml
    role: maintained_record
- target_id: cmmmech:azurite
  path: data/records/azurite.yaml
  label: Azurite
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: e4e336a1fab18c45f32fa737356dc4c704f3fbbce83f15ad8d1db6c05640abe1
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/azurite.yaml
    role: maintained_record
- target_id: cmmmech:bainbridgeite-yce
  path: data/records/bainbridgeite-yce.yaml
  label: Bainbridgeite-(YCe)
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 03fa983c13377c02d37edc286632e927a7af15d9ad437a70c4af0e865d9dc6ad
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/bainbridgeite-yce.yaml
    role: maintained_record
- target_id: cmmmech:brucite
  path: data/records/brucite.yaml
  label: Brucite
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 1a0f2f63fbad406df282ecf2d8dcd7ff00bf5829384ab1a0b336ab9d48c66e5c
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/brucite.yaml
    role: maintained_record
- target_id: cmmmech:burbankite
  path: data/records/burbankite.yaml
  label: Burbankite
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 1f73514962eda538ad4fc01ad4770f8919652df2fca13c1318f1cc9ec22f2ac2
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/burbankite.yaml
    role: maintained_record
- target_id: cmmmech:calcioancylite-la
  path: data/records/calcioancylite-la.yaml
  label: Calcioancylite-(La)
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: ab19ed81a3ef357a5f7cdfbf12f1c6359178ea63d8ec799f90614d11a3a347c8
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/calcioancylite-la.yaml
    role: maintained_record
- target_id: cmmmech:calcioburbankite
  path: data/records/calcioburbankite.yaml
  label: Calcioburbankite
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 3b0a6b09a42a26e7a65e0f4ca4dc593bdf793456b2c6ac4a6f14b53b51532028
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/calcioburbankite.yaml
    role: maintained_record
- target_id: cmmmech:caysichite-y
  path: data/records/caysichite-y.yaml
  label: Caysichite-(Y)
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: b9e56a2da22dd26680cb72e9eb6a065acafa7a2dec8ff368c55a64c8c7d628dc
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/caysichite-y.yaml
    role: maintained_record
- target_id: cmmmech:cerianite-ce
  path: data/records/cerianite-ce.yaml
  label: Cerianite-(Ce)
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: e38b86bbd88ca0397b8ff32d05c273b5711f4b2d5ef7fc2ed36700027a0fbb5d
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/cerianite-ce.yaml
    role: maintained_record
- target_id: cmmmech:cordylite-ce
  path: data/records/cordylite-ce.yaml
  label: Cordylite-(Ce)
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: e664d3478a2345e9d374d1a9c16ca3f3e696d9bb87fd076c29469e8522566b8f
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/cordylite-ce.yaml
    role: maintained_record
- target_id: cmmmech:dolomite
  path: data/records/dolomite.yaml
  label: Dolomite
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 793180dc8f20e2cf07141865ba4755f6b11f156671b136c7b0e1cceedc355eae
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/dolomite.yaml
    role: maintained_record
- target_id: cmmmech:donnayite-y
  path: data/records/donnayite-y.yaml
  label: Donnayite-(Y)
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 3ae1ebfc1ae87fe1ce47b65a5aba1cc9ab6f5eda83206ef58c7639dba46cf0e9
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/donnayite-y.yaml
    role: maintained_record
- target_id: cmmmech:greenockite
  path: data/records/greenockite.yaml
  label: Greenockite
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 3f3529f48ed275de435080de47e8657c455d040fdc9d5f627208a6794ec3bfbc
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/greenockite.yaml
    role: maintained_record
- target_id: cmmmech:gysinite-nd
  path: data/records/gysinite-nd.yaml
  label: Gysinite-(Nd)
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 679aac8eeb7e755cfc12f422bac506dcbcf0af9c7f2ac4b59e9198fc7b92795c
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/gysinite-nd.yaml
    role: maintained_record
- target_id: cmmmech:hawleyite
  path: data/records/hawleyite.yaml
  label: Hawleyite
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: c22d696323198ede1fedfb7f0cb1a9594ef569e9e93ee4e1a6b23818fe432cda
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/hawleyite.yaml
    role: maintained_record
- target_id: cmmmech:hydrotalcite
  path: data/records/hydrotalcite.yaml
  label: Hydrotalcite
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 6781e9dd9e3fe44a67edc307e7ac977bdb6834f89a9e9231680dbc21102f8fc4
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/hydrotalcite.yaml
    role: maintained_record
- target_id: cmmmech:ilmenite
  path: data/records/ilmenite.yaml
  label: Ilmenite
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 841d0ee7d4b43d1cfc02be35a50d5e237e06f0382eda9db446a20a983f5ca472
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ilmenite.yaml
    role: maintained_record
- target_id: cmmmech:katsarosite
  path: data/records/katsarosite.yaml
  label: Katsarosite
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 8a67e3d0e90b4bb2d9d9708b3c7289d7251bbf8879aa502ca2e988375fcb52f5
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/katsarosite.yaml
    role: maintained_record
- target_id: cmmmech:kukharenkoite-ce
  path: data/records/kukharenkoite-ce.yaml
  label: Kukharenkoite-(Ce)
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 9fb541b7b40f03bb250ea74fcf6da677187d80943c513250eff15b6cf55a8bae
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/kukharenkoite-ce.yaml
    role: maintained_record
- target_id: cmmmech:kuliokite-y
  path: data/records/kuliokite-y.yaml
  label: Kuliokite-(Y)
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 9b86338da473672a6c7431ce0280c83658bedd22019aa5c607d4d9f7507718e7
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/kuliokite-y.yaml
    role: maintained_record
- target_id: cmmmech:lorenzenite
  path: data/records/lorenzenite.yaml
  label: Lorenzenite
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: c84c95eb234e5d84660b45cac94fdabcaee7d0e9eed98f60983560f70b1a7c40
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/lorenzenite.yaml
    role: maintained_record
- target_id: cmmmech:millerite
  path: data/records/millerite.yaml
  label: Millerite
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 99d53af0ad69c76ea8a55a984aeb71d922317528351c9a743bb13a18026366c1
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/millerite.yaml
    role: maintained_record
- target_id: cmmmech:perovskite
  path: data/records/perovskite.yaml
  label: Perovskite
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 3fee8bbed1bc5fb58c48fea0f8137c00d0c453f2b95d20f6bf8445b7ee3e01b2
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/perovskite.yaml
    role: maintained_record
- target_id: cmmmech:polydymite
  path: data/records/polydymite.yaml
  label: Polydymite
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: c3b88f6bc89a86d166704ce3f06140c094f0650176c6a2ab5b9d7450f308c9a5
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/polydymite.yaml
    role: maintained_record
- target_id: cmmmech:pyroaurite
  path: data/records/pyroaurite.yaml
  label: Pyroaurite
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 75723b450bae2dc23b4a2b61309987ae89caaaeb0319e736314f0632bec6792d
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/pyroaurite.yaml
    role: maintained_record
- target_id: cmmmech:synchysite-ce
  path: data/records/synchysite-ce.yaml
  label: Synchysite-(Ce)
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: fd443f5bbefffd39b1bb2497af25fc7e029b5f87e17c9b10e60d372f639d2e1e
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/synchysite-ce.yaml
    role: maintained_record
- target_id: cmmmech:tenorite
  path: data/records/tenorite.yaml
  label: Tenorite
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 2e0322d4b5d457b086fa3eb06e76050dc1d37e88964e56c3e9fab07c7879f2c6
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/tenorite.yaml
    role: maintained_record
- target_id: cmmmech:thulium
  path: data/records/thulium.yaml
  label: Thulium
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 2fad9beb7e53381739630cb90905f14bcdea92622a868d10fe3212aad4b1572e
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/thulium.yaml
    role: maintained_record
- target_id: cmmmech:titanite
  path: data/records/titanite.yaml
  label: Titanite
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 2b6dd2ea9ca2b2313d23b4bd9eaa2bfc6ff278387abe70a33744e55fabd766c5
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/titanite.yaml
    role: maintained_record
- target_id: cmmmech:vaesite
  path: data/records/vaesite.yaml
  label: Vaesite
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 26abdb251fde44c2dc316615fbcce84fa9b12cb30ff78f27914f1301ba42710e
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/vaesite.yaml
    role: maintained_record
scope:
  description: 'All 33 CMMMech records affected by the 3 Cycle 2 Stage 4 findings
    carried into Stage 5 (30 mineral records in GRP-C2S5-001 / #817, 2 records in
    GRP-C2S5-002 / #818, and 1 mineral record in GRP-C2S5-003 / #819).'
  selection: cycle2_stage4_open_finding_targets
  coverage: full
  population_size: 33
  reviewed_target_ids:
  - cmmmech:alicewilsonite-yce
  - cmmmech:alicewilsonite-yla
  - cmmmech:allanite-concentrate
  - cmmmech:ancylite-ce
  - cmmmech:azurite
  - cmmmech:bainbridgeite-yce
  - cmmmech:brucite
  - cmmmech:burbankite
  - cmmmech:calcioancylite-la
  - cmmmech:calcioburbankite
  - cmmmech:caysichite-y
  - cmmmech:cerianite-ce
  - cmmmech:cordylite-ce
  - cmmmech:dolomite
  - cmmmech:donnayite-y
  - cmmmech:greenockite
  - cmmmech:gysinite-nd
  - cmmmech:hawleyite
  - cmmmech:hydrotalcite
  - cmmmech:ilmenite
  - cmmmech:katsarosite
  - cmmmech:kukharenkoite-ce
  - cmmmech:kuliokite-y
  - cmmmech:lorenzenite
  - cmmmech:millerite
  - cmmmech:perovskite
  - cmmmech:polydymite
  - cmmmech:pyroaurite
  - cmmmech:synchysite-ce
  - cmmmech:tenorite
  - cmmmech:thulium
  - cmmmech:titanite
  - cmmmech:vaesite
checks:
- check_id: chk-validate-records
  name: Schema and semantic record validation
  status: passed
  required: true
  summary: All 631 records (including all 33 remediated records) pass .venv/bin/python
    -m cmmmech validate --require-records with 0 errors and 0 warnings.
  target_ids:
  - cmmmech:alicewilsonite-yce
  - cmmmech:alicewilsonite-yla
  - cmmmech:allanite-concentrate
  - cmmmech:ancylite-ce
  - cmmmech:azurite
  - cmmmech:bainbridgeite-yce
  - cmmmech:brucite
  - cmmmech:burbankite
  - cmmmech:calcioancylite-la
  - cmmmech:calcioburbankite
  - cmmmech:caysichite-y
  - cmmmech:cerianite-ce
  - cmmmech:cordylite-ce
  - cmmmech:dolomite
  - cmmmech:donnayite-y
  - cmmmech:greenockite
  - cmmmech:gysinite-nd
  - cmmmech:hawleyite
  - cmmmech:hydrotalcite
  - cmmmech:ilmenite
  - cmmmech:katsarosite
  - cmmmech:kukharenkoite-ce
  - cmmmech:kuliokite-y
  - cmmmech:lorenzenite
  - cmmmech:millerite
  - cmmmech:perovskite
  - cmmmech:polydymite
  - cmmmech:pyroaurite
  - cmmmech:synchysite-ce
  - cmmmech:tenorite
  - cmmmech:thulium
  - cmmmech:titanite
  - cmmmech:vaesite
  command: .venv/bin/python -m cmmmech validate --require-records
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-ima-2026-09
  - ev-cycle2-stage4-findings
  - ev-schema
- check_id: chk-validate-history
  name: Append-only history sidecar validation
  status: passed
  required: true
  summary: All 33 new EDIT history sidecars and existing history sidecars pass .venv/bin/python
    -m cmmmech validate-history --base origin/main.
  target_ids:
  - cmmmech:alicewilsonite-yce
  - cmmmech:alicewilsonite-yla
  - cmmmech:allanite-concentrate
  - cmmmech:ancylite-ce
  - cmmmech:azurite
  - cmmmech:bainbridgeite-yce
  - cmmmech:brucite
  - cmmmech:burbankite
  - cmmmech:calcioancylite-la
  - cmmmech:calcioburbankite
  - cmmmech:caysichite-y
  - cmmmech:cerianite-ce
  - cmmmech:cordylite-ce
  - cmmmech:dolomite
  - cmmmech:donnayite-y
  - cmmmech:greenockite
  - cmmmech:gysinite-nd
  - cmmmech:hawleyite
  - cmmmech:hydrotalcite
  - cmmmech:ilmenite
  - cmmmech:katsarosite
  - cmmmech:kukharenkoite-ce
  - cmmmech:kuliokite-y
  - cmmmech:lorenzenite
  - cmmmech:millerite
  - cmmmech:perovskite
  - cmmmech:polydymite
  - cmmmech:pyroaurite
  - cmmmech:synchysite-ce
  - cmmmech:tenorite
  - cmmmech:thulium
  - cmmmech:titanite
  - cmmmech:vaesite
  command: .venv/bin/python -m cmmmech validate-history --base origin/main
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-cycle2-stage4-findings
- check_id: chk-ima-source-id-normalization
  name: Canonical ima_2026_09 source key across all 30 remediated mineral records
  status: passed
  required: true
  summary: All 30 mineral records in GRP-C2S5-001 (#817) now key the September 2026
    IMA-CNMNC Master List under canonical ima_2026_09, achieving 100% (380/380) uniformity
    across all mineral records in CMMMech.
  target_ids:
  - cmmmech:alicewilsonite-yce
  - cmmmech:alicewilsonite-yla
  - cmmmech:ancylite-ce
  - cmmmech:azurite
  - cmmmech:bainbridgeite-yce
  - cmmmech:brucite
  - cmmmech:burbankite
  - cmmmech:calcioancylite-la
  - cmmmech:calcioburbankite
  - cmmmech:caysichite-y
  - cmmmech:cerianite-ce
  - cmmmech:cordylite-ce
  - cmmmech:dolomite
  - cmmmech:donnayite-y
  - cmmmech:greenockite
  - cmmmech:gysinite-nd
  - cmmmech:hawleyite
  - cmmmech:hydrotalcite
  - cmmmech:ilmenite
  - cmmmech:kukharenkoite-ce
  - cmmmech:kuliokite-y
  - cmmmech:lorenzenite
  - cmmmech:millerite
  - cmmmech:perovskite
  - cmmmech:polydymite
  - cmmmech:pyroaurite
  - cmmmech:synchysite-ce
  - cmmmech:tenorite
  - cmmmech:titanite
  - cmmmech:vaesite
  command: .venv/bin/python -m cmmmech validate --require-records
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-ima-2026-09
  - ev-cycle2-stage4-findings
- check_id: chk-protein-evidence-parity-and-predicate
  name: Causal-graph protein_examples evidence parity (#818) and dissolution predicate
    alignment (#819)
  status: passed
  required: true
  summary: 'allanite-concentrate (UniProtKB:Q5FT13, UniProtKB:Q5FTI1) and thulium
    (UniProtKB:O34952, UniProtKB:Q797B3, UniProtKB:P54496, UniProtKB:O32206) have
    identical evidence[].explanation strings between mechanisms[].protein_examples
    and causal_graphs[].nodes[].protein_examples, and katsarosite uses predicate:
    solubilizes on its secreted_organic_acids -> znso4_hopeite_culture_substrate dissolution
    edge.'
  target_ids:
  - cmmmech:allanite-concentrate
  - cmmmech:katsarosite
  - cmmmech:thulium
  evidence_ids:
  - ev-cycle2-stage4-findings
  - ev-schema
evidence:
- evidence_id: ev-ima-2026-09
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: IMA-CNMNC List of Mineral Names (September 2026)
  accessed_at: '2026-10-22T13:20:00Z'
  support: supports
  summary: Official IMA-CNMNC Master List (September 2026) cited across all 380 mineral
    records under canonical source key ima_2026_09.
- evidence_id: ev-cycle2-stage4-findings
  kind: record_content
  reference: reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-04/revision-0001/review_findings.yaml
  locator: findings[0..2]
  accessed_at: '2026-10-22T13:20:00Z'
  support: supports
  summary: Frozen Cycle 2 Stage 4 review findings ledger defining cmmmech-cycle2-stage4-finding-0001,
    cmmmech-cycle2-stage4-finding-0002, and cmmmech-cycle2-stage4-finding-0003 across
    the 33 target records.
  snapshot_sha256: d6eeece41ce9a8d4ca3ea11f52e2018a0b268c9b6ee5bcc6c93ff09c4348cd37
- evidence_id: ev-schema
  kind: record_content
  reference: src/cmmmech/schema/cmmmech.yaml
  locator: classes.CriticalMineralRecord, enums.CausalPredicateEnum
  accessed_at: '2026-10-22T13:20:00Z'
  support: supports
  summary: Canonical LinkML schema defining CriticalMineralRecord, ProteinExample,
    and CausalPredicateEnum (including solubilizes).
  snapshot_sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
assessments:
- assessment_id: assess-grp1-ima-source-id
  area: consistency
  topic: Canonical ima_2026_09 source key across 30 mineral records (#817)
  outcome: supported
  summary: All 30 mineral records previously using ima2026 (14), ima202609 (9), or
    ima_202609 (7) now use canonical ima_2026_09.
  target_ids:
  - cmmmech:alicewilsonite-yce
  - cmmmech:alicewilsonite-yla
  - cmmmech:ancylite-ce
  - cmmmech:azurite
  - cmmmech:bainbridgeite-yce
  - cmmmech:brucite
  - cmmmech:burbankite
  - cmmmech:calcioancylite-la
  - cmmmech:calcioburbankite
  - cmmmech:caysichite-y
  - cmmmech:cerianite-ce
  - cmmmech:cordylite-ce
  - cmmmech:dolomite
  - cmmmech:donnayite-y
  - cmmmech:greenockite
  - cmmmech:gysinite-nd
  - cmmmech:hawleyite
  - cmmmech:hydrotalcite
  - cmmmech:ilmenite
  - cmmmech:kukharenkoite-ce
  - cmmmech:kuliokite-y
  - cmmmech:lorenzenite
  - cmmmech:millerite
  - cmmmech:perovskite
  - cmmmech:polydymite
  - cmmmech:pyroaurite
  - cmmmech:synchysite-ce
  - cmmmech:tenorite
  - cmmmech:titanite
  - cmmmech:vaesite
  evidence_ids:
  - ev-ima-2026-09
  - ev-cycle2-stage4-findings
  metrics:
  - name: canonical_ima_source_key_compliance
    value: 1.0
    unit: fraction
    definition: Fraction of the 30 remediated mineral records using canonical source
      id ima_2026_09
    denominator: 30
    minimum: 0.0
    maximum: 1.0
- assessment_id: assess-grp2-protein-evidence-parity
  area: consistency
  topic: Parity of protein_examples evidence explanations between mechanisms and causal_graphs
    (#818)
  outcome: supported
  summary: Both allanite-concentrate (UniProtKB:Q5FT13, UniProtKB:Q5FTI1) and thulium
    (UniProtKB:O34952, UniProtKB:Q797B3, UniProtKB:P54496, UniProtKB:O32206) now carry
    identical full evidence[].explanation strings on causal_graphs[].nodes[].protein_examples
    and mechanisms[].protein_examples.
  target_ids:
  - cmmmech:allanite-concentrate
  - cmmmech:thulium
  evidence_ids:
  - ev-cycle2-stage4-findings
  - ev-schema
  metrics:
  - name: protein_example_evidence_parity
    value: 1.0
    unit: fraction
    definition: Fraction of remediated records with identical mechanism and causal-node
      protein_examples evidence explanations
    denominator: 2
    minimum: 0.0
    maximum: 1.0
- assessment_id: assess-grp3-katsarosite-predicate
  area: consistency
  topic: Dissolution edge predicate solubilizes on katsarosite causal graph (#819)
  outcome: supported
  summary: 'data/records/katsarosite.yaml (niger_associated_zinc_oxalate_formation_graph)
    now uses predicate: solubilizes on its secreted_organic_acids -> znso4_hopeite_culture_substrate
    dissolution edge, matching the sibling Aspergillus niger oxalate biomineralization
    cohort.'
  target_ids:
  - cmmmech:katsarosite
  evidence_ids:
  - ev-cycle2-stage4-findings
  - ev-schema
  metrics:
  - name: oxalate_cohort_predicate_alignment
    value: 1.0
    unit: fraction
    definition: 'Fraction of remediated oxalate biomineralization records using predicate:
      solubilizes on substrate dissolution edges'
    denominator: 1
    minimum: 0.0
    maximum: 1.0
findings:
- finding_id: cmmmech-cycle2-stage4-finding-0001
  issue_key: cmmmech.mineral.noncanonical-ima-master-list-source-ids
  category: consistency
  severity: minor
  status: resolved
  certainty: confirmed
  title: 30 mineral records now use canonical ima_2026_09 source key for the September
    2026 IMA Master List
  description: Normalized sources[].id from ima2026 (14 records), ima202609 (9 records),
    and ima_202609 (7 records) to canonical ima_2026_09 across all 30 mineral records
    and recorded 30 append-only EDIT history sidecars.
  target_ids:
  - cmmmech:alicewilsonite-yce
  - cmmmech:alicewilsonite-yla
  - cmmmech:ancylite-ce
  - cmmmech:azurite
  - cmmmech:bainbridgeite-yce
  - cmmmech:brucite
  - cmmmech:burbankite
  - cmmmech:calcioancylite-la
  - cmmmech:calcioburbankite
  - cmmmech:caysichite-y
  - cmmmech:cerianite-ce
  - cmmmech:cordylite-ce
  - cmmmech:dolomite
  - cmmmech:donnayite-y
  - cmmmech:greenockite
  - cmmmech:gysinite-nd
  - cmmmech:hawleyite
  - cmmmech:hydrotalcite
  - cmmmech:ilmenite
  - cmmmech:kukharenkoite-ce
  - cmmmech:kuliokite-y
  - cmmmech:lorenzenite
  - cmmmech:millerite
  - cmmmech:perovskite
  - cmmmech:polydymite
  - cmmmech:pyroaurite
  - cmmmech:synchysite-ce
  - cmmmech:tenorite
  - cmmmech:titanite
  - cmmmech:vaesite
  field_paths:
  - sources
  - curation_history
  - history_refs
  evidence_ids:
  - ev-ima-2026-09
  - ev-cycle2-stage4-findings
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/alicewilsonite-yce.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/alicewilsonite-yla.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/ancylite-ce.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/azurite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/bainbridgeite-yce.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/brucite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/burbankite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/calcioancylite-la.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/calcioburbankite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/caysichite-y.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/cerianite-ce.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/cordylite-ce.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/dolomite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/donnayite-y.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/greenockite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/gysinite-nd.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/hawleyite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/hydrotalcite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/ilmenite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/kukharenkoite-ce.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/kuliokite-y.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/lorenzenite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/millerite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/perovskite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/polydymite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/pyroaurite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/synchysite-ce.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/tenorite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/titanite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/vaesite.yaml
    role: maintained_record
  disposition_reason: 'Resolved under GitHub issue #817 (group GRP-C2S5-001) by normalizing
    sources[].id to ima_2026_09 with append-only EDIT history sidecars on all 30 records.'
  previous_occurrences:
  - repository: CultureBotAI/CMMMech
    review_id: 20261022T115001Z-cycle2-stage4-mineral-cohort-review
    finding_id: cmmmech-cycle2-stage4-finding-0001
  external_issues:
  - https://github.com/CultureBotAI/CMMMech/issues/817
- finding_id: cmmmech-cycle2-stage4-finding-0002
  issue_key: cmmmech.protein_examples.mechanism-node-evidence-explanation-drift
  category: consistency
  severity: minor
  status: resolved
  certainty: confirmed
  title: allanite-concentrate and thulium causal-graph node protein_examples evidence
    explanations now match mechanisms[].protein_examples
  description: Synchronized causal_graphs[].nodes[].protein_examples[].evidence[].explanation
    with mechanisms[].protein_examples[].evidence[].explanation for UniProtKB:Q5FT13
    and UniProtKB:Q5FTI1 in allanite-concentrate.yaml and UniProtKB:O34952, UniProtKB:Q797B3,
    UniProtKB:P54496, and UniProtKB:O32206 in thulium.yaml with append-only EDIT history
    sidecars.
  target_ids:
  - cmmmech:allanite-concentrate
  - cmmmech:thulium
  field_paths:
  - causal_graphs
  - curation_history
  - history_refs
  evidence_ids:
  - ev-cycle2-stage4-findings
  - ev-schema
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/allanite-concentrate.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/thulium.yaml
    role: maintained_record
  disposition_reason: 'Resolved under GitHub issue #818 (group GRP-C2S5-002) via scripts/curate_causal_graphs.py
    with append-only EDIT history sidecars on both records.'
  previous_occurrences:
  - repository: CultureBotAI/CMMMech
    review_id: 20261022T115006Z-cycle2-stage4-causal-graphs-cohort-review
    finding_id: cmmmech-cycle2-stage4-finding-0002
  external_issues:
  - https://github.com/CultureBotAI/CMMMech/issues/818
- finding_id: cmmmech-cycle2-stage4-finding-0003
  issue_key: cmmmech.katsarosite.legacy-chelates-predicate-on-hopeite-solubilization
  category: consistency
  severity: minor
  status: resolved
  certainty: confirmed
  title: 'katsarosite causal graph now uses predicate: solubilizes on its substrate
    dissolution edge'
  description: 'Updated predicate: chelates to predicate: solubilizes on the secreted_organic_acids
    -> znso4_hopeite_culture_substrate edge in data/records/katsarosite.yaml (niger_associated_zinc_oxalate_formation_graph)
    with an append-only EDIT history sidecar.'
  target_ids:
  - cmmmech:katsarosite
  field_paths:
  - causal_graphs
  - curation_history
  - history_refs
  evidence_ids:
  - ev-cycle2-stage4-findings
  - ev-schema
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/katsarosite.yaml
    role: maintained_record
  disposition_reason: 'Resolved under GitHub issue #819 (group GRP-C2S5-003) via scripts/curate_causal_graphs.py
    with an append-only EDIT history sidecar.'
  previous_occurrences:
  - repository: CultureBotAI/CMMMech
    review_id: 20261022T115007Z-katsarosite-cycle2-stage4-record-review
    finding_id: cmmmech-cycle2-stage4-finding-0003
  external_issues:
  - https://github.com/CultureBotAI/CMMMech/issues/819
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - cmmmech:alicewilsonite-yce
  - cmmmech:alicewilsonite-yla
  - cmmmech:allanite-concentrate
  - cmmmech:ancylite-ce
  - cmmmech:azurite
  - cmmmech:bainbridgeite-yce
  - cmmmech:brucite
  - cmmmech:burbankite
  - cmmmech:calcioancylite-la
  - cmmmech:calcioburbankite
  - cmmmech:caysichite-y
  - cmmmech:cerianite-ce
  - cmmmech:cordylite-ce
  - cmmmech:dolomite
  - cmmmech:donnayite-y
  - cmmmech:greenockite
  - cmmmech:gysinite-nd
  - cmmmech:hawleyite
  - cmmmech:hydrotalcite
  - cmmmech:ilmenite
  - cmmmech:katsarosite
  - cmmmech:kukharenkoite-ce
  - cmmmech:kuliokite-y
  - cmmmech:lorenzenite
  - cmmmech:millerite
  - cmmmech:perovskite
  - cmmmech:polydymite
  - cmmmech:pyroaurite
  - cmmmech:synchysite-ce
  - cmmmech:tenorite
  - cmmmech:thulium
  - cmmmech:titanite
  - cmmmech:vaesite
  evidence_ids:
  - ev-ima-2026-09
  - ev-cycle2-stage4-findings
  - ev-schema
  rationale: 'All 33 remediated records represent distinct mineral species (31 records),
    elements (1 record: thulium), or primary resources (1 record: allanite-concentrate)
    with disjoint identifiers and provenance; cohort boundaries from Cycle 2 Stage
    4 are retained unchanged.'
limitations:
- This verification review is scoped to the 33 records remediated in Cycle 2 Stage
  5; the remaining 598 records were verified with 0 open findings in the immutable
  Cycle 2 Stage 4 review bundles.
```
