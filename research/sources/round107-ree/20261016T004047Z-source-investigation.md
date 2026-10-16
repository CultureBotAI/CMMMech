# Round107 rare-earth source investigation

UTC: 2026-10-16T00:40:47.854185+00:00. Researcher: codex (GPT-6; codex), /root/round104_ree.
Worktree: /private/tmp/CMMMech-expansion-round107-20261016; base 27d842b3e6239bf60565f93c958d3f2cad395037; dedicated branch curate/cmm-expansion-round107-20261016.
This dossier records source investigation and curation handoff, not an independent review verdict.

## Scope and decision

Added lanthanite-(Nd), a hydrated Nd-dominant carbonate, and xenotime-(Yb), a Yb-dominant phosphate. Both have freshly checked September2026 IMA authority and primary natural-specimen characterization. These are distinct species, not elemental Nd/Yb, REE commodities or concentrate resources. No criticality or microbial mechanism is inferred.

The paired [JSON](20261016T004047Z-source-investigation.json) records exact queries, acquisition times, failed routes, file hashes, claim locators, owner/history hashes and named validation.

## Evidence checked

| Source | Inspected material | Decision and limits |
|---|---|---|
| [IMA September2026](https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf) | Fresh official PDF; definitions p1 and rows pp121/236 visually checked | IMA1979-074 lanthanite-(Nd), IMA1998-049 xenotime-(Yb); mineral identity, not criticality |
| [Morrison et al.2013](https://doi.org/10.1107/S1600536813003164) | Complete downloaded PMC HTML, rendered supplementary crystallographic information/tables, original Figures1-3 | Natural mixed-REE specimen;23-point microprobe average; water by difference; all REE modeled as Nd; hydrogen positions excluded |
| [Buck et al.1999](https://www.frankhawthorne.com/_files/ugd/70a3a9_2d8c306f59d549588c28170df5e36c15.pdf) | Entire4-page original, both tables, all page renders | Mixed natural grains; low analytical totals and powder limitations retained; density calculated; no verified DOI |
| [Vallina et al.2015](https://doi.org/10.1039/C5NR01497B) | Entire14-page published version, Tables1-3, Figures1-10 | Useful abiotic transformation lead deferred: SI unavailable and exact experimental timing/phase labels conflict |

Morrison's full article was available through PMC even though direct publisher PDF routes failed. Three nominal PMC PDF/CIF/HKL downloads returned HTML challenges; they are retained only as failed-acquisition evidence. No original CIF or reflection file was verified, and no full visual PDF inspection is claimed. The source-reported RRUFF R060993 is a specimen lead, not a separately verified record identifier.

Buck's Table1 separates three spots on one diffraction grain from a second embedded grain. The first low total is attributed to charging by the authors, not corrected here. Powder diffraction supports a xenotime pattern but there was no suitable single crystal for structural refinement. The abstract and body give different ordinary refractive indices,1.715(3) and1.717(3); numerical optics are omitted from the owner. Geological fluoride-complex discussion is not experimental extraction.

## Deferred abiotic experiment

Vallina2015 used synthetic Nd nitrate and sodium-carbonate solutions, with wet aging, dry storage, heating and hydrothermal treatments kept separate. Table2 describes room-temperature lanthanite followed by a mixed tengerite/lanthanite product; these phase percentages are not Nd recovery yields. The paper also reports a dry-storage null and a60C pathway bypassing lanthanite.

Three original conflicts matter before any time-specific curation: Table2 calls the21C4h material amorphous while the morphology text calls it lanthanite; Figure6b reverses the24h/60d phase labels relative to Table2/narrative; and the separate dry-heated Nd dioxycarbonate is inconsistently called monoclinic, hexagonal and cubic. Figure10 also labels90C where methods/table use95C. These are retained as source conflicts, not silently repaired. Acquire original SI indexing/spectra and resolve sample provenance before an exact-condition mechanism is accepted. The experiment has no microbial component.

## Search and provenance limits

Searches included hidden/ignored files and followed relevant symlinks in records/research/reviews/history, original-main ignored reports, and prior round104–106 REE raw roots. Pre-creation name/DOI searches found contextual Yb citations/concentrate composition but no existing owners for this pair. All-state issue title/body inventory contained299rows and no candidate/DOI match; comments were not searched. These are bounded results, not machine-wide absence claims.

The JSON gives the exact web queries, first-result-set bounds, full acquisition log and hashes. Correction/retraction queries and inspected Crossref relations yielded no affecting notice in this bounded pass; empty relations do not prove universal absence. Existing inaccessible405/406/397 leads were not retried without a new route. No new criticality list, organism taxonomy or industrial-deployment claim was investigated.

Raw sources and figures remain under /private/tmp/cmm-round107-ree-research; no raw full text or bulk dataset is committed. Morrison states CC BY; White Rose identifies Vallina's published version as CC BY-NC3.0. Buck redistribution rights and IMA redistribution conditions were not fully assessed.

## Handoff and checks

1. Obtain Vallina2015 original SI and reconcile the Nd timing/label conflicts; only then assess a qualified abiotic mechanism.
2. Retrieve Morrison2013 original CIF/HKL through a legitimate public route and verify contents against the rendered crystallographic tables.
3. Preserve the xenotime optical discrepancy and low-total explanation if future property evidence is added.

Named strict validation completed successfully:2records,0failed. Canonical CREATE histories and inline actual-time events are included. Current schema supports the accepted scope; no validator/schema change was needed. Independent per-record reviews, final corpus checks and publication remain the parent workflow's separate pending gates.
