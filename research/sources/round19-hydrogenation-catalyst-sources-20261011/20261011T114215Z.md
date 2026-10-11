# Round 19: hydrogenation catalyst and automotive sludge source investigation

## Scope and provenance

UTC report time: 2026-10-11T11:42:15.508365Z. Researcher: Codex, GPT-6, agent
`/root/round19_hydrogenation_catalyst`. Worktree:
`/private/tmp/CMMMech-expansion-round19-20261011`; branch
`curate/cmm-expansion-round19-20261011`; trusted base
`c4b2a6c21a2ff54d1fdd3965ac98a6d90effba7a`. The root coordinator observed baseline
`just check` terminal exit 0 before record writes: 308 passed, 3 skipped,
138 records and 154 histories. This lane adds two records and actual CREATE
sidecars; no existing record, schema or governed file is edited.

The question was whether Bosio's spent vegetable-oil hydrogenation catalyst
could support a distinct material and complete microbial mechanism. Its
accessible material description, checked against full IFC process guidance,
supports identity; missing full experiments still prevent a mechanism. A
reference-following search located a complete primary paper for a separate
automotive wastewater-treatment sludge. That laboratory study supports narrow
biogenic-acid leaching evidence with important control and reporting limits.
Neither resource inherits elemental criticality. No criticality-list assessment
was conducted in this lane.

Novelty checks included hidden/ignored files and followed relevant symlinks over
`data/records`, `research`, `reviews`, `history`, and the named round18/19 catalyst
raw directories. Successful searches used `rg --no-ignore --hidden --follow -n -i`
with catalyst terms `hydrogenation|2007.10.095|Bosio` and sludge terms
`automotive.*sludge|wastewater-treatment-sludge|Yagnentkov|AMR.71-73.649|DSM 11478`.
Receipts: `/private/tmp/cmm-round19-catalyst-dedup.txt` and
`/private/tmp/cmm-round19-sludge-dedup.txt`. No same-identity record was found in
these boundaries before creation; adjacent hydrocracking/HDS/FCC records and the
round18 Bosio handoff were found. An initial command named a nonexistent
`/private/tmp/cmm-round17-secondary-raw`; its exit 2 is not negative evidence.
The successful bounded rerun omitted that nonexistent directory. These are not
machine-wide or literature-exhaustion claims. Binary PDFs were inspected with
PDF tools rather than relying on text-search completeness.

## Candidate inventory and evidence checked

