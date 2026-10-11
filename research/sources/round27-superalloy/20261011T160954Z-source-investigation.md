# CMM source investigation: superalloy residue follow-up

## Scope and provenance

- UTC: 2026-10-11T16:09:54.669745+00:00. Researcher: Codex (GPT-6; round27_superalloy).
- Base `3f1350b24b4f6248ed2e17caade936c15af9be93`; branch `curate/cmm-expansion-round27-20261011`. Source-only work; no record or canonical history created.
- Follow-up to [round26 assessment](../../ingests/round26-superalloy-sources-20261011.md). The material is an industrial mixed residue, distinct from elemental nickel/cobalt and from a certified alloy grade. No criticality or industrial deployment claim is proposed.
- `rg --no-ignore --hidden --follow` included records, research, reviews and history in this worktree; original-checkout records/research/reviews; and referenced round25 button/frontier/blast-furnace-dust and round26 superalloy raw directories. DOI and stock codes 30167/30168/32083 matched research leads, not a curated resource root. Exact command/output are in `/private/tmp/cmm-round27-superalloy-raw/dedup-receipt.json` and `dedup.txt`. Unrelated home/temp trees excluded; no machine-wide absence claim.

## Search and acquisition log

The paired JSON records every exact query (first returned results, no pagination). On 2026-10-11 the MDPI web landing page returned 429 and the Coventry final-version link failed through the web provider. Local requests initially failed sandbox DNS; one network-enabled batch distinguished network limits from source responses:

| Source route | Result | Evidence gained |
|---|---|---|
| [Coventry final PDF](https://pureportal.coventry.ac.uk/files/116283497/Constantin2025VoR.pdf) |403 | No original pages |
| [Publisher XML](https://www.mdpi.com/2227-9717/13/7/2157/xml) |403 | No complete XML |
| Public MDPI figure-asset candidate, full URL in JSON |404 | No figure pixels; guessed asset is not evidence of image absence |
| [Crossref DOI metadata](https://api.crossref.org/works/10.3390/pr13072157) |200, 15905 bytes | Fresh metadata identical in SHA256 to round26 |
| [Coventry institutional record](https://pureportal.coventry.ac.uk/en/publications/strategies-for-nickel-and-cobalt-mobilisation-from-ni-based-super/) |Readable |21-page VoR advertised; bibliography and CC BY 4.0 notice |

No challenge/login bypass was attempted. Previously failed ResearchGate/CDN PDF routes were not cycled again. Indexed publisher text remains partial, and no quantitative mechanism claim is accepted from it.

## Candidate inventory

| Candidate | Identifier | Role/access | Decision |
|---|---|---|---|
| Constantin, Hall, Pourhossein & Farnaud 2025, Strategies for Nickel and Cobalt Mobilisation from Ni-Based Superalloy Residue Powders Using a Sustainable and Cost-Effective Bioleaching Method | [10.3390/pr13072157](https://doi.org/10.3390/pr13072157) |Primary experiment; fresh metadata, incomplete original access |Defer mechanism curation |
| Fečko & Kučerová 1996, Bacterial leaching of waste materials at the Tatra joint stock company, Kopřivnice | [Publisher index](https://www.geology.sk/mineralia-slovaca-5-1996/), Mineralia Slovaca 5/1996, p. 388 |Primary-study lead via publisher search index; page timed out |Pursue full paper only |
| Ogi et al. 2016, Selective Biosorption and Recovery of Tungsten from an Urban Mine and Feasibility Evaluation | [10.1021/acs.iecr.5b04843](https://doi.org/10.1021/acs.iecr.5b04843) |Existing round6 deferred lead; ACS 403 |Duplicate discovery lead; no new acceptance |

The Tatra title/material terms produced no matching entry in the hidden/ignored-inclusive named corpus/research boundaries; this establishes a new lead within these boundaries, not a newly published experiment. The tungsten-carbide lead was already documented in `research/ingests/round6-mo-w-20261011.md`.

## Source assessments

Crossref and Coventry agree on authors, journal Processes 13(7), article 2157, publication 7 July 2025 and version-of-record CC BY 4.0. Crossref deposit 9 October 2025 and index 18 August 2026 are metadata-maintenance dates. Fresh Crossref SHA256 is `3fdbdb41b910c3d98d85051230ed0a17aff37915bb73f3b730782ceba7e7c992`, identical to prior receipt; empty relations and absent update-to do not prove universal absence of corrections.

The round26 handoff records cell-free culture filtrates from A. thiooxidans or an unresolved consortium, unequal starting acidity among lixiviants, and an aqua-regia feed denominator acknowledged to be incompletely digested. It also flags SAR-Re cobalt 65.30 g/kg versus a discussion conversion implying a different inventory. These are **prior partial-primary assessments**, not fresh full-paper verification in this round. Original figure/control/normalization inspection is still required. No strain identifier, assay endpoint, total-feed yield, isolated product, industrial scale, sustainability or cost advantage is accepted here.

The exact DOI/title correction queries found no relevant notice in their first result sets; publisher version/supplement inventory remains unavailable. No raw experimental dataset was inspected. CC BY 4.0 is verified for the article, but acquisition completeness is independent of reuse permission. All raw receipts stay outside Git; the JSON records paths, times, bytes and checksums. A successful metadata download is not acquisition of the experiment.

## Priorities and handoff

1. Resume superalloy curation when an accessible original VoR plus figures/tables is available. Avoid repeating identical forbidden routes without a changed access route.
2. Verify matched chemistry controls, all Table1/2 and figure denominators, sample origins, replicate/sample compensation definitions and the cobalt inconsistency; then map only supported context/evidence to a secondary-resource record.
3. Investigate the distinct Tatra grinding-sludge source through its original publisher archive; accept no method or measurement from index keywords. Broader industrial-goethite byproduct curation is being pursued separately by the parent task.

## Limits and unresolved questions

Full original superalloy evidence remains unavailable after bounded follow-up; this does not establish scientific falsehood or source exhaustion. No new material record/history was authored. JSON parsing, receipt hashes and Markdown relative-link resolution were checked for this source report. Parent baseline and batch gates are separate; no scientific acceptance review is claimed for this research-only deferral.
