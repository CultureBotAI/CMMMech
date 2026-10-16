# Round 108 receipt-consumer review

2026-10-16T01:51:17.268493Z

Verdict: **needs curation**. Two minor guard defects; no maintained scientific-record defect was assessed.

Independent static and inert assertion audit of two temporary receipt consumers; no consumer body, Git, GitHub or maintained owner mutation executed.

The exact source hashes and ten inert probes are retained in the paired JSON. Every invalid fixture was accepted by the relevant existing assertion block. No consumer body or write operation was executed.

## F1: Report consumer permits provisional counts and stale successful receipts

Stable key: `round108-report-receipt-bindings`. Severity: minor. Status: open.

Empty config counts make all(count comparisons) vacuous. The report consumer does not require finalized config or bind gates/review-check to configured base, required command set, current owner bytes and matching coverage. Five inert invalid receipt fixtures pass its entire initial assertion block. Downstream commit guards mitigate publication, but do not make the report consumer independently truthful.

Acceptance:

- Require finalized config and measured nonempty required count keys.
- Reuse the existing check_gate_receipts contract with a digest function rooted at W; bind expected worktree and coverage root.
- Compare current record hashes with the gate record_inputs and coverage rows before reporting exact final-byte coverage.
- Reject provisional config, wrong base, missing commands and stale hashes in inert negative tests; retain a complete positive fixture.

## F2: Positive uranium review builder does not bind the gate to the inspected owner

Stable key: `round108-uranium-review-gate-bindings`. Severity: minor. Status: open.

The positive branch checks completion, envelope exit, unchanged flag and log digest, but omits trusted base/worktree, all four unique successful required commands and record_inputs equality with the exact native-inspected owner. Five inert invalid gate fixtures pass that assertion. The native capture does bind owner/history bytes correctly; the gap is the separate validation claim.

Acceptance:

- Assert configured trusted base, exact worktree and current owner hash == capture target hash == gate record_inputs[owner].
- Require each of just check, strict nonempty validate, validate-history with trusted base and render_pages --check exactly once and exit zero.
- Reject wrong base/worktree, stale owner hash, missing/duplicate/failed commands with inert tests.
- Keep existing initial finding bundle immutable; successor must retain exact stable key and previous occurrence.

Report prose, seven owner paths, relative Markdown links, nine expected native artifacts, source issues 427-431 and corrective issues 432-434 match the planned prepublication scope. No hosted CI/merge is claimed. Uranium successor uses the initial exact review ID and F108-SKL-1, and the new native capture hashes all listed owner/context inputs; no lineage defect found. A new corrective issue will require updating the report issue set.

Corrected final gates and the final native checker remain pending. This audit does not claim report generation, hosted CI or publication success.
