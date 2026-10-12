# Zirconolite validation provenance correction

UTC: 2026-10-12T11:53:10.029181Z

Source-dossier validation provenance correction only; no record, history or scientific change.

The initial dossier validation.command string was reconstructed incorrectly as uv run python scripts/validate_records.py data/records/zirconolite.yaml. That script does not exist in the current repository; do not treat this string as an executed command. Its original validation output remains retained, but it does not establish that incorrect command.

Executed a fresh named CLI validation and recorded its exact argv, working directory, actual timestamps, terminal status and raw log hash. This receipt supersedes the initial dossier command provenance without editing the original dossier.

Actual command: `uv run --locked cmmmech validate data/records/zirconolite.yaml`; working directory `/private/tmp/CMMMech-expansion-round56-20261012`; exit0, checked1record,0failed. Log: `/private/tmp/cmm-round56-zirconolite-research/named-validation-recheck.log`, SHA256 `6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e`.

The original dossier pair remains immutable. Record/history hashes remain unchanged. Independent review must include this correction and the original dossier; no record EDIT was manufactured. Exact receipts and before-context hash are in the paired JSON.
