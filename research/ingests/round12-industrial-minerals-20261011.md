# Industrial-mineral commodity boundaries and additions, round 12

Prepared on 2026-10-11 UTC by codex / GPT-6 / codex against trusted base
`1e52585c9019a32d37f959e0dafa00ae431f28c4`. This dossier assesses the eight
industrial-mineral proposals from the round11 frontier. Its accompanying JSON
records exact searches, source acquisition receipts, raw hashes, local search
boundaries, record hashes and actual CREATE histories for issue #48.

Seven **commodity** records were created. `phosphate` remains a deferred separate
root because the US designation can be explicitly mapped to phosphate rock.
This is not an assertion that phosphate ions, phosphate minerals, elemental
phosphorus and phosphate rock are synonyms. No mineral-only or elemental
external identifier is assigned to any commodity. Independent reviews and
whole-corpus gates are handled separately and are not pre-asserted here.

## Identity and designation decisions

| Proposal | Disposition | Grounding and boundary |
|---|---|---|
| `baryte` | Create commodity | USGS MCS2026 Barite, printed pp. 48-49, treats crude, ground and crushed products. EU original Annex II(d) says baryte; US final 2025 says Barite. The record covers that industrial material, not the barite mineral species or barium element. |
| `fluorspar` | Create commodity | USGS's 2010 definition covers crude/beneficiated material mined or milled for fluorite. MCS2026 pp. 80-81 distinguishes commercial grades and recognizes synthetic recycled fluorspar. This is a commodity rather than fluorite species, fluoride ion or fluorine element. US 2025 and EU original Annex II(l) name fluorspar. |
| `feldspar` | Create commodity | USGS SIR2017-5118 establishes the aluminosilicate mineral scope; MCS2026 pp. 78-79 establishes separately traded, mined, beneficiated and ground feldspar. This is an industrial commodity rather than the mineral group or an individual K/Na/Ca species. The common chapter does not merge nepheline syenite into feldspar. EU original Annex II(k) names feldspar. |
| `magnesite` | Create source-defined commodity | BGS/CMIC OR/24/059 Table 11 names Magnesite. Its HS-code table, printed p. 259/PDF p. 263, includes natural magnesium carbonate, MgO, dead-burned magnesia and fused magnesia. Therefore the designated category is broader than the mineral MgCO3. No mineral identifier is transferred. MCS2026 Magnesium Compounds pp. 120-121 provides additional product context. |
| `phosphate` | Defer duplicate root; preserve designation mapping | The US final 2025 notice uses phosphate. USGS MCS2026 p. 143 explicitly describes phosphate rock as the material added to that list. This supports a documented mapping in `phosphate-rock`, not a second generic chemical-phosphate record. The historical frontier exact-key count must not silently call this an exact-root match. |
| `phosphate-rock` | Create commodity with bounded mechanism | MCS2026 pp. 142-143 distinguishes mined ore and beneficiated marketable rock from downstream acid and elemental phosphorus. EU original Annex II(y) names phosphate rock separately from phosphorus in (z). US 2025 phosphate is mapped using the explicit USGS interpretation. One Araxa rock experiment supplies the mechanism; no generic apatite or commodity-wide performance claim follows. |
| `potash` | Create commodity | MCS2026 p. 146 defines mined/manufactured salts with water-soluble potassium, describes KCl, sulfate and potassium-magnesium-sulfate products, and reports statistics as K2O equivalent. Potash is neither K2O nor every K-bearing mineral. US final 2025 directly names potash. |
| `sodium-compounds` | Create source-defined commodity | OR/24/059 section 2.6.3, p. 29, says mostly sodium carbonate, some sodium nitrate and minor sodium metal. Industrial salt is separate. Table 11 designates Sodium (Na) (compounds); the HS table p. 276/PDF280 confirms the three product categories. The name does not make metallic sodium a compound or cover all sodium salts. |

