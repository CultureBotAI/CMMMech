# Smithsonite source investigation

UTC: 2026-10-12T13:26:17.662692Z

Worktree: `/private/tmp/CMMMech-expansion-round58-20261012`; trusted base `b6014c43b8174904e80f71df22be2251a802b418`. Curator: codex, GPT-6, codex. This is an author curation handoff, not independent scientific approval.

## Accepted owner and evidence

`data/records/smithsonite.yaml` identifies the mineral smithsonite, Zn(CO3), separately from zinc, dissolved ZnCl2 and mixed oxidized zinc ore. The current IMA September 2026 row (page 201; definitions page 1) is grandfathered G/1832, not a numbered approval. The complete official Handbook datasheet supplies natural occurrence context. No criticality is inherited.

Huang, Zhang and Zheng's *Comparison of the efficiency of traditional MICP and two-step MICP method for immobilizing heavy metals in aquatic environments*, DOI10.1016/j.bgtech.2024.100106, is an original ten-page paper, online 25 May 2024 in Biogeotechnics 3 (2025) 100106. The official HEP PDF was acquired successfully and every original page, all four figures and both tables were personally viewed. Figure 2U was additionally recropped without clipping. The full text, original PDF and images stay outside Git at `/private/tmp/cmm-round58-mineral-research/raw`; the paired JSON pins every artifact and acquisition receipt. The article is CC BY-NC-ND4.0. No separate SI was identified in the inspected article/official landing inventory; the paper states data are in the article.

## What the record supports

The traditional20mL tube assay uses a reported Bacillus pasteurii BNCC337394 suspension, urea and separately prepared ZnCl2 solution. Current NCBI1474 maps that species name to Sporosarcina pasteurii, but does not authenticate the experimental stock. Figure 1 shows culture preparation/washing; detailed medium/cultivation are delegated to the unavailable Huang2024 main methods. Neither that recipe nor physical assay temperature is invented;30°C is the model setting. Triplicates and initial OD600about1.0/urease4–5U/mL are stated in the original.

Figure 2U and Section 3.2 assign the traditional10mmol/LZn/100mmol/Lurea precipitate to smithsonite, using PDF08-0449ZnCO3. Section2.2.1(3) explicitly dries it at105°C, grinds/sieves it to0.1mm and keeps it dry at40°C. The supported observation is a qualitative prepared-solid assignment; no wet-state or heating control, phase fraction, purity or isolated product yield is shown. No matched uninoculated/killed/no-urea/pH-matched experimental control is reported in the program.

Equation 1's denominator is initial aqueous metal concentration. At stated100mmol/Lurea, Section 3.1.4/Figure 2M gives99.89%removal at1mmol/LZn and40.67%at10mmol/LZn after24h. These are solution depletion endpoints, not smithsonite yields or kinetic rates. Atomic absorption/Nessler methods, unspecified separation cutoff/detection limits and weaker model agreement are retained. Model carbonate is assumed from ammonium, not independently speciated.

Figure 4D–F is a different50mmol/Lurea experiment, varying the delay beforeZnaddition while fixing total elapsed time at24h. The Znexposure duration therefore varies. No XRD for those sequential products is supplied. Figure 4E's10mmol/Lcurve is not strictly monotonic to8h despite generalizing Section 3.3 prose; no uniform100%or mineral-yield claim is admitted.

## Deduplication and acquisition boundaries

Both the current worktree and original Documents checkout were searched in data/records, research, reviews and history with hidden/ignored files included and relevant symlinks followed.217 referenced raw roots were extracted,193 were available, and24missing roots are individually listed in JSON. Material/formula and historical DOI patterns were followed by the exact accepted DOI/title/BNCC experiment search. No accepted owner or matching experiment was found in that boundary; existing smithsonite mentions concern mixed oxidized zinc ore and deferred literature. Binary suppression/noOCR and non-machine-wide scope are explicit. Both exact-search logs and receipt hashes are retained.

The fresh NCBI1476 probe was rejected as the wrong species;1474 is correct. A guessed BNCC337394 route returned a404page withHTTP200 and is not collection authentication. Swęd2021 DOI10.1016/j.apgeochem.2021.104966 and BaasBecking/Moore1961 DOI10.2113/gsecongeo.56.2.259 remained inaccessible at bounded official routes. A complete Wolicka/Borkowski paper (printed2014, despite retained filenamewolicka2013.pdf) cites the latter; its citation is a lead, not original support. The historical1962comment literature has not been adjudicated. Prior Ilyas2012 mixed ore is already deferred and not retried or transferred to the mineral.

Bounded live searches for the accepted DOI/title plus correction, erratum, corrigendum and retraction returned no affecting notice; Crossref fields also showed none. This is not an exhaustive absence claim. Referenced Huang2024 cultivation methods remain the most direct source gap.

## Provenance and checks

Record SHA256: `35d845d7a0ae5608ed5a7c37e7e35b6928e330ef968a3cb65c9cc1bdd9883e85`.

CREATE: `history/records/smithsonite/2026-10-12T132345Z-codex-ba48e7.yaml`; SHA256 `d197dd7e86e617ff3f2a0de33d712255026cf63fe1b4006d7f77c33be5ffb376`. The inline event is separate and uses actual UTC. No prior record/history is edited.

Named validation `uv run --locked cmmmech validate data/records/smithsonite.yaml` passed with1 checked / 0 failed in the explicit round 58 worktree and temporary UV cache. The initial schema-key failure and one cache-environment failure are preserved outside Git and are not called passing checks. Shared final gates and independent review are coordinated by the parent.

The paired JSON has 39 raw artifact entries and 17 receipt/log entries with SHA256s, exact access URLs and search bounds. Raw originals remain outside Git; no source exhaustion or industrial performance is asserted.
