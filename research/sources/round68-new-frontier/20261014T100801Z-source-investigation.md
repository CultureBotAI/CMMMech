# CMM source investigation: silicate microbial dissolution frontier

## Scope and provenance

UTC 2026-10-14T10:08:01.773342+00:00; Codex GPT-6, `/root/round68_new_frontier`.
Checkout `/private/tmp/CMMMech-expansion-round68-20261014`, branch `curate/cmm-expansion-round68-20261014`, base `e8a5f936607481446e4897e3bf2e0d10f0556632`.
Root confirmed the baseline pass before curation. Two new maintained owners were selected for direct controlled evidence and clear species identities: wollastonite and diopside. A null or modest effect is useful evidence and was not converted into an extraction success. No criticality designation was assessed or inherited.

Hidden/ignored-inclusive, symlink-following `rg --no-ignore --hidden --follow` searches covered records, research, history and reviews for all candidate names and resolved study DOIs. Relevant prior downloads were searched as extracted text/metadata under `/private/tmp/cmm-round67-new-frontier-research`, `/private/tmp/cmm-round18-dunite-raw` and `/private/tmp/cmm-round17-enstatite-raw`; current downloads were inventoried. No earlier wollastonite or diopside owner appeared in that bounded corpus. Antigorite already occurs as a constituent of the dunite feed, which does not prove a separate mineral mechanism. Binary-only unextracted content and unrelated home/temp trees were not exhaustively searched; this is not machinewide absence or exhaustion evidence.

## Search and acquisition log

All live searches used the web search provider on 14 October 2026 UTC, first result batches only, with no date filters or pagination; query-specific site restrictions appear literally below. Full URLs and acquisition metadata/checksums are in the accompanying JSON. Search snippets were used only to locate originals.

- `tremolite actinolite microbial dissolution bacteria fungal original study`
- `tremolite iron bioweathering Streptomyces microbial`
- `"microbial" "wollastonite" dissolution fungal`
- `"microbial" "antigorite" "2022" oxalate`
- `"microbial" "tremolite" iron fungi dissolution Rozalen`
- `"Actinobacteria-mediated serpentine dissolution" pdf`
- `"Mineralogical Characterization" "Caldenno" actinolite tremolite 2018`
- `"10.1016/j.chemgeo.2021.120697" pdf`
- `"Liu" "serpentine" "FXJ8.102" pdf`
- `"wollastonite" "Pokrovsky" "2009" pdf`
- `"Comment" "Effect of organic ligands" "Berner" 2010`
- `"10.1016/j.chemgeo.2021.120697" repository OR ustc OR supplementary`
- `"wollastonite" "Pokrovsky" correction retraction 2009`
- `site:ajsonline.org "Berner" "2010" "424"`
- `site:ajsonline.org "05.2010.05"`
- `"Weak impact of microorganisms" pdf`
- `"10.1038/s41529-021-00199-w" supplementary`
- `"10.1038/s41529-021-00199-w" correction OR retraction`
- `"Pseudomonas aureofaciens" "NCBI" taxonomy`
- `"Pseudomonas reactans" "NCBI" taxonomy`
- `"Chaetomium brasiliense" "F-3649"`

The publisher API route for the 2009 PDF returned HTTP 403; the normal article PDF succeeded. Nature web-open returned an internal error, but normal HTTPS downloads supplied the full HTML, original PDF and linked supplement. The supplement was acquired before a subsequent Handbook request failed with HTTP 406. A redundant Springer CDN retry failed DNS resolution; the supplement was already available locally. Handbook downloads then succeeded with a normal user agent. Official NCBI XML and the VKM catalogue were acquired, although some browser opens failed. The September 2026 IMA official PDF was reopened live; retained round 65 bytes supplied visual row inspection. The ScienceDirect full-text route for antigorite returned HTTP 403. Metadata, abstract and bounded repository searches did not supply its methods or supplement, so no antigorite record was created.

## Source inventory and assessments

| Source | Role and inspected evidence | Decision |
|---|---|---|
| Pokrovsky et al. 2009, DOI 10.2475/08.2009.05 | Original 42-page PDF; bacterial methods printed 734–735 and 739; results 754–756; original Figures 5–6, Table 3 and Appendix 2 visually checked; discussion, conclusions and ligand context read | Curate narrow live/dead wollastonite assay; no pooled effect or rate import |
| Berner 2010, DOI 10.2475/05.2010.04, and author reply, DOI 10.2475/05.2010.05 | Complete one-page comment and two-page reply | Preserve published disagreement about extrapolation; no claim of retraction |
| Pokrovsky et al. 2021, DOI 10.1038/s41529-021-00199-w | Complete 10-page primary, all five figures, Tables 1–2, both pages of the original supplement | Curate separate bacterial flow and fungal batch contexts under diopside |
| IMA September 2026, PDF pages 57 and 235; Handbook diopside/wollastonite entries | Official names, formulas, status and definitions; complete Handbook entries | Species grounding; special-procedure years are not fabricated accessions |
| NCBI 117680/587851; VKM F-3649 | Official XML names, ranks and synonyms; exact collection entry | Name and strain-code context only; no authentication of the experimental culture or genome |
| Vigliaturo 2018, DOI 10.3390/min8120557 | Original 24-page deposited PDF; methods and EPMA context, Table 1 and Figure 3 on PDF pages 8–9 visually checked | Tremolite/actinolite deferred: specimen lies at the compositional boundary; no duplicated species outcomes |
| Liu et al. 2022, DOI 10.1016/j.chemgeo.2021.120697 | Publisher metadata and abstract only | Antigorite lead; acquire original methods, figures and supplement before curation |

