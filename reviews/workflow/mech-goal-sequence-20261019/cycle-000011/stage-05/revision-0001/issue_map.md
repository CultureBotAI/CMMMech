# Cycle 11 Stage 5 Issue Map & Finding Dispositions

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage / Revision**: Cycle `11`, Stage `5` (`resolve_review_findings`), Revision `1`
- **Frozen Predecessor Commit (`source_revision`)**: `e5435802649ba486fc86d883ffed926e23fa8719`
- **Predecessor Stage 4 Evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000011/stage-04/revision-0001/evidence.yaml` (`sha256: 99de4737c419ba8a1368933e1f7221be4aae1affccaef5d220e4867680c45750`)
- **Post-Remediation Structured Review Bundle**: `reviews/structured/20261109T111500Z-cycle11-stage5-remediation-verification/review.yaml` (`verdict: pass`, `0` open findings)

## Grouped Remediation Summary

| Group ID | Finding ID | GitHub Issue | Target Records | Status |
| :--- | :--- | :--- | :--- | :--- |
| `GRP-C11S5-001` | `cmmmech-cycle11-stage4-finding-0001` | [#967](https://github.com/CultureBotAI/CMMMech/issues/967) | `cmmmech:enstatite`, `cmmmech:olivine-group`, `cmmmech:dunite` | `resolved` |
| `GRP-C11S5-002` | `cmmmech-cycle11-stage4-finding-0002` | [#968](https://github.com/CultureBotAI/CMMMech/issues/968) | `cmmmech:metacinnabar` | `resolved` |
| `GRP-C11S5-003` | `cmmmech-cycle11-stage4-finding-0003` | [#969](https://github.com/CultureBotAI/CMMMech/issues/969) | `cmmmech:scandium` | `resolved` |

## Detailed Finding Dispositions

### 1. `GRP-C11S5-001` (`cmmmech-cycle11-stage4-finding-0001` -> Issue [#967](https://github.com/CultureBotAI/CMMMech/issues/967))
- **Root Cause**: Across the three *Gluconobacter oxydans* whole-culture biolixiviant silicate bioleaching records — `data/records/enstatite.yaml` (`klug_2026`), `data/records/olivine-group.yaml` (`klug_2026`), and `data/records/dunite.yaml` (`lee2025`) — `enstatite.yaml` `causal_graphs[0].nodes[4].description` retained a generic parenthetical template string repeating the capitalized node label, `edges[0..2]` in `enstatite.yaml` and `olivine-group.yaml` and `edges[1..2]` in `dunite.yaml` retained generic one-line template explanations, and `dunite.yaml` asserted unqualified `supports: support` on `pqqC` (`UniProtKB:Q9L3B2`) and `gdh` (`UniProtKB:P27175`) `protein_examples` and `edges[1..2]` despite whole-culture comparisons without single-gene `pqqC`/`mgdh` knockouts.
- **Remediation**:
  - Updated `causal_graphs[0].nodes[4].description` and `causal_graphs[0].edges[0..2].evidence[0].explanation` in `data/records/enstatite.yaml`, `causal_graphs[0].edges[0..2].evidence[0].explanation` in `data/records/olivine-group.yaml`, and `mechanisms[0].protein_examples[2..3].evidence[0]`, `causal_graphs[0].nodes[1..2].protein_examples[0].evidence[0]`, and `causal_graphs[0].edges[1..2].evidence[0]` (`supports: partial`) in `data/records/dunite.yaml` via `scripts/curate_causal_graphs.py` (`curate_record_file`).
  - Minted append-only `EDIT` history sidecars:
    - `history/records/enstatite/2026-11-09T111134Z-marcin-676ddc.yaml`
    - `history/records/olivine-group/2026-11-09T111134Z-marcin-1b0cea.yaml`
    - `history/records/dunite/2026-11-09T111134Z-marcin-ab3f8b.yaml`

### 2. `GRP-C11S5-002` (`cmmmech-cycle11-stage4-finding-0002` -> Issue [#968](https://github.com/CultureBotAI/CMMMech/issues/968))
- **Root Cause**: In `data/records/metacinnabar.yaml` (`vazquez_rodriguez2015`), `mechanisms[0].protein_examples[0]` and `causal_graphs[0].nodes[0].protein_examples[0]` for `UniProtKB:U5TVQ7` (`soxB`) stated that Vazquez-Rodriguez et al. (2015) studied pure-culture dissolution of `"synthetic metacinnabar (beta-HgS)"` whereas primary pure-culture incubations (Figures 3-5, Table 1) used 2 g/L ground natural museum metacinnabar (<250 um, with pyritic inclusions) and tested synthetic black HgS in the separate daily-thiosulfate-spike comparison (Figures 6-7); `causal_graphs[0].nodes[1].description` omitted feed specifics; `edges[1]` asserted `supports: support` for soluble Hg(II) accumulation despite low aqueous Hg in viable cultures and chemical Hg release / S0 carryover in controls; and `edges[0..3]` retained generic one-line explanations.
- **Remediation**:
  - Updated `mechanisms[0].protein_examples[0].evidence[0].explanation`, `causal_graphs[0].nodes[0].protein_examples[0].evidence[0].explanation`, `causal_graphs[0].nodes[1].description`, and `causal_graphs[0].edges[0..3]` (with `edges[1].evidence[0].supports: partial`) in `data/records/metacinnabar.yaml` via `scripts/curate_causal_graphs.py` (`curate_record_file`).
  - Minted append-only `EDIT` history sidecar:
    - `history/records/metacinnabar/2026-11-09T111134Z-marcin-d664eb.yaml`

### 3. `GRP-C11S5-003` (`cmmmech-cycle11-stage4-finding-0003` -> Issue [#969](https://github.com/CultureBotAI/CMMMech/issues/969))
- **Root Cause**: In `data/records/scandium.yaml` (`dong2024`), `mechanisms[0].protein_examples[0]` and `causal_graphs[0].nodes[0].protein_examples[0]` for `UniProtKB:C5B164` (`lanM` / Mex-LanM) asserted `supports: support` with `"mild acid stripping"` over `"competing transition/base metals"` whereas Dong et al. (2024) Section 3.4 and Figures 3C and 5E-F loaded a synthetic pH 3.0 16-REE chloride mixture and eluted Sc(III) at >99 mol% purity among REEs and >99% two-step yield (~94.5% Sc yield at 30 mM malonate in Figure 3C) using stepwise 30 mM and 50 mM malonate at pH 5.0 without a matched Sc-only resin-without-LanM control (`supports: partial`), and `causal_graphs[0].description`, `nodes[1..2]`, and `edges[0..1]` described the synthetic 16-REE chloride feed as a `"mixed leachate feed"` / `"multi-metal leachate"` with unqualified `supports: support` on `edges[0]`.
- **Remediation**:
  - Updated `mechanisms[0].protein_examples[0].evidence[0]`, `causal_graphs[0].nodes[0].protein_examples[0].evidence[0]`, `causal_graphs[0].description`, `causal_graphs[0].nodes[1..2]`, and `causal_graphs[0].edges[0..1]` (with `supports: partial` on `protein_examples[0]` and `edges[0]`) in `data/records/scandium.yaml` via `scripts/curate_causal_graphs.py` (`curate_record_file`).
  - Minted append-only `EDIT` history sidecar:
    - `history/records/scandium/2026-11-09T111134Z-marcin-689379.yaml`
