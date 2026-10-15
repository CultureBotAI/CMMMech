Resolved OP1 before runtime. The finalizer now binds the peer PR, posted COMMENT, queue and producer input hashes to the current receipts, requires the five named workflow roles, and reconciles their commit/event/branch/attempt/job identities with retained actual and closing API responses. Missing raw `run_attempt` is accepted only with the exact attempt-pinned endpoint; explicit null is rejected.

Independent review executed 19 actual AST-extracted fixture cases against finalizer SHA-256 `588ade004e53594085f5013fb55b4f5727cbe0374e74f598f88dc9173c733a00`; all passed. The original observation, corrected helper, exact diff, fixture source/results and successor disposition are retained under `reviews/publication/20261015-round93/finalizer-evidence/`.

This closes the consumer-contract defect. Actual merge, hosted checks, cleanup, fresh-main validation, synchronization and durable report creation remain separate later runtime gates and are not claimed by this static/fixture review.
