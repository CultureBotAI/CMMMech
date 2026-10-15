# Round 95 source investigation: heterosite and alunite

Researcher: codex /root/round68_phosphates (GPT-6; codex). Scientific acceptance is assigned to an independent reviewer and is not asserted by this dossier.

## Scope and provenance

The bounded selection adds heterosite and alunite as distinct mineral identities, with useful primary abiotic transformation/extraction evidence. Neither organism activity nor constituent-element criticality is claimed. Work is in the isolated round95 checkout at trusted base `73d4b1c42541ee7ca139effae00b94ddb1c8a631`. Root's actual clean-baseline receipt passed before maintained curation; no baseline or broad suite was duplicated here.

Hidden/ignored-inclusive, symlink-following `rg` searches covered `data/records`, `research`, `reviews`, `history`, and specifically referenced raw roots round93-minerals, round92-minerals and round64-lithium/raw. Heterosite already appears as a reclassified oxidation product in triphylite's round93 study, and alunite occurs as group/association context in other mineral records. Those references do not own these identities. The newly selected Reich2024 and Zhong2019 studies were not found in these bounded maintained/referenced roots before this curation. No whole-home or whole-temporary-directory search or global exhaustion claim is made. Exact query logs and match-path inventories are bound in the JSON. The all-state issue snapshot was searched for the two names and DOI endings; matches, if any, are listed there.

## Search, acquisition and versions

Searches on 2026-10-15 used the exact queries in the paired JSON. Initial network requests failed DNS in the restricted shell; read-only network retry acquired original bytes, with failures preserved. Reich et al. (2024), DOI10.1016/j.desal.2024.117883, was acquired as the complete eighteen-page publisher edition from KIT, whose landing page labels CC BY4.0 and deposit DOI10.5445/IR/1000172429. The initial local mnemonic `klein2024.pdf` was wrong: its author is Reich; `reich2024.pdf` is a byte-identical correctly named copy, not another edition. Direct ScienceDirect HTML returned403. Guessed DOCX/PDF supplement routes returned404; the actual publisher XLSX succeeded and is accepted.

Zhong et al. (2019), DOI10.3390/met9030337, was acquired in two publisher files: an older fourteen-page PDF and a current thirteen-page `-v2.pdf`. Current claim locators use v2, and both originals remain unchanged externally. The official one-page SI was acquired and visually inspected. The publisher notes page returned403; the file version is not misrepresented as a verified formal correction. Bounded exact-DOI correction/retraction searches surfaced the existing articles/notes, but no separate formal correction was identified in inspected results; this does not establish that none exists.

Eventoff1972 was acquired as the complete seven-page original from RRUFF. Its printed Table1 is a separately deposited structure-factor listing, NAPS01668, not contained in the paper; it remains unacquired. Tables2-4 and Figure1 are visible and were inspected. No independent re-refinement is claimed. Current Handbook entries were acquired. The live CNMNC homepage links the September2026 list; downloaded bytes equal the previously acquired round93 list, with fresh provenance retained. Nomenclature2023 is an honestly reused original from round93, not an independent transformation experiment.

Raw articles, workbook, original images and source-derived text remain outside Git. KIT/Reich and Zhong publisher originals state CC BY4.0; Handbook material carries its publisher's restrictions, and Eventoff redistribution terms were not independently established. Only original curation/metadata are maintained.

## Heterosite: accepted scope and limits

Current IMA row page93 gives Fe3+(PO4), grandfathered,1826; the year is not a new approval identifier. Eventoff's natural Fletcher Quarry specimen is approximately(Fe0.65Mn0.35)PO4 with an effectively vacant lithium site. The modern nomenclature retains heterosite and discredits ferrisicklerite/sicklerite. The earlier2013 oxidation lineage remains explicitly cross-linked to triphylite instead of being advertised as a new study.

Reich2024 uses commercial carbon-coated IBUvolt LFP400, not natural heterosite ore. Figures1-4 and Table1 support a synthetic heterosite-structure product after persulfate delithiation, with residual Li1.7mg/g, nonideal composition, shifted peaks and an unidentified64.35-degree reflection. A pure FePO4 yield or full mineral purity is not inferred. Selected0.1MNa2S2O8 preparation released about42-43mgLi/g precursor withinone minute; water and alternative reagents provide controls with different chemistry and some different durations.

