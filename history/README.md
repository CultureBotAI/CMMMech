# Curation history

This directory stores append-only canonical `HistoryRecord` sidecars. Use
`just new-history` and follow [the record guide](../docs/records.md#append-only-curation-history).
Do not hand-write session filenames or edit committed sessions. A correction
belongs in a new session that identifies the earlier one in its details.

The CMMMech adapter requires actual actor metadata, uses the current UTC time,
validates against the vendored schema, and creates a complete file without
overwriting any existing session. Its printed path is a reference for a
separate reviewed addition to a record's `history_refs`; generation alone
does not attach the sidecar or modify the record.

Initial adoption events describe the present migration. Earlier timestamped
scientific reviews remain evidence of those earlier reviews, with their own
record hashes and limitations. These new history events do not reconstruct
unknown authorship or claim new scientific verification.
