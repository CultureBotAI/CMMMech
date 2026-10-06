# CMMMech

An evidence-backed knowledge base for **critical minerals and materials**, with
**microbial extraction, transformation, and recovery mechanisms** alongside
their wider resource and material context.

The initial release provides a LinkML schema, an offline strict validator,
tests, CI, and a read-only issue-review skill. The curated corpus is deliberately
empty. Synthetic test fixtures are not mineral records or scientific evidence.

## Scope

- Distinguish elements, mineral species, mineral groups, commodities, and
  secondary resources rather than treating those as synonyms.
- Record criticality by jurisdiction, list name, and edition, with a source.
  There is no universal or timeless `is_critical` flag.
- Represent mechanisms such as bioleaching, biosorption, biomineralization,
  redox transformation, separation, recovery, and recycling.
- Mark microbial involvement explicitly; connect identified organisms and
  experimental context to evidence for the particular mechanism.
- Preserve uncertainty and evidence that supports, partially supports, or
  contradicts a mechanism. Validation is not scientific verification.

## Local Checks

```bash
uv sync --extra dev --locked
just check
uv run cmmmech validate
uv run cmmmech validate path/to/record.yaml
uv run cmmmech validate --require-records
```

Without `just`, use `uv run python scripts/check.py`. The same command is used
by CI. No research provider, model, credential, or network lookup is used by
the checks after dependencies are installed.

Each future record belongs in `data/records/<slug>.yaml`. See
[the record guide](docs/records.md) and the packaged
[LinkML schema](src/cmmmech/schema/cmmmech.yaml). Validation rejects unknown
fields, duplicate YAML keys, malformed references, dangling source references,
and duplicate record identifiers. An empty corpus is reported explicitly;
`--require-records` makes it an error.

## Sources

Criticality is a designation made by a named authority at a particular time.
Useful discovery sources include the [USGS critical-minerals programme](https://www.usgs.gov/programs/mineral-resources-program/science/about-2025-list-critical-minerals)
and the [EU critical raw materials overview](https://www.consilium.europa.eu/en/policies/the-critical-raw-materials-act/).
These are entry points, not imported datasets or an endorsement of a frozen list.
Curate microbial mechanisms from the underlying research, preserving organism,
substrate, conditions, and the distinction between laboratory results and field
or industrial deployment.

## Integration Status

CLAW fleet registration, canonical shared/history schemas and adapters,
vendored governance, PR shepherd, and native merge-queue configuration are
**pending**. Nothing in this bootstrap claims those are deployed. Admission
requires a separate CLAW change and coordinated governing release; do not invent
a vendored pin or silently copy a different Mech's capabilities.

The included CI handles pull requests, pushes to `main`, and `merge_group`
events, but a workflow alone does not enable a remote merge queue.

## License

Project-authored code and schemas use BSD-3-Clause. Project-authored data and
narrative documentation use CC-BY-4.0. Third-party materials retain their own
terms. See [LICENSE](LICENSE), [LICENSE-CODE](LICENSE-CODE), and
[LICENSE-DATA](LICENSE-DATA).
