# Tungsten mining-waste source investigation

Created 2026-10-11T17:42:44.987865Z; Codex `/root/round27_superalloy` (GPT-6). Worktree `/private/tmp/CMMMech-expansion-round29-20261011`, branch `curate/cmm-expansion-round29-20261011`, trusted base `7629ab50846229c87987d7fa0ac12389212bb70f`. [Machine-readable assessment and receipts](20261011T174244Z-source-investigation.json).

**Decision: retain a source-only deferral; no record or history created.** The original supplement and six publisher figures now provide a substantially better handoff, but the complete main methods, captions and tables remain inaccessible. This is not a completed scientific acceptance review.

## Scope, prior knowledge and duplicate checks

The assigned source is Han, Levett, Edraki, Jones, Howard and Southam, [*Accelerating bioleaching of tungsten mining wastes using indigenous acidophilic bacteria*](https://doi.org/10.1016/j.jhazmat.2023.131490), *Journal of Hazardous Materials* **454**, 131490 (2023), PII `S0304389423007732`, PMID `37121042`. Publisher metadata dates the issue 15 July 2023; indexed PubMed metadata gives online publication 25 April. The latter is not an experimental date. This was already a deferred lead in `research/ingests/round6-mo-w-20261011.json` and the round28 mineral handoff; the publication is not claimed as newly discovered.

Hidden and ignored files were included with `rg --no-ignore --hidden --follow` across current and original checkout `data/records`, `research`, `reviews` and `history`. Matching reports led to `/private/tmp/cmm-round14-mineral-raw`, `/private/tmp/cmm-round14-product-raw`, `/private/tmp/cmmmech-round6-mo-w-raw`, `/private/tmp/cmm-next-eu` and `/private/tmp/cmm-expansion-authorities-20261011`; these and this investigation's raw directory were searched. Commands, timestamps, output paths and errors are in the manifest and `/private/tmp/cmm-round29-tungsten-waste-research/dedup-*.json`. No accepted mining-waste resource or represented Han experiment was identified within those bounds. The existing tungsten element and scheelite mineral records use the distinct Blazevic 2019 study. Unrelated home/temp trees, Git internals and dependency trees were not searched.

## Acquisition and evidence actually inspected

| Artifact/route | Result | Evidentiary boundary |
|---|---|---|
| Publisher page and PDF, DOI, UQ `UQ:aac5c76` | Publisher/UQ returned 403 through available routes | Main body, original captions, tables and complete figure inventory not acquired |
| Crossref and Elsevier public metadata | Acquired; title, six authors, DOI/PII and journal agree | Elsevier XML is only 2,042 bytes of `coredata`, despite its full-text-response root |
| Elsevier full-view XML / text route | 401 / 400 | No authenticated endpoint was bypassed |
| OpenAlex | Acquired; lists DOI and PubMed locations with no PDF URL | Open-access status does not establish acquired full text |
| [Original supplement DOCX](https://ars.els-cdn.com/content/image/1-s2.0-S0304389423007732-mmc1.docx) | 81,730-byte real ZIP/DOCX; matching title/authors; complete text and four native-chart caches inspected | No main methods or metal-assay table; original rendered Word chart pixels and embedded OLE objects not adjudicated |
| Original CDN figure assets `gr1`–`gr6` | All six genuine JPEGs acquired and visually inspected | Their captions and any later figures remain unavailable; figure-set completeness is not established |

The main article is expressly CC BY 4.0 in Elsevier metadata; Crossref records that version-of-record license from 27 September 2023. The inspected supplement has no separate license statement. All bulk raw artifacts remain outside Git at `/private/tmp/cmm-round29-tungsten-waste-research/raw`. Each acquisition has exact URL, UTC time, status, byte count and SHA-256 in the manifest; unsuccessful responses are preserved as receipts, not mislabeled full text. The supplement SHA-256 is `eb2debbd8bfc51bde1f0f701f071b7c4421154e22423ffc56b57a24fb9692afd`.

## New findings and limits

**Feed and scale.** Original Figure 4 explicitly separates tailings and waste rock. These are experimental feeds, distinct from elemental tungsten, the wolframite mineral series and secondary precipitates. The available abstract calls the model laboratory/in-vitro. Figure 6 site photographs and an “in-situ” highlight do not demonstrate field or industrial deployment. Exact site, sample origin, waste-production history and preparation still require the main methods.

**Organisms and comparison arms.** Supplement S1 contains separate Fe/S stock categories from AMD sediments and biofilm; S2 uses `R+B+9k`, `R+B+M`, `R+M`, `T+B+9k`, `T+B+M` and `T+M`. The chart caches contain archaeal and fungal labels as well as bacterial groups. `Dothideales` and `Fimbriimonadales` appear in panels captioned genus-level, so the displayed labels should not be treated as a clean genus-only classification. Figure 2 is explicitly a nearest-named-representative/BLAST-identity heatmap, not experimental isolate authentication. It cannot support an authenticated *A. ferrooxidans* strain or a member-specific tungsten pathway. No taxon CURIE is adopted.

Figure 1 plots Fe-/S-oxidizing populations for all six resource/arm combinations, including nonzero signals in the `+M` arms. **Do not assume these arms are sterile abiotic controls.** Their actual definitions, inoculum/background community, sterilization status and chemistry must be read before assigning causal support. Microscopy in Figure 3 shows cell-like objects and deposits, but missing panel/sample mapping and preparation preclude taxon, mineral or viability assignments.

**Mass and denominator.** Figure 4 follows Bi, Mo and W cumulative extracted mass in micrograms through 180 days, with different tailings and waste-rock panels. The late W curves labelled `+B+9k`/`+B+M` exceed their `+M` counterparts; their chemical basis and causal attribution remain unverified. No endpoints were digitized or converted into percentages. Error-bar meaning, replication, solution sampling/replacement and extraction equation are unknown.

Figure 5 shows element-dependent treatment rankings. Its axes say cumulative mass in micrograms, while the waste-rock panel separately marks Ce, Mn and Zn in milligrams. Any future extraction must preserve those local unit overrides. Neither these masses nor the native community fractions meet the repository's exact `mg/kg` observation contract; no unsupported denominator conversion is proposed.

**Mineralogy and speciation.** The inspected primary abstract reports dissolution limited by secondary reprecipitation, naming gallium-rich tungstate and minor sanmartinite. The [CSIRO sanmartinite entry](https://spectroscopy.csiro.au/material/Sanmartinite) verifies nomenclatural context, ZnWO4 and grandfathered status, but cannot validate an experimental phase assignment. Main diffraction/XANES reference fits, uncertainty and alternative species are not inspected. The earlier “gaertnerite” shorthand remains unverified and is not adopted. No named gallium-rich mineral, W redox route, pure product or product-recovery yield is accepted.

## Search coverage, related evidence and notices

The manifest records every query, provider and access route. Searches used exact title/DOI/PII, institutional-repository and PDF terms, corrections/retractions, and wolframite/abiotic/control terms. Coverage was the first returned sets, without pagination or date filters. Broad article-number and generic-control queries were often unproductive. No affecting notice was identified in those returned sets; an unrelated vanadium erratum on a coauthor page is not a correction to this paper. Crossref has no populated relation/update-to notice in the acquired response. These are bounded observations, not proof of no corrections or contradictory work.

The related [Han paper DOI 10.1016/j.jhazmat.2022.130508](https://doi.org/10.1016/j.jhazmat.2022.130508), UQ `UQ:266c38f`, and [author thesis DOI 10.14264/9e55310](https://doi.org/10.14264/9e55310) are distinct acquisition leads. Their complete texts were not inspected and cannot fill missing methods by assumption. Determine experiment overlap before treating them as independent evidence. Secondary reviews were discovery aids only; they do not establish microbial causality. The target abstract's own secondary-precipitation limitation is already a reason to reject blanket extraction/recovery claims.

## Ranked handoff

1. Obtain a complete legitimate publisher or institutional main article through a working route. Current unchanged 403/401 routes should not be retried indefinitely. Read feed provenance, preparation, all arm/control definitions, medium/loading/inoculum, pH/temperature, replication, metal analytics, cumulative-mass calculation and all captions/tables.
2. Reconcile the already retained Figures 1–6 and S1/S2 with those methods. Preserve tailings versus waste-rock scope, `+M` background microorganisms, chemical matching, unit overrides and treatment-specific outcomes.
3. Inspect secondary-phase characterization and reference fits before accepting mineral species, aqueous W species or a redox mechanism. Keep microbial sequence neighbours separate from authenticated strains or causal roles.
4. Follow the earlier paper/thesis only when it closes a named gap; identify shared experiments. Then propose a narrowly supported resource record, canonical history and independent native review. No schema change is demonstrated.

A potential `secondary_resource` root requires verified waste/process origin; precise resource naming and slug remain deferred. Criticality is not proposed for the waste. No record/history was written, no record validation or independent scientific review is claimed for this research-only result, and no GitHub mutation occurred. The parent reports a passing round29 baseline separately. Report checks: JSON parsed, successful acquisition checksums verified, and this agent’s repository writes restricted to this dossier pair.
