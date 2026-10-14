# Artinite correction following independent review

UTC: 2026-10-14T14:09:01.647084+00:00

Issue [236](https://github.com/CultureBotAI/CMMMech/issues/236), stable finding `CMMMech.artinite.daily-shaking-duration`. Initial observation `reviews/structured/20261014T140422Z-artinite-round73-initial/review.yaml` (SHA256 `12ea998cf2dfcba703afb6b905486fdabeb906ee30b0e026ab61e0fbf6f77fd6`) and original source dossier are preserved unchanged.

Both contexts now distinguish initial one-minute shaking before storage from subsequent daily workday shaking whose duration was not reported. Primary Lothenbach2026 p176 sections2.2/2.3. No phase, temperature, biological scope or outcome changed.

Canonical EDIT `history/records/artinite/2026-10-14T140827Z-codex-dbfd84.yaml` and inline EDIT retain the actual correction time. The initial CREATE remains attached. Lansfordite is unchanged. This correction note is not an independent acceptance review.

Named validation passed: `uv run --locked cmmmech validate --require-records data/records/artinite.yaml data/records/lansfordite.yaml`; `Checked 2 record(s); 0 failed.`. Log `/private/tmp/cmm-round73-carbonates-research/corrected-named-validation.log` SHA256 `4022ad8ba440a72bf4f1c8b321e447df36133d812f52f21611becf103551b042`. Start time was not separately recorded; completion was observed before this note.

## Frozen corrected inputs

- `data/records/artinite.yaml`: `54de7013ba0cef8aa1976fa8bb5e9ddcbc7979bff33c6db137e20d02223235c4`
- `data/records/lansfordite.yaml`: `0a98ebec9f1fb285661945880c01eab366c38440659f02ca0ae284f42c1ee80f`
- `history/records/artinite/2026-10-14T135947Z-codex-a1da31.yaml`: `b532a5a513ae03f4be3e5b0b4e094de0dbc28910997b353156035a19de3d34de`
- `history/records/artinite/2026-10-14T140827Z-codex-dbfd84.yaml`: `1015c069a28e772c0d78d5058cab880ce5aed5b67ff5d5890ab3bff2ca27b978`
- `history/records/lansfordite/2026-10-14T135948Z-codex-fa83c2.yaml`: `116dd6f3802dc42a8b7f64da74fe33e401a319864f9133daba7392d3fce03eee`
