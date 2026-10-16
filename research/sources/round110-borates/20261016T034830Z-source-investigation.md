# Round110 borate source investigation

UTC: 2026-10-16T03:48:30.222688Z
Base: `0482e7b0af9b18685dabe310dbe86487b6ac4226`
Worktree: `/private/tmp/CMMMech-expansion-round110-20261016`
Author: codex (GPT-6; codex). This is a curation handoff, not an independent review.

Nobleite and gowerite add two distinct, currently approved borate species with original laboratory precipitation evidence. Neither inherits elemental criticality, microbial activity or industrial deployment. Current IMA formulas and special-procedure notations were checked in the official September 2026 list; the years are not unique approval identifiers.

## Evidence and admitted scope

| Owner | Primary evidence | Scope |
|---|---|---|
| `data/records/nobleite.yaml` | Erd, McAllister and Vlisidis 1961, AmMin46:560–571, complete 12-page original | Own CaO/boric-acid precipitation recipe and natural/synthetic powder comparison; natural chemistry kept separate. |
| `data/records/gowerite.yaml` | Erd, McAllister and Almond 1959, AmMin44:911–919; Konnert et al. 1972, AmMin57:381–396; Kyono and Yamaguchi 2025, DOI 10.2138/am-2024-9367, complete 33-page accepted manuscript | Historical stirred precipitation, separate unreplicated room-temperature crystal-growth route, and 120°C 12 h hydrothermal formation; no quantitative recovery or phase-purity claim. |

Nobleite uses 1.6 g CaO,10.0 g H3BO3 and 25 mL water,30 h stirring at48°C then 10 days at68°C. The original synthesis points to the wrong table: the comparison is Table 2, not Table 1. Preferred orientation limits intensity comparison. The original explicitly does not establish simple hydration/dehydration into gowerite.

Gowerite 1959 uses 20g calcium acetate monohydrate,40g boric acid and 100 mL water,35°C with continuous stirring for 24 h and initial/final pH around 5. Its18-day unstirred room-temperature arm is separate. The 2025 authors report failure to reproduce that single-crystal route. Their own hydrothermal experiment uses 1.00 g H3BO3,0.476 g CaCl2·2H2O,0.129 g NaOH and 10 mL water in a 28 mL autoclave at120°C for 12 h; cooling, filtration and drying are recorded in the owner. The selected crystal supports phase identity; bulk powder Figure S1 and refinement Tables S1–S2 remain unavailable. Hotter, longer or more alkaline preparations yielded priceite, but endpoint observations do not directly show a dissolution sequence or intact solution-unit inheritance.

## Inspection and limitations

All cited originals were read in full. Nobleite's12pages and its figures/tables were visually checked. Gowerite 1959 figures, powder table, chemistry table and synthesis pages were visually checked. Gowerite 1972 provenance, atom table, figures and structural comparison tables were inspected. The 2025 manuscript methods, null replication, Figures 1–2 and Tables 1–3 were inspected. The published version and original supplements were not acquired after bounded legitimate access attempts. The accepted manuscript's fixed-O–H wording and variable Table 2 distances need the actual refinement instructions for quantitative reuse.

The 1972 crystal is explicitly natural; a secondary synthetic-data label is not adopted. Hydrogen sites were not located in 1972 and were distance-constrained in 2025. Thermal narratives partly repeat older unacquired reports and warn of possible boric-acid loss. No water-only decomposition yield is inferred. An apparent nobleite optical contradiction was an OCR error resolved by the page image before curation.

## Bounded search and provenance

Hidden and ignored files were included and relevant symlinks followed across worktree records/research/reviews/history/skills, original-main reports and cited borate raw roots 101–109. Initial candidate search returned 126 tokens in 27 context files and zero current owners. Final identity/reference search includes the just-created owners and generic nonunique special-procedure years; it is not an exhaustive global inventory. The 148 open issue title/body inventory had no selected-material/DOI match; comments and closed issues were not inspected by this agent.

Raw matches, full PDFs, acquisition receipts, page images and web results remain outside Git in `/private/tmp/cmm-round110-borates-research`. This paired JSON stores only bounded summaries, file paths, sizes and hashes, addressing the compact-evidence requirement from issue 445. It does not embed recursive matches or full text.

## Checks and handoff

The baseline receipt records `just check` PASS at 03:41:30Z for this base/worktree. Named validation reports two records checked and zero failed. No schema change was needed; abiotic precipitation uses the existing `other` process. Parent batch gates and independent native scientific reviews are pending at this authored snapshot.

One source follow-up is drafted at `/private/tmp/cmm-round110-borates-research/source-followup-gowerite.md`: obtain the 2025final/supplementary evidence, clarify H-refinement instructions and the failed room-temperature route if primary documentation exists. It does not require changing the currently qualified observations. The detailed JSON binds exact owner/history hashes and raw-source provenance.
