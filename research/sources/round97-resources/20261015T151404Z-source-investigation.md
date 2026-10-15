# Round97 bone-residue source investigation

- UTC assessment timestamp: 2026-10-15T15:14:04.141600+00:00
- Researcher: Codex (GPT-6; codex), `/root/round97_resources`.
- Worktree: `/private/tmp/CMMMech-expansion-round97-20261015`; trusted base `9272005a590c9fa1e5fbb75b30f914ce38c3924a`.
- Scope: bounded search for new secondary-resource owners with primary microbial extraction/transformation evidence. Initial manure and coal-bottom-ash leads led to two distinct bone-residue owners. This does not establish exhaustion of CMM sources.
- Skill: installed `cmmmech-add-record`, local discovery and review contracts. Baseline passed before owner writes; records have actual CREATE histories. Separate independent scientific reviews are still required.

## Selection and concept boundaries

1. **Poultry-bone residues**: cooked/boiled, ground bone feed with culture-associated phosphorus elution in soil columns and acidophile broth. Animal species, supplier and detailed cooking conditions are unreported; poultry is not silently identified as chicken.
2. **Fish-bone residues**: ground fish-bone feed with a distinct low-dose null and qualified culture-associated phosphorus elution. Fish species, supply chain and pretreatment beyond grinding are unreported. No industrial-feed origin is invented.

Both are secondary-resource owners, distinct from manure, bone ash, purified hydroxyapatite, elemental phosphorus and phosphate rock. No element/mineral identifier or criticality designation is assigned to either resource. The same paired papers underlie both owners: two records are not two independent replications. The papers describe distinct culture/column experiments by overlapping authors; no independently replicated performance claim is made.

## Primary sources and inspected evidence

### Wyciszkiewicz, Saeid and Chojnacka (2017), Engineering in Life Sciences

