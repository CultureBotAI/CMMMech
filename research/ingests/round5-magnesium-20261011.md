# Magnesium curation dossier

The [magnesium record](../../data/records/magnesium.yaml) adds a new element
root from the [round4 frontier](round4-frontier-20261011.md). The underlying
Suyamud study was already a deferred lead; this is evidence completion, not a
claim of discovering an unknown paper. Exact search and acquisition receipts
are in [the companion JSON](round5-magnesium-20261011.json).

## Identity and authority

[ChEBI:25107](https://www.ebi.ac.uk/chebi/CHEBI:25107) resolves to magnesium
atom, Mg, charge zero. The [official US 2025 final notice](https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm)
lists Magnesium explicitly. Its commodity designation maps to the element;
struvite, dittmarite, glushinskite and magnesium metal production are distinct.
[NCBI 380704](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=380704&mode=Info)
resolves the named ATCC 1015 strain.

## Primary evidence and curation decision

[Suyamud et al. 2020](https://doi.org/10.1111/1462-2920.14949),
Environmental Microbiology 22:1588-1602, was inspected through the
[author repository PDF](https://discovery.dundee.ac.uk/ws/files/48409012/1462_2920.14949.pdf).
The record selects its solid-medium experiment and phase evidence in Figures
3-5, Table 2 and Experimental procedures. It preserves the explicit dittmarite
identification of the synthetic feed. It does not import the paper's malformed
Discussion reaction equation as a chemical mechanism, nor infer a recovery
percentage from crystal formation. Liquid-medium magnesium endpoints and
pellet accumulation remain uncurated in this batch.

Ordinary publisher and repository downloads returned HTTP 403. The web PDF
parser supplied full Methods/Results text and captions; screenshot calls did
not yield visible images in this interface. No direct diffraction-image
reinterpretation is claimed. The article and repository identify CC BY;
raw full text is not committed. Correction/retraction and supplement searches
were bounded and their exact queries/access limitations are retained in JSON.

## Repeatable next work

An independent reviewer should confirm phase, strain, conditions, list mapping
and control limits against the cited primary text. A later extension can audit
liquid-culture mass balance or create separately grounded mineral identities.
The present record needs neither a schema change nor invented measurements.
