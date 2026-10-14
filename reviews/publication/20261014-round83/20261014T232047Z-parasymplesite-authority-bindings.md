# Parasymplesite review authority-artifact mapping

Recorded UTC: 2026-10-14T23:20:47.602249+00:00. Issue [279](https://github.com/CultureBotAI/CMMMech/issues/279).

Maps four existing native review authority rows to exact archived artifacts and an existing dossier. No new science, verdict, experiment, acquisition or history; immutable review and owner bytes unchanged. Native schema allows these optional metadata fields to be absent.

Immutable review: [20261014T231235Z-parasymplesite-round83-independent](../../structured/20261014T231235Z-parasymplesite-round83-independent/review.yaml), SHA256 `370b81af27947f4a6b5dfd1b58192e1d441593e94bd65850733284e7785bcaee`.

Dossier: `research/sources/round83-phosphates/20261014T225525Z-source-investigation.json`, SHA256 `a822965572a16f6f5f71e20eed593da1816e50b07ab9780a9d78de4a76e4ae97`.

| Evidence ID | Authority reference | Archived artifact | SHA256 |
|---|---|---|---|
| handbook | [handbook](https://www.handbookofmineralogy.org/pdfs/parasymplesite.pdf) | `/private/tmp/cmm-round83-phosphates-research/parasymplesite-handbook.pdf` | `b889ce6ae73ad314df90102e4e382291fbb757dd8b570391ca950cc8a8759f4d` |
| ima | [ima](https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf) | `/private/tmp/cmm-round80-carbonates-research/ima2026-09.pdf` | `2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973` |
| genbank | [genbank](https://www.ncbi.nlm.nih.gov/nuccore/MZ227386.1) | `/private/tmp/cmm-round83-phosphates-research/mz227386.xml` | `3c74b180f546e5aa41c41747c0da747c8dcfe042ebbff842ac10d73bd456f167` |
| taxonomy | [taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1896336) | `/private/tmp/cmm-round83-phosphates-research/citrobacter-sp-taxonomy.xml` | `379b70e555a5de4147ea3948a576fed4cc38800989405078fb3e91f676e746ec` |

The paired JSON retains source locators and prior-acquisition scope. The final independent package audit verifies these links; this addendum does not replace or rewrite the scientific review.
