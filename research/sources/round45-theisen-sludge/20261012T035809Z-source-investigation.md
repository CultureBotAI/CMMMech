# Theisen sludge: resource context with bioleaching source gap retained

UTC: 2026-10-12T03:58:09.057901+00:00
Worktree: `/private/tmp/CMMMech-expansion-round45-20261012`
Trusted base: `2b975ae5327b94ac3c1e6583378408add2b8d1f2`
Curator: codex (GPT-6; codex). Independent review remains a separate step.

## Decision

Created [`theisen-sludge.yaml`](../../../data/records/theisen-sludge.yaml) as a secondary resource with identity and sampled-feed analytical context only. The complete official Meschke et al. IMWA2016 paper independently supports the Helbra sample; its biological data are attributed to another source, and its membrane tests use synthetic solutions. No mechanism, criticality, taxon/strain identifier, numerical yield or industrial recovery assertion was added. [Issue140](https://github.com/CultureBotAI/CMMMech/issues/140) remains open.

Record SHA-256: `9b06fd03d106e687f5618d9a5faf1601e80b0c88f5fc908e0d5604d5d10a96d5`. CREATE history: [`history/records/theisen-sludge/2026-10-12T035605Z-codex-f36615.yaml`](../../../history/records/theisen-sludge/2026-10-12T035605Z-codex-f36615.yaml), SHA-256 `4a8d5aa67b02c5e1b43e01892f785fe0c6e159119c8783d506beadf6261c9aee`. Actual named validation exited0, checked1/failed0; `/private/tmp/cmm-round45-theisen-research/named-validation-terminal.json` binds the log and exact bytes. The coordinator's initialization receipt honestly reuses fresh checks at this identical published base.

## Acquisition and identity

Read the live issue and round42 dossier before new attempts. Fresh official EuropePMC and NCBI conversion responses identify PMID27005888 and explicitly report that DOI10.1111/jam.13142 is not in PMC. The newly available official PMC Cloud route therefore does not apply. Prior unchanged Wiley/ResearchGate denials and UFZ verification challenge were neither repeated nor bypassed. Bounded author/institutional searches did not yield a complete original Klink graphic/SI package; HZDR reported a robots restriction.

The newly acquired [official IMWA paper](https://www.imwa.info/docs/imwa_2016/IMWA2016_Meschke_283.pdf), *Nanofiltration – A new separation pathway in secondary mining*, is eight pages, printed1356–1363. Its five printed authors are Meschke, Gumnior, Daus, Haseneder and Repke, matching the [official proceedings index](https://www.imwa.info/imwaconferencesandcongresses/proceedings/298-). The PDF metadata incorrectly names an unrelated Chile-tailings paper and different authors; UFZ's citation adds editor Paul to the author list. The record follows the printed article and matching proceedings entry. No DOI is invented.

Original PDF: `/private/tmp/cmm-round45-theisen-research/raw/meschke2016.pdf`, SHA-256 `3229ef0a16fef1dce2eeff82d306c8c6cd280c95af20fe54fc82027be4bbd6a1`. All eight pages, nine figures, Table1 and three equations were visually inspected in `raw/meschke2016-pages/page-01.png` through `page-08.png`; complete extracted text is adjacent. The complete paper cites no supplement, and its specific proceedings entry links only this PDF. This is a bounded inventory, not proof no auxiliary material exists anywhere.

## Evidence and limits

- Printed1356 identifies copper-shale blast-furnace gas-scrubbing residue. Printed1357–1358 documents Helbra mono-landfill sampling at4m inMay2015, EDXRF for Cu/Mo/Pb/Sn/Sb/Zn and aqua-regia-extract ICP-MS for Ag/Co/Ge/Re. These distinct assay fractions do not establish total extractability. Figure5A on1360 supports qualitative Zn/Pb predominance among measured components; no exact graph values were transcribed.
- Figure5A labels mg/kg but adjacent prose uses mg/L for solid trace constituents and repeats Co. Figure5B prints density0.6kg/m3. No affected values, density, sales estimate or reserve calculation is adopted.
- Figure2 on1357 explicitly reuses Klink2016 bioleaching-solution information. It is not independent replication or a substitute for original controls, Tables1–2/Figures1–3 and SI TableS1/FiguresS1–S9.
- Printed1358 makes the membrane feeds synthetic, containing Ge/Mo/Re separately or combined. Figures6–9 do not test the sampled sludge or its actual leachate. Equation1 measures concentration retention; equation2 defines permeate-volume recovery, not metal yield. The87.5/85.7% protocol discrepancy and nominal pH-range/test difference remain outside accepted claims.
- Figure1 is a proposed process chain; later cross-flow testing is future work. Neither a laboratory membrane result nor industrial waste origin demonstrates industrial deployment.

## Study overlap, notices and remaining acceptance needs

Indexed2015 DOI10.4028/www.scientific.net/AMR.1130.321 text repeats Ram6F/Nochten2 and flask/bioreactor patterns. Indexed2016 poster text describes a distinct short2wt% assay but does not establish independent complete evidence. The overlap must be resolved against originals before mechanism extension. GenBankKU569322 remains an unverified accession for that future assessment. No source-derived species ID was placed in the record.

Searches covered exact title/DOI with correction, erratum, retraction and supplement terms; no affecting notice appeared in the returned sets. No exhaustive absence claim is made. Indexed Wiley publication-history labels now distinguish accepted-manuscript online23March2016, version-of-record online25April2016 and issue-online13May2016, with June2016 issue dating. These metadata labels do not resolve missing experimental originals.

Issue140 still needs legitimate full originalKlink main/SI acquisition, culture/accession verification, viable/inactivated and uninoculated control assessment, feed pretreatment/loading/pH/temperature/sampling/replication, dissolved-versus-solid accounting, and2015/2016 overlap checks. The new resource record does not close those requirements. Older UFZ2001 characterization chapters and later oxidative-leaching/analytical papers remain leads, not imported evidence.

## De-duplication and provenance

Cycle-safe reference extraction read3462 metadata files across current round45 and original-main scientific directories (`data`, `research`, `reviews`, `history`). `rg --no-ignore --hidden --follow` searched these trees plus145 available referenced raw roots. There were no maintained record hits for Theisen/study/culture patterns. Existing matches were source-only dossiers, review/reference logs and31 prior-raw metadata/indexed-text/dedup files. Nine referenced roots were unavailable; exact paths and commands are in the JSON. Unextracted image/PDF content is not claimed exhaustively absent. Searches did not touch environments or modify original main.

Acquisition receipts1–3, search assessment, dedup outputs, named validation and all retained raw artifact hashes are listed in the paired JSON. Raw copyrighted sources remain outsideGit; no redistribution permission or license is inferred. This dossier is a curation handoff, not its own scientific approval.
