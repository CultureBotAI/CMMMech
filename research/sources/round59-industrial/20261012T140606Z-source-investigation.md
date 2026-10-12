# Pyrite-roasting cinder source investigation

- UTC: 2026-10-12T14:06:06Z
- Curator: codex (GPT-6; codex), `/root/round43_hardmetal`
- Worktree: `/private/tmp/CMMMech-expansion-round59-20261012`; trusted base `d88bd5c0f89f9f2fcd80debfd9bd3a2b1a7786a5`.
- Decision: create only `data/records/pyrite-roasting-cinder.yaml`; independent acceptance review remains separate and pending.
- Record SHA256: `2f0285c341ab210862675b6e438ed7067234ecbaf4f074a0ee7a2b3799e51838`.
- Canonical CREATE: `history/records/pyrite-roasting-cinder/2026-10-12T140217Z-codex-e8c8b0.yaml`; SHA256 `701ae3803d3a003a02c9096a823255b5fbc90892bcf76947b9be8b9e7aee9060`.

## Material and experiment ownership

Roasting/calcination creates this secondary resource. Natural pyrite, unroasted tailings, slag, spent acid-production catalyst and downstream copper autoclave slime do not denote the same feed. The Turkish calcined ash and Portuguese weathered ash are separate experiments under one residue owner; compositions and results are not pooled. No criticality status is inherited from constituents.

## Original evidence and actual inspection

