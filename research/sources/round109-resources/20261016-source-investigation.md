# Round109 secondary-resource investigation

UTC 2026-10-16T02:49:25.124816+00:00; codex /root, GPT-6. Base `a11e47d1c90806e056bd60610a0edd2cf77813a9`; worktree `/private/tmp/CMMMech-expansion-round109-20261016`.

Copper anode slime is selected as a distinct refinery residue, separate from elemental copper, a mineral species and downstream copper autoclave slime. The accepted claim is comparative laboratory abiotic acid-chloride leaching of real Guixi-smelter material. No criticality, microbial mechanism or industrial deployment is inherited.

Primary source: Zeng Y, Liao C, Liu F, Zhou X (2023), *Occurrence Behaviors of As/Sb/Bi in Copper Anode Slime and Their Separation by Compound Leaching Followed by Stepwise Precipitation*, ACS Omega8:10022–10029, [DOI](https://doi.org/10.1021/acsomega.2c07251), PMID36969429, PMC10034837 version1. Complete original XML acquired through [EuropePMC](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10034837/fullTextXML). Online10March; issue21March2023. CC BY-NC-ND4.0; copyrighted originals remain outside Git.

## Evidence inspected

Complete main text, methods/results/conclusions, Tables1–4 and all figure captions. Original Figures1–5 and graphical abstract were visually inspected, with file-to-figure correspondence from original JATS. Equation1 was acquired from the public CDN and inspected. Figures1–4 establish heterogeneous feed/sample characterization; Figure5 provides comparative leaching plots, including zero-added-chloride controls. No plot digitization or numerical reconstruction was adopted.

Selected leaching conditions:4M sulfuric acid,120g/LNaCl,70C,2h,10mL/g. Figure5a/b salt/acid series instead80C. Drying conditions, sample mass, vessel volume, stirring speed and replicate counts are unavailable. Table3 reports within-element phase distribution, not mineral mass fractions. Modelled complexation is not directly observed solution speciation.

## Acquisition limits and narrowed scope

- ACS article/PDF403; PMC article/PDF routes recaptcha HTML, not article/PDF.
- EuropePMC asset ZIP timed out at240s with687067bytes; complete individual entries recovered using raw-deflate EOF and original ZIP CRC/compressed/uncompressed length verification. No incomplete image retained as evidence; archive remains explicitly incomplete.
- Range retrieval first failed sandboxDNS, permitted retry returnedHTTP500. Full-size Figures6/7 remain unavailable. Their captions/text were read, and graphicalabstract contains miniature product labels, but these do not substitute for original full-size pattern inspection.
- Accepted mechanism narrowed to leaching before final owner freeze; precipitation assignment and models are attributed context_only.

The source's precipitation narrative and Table4 were read. However, the accepted mechanism was narrowed to leaching before scientific-review capture. Full-size Figure7 assignments remain attributed context; no accepted oxychloride recovery or phase-purity assertion. Figure6 is a model, not measured precipitation.

## Adversarial accounting

Table1 gives Cu21.43,Sb5.805,Bi2.868,As5.569wt%. Conditional on the same feed,10mL/g and unchanged volume, elemental maxima are21430,5805,2868,5569mg/L. Table4 initial concentrations25880,29450,28050,24000mg/L exceed these. This is a conditional diagnostic of an unresolved relationship, not a corrected yield. Unreported intermediate concentration or a different feed could matter; neither is documented. Exact assumptions/source hash are in `conditional-mass-balance.json` externally.

The reported92.72%As,99.98%Sb,89.13%Bi,90.31%Cu leaching and>98%Sb/Bi precipitation are explicitly source-reported and not adopted as independently reconciled overall recovery. Unknown NaOH volumes and product masses prevent closure. H+0.8/0.2g/L is not pH; finalSb<5mg/L is not zero. Arsenic stabilization and copper recycle are proposed downstream uses only.

## Discovery and duplicate coverage

W and original main records/research/reviews/history/skills and ignored publication reports plus cited raw57,74(actualpvroot),102; rg --no-ignore --hidden --follow, bounded and cycle-safe through declared roots. Context/deferred mentions exist but no dedicated owner in inspected corpus. All-state GitHub inventory316 issues includes titles/bodies, not comments.

Bounded exactDOI/title correction/erratum/retraction queries; no affecting notice surfaced in returned windows. No exhaustive absence claim or author outreach. Crossref relation/update metadata checked; archived version not independent replication.

Prior reports57/74/93 and cited raw context were read. The wrong guessed raw74path was corrected to the actual cited pv-research root; a missing guessed path was not treated as a negative result. Raw search outputs and exact public acquisition requests/outcomes are retained in the paired JSON artifact manifest. Discovery is not exhausted.

## Follow-up

Acquire full-size Figures6/7 and any attributable clarification of Table1/Table4 feed and volume accounting before accepting precipitation recovery. Other phosphating, salt-slag and tailings leads remain deferred until primary evidence is accessible. Independent scientific review and final batch validation follow; this curator dossier is not its own acceptance verdict.
