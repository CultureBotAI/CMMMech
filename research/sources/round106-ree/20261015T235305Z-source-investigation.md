# Round106 rare-earth source investigation

- UTC: 2026-10-15T23:53:05.919866+00:00
- Researcher: codex; actual model GPT-6; tool codex; agent /root/round104_ree.
- Worktree: `/private/tmp/CMMMech-expansion-round106-20261015`; branch `curate/cmm-expansion-round106-20261015`.
- Reviewed source base: `af6cbead934deb4667764fa4a325246158ee4a0a`.
- Machine-readable companion: `20261015T235305Z-source-investigation.json`. Raw acquisition receipts, original PDFs, page renders, web logs and hashes remain under `/private/tmp/cmm-round106-ree-research`.

## Selection and deduplication

Two new mineral owners are supported: **monazite-(Gd)**, IMA2022-055, and **xenotime-(Gd)**, IMA2023-091. They share ideal Gd(PO4) but have different monoclinic and tetragonal structures. They are separate from elemental gadolinium, other monazite/xenotime species and mixed ores. Natural material contains several REEs; dominant Gd is not a claim of a pure end-member.

Before creation, `rg --no-ignore --hidden --follow` searched names, exact IMA IDs and DOIs across maintained records, research, reviews, history, local skills, the cited round104/105 raw REE roots and original-main ignored reports. The only three semantic matches were prior raw authority/reference context. The all-state issue inventory contained293 titles/bodies with no Gd-pair match; issue comments were not searched. No machine-wide or literature-wide absence is claimed.

## Verified authority and primary evidence

The fresh official IMA homepage links the September2026 edition. Its previously acquired bytes were rechecked, with definitions page1 and species rows146/236 visually inspected. The PDF SHA256 is `2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973`. This is reuse with a current homepage check, not a claimed fresh PDF download.

[Ondrejka et al.2023](https://doi.org/10.1180/mgm.2023.37) is complete in the SAV public library copy: seven original pages plus a permission notice. Every page, Tables1–4 and Figures1–3 was inspected. The study uses WDS chemistry, Raman and selected-area electron diffraction on natural material. Table2's22.84wt%Gd2O3 mean covers six analyses with substantial Sm/Nd. The reported abstract/Table3 cell is estimated from weighted synthetic end-members, whereas the larger, less precise SAED cell is a separate result. Neither is a single-crystal XRD refinement. Density is calculated and several physical properties are unmeasured. The proposed hydrothermal origin remains an interpretation. The original reprints a Raman spectrum also reported in a companion paper's supplement; that separate supplement was not acquired or counted as independent replication.

[Ondrejka et al.2024](https://doi.org/10.1180/mgm.2024.62) is a complete ten-page SAV library original. All pages, Tables1–5 and Figures1–4 were inspected. The holotype FIB lamella is tied to microscopic Gd-rich domains in xenotime-(Y), with six analysis positions located in Figure1. Table2's mean is29.16wt%Gd2O3. HRTEM/FFT supports the tetragonal identity. Table3's powder pattern is calculated; measured powder and single-crystal XRD were unavailable. The25-reflection cell refinement is separate from weighted end-member estimates. Density and refractive index are calculated. REE photoluminescence obscures parts of the Raman signal.

The [2026 corrigendum](https://doi.org/10.1180/mgm.2025.10190) corrects swapped black Y/Gd Raman traces in Figure4. Full publisher correction text and the corrected original PNG were inspected and compared with the original. The authors retain the text and interpretations. Crossref confirms online publication13January2026; the DOI's2025 component is not its publication year. Original Crossref `relation` and `update-to` fields were empty despite this real correction, so those fields alone cannot establish no correction.

## Access, conflicts and limits

- Monazite Crossref lookup returned429; its DOI/title are verified through the full original and publisher page instead.
- Xenotime original was acquired through a public SAV coauthor-library page after publisher requests failed. The refreshed Uher author page lacked the target in its first ten results; a different observed Caplovicova author-result link supplied the actual PDF.
- Xenotime reports supplementary CIF AMCSD0021444. Publisher full/abstract/content routes and AMCSD entry routes were unavailable in this bounded pass. No CIF bytes, raw intensities or refined atomic model were independently verified. The record discloses this gap and assigns no AMCSD identifier.
- Published cell-method differences, calculated properties, natural substitutions, and the corrected spectrum are retained. Geological co-occurrence is not microbial causality or a controlled formation experiment.
- No recovery yield, jurisdiction-specific criticality designation, organism assertion or industrial deployment is assigned. These are laboratory characterizations of natural minerals.
- Public reading access does not grant bulk redistribution rights. Copyrighted PDFs and figures stay outside Git; the monazite copy expressly restricts further reproduction.

## Bounded initial leads and source handoff

Existing [issue405](https://github.com/CultureBotAI/CMMMech/issues/405) remains the handoff for DOI10.1016/j.gca.2026.02.015 and the M.auratinigra La/Gd datasets. Fresh OpenAlex reports closed access without a repository full text. New title/repository searches did not provide the missing complete article. The round105 two-workbook/62-file inventory is preserved; the105.6MBZIP and60image files were not redownloaded. No new microbial claim was made from snippets or spreadsheet labels.

Existing [issue406](https://github.com/CultureBotAI/CMMMech/issues/406) retains florencite-(Nd)'s missing1971original and1986diffraction evidence. Bounded new title/publisher queries did not resolve them. Unchanged failed RRUFF/nominalPDF routes were not retried. No florencite-(Nd) owner was created.

One new follow-up is appropriate: retrieve the legitimate xenotime CIF/publisher supplement, inspect sample metadata and the distinction between calculated model and measured electron evidence, then amend only claims supported by that inspection. Existing scoped identity is not a claim of a complete atomic-model audit. Root handles any issue creation after deduplication.

## Repeatable search and validation

The JSON companion records31 exact web queries, providers, date, first-result-set coverage, selected direct routes, acquisition outcomes and artifact hashes. Search included correction/erratum/retraction and supplement queries. No affecting monazite notice was found in the inspected bounded results; this is not an exhaustive absence claim. Original acquisition failures remain recorded.

Both owner files passed named `cmmmech validate ... --require-records`:2records,0failed. Receipt: `/private/tmp/cmm-round106-ree-research/named-validation.json`. Canonical CREATE histories precede review hashes. The existing schema supports these identity-only records; no schema or validator change was needed. Independent native scientific reviews and root batch gates are still separate required steps.

## Frozen owners

- `data/records/monazite-gd.yaml` SHA256 `22dadc915191c2e871fd01ac84205b4489c90c39d1145e3f1d7531da483a4b34`; history `history/records/monazite-gd/2026-10-15T235136Z-codex-3749ea.yaml` SHA256 `01479516f339d057a650f46890dd8d4c4bc6951d33f662eb573971c19dc38bb0`.
- `data/records/xenotime-gd.yaml` SHA256 `94ea0b1119f49bf293fb2a7ce65872a58aa0cf5c046202cdb209b66e710c79e4`; history `history/records/xenotime-gd/2026-10-15T235147Z-codex-46ec8c.yaml` SHA256 `84c7ae676ce2f7950e59086d517e617edec78072ef060a4800056eef4bdb935c`.
