# Copper and chalcopyrite evidence, expansion round 1

Opened 2026-10-11 UTC by Codex (GPT-6). Base `76cd81d310a6ccb4cf7bdebcc61be050d0863222`,
worktree `/private/tmp/CMMMech-expansion-20261011`, branch `curate/cmm-expansion-20261011`.
This is curation research, not an independent record review or a claim of search exhaustion.

## Search and evidence inspected

Hidden/ignored-inclusive search across `data`, `research`, `reviews`, and `history`
for copper/chalcopyrite found earlier copper-inhibition discussion in palladium
reviews, but no existing root copper/chalcopyrite record in this checkout. The
initial authoritative corpus contained ten records. Download inspection is limited
to the directories named here and previously cited acquisition manifests; the
original Documents checkout remains inaccessible to the shell.

Web search on 2026-10-11, one returned result set per query, no pagination:

- `copper chalcopyrite bioleaching Acidithiobacillus primary study PMC bioleaching controlled experiment`
- `2025 final list critical minerals 60 selenium copper tellurium Federal Register November 7 2025`
- `"Weak Iron Oxidation by Sulfobacillus" "10.3389"`
- `site.ebi.ac.uk/chebi "copper atom"`
- `"Weak Iron Oxidation" correction retraction`
- `site.ncbi.nlm.nih.gov/Taxonomy "Sulfobacillus thermosulfidooxidans" "Taxonomy ID"`
- `site.ncbi.nlm.nih.gov/Taxonomy "Leptospirillum ferriphilum" "Taxonomy ID"`
- `site.ncbi.nlm.nih.gov/Taxonomy "Acidithiobacillus caldus" "Taxonomy ID"`

The correction query returned the original study and citing work; it did not
establish a correction or retraction in that bounded result set. This is not a
global negative claim. PMC's web route returned a browser challenge. The
[publisher full text](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2018.03059/full)
and the [Europe PMC full-text XML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6315122/fullTextXML)
were accessible. They are two representations of the same experiment.

The XML, issuing-source ChEBI page, and complete GovInfo final-list notice were
downloaded to `/private/tmp/cmm-expansion-copper-20261011/`; exact URLs, acquisition
times and SHA-256 hashes are in [the receipt](expansion-copper-20261011-acquisition.json).
The paper states CC BY licensing. Full text is retained outside Git; this dossier
records facts and claim decisions, not an imported article. Identity: ChEBI:28694
resolves to copper atom, Cu, zero charge. The complete final US2025 notice names
copper in its summary and table; the record asserts that edition, not timeless
criticality. The identifier grounds an element, not the experimental copper ions.

NCBI species pages 33059, 28034 and 178606 were opened and their current names,
rank and listed type strains checked. They corroborate the names used for DSM
8584, DSM 9293 and DSM 14647 in the paper. The YAML intentionally uses species
IDs and records exact experimental strains separately; no genome sequencing of
the experimental inocula is inferred.

## Claim decisions

Primary experiment: Christel et al. 2018, DOI `10.3389/fmicb.2018.03059`.
Inspected complete Methods, the Bioleaching of Chalcopyrite Concentrate results,
Figure 1 caption, discussion and conclusion; gene-level claims are not curated.

| Claim | Locator and disposition |
|---|---|
| Defined-culture leaching of chalcopyrite concentrate | Mineral, Bacterial Strains and Growth Conditions, and Bioleaching Experiments Methods. Record pretreatment, three DSM strains, inoculum basis, initial pH, loading, temperature, shaking and replication. |
| Largest initial copper concentration in the A. caldus/S. thermosulfidooxidans pair | Results and Figure 1C: 14.2 +/- 0.3 mM, mean +/- SD, n=4. Retain as total released Cu, not dissolved-only Cu or isolated product. |
| Abiotic dissolution and non-optimal consortium | Results: control 2.4 +/- 0.3 mM Cu at 15 days; three-species mixture underperformed all pairs. These qualify rather than erase the narrow biological observation. |
| Unequal elapsed times | Runs stopped 14 days after redox-defined onset; total durations 14-20 days. Do not compute a common-time effect or rate from endpoints. |
| A. caldus alone | Late iron oxidation was attributed to possible surviving environmental bacteria; do not assign iron oxidation unequivocally to A. caldus. |
| Analytical fraction | Methods: heated HCl slurry digest followed by AAS includes released dissolved and precipitated Cu. No purified-product yield. mM prose is not forced into the mg/kg concentration-observation schema. |
| Redox mechanism | Initial AS/S groups lower than groups with L. ferriphilum, but the seven-run AS repeat reached 593 +/- 15 mV. No universal 550 mV ceiling is asserted. Low-affinity iron oxidation, attachment and candidate genes are interpretive. |
| Mineral purity | Paper claims >98% purity from digestion/elemental analysis and 29.5% Cu. Those values are not reconciled here into an independently measured phase purity; possible accompanying bornite is noted. |
| Industrial scale | Authors explicitly call for large-scale testing; background industrial bioleaching statistics do not establish deployment of this particular consortium. |

## Expansion leads

- Chalcopyrite is a distinct mineral-species candidate; copper's US designation
  must not be inherited by it. Its formula is given as CuFeS2 in this primary
  article. A dated IMA master list was acquired in a previous discovery round at
  `/private/tmp/cmm-source-datasets-downloads/ima-master-2026-09.pdf`; any new row
  claim requires inspecting the actual row and dictionary.
- Cited primary redox-control study: Masaki et al. 2018, DOI
  `10.1080/01490451.2018.1443170`, Geomicrobiology Journal 35:648-656. Identified
  from the reference list; methods not yet read. Candidate additional mechanism
  evidence, not an independent accepted observation here.
- Other search leads include primary low-grade chalcopyrite consortium assays
  (`PMC3833157`, `PMC6974477`, `PMC9088944`) and the chloride-tolerant Cutipay
  experiment (`PMC4884008`). Full texts not assessed in this round; material
  identity must be deduplicated before new records are added.
- Bornite and pyrite are related distinct mineral candidates surfaced by the
  selected paper. Their mention does not establish a demonstrated mechanism or
  critical designation for either root material.

Candidate discovery remains open. Independent per-record review and validation
are separate acceptance steps, with exact final hashes captured after history.
