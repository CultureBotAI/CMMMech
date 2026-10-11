# Molybdenite source investigation

## Scope and provenance

UTC: 2026-10-11T19:50:00.143682+00:00. Researcher: codex (GPT-6; codex).
Worktree: `/private/tmp/CMMMech-expansion-round32-20261011`; branch `curate/cmm-expansion-round32-20261011`; trusted base `09c15cbfb7699e40ae4648b6b414784a00b488db`.
This investigation concerns the natural MoS2 mineral species and a controlled mixed-specimen experiment, not elemental Mo, soluble molybdate, a commodity, or manufactured MoS2. No criticality jurisdiction/list claim is proposed. Source roles are mineral identity, microbial assay and species context. Source years span 1974–2026 in a bounded survey; this is not an exhaustive history.

The selected 2007 experiment is valuable because it supplies a supported limited-leaching result with original controls, not because it promises high recovery. The record is `data/records/molybdenite.yaml`; CREATE history is `history/records/molybdenite/2026-10-11T194752Z-codex-f27d24.yaml`. This report is the curator's evidence handoff, not independent scientific acceptance.

## Search and acquisition log

Search provider: web search tool, first result sets on 2026-10-11, no date filters or pagination. Exact queries are preserved in the paired JSON. Publisher/DOI, official taxon, IMA and institutional routes were followed; index snippets were used only to find originals.

