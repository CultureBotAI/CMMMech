# Zircon-feed follow-up and chemical eudialyte-concentrate evidence

## Scope and provenance

UTC: 2026-10-12T09:59:15Z. Investigator: Codex `/root/round43_hardmetal`, GPT-6.
Worktree: `/private/tmp/CMMMech-expansion-round53-20261012`; branch `curate/cmm-expansion-round53-20261012`; base `b85c2c2c753fe83a2fc21f073ee1e49675ae647e`.
This succeeds the [round51 zircon assessment](../round51-zircon-feed/20261012T082652Z-source-investigation.md) and addresses a bounded part of [issue153](https://github.com/CultureBotAI/CMMMech/issues/153).

**Decision:** retain the microbial zircon-feed deferral; curate one distinct **eudialyte concentrate** from complete chemical recovery evidence. This is a source assessment and curation handoff, not its independent scientific acceptance review. The accepted owner is an upgraded primary resource, not a species, group, commodity, waste or element. No criticality claim is proposed, so a jurisdiction/list assessment is inapplicable.

## Changed routes and actual acquisition

Exact queries, dates, returned first result sets, requests, responses and hashes are retained in the paired JSON and external artifact inventory. Searches used no pagination or recency filter. No author contact, purchase or access-control bypass occurred.

| Route | Actual result | Fitness |
| --- | --- | --- |
| Reachable CSIR-NCL author bibliography and exact Bansal article link | Bibliography corroborates article; exact linked page returned403 | New route did not supply missing Figure1/4 |
| Bansal public author bibliography | Web timeout; direct request certificate-verification failure | No full text or image acquired; certificate check was not disabled |
| Schippers, Biomining2023 public original extended abstract | Complete2-pagePDF acquired, both pages viewed | Author context for Hedrich matched-acid null result; no original assay tables or methods |
| Previously reported Leibniz project-volume URL | Web error again | Not new scientific progress; unchanged limitation retained |
| Ma2019 RWTH record758718 | Indexed institutional metadata verifies title/authors/DOI/issue; direct PDF URL returns tinyHTML; web reader misbinds it to unrelated Paskin paper | Failed PDF content was rejected |
| Ma2019 publisher original landing/fulltext route | Web metadata readable; directGET403; Supplements tab gives no visible file entry | Bibliographic authority, not a downloaded primary PDF |
| Indexed open Ma2019 original PDF mirror | HTTP200,565200bytes, valid12-page original; SHA256`8c8f68490eef55fc657afa3d4762bd6a1e397c1a803c6a95ebec3125ad4924a7` | Full original scientific text and every graphic inspected |
| Newly found author-group RWTH test-subdomain PDF | Direct DNS failure | Honest failed corroborating route, no fresh primary bytes |

The full original is [Ma, Stopic and Friedrich2019](https://doi.org/10.1595/205651318X15270000571362), *Johnson Matthey Technology Review*63(1):2–13. Its DOI/title/authors/pages agree with the primary publisher and [RWTH institutional record](https://publications.rwth-aachen.de/record/758718). RWTH's2018-12-04 online date differs from the2019 issue date; both are preserved. PDF metadata dates are file history, not new experiments. The inspected [mirror](https://pdfs.semanticscholar.org/836a/07cfca436826fbbf06a7c18f00ca654cb55f.pdf) is the correct complete original, not the unrelated response returned for the institutional PDF URL.

## Owner and experiment deduplication

Ignored and hidden files were included and relevant symlinks followed across current and original checkout `data/records`, `research`, `reviews` and `history`, plus194 existing cited raw/research/evidence roots.4092 metadata files were read;654 corpus and3587 raw matching lines were retained. No matching concentrate owner was found within those bounds. Nine unavailable historical raw roots are explicitly listed in JSON. Binary PDF/image/archive contents were not all decoded, and unrelated machine directories were excluded; this is not machine-wide absence.

The existing [eudialyte ore](../../../data/records/eudialyte-ore.yaml) explicitly describes Hunter2020 jaw-crushed and ground ore with unestablished mineral proportions/grade and excludes upgraded concentrate. Ma2019 Methods pp.3–4 explicitly describe crushing and partly magnetic beneficiation of TANBREEZ ore, with measured feed composition and QEMSCAN phase proportions. Thus the concentrate owner is based on processing state and composition, not merely a second paper or locality. No exact specimen equivalence between the studies is claimed. Extraction alone does not make this natural feed a secondary resource.

The exact Ma2019 DOI was previously present only in Hedrich reference metadata and recursively retained dedup receipts, not as an accepted experiment. Its earlier same-group modeling reference DOI10.3390/met8040267 and the prior fuming study DOI10.1016/j.mineng.2016.12.011 are contextual leads; their experiments were not counted as independent replication or separately imported.

## Complete primary assessment

All12 PDF pages (printed2–13), Figures1–18, TablesI–IV and equations were personally viewed, and the scientific text, methods, references and acknowledgements were read. No supplement is declared in the complete paper. The publisher Supplements tab exposed no file entry in the web reader; directHTML access failed. This is a bounded interface observation, not proof that no underlying measurements or supplementary files exist. No raw measurement workbook or data dictionary was supplied or invented.

| Claim | Exact evidence | Retained boundary |
| --- | --- | --- |
| Beneficiated mixed feed | Methods pp.3–4; TableI; Figures1–4 | TANBREEZ southernGreenland feed,67.05% QEMSCAN eudialyte classification,1.60wt%TREE/6.46wt%Zr; no universal grade or IMA species assignment |
| Chemical leaching | Methods p.6; Figures10–13 |500g laboratory aliquots,10MHCl,1.25L/kg,40min digestion;2L/kg water; about88.8% solution extraction at selectedconditions; no microbial arm |
| Temperature and time | Section4.1.2/4.1.4; TableIII; Figure15 | No externalheat nevertheless70–80degreesC digestion; subsequentwaterleach20–25degreesC;1h labparametercomparisons versus30minpilot preserved |
| Impurity separation | TableII, Figure14 | pHabout4/CaCO3 removesco-leachedZr/Al/Fe withREE loss; no isolatedZr/Hf/Nb product |
| Actual pilot | Section3.2/4.2; TableIII; Figures7–9,15–17 |36kg test, two40L digestionreactors,6kg percharge; alternatingfeed needed; not continuouscommercialdeployment |
| Mixed product | p.11, Figure18, TableIV | Carbonate assignedbyprocess; >98.8% precipitationfromliquor versus85.5% reportedoverallrecovery; no pure singleelementproduct |

TableIV prints TREE29.95wt%, while the individually listed REE cells sum30.40wt%; the article rounds the product grade to about30wt%. The discrepancy is retained without silently replacing a measured value. TableIV also retainsAl3.31wt% andCa4.18wt%, so elementalgrade is not carbonatephasepurity. No productdiffraction or finalsolidmass is supplied. Figure16 reports major processflows, not a closed elementbalance through final dissolution/reprecipitation. The85.5% recovery remains source-reported, not independently recalculated. Equation(x) is schematic/unbalanced as printed and is not used to infer new stoichiometry. Initialfeed Figure3 contains a legend class named eudialyte leach residue; that label is not treated as proof that the suppliedfeed had previously been chemically leached.

Missing replicate counts/statistical uncertainties prevent independent inference from small differences among bars. Pilot mixing difficulties and residual eudialyte are retained. Environmental superiority, operating cost, sustainedthroughput and industrialdeployment do not follow from absence of externalheating or a pilotphoto. Percentages, wt% and solutionconcentrations remain qualified prose; they were not converted into unsupported native mg/kg observation cells.

## Unresolved zircon evidence

Bansal2007 DOI10.1021/la062535x still lacks personally inspectable original Figure1 TEM/SAED and Figure4 paired sandXPS. The prior text, Figures2/3/5 and two ACS supporting artifacts were not re-downloaded or re-viewed this pass; their previous provenance remains in round51/round50. No repeated RMIT files-array probe or prior ResearchGate figure/PDF failure is presented as new acquisition.

Hedrich2023 DOI10.1016/j.hydromet.2023.106068 still lacks its complete primary methods, feed characterization, graphics and supplements. Newly acquired [Schippers2023 original extended abstract](https://www.min-eng.com/biomining23/drafts/session1/schippers.pdf) independently confirms the coauthor's published interpretation that matched acid conditions give no additional biological extraction effect, but supplies no missing experiment detail. Its general industry statements are not imported. Neither this context nor the chemically treated concentrate closes issue153 or licenses inherited microbial claims.

The exact DOI notice queries returned no applicable correction/retraction in the inspected first sets. Crossmark was not separately checked; universal absence is not asserted. A later financial critical report appeared in search but was not promoted to primary experimental evidence.

## Curation, checks and next actions

- Record: [`data/records/eudialyte-concentrate.yaml`](../../../data/records/eudialyte-concentrate.yaml); SHA256`afa309420e2e20f08868b5708c24e08ba612088643b9c484d9c53d755846b647`.
- Actual CREATE: [`history/records/eudialyte-concentrate/2026-10-12T095619Z-codex-9b0f45.yaml`](../../../history/records/eudialyte-concentrate/2026-10-12T095619Z-codex-9b0f45.yaml); SHA256`a86172b746388969cdd20a1c3610746e1e9b5a667d0e2cb891ba3eca08b90a49`. Inline event and attached sidecar are distinct.
- Named validation completed exit0: `uv run --locked cmmmech validate data/records/eudialyte-concentrate.yaml`;1record,0failed. Exact receipt/log hash are in JSON.
- Baseline is the parent's just-completed freshmain check at the exact unchanged base/tree; shared final gates and independent review are coordinated separately. No schema/validator/tests/README/pages/governance/Git/GitHub mutation by this curator.

First independently review the new concentrate record against all original graphics, table arithmetic and owner boundary. Continue issue153 through genuinely new routes for Bansal Figures1/4 and complete Hedrich evidence. An acquired chemical concentrate is not a substitute microbial experiment. If further quantitative process assessment is needed, obtain final product mass, impurity-removal/reprecipitation details, raw repeat data and the related prior modeling study with experiment-overlap assessment.

Raw originals remain outsideGit. The original bears©2019JohnsonMatthey and the publisher marksOA, but a specific redistributionlicense was not verified. The record and dossier retain factualparaphrase and locators, not the copyrighted article/graphics. The pairedJSON inventories 50 externalartifacts with exacthashes; reportformat, links,JSONparse and trailingwhitespace are checked by the builder. Scientificacceptance remains the independentreviewer's task.
