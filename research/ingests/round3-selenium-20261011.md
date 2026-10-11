# Selenium curation dossier

Prepared 2026-10-11 UTC by Codex (GPT-6), against trusted base
`5892e9a0aca54ef3f45d2ce87a6dcfb80d1569da`. The earlier
[source handoff](../sources/round2-selenium-handoff/20261011T042117Z.md)
remains a historical screening snapshot. This pass completes claim-level
inspection for `data/records/selenium.yaml`; it is not independent acceptance.

## Selection and identity

Selenium adds a distinct selenite-transformation case with genetic comparisons
and spectroscopy, using the earlier handoff's primary leads. The live ChEBI
entry resolves CHEBI:27568 to selenium atom, Se, charge zero. NCBI211586 is
the MR-1 no-rank strain entry. Neither the element ID nor its criticality
designation identifies the experimental oxyanion or a host mineral.

The Australian government page's Table1 contains Selenium and dates the list
revision to20February2024. The record uses Australia's own designation and
explicit commodity-to-element mapping. Comparison columns for other countries
do not establish those countries' current designations.

## Primary evidence and checked claims

[Li et al.2014](https://doi.org/10.1038/srep03735), Scientific Reports4:3735,
PMID24435070, PMC3894562. The legitimate EuropePMC XML acquired in the prior
handoff was read in full for Results, Discussion, Methods, Table1, captions,
identity and permissions. Its SHA256 is
`76de6506252b8883844bebcf649b069cb7cc49a0d9d77b9bc916c7b92219c3a2`.
Figures2,4,5 were downloaded from the publisher and visually inspected.
No plotted data were digitized or spectra refitted.

The accepted protocol is LB-grown, twice-washed MR-1 cells in40mL anaerobic
mineral medium, OD6001.0, 0.5mM selenite,20mM lactate,30C. The medium recipe
does not establish a measured pH. Fumarate20mM belongs only to a separate
competition experiment. Initial12h depletion rates are not instantaneous
enzyme turnover. Figure2's triplicate standard errors accompany the WT and
delta-fccA rates. Figure4 retains later residual delta-cymA activity; the
paper's word "essential" is stronger than an exclusive-pathway conclusion
these observations warrant. No purified-FccA assay or complementation is
reported in the inspected Methods/results. Other pathway involvement remains
possible; the paper's proposed glutathione contribution is not curated as fact.

Figure5 independently supplies the Se3d XPS oxidation-state support that EDX
alone cannot. TEM shows larger intracellular and smaller surface particles,
without resolving all deposits to the periplasm. The48h cell fraction was
anaerobically washed and lyophilized for XPS. Table1's selenium balance uses
digestion/ICP-AES of an analytical fraction, not a pure product yield.

The publisher supporting Word file was acquired and recognized as an OLE
document. `textutil` extracted FigureS1-S3 captions and S4Methods. S1 names
autoclaved cells as an adsorption control; the main Results report negligible
adsorption. S2 and S4 identify BSA-equivalent protein measured by MicroBCA,
not viable-cell counts. The legacy embedded graph pixels were not rendered;
conversion to DOCX lost images, so it was not treated as a visual inspection.
No supplementary plot values or S3 localization measurements enter the record.

[Klonowska et al.2005](https://doi.org/10.1128/AEM.71.9.5607-5609.2005),
PMC1214622, was read in full through the public ASM web representation,
including both figure captions and references. It describes external or
surface-attached selenium deposits in LB with2mM selenite, and residual
cymA-mutant reduction with data not shown. Its medium, growth and substrate
conditions differ from Li2014. The record preserves the different observations
without treating them as a matched quantitative refutation. The older EDX
assignment is not an independent oxidation-state determination. Figure pixels
from this older article were not inspected; the record attributes its reported
localization instead of claiming a new microscopy analysis.

## Search, novelty and access limits

This pass used `rg --no-ignore --hidden` across data, research, reviews and
history for selenium, selenite, selenate, srep03735, CHEBI:27568 and the2005DOI.
Ignored and hidden files were included. Before adding the record, matches were
the authority inventory, prior handoff, and tellurium/priority references;
there was no selenium root in those searched files. The cited prior selenium
download and new evidence directory were also inspected; this is not a search
of unrelated local directories or the entire literature.

In addition to the earlier handoff's exact query log, live2026-10-11 first
returned web result sets, without complete pagination, used:

- `"10.1038/srep03735" correction retraction`
- `"selenite" "FccA" "CymA" "contradict"`
- `"srep03735-s1.doc"`

No affecting correction/retraction appeared in those inspected results. This
is a bounded search, not a claim of exhaustive absence. Primary full text
supports the accepted claims; abstracts alone do not enter the mechanism.

PMC main and supplement requests returned challenge HTML, rejected as article
content. EuropePMC supplementaryFiles timed out. The normal public publisher
CDN supplied the Word supplement and figure images. A local ASM HTML request
returned403, while the web tool supplied the full article. Acquisition URLs,
timestamps, sizes, hashes and failures are in the adjacent JSON; the older
XML receipt remains separately linked. Raw files stay outside Git under
`/private/tmp/cmm-round3-selenium-evidence-20261011` and the earlier handoff
directory. Li2014 is CC BY-NC-SA3.0; ASM2005 is copyright-controlled. No raw
article, figure or supplement is redistributed here.

## Remaining leads

- PMC12016495,2025: anaerobic reducers from FGD wastewater. Primary methods,
  controls and resource mapping remain uninspected.
- DOI10.1080/01490451.2025.2563890: Shewanella exudate proteome study; lead only.
- DOI10.1038/s41598-017-03558-3: Enterobacter cloacaeZ0206 aerobic selenium
  study; lead only, not evidence for the MR-1 mechanism.
- Render the legacy supplement graphs if detailed adsorption or biomass
  quantification is later curated. Current record deliberately retains the
  narrower main-text/caption-supported claims.

No schema change is needed. Quantities remain qualified prose rather than
incorrect mg/kg observation cells. Canonical CREATE history and a separate
inline event are attached before independent review; final acceptance and
batch validation belong to that subsequent workflow.
