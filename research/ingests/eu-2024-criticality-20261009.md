# Historical EU 2024 criticality: Annex I/II verification

Prepared by Codex (GPT-6), 2026-10-09 UTC, against accepted base
`610d27a40d89861961052f0e0bebfaa7882e35cf` plus this working change.
This is a curation dossier, not an independent acceptance review.

## Scope and decision

Discovery input A2 in
`research/sources/cmm-landscape/20261008T073140Z.md` had an access limitation.
Ordinary public HTTPS retrieval now obtained the complete authentic original
act, English consolidated text, metadata, two English corrigenda, and an official
Commission group-definition source. Earlier access failures remain historical;
they are not evidence that the authority is unavailable.

Append dated **critical** EU entries to neodymium, palladium, lithium and
manganese. The Nd/Pd mappings explicitly use issuer-defined groups. Preserve
every preceding identity, mechanism, evidence entry and dated designation.
No strategic designation or resource-level inheritance is imported. Cobalt's
existing original-2024 Annex II(h) mapping was rechecked and requires no edit.
Uranium/vanadium are assessed below only, leaving their records to the other
curator. Hidden and ignored files were included in the scoped deduplication
searches of records, history, reviews and research.

## Primary authority and edition

[Regulation (EU) 2024/1252, authentic original OJ PDF](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202401252),
adopted 11 April and published 3 May 2024, has 67 pages. Annex I Section 1
is on page 55; Annex II Section 1 spans pages 57–58. The original act supplies
the stored historical edition, not a claim about every later edition or present
operational eligibility. Article 49 gives entry into force 20 days after publication.

The [English consolidated PDF](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:02024R1252-20240503)
has 71 pages, header `02024R1252 — EN — 03.05.2024 — 000.002`. Its first page
expressly identifies it as a documentation tool rather than an authentic legal
text. The complete 17-entry strategic list (page 57) and 34-entry critical list
(page 59) agree with the original for all entries. Text was extracted with
PyMuPDF; the original pages 55, 57–58 and consolidated page 59 were also visually
checked. The complete lists, rather than keyword snippets, support the bounded
absence findings below.

| Element | Annex II: critical, original 2024 | Annex I: strategic, original 2024 | Curation decision |
| --- | --- | --- | --- |
| Co | (h), directly named | (d), directly named | Existing critical mapping correct; unchanged |
| Nd | (r), through light rare earths | (n), expressly Nd among REEs for permanent magnets | Add critical group mapping; no unqualified strategic assertion |
| Pd | (aa), through platinum group metals | (m), through the same group | Add critical group mapping only |
| Li | (s), directly named without a grade qualifier | (h), battery-grade qualification | Add critical only |
| Mn | (u), directly named without a grade qualifier | (j), battery-grade qualification | Add critical only |
| U | Not named or covered by these listed groups | Not named or covered by these listed groups | Dossier only; no new record assertion |
| V | (ah), directly named | Absent from the complete list | Dossier only; no record edit in this task |

Articles 3(1) and 4(1) cover unprocessed materials, processing stages and
by-products. Recital 8 addresses the value chain leading to a specified grade.
The strategic qualifiers therefore must not be reduced to a claim that only
an already finished battery chemical is covered. Nor do they justify attaching
an unqualified strategic flag to every Li/Mn form. Mineral species, secondary
resources and chemical elements remain separate record concepts.

## Group mapping evidence

[European Commission COM(2017) 490 final](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:52017DC0490),
13 September 2017, is an eight-page issuer publication. Annex 1, page 4,
footnote 12 explicitly places Nd in the five-member light-REE group; footnote
13 explicitly includes Pd in the five-member PGM group. Both footnotes and their
group labels were verified from the complete PDF text and a rendered page.
This source supplies **membership only**. The separate 2024 legal act supplies
the designation. The mapping from those issuer group definitions to Annex II
is an explicit curation inference, not an assertion that the 2017 list is the
2024 authority. Each affected record includes both sources and identifies the
membership source in the list entry.

The 2023 Commission assessment was also sought. Its directly linked DG GROW
PDF returned HTTP 403; that attempted file was not acquired. The accessible
2017 issuer definition resolves these two stable group memberships without
pretending to have read the unavailable 2023 report.

