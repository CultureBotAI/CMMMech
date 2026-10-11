# Round 12: platinum and rare-earth commodity groups

Curated on 2026-10-11 by codex / GPT-6 / codex for issue 48, in
`/private/tmp/CMMMech-expansion-round12-20261011`, against trusted base
`1e52585c9019a32d37f959e0dafa00ae431f28c4`. This is a source assessment and
curation handoff; independent scientific reviews and batch gates are owned by
the parent agent. Five records and five canonical CREATE sidecars were created.

## Decisions and identity boundaries

| Proposal | Curated scope | Exact dated designation | Mechanism decision |
|---|---|---|---|
| `platinum-group-commodities` | Six-member commodity family: Ru, Rh, Pd, Os, Ir, Pt. The collective scope overlaps individual elements; it is not a fixed alloy or mineral. | Australia's list updated 20 February 2024, Table 1 and footnote 16. EU mapping remains unresolved; see correction below. | Identity and designation only. Individual metal experiments are not assigned to all six. |
| `rare-earth-element-commodities` | Australian 16-member commodity family: Y and all 15 lanthanides, including Pm; Sc is separately listed. Explicitly distinguished from the chemical 17-member definition and the EU 15-member assessment scope. | Australia, 20 February 2024 update, Table 1 and footnote 17. | One narrowly qualified synthetic Nd/Dy cell-free protein experiment; no claim for all 16 members. |
| `heavy-rare-earth-elements` | EU 2020 assessment convention: Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu, Y. | EU 2024 Annex II 1(q), critical. The act names the group but does not enumerate members; the record explicitly discloses its EU 2020 membership convention. | Identity and designation only. |
| `light-rare-earth-elements` | EU 2020 assessment convention: La, Ce, Pr, Nd, Sm. | EU 2024 Annex II 1(r), critical, with the same explicit convention mapping. | Identity and designation only. |
| `rare-earth-permanent-magnet-materials` | Seven-element end-use family: Nd, Pr, Tb, Dy, Gd, Sm, Ce for permanent magnets. No numeric grade, fixed alloy or finished-magnet identity is invented. | EU 2024 Annex I 1(n), strategic, retaining the end-use restriction. | Identity and designation only. Synthetic ions do not establish actual magnet processing. |

The EU 2020 factsheets, Section 21.1, printed/PDF page 547, explicitly exclude
Sc and Pm from the assessed light/heavy groups. They distinguish initial
oxide-mixture or low-purity oxide processing from advanced refining into metals
or interalloys. The Australian footnote explicitly includes Pm, and its separate
Sc row must not be silently merged. Pm inclusion records the authority's list,
not an ordinary mined Pm supply. No external ontology identifier was invented
for these collective or end-use commodity identities.

## Deduplication and existing evidence

Before creation, `rg --no-ignore --hidden --follow` covered `data`, `research`,
`reviews` and `history`, using broad group terms plus exact candidate slugs,
the DOI fragment `05945`, `R100K` and `Hans-LanM`. The broad search matched 67
files. The 73 exact-search lines were proposal/frontier references; they did
not identify an existing accepted group root or curated Mattocks 2023 mechanism.
Ignored files and relevant symlinks were included. This is a bounded repository
finding, not a machine-wide absence assertion.

Raw-source searches included the task's group and carbon/metals raw roots,
the cited round-9 graphite root, `/private/tmp/cmm-round8-sc-pr-raw` and
`/private/tmp/cmmmech-round5-ree-raw`. Existing raw Diep 2026 and scandium 2024
papers cite or discuss Hans-LanM. Those are source overlaps, not independently
curated copies of the Nd/Dy experiment. The accepted praseodymium record uses
Melba-LanM with synthetic Pr/La; the scandium record uses Mex-LanM with its own
substrate. Individual rare-earth and platinum-group element records are
intentional members/overlaps of the new families, not synonymous roots.

Search receipts remain outside Git as `dedup-matches.txt`,
`dedup-specific.txt`, `raw-dedup.txt` and `prior-raw-dedup.txt` under
`/private/tmp/cmm-round12-groups-raw`. The companion JSON retains their hashes.

