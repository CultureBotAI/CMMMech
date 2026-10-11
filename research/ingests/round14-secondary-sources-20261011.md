# Round 14 secondary-resource investigation and curation

Prepared 2026-10-11 UTC in `/private/tmp/CMMMech-expansion-round14-20261011`,
branch `curate/cmm-expansion-round14-20261011`, against trusted base
`8f8abedfce68f932e4f6f333a5470ee5f3897ff4`. The accompanying
[JSON dossier](round14-secondary-sources-20261011.json) records exact queries,
fresh acquisitions, failures, hashes, source locators, histories and current
record hashes. This is curation provenance; independent scientific reviews are
separate. Acceptance work is tracked by issue #56.

Five resource identities are supported by four primary publications. These are
heterogeneous feeds, distinct from constituent elements, mineral species and
market commodities. No criticality designation or external material identifier
is inferred. The old niobium experiment is deliberately represented through its
two different feed identities; that reuse is not additional replication.

| Record | Selected primary evidence | Accepted scope |
|---|---|---|
| [Spent FCC catalyst](../../data/records/spent-fluid-catalytic-cracking-catalyst.yaml) | [Reed et al. 2016](https://doi.org/10.1016/j.hydromet.2016.08.006), full [OSTI manuscript](https://www.osti.gov/servlets/purl/1357607), Sections 2.1–2.7, 3.3–3.6, Table 1, Figures 3 and 5 | B58 cell-free supernatant leaching of one characterized Valero catalyst, with unmatched chemical-control acidity |
| [Coal fly ash](../../data/records/coal-fly-ash.yaml) | [Park and Liang 2019](https://doi.org/10.1007/s40789-019-0238-5), complete publisher PDF/HTML, methods and Figures 1–3, 6–7, Tables 1–2 | ATCC 22214 supernatant treatment and residual-solid elemental inventory loss; no directly measured liquid recovery |
| [Municipal-waste incineration ash](../../data/records/municipal-waste-incineration-ash.yaml) | [Andrzejewska-Górecka et al. 2019](https://doi.org/10.24425/aep.2019.128643), methods pp.73–74, Figures 1–5, Tables 1–4 | Ash A, unresolved fly/bottom fraction, condition-dependent release including aerated Nb null |
| [Sewage-sludge incineration ash](../../data/records/sewage-sludge-incineration-ash.yaml) | Same primary paper, ash B, Figures 6–8 | Different feed with modest Nb release and condition-specific In release; no transfer of ash-A complete-release claims |
| [Spent hydrocracking catalyst](../../data/records/spent-hydrocracking-catalyst.yaml) | [Sawangchart et al. 2026](https://doi.org/10.48048/tis.2026.13063), complete 17-page publisher PDF, methods pp.3–5, Tables 4–8, Figures 1–4 | Qualified fungal-filtrate mobilization from decoked Thai refinery feed; substantial protocol and numerical inconsistencies retained |

## Search boundaries and source access

Deduplication used `rg --no-ignore --hidden --follow` over records, research,
reviews and history, the current raw directory, and cited prior raw roots for
round 13 secondary resources, round 10 Nb/Ta and round 5 germanium. Hidden and
ignored files were included. Selected PDFs were separately extracted/read;
text search alone is not an exhaustive PDF-content search. No matching resource
roots existed before these writes within those boundaries. A guessed germanium
raw path was corrected to the actual cited `cmm-round5-germanium-20261011`
directory. No symlinks were found in these scoped scientific/raw trees.

Queries included exact DOI/full-text searches, material/control combinations,
and DOI correction/retraction terms. Only returned first-page responses were
covered, with no pagination or claim of literature exhaustion. No applicable
correction notice was identified in those results. Current Crossref records for
Park, the ash study and Sawangchart have no `update-to` entry and empty relations;
Reed's Crossref endpoint returned 429, so its identity was checked through the
primary publisher and OSTI manuscript instead. This is bounded checking, not a
universal retraction clearance.

Initial sandbox network requests could not resolve hosts. Authorized public
network acquisition succeeded for the four primary PDFs. Springer redirected
with a cookie-error query string but returned actual parseable PDF and article
HTML, not a challenge masquerading as an article. The related 2011 WASET
hydrotreating-catalyst PDF route returned 403. The primary 2011 Gholami journal
lead remains without fully inspected methods. All failures are logged.

NCBI species identifiers 442, 75736 and 5053 were freshly resolved.
*Candida bombicola* maps to *Starmerella bombicola*, and NCBI lists ATCC 22214
among type-material cultures. An initial incorrect candidate ID 4909 resolved
to *Pichia kudriavzevii* and was rejected. NCBI RefSeq NR_111412.1 is the
*Aspergillus aculeatus* CBS 172.66 type-material ITS sequence; it is the
reference matched by the 2026 paper, not its experimental isolate accession.

## Scientific assessment and retained limits

**FCC catalyst.** The 29-page accepted manuscript was read, with Figures 3 and
5 rendered for visual checking. Four-day B58 Pkm supernatant was centrifuged and
sterile-filtered, then contacted with triply autoclaved FCC at 1.5% w/v for
24 hours, 30°C, 150 rpm. Triplicate ICP-MS measurements of filtered liquid
support the reported approximately 49% total-REE leaching relative to an
acid-digested feed inventory. This is not an individual-element yield. Figure 3
shows about 33% in PkmT, versus 49% in Pkm. PkmT cultures were grown at
20°C while Pkm cultures were grown at 30°C; both supernatants then leached
at 30°C. This comparison cannot isolate the effect of added tryptone.
The 10, 30 and 90 mM gluconic-acid controls produced approximately 24%, 36% and
45%, but started at pH 3.2, 2.9 and 2.5 versus B58 pH 2.3. The result does not
isolate a special ligand effect at matched acidity. The proposed
2,5-diketogluconate was not verified. Whole-cell, fungal and biosorption
observations from the separate phosphor assays do not establish corresponding
FCC behavior. Feedstock origin is industrial; the leaching experiment is not.

**Coal fly ash.** Complete publisher text and figures were read. The selected
ATCC 22214 supernatant was grown with ash for three days and used on fresh,
milled ash for six hours. The study measured initial and residual solids after
washing, drying, heating and acid reflux. Its “leaching efficiency” is inferred
from solid-inventory differences, not measured in solution, and the
approximately 59.7% gravimetric mineral loss is not a total-REE yield. Common
digestion procedures do not prove equal quantitative extraction of original and
altered host phases. Water/fresh-medium controls are mentioned without
quantitative outcomes in the main leaching figures; the plotted growth control
without ash is a different comparator. Active metabolites were not identified.
Figure 2 reverses the two nonselected organism labels relative to the text's
reported values, and Figure 3 gives Ce 27.3% while the text groups the lowest
light-REE losses as 28.1–30.7%. These contradictions are preserved, with no
inferred corrected measurement. The separate Rezaei 2023 roasted-feed process
remains an uncurated lead rather than being silently substituted.

**Incineration ashes.** The complete seven-page primary paper was freshly
acquired and read; methods, tabular conditions and plotted outcomes were
checked. Ash A and B have different source processes; neither is identified
as a specific fly/bottom fraction. The sludge culture starts below pH 3, but
final values rise to 6–10. Aeration improves several reported ash-A metal
releases but gives the reported Nb null, while ash-B Nb remains around 15%.
Sulfur oxidation cannot therefore be assumed to cause the Nb result.
Undefined control preparation, analytical separation, culture-background
subtraction and biological replication prevent a strong causal assertion.
Instrument exposures are not biological triplicates. Table 4 says 120 rpm for
variant 3 versus 50 rpm in Table 2/figures, and uses “Rd” for the ash-B Rh row.
Its caption mentions culture while the text expresses released amount per kg
initial waste. Figures and source wording remain explicit; none is silently
normalized into a validated product-recovery yield. Cd/Cr table dashes are not
analytical zeros.

**Hydrocracking catalyst.** This newly acquired 2026 primary study supports the
narrower hydrocracking resource identity. The feed was heated at 600°C for six
hours and ground below 150 µm. A reported *A. aculeatus* soil isolate produced
culture filtrate over nine days; the filtrate was subsequently adjusted and
autoclaved before the three-hour leach. It is not live-cell extraction during
that stage. Figure 1 shows culture pH falling near 3.5, while methods say to
adjust resulting filtrate to 6.5 using HCl. Tables 2/5 label pulp density mg/L,
whereas methods and optimization text say %w/v. Control speed and percentage
values differ between methods, prose and Table 7. No corrected protocol is
invented. Table 7 distinguishes measured Mo 22.95 ±0.80% from predicted 24.55%;
the paper also acknowledges incomplete digestion of the denominator feed.
Consequently the record accepts qualified mobilization, not a reliable optimal
recovery yield. The Al model has significant lack of fit, and kinetic fitting
without direct surface characterization does not establish molecular causality.
Neither isolated product nor pilot/industrial operation was demonstrated.

## Handoff and remaining sources

All five records have actual `CREATE` histories linked to issue #56 and distinct
inline creation events. Named validation exited 0: **5 records checked,
0 failed**. Parent agent owns full-corpus checks and independent saved reviews;
these are not claimed by this dossier. No schema, validator, tests or governance
were changed. Structured observations were not manufactured from percentages,
incomplete dates or incompatible units.

Further useful work remains:

1. Acquire complete methods for [Gholami et al. 2011](https://doi.org/10.1016/j.hydromet.2010.11.011)
   and establish whether a distinct hydrotreating feed root is justified.
2. Obtain [Rezaei et al. 2023](https://doi.org/10.1016/j.hydromet.2023.106038)
   full methods and supplements for the salt-roasted coal-fly-ash process.
3. The full [Das et al. 2019](https://doi.org/10.1016/j.btre.2019.e00349)
   EuropePMC XML was acquired but not completely reviewed this round; inspect
   it before adding its fungal Al mechanism to the FCC record.
4. Acquire [Ishigaki et al. 2005](https://doi.org/10.1016/j.chemosphere.2004.12.060)
   for an explicitly identified municipal-incineration fly-ash experiment.
   That citation cannot retroactively resolve the ash-A fraction.

Raw reading copies and rendered images remain outside Git in
`/private/tmp/cmm-round14-secondary-raw`. Licenses and access are recorded per
artifact; public reading access does not imply unrestricted redistribution.

## Independent-review correction

Issue #57 identified omission of the Pkm/PkmT culture-temperature
confound. The record now distinguishes 30°C Pkm and 20°C PkmT growth from
the common 30°C leaching step, with no isolated tryptone-effect claim.
An actual EDIT sidecar was appended; the original CREATE is unchanged.
Successor scientific review is parent-owned and recorded separately.

After this correction, named FCC validation completed with exit 0: one
record checked, zero failed (session 88662). The initial parent batch passed
307 tests with three skipped, 119 records and 134 histories before this
correction; parent-owned final checks and successor review remain separate.