The authoritative US notice is [90 FR 50494-50497, 7 November 2025](https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm),
whose Summary and list were directly read. EU entries use only the
[original Regulation (EU) 2024/1252](https://eur-lex.europa.eu/eli/reg/2024/1252/oj/eng),
recital 8 and Annex II Section 1; no claim is made to have audited every
consolidated amendment. Canada and India mappings in the historical frontier
were not freshly inspected or added to these records.

For the UK, the [current NORA landing page](https://nora.nerc.ac.uk/id/eprint/539735/)
was freshly acquired and the retained [OR/24/059 PDF](https://nora.nerc.ac.uk/id/eprint/539735/1/OR24059.pdf)
was rehashed and read. Table 11 and the magnesite HS table were inspected as
rendered images. OR/24/059 is the replacement identified in the round10 graphite
report; the original OR/24/047 historical inventory is not silently rewritten.
The older landing-page replacement-number discrepancy remains documented in
round10. The assessment explicitly does not constitute government policy.

## Accepted phosphate-rock mechanism

[Mendes et al. 2013, DOI 10.1128/AEM.01487-13](https://pmc.ncbi.nlm.nih.gov/articles/PMC3754696/)
was acquired as complete PMC HTML after the web browser route returned a
challenge and Europe PMC full-text XML twice returned HTTP 500. Article
metadata identifies Applied and Environmental Microbiology 79(16):4906-4913.
Materials and Methods, rock characterization, Tables 1-2 and Figures 1 and 4
were read; the figure images were independently acquired and visually inspected.

The source-designated A. niger FS1 inoculum was 10^6 conidia per 125 mL flask
containing 50 mL NBRIP and 3 g/L Araxa rock phosphate, below 75 micrometres,
at 32 degrees C and 160 rpm. The source reports XRD and chemical characterization
consistent with fluorapatite plus hydroxyapatite and 13.97% P. This is a
characterized rock feed, not a pure-species experiment. Medium was adjusted to
pH 7 before P addition; Figure 1's initial pH is about 5.5. The record preserves
that distinction. The 10-day kinetics sampled three flasks at each time point;
0.45-micrometre filtrates were analyzed, with uninoculated flasks at start and
end. Phosphorus was assayed by the referenced ascorbic-acid method.

Figure 1 shows about 80 mg/L soluble P at 60 h and subsequent increases and
decreases; it does not show a continuously rising extracted fraction or an
isolated product. The three-replicate error bars are standard deviations.
No time-matched abiotic trajectory or acid-matched comparison is shown in that
figure. The record consequently describes culture-associated mobilization and
does not assign exclusive causation to a particular organic acid.

The separate 60-hour NaF-dose experiment (0-50 mg F/L, 5 mg/L increments) is a
useful challenge to universal solubilization. Figure 4a shows lower soluble P
with added F. Methods state three replicates at the 25 mg/L central point,
not every dose. Biomass and organic-acid determinations belong to the soluble
K2HPO4 arm; the paper's broader discussion must not silently move them into
the rock-fed arm. Possible P reprecipitation is an interpretation, not directly
established phase chemistry. The supplement URL returned HTML instead of a PDF;
no supplementary numerical values were imported. No taxon/strain CURIE was
invented. This is one laboratory experiment, without isolated phosphorus,
fertilizer-grade product or industrial deployment evidence.

## Deferred primary mechanisms

- **Baryte/barite:** [Ouyang et al. 2017, DOI 10.1016/j.apgeochem.2016.11.008](https://pubs.usgs.gov/publication/70180312)
  concerns pure barite and halophilic enrichment cultures. The USGS abstract
  and publisher partial methods identify sterile brine/freshwater controls,
  solution Ba, surface microscopy and dialysis comparisons. Full methods,
  figures and composition details were not acquired; the publisher direct
  route returned HTTP 403, and title/DOI repository searches did not close the
  gap. The claim is deferred rather than copying abstract fold changes into
  a commodity record. Related dissolution and precipitation papers remain
  leads, not independent verification of commercial barite processing.
- **Fluorspar/fluorite:** [Haas et al. 1999, DOI 10.1590/S0001-37141999000300007](https://www.scielo.br/j/rm/a/z8L9Q7ySk4FDJvptK4HYmhh/?lang=en)
  is an identified primary flocculation lead using C. xerosis and fine fluorite.
  Publisher abstract and indexed figure excerpts were found; complete methods,
  strain resolution, feed purity and particle mass balance were not verified.
  The comparison is mineral suspension settling, which does not automatically
  establish fluorspar commodity beneficiation or product purity. No mechanism
  or numerical efficiency is imported.
- **Feldspar:** [Wang et al. 2023, DOI 10.3390/ijms241814226](https://pmc.ncbi.nlm.nih.gov/articles/PMC10531590/)
  was acquired as complete Europe PMC XML and PMC HTML. Sections 2.4 and
  4.1-4.7 and Figure 5 captions describe NK851 in 5 g/L potassium-feldspar
  medium, 50 mL cultures, 10^7 cells/mL, 30 degrees C and 140 rpm, with
  untreated medium, HCl pH4, culture supernatant, ultrafiltered protein and
  protein-free comparisons. The general assays state n=3. The paper reports
  ICP-MS soluble K, not isolated potash or saleable feldspar. It does not
  verify a commercial ore/product scope or mineral phase/purity in the
  inspected methods. Section 4.5's 120,000 rpm conflicts with 12,000 rpm in
  section 4.2. Protein binding and structural prediction do not demonstrate
  that either EF-Tu or enolase causes dissolution; the discussion explicitly
  proposes later expression tests. Full figures/supplement were not reviewed.
  Retain as a strong mineral-group/powder follow-up, not an accepted commodity
  mechanism or a potash-production claim.
- **Magnesite:** [McCutcheon et al. 2019, DOI 10.1021/acs.est.8b07055](https://eprints.whiterose.ac.uk/id/eprint/145175/)
  was acquired as a repository accepted manuscript. Methods pp. 4-9 and
  results pp. 9-12 (manuscript numbering) plus rendered Figures 2-3 show a
  67-day, 10 m flow-through greenhouse bioreactor with natural cyanobacteria-rich
  mats, synthetic wastewater and nutrient additions. XRD, TEM-EDS and SAED
  support magnesite among a mixed carbonate assemblage. The inspected main
  methods have no matched sterile reactor or biological replicate series;
  the supplement acquisition returned an empty HTTP202 response. The quoted
  carbon-storage rates are projected from solution balances and idealized
  phase masses, not measured tonnes or purified magnesite recovery. Keep this
  as a mineral-species follow-up; do not equate mixed biogenic carbonates with
  the assessment's broad magnesite/magnesia commodity.
- **Potash:** Returned primary leads mostly involved potassium release from
  feldspar, fertilizer trials or broad biofertilizer screening. The inspected
  NK851 paper is not evidence that a water-soluble commercial potash product
  was recovered. No mechanism is adopted.
- **Sodium compounds:** Searches returned chemical carbonate crystallization,
  sodium-containing reagents and communities in soda-process waste. These do
  not show microbial production/recovery of the source-defined sodium commodity
  category. No mechanism is adopted; this bounded search does not establish
  absence of such research.

## Search, access, provenance and validation

Local deduplication included ignored and hidden files, followed relevant
symlinks and covered `data/records`, `research`, `reviews`, `history` and the
cited round9 graphite, round10 graphite, round10 B/F, expansion-authority,
`cmm-next-eu` and current raw directories. The pre-curation pass yielded 1,147
matching lines without path-access errors. No symlinks were found in those
bounded roots. Existing fluorine/phosphorus/magnesium records do not identify
these commodities. This is not a machine-wide absence claim.

Searches used web.run's returned default result pages without pagination;
exact queries are in JSON. Exact-title/DOI correction and retraction queries
for the examined phosphate, feldspar, barite and magnesite papers did not return
matching notices. This is a bounded integrity check, not proof that no notice
exists. Within-paper controls, fluoride inhibition, non-monotonic P, predicted
protein mechanisms and mixed mineral phases were retained as relevant limits.

Raw files remain outside Git at `/private/tmp/cmm-round12-industrial-minerals-raw`.
The retained MCS2026 and OR/24/059 PDFs are distinguished from fresh downloads.
USGS publications are government sources; UKRI, ASM and ACS materials retain
their copyright terms. The feldspar PMC XML states CC-BY terms. Reading access
does not establish rights to republish primary full text. Only original
curation and provenance receipts are saved in the repository.

The seven named records passed `cmmmech validate` (7 checked, 0 failed). A
magnesite chapter locator was intended to be corrected during that pass, but
the initially frozen record still incorrectly cited printed pp.118-119/PDF122-123
(Lithium). Independent review F1, issue #50, identified the persistence error. The fluorspar source-title attribution was
then normalized to the inspected USGS metadata and passed its named-file check. Actual `just new-history` CREATE sidecars
use codex / GPT-6 / codex and issue #48. Final hashes and validation results are
in the JSON. No Git/GitHub operation, shared README edit or whole-corpus test
was performed by this subtask.

## Post-review magnesite locator correction

On 2026-10-11T08:39:32Z, corrected the supporting USGS source to Magnesium Compounds,
printed pp.120-121/PDF124-125, after re-reading both pages and visually inspecting
PDF124. Added actual codex / GPT-6 / codex EDIT provenance linked to issue #50.
The original frozen hash and receipt remain in JSON `post_review_corrections`;
the current `records` receipt identifies the corrected bytes. Identity and
BGS criticality are unchanged. Named record validation passed (1 checked, 0 failed),
and trusted-base magnesite history validation passed (2 checked, 0 errors).
The initial saved review remains immutable and an independent successor assessment
is pending.