Ermurat2013, DOI[10.2225/vol16-issue2-fulltext-1](https://doi.org/10.2225/vol16-issue2-fulltext-1), was acquired as a complete 12-page [official SciELO PDF](https://www.scielo.cl/pdf/ejb/v16n2/a04.pdf). All 12 pages, all 5 figures, Table 1 and full methods/equations were personally inspected. The assay supports only qualified culture-associated sulfur solubilization. The publisher/Crossref/PDF disagree on March dates; year2013 is stable. The current publisher landing offers HTML/PDF galleys; no separate supplement was observed in that bounded inventory. No universal absence claim is made.

Pereira da Luz's [2025 public author deposit](https://scriptiebank.be/scriptie/2025/statistical-optimization-parameters-bioleaching-mine-wastes-sao-domingos-mine) supplies a complete 101-page master's thesis including appendices. It is not represented as a peer-reviewed journal article. The directly reviewed ash methods and results are printed 15–22,33–34 with Tables 4.3–4.9 and Figures 4.2–4.4/5.12–5.14. Visual page inventory: [1, 3, 4, 5, 6, 7, 8, 9, 26, 27, 28, 29, 30, 31, 32, 33, 34, 42, 43, 44, 45, 58, 59, 60, 63, 64] (one-based PDF pages). Relevant discussion/conclusion, adjacent crushed-pyrite confirmation and controls were also read. The complete figure/table inventories and appendix text were screened: separate crushed-pyrite/slag model outputs are not imported as ash data. Rendering other pages does not imply inspecting all 101 pages or every unrelated figure. No separate deposited SI was observed.

The thesis explicitly reports an unsuccessful transfer of the crushed-pyrite optimization to ash. Its graph/prose conflict prevents asserting an exact or statistically established null; that uncertainty is retained. No favorable slag percentage is transferred to cinder.

Five fresh official NCBI Info pages verify species names 4932/435/28034/178606/33059. They do not authenticate experimental isolates. The three acidophile pages agree with source DSM designation names, while the 2013 bakery/vinegar isolates have no strain deposit or sequence evidence.

## Evidence limits and contradictory observations

- 2013 lacks matched uninoculated/killed controls, full medium/substrate doses, inoculum/working volume/replicate/uncertainty and isolate sequences. Culture-associated sulfate release only; acid dissolution not separated.
- 2013Figure5 stacks separate25/35degreeCseries; combinedheight is not a single yield. TextmaximumSd/St0.5 preserved as source-reported, without independent recalculation or30degree outcome.
- 2013Fe ratios and specific-growth quantities are pH/ORP-derived models, not measured Fe speciation, growth or proven yeast/acetic-bacterium iron oxidation. No product or sulfur mass balance.
- Thesis ash SD-BIO-2 is roasted, weathered sulfate-rich residue, distinct fromSD-BIO-1slag andSD-BIO-3crushedpyrite. No uniformhematite composition inferred. Originalroasterparametersunknown.
- Thesis p34 prose saysMn/Sbnotabovechemicalcontrol butFig5.14shows visibly higherday9bioticSbbar and smallerMndifference. No errorbars or ash-specific significanceanalysis; no exact equality/statisticallyconfirmednull asserted.
- ThesisFig5.13Bday2ferrous excursion is large relative to54mMnominaladdition; Eq5variable-description reversesFig4.4axes; Eq7denominator/unitnormalization insufficientlyspecified. No ashpercentage or ironmassbalance adopted.
- Thesis Tables 4.10/4.11crossreferences do not match compositionTable4.9; Table4.8uncertainphaseflags retained. Trace-metalmediuminputs notblankcorrecteddocumented.
- Thesis ashcontrol calledabiotic butsterilitynotdemonstrated. Cellsobserved in separatecrushedpyrite/slagcontrolsshouldnotbetransferredtoash. Adaptation120rpm notsilentlyassignedtoashassay.
- Thesis failure of transfer fromcrushedpyritemodel is a bounded negative result, not proofallbiologicalcinderleachingfails or refutationofinaccessiblePandaresults.
- No measuredisolatedCu/Co/Znrecovery, purity, completebalance, economicviability or industrialmicrobialdeployment adopted. No criticality claim or mineral speciesID for mixedresidue.

## Deferred sources and repeatable follow-up

Panda2017 DOI10.1016/j.jhazmat.2016.11.050 and Panda2018 DOI10.1016/j.jhazmat.2017.08.038 are promising multimetal leads. This pass obtained official metadata/abstracts, not complete methods or graphics. The ElsevierAPI HTTP200 response is core metadata only, not full text. ResearchGate2017 is request-only; ScienceDirect403 and Crossref2017 initial429 are preserved. Their abstract percentages are not record evidence. Cui2017 DOI10.4028/www.scientific.net/KEM.748.451 is likewise landing/preview-only. Related KEM730.226 and Zuo2018 work need primary acquisition and experiment-overlap checks. The identity of the 2018Zuo paper remains a lead, not a verified adoptedDOI.

First acquire the Panda full originals and SI via legitimate institutional/author routes, then verify feed, community/strain, controls, rates/denominators and whether the 2018 reactor uses the 2017 ash/consortium. Second seek original replicate data/clarification for the 2013 missing controls and thesis graph/calibration inconsistencies. Third assess the Deerni papers together to prevent duplicate experiments. No author contact or access-control circumvention occurred.

## Search and deduplication scope

The paired JSON records exact queries, access results and hashes. Public web searches used first returned result sets, without comprehensive pagination. Exact-title/DOI correction and retraction searches found no relevant notice in those bounded results; this is not proof of no possible correction. The2013 Crossref relation was empty.

Pre-curation inventories used `rg --files --hidden --no-ignore -L` across original-checkout and round59 records/research/reviews/history, then bounded raw roots cited in those scientific texts. All 8 scientific roots were readable. The pass read 4436 scientific text files and 8484 total text files across 197 extant referenced raw directories. 9 missing older paths and 14 greater-than16MB file limits are enumerated in JSON. Text suffixes were MD/JSON/YAML/YML/TXT/XML/HTML, with realpath deduplication. No machine-wide or unextracted-binary absence assertion is made. The supplemental exact2013DOI/thesis-title scan uses the same bounded roots after writing the new owner, which is an expected match. Existing hits are bibliographic/context or unrelated review-gate wording; no prior accepted owner/experiment was found in these bounds.

## Provenance, checks and handoff

Raw originals remain outside Git at `/private/tmp/cmm-round59-industrial-research/raw`. The JSON pins 104 actual raw/derived artifacts and 11 receipts. Derived renders are individually distinguishable from original PDFs and explicit viewed-page scope above. Public availability does not establish redistribution rights:2013 publisher metadata links CC BY-NC-SA3.0 alongside copyright-transfer text; thesis reuse license is unknown. No originals are committed.

Named validation actually completed exit 0: `uv run --locked cmmmech validate data/records/pyrite-roasting-cinder.yaml`,1 checked/0 failed. Final receipt `/private/tmp/cmm-round59-industrial-research/named-validation-final.json` and log SHA `6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e`. An earlier external receipt used the wrong success substring and is preserved; final explicit subprocess exit supersedes its parser flag. No schema change or shared batch gate was performed by this curator. Root coordinates full validation and independent review. This source dossier is not scientific acceptance.
