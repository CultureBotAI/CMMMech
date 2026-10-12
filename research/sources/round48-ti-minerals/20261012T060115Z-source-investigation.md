# Round48 titanium-mineral source investigation

UTC: 2026-10-12T06:01:15Z. Author: codex / GPT-6 / codex (`/root/round27_packaging`). This is a curation handoff, not independent scientific acceptance.

Worktree: `/private/tmp/CMMMech-expansion-round48-20261012`; trusted base `9b397b1f215381208c3381b175b3da8b6fe31399`.

**Decision:** curate one rutile mineral record with a qualified photocatalysis and microbial iron-cycling association. Keep ilmenite issue #104 and the 2015 rutile-concentrate study deferred.

## Identity and inspected evidence

The [September 2026 IMA list](https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf), PDF page 189, identifies rutile as TiO2, grandfathered status G, original-description year 1803. Definitions on page 1 distinguish that year from an approval identifier. No `IMA:1803` was invented. This species differs from other TiO2 polymorphs, manufactured nanoparticles, elemental titanium and rutile-bearing concentrates.

[Lu and colleagues (2012)](https://doi.org/10.1038/ncomms1768), *Nature Communications* 3:768, published 3 April 2012, is the accepted primary study. The complete official eight-page PDF, publisher HTML, all seven original figures and original twelve-page supplement were acquired. The indexed university PDF returned 404; the successful PDF came directly from the publisher. All eight original main pages/Figures 1–7 and all twelve supplement pages/Figures S1–S2/Table S1 were personally visually inspected. The main article has no numerical tables.

Raw files are under `/private/tmp/cmm-round48-ti-research/raw`:

- Main `lu2012.pdf`: SHA256 `611696cb5a6d1cd16d81a0562dfd7115e411b10489f639686c8b11e1a239bb4e`.
- Supplement `lu2012-si.pdf`: SHA256 `e766391dde2092ad8d6b9d32169c10910913b0f79c6e795325ae1a1e8db4ec0e`.
- Original-page renders are in `lu2012-pages` and `lu2012-si-pages`; seven original figure JPGs are retained separately.
- Paired JSON pins all 43 raw artifacts, authority receipts, acquisition times, URLs, failures and checksums.

The main PDF retains the 2012 Macmillan all-rights-reserved notice. Bulk originals remain outside Git. The IMA document states CC-BY-SA 3.0 on page 2.

## Experimental claim and boundaries

Methods call the coating natural rutile, with average powder diameter 40 micrometres. They do not supply a locality, chemical purity or diffraction-based specimen phase-purity determination. The coating used 0.54 g mineral and 0.06 g acetylene black with approximately 0.3 mL PTFE and ethanol, spread on 5 by 7 cm graphite and air-dried for 12 h. The 350 mL photocatalytic chamber contained 12.5 g/L ascorbic acid and 2.5 g/L KCl. A membrane and external wire/1000 ohm resistor separated it from the 350 mL microbial chamber, containing growing *A. ferrooxidans* and m9K with 41.7 g/L FeSO4·7H2O. Medium iron was the Fe feed; rutile and cells remained spatially separated. Ascorbate was a supplied chemical hole scavenger, so light/rutile were not the sole supplied sources of reducing equivalents.

Final inoculum was 3.5e5 cells/mL, 10% v/v. Temperature remained near 30 degrees C, with magnetic stirring. The supplement's 150 rpm refers to enrichment, not reactor stirring. Isolation medium was adjusted to pH 2.2 plus/minus 0.02; no reactor pH trajectory is supplied. Figure 2 follows four days at 380–760 nm and approximately 13.5 mW/cm2. Figure 4 separately varies wavelength or intensity. Cells were directly counted, not measured by the CFU procedure used for another organism. Exact replicate numbers and error-bar definitions are missing.

Figures 1, 2 and 4 support conditional sustained growth associated with photocurrent and Fe cycling. The authors interpret regenerated Fe(II) as supporting further microbial Fe(II) oxidation. Controls also initially grow using supplied iron. At 420 nm, growth rises from 2 to 8 mW/cm2 but falls at 16 mW/cm2. This laboratory association does not demonstrate rutile transformation, Ti extraction, an enzyme pathway or industrial deployment. The record uses `process: other` to avoid implying Ti transformation.

## Uncertainties retained

1. Figure 2 labels a comparator both rutile-free and open circuit, whereas Methods specify a mineral-free anode without its circuit state. These factors cannot be cleanly separated. The caption's about-fivefold statement has no specified time-point denominator; no numerical enhancement factor is adopted.
2. The cell-free control substitutes 6.1 g/L ferric chloride for ferrous sulfate, changing initial iron speciation/concentration. Figure S2 shows additional rutile-free/dark controls, but its axis says Fe(III), while the experiment is discussed for Fe(II) generation. These curves are not treated as interchangeable sterile counterparts.
3. The primary article describes Shanxi acid-pit water. Fresh GenBank `HQ603786.1` instead says `isolation_source="soil"` and names strain HZ-PKU-1. Its 1495 bp partial 16S sequence and the verified species identifier `NCBITaxon:920` do not establish a functional gene or reconcile the origin.
4. The 2.1 micrograms/L Ti(IV) value is calculated from solubility, not measured release. Photon/biomass efficiencies depend on model assumptions. SI page 8 alternates oxidation/reduction wording, but page 9 explicitly multiplies the oxygen-consumption rate by 60 h: no missing time-conversion defect is inferred. Page 10 gives roughly 3500 and then 2531 mg/L medium Fe(II) consumption for the 36–96 h interval. Efficiencies are not adopted.
5. Figure 4b labels current density mA/m2, Figure 4d mA/cm2; SI refers to C-chamber graphite area while main prose refers to rutile-electrode area. No numerical current-density result is adopted.
6. Other mineral and organism experiments were inspected, but not pooled. The soil study uses applied voltage to simulate light in the absence of sunlight; its Table S1 light/dark heading and voltage labels do not establish rutile-specific field causality.

## Searches, deduplication and deferred work

The paired JSON logs exact queries/providers and returned-result coverage. Exact DOI correction/erratum/retraction and title/control searches, the publisher page and Crossref relation/update fields revealed no specific notice in this bounded pass. This does not prove none exists. Citation leads PMC8456820 (salt-marsh rutile colonization) and PMC6410676 (rock varnish) remain unreviewed future work.

Dedup used `rg --no-ignore --hidden --follow` across current and original `data/records`, `research`, `reviews`, `history`, and 173 existing referenced raw roots. A cycle-aware inventory read 3702 textual metadata files; nine unavailable historical roots and all commands are recorded in JSON. Search covered material names, DOI fragments and HQ603786. No existing rutile owner or accepted Lu2012 experiment was identified within that boundary. Titanium and titanium-metal are different owners. Hidden/ignored files and relevant links were included; binary files were not automatically decoded and no machine-wide absence claim is made.

[Issue #104](https://github.com/CultureBotAI/CMMMech/issues/104) remains open. Newly inspected Mahidol entity/full metadata and author-publication routes did not expose the missing main articles. A new public bundles API and direct author-page request returned 403. Old blocked Wiley/Cambridge PDF attempts were not repeated. Complete articles for DOI 10.1002/apj.1663 and 10.1017/S1473550412000493 must still establish feed identity, methods and controls, and reconcile the preliminary 2010 versus journal 2013 outcomes and experiment overlap. The prior original Cambridge supplement checksum was reverified (`1dc1002a67861250af78acaf1cac2ca08e53351f315e70c7bff134be49532055`); its scientific assessment remains explicitly inherited from round31, not freshly repeated in full. Rutile does not resolve issue #104.

The [2015 rutile-concentrate bio-desilication study](https://doi.org/10.1016/S1003-6326(15)63855-9) remains abstract/metadata only. No HY-7 taxon mapping, TiO2 grade or recovery measurement was adopted. An unverified exploratory TNMSC paperView route failed and is not a canonical citation. Complete feed origin, strain/mutagenesis, controls, denominators and original figures/SI are prerequisites for any later concentrate record.

## Handoff

- `data/records/rutile.yaml`: SHA256 `42b825d1ad84f74dd587edc0651d66838bd282027714116d75b79068a599b73b`.
- CREATE sidecar `history/records/rutile/2026-10-12T055843Z-codex-ffbafe.yaml`: SHA256 `41d405c6b22942b1a0e915ca28f46af75275209f31601c641df46faa87df30ed`.
- Named validation passed: one record checked, zero failed, terminal exit 0. Receipt: `/private/tmp/cmm-round48-ti-research/named-validation.json`.
- Baseline is the parent's disclosed reuse of the fresh identical published base. Independent scientific review and full cohort gates are parent-coordinated and remain pending in this handoff.
- This contribution changed no existing record, schema, governance or README and made no remote mutations. Raw originals remain outside Git.
