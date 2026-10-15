Follow-up A1 (`round87-final-auditor-native-status-scope`) arose during the final local package audit. The first auditor stopped before producing acceptance because its whole-module `dismissed` text check matched the valid GitHub message “non-dismissed change-request review.” Both native finding predicates already used the correct `resolved`/`rejected` dispositions. This was an auditor false positive, not a record or scientific-evidence defect.

The successor now inspects only the AST of `verify_native_lineage` and requires both actual native finding-status predicates to use `resolved`/`rejected`. The original auditor, failed exit-1 receipt/log, scoped diff, six focused author cases, and ten independently executed cases are preserved. An independent successor explicitly resolves A1 and discloses that the earlier static pass missed this guard. The earlier HP1 initial/expanded/successor and 25 cases remain unchanged.

Publication artifacts (these main-branch links become available when the forthcoming PR merges):

- [Initial A1 observation](https://github.com/CultureBotAI/CMMMech/blob/main/reviews/publication/20261015-round87/cmm-round87-auditor-scope-initial-20261015T041052Z.json)
- [Original auditor](https://github.com/CultureBotAI/CMMMech/blob/main/reviews/publication/20261015-round87/20261015T041052Z-final-package-audit-initial.py)
- [Failed execution receipt](https://github.com/CultureBotAI/CMMMech/blob/main/reviews/publication/20261015-round87/cmm-round87-final-auditor-failed-execution.json)
- [Scoped current auditor](https://github.com/CultureBotAI/CMMMech/blob/main/reviews/publication/20261015-round87/cmm-round87-final-package-audit.py)
- [Exact correction diff](https://github.com/CultureBotAI/CMMMech/blob/main/reviews/publication/20261015-round87/cmm-round87-final-auditor-scope-bound.diff)
- [Six focused cases](https://github.com/CultureBotAI/CMMMech/blob/main/reviews/publication/20261015-round87/cmm-round87-final-auditor-scope-fixtures-bound.json)
- [Ten independent cases](https://github.com/CultureBotAI/CMMMech/blob/main/reviews/publication/20261015-round87/cmm-round87-auditor-scope-independent-fixtures-20261015T041232Z.json)
- [Independent A1 successor](https://github.com/CultureBotAI/CMMMech/blob/main/reviews/publication/20261015-round87/cmm-round87-auditor-scope-peer-20261015T041310Z.json)

Corrected auditor SHA256: `7c7cf885302b87b3b70743aa90edd88dd83fbd836a8f198e49307c72b02e9ce3`; independent successor SHA256: `4b343f4bb00b6db7cc3588bde337baf1d4d97793edfbeb518c4e9ed6af2eb5cb`. No owner, canonical history or native scientific review changed, and their completed gates remain applicable. Final package runtime acceptance is still pending; this comment records the narrowly resolved tooling finding, not a completed publication.