### Wollastonite

Natural CaSiO3 identity is supported by IMA and the Handbook. PsB-03 is a source-named soybean-rhizosphere isolate. NCBI maps the historical name to the current subspecies but does not independently identify that isolate. Live/dead comparisons used EPS-rich SP and EPS-poor SA cultures, nutrient solutions or 0.01 M NaCl, 25 degrees C, 120 rpm and up to seven days. Heat-killed biomass has microbial origin without metabolic activity. The plotted contrasts are not a complete set of matched biomass-free dissolution controls. Methods describe eight condition combinations; independent biological replication is unclear. Filtered aqueous release and fitted surface-normalized slopes are not recovered products.

The record retains important source conflicts. Methods give 0.5 g per 250 mL but also state 2.5 g/L. Figure 6 SP pH 7.3–6.5 differs from the generic Table 3 pH 7.2–8.2. Figure 6 labels SP silica in ppm and SA silica in mM. Table 3 silica rates do not transparently produce the quoted 37/55 percent exceptions or a pooled enhancement. Some individual live curves increase faster, so a universal null assertion would be wrong. The record retains the authors' overall uncertainty interpretation while excluding exact effect estimates. Berner's comment and the reply restrict generalization to basalt, aluminosilicates and field biota; no global pH-only explanation or CO2 benefit is imported.

### Diopside

The primary identifies natural Fe/Cr-bearing diopside and separate assays. Bacterial 25 mL flow reactors sequentially received sterile medium, 0.54 then 3.85 g wet cells/L, then sterile medium, at 25 degrees C with MES or bicarbonate and optional 10 percent broth. The species name is verified; the strain accession remains unassigned. Paired timepoints are not independent reactor replication. Fungal 19-day batches used F-3649: live biomass with or without 1 percent Czapek and dead biomass without nutrient, in duplicate, with 1.3 g mineral per 250 mL at pH 6.13–6.50. There was no matched dead-plus-nutrient arm. Filtered Ca/Mg/Si analyses and fitted rates do not establish isolated recovery.

Table 1 includes nutrient MES pH 7.80–8.05 despite Figure 2A and supplement labels of pH 6.1. D3/D4 endpoint rates do not show a universal three-to-five-fold decline, despite the broad prose claim. Supplement plots exhibit early baseline drift and later changes. AFM coverage is compatible with proposed passivation but does not establish its molecular cause or remove aging as a confounder. Methods' statements of four to five days/five volume replacements and 24 hours for steady state disagree. Modest fungal Si enhancement coexists with unchanged Mg and variable Ca. Results mention etched or rounded edges while the Discussion broadly denies dissolution features. Figure 5a is described as dead fungus in Results but sterile/no fungus in the image and caption. No uniform enhancement, universal null effect or causal passivation factor is assigned. The supplement lacks raw replicate data; fungal biomass labels differ slightly from Table 2. These source gaps remain explicit in the maintained YAML.

### Deferred sample identities and new frontiers

Vigliaturo 2018 Table 1/Figure 3 and the cited 2020 preparation method trace Choi's tremolite-actinolite to Passo di Caldenno. Mg/(Mg+Fe) values of 0.86–0.90 approach or straddle the naming boundary; the source calls it tremolitic amphibole. Assigning the same 2023 result independently to two pure species is unsupported. Prepared natural crystals do not establish a new waste or resource identity. The Choi supplement issue remains the prior round's follow-up, not a new experiment or duplicate issue here.

Antigorite is a concrete next lead. The Liu 2022 publisher abstract identifies Streptomyces FXJ8.102 and secondary glushinskite, but unseen methods, figures and supplement preclude accepting its experimental conditions, mechanism or causal extent. Other references encountered but not assessed include the Lee and Fein 2000 gibbsite study (DOI not verified in this pass), hornblende siderophore studies and a 2026 Talaromyces calcium-magnesium silicate study. These are research leads, not accepted records or evidence of exhaustion.

## Reuse, data and limits

Reading access to the 2009 AJS paper and 2010 comment/reply does not establish redistribution permission; retained full texts stay outside Git. The Handbook states all rights reserved. IMA states CC BY-SA 3.0; the 2021 Nature article states CC BY 4.0 and links its supplement. VKM/NCBI reuse terms were not comprehensively audited. No bulk dataset or dictionary was ingested. Rate plots and tables do not satisfy the schema's mg/kg concentration-observation contract; no numeric observations or schema changes were fabricated. The 2021 data statement makes other relevant data available from the corresponding author on request. No author contact was made.

## Priorities and curation handoff

1. Independently review both frozen owners and retained primary artifacts; complete corpus, history and review gates before acceptance.
2. Resolve the 2009 loading, unit and rate-summary conflicts and the 2021 pH, endpoint and control-label contradictions from original run-level metadata or a formal correction. Exact kinetics remain uncurated meanwhile. A source-follow-up issue draft goes to root for deduplication and publication.
3. Acquire the Liu 2022 original and supplement for antigorite, then inspect organism and specimen identity, controls and outcomes. Do not substitute its abstract for mechanism evidence.
4. Investigate additional uncurated silicate identities from cited original studies, keeping hornblende/labradorite series and mineral-species boundaries explicit.

Named validation completed with exit code 0: `uv run --locked cmmmech validate data/records/wollastonite.yaml data/records/diopside.yaml` checked two records with zero failures. Canonical CREATE histories at 10:05:51Z and 10:05:54Z are attached. Root coordinates final batch gates; this discovery dossier does not claim independent acceptance. Raw source/artifact hashes and exact record hashes are in the JSON.