Lithiation studies separate pureLiCl, pretreated iron-depleted natural Bruchsal brine and synthetic Neustadt-Glewe-like brine. They use thiosulfate and laboratory quantities. Natural-brine kinetic uptake about23mg/g afterthreehours is distinct from isotherm24-27mg/g at2.5-5g/L. Synthetic-brine kinetic1mg/g differs from its isotherm1.3mg/g at2g/L/fourhours. The pure-LiCl60/80-degree seven-day null is retained, with thiosulfate instability/pH changes preventing a simple temperature-only interpretation. Long treatments releaseFe/P and accumulateNa/S; gypsum and sulfur are identified. These are limits on stability and selectivity, not an isolated lithium-product yield or industrial-cycle result.

The complete official workbook has14sheets and no formulas or embedded images. All worksheet layouts/method labels and selected supporting/control/censoring cells were inspected via native ZIP/XML, preserving raw values. The source does not use one analytical basis throughout: kinetic Li columns are fluidOES, while the two brine-isotherm Li columns are digestionOES. The separate experimental and digested masses are retained. Bruchsal sheet`Fig.10, Fig.11a+b` K9/K10 are about26.76/23.68mg/g; synthetic sheet`Fig.10, Fig.11c+d` M11 is1.317mg/g. High-loading residual cells encoded0 or<LOQ are not proof of exactzero. Zero-sorbent blank rows carrying load-labelled numerical entries have unexplained normalization; the record does not manufacture a closed mass balance or replace their calculations. All fourteen sheets are the same study's supplementary values, not independent replications. No attempt to revalidate every cell or fit is claimed.

## Alunite: accepted scope and limits

Current IMA row page9 gives KAl3(SO4)2(OH)6, redefined1987s.p.; the natural mixed ore from Zijin Mining Group is independently supported by SI FigureS1 (alunite/quartz/kaolinite) and oxide chemistry. It is not presumed a specified waste stream or pure mineral. Methods use1gore, variedCaO ratios, nitrogen heating600-900degreesC/twohours, then water leaching30degreesC/onehour at1:10g/mL. Figure1 supports source-reported approximately81% solubleK at700degreesC andCaO/ore0.1 versus approximately27% withoutCaO at that temperature. It does not support a universal benefit at every temperature. HigherCaO can coextract moreAl.

The evaporation product is a separate0.2-ratio700-degree experiment; Figure4 assigns mixedK2SO4/CaSO4/K2Ca2(SO4)3 and Table1 reports40.42wt%K2O equivalent. This is neither40.42wt%elementalK nor pureK2SO4 nor81%isolated-product yield. The name syngenite used forK2Ca2(SO4)3 is unresolved; the published Handbook/USGS syngenite formula is K2Ca(SO4)2·H2O. No separate new species owner or alternative phase assignment is created from this discrepancy.

Abstract/conclusion reverse the AlO6/AlO4 coordination labels relative to section3.2.2. Figure6 shows multipleCaO ratios despite its0.4caption. Figure7/Table2 use800degreesC/30minutes/0.4ratio, distinct from thetwohour leaching batches; localEDS and proposedcore/diffusion interpretations are not quantitative phase proofs. TG interpretation is not a closed sulfur-gas balance. Replication/errorbars and leachpH are unreported.

A preliminary text-extraction concern was rejected after viewing original pixels: a hidden text object saysCaCO3/0.4 in Figure3, but the actual v2 plotted label and caption consistently showCaO/alunite0.2. This is retained as an extraction-artifact observation, not an asserted visible source contradiction.

## Validation and handoff

Both new owners have actual CREATE sidecars, inline timestamps and named validation: two records checked, zero failed. Exact frozen owner/history paths and hashes are in the paired JSON and external `frozen-records.json`. No self-scientific review is claimed. Root owns generated pages and full-batch gates; the independent reviewer must inspect final bytes and sources before acceptance. Proposed source questions concern alunite's product naming/coordination/caption and Reich's blank normalization/assay basis; the narrow record claims do not require invented resolutions.

## Remaining limits

Eventoff NAPS structure factors are not acquired. Direct publisher HTML/notes access was bounded by403; accepted full originals and actual supplements are complete within the inspected routes. The workbook is inspected source data, not a recalculated experimental mass balance. Source follow-ups, if posted, remain open until original data/version clarification is available. No global literature exhaustion, modern microbial absence, universal phase purity or industrial efficacy claim is made.