| Source | Actual access and locators | Decision |
|---|---|---|
| [Bosio, Viera and Donati 2008](https://doi.org/10.1016/j.jhazmat.2007.10.095), J Hazard Mater 154:804-810, PMID 18079054 | Publisher abstract, introduction, Spent catalyst section excerpt, chemical-leach excerpt and conclusion; Crossref and PubMed identity | Accept material-origin context only; no mechanism, assay numbers or product yield |
| [IFC 2015 vegetable-oil guidance](https://www.ifc.org/content/dam/ifc/doc/2010/2015-vegetable-oil-processing-ehs-guidelines-en.pdf), dated 12 February 2015 | Complete PDF acquired; paragraphs 8-9 pp2-4 and paragraph56 pp23-24 read; pp3 and23 rendered and viewed | Accept distinct spent catalyst/filter-aid resource context; historical guidance, not criticality or deployment |
| [IFC 2007 retired predecessor](https://www.ifc.org/content/dam/ifc/doc/2000/2007-english-vegetable-oil-processing-retired.pdf), dated 30 April 2007 | Complete PDF acquired; pp3 and13 read | Confirms predecessor process context; not a current legal claim and not substituted for 2015 edition |
| [Yagnentkovsky, Viera and Donati 2009](https://doi.org/10.4028/www.scientific.net/AMR.71-73.649), AMR71-73:649-652 | Complete CONICET publisher-layout PDF; pp649-652, all Figures1-3, appended reference-link page; pp650-651 figures rendered/viewed | Accept distinct sludge and conditional laboratory leaching; no pure-product recovery or microbial superiority |
| [DSMZ DSM11478](https://www.dsmz.de/collection/catalogue/details/culture/DSM-11478) and [NCBI930](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=930&mode=Info) | Live catalogue and taxonomy; downloaded HTML/XML | Verify Tth04 strain designation and species CURIE separately |
| [Garole and Sawant 2012](https://www.isca.me/rjcs/Archives/v2/i12/6.ISCA-RJCS-2012-184.php), Res J Chem Sci2(12):27-30 | Full four-page PDF text read, including methods and figure captions; figures not visually adjudicated | Context/lead only; chemical process has conflicting purification/product and temperature accounts; not curated mechanism |

## Scientific boundaries and contradictions

The catalyst record denotes nickel-bearing oil-hardening residue, including
filter-aid mixtures. It is not renewable-diesel hydroprocessing feed, spent
bleaching earth, fresh Ni catalyst or pure nickel. IFC2015 explicitly excludes
biofuel production from its scope. Bosio's visible source material section
identifies organic material and diatomaceous earth in its selected sample.
General industrial-origin context does not prove industrial microbial treatment.
Bosio's reported bacterial dissolution and later sulfide precipitation remain
separate, unaccepted claims until full preparation, culture state, conditions,
controls, products and balances can be inspected. The chemical-leach excerpt
already cautions against assuming microbial necessity. No excerpt percentage is
imported. OpenAlex returned only publisher and PubMed locations, with no OA URL;
that index does not prove no legitimate copy exists elsewhere.

The automotive-sludge paper provides factory wastewater-treatment origin but
neither factory identity nor enough production-process detail to rename it
unambiguously as electroplating sludge. Ni/Zn host phases remain unresolved.
Its living DSM11478 culture acidifies sulfur medium upstream; prepared sludge
is treated downstream. No filtration or centrifugation is reported between
stages, so the record does not call the lixiviant cell-free. Stabilized acid
production was used to infer biofilm attachment; direct attachment imaging was
not reported. Commercial-acid and uninoculated controls are not described in
the complete four-page paper. Accordingly, it supports conditional mobilization,
not microbial enhancement over equivalent acid chemistry.

Figure3 has no exact numerical table or defined error bars. Its pH2 higher-solids
arms perform worse, while some near-complete bars reach around or above the
nominal total. The percentages are not imported as exact yields; neither a
calculation denominator formula nor full solid/liquid balance is reported.
Methods give sulfur column B as 54% whereas conclusions say 50%; leach methods
say dilution0.21/h while results say0.22/h. Figure1 proton-axis `mM` values are
ambiguous relative to pH and should not be silently corrected. These limits
preclude an exact optimized productivity claim. The 360mL volume and15mL/h
nominal flow do not justify inventing an explicitly reported24h endpoint.
Liquid AAS and dissolution do not establish isolated metal recovery.

DSMZ confirms DSM11478=Tth04 and Brazilian mine-drainage provenance, including
Donati deposit history. NCBITaxon930 is a species identifier, not a strain ID;
no genomic accession or strain-CURIE is invented. No quantitative observation
rows are added: reported graph percentages and mg/g feed composition do not
satisfy the current exact-table mg/kg concentration-cell contract.

Garole2012 describes a local soap-industry sample but disagrees internally:
abstract/conclusion use a calcium-oxalate purification path, while methods
introduce NaF/HF and Mg; final product changes between nickel carbonate and
chloride. Temperatures and acid-comparison yields also differ. Its data are not
used to complete Bosio's unavailable microbial experiment.

## Searches and access log

All following exact queries used web search on 2026-10-11 UTC, first returned
set only, without pagination or date/domain filters beyond query text. Search
result publication/recrawl ages were not treated as article edition dates.

- `"10.1016/j.jhazmat.2007.10.095" pdf`
- `"Bosio" "Viera" "Donati" "nickel" catalyst 2008 full text`
- `site.sedici.unlp.edu.ar "Recovery of nickel" catalyst Bosio`
- `"Integrated bacterial process for the treatment of a spent nickel catalyst"`
- `"Bosio" "Viera" "Donati" "catalizador" níquel 2008`
- `"Integrated bacterial process" "Bosio" repository`
- `"Recovery of Nickel and Zinc Using Biogenerated Sulphuric Acid"`
- `"2007.10.095" "pdf" -site:researchgate.net -site:sciencedirect.com -site:diva-portal.org`
- `site.sedici.unlp.edu.ar "Bosio" "catalizador"`
- `site.ri.conicet.gov.ar "Integrated bacterial"`
- `"spent nickel catalyst" "Bosio" correction retraction`
- `"Integrated bacterial process" filetype:pdf`
- `site.ifc.org "Vegetable Oil" "nickel" "catalysts" pdf`
- `"Bosio" "Integrated" "nickel" site:core.ac.uk`
- `"Bosio" "Integrated" "nickel" site:sedici.unlp.edu.ar`
- `"Recovery of Nickel and Zinc Using Biogenerated Sulphuric Acid" correction OR retraction OR supplement`
- `"Yagnentkovsky" "sludge" "sulphuric" control`
- `"Acidithiobacillus thiooxidans" "DSM 11478" dsmz`
- `"automotive" "sludge" "Yagnentkovsky" bioleaching commercial acid`
- `"Recovery of Nickel and Zinc Using Biogenerated Sulphuric Acid" erratum`
- `"Bosio" "nickel catalyst" "abiotic" sulphuric`

Targeted corrections/retractions/errata queries did not expose a specific notice
in the returned sets; this bounded negative result is not proof of absence.
No supplement or data accession was listed on the inspected 2009 publisher page
or four-page article. No data dictionary, bulk tabular dataset or update policy
was available there; these fields are therefore not applicable to a dataset
import. The sludge graph remains a graph, not a source table.

Initial direct downloads failed DNS inside the sandbox; a permitted network
retry retrieved actual PDFs, HTML/XML and JSON. Bosio direct publisher fetch
returned403 despite browser-tool excerpts being readable. Public repository
searches and OpenAlex did not yield a verified full copy. The initial guessed
IFC2007 URL failed in the web tool; the discovered retired-file URL succeeded.
CONICET's handle page failed through the web tool, but its public bitstream
returned a valid five-page PDF. Download content types, PDF parse/page counts,
exact times and SHA-256 values are retained in the paired JSON. The final
Crossref-linked Elsevier API attempt returned HTTP200 and valid XML containing only core metadata (1,833 bytes); it did not deliver article methods or figures. This is recorded separately.

Raw artifacts remain outside Git at
`/private/tmp/cmm-round19-hydrogenation-catalyst-raw`.
The 2009 publisher PDF explicitly reserves all rights; public author-repository
availability does not grant redistribution rights. Bosio publisher text is
Elsevier copyright/all rights reserved. IFC raw documents and ISCA article are
retained for research; a redistribution license was not established in this
pass. DSMZ/NCBI catalogue data were read for identifiers, not bulk redistribution.
No raw articles, figures, abstracts or downloaded databases are committed.

## Priorities and handoff

1. Independently review both new record states and their CREATE histories;
   individual structural validation succeeded, while scientific acceptance and
   full batch gates remain the coordinator/reviewer responsibility.
2. Acquire Bosio2008 complete primary evidence through a legitimate institutional
   or author repository, including leaching/precipitation controls and recovered
   solid characterization. Add a mechanism only if those details support it.
3. Inspect the linked [2011 UNLP thesis](https://sedici.unlp.edu.ar/bitstream/handle/10915/2706/Documento_completo.pdf?sequence=1)
   for experimental overlap and missing controls of the2009 sludge study.
   Only search excerpts were seen this round; no thesis data are accepted.
4. Reassess the existing spent-three-way-catalyst lead in
   `research/ingests/round12-aluminium-boron-20261011.md` using the rediscovered
   [2023 author-deposited PDF](https://rodin.uca.es/bitstream/handle/10498/30253/S0301479723016134.pdf?isAllowed=y&sequence=1).
   The round12 dossier already records a full eleven-page version of record
   for Compagnone et al., DOI10.1016/j.jenvman.2023.118825, and unresolved
   supplement/Mendeley dataset c96gpb6zpm/1 access. Resume those exact gaps and
   determine the spent-catalyst resource boundary. This lane inspected only
   the search excerpt and prior dossier, not the full article anew; the route
   is neither a newly discovered study nor new accepted mechanism evidence.

## Curation receipts and limits

- `data/records/spent-vegetable-oil-hydrogenation-catalyst.yaml` — SHA-256 `4805ee17fbc683dc7cd6cd1a314493ab3a770b20987c4853dbb330eb2b61cbe4`; history `history/records/spent-vegetable-oil-hydrogenation-catalyst/2026-10-11T114047Z-codex-36ce3e.yaml`. `uv run --locked cmmmech validate data/records/spent-vegetable-oil-hydrogenation-catalyst.yaml` exited 0 at 2026-10-11T11:40:50.429664+00:00.
- `data/records/automotive-wastewater-treatment-sludge.yaml` — SHA-256 `e26dec67a01c947e377d5a54e2c787b0f7d1474518a417ccb1a116942e4f5ac6`; history `history/records/automotive-wastewater-treatment-sludge/2026-10-11T114051Z-codex-5e4461.yaml`. `uv run --locked cmmmech validate data/records/automotive-wastewater-treatment-sludge.yaml` exited 0 at 2026-10-11T11:40:54.552278+00:00.

No independent review is claimed by this curator report. No schema changes were required. The catalogue is not scientifically exhausted: the named access gaps and adjacent source leads remain.
