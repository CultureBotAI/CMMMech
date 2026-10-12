# Round45 Ge minerals: corrected source handoff

UTC: 2026-10-12T04:06:30.673068Z. Curator: Codex (GPT-6; codex), agent `/root/round43_hardmetal`.

This successor corrects the Handbook reference locator after independent [finding F1](../../../reviews/structured/20261012T040400Z-argyrodite-round45-initial/review.md) and [issue #146](https://github.com/CultureBotAI/CMMMech/issues/146). The initial [Markdown](20261012T040254Z-source-investigation.md) and [JSON](20261012T040254Z-source-investigation.json) are preserved; their hashes are pinned in this successor JSON. All original acquisition, deduplication, primary inspection and source-access limitations remain applicable.

The one-page Handbook's **reference 3**, Eulenberger (1977), explicitly concerns synthetic Ag8GeS6. Reference 2 is Berry and Thompson (1962). The original record title and source-assessment JSON used the wrong reference number. The scientific distinction between synthetic structural material and the natural Ezuri specimen remains unchanged.

The argyrodite record now uses reference 3, with an actual EDIT sidecar linked to issue 146 and an inline correction event. The original CREATE sidecar and initial independent review remain intact. The initial JSON's historical wrong locator is superseded by the corrected `handbooks.inspection` entry here; it is not treated as current evidence. Briartite is unchanged.

Named validation `uv run --locked cmmmech validate data/records/argyrodite.yaml` completed terminal 0: **1 record; 0 failed**. This is a curator correction, not an independent acceptance. The parent coordinates the independent successor disposition and final-v2 batch gates.

## Frozen current targets

- `data/records/argyrodite.yaml` SHA256 `7944de7d27f422ff2778c454e466b0c6397367b1af4efcfb7a3a227e886d7190`
  - `history/records/argyrodite/2026-10-12T035954Z-codex-d6c8f5.yaml` SHA256 `e597e55fd185cb2075c934f24e211bcaebfe733186d92ae31fbf94fa77a348c8`
  - `history/records/argyrodite/2026-10-12T040537Z-codex-a2857d.yaml` SHA256 `b6a3dcd9ff7321df96d5fe3337849349ae6a7003e45a5310216754fb0338e929`
- `data/records/briartite.yaml` SHA256 `78d179ae37d35050510f0083df0936bee843ff76eab448bef817c12198ed6d51`
  - `history/records/briartite/2026-10-12T035949Z-codex-155fbb.yaml` SHA256 `b0d50607144b2f7d1481dc058f201366fd30145bec65d0525249af214d5e532c`

The paired JSON repeats the source acquisition and bounded search provenance, preserves initial targets separately, and records current targets plus the exact issue and predecessor finding.
