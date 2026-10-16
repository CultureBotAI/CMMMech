# Initial review: borate source-file locators

UTC: 2026-10-16T03:53:51.730125Z

Reviewer: codex /root/round104_ree (GPT-6); different agent from the dossier curator. Base `0482e7b0af9b18685dabe310dbe86487b6ac4226`, working-tree changes.

Reviewed: `research/sources/round110-borates/20261016T034830Z-source-investigation.json` SHA256 `96e25850ced5d65943a08fb63cb7e013666e6edb01ee63e165f587efc4faf7fd`. Exact original retained at `/private/tmp/cmm-round110-ree-research/borate-dossier-initial.json`.

Scope: source-file provenance only. The separately assessed owners remain unchanged; their native scientific observations await terminal batch gates.

## Finding — minor

Stable key: `round110-borate-dossier-source-paths`. Two `primary_sources[].path` values contain added spaces and fail direct filesystem existence checks, independent of gitignore:

- `/private/tmp/cmm-round110-borates-research/ima 2026-09.pdf` should be `/private/tmp/cmm-round110-borates-research/ima2026-09.pdf`. Actual bytes match recorded SHA256 `2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973`.
- `/private/tmp/cmm-round110-borates-research/gowerite 2025-aam.pdf` should be `/private/tmp/cmm-round110-borates-research/gowerite2025-aam.pdf`. Actual bytes match recorded SHA256 `43d55b0c45aa68a9bac3811c476d56cac0d742bbd08035313f70ea661269e138`.

All other primary-source paths resolve and all six actual file hashes match the recorded values. Correct only the two locator strings; preserve source bytes, owner/history bytes and this finding. Recheck all source paths/sizes/hashes, then refresh native context capture.

No correction applied by reviewer. No owner scientific defect is asserted. Final gates and publication are pending.

Verdict: **needs_curation** for the dossier locators.
