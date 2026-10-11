# Round 20 mafic-tailings and boron-concentrator source assessment

## Scope and provenance

Actual UTC: 2026-10-11T12:15:50.101513+00:00. Researcher: codex (GPT-6; codex), agent `/root/round20_mafic_tailings`.
Worktree `/private/tmp/CMMMech-expansion-round20-20261011`, branch
`curate/cmm-expansion-round20-20261011`, trusted base `e98bdfaba62869faf5112ef281a9371d2a04d78e`.
The lane followed the add-record, discover-sources, review-record and read-only PDF workflows.
Root baseline finished before authoring: 308 passed, 3 skipped, 145 records and
162 histories, 142.63 seconds, exit 0. This is a source dossier, not the independent
acceptance review. Subsequent batch publication is coordinated by root under issue 74.

The starting question was whether Brar2026's mafic tailings define a distinct
secondary resource or belong to existing iron-ore tailings. Its references exposed
an evidence-backed boron concentrator residue. One record was created; neither a
quota nor a global exhaustion claim determined that outcome.

## Identity decisions and complete local search boundaries

- **Mafic tailings: defer identity assignment.** Brar2026 Methods2.1 says only
  an unnamed V/Ti-bearing magnetite deposit in north-central Québec, associated
  with a mafic layered intrusion. Introduction describes generic beneficiation,
  but neither main nor supplement identifies this sample's concentrator, product,
  processing operation or mine. Iron content is insufficient to assign the
  existing iron-ore-production root. A separate mafic/V/Ti root would likewise
  force an unsupported split. Copper flotation tailings denote a different
  evidenced process; no relationship to that process was established here.
- **Boron-ore concentration tailings: create.** Ertan2026 Materials p2 names
  minus-25-mm solid waste of Eti Mine's Espey concentrator at Emet. Its XRD
  characterization identifies a mixed colemanite/muscovite/quartz/dolomite feed.
  Ertan2025's author-posted Introduction independently describes the sampled
  boron industrial waste as a colemanite ore-processing by-product, but only the
  full-verified 2026 assay is curated. The process-root name avoids a mine-specific
  or single-mineral root. Existing `borates.yaml` is a commodity and its Bayat2011
  assay uses ore, not concentrator waste; no constituent criticality is inherited.

All novelty searches included ignored and hidden files and followed symlinks.
The paired JSON preserves exact commands, times, exit codes and stderr. Searches
covered `data`, `research`, `reviews`, `history`, raw directories from rounds17,
18 and19 named in the handoff, and this lane's raw directory. Additional relevant
borate-review references led to round12 aluminium/boron and round10 B/F raw
folders, which were also searched. No inaccessible paths or stderr were reported
for these bounded searches. Round12 review matches were contextual boron evidence;
round10 matches were unrelated Bacillus fluoride evidence and the substring
Bertani. They are not Ertan studies. No prior record for the accepted process
identity or Ertan study DOI was found within these boundaries. This is not a
machine-wide absence claim; binaries were not treated as searchable full text
without their extracted content. The supported identity comparison also read
actual nearby records and prior review dossiers, rather than relying on names.

## Search and acquisition

Search provider: web tool, 2026-10-11 UTC, first returned result set for each query,
no date/domain filters and no pagination. Exact queries appear in the JSON.
The short numeric supplement query produced substantial irrelevant results and
was followed by exact-DOI/source-link acquisition. Publisher links, DOI landing
pages, the author's public ResearchGate text and primary PDF/XML were inspected.
The JSON includes acquisition UTC, URLs, MIME/content checks, bytes, hashes and
failures; derived renders/extracts remain outside Git.

Ordinary shell network lookup initially failed because networking was restricted;
authorized read-only retrieval then obtained public files. MDPI direct HTML gave
403 and the web open route gave429, but its publisher CDN returned real primary
PDF and XML. Guessed PDF/DOCX supplement names returned404; the actual XML link
identified a ZIP containing the real two-page PDF. Springer2025's PDF route
returned HTML subscription preview, not a full paper. Author-publication text was
read through the web tool, but its downloadable-copy route returned404/403.
These failures are preserved, not claimed as full-text file acquisitions.

## Brar, Du Preez and Perreault 2026, DOI10.3390/met16020178

Actual artifacts: 17-page publisher PDF, XML and two-page supplement (S1-S3).
All main text, methods and tables were read; Figures2-5 and SI figures were
visually checked. Publisher notes show original publication2February2026,
PDF version-of-record upload2February2026, and HTML update2September2026.
The HTML update is not described as a formal correction; no correction/retraction
surfaced in the bounded exact-DOI searches. The main PDF prints CC BY; XML links
CC BY4.0. Raw files are retained outside Git despite permissive license.

Methods2.5/Results3.3: living Enterococcus CBGM-1C, Acetobacter BL-F and
Lactiplantibacillus plantarum ATCC8014; four-day growth/acid phase followed by
5%w/v tailings, 30C/120rpm, ten-day contact. Tailings were dried/sieved/homogenized;
sieving size, sample processing origin, inoculum density and culture-replicate
count remain unresolved. Short16S identification supports only reported isolate
genera; no species/strain CURIE is assigned. MRS contains acetate and citrate,
so organic-acid totals cannot automatically equal net biosynthesis.

Table2 is triplicate bulk chemistry in mg/kg, without source analysis date; it
is not importable into dated native observations. Table3 is called mean±SD but
prints only values. Sulfur is called not detected in prose while Table3 lists
0.10%SO3; assay distinctions/limits are unclear. Figure4 shows only three biotic
metal arms; a matched abiotic metal-release series is unavailable despite the
text claiming improvement over untreated control. pH/glucose controls in Figure2
and S3 do not substitute for that missing metal comparison. Main text calls
L.plantarum best for Al even though its own reported16556mg/kg is less than
Enterococcus18410mg/kg; Figure4 supports that ordering tension. Zn≈74% is an
assayed leachate fraction, not pure product; other metals remain limited.

