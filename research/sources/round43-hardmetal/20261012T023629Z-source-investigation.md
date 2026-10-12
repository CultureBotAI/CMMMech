# Hardmetal follow-up and titanium-sponge processing

Recorded 2026-10-12T02:36:29.130974+00:00 by Codex /root/round43_hardmetal (GPT-6; codex). Trusted base `59e24ec38d9c7b377dcfeade1637b298aab9623e`. This curator dossier is separate from independent scientific review.

## Decision and record owner

Updated [data/records/titanium-metal.yaml](../../../data/records/titanium-metal.yaml) with [canonical EDIT history](../../../history/records/titanium-metal/2026-10-12T023444Z-codex-ff8e43.yaml) after fully inspecting a new primary found by following the official issue of the hardmetal study. Titanium sponge is an existing metallic commodity form; no duplicate sponge record is needed. The paper's other feed is ambiguously called titanium cut-offs in its tasks and titanium slag in its results. No new slag resource is created, and the pooled results are not attributed to a specific feed. Existing cemented-tungsten-carbide-scrap remains unchanged: the unavailable2012/2015 sources do not warrant fabricated curation or history.

## Source identity and access

Baranov, Kryukovskaya and Maronchuk (2013), *Visnyk NTUU KPI, Mechanical Engineering*3(69):131–135, “The production of titanium nanopowders from the titanium sponge and titanium industry waste using method of the bacterial leaching.” The [official article](https://journal.mmi.kpi.ua/old/article/view/29005) links the [complete Russian original](https://journal.mmi.kpi.ua/old/article/download/29005/28485). The [institutional mirror](https://ela.kpi.ua/server/api/core/bitstreams/29bb1fbb-12d1-4dfc-b90d-faa28919056e/content) is byte-identical: SHA256 `15dc0b0689cd17d66d7cdf9920a56fe5db32b096ab7f739a2f6099072c779602`. All five pages and original page images were inspected, including Figures1–3 and the sole unnumbered table. Renders and text are under `/private/tmp/cmm-round43-hardmetal-research/raw/` and hashed in the JSON.

The printed2013 issue and printed manuscript receipt22Dec2012 remain distinct from portal `Published`7Jan2014 and its `DC.Date.dateSubmitted`3Nov2014. No unverified version history is inferred from those conflicting metadata dates. Publisher-declared DOI **10.20535/2305-9001.2013.69.29005** returned404 at both doi.org and Crossref; the record cites the verified official URL. The inspected article and landing page supplied no separate supplement pointer, a bounded observation only. The portal states Creative Commons Attribution without a verified version; originals remain outsideGit.

## Evidence and adverse interpretation

| Locator | Assessed evidence | Retained boundary |
|---|---|---|
| p132 tasks and Fig1 | Two sponge size ranges0.1–1/0.1–3mm; waste labelled slag10–100mm but tasks say cut-offs | No waste provenance/grade/phase identity; no conclusion they are a single commercial slag. Separate versus combined processing unresolved. |
| pp132–133 | Rotating disintegrator, ferric-sulfate solution with source-named T.ferrooxidans; feed:solution1:1 **mass** | No imported1:1volume protocol from Chaika; no strain/purity check/inoculum/Feconcentration/pH/temperature/duration/rpm/vesselvolume/replicate count. |
| p133 table | Four-element averages Ti95.84→98.14%,Cr0.60→0.30%,Fe3.42→1.50%,Ni0.10→0.06% | XRF excludes gaseous impurities; O/H unaccounted; these are not elemental-metal purity, extraction yield or a source-specific massbalance. No masses supplied. |
| p133 diffraction prose; p134 conclusion | Source reports mixed titanium oxides and hydride; unclear peaks prevent crystallite sizing | No original diffraction figure, phase fractions, oxide polymorph or hydride formula. Pure titanium is future work, despite title shorthand. |
| Figs2–3 | SEM agglomeration; TEM after ultrasonication with100/500nm bars | TEM caption repeats SEM2500/1000 labels. Text estimates average grain size≤150–200nm vs conclusion100–200nm; no counted distribution/error/sizefractionyield. Not uniformly nanoscale powder. |
| pp133–134 proposed functions | Bacterial redox/acid regeneration and process advantages asserted | No measured redox/acidity/growth/Feoxidation or matched sterileferric/acid/mechanical controls. No demonstrated enhancement, industrial throughput, cost or waste-free operation. |

Fresh NCBI API and browser authority verify species920 and its historical homotypic synonym. This nomenclature does not authenticate the stock. The new mechanism uses `other`, with `microbial:true` limited to participation in the source-described culture-containing workflow, not causal necessity. No schema or validator change is needed.

## Deduplication and search boundary

Before drafting, hidden/ignored-inclusive, symlink-following searches covered records/research/reviews/history in both this worktree and original main, plus **154** existing referenced raw/research/evidence roots. A cycle-aware discovery scan read **3324** textual files. Exact roots, missing references, commands, stderr and result receipts are saved and embedded in paired JSON. No read errors were reported. A more precise title/author/DOI/bitstream query after drafting matched only this agent's new titanium-metal draft within those bounded trees; the draft is not treated as prior evidence. This does not decode every unextracted binary or search unrelated machine directories. Existing titanium-element evidence remains distinct and unchanged.

The paired JSON records **25** actual web queries, provider/date and first-result coverage. Exact-title/author notice searches found no affecting formal notice in those returned sets; no exhaustive retraction audit is claimed. Fresh OpenAlex2015 metadata reports closed/no repository fulltext. ScienceDirect's indexed preview expands the2015 discovery context but does not supply full original methods/graphics. Previously denied endpoints were not repeatedly retried.

## Deferred handoffs

1. Obtain complete originals for Chaika/Derbasova2012 apparatus4(44):194–200 and Baranov etal2012 WCpowders2(42):88–94. The2017 citation listing gives the same apparatus title twice with incompatible issue/page combinations; the complete primary must settle the identity. The national-library entry and attempted archive route returned HTML but not those original papers.
2. Obtain legitimate complete methods, originalgraphics and SI for DOI[10.1016/j.corsci.2015.01.036](https://doi.org/10.1016/j.corsci.2015.01.036); preserve medium-dependent acceleration/inhibition as unadmitted discovery leads. No measurements imported from the abstract.
3. The titanium primary's reference11 adds a2011 Baranov tungsten-alloy-waste powder paper, pp158–165, without issue number. Investigate its identity and original apparatus/size data next; do not count it as independent replication now.
4. Titanium-specific follow-up needs source-resolved feed arms, original diffraction/size data, stock identity and matched abiotic mechanical/ferric controls before stronger causal or recovery claims.

## Validation and frozen state

Actual single-record validation exited0: **Checked1record(s);0failed**, session23156. Parent owns final corpus/history/review gates and independent review. Exact-base baseline reuse is documented in `/private/tmp/cmm-round43-initialization.json`; this agent did not execute a new baseline. Initially reviewed record SHA256 `627a897cadf7c806be66e6fc0a7b8c0f2928f374f6a8a1c56768409a1016718e`; new history SHA256 `75908fd0a32abbaf58ad8e34cc5e79a43a510a9ff175c5d18dcf38faf8629bf4`. All existing history sidecars remain unchanged. Final review pending; no self-approval.

## Independent-review correction

[Issue142](https://github.com/CultureBotAI/CMMMech/issues/142), stable key `CMMMech.titanium-metal.average-grain-size`, identified that the original wording lost the source's **average** qualifier. The preserved [initial review](../../../reviews/structured/20261012T023745Z-titanium-metal-round43-initial/review.yaml) precedes this correction. The record now describes the average grain-size estimate without implying an upper bound on every particle; the table above was corrected consistently. A new [EDIT history](../../../history/records/titanium-metal/2026-10-12T023836Z-codex-e31d46.yaml) preserves the earlier session. Final corrected record SHA256 `30e8ba344b68e000b74415cf7345252187af4f9075b4bfe2823257d63aae3e53`. Named validation rerun session40354 exited0, Checked1record(s);0failed, log `/private/tmp/cmm-round43-titanium-correction-validate.log`. Successor independent review and parent batch gates remain required.
