# Spent nickel-cadmium battery resource: source investigation

Recorded 2026-10-12T14:04:39.527817+00:00 by Codex (GPT-6; codex), task /root/round27_packaging.
Trusted base `d88bd5c0f89f9f2fcd80debfd9bd3a2b1a7786a5`; worktree `/private/tmp/CMMMech-expansion-round59-20261012`.

## Accepted scope

Created `data/records/spent-nickel-cadmium-batteries.yaml` as a secondary resource, with one narrow culture-associated cathode-leaching mechanism from Sedlakova-Kadukova et al.2017, DOI [10.1515/amm-2017-0226](https://doi.org/10.1515/amm-2017-0226). End-of-life NiCd active powder is distinct from existing NiMH, alkaline/Zn-C, button-cell and Li-ion black-mass owners. Cathode extraction is not an intact-battery yield. No criticality, external material identifier, isolated product or industrial claim is inherited.

The official complete eight-page PDF was freshly acquired, not silently reused. All original pages1459–1466, six figures, Table1 and eight equations were inspected. Figure2A/B and Methods2.1–2.4/Results3.1.2 are the accepted NiCd evidence. Figures1,3–5 concern other feeds; Figure6 is a proposed model. Table1 is prior literature. No article-specific supplement was identified in the full paper and accessible official issue listing. The DOI landing returned an HTTP200 browser challenge, not full text; no bypass was attempted. Crossref429 is retained. Public reading access does not establish redistribution rights; fulltext and images remain outside Git.

## Conditions and limits

The cells were opened, rolled electrodes separated, active material removed from grids and ground below40µm. The cathode had6.5%Cd/47.1%Ni; the anode had38%Cd/22.2%Ni. Results assign Figure2 to cathode. The setup states2g powder,200mL medium,250mL flask, initialpH1.5,5mL pure inoculum,28-day sampling and triplicates. Five-mL filtered leachate samples were analyzed by AAS. No full denominator/sampling-balance equation, NiCd temperature/agitation, strain accession or original replicate dataset is supplied.

Methods names pure A.ferrooxidans/9K, while Figure2 caption names a mixture with A.thiooxidans. NCBI920 is a species mapping, not a resolution of that contradiction. Abiotic ferric sulfate and dilute sulfuric acid are real comparators. Cd approaches reported100% in both biotic/ferric treatments. The abstract/prose say55%Ni, but original Figure2B is near45–47%; no harmonized numerical yield is adopted. Partial Ni and comparable biotic/ferric performance are supported. No microbial superiority or live-cell necessity is established. The malformed hydrated ferric reagent formula prevents conversion of stated44.63g/L reagent to elementalFe.

The proposed ferric oxidation/hydrolysis explanation is qualified. Figure5 is LIB pH, not a NiCd trajectory. A closed-loop process in Figure6 is proposed, not demonstrated deployment. References20–21 overlap authors with earlier NiCd work; full originals remain unavailable and study independence is not asserted. Reference21's printed2014 conflicts with bibliographic discovery of2013; no data are imported from its abstract.

## Dedup and source search

Searched current and original Documents scientific directories `data/records`, `research`, `reviews`, `history`, including hidden/ignored files and followed symlinks. Initial corpus/raw inventory read 8798 retained-text files; supplementary uncapped `rg --hidden --no-ignore --follow` searched 237 normalized cited raw roots/files. The original directory was readable. Thirteen normalized cited paths were unavailable and are listed in JSON. PDF/image/binary spreadsheet contents were not machine-decoded during raw-root dedup; selected original PDFs were fully inspected separately. Unreferenced temp/home directories were excluded.

No existing NiCd owner or accepted exact-study match was found in this bounded scope. The sole maintained hit was a historical round24 NiMH search string. Raw hits include general policy/chemistry mentions, later NiMH mislabeling context, Falco2014's reference to Cerruti1998 and Kordloo2026's reference to a2025 chemicalNiCd paper. These were not mistaken for the accepted 2017 experiment. Exact DOI/source strings, commands, paths, errors and hashes are retained. No machine-wide absence claim is made.

Exact live queries and first-result limits are in paired JSON and raw web receipts. DOI/title correction/retraction/erratum searches returned no relevant notice within that limited scope; this is not proof that none exists. NCBI920 freshly resolves the stated species.

## Same-owner extension assessed and deferred

Netpae and Suckley, DOI [10.22104/AET.2021.4759.1286](https://doi.org/10.22104/AET.2021.4759.1286), is now available as a complete official six-page PDF. All pages167–172, both multipanel figures, both tables and references were inspected. This Thai recycling-shop NiCd/A.niger ATCC1015 study would extend the same owner, not justify another CREATE. It is not an accepted record mechanism this round.

The paper describes0.3g/80mL,28±2C,150rpm,42days, three named media,7-day pregrowth for two-step treatment and no-fungus controls, but control results and exact medium recipes are absent. Tables use mixed `Mg/g`/`mg/g` labels and initial assay denominators; no complete mass balance is reconstructed. The claimed day21 maximum (Ni81.41%,Cd92.31%) is exceeded by later table rows. Printed2020 issue metadata precedes received/accepted2021. Organic acid association is not citrate-specific causal proof, and several background/method reference assignments are weak. Fresh ATCC1015 and NCBI5061/380704 checks corroborate named culture identity only. A later EDIT should address these control/time/denominator questions explicitly. Official landing declares CC BY-NC4.0; raw stays outside Git.

Other actionable followups are full Velgosova2014/2013 originals for experiment overlap and phase-specific dissolution, and Cerruti1998 fulloriginals for the separate indirect-acid arm. The Chinese2005 official landing remains a discovery lead. No lead-acid-paste original was accepted from the bounded search. These are source gaps, not defects invented in accepted records.

## Files and validation

- Record SHA256: `3ab36654c99842e481666088f5cf0b402ba7a2598ffb4bea8a448af021deeffe`.
- Canonical CREATE: `history/records/spent-nickel-cadmium-batteries/2026-10-12T140131Z-codex-21a6a4.yaml`, SHA256 `e1f5208076d0adda92ded1db6fd2bd9e7afd8ab86a282b35bee54feb8820c1c3`; separate actual inline event attached.
- Actual named validation: `uv run --locked cmmmech validate data/records/spent-nickel-cadmium-batteries.yaml`, exit0,1checked/0failed; log hash `6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e`.
- 31 raw artifacts and 12 receipts pinned in paired JSON; raw root `/private/tmp/cmm-round59-battery-research`.
- Baseline reuse is parent-reported exact unchanged published state; this curator did not rerun global gates.

This is author research and curation. Independent scientific review and final corpus/publication gates remain parent-coordinated; no Git/GitHub or shared-document changes were performed here.
