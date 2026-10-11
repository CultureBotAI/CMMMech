# Round16 produced-water source assessment

- UTC: 2026-10-11T10:25:17.810764+00:00
- Curator: codex (GPT-6; codex), agent /root/round16_produced_water.
- Worktree: `/private/tmp/CMMMech-expansion-round16-20261011`; branch `curate/cmm-expansion-round16-20261011`.
- Trusted base: `b714ce2bd8050d5e19ed9ca072460ba2b8154c3b`.
- Scope: resolve Hu2021 from round15 brine supplementary reference10; assess a distinct produced-water feed identity and defensible microbial claim.

## Decision and identity

Added `data/records/oil-and-gas-produced-water.yaml` as an **identity-only secondary_resource**. USGS Fact Sheet 2014-3104, pp. 1-2, explicitly includes formation water, injected returns and other waters from hydrocarbon wells. Here the material is the generated production byproduct considered for constituent recovery. It is not a mineral species, elemental lithium, or an untouched geological brine. The existing geothermal-brine record remains distinct. No assumed lithium content, universal hypersalinity, criticality designation, organism identifier, microbial treatment outcome or industrial deployment is accepted.

USGS historical Mendenhall opportunity 23-04 supplies resource context: petroleum co-produced waters are investigated for lithium. Its November 2024 deadline is historical, not evidence of current recruitment, completed research or recovery performance. The broader USGS Thesaurus term2270 was inspected but no exact identifier was assigned to this narrower oil-and-gas stream.

## Primary mechanism assessment: deferred