## Primary mechanism inspection

Mattocks et al., **Enhanced rare-earth separation with a metal-sensitive
lanmodulin dimer**, Nature 618:87–93 (2023),
[DOI 10.1038/s41586-023-05945-5](https://doi.org/10.1038/s41586-023-05945-5),
was inspected through the main paper, supplement and Figure 4 source workbook.
The paper was published online 31 May 2023 and in print 1 June 2023. The
protein originates from *Hansschlegelia quercus* (NCBI Taxonomy 2528245), and
was recombinantly produced in *E. coli*. The separation used purified protein,
not living cells. The R100K variant with terminal cysteine was attached to
maleimide-functionalized agarose.

The accepted experiment is Figure 4d, main PDF page 5 / printed page 91:
a 0.7 mL column bed separates a synthetic 95:5 Nd/Dy chloride mixture. The
supplement, PDF pages 4–5 / printed pages 3–4, specifies 10 mM
homopiperazine-1,4-bis(2-ethanesulfonic acid) at pH 5, default flow of
0.5 mL/min, a five-bed-volume water wash and ICP-MS for mixed-ion fractions.
Elution proceeds through 30, 50 and 90 mM malonate, then pH 1.5 HCl.
Table S16 (SI PDF page 54 / printed page 53) reports mean feed concentrations
of 344.2 micromolar Nd and 18.5 micromolar Dy. The Figure 4d, Extended Data
Figure 6 and Table S16 renderings were visually inspected in addition to text.

Figure 4d reports Dy purity/yield of 98.1%/99.3%, and Nd purity/yield of
99.9%/99.8%. Wild-type Hans-LanM in Extended Data Figure 6 (main PDF page 17)
reports Dy 83.6%/98.1% and Nd 99.8%/98.5%. The comparator does not establish
protein necessity. Column replication and operating temperature are not
explicitly established for Figure 4d; no matched bare-agarose separation
control was located in the inspected main paper and supplement. Purity is
the molar share of the measured Nd-plus-Dy pair, not a total-contaminant
specification. No complex feed, isolated metal, actual waste/magnet treatment
or industrial deployment is inferred.

The solution dimerization story is separated from column performance. Page 92
and Extended Data Figure 6 state that dimers may involve only a minority of
immobilized units. The R100K result therefore does not directly demonstrate
that dimerization causes the improved column separation.

The workbook formula audit changes the interpretation of the reported yield:

- In worksheet `Fig4d`, Dy yield cell O33 is `L32/O32*100`, where L32 is
  `SUM(H32:H43)` and O32 is `SUM(H32:H51)`.
- Nd yield N45 is `K44/N32*100`, where K44 is `SUM(G44:G51)` and N32 is
  `SUM(G32:G51)`.
- These denominators are summed tabulated eluate, rather than an independently
  measured feed/loaded-ion mass balance. Purity L33 and K45 likewise uses the
  selected Nd and Dy fraction sums. Formula receipts are saved outside Git as
  `fig4d-yield-formulas.json`.

The figure values remain source-reported values. The workbook's Dy result
O33 is 99.396415%, while the figure prints 99.3%; Table S16's Nd standard
deviation is 4.4, while worksheet K56 is approximately 15.1942. The workbook
also maps not-detected values to zero and contains negative analytical cells.
These are retained source ambiguities, not silently corrected data. No native
concentration observations were added: these source units and conventions do
not satisfy the current numeric mg/kg observation contract.

## Bounded current-status and conflicting-evidence checks

Three `web.run` searches were run on 2026-10-11 without date/domain filters;
only their first returned result sets were inspected:

1. `"10.1038/s41586-023-05945-5" correction retraction`
2. `"Hans-LanM" "R100K" limitation separation`
3. `"rare earth elements" "heavy" "light" "2024/1252"`

The [Crossmark record](https://crossmark.crossref.org/dialog/?doi=10.1038%2Fs41586-023-05945-5)
was opened directly and stated that the document is current, with no listed
update. Returned results did not identify a matching correction or retraction;
this does not prove exhaustive absence. The original paper's weaker wild-type
performance, immobilization/dimerization caveat, and source-data inconsistencies
are retained. Search also surfaced the primary lead **Group Separation of Rare
Earth Elements by Protein-Functionalized Magnetic Nanoparticles**, DOI
10.1021/acsestengg.5c00508. Its full methods, feed and controls were not inspected
in this pass, so it remains a deferred research lead and is not imported.

## Acquisition, reuse and access limits

The parent acquired the primary artifacts during this same round. This curator
reused and rehashed them; this is not a claim of new downloads. All bulk raw
files and renderings remain outside Git at
`/private/tmp/cmm-round12-groups-raw`. Exact URLs, acquisition timestamps,
HTTP status, byte counts and local recheck hashes are in the companion JSON.

| Artifact | SHA-256 |
|---|---|
| EU 2020 factsheets PDF | `40506fa2981d6769f027e39b520654a5ddb6acd8ddd50174f9bc48d0ce75a68d` |
| Original EU 2024 regulation HTML | `c70c14e4a1d7076cca516572a77002c1e651dd8042605fbbd93d3cb8842a5696` |
| Mattocks 2023 main PDF | `44b1001dcbc6595b8eba0802454d733983a2b9d2e3a8cb85874e5a9b0f6e825d` |
| Supplementary PDF | `5f3be229d39e4b36259c3a8b383ceb51170173c6c3e007c6a6ac7067eae937bf` |
| Figure 4 workbook | `c7ec6fd3365e7ca64a2b3a5aad67311fccb4d9a963c672a0e1bf867396c0d64d` |

The Australian direct HTTP request timed out; the parent's official-page web
extract successfully preserves the update date, table rows and footnotes 16–17.
Failed EC 2023 acquisition routes returned 403 or 404 in saved parent
receipts. The parent separately reported Publications Office 429, without a
preserved receipt in this dossier. No inaccessible 2023 definitions are asserted; the acquired EU 2020
factsheet page 547 is explicitly identified instead. The main Nature paper is
CC BY 4.0; the EU 2020 report permits reproduction with acknowledgment. Other
asset redistribution terms were not independently resolved, and no bulk source
content is committed.

## Validation and handoff

Named-file validation checked five records with zero failures. Named canonical
history validation checked five sidecars with zero errors. Each record has an
actual UTC inline CREATE event and a helper-created CREATE sidecar with
codex / GPT-6 / codex metadata and issue 48. Exact record and sidecar hashes are
in `round12-groups-20261011.json`.

The five records and sidecars are frozen for the parent's independent scientific
review. No whole-corpus gate, Git/GitHub mutation, shared README or frontier edit
was performed by this subtask. Any further substantive correction needs review
of the changed bytes; this dossier does not claim the independent review passed.

## Independent-review correction, issue 51

Initial PGM review
`reviews/structured/20261011T084025Z-platinum-group-commodities-round12-independent/review.yaml`
raised F1, `pgm-eu-six-member-mapping`. The initial record mapped the EU 2024
PGM labels to all six chemical members without acknowledging that the act does
not enumerate them. Independent inspection of EU 2020 factsheets page 399
confirms six chemical PGMs but only five metal-specific quantitative
assessments; osmium lacked sufficient value-chain data. This does not prove
that osmium is legally excluded from the EU 2024 list.

The corrected record removes the EU mapping sentence, EU source and both EU
designations. Australia's explicitly enumerated six-member designation remains.
No osmium `not_listed` claim is made. Actual EDIT history for issue 51 is
`history/records/platinum-group-commodities/2026-10-11T084108Z-codex-8cbb66.yaml`;
the original CREATE session is preserved. The corrected record and new sidecar
each passed named validation (one checked, zero errors). The companion JSON
retains the original reviewed hash and final corrected hashes. The parent's
successor review, not this curation receipt, determines finding resolution.
