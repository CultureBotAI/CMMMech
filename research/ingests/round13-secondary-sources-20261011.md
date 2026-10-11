# Round 13 secondary-resource source assessment and curation

Prepared 2026-10-11 UTC against trusted base `14ceff0da3e19d6d36426d33f4cf577b8e64760f`
in `/private/tmp/CMMMech-expansion-round13-20261011`, branch
`curate/cmm-expansion-round13-20261011`. The [machine-readable dossier](round13-secondary-sources-20261011.json)
contains exact queries, acquisition times, source hashes, access failures,
reviewed locators, record hashes and history paths. This report is a curation
handoff and provenance assessment; independent scientific reviews are separate.

Three secondary-resource identities are added. Battery black mass and red mud
already appeared as substrates in the cobalt and aluminium records, so their
experiments are deliberately shared evidence, not new independent replications.
The resource roots capture heterogeneous feeds without confusing them with
constituent elements or inheriting their criticality designations.

| Priority and record | Primary evidence and exact scope | Scientific boundary |
|---|---|---|
| 1. [Battery black mass](../../data/records/battery-black-mass.yaml) | [Lalropuia et al. 2024](https://doi.org/10.3389/fmicb.2024.1347072), Sections 2.1–2.7, 3.1–3.3, Tables 1–2, Figures 4–6; pretreated NMC battery powder and an adapted Lake Hromnice enrichment | Original-enrichment taxonomy is not post-adaptation community identity. Different abiotic pH/iron chemistry and inconsistent source inventories prevent an accepted complete-recovery yield. |
| 2. [Bauxite residue](../../data/records/bauxite-residue.yaml) | [Urík et al. 2015](https://doi.org/10.1016/j.jinorgbio.2015.08.022), journal 154–159; full reproduction in [official author thesis](https://www.vut.cz/uredni-deska/habilitace?action=priloha&priloha=226417), PDF 80–85; Ajka residue and fungal G-10 culture | Al-host phases unresolved. Comparable acid-only release used different medium and duration. Filter-passing aluminium is not isolated alumina or metal. |
| 3. [Phosphogypsum](../../data/records/phosphogypsum.yaml) | [Antonick et al. 2019](https://doi.org/10.1016/j.jct.2018.12.034), Sections 2–4, Tables 1–2, separately synthesized REE-doped powders; and [Zhang et al. 2025](https://doi.org/10.3390/molecules30030674), actual Xifeng residue | Synthetic-feed comparisons and actual-residue observations remain separate. The latter supports only qualified association because units, timing, volume accounting and extraction denominators conflict. |

## Search and identity checks

`rg --no-ignore --hidden` searched `data/records`, `research`, `reviews` and
`history`, plus the task's raw directory and the relevant cited raw roots listed
in JSON. Symlinks were checked in the selected repository/task/previous-article
boundaries. Selected binary PDFs were separately extracted and inspected;
ordinary text search is not evidence of absence from a PDF. Before these writes,
the corpus had two secondary-resource roots: fluorescent-lamp-phosphor and
GaAs-production hydroxide sludge. No matching resource roots were found in the
searched record boundaries, including ignored and hidden files. This is not a
machine-wide or literature-wide absence claim.

No external material identifier is assigned to these heterogeneous waste roots.
Fresh NCBI Taxonomy XML verifies species identifiers 5061 (*Aspergillus niger*)
and 442 (*Gluconobacter oxydans*), without authenticating the experimental strain
or an unspecified supplier culture. No criticality entry is inferred from an
Al-, Li-, Co- or REE-containing feed.

Live searches used first returned results without filters or pagination and
included DOI/title correction and retraction searches. No applicable notice was
found in those results; the four inspected current Crossref records had empty
relations and no `update-to` entry. These bounded checks do not establish
exhaustive retraction clearance. The MDPI version notes report PDF/XML updates
on 7 February 2025 and an HTML update on 24 June 2025, without explaining a
scientific correction. Publication years follow the original articles; the
Antonick manuscript's 2021 repository cover is not a new experiment.

## Evidence inspected and retained limitations

**Battery black mass.** Fresh publisher HTML and full PDF were read, including
methods, feed composition, adaptation table and assay figures. The cultured and
sterile arms differ in acidity and iron chemistry. The source's day-zero
background subtraction does not reconcile the Figure 5 adapted-Co bars around
2 g/L with the nominal 1.45 g/L feed inventory implied by 145 g Co/kg and
10 g black mass/L. Table 2 adaptation doses also disagree with Table 1
composition equivalents. The record accepts the reported mobilization pattern,
not a closed mass balance or an abstract-level 100% recovery claim. The source
lists a supplemental `Table_1.XLSX`; no direct download was exposed in the
inspected page, and a tested standard publisher file route returned 404. No
supplement-only ASV or post-adaptation claims were accepted.

**Bauxite residue.** The previously acquired official thesis was rehashed and
the full embedded six-page primary paper reread; Figures 3, 5–9 were visually
checked. Acquisition time is preserved as earlier in this session, not described
as a fresh download. The selected 0.2 g assay avoids a separate high-loading
40/50 g/L label inconsistency. No-fungus results lack a numerical Al detection
limit. The synthetic-acid comparison supports a chemical contribution but
cannot establish equal kinetics because incubation times and media differ.

**Phosphogypsum model assay.** The complete OSTI manuscript was acquired and
read, with Table 2 visually checked. Its empirical hydration states are near
0.5 rather than two waters per formula unit, and the samples each contain a
single REE at a higher concentration than typical industrial residue. Equal
pH and equal acid concentration are separate comparisons. Sulfuric acid usually
outperformed spent medium at equal molarity; Y is an exception. Small organic
lixiviant differences have overlapping confidence intervals. Ce concentration
and percent-dissolved ordering differ between the organic lixiviants in Table 2,
so no simple uniform superiority claim is accepted. Cell-removal preparation
and the printed `0.22 mm` filter unit remain unresolved; neither is silently
corrected. Thermodynamic modeling omits kinetic/mass-transfer effects.

**Phosphogypsum industrial sample.** Actual PMC HTML and the Figure 7 image
were acquired despite a web-opening challenge and direct MDPI 403 responses.
The paper supplies no strain accession, matched acidified sterile control,
replicate count or error-bar definition. Figure 7 labels micrograms/kg while
its discussion uses micrograms/L; the plotted maximum is near day 24 while the
conclusion says approximately day 21. Nutrient addition changes volume, with
unclear liquid-to-solid accounting. The claimed 24.67% total and 55.67% Nd
extraction are retained only as rejected-for-acceptance source claims, not
verified yields. Organic-acid production is proposed, not chemically quantified.
These limits are explicit in the record's partial evidence.

## Next source investigations

1. **Spent fluid catalytic cracking catalyst:** verified [Reed et al. 2016](https://doi.org/10.1016/j.hydromet.2016.08.006),
   *Bioleaching of rare earth elements from waste phosphors and cracking catalysts*,
   Hydrometallurgy 166:34–40. A legitimate [OSTI manuscript](https://www.osti.gov/servlets/purl/1357607)
   was located after this round's three-record selection. Read full methods,
   substrate preparation and controls before curating a distinct FCC resource.
2. **Spent hydroprocessing refinery catalyst:** [Gholami et al. 2011](https://doi.org/10.1016/j.hydromet.2010.11.011)
   is a primary lead, but complete methods and controls were not obtained in this
   pass. Keep refinery hydroprocessing, FCC and automotive catalysts distinct.
3. **Coal fly ash:** [Rezaei et al. 2023](https://doi.org/10.1016/j.hydromet.2023.106038)
   remains an earlier research lead. Publisher abstract/sections describe a
   sequential salt-roasting and spent-medium process; full methods and matched
   controls remain necessary. Coal fly ash is not synonymous with the
   municipal-incineration/sewage-sludge ashes used by the current niobium record.

Raw primary text and images remain outside Git under
`/private/tmp/cmm-round13-secondary-raw`. The 2015 article remains under its
original prior-acquisition path. Licensing and access are recorded per artifact;
reading access does not establish unrestricted redistribution.

## Local validation and handoff

All three records have canonical `CREATE` history sidecars linked to issue
[#54](https://github.com/CultureBotAI/CMMMech/issues/54), plus distinct inline
curation events. The explicit three-record validator command exited 0:
**3 checked, 0 failed**. No schema, validator or test behavior changed. Parent
agent owns whole-batch gates and independent saved scientific reviews; this
assessment does not claim those later results. Current byte hashes and exact
sidecar paths are in the JSON dossier.
