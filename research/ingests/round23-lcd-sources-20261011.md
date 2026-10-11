# Waste LCD panels: source assessment and curation

Investigation by Codex (GPT-6; Codex), begun 2026-10-11 UTC, at trusted base
`80899a3d3ea5c0f7c5d54f1b3583e43768e92767` in
`/private/tmp/CMMMech-expansion-round23-20261011`. The
[JSON companion](round23-lcd-sources-20261011.json) records searches, acquisition
receipts, artifact hashes and the selected record. This is curation research,
not the independent scientific review.

## Identity, scope and acquisition

The [2018 primary study](https://doi.org/10.5277/ppmp1878) documents real panels
removed from used mobile phones. This is a secondary composite resource,
distinct from existing indium, tin, waste printed circuit boards and photovoltaic
modules. It is not a pure ITO commodity or an element. The record covers waste
LCD panels, with the particular prepared powder specified in its mechanism.
No criticality claim is inherited from a constituent.

The study was already a lead in rounds 6 and 9. Searches included hidden and
ignored files and followed relevant symlinks in data, research, reviews, history,
and the explicitly cited round6-indium and round9-si-sn raw directories. The
matches were prior source leads, not an existing LCD resource record. This is
bounded repository/download deduplication, not a machine-wide search.

Publisher landing-page authors, DOI, volume, issue and pages match the seven-page
published PDF acquired from the Wroclaw institutional digital library. Its SHA-256
is `95c92c21d2090aa6c23748dc68c71ea77ae4452d35cb98847b1872e4b607d20f`
(414457 bytes). The publisher PDF was readable through web extraction but direct
shell acquisition returned 403. The institutional PDF succeeded despite the web
reader failing on that route. `pdftotext` was unavailable; isolated cached
PyMuPDF extracted all seven pages and rendered them without changing project
dependencies. Figures 1-4 and Tables 1-2 were visually inspected on pages 641-644.
Web screenshot calls returned text placeholders, so they are not counted as
visual inspection. Raw PDF and renders remain in `/private/tmp/cmm-round23-lcd-raw`.
The paper states publisher copyright; redistribution permission is not inferred.
No supplement or downloadable source-cell dataset was exposed by the inspected
paper and landing page; this is an access-scope statement, not global absence.

## Evidence and adversarial interpretation

Section 2 establishes physical dismantling, two sieved fractions and their
homogenization. The nominal feed contains 0.1% In and 0.025% Sn. It is not the
same feed as every LCD product or a pure oxide. The modified 9K recipe, sulfur
additions, 2.5% w/v loading, 30 degrees C, four-week culture adaptation and
35-day leaching protocol are preserved in the record. Inoculum volume is known;
working volume, exact sulfur addition accounting and independent replicate
number remain unresolved. The paper's two series do not prove duplicate
biological reactors. Sample replacement and cumulative removal corrections are
not specified. Native mg/kg concentration observations are therefore inapplicable
to these mg/dm3 filtrate concentrations and reported extraction percentages.

Figure 4A and Table 2 support higher indium in inoculated 9K filtrate; Figure 4B
and Table 2 also show substantial sterile tin leaching and declining tin after
its peak. The record preserves the sterile comparison rather than inferring a
universal microbial benefit. The nominal feed denominator supports an arithmetic
check of the reported percentages but cannot establish an independently closed
mass balance. At 25 g/L and 0.025% Sn, nominal inventory is 6.25 mg/L; 5.52 mg/L
is 88.32%, not the 90.2% stated peak. The paper does not resolve that difference.
Similarly, its statement of 3.4% for both indium controls cannot reconcile Table
2 values 0.82 and 0.49 mg/dm3 under one nominal denominator. No replacement
percentage is curated.

Figure 2 shows chemically unmatched pH/ORP trajectories, including plotted
initial pH differences despite the nominal pH 1.9 protocol. Iron oxidation,
acid generation, hydrolysis and feed dissolution can all affect these measures.
The assays do not directly measure an indium-valence change, identify a necessary
species or separate ferric chemistry from acidity. SEM-EDS establishes elemental
composition, not crystallographic identification of jarosite; Figure 3 labels
the spectrum pt1 while Table 1 names pt2. Tin reprecipitation is an interpretation,
not a measured isolated tin phase. No product isolation or industrial deployment
follows from leachate concentrations.

NCBI's own pages resolve species identifiers 920 and 930 and their labels. They
do not verify strain identity or mixture membership independently of the paper.
The paper's abstract spelling differs from the standard genus spelling; the
record uses the verified names and retains the reported isolate origins.

## Counterevidence search and handoff

Exact-DOI/title correction/retraction/supplement searches and targeted organism
queries inspected the first web result sets without date filters or pagination.
They returned the original source and related work, without a matching notice
in that bounded set. The most direct counterevidence is the 2018 sterile tin
comparison itself.

The [2022 follow-up](https://doi.org/10.37190/ppmp/143580) was read as publisher
PDF text through the bioleaching Methods and Results; its local download returned
403. It reports different preparation (NaOH treatment and <0.1 mm feed), 10-week
adaptation, named Smolnik isolates and 1/2% loadings. Its figures have not been
visually inspected here, and its later result sections have not been fully
audited. It is a separate proposed mechanism extension, not a replication of the
2018 feed or a basis for importing its percentages. Referenced Jowkar, Rezaei,
Xie and fungal studies likewise require their own full evidence reviews.

The new [record](../../data/records/waste-liquid-crystal-display-panels.yaml)
retains a narrowly supported laboratory mechanism. A real CREATE sidecar and
inline event were attached before final review capture. Baseline passed 308
tests, 3 skipped, 154 records and 173 histories; named validation before history
attachment passed. Final named/batch validation and independent review are
tracked separately; this dossier does not predeclare acceptance.
