# Pyrrhotite source assessment

Assessed on 2026-10-11 by codex (GPT-6); record: `data/records/pyrrhotite.yaml`.
Trusted base: `930ce995269f0ded5df009eb5916162971eb1f58`.

## Admission decision and identity

Admit the mineral species, grounded in the September 2026 IMA-CNMNC list,
page 180, formula Fe7S8, status G, original-description year 1835. Pages 1-2
define grandfathering, distinguish the year from an approval number, and give
CC BY-SA 3.0 terms. Experimental Fe1-xS notation does not make an elemental iron,
troilite, pentlandite or mixed-resource record interchangeable. No external
identifier or inherited criticality is asserted. The paper's historical organism
name and TFI-35 label are retained without inventing a strain accession.

## Primary evidence inspected

1. Bhatti, Bigham, Carlson and Tuovinen (1993), AEM 59:1984-1990,
   [DOI 10.1128/aem.59.6.1984-1990.1993](https://doi.org/10.1128/aem.59.6.1984-1990.1993),
   [PMC182203 public page reader](https://pmc.ncbi.nlm.nih.gov/articles/PMC182203/?page=1).
   All seven original page scans were inspected, including Figures 1-6, methods,
   discussion and references. Initial PMC base-URL retrieval was a CAPTCHA page;
   Europe PMC and publisher download routes failed. The public PMC page reader
   subsequently exposed all original NIH CDN page images. No challenge was solved
   or access control bypassed. The article retains ASM 1993 copyright; no scans
   or full text are committed.
2. Kim, Koh and Kwon (2021), Metals 11:295,
   [DOI 10.3390/met11020295](https://doi.org/10.3390/met11020295).
   Complete 11-page original publisher PDF inspected; Figures 1-8, Table 1,
   Equation 1, methods, conclusions and references checked. The article declares
   CC BY 4.0 and data sharing not applicable; no supplementary data identifier
   was indicated in the inspected PDF. Crossref bibliographic metadata was checked.
3. [Official IMA September 2026 PDF](https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf),
   complete download, text extraction and original page-180 row inspected.

## Main study and adverse interpretation

Bhatti used a Santa Eulalia specimen (Ward's 49E5885), ground below 74 micrometres,
5% wt/vol solids, mineral salts in 0.005 M sulfuric acid, source-named
Thiobacillus ferrooxidans TFI-35, 22 degrees C shake flasks and chemical controls.
XRD characterized monoclinic 4C pyrrhotite with minor pyrite and marcasite.
Chemical controls also altered the feed; early pH/redox behavior was similar.
Later inoculated residues showed greater pyrrhotite depletion and secondary
elemental sulfur, K-jarosite, goethite and schwertmannite. Selective dissolution
and difference XRD support the poorly crystalline phase assignment. Pyrite and
marcasite were starting impurities that became relatively enriched.

Normalized diffraction peaks are not absolute phase masses or recovery yields.
Dissolved iron was explicitly not analyzed (page 1985), and no closed mass
balance was produced. Individual cells were not identified by SEM. Sulfur
oxyanions are proposed intermediates, not measured products. Flask volume, rpm,
inoculum density and replicate counts are not specified in the inspected article.
This supports a qualified laboratory weathering mechanism, not industrial recovery.

## Why the newer study is context only

The 2021 feed was a magnetic fraction of Korean iron-mine waste, with quartz
impurity. Its bulk-waste elemental composition cannot be substituted for the
separated experimental fraction's composition. The fresh medium contains iron,
and 10 mL inoculum came from iron-rich adaptation medium; washed inoculum,
matched carryover blanks and background correction are not documented.
Figure 8 starts at zero despite the iron-containing recipe. Thus reported
aqueous iron is not an established mineral-only mass or microbial increment.

At initial pH 2.8, day-41 reported aqueous Fe was 1.9/23.8/47.4 mg/L for
abiotic/nonadapted/adapted arms; at pH 3.2 it was 0.7/19.4/21.9 mg/L.
These are distinct from Table 1 fitted limiting concentrations (21.6/44.2 and
19.8/21.3 mg/L respectively). The abstract/conclusion blur fitted and observed
values. Equation 1 prose also mixes concentration and mineral-mass terminology.
No such values are promoted to machine-readable concentration observations,
whose schema requires exact source mg/kg cells, or to a recovery percentage.

Single-colony methods wording conflicts with Figure 4's three-taxon profile.
The source's organism labels, including its ambiguous thermosulfidooxidans name,
do not justify strain or consortium-member identifiers. Enrichment temperature
(32 degrees C) does not establish the leaching temperature. Replicate count,
error-bar meaning, starting cell density and leaching agitation are unresolved.
Initial pH comparisons do not isolate contact; bacterial zeta potential was
not measured, and Figure 7 images have unlike magnifications. The conclusion
that nonadapted cultures did not enhance Fe over abiotic arms conflicts with
the reported endpoint ordering. References 25-26 invoked for a generic adaptation
statement concern unrelated topics and are not propagated as supporting evidence.

## Discovery, novelty and counterevidence boundary

Queries included pyrrhotite microbial dissolution, the two exact titles/DOIs,
and correction/retraction variants. Returned sets did not surface a dedicated
correction or retraction; this is a bounded search result, not proof of absence.
The two complete studies were explicitly compared rather than pooled. Bibliographic
leads DOI 10.1016/j.hydromet.2006.03.011 and PMID 27332502 remain unassessed.

Hidden/ignored-inclusive, symlink-following searches covered `data`, `research`,
`reviews`, `history`, `.claude`, and the relevant prior raw directories
`/private/tmp/cmm-round13-mineral-raw`, `/private/tmp/cmm-next-li`,
`/private/tmp/cmm-round12-aluminium-boron-raw`; the 1993 query additionally covered
`/private/tmp/cmm-round28-black-shale-research`. Earlier pentlandite source files
contain contextual pyrrhotite mentions, not an existing pyrrhotite root record.
Results do not establish machine-wide novelty. Raw receipts, query outputs,
page images and downloaded files are retained in
`/private/tmp/cmm-round30-pyrrhotite-research`; the adjacent JSON pins inspected
artifacts without redistributing them.

## Remaining work

Independent exact-state scientific review and the publication gates are required.
Stronger quantitative claims would need dissolved-metal accounting and replication
for the 1993 work or iron-background controls and clarified community/methods for
the 2021 work. Neither evidence gap prevents the bounded weathering record.