- Complete publisher primary: [Química Nova PDF](https://quimicanova.sbq.org.br/Content/pdf/Vol30No5_1095_07-AR06093.pdf), actual public download 19:42:07–19:42:09 UTC, HTTP 200, 182013 bytes, SHA-256 `a457841e8795cc456dd09b3fb9c66dde7f083ed8ae9b7bb63c120fcc17050823`. The web-open route returned 403; a separate ordinary download succeeded. An earlier sandbox attempt had DNS failure; it is not an unavailable-source conclusion.
- [UNESP original main plus SI](https://repositorio.unesp.br/server/api/core/bitstreams/4a0fec08-6d23-49aa-b365-0eff66bd691f/content): acquired 19:44:06–19:44:07 UTC, HTTP 200, 261981 bytes, SHA-256 `dbab73ee9ceaaf8648c94e79fe5b8007d79d1b5acf394c5917113cb16a6655db`. Six pages; first five extracted pages match publisher text exactly, last page is original supplement S1. All original main figures 1–6 and SI figures 1S–2S were inspected visually.
- [Crossref DOI metadata](https://api.crossref.org/works/10.1590%2FS0100-40422007000500008), [NCBI 920](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=920&mode=Info) and [publisher issue](https://quimicanova.sbq.org.br/default_periodicidade.asp?ed=60) were acquired successfully at 19:44 UTC; exact times, URLs, response types and checksums are in acquisition-2.json and the paired dossier.
- The dated September 2026 IMA original is a byte-identical local reuse, not a fresh download. Original acquisition was 2026-10-11T17:41:04.402075Z; this round copied it from round31 stibnite raw and inspected page146 and definitions. SHA-256 `2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973`; copy receipt and provenance chain retained.
- [University synthetic-sulfide thesis](https://repositorio.unesp.br/bitstreams/4d64f58e-f5f3-401d-ad4f-09ea41c6543d/download): complete96-page PDF acquired 19:42 UTC, SHA-256 `b03c239a3f19cd432d1a5e9771c87f061b4f5e4033332ea59fd9fbfaa8a36f89`. Rendered all pages, but only title/contents and relevant keyword sections inspected. It is explicitly a synthetic MoS2/CuS study and is not natural-mineral corroboration.
- Brierley government report `https://stacks.cdc.gov/view/cdc/234441/cdc_234441_DS1.pdf`: web-open rejected oversized content; one direct acquisition returned403. Romano2001 OUP original PDF `https://academic.oup.com/femsle/article-pdf/196/1/71/19107774/196-1-71.pdf`:403. Neither full primary was inspected. No unchanged retry loop was used.

Raw originals and rendered pages remain outside Git under `/private/tmp/cmm-round32-molybdenite-research/raw`. All retained raw paths, bytes and SHA-256 values are enumerated in the paired JSON, together with acquisition failures. IMA page2 states CC BY-SA3.0. Other article/thesis redistribution terms were not verified; public reading access is not treated as redistribution permission. No bulk dataset is claimed or imported; quantitative concentration-cell schema is inapplicable to these prose assay results.

## Duplicate and source-family assessment

A successful `rg --no-ignore --hidden --follow` search covered476 declared current/original corpus and prior referenced non-cache raw roots, including round31 research and this raw directory. It searched mineral names, Portuguese synonym, formula and relevant DOI fragments across records, research, reviews and history, with hidden/ignored files and relevant symlinks included. Available extracted text/metadata were searched; PDF, raster, Office and archive bytes were excluded, with accepted originals read separately. No machine-wide absence or OCR completeness is asserted. One UTF-8 decoding failure was corrected using replacement decoding; final search exit0, no stderr,322 matching lines/84 paths. Full commands/boundaries and output checksum are retained in `/private/tmp/cmm-round32-molybdenite-research/dedup.json` and the paired JSON.

Existing `molybdenum.yaml` concerns the element and soluble molybdate reduction, explicitly excluding molybdenite. `metalliferous-black-shale.yaml` explicitly excludes its source's separate molybdenite-concentrate arm. No existing record for this mineral or the2007 experiment was found within the successful search boundary. Publisher and university copies plus S1 are one experiment, not independent replication. The2006 thesis has related same-group conference entries, but its declared experimental material is synthetic; overlap is not counted as replication.

## Accepted primary assessment

Francisco Jr., Bevilaqua and Garcia Jr., Química Nova30(5):1095–1099 (2007), [DOI10.1590/S0100-40422007000500008](https://doi.org/10.1590/S0100-40422007000500008). Crossref matches authors/title/pages and year. The printed article says online2July2007 while Crossref has October2007; year2007 is used without inventing a day-level reconciliation. Crossref has empty relation metadata and no correction/update assertion. Exact-DOI correction/retraction search and the inspected publisher issue/PDF identified no affecting notice within those routes; this is bounded, not exhaustive.

Identity: official IMA September2026 page146 states Molybdenite, MoS2, statusG, year1796. Page1 definesG and the year as the original-description year, not an IMA approval accession. A search-result1807 shorthand was rejected after checking the original row. NCBI920 verifies Acidithiobacillus ferrooxidans at species rank only. LR has no authenticated strain identifier in this dossier.

The specimen was commercial natural ore-grade material from Ward's, not pure MoS2: less than0.2mm, bulk0.8wt%Mo/34.0wt%Fe/23.0wt%S, initial XRD molybdenite/pyrite/pyrrhotite plus unidentified Cu-mineral peaks (p1095,Figure5). Supplier Rochester is not a mine provenance. LR came from acidic uranium-ore liquor at LagoaReal,Bahia and was adapted to mixed sulfide. Flask method p1096:250mL vessels,150mLmedium,2.5%w/vore,120°C30min autoclaving,5%v/vinoculum,150rpm,30±2°C,43day reported time course; biotic ±30mmol/LFeII and corresponding uninoculated controls, plus ferric control. Full cited medium recipe, flask replication, inoculum count/washing and initial pH are not printed. The triplicate washed resting-cell respiration experiment is distinct and cannot fill those gaps.

Main outcome p1098: Mo in centrifuged supernatant was below2mg/L in all assays by ICP spectrometry (subtype unspecified). This is censored concentration, not zero, a recovery percentage or total-Mo balance. Figure6 shows22day residues; authors attribute lost iron-sulfide peaks in biotic arms to preferential removal while molybdenite persists. XRD is qualitative, not absolute mineral consumption. Persistent molybdenite at43days is reported for both arms; biotic final patterns are explicitly data-not-shown. Original SI Figure2S provides only43day uninoculated patterns.

Contradictions/limits retained in the YAML: the p1098 sentence asserting no mineralogical changes in inoculated22day samples conflicts with the adjacent description and conclusions. It is not silently corrected to 'uninoculated.' Methods call ferric sulfate30mmol/L, while captions state30mmol/LFeIII; exact addition basis remains ambiguous. Early pH rose toward4 and acid corrections occurred over roughly15days, followed by different trajectories and eventual1.7–1.9; these are not matched dynamic-pH controls. Galvanic protection/high rest-potential is an author explanation, not directly measured. Mixed-feed respiration and its fittedKm/Vmax cannot establish MoS2 oxidation. No complete product balance, improved concentrate grade or industrial deployment was demonstrated.

## Deferred and context candidates

| Candidate | Evidence actually inspected | Decision |
|---|---|---|
| Romano2001, DOI10.1111/j.1574-6968.2001.tb10543.x (Elsevier alias10.1016/S0378-1097(01)00039-8), selective chalcopyrite leaching of molybdenite concentrate | Official metadata/abstract; original PDF403 | Obtain complete methods/figures before adopting any mineral-specific extraction values. Different feed/experiment. |
| Nasernejad1999, DOI10.1016/S0032-9592(99)00067-9 | Original publisher abstract and2007discussion only | Important possible higher-Mo-release counterexample under distinct conditions; reported abstract yield is not adopted. Weekly residue-washing details are2007secondary reporting, not verified1999methods. |
| Olson and Clark2008, DOI10.1016/j.hydromet.2008.02.013 | Citation lead only | Acquire original primary to assess redox/Fe conditions; no measurements adopted. |
| Brierley1974 DOI10.1016/0022-5088(74)90107-6 and government report | Primary abstract/metadata; report blocked | Thermophilic lead, not methods-verified; no transfer of organism or yield. |
| Francisco synthetic2006thesis and2009 DOI10.1590/S0100-40422009000600022 | Thesis title/selected sections;2009metadata only | Manufactured MoS2 context; separate source-family/overlap assessment required. |
| Lu2026 Minerals16,197, already retained under historical filenamezhao2026 in round28raw | Relevant primary method/results text for separate concentrate arm, not fresh full mineral-assay review | Follow-up priority, not duplicate current mechanism. Method10%pulp/10%inoculum/pH1.4/9K/WZ-Q differs; results prose refers to aqueous concentration while Figure4 caption uses residue composition. Do not infer recovery from normalized residue percentages. |
| Jordisite surfactant study DOI10.13374/j.issn2095-9389.2018.07.004 | Search discovery only | Distinct mineral identity, not molybdenite; outside this accepted record. |

## Priorities, validation and handoff

1. Independently review the frozen molybdenite record against the originals and source contradictions; parent runs cohort gates. Single-file validation completed at 2026-10-11T19:48:26.324559+00:00, exit0, one checked/zero failed. Record SHA-256 `1fcf52ffb9a97856e1cb92358755f86801d9741dd2493a9c3a8e499a94884a3a`; history SHA-256 `83c28c85d96658de53ea2b1bffffe8f98a92199716b68e12bc844cdcdac9b180`. No schema change was needed.
2. Assess the already available Lu2026 separate concentrate arm with full original figures/controls, then obtain Romano2001/Olson2008 for conditional comparison. Preserve feed identities and measurement denominators.
3. Acquire Nasernejad1999 complete primary to resolve its reported contrast; do not treat the2007 null as universal mineral behavior. Resolve flask replication, ferric addition basis, original22day wording and missing final biotic XRD only with authentic additional evidence.

No new dataset ingestion, organism accession, criticality status or molybdenum recovery measurement is invented. This source report does not replace the required saved independent scientific review.
