# Allanite-derived leachate: source assessment

Recorded 2026-10-12T10:01:50.800758+00:00; trusted base `b85c2c2c753fe83a2fc21f073ee1e49675ae647e`. [Provenance and arithmetic receipt](20261012T100150Z-source-investigation.json).

## Decision and material boundary

Create [allanite-leachate](../../../data/records/allanite-leachate.yaml), a secondary resource defined by chemical processing. The Halleck Creek feed was concentrated, acid-leached, stripped of impurities, precipitated as an REE cake and redissolved. It is distinct from geological ore and the existing WRE/Zappall allanite concentrate in Schmitz2025. No mine identity is transferred between studies; no generic allanite-species ID or constituent criticality is assigned.

This assessment addresses [source issue163](https://github.com/CultureBotAI/CMMMech/issues/163). Acceptance remains subject to independent final-byte scientific review and batch gates; this dossier does not claim publication or issue closure.

## Evidence actually checked

The original Lu2026 paper (DOI10.1038/s41467-026-68957-5), all11 publisher-linked supplements and Crossref metadata were acquired in round52 and their hashes rechecked here. Original acquisition times and exact source URLs are preserved, not presented as new downloads. The primary11-page PDF SHA256 is `6e452116325eb24021399bad565be7058c79cd866a744fcae5c374155274f3b1`. Original main pages3,4,5,6,8,9, SI pages5,7,12-19 were visually inspected. Scientific main text and SI strain methods were read; relevant peer-review replies were inspected selectively. All workbook sheets were inventoried/extracted. This is not an exhaustive visual audit of every economic-model appendix or a TEA rerun.

NCBI4909 resolves to Pichia kudriavzevii; the paper's Issatchenkia orientalis is a listed heterotypic synonym. Species taxonomy does not authenticate JL04. The paper is dated2026, with initial online publication January30 and version of record March4. The inspected Crossmark returned current; exact DOI notice searches did not return an affecting correction in their bounded result sets.

## Mechanism, controls and outcome

JL04 was engineered from SD108 to produce oxalate. Separate glucose-fed cultures used100mL bioreactors,30°C,pH4 and10%DO. Centrifugation at8000g for30min removed pellets before the REE stage. Real-liquor assays used22.00 and42.70g/L supernatants and a1M commercial-acid comparator at controlledpH1.5. The paper does not separately specify real-liquor precipitation time/temperature; synthetic salt overnight room-temperature conditions are not transferred. Methods state n=1 per real-liquor condition, while workbook dose points track sequential additions and1.5mL withdrawals.

Reported >99%TREE near a nominal2.7g/L dose means solution depletion. It is neither ore extraction nor an isolated-product mass yield. No matched uninoculated-medium or parental-supernatant real-liquor arm was identified in the main article/Data1; the matrix contribution is unresolved. A recovered precipitate is described, but single-Nd XRD/FTIR cannot establish mixed real-feed purity. Modeled127000ton/year production and environmental credits are not operation of a commercial plant.

## Workbook adversarial checks

Supplementary Data1 (`MOESM4`) has four sheets. The first contains feed ICP data, three reagent programs and volume additions. OAP-O begins100mL; OAP-A/B begin95mL. Analysis rows41-53 correct cumulative volumes and withdrawal; rows66-77 calculate recovery. SourceData (`MOESM11`) joins these curves in `Fig.3a and 3b` rows17-28 and34-45, and `Fig. S1 to S8` rows68-79. All1104 tested formula/plot relationships reproduce cached values. This verifies arithmetic/joins, not instrument accuracy or process mass closure.

- Row74 TREE removal is99.674% (commercial),99.745% (A),99.576% (B), at source-nominal doses2.7009,2.6901,2.772g/L. Dosage uses100mL even for95mL starting biological arms. No silent denominator correction is substituted.
- Feed Th/U cells are15.36/30.39ppm. High-dose zeros produce apparent100% removal without per-cell censoring limits; possible co-retention contradicts an unqualified pure-product inference. It does not establish solid phases or true absence.
- Negative apparent removals remain present, including first-A TREE−19.09% and strong negative Mg values. Missing cells are not zeros. The record retains these as source limitations.
- Biological-A row74 Mn is6.8856%, also SourceDataFig3bG42, contradicting the blanket text claim of less than6% for Ca/Mg/Mn/Zn.
- Commercial raw126g/L is oxalic-acid dihydrate and is converted using126.07/90.03; this is not treated as an unexplained concentration discrepancy.
- TREE is the source's16-element set; its LREE includesSc. No universal grouping or undefined pooled denominator is asserted.
- Fig.2F11-F12 show38.78 and40.27g/L at10days (reported mean39.53), distinct from42.70g/L precipitation reagent. Peer-review replies explain early versus later culture work but do not fully map this reagent to those two displayed samples.
- Main abstract and single-salt results differ in La/Dy percentage ordering. The mixed-feed record does not import those individual salt percentages. TableS3Nd-oxalate decahydrate assignment is kept within its synthetic-Nd assay.

## Deduplication, provenance and access limits

Hidden and ignored files were included, relevant symlinks followed, and records/research/reviews/history in both checkouts plus cited local raw roots searched.4092 metadata files were read and85 raw matching paths screened by context. Prior matches concern IMA mineral entries, background mentions, the separate Schmitz study and the round52 Lu handoff. No duplicate accepted processing-liquor owner was identified within this scope. Nine referenced historical roots were unavailable; unextracted binary contents and unrelated filesystem paths were not semantically searched. The JSON preserves the exact boundaries and receipts.

Original articles and workbooks remain outside Git. Publisher source terms include CC BY-NC-ND4.0; no full texts, graphics or bulk source cells are redistributed. Canonical CREATE history `history/records/allanite-leachate/2026-10-12T100026Z-codex-3c88ef.yaml` and the distinct inline event describe actual curation. Named validation returned0 and checked one record with no failures. No schema behavior changed.

## Remaining questions

Replicate real-liquor assays with matched broth controls; resolve zero/detection conventions and dose denominators; measure full product composition and mass balance; identify real mixed-precipitate phases; document precipitation temperature/time and the exact high-titer culture batch. These scientific limits do not erase the supported narrower observation. Shared issue closure should describe completed assessment, not claim these experiments were performed.
