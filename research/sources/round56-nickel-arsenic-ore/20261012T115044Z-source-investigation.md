# Nickeline-bearing ore source investigation

UTC: 2026-10-12T11:50:44.555819Z
Researcher: codex, GPT-6; record curator, not independent reviewer.
Base: `934bb36319e857321840c0ae145664ca6910c382`; branch `curate/cmm-expansion-round56-20261012`.

## Scope and decision

Curated one primary-resource owner, [`nickeline-bearing-ore`](../../../data/records/nickeline-bearing-ore.yaml), pending independent review. The Patang low-grade and Talmesi high-grade natural feeds are separate experimental arms, not two new materials or pure nickeline. Nickel/arsenic element owners, laterite and process residues remain conceptually separate. No criticality list, purified-metal recovery, deployment, external mineral ID or consortium taxon ID is inferred.

Record SHA256 `ed5380b36177b247c2adbb0b63444f8663c7bbad02ea438c29800e05a270a47a`. Canonical CREATE [`2026-10-12T114742Z-codex-afabd0`](../../../history/records/nickeline-bearing-ore/2026-10-12T114742Z-codex-afabd0.yaml) SHA256 `1367e6b8d34a651f5db58f0c40a569e31b5051653f225a146e9317080435cbb8`. Named validation completed with exit 0, one record checked and zero failed. Shared gates and scientific acceptance belong to the parent/independent reviewer and are not claimed here.

## Search and acquisition

