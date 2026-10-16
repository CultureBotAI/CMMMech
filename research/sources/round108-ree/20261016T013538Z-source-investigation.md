# CMM source investigation: lanthanite-(La) and lanthanite-(Ce)

UTC: 2026-10-16T01:35:38.003695+00:00. Researcher: codex, GPT-6, codex; agent `/root/round104_ree`.
Worktree `/private/tmp/CMMMech-expansion-round108-20261016`, branch `curate/cmm-expansion-round108-20261016`, trusted base `26661b7f033d4bdb915e48e71080aa5774b4c3d6`.

## Scope and decision

Two distinct mineral owners were added with bounded abiotic transformation evidence. Neither inherits criticality from its element, nor a microbial process from another mineral or generic carbonate. Synthetic phase fractions are not extracted-metal yields. The parent verified baseline PASS before maintained edits. Named strict validation passed for both files; independent native reviews and final batch gates remain pending at this dossier timestamp.

The paired JSON is the detailed search/acquisition log, original-artifact manifest, claim matrix and condition/uncertainty handoff. Raw originals are retained under `/private/tmp/cmm-round108-ree-research` outside Git. Hidden and ignored files and relevant symlinks were included in the declared corpus/history/reviews/research, original-main ignored reports and round104–107 REE raw-root searches. Context mentions are acknowledged; the search was not machine-wide. Issue title/body inventory covered307 all-state rows; comments were excluded. No matching owner/source issue was found within that stated scope.

## Candidate inventory

| Source | Actual inspection | Decision |
|---|---|---|
| IMA-CNMNC September2026, definitions p1 and rows p121 | Fresh official homepage, downloaded PDF and visual rows | Ce approval1983-055; La renamed1987s.p., no fabricated approval CURIE |
| Bevins et al.1985, American Mineralogist70:411–413 | All3pages, Figure1, Tables1–3 | Natural Ce identity, mixed chemistry and probe limits |
| Atencio et al.1989, DOI10.1180/minmag.1989.053.373.17 | All4pages, Table1, Figure1 | Reclassification and locality caution; distinguish new analyses from literature compilation |
| Terribili et al.2025, DOI10.1021/acs.cgd.4c01168 | All18publishedpages, complete XML, original Figures1–14, Tables1–5, all8SIpages | Selected La thermal/water arm and Ce35°C phase progression |

## Natural and synthetic identities

The current authority lists La2(CO3)3(H2O)6·2H2O and Ce2(CO3)3(H2O)6·2H2O. La's renamed1987s.p. row retains Sweden, while the1989 paper's Bastnäs B10531 analysis is Ce-dominant. Its Curitiba literature data span La/Nd dominance. No universal reassignment from locality is defensible. The1985 Ce original gives mixed natural chemistry and explicitly reports probe/sample deterioration; its diffraction pattern alone cannot distinguish lanthanite members. The2025 processing experiments use separately synthesized single-REE carbonates, not those natural specimens. Experimental La/Ce tengerite-type products are not assigned unverified natural-species identifiers.

## Mechanism evidence admitted

La: Methods p948 heats2g synthetic lanthanite in a lidded50mL crucible at80°C, sampling0.2g. Figure10 reports tengerite-type material after7h. A0.3g product portion is then placed in a15mL reactor filled with Milli-Q water at21°C, static; reactor capacity is not a specified water dose. Figure12 shows89wt%lanthanite and11wt%tengerite at120.5h. TableSI-1 also lists both phases. This supports partial return at the sampled endpoint, while eventual completion, equilibrium and comparable forward/reverse activation energies remain unverified. No replicate count or phase-fraction uncertainty is supplied for this separate arm.

Ce: Methods p946 mixes40mL50mMCe nitrate with40mL50mMNa2CO3, seals the glass reactor and holds it static at35°C. Five-mL suspension samples are0.2µm-filtered, isopropanol-rinsed and air-dried; TOPAS Rietveld analysis provides crystalline phase fractions. Table2/Figure2b agree at24h(66/34lanthanite/kozoite),192h(7/86/7lanthanite/kozoite/cerianite) and865h(100cerianite among quantified crystalline phases). These are one-reactor results, not a complete Ce mass balance. The5°C arm retains lanthanite alone over sampled28–147h, constraining generalization. Dissolution-recrystallization and oxidation are proposed causal explanations; a controlled oxidant comparison was not supplied.

## Contradictions and excluded extensions

The La text's broad final-completion wording exceeds Figure12's120.5h endpoint. Ce35°C526h fractions differ between Table2(1/71/28) and Figure2b(2/71/27). Ce50°C145h differs between99%cerianite+1%kozoite in Table2 and100%cerianite in Figure2c. La80°C72h differs between93/7 in Table1 and94/6 in Figure1d. These disputed endpoints were excluded. The SI-2 turbidity axis labels seconds despite times resembling minutes relative to Table5; WAXS prose and Figure5 timing also differ. No kinetic rates, digitized timings or complete-conversion claims are taken from these disputed passages. The exact discrepancy matrix is in the JSON. Limited phase/refinement uncertainty, no organism and laboratory-only scale remain explicit.

## Search, rights and remaining work

Exact query objects and UTC acquisition receipts are preserved in the paired JSON. Initial two search queries were recorded, but their first raw provider response was not retained; later selected sources have direct provenance. Correction/retraction and contradictory/microbial searches found no affecting formal notice in returned results, not proof of universal absence. Generic fungal carbonate/oxalate leads do not establish either exact mineral's microbial mechanism. Unchanged blocked routes#397/#405/#406 were not retried; separate2015Nd issue#421 remains unresolved.

The2025 published article statesCCBY4.0; its official ACS Figshare supplement metadata statesCCBY-NC4.0. EuropePMC's downloaded supplement bytes exactly match the official SI. Older originals have public reading access but no verified redistribution grant. OriginalPDFs/figures stay outside Git; maintained artifacts contain curated facts, locators and checksums.

Priority1: resolve2025 phase-fraction/time/rehydration conflicts with original data or author clarification before broader kinetic claims. Priority2: reconcileLa historical/type-locality and natural specimen provenance against current IMA authority. Priority3: reassess the2025Nd arm for the existing owner separately; it does not automatically resolve2015#421. The existing schema supports this work without changes.

## Frozen owners and validation

- `data/records/lanthanite-la.yaml` SHA256 `ffba6de0e9dd8b228659c7b623c463711f3970b373865c9d049dbc0b80889aeb`; history `history/records/lanthanite-la/2026-10-16T013309Z-codex-a2893c.yaml` SHA256 `17e12b77b042a50daff947a5758a1e3746b76c61f9adbd055937143588a46a9d`.
- `data/records/lanthanite-ce.yaml` SHA256 `af5d8468a74e6e252c316f46b3229eb7555be1cf32f71e4fe16a6e8fa217bad4`; history `history/records/lanthanite-ce/2026-10-16T013320Z-codex-a7120f.yaml` SHA256 `489b84268abc274425ab9482d89e62c8d9ca501113be02d642a0905745ceddf3`.

Named validation: `uv run --locked cmmmech validate data/records/lanthanite-la.yaml data/records/lanthanite-ce.yaml --require-records`, exit0, `Checked 2 record(s); 0 failed.` No independent acceptance or final batch PASS is claimed here.
