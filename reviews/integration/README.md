# History adapter review provenance

The following immutable review artifacts were copied from the earlier local
worktree `/private/tmp/CMMMech-claw-integration-20261007`:

- `20261008T021706Z-history-adversarial.md`: independent review identifying the
  ancestor-symlink defect tracked by CMMMech issue #8.
- `20261008T022040Z-history-recheck.md`: independent acceptance of that repair,
  with 97 tests against the documented isolated canonical-schema fixture.

They describe their original reviewed revisions and file states. That design
used `curation_history` for path references, before CMMMech PR #9 established
native inline `CurationEvent` objects. The current integration preserves PR #9's
inline events and moves canonical sidecar links to a separate `history_refs`
field. The old artifacts are evidence for the earlier implementation and its
repairs, not acceptance of the subsequently combined code or of the new field.
The combined implementation requires a fresh independent review and actual
repository checks against the already governed schemas.
