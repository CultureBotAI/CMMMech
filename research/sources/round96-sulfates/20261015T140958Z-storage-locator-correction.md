# Sulfate dossier storage-locator correction

Recorded 2026-10-15T14:09:58.576987Z. Author correction, not independent acceptance.

The storage-check bullet now cites printed181/PDF7, where the original describes 295 K/55% RH storage and daily XRD/weight-loss checks. The earlier printed177/PDF3 locator was incorrect. Original paired dossier snapshots and D1 observation remain preserved. The paired JSON changes only its Markdown digest and byte count; the JSON had no duplicate storage locator. Both mineral owners and their CREATE histories remain byte-identical.

```diff
--- /private/tmp/CMMMech-expansion-round96-20261015/research/sources/round96-sulfates/20261015T135702Z-source-investigation.md (initial)
+++ /private/tmp/CMMMech-expansion-round96-20261015/research/sources/round96-sulfates/20261015T135702Z-source-investigation.md (corrected)
@@ -40,7 +40,7 @@
 - Current phase assignments: Table1 printed177/PDF3 gives ferricopiapite P-1 and rhomboclase Pnma; Tables2–3 printed178/PDF4 contain their coordinates/occupancies; Table5 printed179/PDF5 contains fit statistics.
 - Purity and composition: printed180–181/PDF6–7 and Table8. Conventional XRD did not show the ferricopiapite impurity that synchrotron XRD detected at d10.570 Å. The authors estimate at most 1% only crudely. Refined Fe1 occupancy 0.619(4) and bulk formula Fe4.78(SO4)6(OH)2.34(H2O)20.71 must not be equated with an ideal composition or exact purity. Rhomboclase was analyzed as (H3O)1.34Fe(SO4)2.17(H2O)3.06. The suggested interlayer excess-sulfate/proton accommodation is a proposal; the argument against trapped free acid is not direct proof.
 - Calorimetry: methods printed179/PDF5, thermochemistry/Table10 printed182/PDF8 and Table11 printed183/PDF9. The apparatus starts with 25 mL5 N HCl at298.15 K, but the cycle dissolves MgO before the ferric sulfate in the same solvent. Pellet mass12–18 mg is a range across materials, not a unique species loading. The sample-specific dissolution enthalpies are +74.20±0.22 kJ/mol (ferricopiapite, five measurements) and +15.07±0.16 (rhomboclase, seven); uncertainty is two standard deviations of the mean. These are per mole of analyzed Table8 formula, not molFe, kinetic rates or recovery percentages.
-- Storage checks: printed177/PDF3 describes 295 K/55%RH storage with daily XRD and weight-loss checks during experiments. Overall duration is not given; indefinite stability is not demonstrated.
+- Storage checks: printed181/PDF7 describes 295 K/55%RH storage with daily XRD and weight-loss checks during experiments. Overall duration is not given; indefinite stability is not demonstrated.
 - Thermodynamic limits: printed184–185/PDF10–11/Figure1 uses estimated entropy, calculated Gibbs energies and specified activities. The authors explicitly identify the ferricopiapite/rhomboclase boundary as metastable and distinguish sulfate versus bisulfate assumptions. It is not an observed environmental pH threshold.
 
 The second supplier ferric sulfate batch is phase- and water-content-distinct and did not reproduce all syntheses; a proposed grain-size explanation is not a controlled causal result. Table8 total high-temperature weight loss is not simply water content or mineral yield. Table14's caption points to Table5 for formulae while the formulae are in Table8; owner locators use the actual table. No organism enters either accepted experiment. General microbial pyrite oxidation in the introduction is contextual.
```

Exact before/after, source, original snapshot and initial-observation hashes are in the companion JSON. Independent successor remains pending.