The exact PII led to [Boroumand et al., Chemosphere 370 (2025):143944](https://doi.org/10.1016/j.chemosphere.2024.143944). Crossref and OpenAlex resolved identity, then Lincoln's [public Figshare API](https://api.figshare.com/v2/articles/28100066) exposed [original PDF file 51716801](https://ndownloader.figshare.com/files/51716801). Its repository MD5 matches the downloaded 8,901,198-byte PDF; title, all five authors, DOI and original journal layout agree. The 12-page original states online publication on 27 December 2024. February 2025 is the issue date; Crossref's 12 December VOR license start is a different metadata date. OpenAlex's submitted-version label does not override the acquired published layout.

Publisher main access returned HTTP 403. The first Elsevier API attempt returned 429; a bounded alternate DOI-metadata route returned only 2,049-byte XML, not full text. The inferred standard [original DOCX supplement endpoint](https://ars.els-cdn.com/content/image/1-s2.0-S0045653524028522-mmc1.docx) returned a genuine 15,172,028-byte Word ZIP; its full matching study title and data bind it to the main article's Appendix A. The inferred PDF alternative returned 404. LibreOffice successfully rendered the original DOCX into 15 pages; this is a local derivative, not a publisher PDF.

The original main is CC BY 4.0; no distinct license banner occurs in the supplement. Full originals, extracted media and renderings remain outside Git in `/private/tmp/cmm-round56-nickel-arsenic-ore-research`. The paired JSON pins all 82 raw artifacts, 12 receipts, source URLs and acquisition timestamps; it excludes ephemeral signed redirect parameters. No new access is claimed for prior raw files.

The JSON enumerates all eleven exact web queries. Searches used first returned sets, no exhaustive pagination or date filters. Exact DOI correction/retraction queries and Crossref update/relation metadata revealed no affecting notice in that bounded coverage. This is not a universal absence claim.

## Deduplication and boundaries

Hidden and ignored files and relevant symlinks were included in both specified checkouts' records, research, reviews and history, plus 205 existing referenced raw/research/evidence roots. Missing roots are explicitly listed in JSON. Text-bearing extensions were searched; every binary and unrelated machine directory was not decoded/searched. Four corpus lines refer to the already deferred round2 heterotroph lead. Current accepted records contain no nickeline-bearing ore owner or this exact study in that scope.

The initial broad raw search produced 2.7 GB because unrelated minified metadata can contain nickel and arsenic far apart. That output is retained but is not claimed fully read. A narrower exact-token file inventory/snippet pass separated IMA nickeline rows, other Boroumand references and numeric false positives. An exact DOI/PII/Patang/Talmesi pass returned exit 1 in the 205 referenced roots. The Acar2025 bibliography and earlier handoff cite JECE112141, the separate heterotroph paper, which is not imported here.

## Primary evidence actually inspected

All twelve main PDF pages were read and visually inspected, including Table 1, Figures 1–6 and the graphical abstract. All fifteen local SI pages were visually inspected, including Table S1 and Figures S1–S14; table XML and document text were also extracted. There are six main scientific figures, one main table, fourteen SI figures and one SI table. Source figures, not abstract-only metrics, support the bounded record.

- Sections 2.1/3.1 and SI Table S1/Figures S1–S6 establish natural provenance, different Ni/As bulk contents, grinding, carbonate/quartz assemblages and local SEM/EDX. These spot measurements and diffraction scale factors are not bulk phase yields. Table S1 has mixed percent/ppm units, a dash and a censored token; no conversion into native mg/kg quantitative observations was made.
- Methods 2.2–2.4, Table 1 and Figures 1–4 support living mixed acidophile assays, initial pH 1.8, nominal 35/45 degrees C and 100-mL working volume in 250-mL flasks. Cultivation versus test amendments are not fully resolved. No strain accessions, exact adaptation transfers, replicate counts or specific sterilization/inhibition protocol are supplied. The official [NCBI genus record](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=74968&mode=Info) confirms Ferroplasma is archaeal; its ID does not identify the mixture.
- Low-grade ferric-only tests 2/11 approach complete early nickel dissolution in Figures 1f/3f. Biological peaks may fall substantially later, notably Figure 3f. Thus neither a universal microbial advantage nor sustained pure-product recovery follows. Initial-pH-only controls and daily-acid chemical tests do not match full biotic pH trajectories.
- SI Figures S7–S12 and main Section 3.4 concern selected residues and qualitative secondary-phase interpretation. Scorodite/jarosite-compatible patterns do not close an arsenic balance or demonstrate long-term stability; added sulfur prevents assigning every sulfur residue to the feed. Kinetic Figures 5/S13 are fitted models, not direct enzyme evidence. Figure 6's inconsistent arm labels preclude exact adopted Co/Cu yields.

## Contradictions retained

Methods 2.3 conflicts with Table 1 and Figures 2–3 on numbering. Highest-loading figure captions say 5 g/L rather than Table 1's 50 or 30 g/L; Section 3.2's 5% maximum conflicts with 0.5% elsewhere. The low-grade mesophilic maximum is called ten versus thirteen days; high-grade completion varies between 27 and 28 days, and Section 3.5 reverses selected nine/thirteen-day assignments. Section 3.2's substrate-benefit prose contrasts with the conclusion's absence of enhancement. Exact optima are not harmonized.

Methods point elemental ICP-MS data to S2, which is a particle-size plot; composition is Table S1. SI S8/S9 list mesophilic tests first but thermophilic duration first. Section 3.4.1 gives the clearer pairing, yet ambiguous captions alone are not used for exact residue timing. Main Figure 6's low-grade numbering conflicts with Table 1 and its high-grade caption excludes plotted tests 35/36. Section 3.3 versus abstract/plot chemical-control percentages also differ. None is silently corrected into a precise new measurement.

## Deferred candidates and next work

1. Independent exact-state scientific review of this new resource, especially control comparisons, arm identity and source qualifications.
2. [JECE112141](https://doi.org/10.1016/j.jece.2024.112141), the separate Glutamicbacter-titled heterotroph study, remains a full-original acquisition and organism/experiment-overlap task. It may reuse the same feed samples and is not independent corroboration for acidophile results.
3. A Persian Geosciences 34(132)(2024):89–106 primary lead comparing chemolithotrophs, heterotrophs and additives needs original DOI/full-text verification and overlap assessment. Its indexed abstract supplies discovery only; no measurements were admitted.
4. Author raw time courses, sterile-control details, replication and sampling/mass-balance data would resolve the exact peak/endpoint, numbering and loading ambiguities. No contact was made.

No schema change, invented history, new deployment claim or duplicated material was needed. This is a curator investigation dossier; the saved independent scientific review is a separate artifact.
