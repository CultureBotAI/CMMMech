# Stage 5 Grouped Remediation Issue Map (`mech-goal-sequence-20261019`, Cycle 7, Stage 5)

- **Repository**: `CultureBotAI/CMMMech` (`cmmmech`)
- **Source Revision**: `7369b587c86b77cbd43a38cdfdb2477ae8bba1d0`
- **Post-Remediation Record Revision**: `4d4079195069940955d7016fab42ff3dd3450803`
- **Scope Frozen At**: `2026-11-04T15:20:00Z`
- **Previous Stage Evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000007/stage-04/revision-0001/evidence.yaml` (`908833964996c9690db95c25eb7249bb5f98e4c2beaebdf015df2ffe270aca4c`)
- **Post-Remediation Structured Review Bundle**: `reviews/structured/20261104T153000Z-cycle7-stage5-remediation-verification/review.yaml` (`sha256: 4d321b019672307f51eed851ed4a1ff3bdd79ca225342144739611dbbe8b90e4`)

## 1. Deduplication Against Open & Closed GitHub Issues

Before creating issues, the open and closed GitHub issue queues in `CultureBotAI/CMMMech` were searched via `gh issue list --repo CultureBotAI/CMMMech --state open --limit 100` and `gh issue list --repo CultureBotAI/CMMMech --state closed --limit 30`. Open issues (`#106`, `#115`, `#805`, `#822`, `#839`, `#840`) were inspected and none covered the 3 Cycle 7 Stage 4 review findings (`cmmmech-cycle7-stage4-finding-0001`, `cmmmech-cycle7-stage4-finding-0002`, `cmmmech-cycle7-stage4-finding-0003`). Three new tracked GitHub issues (`#918`, `#919`, `#920`) were created, one per root-cause and repair-ownership group.

## 2. Root-Cause Groups, Issue Mapping, and Finding Dispositions

| Group ID | Finding IDs | Issue Key | GitHub Issue | Status | Target Records (16 total) | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| `GRP-C7S5-001` | `cmmmech-cycle7-stage4-finding-0001` | `cmmmech.round125-minerals.missing-ima-symbol-slot` | [`#918`](https://github.com/CultureBotAI/CMMMech/issues/918) | `resolved` | 4 mineral records (`fengruiite`, `igelstromite`, `lazerckerite`, `plumbogottlobite`) | Populated top-level `ima_symbol: Fru` in `data/records/fengruiite.yaml` (`IMA 2024-045`, `tian_2026_fengruiite`), `ima_symbol: Ig` in `data/records/igelstromite.yaml` (`IMA 2021-035`, `holtstam_2024_igelstromite`), `ima_symbol: Lzc` in `data/records/lazerckerite.yaml` (`IMA 2022-113`, `pazout_2024_lazerckerite`), and `ima_symbol: Pgtb` in `data/records/plumbogottlobite.yaml` (`IMA 2025-075`, `kampf_2026_plumbogottlobite`) immediately after `material_kind: mineral`, bringing all 8 mineral records in the 427-mineral corpus whose descriptions state an IMA-CNMNC symbol to `8/8` (`100%`) top-level `ima_symbol` completeness, with 4 append-only `EDIT` history sidecars. |
| `GRP-C7S5-002` | `cmmmech-cycle7-stage4-finding-0002` | `cmmmech.cycle7-stage3-sulfur-graphs.edge-desc-grammar-and-incomplete-edge-evidence-loci` | [`#919`](https://github.com/CultureBotAI/CMMMech/issues/919) | `resolved` | 9 records (`cassiterite-polymetallic-sulfide-ore`, `chalcopyrite`, `chalcopyrite-enargite-concentrate`, `coal-beneficiation-waste`, `copper`, `copper-smelter-flue-dust`, `molybdenite`, `pyrite-roasting-cinder`, `skutterudite`) | Pluralized singular verbs (`oxidizes` -> `oxidize`, `catalyzes` -> `catalyze`, `disproportionates` -> `disproportionate`) in `sqr_oxidoreductase` and `tth_hydrolase` outgoing edge descriptions across all 9 records and updated outgoing edge `evidence[0].explanation` across all 9 records to name every node-attached `Sqr` and `TetH`/`Tth` locus, with 9 append-only `EDIT` history sidecars. |
| `GRP-C7S5-003` | `cmmmech-cycle7-stage4-finding-0003` | `cmmmech.aspergillus-atcc1015-cexa-node.description-omits-strain-matched-g3y4n5` | [`#920`](https://github.com/CultureBotAI/CMMMech/issues/920) | `resolved` | 3 records (`birnessite`, `lindbergite`, `manganese-ore`) | Updated `cexa_citrate_exporter.description` in `data/records/birnessite.yaml` (`causal_graphs[1].nodes[0]`), `data/records/lindbergite.yaml` (`causal_graphs[0].nodes[0]`), and `data/records/manganese-ore.yaml` (`causal_graphs[0].nodes[0]`) to explicitly name both strain-matched `Aspergillus niger` ATCC 1015 CexA `UniProtKB:G3Y4N5` (`CEXA_ASPNA` / `ASPNIDRAFT_56962`) and species-level reviewed CexA `UniProtKB:A0A254TZW7` (`CEXA_ASPNG`), with 3 append-only `EDIT` history sidecars. |

## 3. Carry-Forward Blockers & Infrastructure Tasks

- **Carry-Forward Findings (`carry_forward_ids`)**: `[]` (0 open/deferred findings remain).
- **Infrastructure Tasks (`infra_tasks`)**: `[]` (all 3 Cycle 7 Stage 4 findings were resolved directly in record YAML and history sidecars).
