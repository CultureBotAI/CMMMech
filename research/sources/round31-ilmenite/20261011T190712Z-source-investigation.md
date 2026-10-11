# Ilmenite full-evidence follow-up and deferral

UTC: 2026-10-11T19:07:12.245231+00:00; Codex `/root/round27_packaging` (GPT-6). Working revision `075c1ca032b68162eb8350b7e8d9bfe9530ca143`, branch `curate/cmm-expansion-round31-20261011`. This source assessment follows [issue104](https://github.com/CultureBotAI/CMMMech/issues/104) and the [round29 dossier](../round29-ilmenite/20261011T174122Z.md); it is not a record review.

**Decision: defer ilmenite and tin-tailing record creation.** Both complete main journal articles remain unavailable through the bounded new public routes. The newly acquired original supplement is useful progress, but does not replace their Methods or resolve the preliminary/journal discrepancy. No record or history event was created.

## Sources and actual access

| Source | Actual result | Consequence |
| --- | --- | --- |
| [Jonglertjunya and Rubcumintara,10.1002/apj.1663](https://doi.org/10.1002/apj.1663), online2012;2013 issue8(3):323–330 | New OpenAlex location lists a bronze Wiley PDF, but the actual PDF request returns403 HTML. Mahidol item/full routes also return403. | Index openness is not successful acquisition. The abstract's tin-tailing ilmenite concentrate and chemical versus fungal/bacterial assays still need complete material/control verification. |
| [Navarrete et al.,10.1017/S1473550412000493](https://doi.org/10.1017/S1473550412000493), online11December2012;2013 issue12(2):123–134 | Crossref content and publisher-listed PDF routes redirect to abstract HTML. New Pure metadata links only DOI/citation repository; OpenAlex lists no full repository copy. | Journal ilmenite null and separate basalt effects remain abstract-level context. |
| [Original Cambridge supplement](https://static.cambridge.org/content/id/urn:cambridge.org:id:article:S1473550412000493/resource/name/S1473550412000493s.zip) | Genuine253009-byte ZIP, SHA-256 `1dc1002a67861250af78acaf1cac2ca08e53351f315e70c7bff134be49532055`; five original members. | Two experimental XLSX tables, one TIFF and two simulant-characterization PDFs are now available for future full-paper reconciliation. |
| [2010 GSA preliminary abstract](https://gsa.confex.com/gsa/2010AM/webprogram/Paper181015.html) | Prior complete primary abstract reread; current raw checksum retained. | It reports increased ilmenite Fe release/lower pH; later journal abstract says no measurable ilmenite Fe/Ti enhancement. Experimental overlap and accounting differences remain unresolved. |

## Supplement inspection and reusable-data limits

The two single-sheet workbooks contain102 and77 XML row elements, respectively (including headings/blank rows, not102/77 independent experiments). Raw cell coordinates and cached values were extracted. S1 gives short-term concentration data, including Fe(II), total Fe, Ti, pH and day; concentration units are mg/L. S2 separates concentration, batch mass and corrected-final-mass blocks. S1 cellA43 labels the ILC section with the organism, so its supposed control assignment requires the main paper. S2's corrected ilmenite Ti cellsP47/P48 contain literal `err`; these are neither zero nor numerical recoveries. Negative cells must retain their original tokens and unverified detection conventions. No mg/kg conversion, statistical conclusion or isolated product is inferred.

Both supplementary PDFs were text-read; they concern terrestrial regolith simulants, not ilmenite assay methods. The8-page lunar characterization is explicitly versionB.1 draft28June2007; the2-page Mars characterization is a1997 conference document. Original representative pages and the TIFF spectrum were visually inspected; the TIFF's assay/sample assignment is not independently established. These are attached supporting materials, not five independent microbial studies. Complete main figures/tables remain uninspected.

## Search, deduplication and provenance

The accompanying [JSON](./20261011T190712Z-source-investigation.json) retains eleven exact queries, new acquisition URLs/results, the fresh OPEN issue104 receipt, per-file hashes and source-specific prerequisites. First returned web result sets were checked without date/domain filters or pagination, including exact-DOI correction/retraction searches; no affecting notice was identified in that bounded scope. The requested UTEP proceedings URL returned404 HTML despite an indexed abstract. The author thesis search found a different copper-isotope thesis, not the requested journal paper; it was not substituted.

Hidden/ignored-inclusive, symlink-following searches covered this worktree and original checkout records/research/reviews/history, the prior round29 ilmenite raw directory, the referenced round28 frontier response and the adopted round30 basalt raw directory. All17 prior ilmenite files were inventoried and rehashed. The76 matching paths include discovery and citation references; no ilmenite-specific corpus record appeared in that bounded search. Binary journal PDFs were not silently assumed absent from the whole machine. Older unrelated raw directories were not exhaustively rescanned.

Raw evidence and failure responses remain at `/private/tmp/cmm-round31-ilmenite-research`. Successful HTTP200 HTML is not reported as a PDF. No unchanged Wiley abstract block was retried, no author was contacted and no access control was bypassed. Publisher reading access does not establish redistribution rights; bulk originals remain outsideGit.

## Ranked next work

1. Obtain the two complete main articles through a legitimate library/author-deposited route, then verify mineral/concentrate provenance, strains, inoculum, medium,loading,time,temperature,replication and analytical fractions against the acquired tables. Resolve the ILC label and Ti error tokens before accepting any measurement.
2. Compare2010 and2013 experimental identity and dissolved versus precipitated/corrected totals without assuming independent replication or a reason for disagreement. Keep ilmenite species, tin tailing/concentrate and basalt separate; inherit no criticality or deployment claim.
3. Investigate the separately proposed [kaolin-waste-dump study,10.1007/s42860-022-00192-7](https://doi.org/10.1007/s42860-022-00192-7) as a potentially distinct processing-derived resource, subject to complete primary/SI and identity review. That lead does not close issue104.

Report QA: JSON syntax/checksum inventory verified. No schema change, record validation, canonical history creation or scientific acceptance is claimed for this research-only deferral.
