# Round96 publication runtime static review

Recorded 2026-10-15T14:18:47.999593Z. Complete five-helper/config source read, AST parsing only; no helper execution or external mutation. Verdict: **needs curation**.

- **C1 (major):** commit receipt checks are not bound to current owner/review/coverage bytes and identities. A post-gate edit can be committed under stale passing evidence. Require explicit actual receipt schemas and current input/census bindings before staging.
- **C2 (minor):** commit output-path collision is checked after Git mutation. Reject existing/symlink receipt before staging, then create the final receipt exclusively.

The cleanup, sync, queue and hosted-five identity/scope guards were read completely; no additional supported corrective finding. Sync preserves all7,493 baseline nontracked entries, including ignored/hidden files and symlink identity. Hosted-five is read-only and distinguishes pending runs. Its executor metadata currently identifies root.

Exact source snapshots, paths/lines, hashes, positive guard checks, runtime prerequisites and acceptance criteria are in the companion JSON. Neither finding alleges an actual changed scientific record or a failed publication action.