DOI [10.1002/elsc.201600191](https://doi.org/10.1002/elsc.201600191), 17:749–758, PMCID PMC6999332, PMID32624820. Complete official PMC HTML, Tables1–4 and all5 original figure JPEGs inspected. Wiley PDF returned403, EuropePMC XML500, and the nominal PMC PDF request returned an1817-byte HTML document. That document is **not** treated as a PDF. No separate supplement is announced in the inspected HTML. Copyright notice is Wiley2017; redistribution permission not established, so raw full text and figures remain outsideGit.

- Sections2.1–2.3: source-designated Bacillus megaterium PCM1855 from the Polish collection; 30mL glass columns,10g soil/feed; nominal1%,5%,10% feed; ground<1mm. Inoculated arms received10mL culture, controls10mL water. The medium contained glucose and yeast extract plus salts. Table1 separately assigns6.08mg P2O5-equivalent to inoculum and includes soilP. Medium/phosphorus inputs are unmatched, and soil sterilization is unreported.
- Sections2.3–2.4: four3mL collections/day, paper filtration, vanadophosphomolybdate assay expressed as P2O5.34degreesC/120rpm describe inoculum preparation, not established column conditions. Column temperature and independent biological replicate counts are not given. The Methods say28days, while Figures2–3 and crossing-time prose sayminutes; no elapsed-time/rate claim is curated.
- Table2 and Figure2A: poultry10% reported47.3 versus23.5mgP2O5-equivalent total-column elution. Figure2A supplies the amount unit omitted from Table2. At1%,15.2 versus9.32mg differs by less than the6.08mg inoculum contribution, so an attributable bone benefit is not established by that comparison alone.
- Table2/Figure2B: fish10% reported37.05 versus17.3mg, and5%27.1 versus18.6mg. At1%,14.8 versus12.4mg and parallel curves were interpreted by the source as no bacterial effect. A later99.9% SF statement does not overturn this null or establish bone-specific recovery; denominator/correction details are unresolved.
- Poultry-only nutrient follow-up: Figure1B shows concentrated medium delivered to both arms. Figure3/Table2 report153.5 versus30.3mg for10% poultry feed. Medium inputs, soil and inoculum prevent bone-specific attribution; not an isolated product. The follow-up does not apply to fish.
- Figures4–5 and Table4 are empirical pH/model descriptions, not a measured organic-acid pathway. Table4 contains max/min labeling inconsistencies. Table3 includes multiple p-values above0.05 despite broad significance wording; no universal significant dose response is inferred.
- Table1 has fish-feed mass entries incompatible with the nominal dose and a64/65mg inconsistency; the nominal methods doses are retained with the discrepancy explicit. Table1's soil-only arm is labeled Soil+B.m., so the general prose description of a control does not prove a full matched sterile design.
- Full Results/Discussion and concluding section were checked. Soluble/remainingP, nutrient effects and proposed agricultural applications are kept distinct. There is no isolated product, demonstrated field performance or industrial deployment in this study.

### Wyciszkiewicz, Saeid, Malinowski and Chojnacka (2017), Molecules

DOI [10.3390/molecules22030473](https://doi.org/10.3390/molecules22030473),22:473. Complete13-page publisher PDF and official EuropePMC JATS acquired; Tables1–4/Figures1–3 inspected, with visual page checks of3,4,5,7,9,10. The hidden PDF extraction text repeats some image-associated text; page count is13 from the actual PDF. CC-BY4.0 notice appears on PDFp13. Raw artifacts remain outsideGit even where an open license exists.

- Section3.1/p9: A.ferrooxidans F7-01 source designation; reported isolation from Iron Bridge tailings, Poland.10%v/v72h culture;9K medium with44.2g/LFeSO4.7H2O,0.8g/L elementalS,0.5g/LK2HPO4, and H2SO4 adjustment to pH2.5. Seven-day precursor cultivation at30degreesC is described; Figure3's72h/day9 timeline is not reconciled. Growth does not prove added chemical acid has ceased contributing.
- Section3.2/p10: boiled/crushed poultry bones18.6%P2O5 and crushed fish bones20.0%P2O5, sieved<1mm;250mLmedium; nominal2,4,10,20g/L,12days at34degreesC, reportedtriplicate samples. Shaker speed/filtration cutoff unavailable. No matched uninoculated/acid-only arm.
- Section3.3/p10: nitric-acid digestion of permeates and ICP-OES, elementalP expressed asP2O5. Orthophosphate-only speciation is not established. Medium phosphate and background corrections prevent a clean bone-only mass balance.
- Table1/p3 and Figure1/p4 show lower finalpH and increased liquidP. Poultry highest nominaldose gives lower response than10g/L. Fish liquid concentrations increase with nominaldose. These are culture-associated observations; no direct microbial necessity or unique acid pathway is established.
- Figures1a/2a label the highest poultrydose40g/L, versus20g/L in methods/tables. Phosphorite methods list2/4g/L whereas result tables/plots use4/10g/L. These are source conflicts, not reconciled recipes.
- Table2/p5 contains fitted maxima/SF, with repeated/misaligned fish parameter labels; values are not measured yields.1980mg/L in the table and1.98% in narrative are not interchangeable; poultry1.6%/1.9% fertilizer-strength wording and later0.08%/0.14% wording conflict. No fitted yield or percent-concentration claim is adopted. Table2/model regressions and Table3 correlations are not causal tests.
- Table4/p9 and historical Polish fertilizer regulation discussion do not establish comprehensive safety, current compliance, agronomic efficacy or deployment. No legal/criticality claim is copied. Unavailability of source samples is stated onp13. No separate supplement is announced in PDF/JATS.

## Identifier verification

Official NCBI taxonomy efetch verified1404 as **Priestia megaterium**, species, with **Bacillus megaterium** synonym;920 as **Acidithiobacillus ferrooxidans**, species. The YAML maps source species names and explicitly leaves PCM1855/F7-01 authentication and genome accessions unresolved. No species of fish or poultry is inferred. Crossref records corroborate both study titles/DOIs; checked relations did not announce an affecting correction, which is not a guarantee of absence.

## Search, deduplication and limits

Live search queries are retained verbatim in the pairedJSON. No date/domain filters or pagination beyond returned first result sets. DOI/title correction, erratum, retraction, control and abiotic searches were checked; none of the returned results supplied an affecting correction. Source contradictions above are retained regardless. This is a bounded review, not an exhaustive review or absence certificate.

`dedup-before.json` records8 identity/study queries across both original/main and isolated worktree `data/records`, `research`, `reviews`, `history`, including hidden/ignored files and relevant followed symlinks. It also searched12 referenced prior resource-download directories traced from rounds77/88/90/93. No matching bone owner or either DOI was found within this boundary. Binary PDFs are not assumed text-searchable: queried retained raw text/HTML/XML/metadata provides that boundary, and no machine-wide absence claim is made.

Prior pig-manure, wood-ash and coal-fly-ash owners were inspected to avoid resource conflation. The acquired raw materials and datafiles are a source-reading cache, not an automatically reusable structured dataset. The studies expose no verified bulk experimental-data deposit in the inspected originals. No formal concentration observations were created because the contract requires exactmg/kg source cells with analysis dates; this batch's selected measurements are differently based and retained as qualified prose.

## Deferred and duplicate leads

- Poultry-manure/poultry-litter DOI10.5530/jam.2.4.5:9-page publisherPDF acquired. It concerns co-composted straw/manure and operationalPfractions; full independent curation/phase and input-mass audit remains. The current journal landing page displays2024 while the article/issue is2016. Do not treat reposting as a new experiment.
- Poultry-litter Bacillus paper at EKB article194469: HTTP429 again; earlier round93 attempt also failed. Exact methods/source cannot yet support a record.
- Dao/Hoang2008 DOI10.1016/j.chemosphere.2008.04.048: USDA authoritative metadata lead for purified fungal phosphohydrolases; primary full text not acquired, so no enzyme/measurement claim curated.
- Coal bottom ash: ITB2022 Bacillus nitratireducens thesis has publicly visible abstract but chapters marked embargo through2030; not used as primary-method evidence. Lisafitri/Kardena2023 DOI10.5614/j.eng.technol.sci.2023.55.1.8 is a literature review despite research-paper branding. Pangayao coal-ash leads must resolve actual fly/bottom feed before a new bottom-ash owner. Existing coal fly ash is not a duplicate route to a bottom-ash record.
- Additional bone studies DOI10.1515/chem-2015-0123,10.1007/s12649-013-9238-7,10.3390/molecules23112897 and10.1515/chem-2019-0057 remain expansion leads. Full methods/source-data/experiment-lineage assessment is required before adopting their measurements or field-scale claims; secondary summaries are not accepted proof.

## Ranked handoff

1. Independently review both new owners against exact final hashes, including both raw primary sources and figure units. Treat an overbroad yield/biological-causality assertion as a major finding.
2. Seek original experimental sheets or author clarification for column timing, biological replication, inoculum/soilP accounting, nominal-dose table errors and near100%SF denominator; for broth, request backgroundP/acid correction, exact high-dose label and mg/L-versus-percent resolution. Existing records already qualify these limits.
3. Extend the same bone owners through the additional original studies only after experiment deduplication and explicit control/scale checks. Continue separate manure and coal-bottom-ash acquisition leads; this investigation does not exhaust secondary resources.

## Current artifacts and validation

- `data/records/poultry-bone-residues.yaml` SHA256 `2201a05a9daa8019bf451ac6d4f425f5943547359e98cb04325b25e1acdd2785`; history `history/records/poultry-bone-residues/2026-10-15T151128Z-codex-4356f7.yaml`.
- `data/records/fish-bone-residues.yaml` SHA256 `4cf61c97bcb1fbeef34b8a5e842c4f465d0e849938e81d6f9dba82fb5379df5e`; history `history/records/fish-bone-residues/2026-10-15T151141Z-codex-99e593.yaml`.

Individual strict validation: both files passed with one record checked and0failures each. Root runs full-corpus/history/review gates after independent reviews. No schema, validator or governed-copy changes were required.
