# CMM source investigation: eudialyte ore

## Scope and provenance

- UTC: 2026-10-12T09:19:48.381394+00:00; codex (GPT-6), agent `/root/round43_hardmetal`, acting as curator.
- Worktree `/private/tmp/CMMMech-expansion-round52-20261012`; branch `curate/cmm-expansion-round52-20261012`; base `79ed7d69ea654d1b67bbf74bb931ff70c4c6913e`.
- Added only [eudialyte ore](../../../data/records/eudialyte-ore.yaml) and its canonical CREATE history. The parent owns publication, shared gates and independent review.
- Selected the complete primary thesis because it exposes the ore preparation, culture and chemical controls and original assay graphics. The feed is an Ilimaussaq geological ore, not a verified pure species, eudialyte-group definition, upgraded concentrate, element or secondary resource. No criticality claim is made.

## Search and acquisition log

| Provider/source | Query or exact route | UTC date | Inspection and outcome |
|---|---|---|---|
| Web discovery | Queries recorded verbatim in paired JSON, including `"Hunter" "eudialyte" "bioleaching"` and thesis-title correction searches | 2026-10-12 | Located migrated official repository item; no verified separate Chapter4 journal publication or notice in bounded results |
| Edinburgh | [Landing](https://era.ed.ac.uk/items/b5fb0ce1-581b-4980-b09e-29e86e7be419); [original PDF](https://era.ed.ac.uk/server/api/core/bitstreams/f56a44ca-139f-4205-8ed2-5759aa3f7df7/content) | 2026-10-12 | HTTP200, complete217pages; relevant methods/text and original graphics inspected |
| Edinburgh | [Observed supporting ZIP link](https://era.ed.ac.uk/bitstreams/f4ed3ae2-174e-40a0-b60d-7f9ab0de1e3e/download) | 2026-10-12 | HTTP200,32,567,664bytes; all59files inventoried and scope-screened; seven workbooks contain modeling data |
| DataCite | [DOI metadata](https://api.datacite.org/dois/10.7488/era/834) | 2026-10-12 | Author/title/2020thesis identity verified; issued2020-11-30, accepted/available2021-03-24, modified2026-08-17; these dates have different roles |
| NCBI | [Taxonomy920](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=920&mode=Info) | 2026-10-12 | Current species label verified; does not authenticate the experimental culture or NCIMB strain |

The old handle/PDF web route and indexed-text search behaved inconsistently; the new observed official bitstream supplied the actual complete PDF. Landing still displays Restricted Access with an elapsed2021-11-30 embargo, but both downloads actually returned200. No authentication or access-control bypass was used. Exact acquisition timestamps, URLs, response types and hashes are in the paired JSON and raw receipts.

## Deduplication and identity boundaries

`rg --no-ignore --hidden --follow` searched the current and original checkouts' records, research, reviews and history, plus190 existing referenced raw/evidence/research roots discovered from4030 text artifacts. Searches included eudialyte, Hunter2020, its handle and Hedrich106068. Both command stderr outputs were empty. There were110corpus and1248raw matching lines, mainly deferred-source context and mineral-authority mentions; none was an existing record owner. The broad Hunter/year pattern also matched unrelated long metadata lines, not an accepted duplicate thesis experiment.

Nine referenced roots were unavailable; their exact paths are retained in JSON. Text-bearing extensions were searched and relevant symlinks followed; not every binary in those roots was decoded and no unrelated home or broad temporary-directory search was performed. Thus absence is bounded to this declared scope. Earlier [Round51 feed handoff](../round51-zircon-feed/20261012T082652Z-source-investigation.md) remains valid for the different Bansal/Hedrich access gaps. This thesis does not close [issue153](https://github.com/CultureBotAI/CMMMech/issues/153).

## Candidate inventory and source assessment

| Candidate | Source and inspected scope | Decision |
|---|---|---|
| Ilimaussaq eudialyte ore | Hunter2020 DOI10.7488/era/834; complete original thesis, original Chapter4 experimental figures, relevant Chapter7 procedures and deposited ZIP | Curated one `primary_resource`, pending independent review |
| Pure eudialyte mineral/species or upgraded concentrate | Thesis uses a literature unit-cell drawing, without sample-specific phase/grade evidence | No separate mineral or concentrate owner inferred |
| Hedrich2023 zircon/eudialyte concentrates | Prior fulltext/graphics/SI gap, DOI10.1016/j.hydromet.2023.106068 | Defer; abstract null results remain a constraint for future assessment |

Hunter's thesis title page identifies a2020 Edinburgh PhD. DataCite's main title omits “Investigating”; the alternative title, landing and actual PDF agree with the citation used. The thesis publication list on printedp.VII identifies other chapters' journal/in-preparation work, but no Chapter4 publication. That observation and bounded searches are not proof that none exists.

All Chapter4 experimental figures were personally viewed from original PDF renders:4.5.2.1–2,4.5.3.1–6,4.5.4.1–2 and4.5.5.1–2. The literature crystal Figure4.4.1 and methods Figures7.2.1/7.4.2.1 and Tables7.3.1/7.4.2.1 were also viewed. Exact visually inspected PDF page numbers are in JSON. Complete Chapter4 text and relevant Chapter7 procedures were read. This is not a claim to visually review every page of the217-page thesis or reconstruct unrelated modeling chapters.

The official ZIP's69entries comprise59files and10directories. All files were hashed; names, decodable text and all cells of seven original workbooks were screened for eudialyte/bioleaching/organism scope terms. No Chapter4 assay table was identified. The named folders and workbook sheets concern ionic-liquid structures, trajectories, radial distributions and energies. Computational executables and scripts were not executed; unrelated calculations were not reproduced. This is a bounded relevance screen, not scientific verification of all modeling results.

### Retained biological observation and limitations

Section7.4.1 places the jaw-crushed feed at Ilimaussaq, Greenland, and names the purchased culture as *Acidithiobacillus ferrooxidans* NCIMB10435. The abstract instead says *A. thiooxidans*. The record retains the disagreement and maps only the body/methods species to NCBI920; it does not invent a sequence, strain taxon, type-strain equivalence or purity result. A historical contaminant-study search hit involving NCIB10435 was not fully assessed and does not establish contamination of the2020 culture.

The laboratory setup uses membrane-capped, agitated flasks with125mL acidic iron-containing growth medium. Initial inoculated cultures are described in triplicate, with an uninoculated-medium reference. The ore time course uses0.50g autoclaved powder and includes a culture-without-ore arm; the acid comparison uses1.00g per125mL. Room temperature25°C occurs in the narrative, but an incubation set point, agitation speed and inoculum density are unresolved. No values were borrowed from the separate solvent-extraction procedure to fill these gaps.

The observed trends support culture-associated acidification and enhanced filtered aqueous mobilization versus the mild uninoculated comparator. Inoculated ore solutions approachpH2.2 while uninoculated ore solutions remain around2.6–2.8. Strong2M nitric/sulfuric acids give substantially greater rare-earth concentrations. Different pH trajectories prevent a pH-independent microbial-effect claim. Dissolved concentrations are not cumulative mineral loss, extraction fractions or product yields.

Internal source limitations are preserved: the FeSO4 stock molarity is inconsistent with its mass/volume; the ferrozine discussion specifies562nm whereas Section7.4.9 says568nm; printed calibration/equations and the claim of complete Fe oxidation are not independently reconstructed. The Si:Zr interpretation compares mass-concentration slopes to atomic stoichiometry and cannot establish adsorption on that basis. No new exact oxidation fraction or dissolution rate is curated. No-gel observations at low loading do not prove scalable pulp behavior.

### Downstream chemical experiment

Figures4.5.5.1 and4.5.5.2 distinguish a synthetic model solution from actual bioleachate. The actual leachate was filtered, vacuum-concentrated fivefold and adjusted to5MNaNO3/0.1MHNO3 atpH1.40 before contact with0.1MIL0 or2AA in toluene. Abstract/conclusion statements of no pH adjustment do not describe that procedure without qualification. Solvent-extraction percentages do not measure whole-ore recovery; the printed general percentage equations leave denominator interpretation unclear, and minorREE signals approach analytical limits. The record keeps this chemical step as context, without measured product purity, closed mass balance or industrial deployment.

## Provenance, validation and handoff

- Original PDF SHA256: `a09ea4909d1c2a261a8d1f85839309e773cec675362afebdcd47c3333643640d`.
- Original ZIP SHA256: `ff7592e32c2f5c51720d7d2d4c0584129cb6f1c959a436c499f4640e098d9c12`.
- Raw sources, renders, extracted text and receipts remain outsideGit at `/private/tmp/cmm-round52-eudialyte-research`. PDF cover retains author copyright and permits personal noncommercial research; no redistribution of full text or raw ZIP is claimed. The repository contains paraphrased curation, metadata and hashes.
- Record SHA256: `ddecf732576b7bd3d791b9bb2d90529a202cae0bcfeb0caefbf8d0e6a6e39f5e`.
- [CREATE history](../../../history/records/eudialyte-ore/2026-10-12T091728Z-codex-d2511a.yaml) SHA256: `55610e308856722c110b9b3445ea423cd082f2a1d54b0566ef89d60aec4411c6`.
- Actual named validation returned exit0: `Checked 1 record(s); 0 failed.` Command, exact record hash and observed terminal-session provenance are retained in JSON.
- Independent scientific review and shared batch gates are parent-coordinated and not claimed by this curator.

Priorities: independently review the narrow record; obtain strain/organism clarification and original Chapter4 assay tables; establish feed mineralogy/grade and pH-matched comparisons before numerical recovery or species-wide generalization; acquire Hedrich2023 complete source separately. Bounded web searches found no verified thesis correction or retraction; this does not establish their universal absence.
