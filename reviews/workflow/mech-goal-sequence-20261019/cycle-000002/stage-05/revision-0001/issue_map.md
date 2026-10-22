# Stage 5 Grouped Remediation Issue Map (`mech-goal-sequence-20261019`, Cycle 2, Stage 5)

- **Repository**: `CultureBotAI/CMMMech` (`cmmmech`)
- **Source Revision**: `e16fd0f59192b2bbc20e9baa943fb67085950171`
- **Scope Frozen At**: `2026-10-22T13:14:00Z`
- **Previous Stage Evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-04/revision-0001/evidence.yaml` (`ed3f293d67647ec6046bea289201746c85e0439da5bd3c205379e9ce16dc7306`)
- **Post-Remediation Structured Review Bundle**: `reviews/structured/20261022T132200Z-cycle2-stage5-remediation-verification/review.yaml` (`sha256: dc297e4313e15ddd8fa1c4f217573f039073b80306e7c741bdeb825d377395d0`)

## 1. Deduplication Against Open & Closed GitHub Issues

Before creating issues, the open and closed GitHub issue queues in `CultureBotAI/CMMMech` were searched via `gh issue list --repo CultureBotAI/CMMMech --state all --limit 100`. Only 2 open backlog issues existed (`#106`, `#115`), neither covering the 3 Cycle 2 Stage 4 review findings (`cmmmech-cycle2-stage4-finding-0001`, `cmmmech-cycle2-stage4-finding-0002`, `cmmmech-cycle2-stage4-finding-0003`). Three new tracked GitHub issues (`#817`, `#818`, `#819`) were created, one per root-cause and repair-ownership group.

## 2. Root-Cause Groups, Issue Mapping, and Finding Dispositions

| Group ID | Finding IDs | Issue Key | GitHub Issue | Status | Target Records (33 total) | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| `GRP-C2S5-001` | `cmmmech-cycle2-stage4-finding-0001` | `cmmmech.mineral.noncanonical-ima-source-id-variants` | [`#817`](https://github.com/CultureBotAI/CMMMech/issues/817) | `resolved` | 30 mineral records (`alicewilsonite-yce`, `alicewilsonite-yla`, `ancylite-ce`, `azurite`, `bainbridgeite-yce`, `brucite`, `burbankite`, `calcioancylite-la`, `calcioburbankite`, `caysichite-y`, `cerianite-ce`, `cordylite-ce`, `dolomite`, `donnayite-y`, `greenockite`, `gysinite-nd`, `hawleyite`, `hydrotalcite`, `ilmenite`, `kukharenkoite-ce`, `kuliokite-y`, `lorenzenite`, `millerite`, `perovskite`, `polydymite`, `pyroaurite`, `synchysite-ce`, `tenorite`, `titanite`, `vaesite`) | Normalized `sources[].id` from `ima2026` (14 records), `ima202609` (9 records), and `ima_202609` (7 records) to canonical `ima_2026_09` with 30 append-only `EDIT` history sidecars. |
| `GRP-C2S5-002` | `cmmmech-cycle2-stage4-finding-0002` | `cmmmech.causal-graphs.node-protein-example-explanation-drift` | [`#818`](https://github.com/CultureBotAI/CMMMech/issues/818) | `resolved` | 2 records (`allanite-concentrate`, `thulium`) | Synchronized `causal_graphs[].nodes[].protein_examples[].evidence[].explanation` with `mechanisms[].protein_examples[].evidence[].explanation` via `scripts/curate_causal_graphs.py` with 2 append-only `EDIT` history sidecars. |
| `GRP-C2S5-003` | `cmmmech-cycle2-stage4-finding-0003` | `cmmmech.katsarosite.legacy-chelates-predicate-on-dissolution-edge` | [`#819`](https://github.com/CultureBotAI/CMMMech/issues/819) | `resolved` | 1 mineral record (`katsarosite`) | Updated `predicate: chelates` to `predicate: solubilizes` on the `secreted_organic_acids -> znso4_hopeite_culture_substrate` edge in `data/records/katsarosite.yaml` (`niger_associated_zinc_oxalate_formation_graph`) via `scripts/curate_causal_graphs.py` with 1 append-only `EDIT` history sidecar. |

## 3. Carry-Forward Blockers & Infrastructure Tasks

- **Carry-Forward Findings (`carry_forward_ids`)**: `[]` (0 open/deferred findings remain).
- **Infrastructure Tasks (`infra_tasks`)**: `[]` (all fixes are record-level YAML and history sidecar updates; no Cycle 2 Stage 4 findings required infrastructure changes).
