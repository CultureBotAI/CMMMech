# Round58 source investigation: mixed spent AA batteries

UTC 2026-10-12T13:25:04.578349+00:00. Curator: Codex /root/round27_packaging, GPT-6, codex. Base `b6014c43b8174904e80f71df22be2251a802b418`.

## Decision and owner

Curated `data/records/spent-alkaline-zinc-carbon-batteries.yaml` as a secondary resource. The primary experiment explicitly mixed discarded AA alkaline and zinc-carbon cells of different brands. Existing watch/button-cell, lithium-ion black-mass and NiMH records denote different feeds/studies. No separate owners for the two mixed AA chemistries and no constituent-element criticality are inferred. This dossier is a curation handoff, not an independent scientific review.

## Complete primary and identity

Falco, Martínez, Di Nanno, Thomas and Curutchet, 2014, *Latin American Applied Research*44(2):123–129, [DOI10.52292/j.laar.2014.429](https://doi.org/10.52292/j.laar.2014.429). Official publisher metadata and Crossref agree on2014-04-30. Received/accepted2013 and Crossref registration2021 are distinct dates.

All seven publisherPDF pages123–129, Figures1–7, Table1 and equations1–9 were personally visually inspected; full text and officialHTML read. OriginalHTML supplies17 images (7figures,1table,9equations), all acquired and inspected. PublicSciELO mirror has identical extracted text but different bytes; it is the same study. No article-specificSI was identified in the complete main/landing inventory. Primary SHA256 `8b34541f3ab6f4dc62e830ba0adc1a3f8fc3941bca0726f3e4f340f34efad0fa`. Original artifact paths and every byte hash appear in the pairedJSON.

FreshDSMZ confirmsDSM11478/Tth04 as *Acidithiobacillus thiooxidans*; NCBI930 is species-level. Collection identity does not authenticate the2014 stock. No material CURIE is invented for this mixed waste.

## Experimental scope

The upstream26.5Lair-lift sulfur reactor produced acid/polythionate medium using living culture at30degreesC. Replacing liquid without reinoculation is distinct from battery exposure. Downstream50Lvessel received2kg pretreated powder in28Lacid medium at pHnear0.4,200rpm, with fresh liquid replacement. These are source-defined pilot apparatus dimensions, not commercial deployment. Cell-free status of the leaching medium was not proven.

The record retains source-reported prepared-powder extraction, a weak commercial-acid comparison, incompleteMn mobilization, and a separate nonmicrobial6.5Lelectrolysis stage. It does not sum load bars, multiply stage efficiencies, infer absolute whole-battery yield or claim isolated pure-product yield. The record's two mechanisms are different stages of this one study.

## Original graphic coverage

- Figures1–2, pp.124–125: integrated flow and air-lift layout; casing/zinc can separated; stages visibly distinct.
- Figures3–4, p.126: acid-production steps and proton/sulfate/polythionate/free-cell time courses; late cell decline retained. These are not leaching replication estimates.
- Table1/Figure5, p.127: with/without-zinc-can composition columns and heterogeneousEDS; no selected whole-feed inventory reconstructed.
- Figure6, p.127: extracted-percent axis, although caption says concentration; first/second-load bars not summed. Main65%Mn versus abstract67% retained.
- Equations1–9, p.127: proposed chemistry inspected, not imported as demonstrated molecular pathways.
- Figure7, p.128: laminar anode-solidSEM; it does not establish purity or as-deposited crystalline phase. References/received/accepted dates onp.129 checked.

## Controls, contradictions and limits

- AA alkaline and Zn-C feed was mixed; no separate chemistry-specific performance. Table1 with/without zinc-can analyses are not unambiguously mapped to all outcome denominators. Whole-cell inventory is not reconstructed.
- Overnight drying printed150 degrees with no explicit unit letter. No leaching-stage temperature inferred from 30-degree culture production.
- Upstream sulfur culture and downstream powder leaching are separate stages. No demonstrated complete cell removal before leaching, live-cell contact necessity, or isolated polythionate causal control.
- Figure6 axis is percent although caption says concentration. Results/Conclusion Mn65% versus abstract67%; first/second bars not summed or cumulatively reconstructed.
- S1/S2 prose reports relative Mn60% and Zn40% increases but no underlying numerical series, matched evolving pH/composition, replication or uncertainty. These are not extraction efficiencies.
- Acid-production productivity calculations contain inconsistent percentage interpretations and KLa units; these optimizations are not recalculated or adopted. Sulfur mesh sign order differs between Methods and Conclusion.
- Late free-cell decline in Figure4 qualifies tolerance. Reactor-step n values are not independent leaching replicates.
- Electrolysis6.5L/68h has reported liquid-stage recovery36%Mn/66%Zn and current efficiency below10%; no multiplication to whole-battery product yield.
- Mn-oxide purity82%Results versus85%Conclusion; final pH1.8 versus1.5. MetallicZn90% source purity is not battery-grade qualification. Iron contamination/anode mass loss remain explicit.
- Mn2O3 is reported after500-degree-C calcination for residue and anodic solid, not directly assigned as-leached/as-deposited crystalline phase. Figure7 morphology is not purity or phase proof.
- Pilot wording is source-scale description bounded by26.5Lairlift/50Lvessel/2kgpowder. Five-year reactor installation statement does not establish five-year continuously verified battery recovery, commercial deployment or full cost/LCA advantage.

## Dedup and access boundaries

Hidden and ignored files plus relevant symlinks were included in current round58 and original Documents `data/records`, `research`, `reviews`, `history`. Initial bounded text scan examined8637 files including cited research/download roots. A supplementary ripgrep pass includes all existing normalized cited roots/standalone text files without the initial30MB cutoff; exact command, matches and unavailable-path classification are retained. Thirteen cited paths remain unavailable after normalization. BinaryPDF/images/spreadsheets are not decoded for this global text search, and unrelated temp/home trees are excluded. No accepted Falco2014 or mixed non-buttonAA owner was found within those bounds; Xin2012 references in existing raw texts are disclosed. This is not an assertion of globally novel science.

Official publisherHTML/images and publicPDF were acquired this session. A web-renderer login result differed from the fresh ordinary unauthenticatedGET, which redirected to the publicPDF; no authentication bypass occurred. SciELO is an independently available public mirror. Raw texts/figures remain outsideGit under `/private/tmp/cmm-round58-battery-research` under the recorded publisher rights (CC BY-NC-ND4.0 in metadata/footer).

Exact live discovery/notice queries, provider, date and first-result-set scope are inJSON. No matching notice was located, but some precise searches yielded irrelevant results; this is bounded negative evidence. Xin2012 fullmethods/graphics and a2013 thesis remain future overlap/extension checks, not accepted additional experiments.

## Frozen inputs and validation

- Record SHA256 `c05ce0a265b6b0a1afb54607bfce9239454db229e4263374fb29dfd639e369ce`.
- CREATE `history/records/spent-alkaline-zinc-carbon-batteries/2026-10-12T131959Z-codex-734d22.yaml`, SHA256 `4412468af70ef4267bbfc46565ca7a4da4f16b6f704efa4417768423294991e5`; distinct actual inlineCREATE attached.
- Named `uv run --locked cmmmech validate data/records/spent-alkaline-zinc-carbon-batteries.yaml` completedexit0:1checked,0failed. Exact command/cwd/log hash inJSON.
- Baseline reused the exact unchanged published-base receipt identified inJSON; no fresh baseline-run claim.
- Independent record review and parent cohort/publication gates remain separate. No other records, shared docs, Git or GitHub state were edited by this curation.
