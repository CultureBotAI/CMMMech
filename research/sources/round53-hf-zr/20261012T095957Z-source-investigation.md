# Hafnon source investigation

Recorded at 2026-10-12T09:59:57Z by codex (GPT-6; codex).

## Scope and reviewed state

Worktree `/private/tmp/CMMMech-expansion-round53-20261012`, branch `curate/cmm-expansion-round53-20261012`, trusted base `b85c2c2c753fe83a2fc21f073ee1e49675ae647e`. This follows the round52 natural-hafnon citation lead. The parent reused completed fresh checks at this exact base; this report does not claim a new baseline run.

The proposed owner is [`hafnon.yaml`](../../../data/records/hafnon.yaml), a mineral species with IMA accession 1974-018. The contribution supports identity and qualified natural-occurrence context. It adds no microbial mechanism, recovery claim or inherited criticality. Canonical CREATE history: [`2026-10-12T095809Z-codex-8232d0.yaml`](../../../history/records/hafnon/2026-10-12T095809Z-codex-8232d0.yaml). Independent scientific review remains separate.

## Acquisition and candidate decisions

| Source and exact route | Actual evidence | Decision |
|---|---|---|
| [Pereira, Ávila and Neumann 2004](https://revistas.ufrj.br/index.php/amn/article/view/48745); [official PDF](https://revistas.ufrj.br/index.php/amn/article/download/48745/26398) | Complete 16-page original acquired; all nine figures and seven tables personally inspected | Use narrowly for its source-reported natural occurrence and sampling context |
| [IMA September 2026](https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf) | Fresh original download; page 1 definitions and page 88 row inspected | Hafnon, Hf(SiO4), approved, 1974-018, Mozambique |
| [Handbook of Mineralogy](https://www.handbookofmineralogy.org/pdfs/hafnon.pdf) | Complete original one-page version 1.2 (2001) inspected | Secondary identity context; keep synthetic constants separate |
| [Exact 2003 institutional PDF](https://repositorio.usp.br/directbitstream/d330411f-b8b2-46cb-80d7-b160452b194d/1764785.pdf) | Indexed text identifies the original, but the direct download returned HTTP 503 and web open timed out | Defer original microanalyses and figures |
| [Author-uploaded 2003 copy](https://www.researchgate.net/publication/354689605_BORDA_DE_HAFNAO_ZIRCONIFERO_EM_ZIRCAO_HAFNIFERO_DA_MINA_DO_VOLTA_GRANDE_PROVINCIA_PEGMATITICA_DE_SAO_JOAO_DEL_REI_MINAS_GERAIS_BRASIL) | Daniel Atencio upload dated 2021-09-19; web reader identifies a 14-page scanned copy with CETEM 2005 cover. Direct PDF returned 403; screenshot responses supplied no usable original images through the tool | Discovery/access lead only; not a complete visual or textual source review |
| Official Mineralis search | Python TLS validation failed; system curl accessed the current public search without disabling TLS checks. Exact query `hafnão` returned no results | Bounded negative query, not repository-wide absence |

Exact queries, successful and failed URLs, acquisition UTC times, formats and checksums are in the paired JSON and outside-Git acquisition receipts. No old unchanged 1974/2013 denied route was retried. Portal posting of the 2004 paper in 2021 is a migration date, not a new publication or experiment.

## Claim-level assessment

The 2004 paper examines cassiterite from eight concentrate samples. Printed pages 324–325 locate the body-E sample in a stream crossing the Volta Grande pegmatite; it is not the separately accessioned body-A museum sample. Table 2 assigns source-reported zirconian hafnon to the body-E column. Methods on page 325 use polished carbon-coated sections, BSE imaging and semiquantitative SEM-EDS.

Pages 326 and 332 explicitly cite overlapping 2002/2003 work for hafnon. The occurrence is therefore retained as source-reported context, without treating the later paper as an independent replication or importing its inherited composition range. The image labels for hafnian zircon do not independently demonstrate a hafnon diffraction refinement. Geological interpretations on pages 332–334 do not establish a controlled transformation experiment.

The Handbook identifies its cell parameters, calculated density and powder diffraction as synthetic. Those constants and its older natural-chemistry summaries are not transferred into measurements of this Brazilian sample. IMA's Mozambique discovery-country field is distinct from the sampled Brazilian occurrence.

## Citation discrepancy and remaining access gap

The 2007 bibliography reverses the rim/core wording of the 2003 title relative to the author-uploaded title and the 2004 bibliography. Its first-occurrence sentence cites 2003a, while its 48.3 wt.% HfO2 sentence cites 2003b, whose bibliography concerns Guaraú zircon/columbite. The exact natural 2003 primary is now located, but its analyses remain uninspected. This report does not silently resolve the attribution or copy that measurement into the record. The 2004 conference report is also not counted as a new experiment.

## Deduplication and notices

The cycle-safe inventory includes hidden and ignored files and follows symlinks in current and original `data`, `research`, `reviews` and `history`, plus 177 available cited raw roots. It inspected 4092 corpus text files and 7607 total text files. Nine cited roots were unavailable; ten files over 16 MB and unextracted binary content remain limits. Exact paths and matches are retained in `dedup.json`. No maintained hafnon owner was found within this boundary before curation; baddeleyite mentions the species, and prior research preserves its acquisition gaps. This is not a machine-wide absence claim.

Bounded live author/title/hafnon queries with correction and erratum terms returned no affecting notice. Later citations confirmed the older occurrence lineage, not a new independent dataset. No exhaustive notice or biological-literature search is asserted.

## Handoff and priorities

1. Independently review the frozen hafnon owner against the complete 2004 original, IMA and Handbook, retaining the explicitly limited occurrence claim.
2. Acquire usable original 2003 pages and microanalysis tables through the located institutional/author routes when access changes. Resolve the 2007 citation error and check phase assignment and rim/core wording before importing any older chemical measurements.
3. Retain the 1974/2013 natural-source gaps and synthetic-source distinction. No additional Hf/Zr candidate is needed for this bounded contribution.

All raw originals stay in `/private/tmp/cmm-round53-hf-zr-research/raw`. The paired JSON lists every retained raw artifact hash, precise inspection coverage and source terms. No schema, shared documentation, site, Git or GitHub changes were made by this curation task.
