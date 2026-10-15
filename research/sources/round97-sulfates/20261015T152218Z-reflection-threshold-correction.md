# Coquimbite reflection-threshold correction

Recorded 2026-10-15T15:22:18Z by codex (GPT-6; codex), the record author. This is a corrective source-assessment successor, not an independent acceptance review. Worktree `/private/tmp/CMMMech-expansion-round97-20261015`, base `9272005a590c9fa1e5fbb75b30f914ce38c3924a`.

## Lineage and correction

The original [source investigation](20261015T151307Z-source-investigation.md) and its [JSON](20261015T151307Z-source-investigation.json) are preserved unchanged. Their statements calling the printed/CIF reflection thresholds an unresolved reporting discrepancy are retracted. The same incorrect wording was removed from `sources[mauro2020_cif].title` in `data/records/coquimbite.yaml` after the independently saved [initial finding](../../../reviews/structured/20261015T151902Z-coquimbite-round97-threshold-initial/review.md) and [issue 353](https://github.com/CultureBotAI/CMMMech/issues/353). CREATE history remains unchanged; a new inline EDIT and canonical `history/records/coquimbite/2026-10-15T152112Z-codex-b92da9.yaml` document the correction.

The original owner snapshot SHA256 was `0065ed172cce35f5cb5c465fa171121b0f734caaaa0e0c4e4feacd6f80c1ab52`; corrected owner is `6af5c6bfe863f716aa767b8b6182d3a9d025b5033fb9d5bf62f5f7e56f8c3176`. Rozenite is unchanged.

## Checked evidence and precise locators

Mauro et al.2020 Table2 is on printed page278/PDF4; Table3 mixed-site occupancy is on printed page279/PDF5. The single-crystal refinement text begins on printed279/PDF5 and continues on280/PDF6. Table2 gives Fo > 4 sigma(Fo), while the publisher CIF `_reflns_threshold_expression` gives I > 2 sigma(I). The different symbols and multipliers are not, by themselves, evidence of contradictory inclusion rules.

The [IUCr CIF checking documentation](https://journals.iucr.org/services/cif/checking/autolist.html), REFLE01, pairs a typical multiplier2 for intensity/F-squared with4 for F. The [IUCr statistical-descriptors discussion](https://www.iucr.org/resources/commissions/crystallographic-nomenclature/statdes/if2f.html) supplies the conventional uncertainty relation. With I = F² and sigma(I) approximately 2F sigma(F), I > 2 sigma(I) corresponds conventionally to F > 4 sigma(F). This reasoning does not establish exact equality for every weak-reflection treatment, prove identical selected raw data, or constitute an independent re-refinement. The owner retains its same-study and no-re-refinement limits.

The direct urllib IUCr requests returned403 (receipt `acquisition-06-iucr.json`); browser-accessible primary documentation was inspected and its tool response retained as `iucr-web-response.json`. No access route failure is treated as source absence. The originalPDF/CIF hashes are unchanged and recorded in the paired JSON.

## Unchanged scope and follow-up

This correction does not alter the current Al-essential species formula, sample chemistry, mixed-site occupancy, history of IMA redefinition or the lack of microbial-mechanism claims. Original analytical versus structural composition distinctions remain. An independent reviewer also reported checking the Newsletter52 corrigendum: it changes Petrovite details, not coquimbite19-F; that inspection belongs to the reviewer and is not claimed as a new author inspection here.

Reviewer-supplied metadata resolves the two previously deferred IMA recent references as Abdulina et al.2025, DOI10.2138/am-2025-9776, and Meusburger et al.2023, DOI10.2138/am-2022-8502. These remain full-original follow-up leads, not imported experimental evidence. The broader source frontier remains open.

## Validation and next disposition

Affected strict validation completed with exit0: `Checked 2 record(s); 0 failed.` Log `/private/tmp/cmm-round97-sulfates-research/corrected-owner-validation.log`. This source correction is ready for independent successor review retaining the issue key `coquimbite-round97-equivalent-reflection-thresholds`; it does not itself resolve the saved finding. Parent full-batch checks and independent final disposition remain necessary.