Hu, Wang, Xu and Zhang, *Biomineralization of hypersaline produced water using microbially induced calcite precipitation*, Water Research 190 (2021)116753, DOI [10.1016/j.watres.2020.116753](https://doi.org/10.1016/j.watres.2020.116753), PMID [33360619](https://pubmed.ncbi.nlm.nih.gov/33360619/). Publication metadata distinguishes December 2020 online publication from February 2021 volume issue. Crossref and PubMed verify authors/title/DOI, not the methods.

The publisher's accessible materials snippet identifies a Permian Basin disposal-site feed from Jal, New Mexico. Abstract/intro snippets describe an activated-sludge-derived consortium and calcium/heavy-metal pretreatment. These are discovery information, not accepted record mechanisms: full main methods, complete results/figures and adequate controls were not acquired. No evidence of lithium recovery was accepted.

The actual publisher supporting DOCX was acquired and opened as a valid ZIP/XML document, with matching article title/authors. Text/tables and Figures S1/S5 were inspected; the supplement does not replace unavailable main text. Table S1 compares 1:1 PW:synthetic-domestic-wastewater feed with 4 g/L urea against a no-urea condition. Its reported 100% As/Cd/Mn/Ni removal rests on ND effluent values; MDLs are respectively 0.1,0.001,0.0017,0.002 mg/L. ND is not a measured zero, and these liquid values cannot become mg/kg concentration cells. Figure S5 caption repeats 1:1 for both salinities, whereas the embedded legend distinguishes 1:1 and 3:1. Resolve that source discrepancy with the main methods before curation. Genus composition cannot establish isolate-specific causality. Table S2 is an economic estimate, not evidence of industrial operation. Other supplementary figures were text-screened; not every graphical element was independently rendered.

## Acquisition and reuse

Raw root: `/private/tmp/cmm-round16-produced-water-raw`. Full acquisition ledger with URLs, actual UTC times, HTTP statuses, bytes and SHA256 is reproduced in the paired ingest JSON. The verified USGS PDF was read in full and p2 definitions rendered. Its identity source has DOI10.3133/fs20143104. USGS government authored text is used as source evidence; no raw PDF is committed. Publisher content has no verified redistribution license; retain outside Git. Reading access does not grant redistribution rights.

| Artifact | Result | SHA256 |
|---|---|---|
| `usgs2014.pdf` | HTTP 200,4-page primary agency PDF | `9e180cef5ba29cd24b693ba59ee3ed34ba125747aeff7f77abff9979e09c3485` |
| `usgs-resource.html` | HTTP 200, historical USGS resource opportunity | `fc0b574eb3532de616281f0e26d50c5ad882726efa2d680d6806911c2b235c83` |
| `publisher-supp.docx` | HTTP 200, valid supporting DOCX | `ee93c7e2bdb9364106653a5efaba167779eec42ff368f216d60c1c5addedd47a` |
| Main publisher | HTTP 403 HTML error, not fulltext | see ledger |
| Crossref-linked Elsevier XML | HTTP 429 JSON error, not XML | see ledger |
| OpenAlex | closed; no repository fulltext location returned | see ledger |
| Author university publications index | verifies citation but links publisher only | see ledger |

The guessed university resources route and NSF search route returned 404. Exact-title/DOI repository searches did not yield a primary manuscript in their returned result sets. No access controls were bypassed, authors contacted, payment made, or access fabricated.

## Search, deduplication and contrary evidence

Queried the web search provider on 2026-10-11 using the exact strings in paired JSON; first returned result sets only, no exhaustive pagination. Explicit correction/retraction/erratum query returned no relevant notice in that bounded set. Crossref `update-to` was null and `relation` empty; this does not prove no corrections exist. No mechanism is accepted, so the lack of full controls is preserved as a deferral rather than filled from reviews.

Deduplication used `rg --no-ignore --hidden --follow` over `data`, `research`, `reviews`, `/private/tmp/cmm-round15-brine-raw`, and this task raw directory, with binary PDF/ZIP contents handled separately where relevant. Terms included normalized DOI 116753, produced-water spellings, exact proposed ID and secondary-resource identities. The referenced `/private/tmp/cmm-round15-brine-review` directory was unavailable; that boundary limitation is retained. Existing reports mention the Hu2021 lead, while the searched pre-change records have no matching produced-water root. No machine-wide or global novelty claim is made. The paper, publisher snippets, abstract, conference abstract and supplement are one experiment, not independent replications.

## Ranked handoff

1. Independently review the new identity-only record and final bytes/history. One-file validator passed (1 record, 0 failed); trusted-base history check passed (139 sessions, 0 errors at that instant). Parent runs final full-batch gates.
2. Acquire a legitimate full Hu2021 manuscript and main figures. Reconcile PW dilution/SDW ratio, inoculum preparation, temperature/residence time, biochar controls, killed/no-inoculum/chemistry-matched controls, fraction handling, ND outcomes and mass balance. Only then consider adding a mechanism to the existing new root. No separate lithium-produced-water root is justified by the present evidence.
3. Follow the newly surfaced publisher lead *Mechanistic insights into ureolytic MICP by halotolerant Bacillus pumilus Soc1 for circular valorization of reverse osmosis brine*, Journal of Water Process Engineering 89 (July 2026)110282, [PII S2214714426008408](https://www.sciencedirect.com/science/article/pii/S2214714426008408). Indexed abstract only in this pass; full methods/supplements, taxon/strain and real RO-feed identity require checking. A full-scale source facility does not establish full-scale microbial treatment. RO concentrate is a separate process stream candidate, not automatically oilfield produced water.
4. A further indexed lead, *Engineering microbiome for carbonate precipitation in heavy oil produced water: Hot-zone identification of ion accumulation and crystallization*, [PII S0304389425032376](https://www.sciencedirect.com/science/article/pii/S0304389425032376), remains unverified beyond discovery; publisher open failed. Resolve source identity and full experiment before assigning any distinct root or mechanism.

## Output and remaining limits

Accepted record: `data/records/oil-and-gas-produced-water.yaml`.
Canonical CREATE sidecar: `history/records/oil-and-gas-produced-water/2026-10-11T102408Z-codex-39636b.yaml`.
No schema, validator, existing record, criticality list or governance change was required. This source assessment is not its independent scientific acceptance review. Produced-water mechanisms and related saline-feed candidates remain open evidence work; this bounded investigation does not establish corpus exhaustion.
