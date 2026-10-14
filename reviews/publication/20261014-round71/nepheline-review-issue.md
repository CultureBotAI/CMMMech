Independent adversarial review of the new nepheline record found a minor source-transcription error. In Andrew King's 1985 thesis, Figure 2.25 (printed page 130; PDF page 138) labels the second strain **CMI 234300**. The frozen record and round 71 silicate dossier transcribe this as **CMI 231300**. Higher-resolution inspection of the original figure independently confirmed 234300.

The source's Table 2.8 and section 2.3.4 instead say **CMI 243400**. That source conflict remains unresolved and must not be silently corrected into an authenticated strain identity. The accepted mechanism's CMI 31821 observation is unaffected.

Affected owners:

- `data/records/nepheline.yaml` (initial SHA256 `d5b71f26fb7ae031187185e427fc79ee1b56cdf5aa87fd6ae44f36dfb537cb20`)
- `research/sources/round71-silicates/20261014T122302Z-source-investigation.{md,json}`

Acceptance criteria:

1. Preserve the initial native finding against the original frozen bytes.
2. Correct the quoted legend to CMI 234300 in the maintained record and dossier; retain the unresolved 243400/234300 difference.
3. Append canonical EDIT history and a separate inline event; keep the original CREATE sidecar immutable.
4. Validate the corrected record and batch. Save an independent successor with the same issue key and exact predecessor occurrence, covering the final record including history references.
5. Link the resolution artifacts and checks here before closure.

Primary original: https://hdl.handle.net/10044/1/37745. Raw thesis and high-resolution render are retained outside Git. This issue tracks the curation error, not resolution of the historical source's strain identity.
