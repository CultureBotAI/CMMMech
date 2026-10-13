# Round 61 initial publication review

UTC: 2026-10-13T02:14:11.399013Z. Reviewer: Codex /root/publication_completion_check.

## Revision and working changes

Reviewed revision `78ba2f4c84ff84be64b0da23e603f59c761905aa` on `research/cmm-source-followups-round61-20261013` in `/private/tmp/CMMMech-source-followups-round61-20261013`. The source report is an uncommitted addition; the paired JSON captures the complete observed working-change list. Fluorine curation and its independent scientific review are separate ongoing work.

## Scope and evidence checked

This initial review checks the exact publisher-corroboration statement in `research/sources/round61-fluorite/20261013T021048Z-source-investigation.md`. The paired JSON pins that report, its manifest, the retained Elsevier XML and Crossref response by SHA-256. The XML was inspected in full; it contains title, DOI, journal and date under `coredata`, but no author fields. Crossref contains authors M. Wainwright and S. Supharungsun. No live acquisition, record mutation or remote mutation occurred.

## Findings by severity

### Minor — ROUND61-PUBLICATION-F1: publisher API author corroboration overstated

The report says: “Crossref and the publisher API independently match title, authors, DOI and March 1984 publication.”

The retained publisher XML corroborates title, DOI, journal and date only. Claiming that it independently matches the authors exceeds the captured evidence. This is a narrow provenance attribution defect; article identity and scientific findings are not disputed here.

## Required correction

Attribute author verification to Crossref and the original scan; state that the Elsevier API corroborates title, DOI, journal and publication date only. Refresh the source manifest report hash. Preserve this initial review and use a timestamped successor disposition.

## Corrections and unresolved questions

No correction has yet been verified. This finding is open. The final frontier/report, independent fluorine scientific review and validation receipts are still required for the final publication audit.

## Verdict

**needs_curation** for publication metadata. This initial artifact is not a final scientific or publication acceptance.
