# Publication wording review

- Review: 20261015T203020Z-separation-display-initial
- UTC timestamp: 2026-10-15T20:30:20.342006+00:00
- Revision: 1c2a3bb043c4bd267a3d911d0e77b029c742689e; uncommitted working changes.
- Reviewer: codex /root/round100_pentagonite (GPT-6).

## Scope

Bounded publication wording review; not a new independent scientific acceptance of reviewer-authored borax.

## Evidence checked

- `scripts/render_pages.py` — SHA256 `5f19c2ffb75edbd9be144b6d8b338a74e49467b4acd3b5d2a2bea7622bc8254d`.
- `pages/index.html` — SHA256 `75e0e21fd8cd234a9c4adf78b8111438774665ce50a1b7037d908e7b8c82022f`.
- `pages/processes/separation.html` — SHA256 `eef08148bbfd1c6cb72a0cbf01cf749bd3c1c3198364acf0900895d67a843bde`.
- `data/records/uranium-mine-tailings.yaml` — SHA256 `a217692da8148f706ce40260f18f1cd83d56b01e60eb3f3e21ba01c52535dfca`.
- `data/records/zinc-leach-residue.yaml` — SHA256 `ea520360db699961992304f933eb8dd4225eab72ceb02148941394aab846511d`.

## Findings by severity

- minor: `CMMMech:publication:separation-microbial-scope`. Maintained PROCESS_NAMES/PROCESS_BLURBS label every separation as Bioseparation using microbial biomolecules. The generated homepage and category reproduce this while this batch includes explicitly microbial:false commercial-resin sorption and acid separation. The label/prose overstate biological involvement.

## Corrections

Use neutral Separation and prose covering selective partitioning with involvement specified per record, regenerate pages and run affected render tests/freshness. Preserve scientific owners and counting logic. No correction performed by this reviewer.

## Unresolved questions

No scientific owner correction is required by this presentation finding.

## Verdict

Needs curation of the presentation wording. This is not a claim that the scientific owners are incorrect.
