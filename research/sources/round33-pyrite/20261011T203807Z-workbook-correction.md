# Pyrite workbook correction

Actual UTC: 2026-10-11T20:38:07.705435+00:00. Issue [#115](https://github.com/CultureBotAI/CMMMech/issues/115); initial [review F1](../../../reviews/structured/20261011T203700Z-pyrite-round33-initial/review.md).

The original supplementary workbook of DOI 10.1038/s41396-021-01028-3 (SHA256 `13fffe1fbd15c28d57e911377df4117acd60c5df20fc31d9411e40a3f73ab3e0`) was independently decoded from its OOXML formulas and cached values by the reviewer and curator. Sheet `Figure 1 CH4 and Sulfide Values` labels E23 total methane in mmol and H24 Unamended, but H26 references G26*1000; H27 starts the shared G27*1000 formula through H32. G contains the adjacent pyrite standard deviations. H29 caches 225.334939 mmol, while Figure 1c shows a near-zero control curve.

The record now discloses this contradiction as context-only evidence. These cells are not accepted as control measurements or silently repaired. Separate natural-specimen Figure S3 and synthetic dialysis Table S3 remain separate supported observations. The earlier dossier and initial review retain their original hashes and accurately describe their earlier record state. The new EDIT sidecar and inline event document the correction; final successor review and corrected-state gates will follow.

No new source-data measurements, schema behavior or test behavior were introduced.