Figure2 has nonzero initial organic-acid baselines and substantial unresolved
medium contributions. Reduced XRD peak heights (Figure5) are not absolute
phase-specific dissolution mass balances or proof that no secondary phases
formed. No enzyme intervention, ligand-speciation measurement or deployment
is established. These limitations remain in research because process identity
is unresolved, not because a valid source must be discarded.

## Ertan2026, DOI10.35229/jaes.1832038 — accepted narrow assay

Actual primary publisher PDF: eight pages, all read; Tables1-2 and Figures1-3
visually inspected. The PDF prints13March2026 while the landing page displays
24March2026; both dates are retained. No supplementary link surfaced in the
inspected landing-page text. Source redistribution license was not resolved;
public reading access is not treated as a redistribution license.

Materials/Methods pp2-3: concentrator solid waste;110C48h drying, ring milling
and38µm sieving; autoclaved feed/media; A.niger supplied by Erzurum Technical
University without strain/sequence accession. Seven-day sucrose100g/L preculture;
250mL flasks with100mL medium,2.5mL spore suspension and1g feed;30C125rpm,
31days. Samples centrifuged,0.45µm filtered and nitric-acid-stabilized for ICP-MS.
The spore density and whether Figure2 N=5 represents independent culture rather
than analytical replicates are unclear. Equation1 defines feed-relative filtrate
percentage; no native observations are created because available bulk cells lack
analysis dates and yields/rates are outside the current concentration contract.

Figure2 supports culture-associated Li/Rb/Cs mobilization; approximate endpoints
79/37/30% are retained only in prose. No abiotic leaching time-series isolates a
microbial increment. The pH passage cites Ertan2023, so independent experimental
replication is not assumed. The2025 author text also attributes the same reported
78.67/37.44/30.47 endpoints to2023; exact2023/2026 study overlap needs full original
methods/data. The2023 abstract gives extracted amounts rather than those
percentages, and its methods were not acquired; no denominator is reverse-engineered.

Text p4's day24Li43.71% conflicts with Figure2 near35%; no exact intermediate
value is adopted. Figure3d's Rb diffusion ordinate is inconsistent with the
printed equation and endpoint. For example, substituting X=0.3744 in the printed
1-2X/3-(1-X)^(2/3) expression gives about0.019, substantially above the plotted
≈0.0024 endpoint; this is an audit calculation, not a source observation.
Fitted shrinking-core comparisons cannot prove microbial causation or Arrhenius
behavior without temperature variation. The possible complexes in Figure1 and
proposed metabolite pathways are not directly verified speciation. No pure metal
product, mass-balanced recovery, universal feed performance or deployment follows.

## Ertan2025 and Ertan2023 — deferred extension frontier

Ertan2025 DOI10.1007/s40831-025-01254-5: publisher metadata/abstract, public author
full-text extraction and actual two-page supplementary TableS-I inspected.
Bacterial methods describe uninoculated controls and ICP-MS after filtering;
the author text contains Table4's15 Box–Behnken runs. But original full main
PDF/figure fidelity is unavailable, so no bacterial mechanism is accepted yet.
The main narrative's21.9/0.9mg/mL acid values disagree with its Table2's much
smaller values; these resemble the earlier fungal assay. Carbonic-anhydrase/
ammonia causation is inferred from pH/EDS, not enzyme intervention. Abstract
optimum conditions and later optimization text differ; model predictions and
three measured center runs must remain separate. Supplementary Cs ANOVA rows
have internal sum-of-squares/mean-square tensions (including nonzero mean square
for zero printed pure-error sum of squares). Neither fit quality nor a proposed
biomineralization mechanism should be imported uncritically. Publisher exclusive
rights apply; author public reading access does not grant redistribution.

Ertan2023 DOI10.1007/s12666-023-03013-0: publisher abstract/metadata only;
full-method, controls, phase data and experimental relationship to2026 are the
next evidence needed. It is a companion lead, not a second accepted experiment.
Publisher exclusive rights apply. The broad boron-waste/abiotic query returned
unrelated composting and remediation sources; no direct contradictory matched
assay was established by that bounded search. No retraction/correction was
surfaced for2025/2026 in the exact queries, not an exhaustive registry check.

## Artifacts, validation and handoff

Created `data/records/boron-ore-concentration-tailings.yaml`; SHA256 `ade7411923a81921cd55f980c8ff48c53a7dc32c652672621e1fb361859c5fa7`.
Canonical CREATE history: `history/records/boron-ore-concentration-tailings/2026-10-11T121340Z-codex-116c97.yaml`,
created through `just new-history` with actual GPT-6/codex metadata. Inline event
records actual creation separately. Tracking issue74 was supplied after scaffolding,
so the already created history was not rewritten to add an issue number.
`uv run --locked cmmmech validate data/records/boron-ore-concentration-tailings.yaml` completed exit0,
`Checked 1 record(s); 0 failed.` No schema/validator/shared README or other lane's
record was changed. Independent scientific review and full batch gates remain
root-coordinated; this dossier does not claim their outcome.

Ranked remaining work: (1) obtain original2023/2025 primary figures and raw control
results to resolve overlap and causal attribution; (2) obtain Brar's actual
processing provenance before deciding iron-tailings extension versus distinct
process identity; (3) retain Brar reference26 mafic-tailings organisms/assays as
an unverified lead, without adding a mine-specific root. Other primary leads in
the reference list were not systematically reviewed. This bounded batch is ready
for independent review, and discovery remains open.
