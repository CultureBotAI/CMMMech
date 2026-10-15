# Homepage labels: independent successor

UTC: 2026-10-15T18:55:01.703774Z. Reviewer: codex `/root/round100_pentagonite` (GPT-6).

Predecessor: [initial finding](20261015T185056Z-homepage-labels-initial.md). Issue: [#368](https://github.com/CultureBotAI/CMMMech/issues/368). Key: `CMMMech:round100:homepage-mechanism-labels`.

**Pass; finding resolved.** The maintained and generated homepage now uses neutral mechanism/process labels and explicitly permits biological and abiotic evidence. Related wording names all six material kinds and qualifies identifier mappings as verified where available. No universal ChEBI/NCBI assertion remains in these two exact files.

The counters are correct and unchanged: 496 curated mechanisms and 405 materials with mechanisms. The counting script is byte-identical to the initial audit, and all 487 owner hashes match the successful batch-gate receipt. No scientific record or prior scientific review was edited.

## Checks and exact inputs

- Independent `uv run --locked python scripts/render_pages.py --check`: exit 0.
- Coordinator rendering and nine existing page tests: completed zero exits; receipt and log hashes independently verified.
- Template diff is limited to labels/prose; old affected phrases are absent in the two exact maintained/generated homepage paths.

- `reviews/publication/20261015-round100/20261015T185056Z-homepage-labels-initial.json` — SHA256 `bce6b3bbd0a0706bb482140d3c858cfa0d463b907c9408a07df88d981bb3b01e`
- `/private/tmp/cmm-round100-homepage-checks.json` — SHA256 `1168b0e686983f3f5423263630b6373aef61d4b8a1a905f72c98d4c0743df280`
- `/private/tmp/cmm-round100-homepage-checks.log` — SHA256 `b03faee0429fe562051be4241289115a0b31bddb57378caf3643b829bf68a169`
- `src/cmmmech/templates/index.html` — SHA256 `362c23f1d87fcced2671f819a86bec38abee784679d8ce7c2ef5632252acd5de`
- `scripts/render_pages.py` — SHA256 `f1aaa6c382b057a4e4f2702a24e2bebb974403703e4e3b055fffdda024797357`
- `pages/index.html` — SHA256 `896e71b4827dad1eba4f3f02d321a170b58edf0b55b3df135e001b5fa68c8f9a`
- `/private/tmp/cmm-round100-package-peer/homepage-render-check.log` — SHA256 `b798d21a609b296cdc2aeb317f68fc259c4e86ee43942b4a3c5008b32b9bfa5e`
- `/private/tmp/cmm-round100-homepage-review-issue.json` — SHA256 `273dfdcf6b07b492c403b0610ed8bb84edeb187a34301c7fee1aadd3323d3916`

## Limitations

- The full just check preceded this text-only template correction; affected renderer tests and independent generated-page check passed afterward. The exact publication commit must still receive normal CI.
- No scientific review, native review bundle or history sidecar changed.
- Final package/provenance review is a separate observation; no preflight, merge or issue closure is asserted by this audit.
