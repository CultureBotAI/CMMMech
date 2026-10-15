# Round93 source investigation: thallium

UTC 2026-10-15T10:31:23.406244+00:00; researcher codex /root; base `e0bffe8eb1c6e359f35d9c52c74a95a4efdc2b9d`. Source handoff, not an independent acceptance review.

## Identity and selection

Thallium is a new element owner grounded to current ChEBI30440, not Tl(I), dorallcharite or a secondary resource. The primary experiment provides controlled evidence of culture-associated mobilization accompanying iron reduction. NCBI319224 maps the reported CN32 strain. No criticality claim is curated. Maintained records, research, reviews and history were searched using `rg --no-ignore --hidden --follow`; the only match was an incidental hash substring. Relevant prior source archives and current downloads were inspected. This bounded search does not claim a machine-wide or literature-wide absence.

## Accepted evidence and access

[Smeaton et al2012](https://doi.org/10.1021/es302292d) has verified DOI, authors and journal identity. Direct final article routes returned403. The accepted full primary route is [author dissertation Chapter4](https://www.collectionscanada.gc.ca/obj/thesescanada/vol2/002/NR78584.PDF), printed113–148/PDF138–173, and [official ACS SI](https://doi.org/10.1021/es302292d.s001),13pages. All3 main figures and all4 SI tables/6 official SI figures were inspected visually, plus the extra thesis K/Mg/Ca figure. These are versions of one experiment, not independent studies or proof of byte identity to final typesetting. The local thesis basename is misleading; its author/title were verified as Smeaton2012.

## Mechanism and experimental limits

Washed living CN32, autoclaved cells and cell-free controls were compared with synthetic nonideal Tl-bearing jarosite in anaerobic28°C, lactate/PIPES tubes. Triplicate destructive samples share culture preparation. Fe(II) accumulation and higher filtered Tl support culture-associated mobilization, but substantial abiotic dissolution and different pH trajectories remain.32°C refers to prior aerobic growth. Filtered ICP-OES Tl is not a directly speciated ion or isolated product.

A separate35µM Tl/0.1M NaCl72-hour assay reports no significant between-arm sorption difference near pH5/6.2–6.3. TableS1 captions, pH assignments and significance notation conflict. This result cannot rule out sorption at the millimolar dissolution-assay concentrations or in other organisms/settings. Source cell-count conversions and ATP-proxy prose assignments also disagree; no count or ATPase function is reconstructed.

The main formula uses(OH)5.22(H2O)0.78 but SI prints(OH)6; no pure mineral species is inferred. Nominal893-hour endpoints coexist with853/863-hour passages. PIPES masks sulfate release; some TableS2 inputs are stoichiometric estimates despite its heading. FigureS5 local Tl/S/O enrichment has an O/Fe caption error and does not establish a stoichiometric sulfate product. Fe/O spots and geochemical saturation indices do not identify crystalline phases. No closed inventory, recovery yield, direct Tl reduction or industrial deployment is established.

## Search and handoff

Paired JSON retains actual query strings, first-result-set coverage, API metadata, acquisition failures, hashes and reused-versus-new files. No applicable correction surfaced in those returned results or Crossref relation/update fields; this is not an exhaustive absence claim. Other dissertation chapters and jarosite studies remain separate leads. The frontier is not exhausted.

Source clarification should resolve formula, sorption labels/statistics, biomass and time assignments, and particle/phase inventory before broader claims. Raw dissertation and source graphics remain outside Git. Official SI metadata statesCCBY-NC4.0; author dissertation redistribution is not assumed.
