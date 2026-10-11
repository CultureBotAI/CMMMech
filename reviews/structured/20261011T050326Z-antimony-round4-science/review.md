# Independent adversarial scientific review of antimony expansion record

- Review: 20261011T050326Z-antimony-round4-science
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T04:58:17Z
- Finished UTC: 2026-10-11T05:03:26Z
- Reviewer: Codex /root/cmm3_chromium (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The elemental identity, dated US designation and narrow laboratory observation of antimonate transformation by coupled microbial and chemical processes are supported. Control design, nonunique speciation, conflicting lactate recipes and removal-versus-reduction distinctions are explicit. Independent figure/supplement acquisition closed the curator access gap. No actionable record defect was identified.

## Scope And Provenance

All fields of the final antimony record, linked canonical CREATE session and curation dossier; independent primary-source, identity, criticality, figure and supplement checks.

Selection: Named final record assigned by coordinating parent after curator reported its bytes and history complete.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base c081a749cd63feafcc25414f5ad006d1f78f1e36.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:antimony | data/records/antimony.yaml | maintained | Antimony |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Antimony record validation | passed | True | cmmmech:antimony | One record checked; zero failed. |
| Append-only canonical history validation | passed | True | cmmmech:antimony | 36 histories checked; zero errors against the captured trusted base. |
| Nonempty corpus validation | passed | True | cmmmech:antimony | Independently executed after final curator handoff: 27 records checked; zero failed. |
| Completed batch checks | passed | True | cmmmech:antimony | Coordinator executed the final batch check and confirmed terminal exit 0; reviewer independently inspected its completed log: 307 tests passed, 3 skipped in 47.17 seconds, 27 records valid and 36 histories valid. |

## Scientific And Domain Assessments

### Elemental identity and dated official commodity designation

identity: supported. Targets: cmmmech:antimony.

The Sb element root is grounded to ChEBI and kept distinct from feed ions and products. Official criticality preserves jurisdiction, authority, list and edition. No organism identifier is invented for the sediment community.

### Coupled biotic-abiotic transformation and measured fractions

evidence: supported. Targets: cmmmech:antimony.

The laboratory system supports Sb(V)-to-Sb(III) transformation under sulfidogenic conditions and a plausible indirect biogenic-sulfide route. The record correctly separates aqueous Sb loss, solids redox speciation, causal inference and recoverable product.

### Source inconsistencies, nonunique products and restrained claim strength

scope: supported. Targets: cmmmech:antimony.

The unresolved lactate discrepancy and nonunique product speciation are explicit. Supplementary fits show why the record appropriately avoids absolute day-5 absence, exact conversion percentages, crystalline mineral assignment and a matched live-versus-dead causal estimate.

Supplementary Tables S11/S12 contain small day-5 Sb(III) fits despite categorical wording in the main Figure 16 caption. Table S16 and main Discussion use differing late fitted percentages. The target makes none of those numerical speciation claims. These are source/model limitations to retain if a future quantitative ingest is proposed, not defects requiring alteration of the current narrow observation.

### Actual session history and independently acquired evidence

provenance: supported. Targets: cmmmech:antimony.

Canonical CREATE and inline history are distinct actual curation artifacts. Exact base and target/context hashes were inspected before final assessment. The curator access limits and later successful independent acquisition are both retained honestly.

The target is uncommitted working-tree content above c081a749cd63feafcc25414f5ad006d1f78f1e36. Input hashes attest inspected bytes and do not claim they were already committed. Independent raw receipts are /private/tmp/cmm-round4-antimony-independent/acquisition.json; newly downloaded authority/figure/PDF files remain outside Git.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/antimony.yaml; Complete YAML, inline CREATE and history_refs | supports | Final working-tree bytes were read before assessment and rechecked after curator freeze. Element, feed and product are distinguished. The linked actual codex/GPT-6 CREATE session and inline event describe this curation without invented prior authorship. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:30513; Entry heading, embedded MolecularEntity label/identifier, formula and charge | supports | Fresh authority response labels CHEBI:30513 antimony atom, Sb, charge zero. It does not denote antimonate, an Sb mineral species or secondary resource. |
| us-list | https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm; Final 2025 table, antimony row on printed page 50496; 90 FR 50494-50497, November 7, 2025 | supports | Live official final notice individually lists antimony. Record correctly scopes the United States Department of the Interior/USGS designation to its 2025 edition and named commodity rather than every antimony compound. |
| bib-identity | https://pubmed.ncbi.nlm.nih.gov/33681496/; Official PubMed metadata returned for exact title/identifier search | supports | Independently verified Johnson et al. Heliyon 2021 e06275, DOI 10.1016/j.heliyon.2021.e06275, PMID 33681496 and PMC7930292. Publisher PII is S2405844021003807. |
| primary | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7930292/fullTextXML; Methods 2.1, 2.3-2.5, 2.7-2.8, 2.11; Results 3.1-3.2; Discussion 4.2-4.3; main figure captions | supports | Read complete primary XML previously acquired by curator at /private/tmp/cmm-round4-antimony-evidence-20261011/johnson2021.xml and independently rehashed. It supports the system D recipe, wetland community, solution analysis, anoxic solids spectroscopy, A control and separate pasteurized B/mackinawite comparisons. No isolate, enzyme or field deployment is established. |
| figure-13 | https://ars.els-cdn.com/content/image/1-s2.0-S2405844021003807-gr13.jpg; Figure 13 panels and caption | supports | Fresh image visually inspected: sulfate/lactate trends and pH are consistent with microbial activity; initial lactate is near 20 mM, reinforcing the Methods/abstract recipe discrepancy. It is not a direct Sb reductase assay. |
| figure-15 | https://ars.els-cdn.com/content/image/1-s2.0-S2405844021003807-gr15.jpg; Figure 15 fitted aqueous/solid Sb distribution and caption | supports | Fresh image visually inspected: rapid solution depletion precedes extensive fitted solid-phase Sb(III) accumulation. Components are model-based allocations, not separately recovered product masses. |
| figure-16 | https://ars.els-cdn.com/content/image/1-s2.0-S2405844021003807-gr16.jpg; Figure 16 EXAFS and Fourier transforms with standards | supports | Fresh image visually inspected: day-5 system D is similar to the uninoculated control and later samples change toward mixed Sb-O/S coordination. Similarity does not establish absolute absence of early Sb(III); phase identity is not unique. |
| figure-18 | https://ars.els-cdn.com/content/image/1-s2.0-S2405844021003807-gr18.jpg; Figure 18 XANES and EXAFS comparisons | supports | Fresh image visually inspected: separate pasteurized biogenic material and abiotic mackinawite comparisons support chemical Sb reduction; they do not quantify the live-microbial contribution to system D. |
| supplement | https://ars.els-cdn.com/content/image/1-s2.0-S2405844021003807-mmc1.pdf; Supplementary PDF, 44 pages: pages 4, 27-29, 34-36 and 42; Figures S18-S19, S25, S31 and Tables S11-S12, S16 | supports | Fresh publisher PDF acquired successfully, text read at specified locators; pages 29, 35, 36 and 42 rendered and visually inspected. Control spectra support Sb(V); time-course fits support progressively greater Sb(III). Early fit fractions and late comparison percentages vary with fit/source location. These constrain quantitative interpretation but do not contradict the narrowly worded record. No source percentages are promoted to recovery yield. |
| search | Live web search and target primary discussion; Bounded correction/retraction and sulfidogenic counterevidence search | context_only | No affecting correction/retraction returned in the inspected sets. Main discussion reports context-dependent contrasting Fe/sulfide results; the record does not claim universal reduction or null effects. Returned reviews and uninspected leads were not used to prove mechanism. |
| local-search | data/ research/ reviews/ history/ and /private/tmp/cmm-round4-antimony-evidence-20261011/; Gitignore-independent identity, DOI and PMC search | supports | Matches were consistent with the new maintained root, its dossier/history and research references. No second maintained root for this exact identity was found within the stated scope. |
| batch-log | /private/tmp/cmm-round4-check.log; Completed coordinator-run batch log; terminal exit 0 separately confirmed | supports | Reviewer read 307 passed, 3 skipped in 47.17 seconds; 27 records, zero failed; 36 histories, zero errors. Structural validation is not scientific proof. |

## Limits And Additional Notes

- Abstract 10 mM lactate conflicts with the Methods recipe yielding 20 mM; Figure 13 also begins near 20 mM. The record preserves this unresolved loading discrepancy and does not silently select a recipe.
- The main Figure 16 caption describes no day-5 reduction, while supplementary fits assign small Sb(III) fractions (10% in Table S11; 13% in Table S12, with stated fit uncertainty). The record says the day-5 spectrum remained similar to the control, not that absolutely no reduction occurred.
- Fit-dependent percentages differ across the main discussion and supplementary Table S16, and O/S coordination does not uniquely distinguish discrete sorbed Sb(III) plus sulfide from mixed-ligand phases. No raw spectra were refitted, exact conversion fraction or isolated mineral yield certified.
- Pasteurized system B is not a matched killed version of system D; direct microbial Sb respiration and taxon-level causality are neither demonstrated nor excluded. Defined laboratory feed and solution depletion are not industrial recovery.
- Correction/counterevidence searches used bounded first returned sets without pagination. No exhaustive absence of correction, conflict or unreviewed antimony literature is claimed.
- Findings by severity: zero blocker, major, minor or informational defects. Corrections: none made; target and curation-history bytes were left unchanged.
- Evidence accessed_at uses the actual receipt timestamp for newly downloaded material; other entries mark completion of the verification interval beginning 04:58:17 UTC, not simultaneous network retrieval.
- Raw primary XML, figures, ChEBI HTML and the supplementary PDF remain outside Git. Primary article is licensed CC BY-NC-ND 4.0. This review commits paraphrased assessment and acquisition facts only.
- The curator dossier accurately records its earlier figure/supplement retrieval failures. The separate independent review subsequently succeeded through the publisher CDN; these are different acquisition events, not contradictory provenance.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T050326Z-antimony-round4-science
kind: record
repository: CultureBotAI/CMMMech
title: Independent adversarial scientific review of antimony expansion record
started_at: '2026-10-11T04:58:17Z'
finished_at: '2026-10-11T05:03:26Z'
reviewer:
  identity: Codex /root/cmm3_chromium
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: A different agent curated antimony. This reviewer curated the
    chalcopyrite and sphalerite records, did not edit antimony or its history/dossiers,
    independently read the primary study, and newly acquired and visually inspected
    its main figures and supplementary PDF.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The elemental identity, dated US designation and narrow laboratory observation
  of antimonate transformation by coupled microbial and chemical processes are supported.
  Control design, nonunique speciation, conflicting lactate recipes and removal-versus-reduction
  distinctions are explicit. Independent figure/supplement acquisition closed the
  curator access gap. No actionable record defect was identified.
source:
  git_revision: c081a749cd63feafcc25414f5ad006d1f78f1e36
  state: working_tree
  inputs:
  - path: data/records/antimony.yaml
    sha256: 3854163557ef588e4d570f71e6939b406bef24763d31332afe0741400cd91576
    role: target
  - path: docs/records.md
    sha256: 212cdbb723eb1ad9eb76ea1b7dad066914659b1f85eb2cdb51ee67466cfcc8ee
    role: context
  - path: history/records/antimony/2026-10-11T045740Z-codex-3839a3.yaml
    sha256: 58d48ca19a54fbec751504a1d966167fbf005aa4af928a60d0d056d080b332c0
    role: context
  - path: research/ingests/round4-antimony-20261011.json
    sha256: 68afa98fcca72e0ee07975ae22fb7e95b59b680ba6c1c2dc350be117a83678bd
    role: context
  - path: research/ingests/round4-antimony-20261011.md
    sha256: bda74ba72da076d63c1ed4605c7f9e4f851ccdf3a9fbf5f0221676091e8bd784
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 861e6299240364ebddc53f7fb238b11014a5c2d48d2a211a80fcb18a5cc2170c
    role: context
targets:
- target_id: cmmmech:antimony
  path: data/records/antimony.yaml
  label: Antimony
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/antimony.yaml
    role: maintained scientific record
scope:
  description: All fields of the final antimony record, linked canonical CREATE session
    and curation dossier; independent primary-source, identity, criticality, figure
    and supplement checks.
  selection: Named final record assigned by coordinating parent after curator reported
    its bytes and history complete.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:antimony
  exclusions:
  - target: Uncurated BES sample attribution, raw spectroscopy fitting and community
      sequence reanalysis
    reason: No BES mechanism, fitted percentage yield, unique Sb mineral phase or
      individual organism causal assignment is asserted by the target. This is not
      a whole-corpus scientific review.
checks:
- check_id: record-validation
  name: Antimony record validation
  status: passed
  required: true
  summary: One record checked; zero failed.
  target_ids:
  - cmmmech:antimony
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked cmmmech validate
    data/records/antimony.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: history-validation
  name: Append-only canonical history validation
  status: passed
  required: true
  summary: 36 histories checked; zero errors against the captured trusted base.
  target_ids:
  - cmmmech:antimony
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked cmmmech validate-history
    --base c081a749cd63feafcc25414f5ad006d1f78f1e36
  exit_code: 0
  expected_exit_code: 0
- check_id: nonempty-corpus
  name: Nonempty corpus validation
  status: passed
  required: true
  summary: 'Independently executed after final curator handoff: 27 records checked;
    zero failed.'
  target_ids:
  - cmmmech:antimony
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked cmmmech validate
    --require-records
  exit_code: 0
  expected_exit_code: 0
- check_id: batch-check
  name: Completed batch checks
  status: passed
  required: true
  summary: 'Coordinator executed the final batch check and confirmed terminal exit
    0; reviewer independently inspected its completed log: 307 tests passed, 3 skipped
    in 47.17 seconds, 27 records valid and 36 histories valid.'
  target_ids:
  - cmmmech:antimony
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache just check
  exit_code: 0
  expected_exit_code: 0
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/antimony.yaml
  locator: Complete YAML, inline CREATE and history_refs
  accessed_at: '2026-10-11T05:03:26Z'
  support: supports
  summary: Final working-tree bytes were read before assessment and rechecked after
    curator freeze. Element, feed and product are distinguished. The linked actual
    codex/GPT-6 CREATE session and inline event describe this curation without invented
    prior authorship.
  snapshot_sha256: 3854163557ef588e4d570f71e6939b406bef24763d31332afe0741400cd91576
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:30513
  locator: Entry heading, embedded MolecularEntity label/identifier, formula and charge
  accessed_at: '2026-10-11T04:59:15.391522Z'
  support: supports
  summary: Fresh authority response labels CHEBI:30513 antimony atom, Sb, charge zero.
    It does not denote antimonate, an Sb mineral species or secondary resource.
  snapshot_sha256: f8a979f1d681d22c7a1c044a2d48555405622272cfc3d27f7a484ebddebdabdb
- evidence_id: us-list
  kind: authority
  reference: https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm
  locator: Final 2025 table, antimony row on printed page 50496; 90 FR 50494-50497,
    November 7, 2025
  accessed_at: '2026-10-11T05:03:26Z'
  support: supports
  summary: Live official final notice individually lists antimony. Record correctly
    scopes the United States Department of the Interior/USGS designation to its 2025
    edition and named commodity rather than every antimony compound.
- evidence_id: bib-identity
  kind: database
  reference: https://pubmed.ncbi.nlm.nih.gov/33681496/
  locator: Official PubMed metadata returned for exact title/identifier search
  accessed_at: '2026-10-11T05:03:26Z'
  support: supports
  summary: Independently verified Johnson et al. Heliyon 2021 e06275, DOI 10.1016/j.heliyon.2021.e06275,
    PMID 33681496 and PMC7930292. Publisher PII is S2405844021003807.
- evidence_id: primary
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7930292/fullTextXML
  locator: Methods 2.1, 2.3-2.5, 2.7-2.8, 2.11; Results 3.1-3.2; Discussion 4.2-4.3;
    main figure captions
  accessed_at: '2026-10-11T05:03:26Z'
  support: supports
  summary: Read complete primary XML previously acquired by curator at /private/tmp/cmm-round4-antimony-evidence-20261011/johnson2021.xml
    and independently rehashed. It supports the system D recipe, wetland community,
    solution analysis, anoxic solids spectroscopy, A control and separate pasteurized
    B/mackinawite comparisons. No isolate, enzyme or field deployment is established.
  snapshot_sha256: d1070cc171b0663c4e47a7043682365230db62451fe09693c21a35537df2422b
- evidence_id: figure-13
  kind: primary_source
  reference: https://ars.els-cdn.com/content/image/1-s2.0-S2405844021003807-gr13.jpg
  locator: Figure 13 panels and caption
  accessed_at: '2026-10-11T04:59:15.392885Z'
  support: supports
  summary: 'Fresh image visually inspected: sulfate/lactate trends and pH are consistent
    with microbial activity; initial lactate is near 20 mM, reinforcing the Methods/abstract
    recipe discrepancy. It is not a direct Sb reductase assay.'
  snapshot_sha256: 16df5691816221b011f44cea38392b543d5cb8bcbf8a30747bd38964988c2c62
- evidence_id: figure-15
  kind: primary_source
  reference: https://ars.els-cdn.com/content/image/1-s2.0-S2405844021003807-gr15.jpg
  locator: Figure 15 fitted aqueous/solid Sb distribution and caption
  accessed_at: '2026-10-11T04:59:15.393254Z'
  support: supports
  summary: 'Fresh image visually inspected: rapid solution depletion precedes extensive
    fitted solid-phase Sb(III) accumulation. Components are model-based allocations,
    not separately recovered product masses.'
  snapshot_sha256: b779f23ea881f3f878cbf484cf969c3f3de100df39e267b26dd409546d4420e0
- evidence_id: figure-16
  kind: primary_source
  reference: https://ars.els-cdn.com/content/image/1-s2.0-S2405844021003807-gr16.jpg
  locator: Figure 16 EXAFS and Fourier transforms with standards
  accessed_at: '2026-10-11T04:59:15.393697Z'
  support: supports
  summary: 'Fresh image visually inspected: day-5 system D is similar to the uninoculated
    control and later samples change toward mixed Sb-O/S coordination. Similarity
    does not establish absolute absence of early Sb(III); phase identity is not unique.'
  snapshot_sha256: b58c190803b96567585ff442183ecf59b1a2d11f5dcff0bbca6649f7a9f2690e
- evidence_id: figure-18
  kind: primary_source
  reference: https://ars.els-cdn.com/content/image/1-s2.0-S2405844021003807-gr18.jpg
  locator: Figure 18 XANES and EXAFS comparisons
  accessed_at: '2026-10-11T04:59:15.394043Z'
  support: supports
  summary: 'Fresh image visually inspected: separate pasteurized biogenic material
    and abiotic mackinawite comparisons support chemical Sb reduction; they do not
    quantify the live-microbial contribution to system D.'
  snapshot_sha256: 2d1b2a24653e6d53be64ef017799360fdd4a44d48d38d6dd8873ee253a95b632
- evidence_id: supplement
  kind: primary_source
  reference: https://ars.els-cdn.com/content/image/1-s2.0-S2405844021003807-mmc1.pdf
  locator: 'Supplementary PDF, 44 pages: pages 4, 27-29, 34-36 and 42; Figures S18-S19,
    S25, S31 and Tables S11-S12, S16'
  accessed_at: '2026-10-11T04:59:15.394352Z'
  support: supports
  summary: Fresh publisher PDF acquired successfully, text read at specified locators;
    pages 29, 35, 36 and 42 rendered and visually inspected. Control spectra support
    Sb(V); time-course fits support progressively greater Sb(III). Early fit fractions
    and late comparison percentages vary with fit/source location. These constrain
    quantitative interpretation but do not contradict the narrowly worded record.
    No source percentages are promoted to recovery yield.
  snapshot_sha256: 1a33cca2b3d82c734db31ba2185cd04b25402352d2a658b1ba55f0329a3a9dfc
- evidence_id: search
  kind: search
  reference: Live web search and target primary discussion
  locator: Bounded correction/retraction and sulfidogenic counterevidence search
  accessed_at: '2026-10-11T05:03:26Z'
  support: context_only
  summary: No affecting correction/retraction returned in the inspected sets. Main
    discussion reports context-dependent contrasting Fe/sulfide results; the record
    does not claim universal reduction or null effects. Returned reviews and uninspected
    leads were not used to prove mechanism.
  search_scope: 'Queries on 2026-10-11: exact DOI plus correction retraction erratum;
    exact DOI plus correction; exact DOI plus retraction; exact primary title; antimony
    biogenic sulfide reduction mobilization Johnson 2021. First returned sets only;
    no recency filters or pagination. Independent ChEBI identity query was also run.'
- evidence_id: local-search
  kind: search
  reference: data/ research/ reviews/ history/ and /private/tmp/cmm-round4-antimony-evidence-20261011/
  locator: Gitignore-independent identity, DOI and PMC search
  accessed_at: '2026-10-11T05:03:26Z'
  support: supports
  summary: Matches were consistent with the new maintained root, its dossier/history
    and research references. No second maintained root for this exact identity was
    found within the stated scope.
  search_scope: rg --no-ignore --hidden -l 'cmmmech:antimony|CHEBI:30513|e06275|PMC7930292'
    data research reviews history /private/tmp/cmm-round4-antimony-evidence-20261011.
    Hidden and ignored files included; no all-filesystem absence claim.
- evidence_id: batch-log
  kind: validation
  reference: /private/tmp/cmm-round4-check.log
  locator: Completed coordinator-run batch log; terminal exit 0 separately confirmed
  accessed_at: '2026-10-11T05:03:26Z'
  support: supports
  summary: Reviewer read 307 passed, 3 skipped in 47.17 seconds; 27 records, zero
    failed; 36 histories, zero errors. Structural validation is not scientific proof.
  snapshot_sha256: 24d0645002879c4d5861c2eab485eb654090a40bb0dadc27198ed3279532e614
assessments:
- assessment_id: identity-criticality
  area: identity
  topic: Elemental identity and dated official commodity designation
  outcome: supported
  summary: The Sb element root is grounded to ChEBI and kept distinct from feed ions
    and products. Official criticality preserves jurisdiction, authority, list and
    edition. No organism identifier is invented for the sediment community.
  target_ids:
  - cmmmech:antimony
  evidence_ids:
  - record
  - chebi
  - us-list
  - bib-identity
  dimensions:
  - name: material-form
    value: Element Sb; experimental KSb(OH)6, ferrihydrite-associated species and
      sulfide-bearing products distinct
    definition: The root identity is not an antimonate or mineral-species identifier.
    evidence_ids:
    - record
    - chebi
  - name: criticality
    value: United States of America; Department of the Interior/USGS; Final 2025 List
      of Critical Minerals; November 7, 2025
    definition: Commodity-list membership does not designate every Sb compound or
      resource.
    evidence_ids:
    - us-list
    - record
  - name: organism
    value: Wetland sediment community from Argonne; no strain or individual taxon
      causal claim
    definition: An inoculum source and community activity do not identify a direct
      Sb-reducing organism.
    evidence_ids:
    - primary
    - record
- assessment_id: mechanism
  area: evidence
  topic: Coupled biotic-abiotic transformation and measured fractions
  outcome: supported
  summary: The laboratory system supports Sb(V)-to-Sb(III) transformation under sulfidogenic
    conditions and a plausible indirect biogenic-sulfide route. The record correctly
    separates aqueous Sb loss, solids redox speciation, causal inference and recoverable
    product.
  target_ids:
  - cmmmech:antimony
  evidence_ids:
  - record
  - primary
  - figure-13
  - figure-15
  - figure-16
  - figure-18
  - supplement
  dimensions:
  - name: biomass
    value: Living sediment-inoculated system D; uninoculated A; separately pasteurized
      day-21 B
    definition: Pasteurized B starts without Sb and is subsequently challenged; it
      is not a killed D replicate.
    evidence_ids:
    - primary
    - record
  - name: substrate-conditions
    value: Duplicate 200 mL microcosms in 240 mL bottles; 2 mM Sb(V), 50 mM Fe(III)
      ferrihydrite, reported 10 mM sulfate; lactate 10 versus 20 mM unresolved
    definition: Argon sparging, 30 degrees Celsius dark roller incubation and observed
      pH time points are retained; medium initial pH is not a clamped reactor pH.
    evidence_ids:
    - primary
    - record
    - figure-13
  - name: controls
    value: Uninoculated A removes about 98% of solution Sb by day 5 without detected
      reduction; separate pasteurized B and abiotic mackinawite form Sb(III)
    definition: Sorption alone can produce removal, while chemical comparisons support
      an indirect route without isolating its exact live-microbial share.
    evidence_ids:
    - primary
    - figure-18
    - supplement
  - name: analytical-fraction
    value: Total Sb in 0.2 micrometre filtrate by ICP-OES; anoxic retained solids
      by Sb K-edge XANES/EXAFS
    definition: Solution depletion and fitted solid-phase oxidation/coordination states
      are distinct measurements.
    evidence_ids:
    - primary
    - figure-15
    - figure-16
    - record
  - name: outcome
    value: More than 99% solution depletion by day 5; later progressive Sb(III) with
      O/S coordination
    definition: Early depletion is not proof of complete early reduction; fitted spectral
      components are not isolated product quantities.
    evidence_ids:
    - primary
    - figure-15
    - figure-16
    - supplement
  - name: deployment
    value: Defined-feed laboratory microcosms
    definition: No ore/waste treatment, recovered-product yield or industrial deployment
      is established.
    evidence_ids:
    - primary
    - record
- assessment_id: uncertainty
  area: scope
  topic: Source inconsistencies, nonunique products and restrained claim strength
  outcome: supported
  summary: The unresolved lactate discrepancy and nonunique product speciation are
    explicit. Supplementary fits show why the record appropriately avoids absolute
    day-5 absence, exact conversion percentages, crystalline mineral assignment and
    a matched live-versus-dead causal estimate.
  target_ids:
  - cmmmech:antimony
  evidence_ids:
  - record
  - primary
  - figure-13
  - figure-16
  - figure-18
  - supplement
  - search
  details: Supplementary Tables S11/S12 contain small day-5 Sb(III) fits despite categorical
    wording in the main Figure 16 caption. Table S16 and main Discussion use differing
    late fitted percentages. The target makes none of those numerical speciation claims.
    These are source/model limitations to retain if a future quantitative ingest is
    proposed, not defects requiring alteration of the current narrow observation.
- assessment_id: provenance
  area: provenance
  topic: Actual session history and independently acquired evidence
  outcome: supported
  summary: Canonical CREATE and inline history are distinct actual curation artifacts.
    Exact base and target/context hashes were inspected before final assessment. The
    curator access limits and later successful independent acquisition are both retained
    honestly.
  target_ids:
  - cmmmech:antimony
  evidence_ids:
  - record
  - local-search
  - batch-log
  - supplement
  details: The target is uncommitted working-tree content above c081a749cd63feafcc25414f5ad006d1f78f1e36.
    Input hashes attest inspected bytes and do not claim they were already committed.
    Independent raw receipts are /private/tmp/cmm-round4-antimony-independent/acquisition.json;
    newly downloaded authority/figure/PDF files remain outside Git.
findings: []
actions: []
limitations:
- Abstract 10 mM lactate conflicts with the Methods recipe yielding 20 mM; Figure
  13 also begins near 20 mM. The record preserves this unresolved loading discrepancy
  and does not silently select a recipe.
- The main Figure 16 caption describes no day-5 reduction, while supplementary fits
  assign small Sb(III) fractions (10% in Table S11; 13% in Table S12, with stated
  fit uncertainty). The record says the day-5 spectrum remained similar to the control,
  not that absolutely no reduction occurred.
- Fit-dependent percentages differ across the main discussion and supplementary Table
  S16, and O/S coordination does not uniquely distinguish discrete sorbed Sb(III)
  plus sulfide from mixed-ligand phases. No raw spectra were refitted, exact conversion
  fraction or isolated mineral yield certified.
- Pasteurized system B is not a matched killed version of system D; direct microbial
  Sb respiration and taxon-level causality are neither demonstrated nor excluded.
  Defined laboratory feed and solution depletion are not industrial recovery.
- Correction/counterevidence searches used bounded first returned sets without pagination.
  No exhaustive absence of correction, conflict or unreviewed antimony literature
  is claimed.
notes:
- 'Findings by severity: zero blocker, major, minor or informational defects. Corrections:
  none made; target and curation-history bytes were left unchanged.'
- Evidence accessed_at uses the actual receipt timestamp for newly downloaded material;
  other entries mark completion of the verification interval beginning 04:58:17 UTC,
  not simultaneous network retrieval.
- Raw primary XML, figures, ChEBI HTML and the supplementary PDF remain outside Git.
  Primary article is licensed CC BY-NC-ND 4.0. This review commits paraphrased assessment
  and acquisition facts only.
- The curator dossier accurately records its earlier figure/supplement retrieval failures.
  The separate independent review subsequently succeeded through the publisher CDN;
  these are different acquisition events, not contradictory provenance.
links:
- research/ingests/round4-antimony-20261011.md
- research/ingests/round4-antimony-20261011.json
tags:
- antimony
- independent-scientific-review
- round4-20261011
```
