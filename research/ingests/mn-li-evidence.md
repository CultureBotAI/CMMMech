# Manganese and lithium ingest evidence

Curator: Codex (GPT-6), 2026-10-09 UTC. This is a curation handoff, not an
independent acceptance review. Input: source candidates M3/M4 in
`research/sources/cmm-landscape/20261008T073140Z.md` and its acquisition JSON.
The existing retained Frontiers HTML/text files were re-read locally and their
publisher pages opened live on 2026-10-09. Bulk article bytes are not imported.

Hidden/ignored-inclusive searches of `data`, `reviews`, `history` and the
assigned research directory found no pre-existing manganese or lithium element
record before this pass. Cobalt's battery context mentioning both elements is
not a duplicate element record. Other worktrees and unrelated temporary files
were outside this deduplication boundary.

## M4: manganese

- Primary experiment: [Wright et al. 2018](https://doi.org/10.3389/fmicb.2018.00560),
  culture conditions, LBB assay, Mn(III)-L oxidation experiments, Fig. 1 and
  Table 4. Read discussion and Fig. 3 for abiotic Mn(III)-DFOB production and
  the distinction between accumulation and biological oxidation.
- Table 4 endpoints have different durations: Mn(II) and Mn(III)-citrate at
  96 h; Mn(III)-DFOB at 168 h. They are not matched-time rates or purified-product
  yields. The assay assumes particulate MnO2 when converting oxidizing
  equivalents; it does not resolve a crystalline oxide mineral.
- Genetically altered strains support involvement of MnxG/McoA, with light
  dependence discussed for MopA. Supplementary light/dark experiments were not
  acquired in this pass; the record states that the discussion reports them.
- [NCBI Taxonomy 76869](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=76869)
  resolves to the exact current label Pseudomonas putida GB-1, rank `no rank`.
  It is a strain-level named entry; mutants remain experimental variants.
- [ChEBI 18291](https://www.ebi.ac.uk/chebi/CHEBI:18291) was inaccessible through
  web-reader routes but successfully fetched from the public authority with
  Python urllib. The HTML confirms manganese atom, formula Mn, charge 0,
  SMILES `[Mn]`. Retained file `/private/tmp/cmm-ingest-manganese-chebi.html`,
  downloaded during 2026-10-09T04:45Z; SHA-256
  `edc89d5cdd2d78be433f2fc1793dff9032c734efd5f8c39cb26d826f59ee3684`.

## M3: lithium

- Primary experiment: [Kirk et al. 2024](https://doi.org/10.3389/fmicb.2024.1467408),
  methods 2.1-2.3, results 3.1-3.4, Table 1, Figs. 1/4/5.
- The detailed jadarite results narrow the abstract: uninoculated acidic medium
  reaches similar dissolved Li at day 30; sulfuric acid alone releases more.
  The accepted claim is a transient comparison, not a final yield advantage.
  Spodumene/lepidolite comparisons show no material microbial enhancement.
- Methods call 2 g in a final 200 mL 2% w/v; arithmetic implies 1% w/v.
  The inconsistency remains unresolved. No normalized yield was imported.
- Nominal pH 1.8 is not stable control: addition of the jadarite-bearing material
  initially raises pH to 7 and demands repeated acid additions. Acid treatments
  receive different amounts. Methods mention initial 0.29 mL 5.5 M acid and
  later 0.1-0.6 mL additions, whereas Figs. 1/4/5 captions mention 2,500 microliters
  acid. These are not harmonized into an acid-consumption comparison.
- The paper reports an in-lab ore-derived culture, no collection strain or
  sequence accession. [NCBI 920](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=920&mode=info)
  verifies the species name Acidithiobacillus ferrooxidans. This normalizes the
  paper's misspelled genus, without independently confirming the culture.
- [ChEBI 30145](https://www.ebi.ac.uk/chebi/CHEBI:30145) verifies neutral lithium
  atom, not the lithium(1+) ion. Mineral mixtures remain mechanism context.
- The source survey could access Mendeley V1 metadata but not its raw data.
  This pass therefore imports no raw observations and does not claim raw-data
  replication. Supplementary acid-dose data were not acquired in this pass.

## Authority and bounded discrepancy searches

The complete [USGS final 2025 table](https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm)
was read live; the explicit Lithium and Manganese rows are on p. 50496.
Both records retain the commodity-to-element mapping and the dated edition.

Web searches on 2026-10-09, first returned result sets, no date/domain filter:

- `"10.3389/fmicb.2018.00560" correction retraction`
- `"10.3389/fmicb.2024.1467408" correction retraction`
- `"10.3389/fmicb.2018.00560" "correction"`
- `"10.3389/fmicb.2024.1467408" "retraction"`
- `"Bioleaching of lithium from jadarite" "correction"`
- `"Oxidative Formation and Removal" "retraction"`

No directly applicable correction/retraction was identified in these bounded
results or the inspected publisher pages. This is not an exhaustive assertion.
Search found a later lead, *One-Step Lithium Bioleaching from a Mineral
Concentrate: Comparison Between Consortium and Isolated Native Strains*;
[PMC route](https://pmc.ncbi.nlm.nih.gov/articles/PMC13362697/) presented a browser
challenge, so its methods were not verified or ingested. It is a follow-up for
coverage, not treated as independent confirmation or contradiction.

Validation is run on both files after adding actual current curation sidecars;
the independent record reviews will record final hashes and acceptance results.