## Corrigenda and amendment context

The [EUR-Lex act metadata](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024R1252)
was retrieved on 2026-10-09. It exposes the 03/05/2024 consolidated version,
two general corrections, and three language-specific corrections marked PT,
NL and EL. The English consolidated header incorporates C1 and C2:

- [Corrigendum 2024/90330, 3 June 2024](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1252R(01)):
  date substitutions in Articles 27, 28, 31, 44, 47, 48 and 49; no Annex I/II
  list alteration.
- [Corrigendum 2024/90589, 1 October 2024](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1252R(02)):
  wording in Article 30(4) and Article 43's market-surveillance amendment; no
  Annex I/II list alteration.

The operative English text of both corrections was read. The PT/NL/EL
corrections were identified in metadata but not independently translated or
reviewed; this dossier makes no multilingual equivalence claim. Metadata also
lists amendment **proposals** `52025PC0946` and `52026PC0590`; their presence is
not treated as an enacted amendment. This bounded check supports the stored
historical edition, not an exhaustive assertion of current law worldwide.

Discovery searches included official-domain queries for the regulation's
corrigenda and amendment status, and for Commission Nd/LREE and Pd/PGM group
definitions. Third-party mirrors were not used as designation authorities.

## Acquisition and reuse

Machine-readable requests, timestamps, response metadata and SHA-256 hashes:
[`eu-2024-acquisition-20261009.json`](eu-2024-acquisition-20261009.json).
Raw bytes and derived text/images are retained in `/private/tmp/cmm-next-eu/`.
Requests succeeded on 2026-10-09 between 05:42:31 and 05:50:06 UTC. The manifest
also retains the blocked 2023 request. Main source fingerprints:

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| `original-oj.pdf` | 2291732 | `eb89f374a725ebde267c90f237898cd1d0bdfa65a1d4a118511e225bde60283e` |
| `consolidated-20240503.pdf` | 809331 | `e51011f38cc440fdeccbb6cd1adbef84641c278eb698d8285341e4d2144993cd` |
| `group-definitions-2017.pdf` | 446654 | `9a3407b786c9cefb486a84e456b0411537593d5da14b35e18f0f1585ad04718d` |

The [EUR-Lex reuse notice](https://eur-lex.europa.eu/content/legal-notice/legal-notice.html)
permits commercial/noncommercial reuse of legal documents unless otherwise
specified, under the Commission document-reuse policy based on Decision
2011/833/EU. It separately identifies EU-owned editorial content and consolidated
texts as CC BY 4.0, requiring attribution and indication of changes, and metadata
as CC0. These distinctions are retained; no blanket CC BY label is assigned to
all EUR-Lex documents. This dossier paraphrases and attributes source facts;
original PDFs are not represented as CMMMech-authored material.

## Local checks and handoff

The Li EU-only record validated before release to the Li raw-data curator.
Nd, Pd and Mn subsequently validated together: three records, zero failures.
Four new EU history sidecars validated against `610d27a`: zero errors. A parsed
comparison against that base proved unchanged prior scientific fields and
unchanged list prefixes in all four records at EU handoff. A transient Nd
history indentation error was caught by validation and fixed before release.

EU-only handoff hashes are below. Li will legitimately change further under
its separate raw-data curation and combined independent review.

| Record | SHA-256 |
| --- | --- |
| neodymium | `3740247c0a93c9af1e068719aa552b43ead2c62b015f3ae98071972b84d88268` |
| palladium | `7f75405ad97e3a2c8cf45b995f58aba01a91771b3075fc7411d5049bf3389acb` |
| manganese | `e4f1d82ea63679f0f3062e4606254326e1830a2b88e4ae84630d819fdc535634` |
| lithium, EU-only handoff | `de9ca530a1cac1189909bcda67f3adac143e85a8a0f62c307913ec077f19f2ce` |

Independent reviewers must check the exact source locators, the historical
scope, group mapping, grade distinction, source/history references and final
record bytes. This dossier does not self-accept the records. Root will run the
combined repository gates after other concurrent changes stabilize.
