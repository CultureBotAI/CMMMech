---
name: cmmmech-discover-sources
description: Investigate and discover data sources for critical minerals and materials (CMMs) in CMMMech, including dated criticality lists, material identities, microbial extraction/transformation/recovery studies, and reusable datasets. Use for source searches, coverage gaps, or reassessing known sources; produces a documented assessment and curation handoff, not automatic record imports.
---

# Discover CMM data sources

Find sources that can support specific CMMMech claims and explain their usable
scope, access, provenance, limitations, and next curation step. A discovered
website, a verified dataset, and evidence for a microbial mechanism are different
outcomes. Prefer a useful, defensible shortlist to an unexamined URL collection.

## Orient and scope

Work against a verified CMMMech checkout. Paths in this workflow are relative to
that repository root; bundled `references/` paths are relative to this skill,
even when installed through a symlink. Read applicable instructions, README.md,
`docs/records.md`, `src/cmmmech/schema/cmmmech.yaml`, git status, and relevant
records and research reports. Do not infer integration capabilities from a skill.

Before claiming a source is new or absent, search the relevant existing records,
source references, reports, and local downloads with `rg --no-ignore --hidden`
(or an equivalent complete inventory). Include ignored files and resolve relevant
symlinks; report exclusions or inaccessible paths. Deduplicate by normalized DOI,
accession, dataset/version, and original publication, not only URL or title.
A publisher page, PMC mirror, supplement and associated dataset are related
artifacts, not four independent experiments.
For local downloads, start with paths cited by existing reports and the task's
download directory; expand only when needed. State that boundary rather than
scanning unrelated home/temp trees or claiming machine-wide absence.

Use the user's materials, mechanisms, jurisdictions, date range and desired
source type. If unspecified, start a bounded survey across source roles and
record the chosen coverage. Do not require criticality-list membership before
investigating a material. Keep element, ion, mineral species/group, commodity,
alloy and secondary resource distinct; do not force every form into a schema
root kind. A host mineral, target element and waste feed may need separate
identities and explicitly scoped relationships.

## Search and acquire

Use live web/repository searches for each investigation. Read the relevant
routes and query examples in [the source guide](references/source-guide.md).
Select routes that answer the question; do not mechanically search every portal.

Combine material names, symbols and verified synonyms with mechanism, organism,
substrate and dataset terms. Use reviews and indexes for discovery, then trace
claims to official authority documents, original experiments and deposited data.
Follow promising references or citing work when it can close an evidence gap
within the requested scope. Include relevant null results, contradictions,
corrections and retractions in the search. Log exact queries,
providers, dates, filters and pagination/coverage limits so a later search can
extend this one. Do not describe a bounded search as exhaustive.

Open the actual primary source and inspect methods, tables/figures, supplements,
metadata and representative data as relevant to the proposed use. Resolve DOI or
accession and confirm title, authors/owner, version and material/organism scope.
For a downloadable dataset, inspect its data dictionary and a relevant sample;
report observed size separately from any advertised total. Identify stable keys,
units, missingness, joins, download/API availability and update/version policy.

Record acquisition failures explicitly. A snippet, abstract or metadata record
can establish a lead but cannot verify unavailable methods or measurements.
Check downloaded file type/content: a successful HTTP response may contain a
challenge/login page instead of the promised workbook or archive. Use a legitimate
publisher/repository mirror when available, then move on after bounded retries;
retain the exact URL and missing evidence needed to resume. If files are retained,
record origin, acquisition time, version and checksum. Avoid committing bulk raw
files or copyrighted full text; distinguish reading access from redistribution
rights and record the source's actual license/terms, or `unknown`.
For a previously acquired file, distinguish its known original provenance from
this investigation's recheck date and checksum; do not claim a fresh download.

## Assess claims and fitness

Assign a source role before judging it: criticality authority, material identity,
resource/commodity context, primary mechanism experiment, organism/sequence
context, or dataset containing experimental observations. Sources can have more
than one role, with separate claim-level limits.

- **Criticality:** verify jurisdiction, issuing authority, exact list name,
  edition/effective date and original versus amended/consolidated version.
  Explain grouped or commodity-scope mappings. A latest-list claim needs a
  current authority check; historical editions remain valid historical evidence.
  `not_listed` requires checking the complete relevant list and its grouping.
- **Identity:** resolve identifiers and labels at the issuing source. An element
  identifier does not identify its ion, ore, alloy or waste. Species identifiers
  do not establish a strain's identity or a consortium member's causal role.
- **Mechanism:** locate organism/strain or community provenance, biomass state,
  substrate and pretreatment, medium, pH, temperature, duration, loading, controls,
  replication, analytical method and outcome. Record unavailable details as such.
  Keep units and denominators with values; distinguish measured/fitted estimates,
  solution depletion, mineral dissolution, precipitation, and isolated product
  recovery. Compare results only when substrates and assay bases are comparable.
- **Causality and scale:** separate observed activity from a proposed enzyme or
  gene mechanism. Genomes, environmental co-occurrence and resistance phenotypes
  alone do not demonstrate extraction or recovery. Dead biomass can support
  biosorption evidence without metabolism. Distinguish laboratory, pilot, field
  and industrial operation; require direct deployment evidence for scale claims.
- **Reuse:** assess provenance, coverage, identifier resolution, license, format,
  maintainership/versioning and acquisition effort. A public portal is not itself
  an open bulk dataset. Unclear reuse rights need resolution before redistribution.

Preserve contradictions and alternative explanations. Specify the exact claim
a source supports, partially supports, refutes, or merely contextualizes; do not
assign one confidence label to every claim in a paper. A useful official list or
sequence repository need not contain microbial assays to be worth retaining.

## Deliver the assessment

For an investigation, save a timestamped Markdown report under
`research/sources/<topic-slug>/<YYYYMMDDTHHMMSSZ>.md`, unless the user requests
another destination. Read the UTC clock and do not overwrite earlier reports.
Use [the report template](references/report-template.md), trimming inapplicable
fields with an explicit reason. This is a source assessment, not a curated record
or the separate per-record scientific review.

Include known-source changes, duplicates, useful candidates, rejected/deferred
leads, search/access limits and a ranked next-action list. Prioritize evidence
fitness and the user's coverage gaps, then reuse feasibility and effort; explain
ranking rather than inventing numerical confidence scores. For each promising
source, give a concrete handoff: claims it could support, exact evidence locators,
identity/version issues to resolve, and fields it can map to in the current
schema. Propose schema work only for a demonstrated gap, not as part of discovery.

Stop when the requested scope is covered or further progress depends on named
unavailable evidence; state what was and was not searched. End with actionable
candidates and unresolved questions, including a negative result when warranted.

Default writes are the local assessment and requested research artifacts. Do not
silently change records, implement importers, contact authors, publish issues or
PRs, or alter fleet/governance configuration. Follow the user's existing task
authorization if it explicitly includes those actions; this skill adds none.
If curation is also requested, use `docs/records.md` and the repository's
`.claude/skills/review-record/SKILL.md` for validation and independent timestamped
record reviews. A discovery report cannot substitute for that acceptance review.
