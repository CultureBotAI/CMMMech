Resolved the posting-consumer gap. The helper now binds the fixed COMMENT path and SHA-256 to the accepted peer `comment_draft` before request creation, rejects a symlink, and rechecks the hash and captured text before POST. Its resulting receipt preserves that binding.

Independent review preserved OP1 and explicitly resolved it. Six actual isolated guard checks passed: valid bytes accepted; wrong path, wrong hash, intervening file change, captured-text mismatch and symlink rejected. Evidence and corrected helper are retained under `reviews/publication/20261015-round93/comment-binding-evidence/`.

No scientific record or governed artifact changed for this fix. This disposition establishes the corrected consumer contract; the actual PR COMMENT and its runtime receipt remain later publication checks, not claimed here.
