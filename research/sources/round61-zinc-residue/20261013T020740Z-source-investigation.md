# CMM source investigation: zinc-leach-residue follow-up

## Scope and provenance

UTC: 2026-10-13T02:07:40.186887+00:00. Researcher: Codex, agent `round61_zinc_sources` / GPT-6. Reviewed repository base `78ba2f4c84ff84be64b0da23e603f59c761905aa` on `research/cmm-source-followups-round61-20261013`. This assessment advances [issue #186](https://github.com/CultureBotAI/CMMMech/issues/186); it does not create or accept a record. Repository science was read only. The parallel lead-paste report visible in the worktree was preserved.

The question is whether complete primary evidence can support a distinct zinc-leach-residue secondary-resource owner. This is separate from zinc element, sphalerite mineral, zinc commodity, and zinc-purification residue. Criticality authorities and editions were outside this bounded acquisition task; no designation is inherited.

Read `CLAUDE.md`, README, `docs/records.md`, schema, source-discovery skill and both bundled references, the round2 zinc handoff, and round60 resource assessment. Hidden/ignored-inclusive, symlink-followed deduplication inventoried 2,085 files in repo data/research/reviews/docs/.claude and the specifically cited round2-zinc, expansion-authorities, next-eu, round60-resource and current download directories. Exact roots, commands, successful exit codes and matching-file hashes are in the paired manifest. The DOI is an existing lead; no accepted zinc-leach-residue owner was found in that bounded science search. Binary contents were not exhaustively searched; no machine-wide absence is claimed. An initial mistyped local round2 path was corrected to the report-cited path before the successful inventory.

## Search and acquisition log

All checks occurred on 2026-10-13 UTC. Exact 22 queries, tool-output extracts and HTTP receipts are retained in the manifest or its externally hashed files. Default first result sets only, with no exhaustive pagination. Queries covered DOI/title, exact thesis filename/NNT, institutional mirrors, supplement identifiers and correction/erratum/retraction plus abiotic/acid counterevidence. No affecting notice emerged within those bounds.

| Route | Actual result | Acquisition scope |
|---|---|---|
| HAL article DOI search | HTTP 200; `hal-01393462v1`, `openAccess_bool:false`, no file fields | Bibliographic metadata, not a deposited original |
| HAL thesis all-fields search | HTTP 200; exact filename and version resolved | Metadata only |
| Exact thesis file | HTTP 200, 12,532 bytes of HTML with anti-bot title | Not a PDF; no pages inspected |
| theses.fr NNT catalog | HTTP 200; title, author, defense date and DOI match | Catalog metadata |
| theses.fr document route | Redirected to challenged HAL, HTTP 200 HTML | No thesis original |
| Crossref DOI deposit | HTTP 200; publisher article links and terms | Metadata, not a correction clearance |
| Wiley TDM endpoint linked by Crossref | HTTP 400, client token required | No article, no credential attempt |
| LUT institutional author publication links | Article link 403; companion link timeout; another 403 | Institutional leads, no original acquired |
| ResearchGate main author deposit | Indexed text and captions readable through web tool | Selective textual recheck, no original page-layout claim |
| Newly located author Appendix S1 deposit | Indexed supplement methods/equations/captions readable | Original PDF and all figure pixels unverified |
| Author and publisher Appendix PDF | Both HTTP 403 | Failed payloads retained and hashed |
| Main Figure1 image and displayed direct-download link | HTTP 403 locally | No image inspection claimed |

Some web-tool relative links incorrectly acquired an extra `/publication/` or `/figure/` prefix and returned 404. Canonical author-deposit paths were then followed explicitly; successful indexed text and failed PDF requests are distinguished. No repeated anti-bot bypass or unofficial archive was used.

## Candidate inventory and evidence limits

| Candidate | Identifier/version | Role and decision |
|---|---|---|
| Sethurajan et al. article | [DOI 10.1002/jctb.5026](https://doi.org/10.1002/jctb.5026), 2017 issue 92(3):512–521; 2016 accepted/online dates | Existing primary mechanism lead; defer pending originals |
| Same-study supplement | [Author Appendix S1 deposit 303382457](https://www.researchgate.net/publication/303382457_jctb5026-sup-0001-AppendixS1), uploaded 20 May 2016 | Newly resolved artifact, not independent replication; partial access |
| Sethurajan thesis | [HAL tel-01407248v1](https://theses.hal.science/tel-01407248v1), NNT 2015PESC1202 | Phase-evidence dependency; metadata resolved, contents still unavailable |

### Main article

The rechecked text retains the preliminary loading conflict: methods 5 g/L versus Figure 1 caption 50 g/L. Another caption conflict is now explicit: Figure 6 sulfur 2.51 g/L versus Figure 4/prose 25.1 g/L. These cannot be silently normalized. Chemical and biogenic sulfuric-acid leaching are reported statistically indistinguishable; the unavailable ANOVA data and original plots limit independent assessment. The source separates acidophile leaching, chemical iron removal and later biogenic-sulfide treatment. Its phase statement refers to thesis reference 37; neither an isolated pure-product yield nor industrial deployment can be accepted from these extracts. These are source questions, not corrections to an accepted record.

### Appendix S1

The newly resolved author deposit identifies Figures S1–S4 and describes equilibrium modeling separately from experiments. Original graphics remain missing. Its indexed S3.2 polynomial evaluated at the displayed stationary coordinates yields approximately 58.054%; its positive pulp-density quadratic coefficient prevents an unconstrained interior maximum. The main text also describes a saddle. This calculation is a qualified diagnostic from indexed text, not a replacement assay result or proof of an author error: original equation, design bounds, time basis and experimental follow-up must be compared. Calculation terms and provenance are externally retained in `polynomial-check.json` and embedded in the manifest.

### Thesis and date identity

[HAL's public metadata](https://api.archives-ouvertes.fr/search/?q=halId_s:tel-01407248&fl=*&wt=json) and the [thesis catalog](https://theses.fr/2015PESC1202) agree on the author/title and defense 11 December 2015. HAL submission 1 December 2016, release 5 December 2016, metadata modification 4 July 2026, and DOI 10.70675/2ba77414z25b8z4514z9279z858597fc0448 do not establish a new experiment or revised thesis edition. The exact linked file is [TH2015PESC1202_diffusion.pdf](https://theses.hal.science/tel-01407248v1/file/TH2015PESC1202_diffusion.pdf); its acquired bytes are a challenge page. No phase spectrum, page number or thesis experiment has been verified here.

## Priorities and curation handoff

1. Acquire the complete article and the now-exact PDF Appendix S1 through legitimate institutional or author access. Inspect original axes, captions, equation and all four supplementary figures; reconcile the two factor-of-ten condition conflicts without guessing.
2. Acquire the exact thesis file and locate reference 37's XRD/phase analysis. Establish whether the analyzed precipitate belongs to the same biological sequence or a separate chemical experiment.
3. Only then reconsider `cmmmech:zinc-leach-residue`, `material_kind: secondary_resource`, with source-linked `bioleaching` and separately scoped `recovery` entries. Preserve chemical controls, modeling limits and resource origin. Do not map percentages into the current mg/kg observation contract or invent species/strain identifiers. No schema change is demonstrated.

Decision: **defer new record; retain issue 186 open**. Metadata and access routes improved; the original-source prerequisites remain unmet. No external message or issue mutation was made by this agent.

## Reuse and verification limits

Publisher terms and author-deposit copyright notices do not establish an open redistribution license. HAL metadata cites its deposit authorization; no blanket reuse permission is inferred. Raw metadata, failed payloads and tool-rendered extracts remain under `/private/tmp/cmm-round61-zinc-research`, outside Git. The manifest pins actual URLs, UTC acquisition times, statuses, byte counts and SHA-256 values. Tool extracts are not represented as downloaded original PDFs. JSON parsing and retained-file hash checks were performed; no record validation or independent record review is claimed for this source-only assessment. Broader zinc literature and the source frontier are not exhausted.
