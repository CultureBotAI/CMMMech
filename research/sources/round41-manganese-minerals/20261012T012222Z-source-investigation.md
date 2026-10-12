# Todorokite and kutnohorite identity curation; fungal study remains deferred

UTC: 2026-10-12T01:22:22.271583+00:00
Author: codex, GPT-6, codex; this is an author handoff, not independent scientific approval.
Trusted base: `762508748eaa4f857179fa6f3450765bc62ebd6a`. Worktree: `/private/tmp/CMMMech-expansion-round41-20261012`.

## Decision and maintained scope

Created two distinct mineral identities, [todorokite](../../../data/records/todorokite.yaml) and [kutnohorite](../../../data/records/kutnohorite.yaml), using current IMA species authority plus complete original Handbook entries. Each adds chemical-identity and geological-occurrence context. Neither assigns a microbial mechanism, organism, criticality designation, recovery yield, industrial deployment or invented external identifier. A mineral produced by geological alteration remains a mineral; the Handbook's term secondary does not denote a processing residue here.

The experiment **10.2138/am-2021-7651** remains deferred under source-access issue134. This round recovered actual selected SEM reproductions through a new legitimate route, but not the missing original phase/control graphics. Mineral identity records do not resolve that experimental evidence gap.

## Authority and original-page inspection

The [CNMNC homepage](https://cnmnc.units.it/) freshly links the September2026 master list as the current edition. The original244-page PDF was reused from the verified round33 artifact, not represented as a fresh download. SHA256 `2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973`; retained at `/private/tmp/cmm-round41-manganese-minerals-research/raw/ima2026-09-reused.pdf`. Field definitions on page1 and actual rows on pages119/218 were visually inspected.

- Todorokite: IMA page218 identifies **A, approved;1962s.p.** The year is a special-procedure entry, not a modern approval-number CURIE. The current generalized formula includes variable cations and hydration. The complete [Handbook original](https://handbookofmineralogy.org/pdfs/todorokite.pdf) supports monoclinic character and weathering/alteration plus marine-nodule occurrence. Its older formula and natural-specimen chemistry are explicitly not substituted for the current IMA definition. No specimen analysis becomes a universal grade.
- Kutnohorite: IMA page119 identifies **G, grandfathered;1903**, an original-description year. Its CaMn2+(CO3)2 endmember is distinguished from natural Mg/Fe2+ substitution in the complete [Handbook original](https://www.handbookofmineralogy.org/pdfs/kutnohorite.pdf). The dolomite-group species, approximate Ca:Mn ordering and sediment-associated geological context support a useful record. Historical spelling kutnahorite is not a second mineral owner. Extracted-text loss of crystallographic overbars was observed; no such ambiguous crystal-system text was imported.

Both Handbook pages were fully read and visually inspected, including chemistry tables and their specimen/ideal-column distinctions. Original copyright-bearing files remain outsideGit. Record source locators name exact pages/sections. The IMA and both Handbook render paths are in the paired JSON manifest.

## Acquisition progress and limits

Five successful fresh HTTP200 acquisitions are documented in `/private/tmp/cmm-round41-manganese-minerals-research/acquisition-1.json`: two Handbook PDFs, current CNMNC homepage, SPbU grant report and a2025 coauthor review. Prior unchanged denied publisher/ResearchGate routes were not retried.

The complete public10-page review [Frank-Kamenetskaya and Vlasov2025](https://pureportal.spbu.ru/files/132149284/xk5108.pdf), *Crystallization induced by fungi and bacteria*, DOI10.1107/S2052520624011041, supplies **Figure7 on page5**, visually inspected. Its six panels reproduce2022 SEM images with attribution and permission: three todorokite and three kutnohorite panels. This is a real visual advance over manuscript extraction, but the caption's phase names cannot replace missing original PXRD evidence. Figure8 is from the separate2021 humboldtine study. Only claim-relevant manganese discussion/captions and title metadata were assessed; unrelated review sections were not independently re-reviewed.

The69-page [SPbU grant report](https://pureportal.spbu.ru/files/91305371/_2019_2021.pdf) supplies overlapping bibliography and summary material. All text and its graphics-object inventory were inspected computationally; pages39-40 were visually inspected and selected summary text60-61 read. These report an accepted manuscript, not a second independent experiment. Its page40 download labels contain PDF file-action relative paths; they are not embedded attachments or a verified accessible article URL. No complete main graphical suite was recovered from this route.

The [round40 handoff](../round40-manganese-ore-oxalates/20261012T005309Z-source-deferral.md) remains the provenance for accepted-manuscript web text and the official original supplementary PDF/CIF. Their reported main-table and condition discrepancies are not silently resolved by the2025 review. The next acceptance step is complete original main figure/table acquisition, especially PXRD2/4 and table1, followed by independent phase/controls/preparation/strain review for each substrate arm. The available SEM panels alone do not justify a microbial mechanism or conversion/recovery percentage.

## Deduplication and correction checks

Fresh `rg --no-ignore --hidden --follow` searches covered both round41 and original main `data/records`, `research`, `reviews` and `history`, then125 existing referenced raw roots. Exact commands, all roots, hits and empty error streams are in `dedup-receipt.json` and its companion files. There were1718 corpus hit lines in136 documents and10549 raw-text hit lines, including known oxalate records and the prior deferred study. Neither exact candidate owner ID was present before creation. No current record text matched either mineral name in the separate direct check. This is a declared repository/referenced-text boundary, not machine-wide absence or automatic binary-PDF/image/archive content search.

Bounded DOI erratum/retraction and current mineral-name-change queries returned no affecting notice in their returned sets. That is not an exhaustive absence claim. The old manuscript's Correction3 label is a manuscript version, not a demonstrated published correction. Exact web responses are retained outsideGit.

## Frozen targets and checks

- `data/records/todorokite.yaml` SHA256 `a8d602a0aabbd1c4fa3b8e53d3ed580d9f51ab8d6b5dd5ce53aecae5516d9088`; CREATE `history/records/todorokite/2026-10-12T011958Z-codex-817443.yaml` SHA256 `0c983b2aadfee03ac706bde3ca00a19d4d7a2d7e0156618645a9840a8b3d52ec`.
- `data/records/kutnohorite.yaml` SHA256 `20562fc3fdb5fc1b2be7f521ae0701920de6a61f994b38dc596c9cc75372ddcd`; CREATE `history/records/kutnohorite/2026-10-12T012017Z-codex-31a32c.yaml` SHA256 `750f0181fa2cc36208d76d5f976a696e643da18dc121bb7b187bf3cb58784ef6`.

Named validation finished successfully: **2records checked,0failed**. Log: `/private/tmp/cmm-round41-manganese-minerals-research/named-validation.log`, SHA256 `4022ad8ba440a72bf4f1c8b321e447df36133d812f52f21611becf103551b042`. Canonical CREATE sessions and distinct inline events record actual work; no earlier history changed. Independent native scientific review and final cohort gates are coordinator-owned and still pending at this handoff. The paired JSON pins all retained raw artifacts and acquisition/dedup evidence; raw originals remain outsideGit.
