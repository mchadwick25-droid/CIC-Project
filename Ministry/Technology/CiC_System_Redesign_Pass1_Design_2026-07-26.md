# Church in Conversation: System Redesign — Pass 1 Design Document

**Date:** 2026-07-26
**Produced by:** Fable (Pass 1 of 2, per `CiC_System_Redesign_Fable_Brief_2026-07-25.md` §10)
**Status:** DRAFT — for Mark's review and refinement. Nothing here is adopted until he says so. Pass 2 (the build blueprint) does not begin from this document until it has been reviewed and finalized. **Adversarially reviewed once (Opus, 2026-07-26); all 3 P0s and all 12 P1s from that review applied directly — see `Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md` for what changed. P2 polish items remain open.**

---

## 0. How this document was produced, and what was verified

**What was read in full, directly:** the brief; all nineteen research documents in `Ministry/Operations/Audits/CiC_Redesign_Research_2026-07-25/` (docs 11 and 18 skimmed as historical per the index's own flag; doc 19 read in full to confirm every prior finding was applied); the Constitution V2.2, Vision V2.0, Facilitator Governance V3.6 and V3.7 PROPOSAL, Representative Construction Framework V3.2, and Table Design V2.3 (text extracted from the .docx files); the L4 templates and Source Registry Template; the live safety-testing script (`CiC_Live_Safety_Testing_Script_2026-07-21.docx`, all seven batteries with transcripts); Cross-World Roundtable Validation PART II in full via `git show CiC-Fable-Experiment:World-Builds/Cross_World_Roundtable_Validation.md`; the one real two-world runtime session (`cic-poc/backend/transcripts/d1ec86a7-…json`, read in full including its citation payloads); and a single-world contrast session (`6bdbe5cb-…json`).

**What was verified against the running code** (each item checked directly in `cic-poc/backend/`, not taken from the brief): the five architecture facts in brief §3 (vestigial LangGraph graph; two turn engines with the single-vs-all decision only on the non-streaming path; the dead participant-role lane system; the single-drift-signal slot; the existing `/api/session/{id}/audit` endpoint), plus the `pending_guidance` single-slot overwrite, the Quick Meaning parser drop, the never-embedded retrieval conditions, the em-dash conditions, the absence of any runtime readability implementation, and the Facilitator-turn exclusion in `build_public_transcript`. **Four verification results refine what the brief carries, and this document uses the refined versions:**

1. **The Quick Meaning drop is format-dependent, not universal:** `indexer.py`'s `split("---", 2)` discards Quick Meaning for the four worlds whose front matter is fenced (Alexandria 45, PAHC 13, Imperial-Juridical 12, Syriac 10 — 80 of 104 chunks). The other 24 survive by formatting accident, not design: Hieronymian's 15 (plain-YAML front matter) and Desert's 9 (a bold inline `**Quick Meaning:**` label rather than the `## Quick Meaning` heading the other worlds use — a format the original per-world audit's own search missed). All 104 chunks have Quick Meaning authored; the fix is the same, and the audit scope is per-world formatting, not per-world authoring.
2. **The Constitution file in `L1-Foundation/` is internally headed V2.3**, while every downstream document's grounding note still cites "Constitution V2.2." Article citations below follow the V2.3 text.
3. **Article 17 mandates a "single fixed vocabulary" of confidence but delegates its content** to the Construction Framework (with its own footnote flagging that update as pending); the five levels (Documented / Widely Accepted / Dominant Modern Reconstruction / Contested / Inferential-Thin) currently live in the Construction Notes Template. The schema treats the five levels as the participant-facing rendering and gives them the canonical home Article 17's delegation is waiting for.
4. **The direct-address rule is already governance law.** Facilitator Governance §8 (identical in V3.6 and V3.7): *"When the participant addresses a specific Representative, you route accordingly. Immediately, completely, without editorial intervention."* The live streaming engine structurally violates this — `MIN_MULTI_WORLD_TURNS = 2` compels a second world to speak, and nothing on that code path reads address at all. §6's turn-selection design is therefore not a new rule but the enforcement of an existing one, and the multi-agent literature's p<0.001 result for it is corroboration, not the warrant. (FG §8 is four prose paragraphs, not numbered rules — cited here and throughout by its actual text, not an invented rule number.)

A consolidated list of governance-document defects found during verification (stale cross-references, count errors, one direct contradiction between RCF ¶189 and the Construction Notes Template's own required-field language) is in Appendix B — most are one-line edits Pass 2 can carry.

**Confidence discipline.** Claims below inherit the research corpus's own confidence ratings. Where a load-bearing claim rests on a Medium-confidence source finding (flagged in the research docs' own "Do not cite" sections), this document says so rather than laundering it to settled. Three examples used carefully throughout: the exact ~25% Claude answer-reversal figure under pushback (doc 16, fetch-summary — the *vulnerability* is designed against; the *number* is not treated as settled), the exact 256-word-piece → ~85% truncation arithmetic (doc 15 rates the cutoff Medium; the mechanism itself is verified from the model's own config), and Archer's morphogenetic cycle (doc 13: Medium-High, secondary sources — the sequence is borrowed as a documentation shape, not as a philosophy of history).

**What governs.** Vision V2.0's rigor language ("what the methodology **requires** of every world build") governs throughout, per the brief's §3 resolution. Constitution Article 5 bounds the cost goal: where cost and rigor genuinely conflict, rigor wins — and this design found no place where they do; every major cost lever below is also a quality lever, which is the brief's own §2 hypothesis, confirmed.

**The bedrock this design never touches:** the mission; the Five Convictions; a genuinely safe space for a participant to explore faith and the story of Jesus — without pressure, without distortion, without harm. Everything else in this document is a proposal.

---

## 1. The design in one page

Today, a CiC world is a set of hand-authored prose documents (Doc_01–Doc_09), a set of hand-authored deployment artifacts (Permanent Prompt, Capsule Core, lexicon chunks, Facilitation Brief) kept in sync with those documents by memory, and a runtime that consumes the deployment artifacts through an untuned retrieval stack and two divergent turn engines. The research corpus converged on one diagnosis from four directions: **the real failures live at the seams — between prose and its companion artifacts, between build layers, between what was built and what is reachable at the moment of speaking.**

The redesign closes the seams structurally rather than by adding more review:

1. **One dataset per world — the World Record Set.** Every addressable unit — a source, a term, a story, a quote, a force, a gravity, a figure, a contested claim — is one structured record carrying its own prose *inside* the record, its confidence axes, its retrieval behavior, its register (emic/etic), and its relations to other records. There is no companion document to fall out of sync with, because there is no companion document: the record is the single place its facts live. (§3)

2. **Every deployment artifact is a generated view.** Permanent Prompts, Capsule Cores, retrieval chunks, indexes, the World Facilitation Brief, the participant-facing repository, and the three access levels are all rendered from the record set by deterministic view specs. The document type that most reliably got dropped (the Facilitation Brief — review-cleared for 2 of 6 worlds, absent for the last world built) stops being a document anyone authors at the end of a long build and becomes a render nobody can forget. Voice-bearing views are versioned artifacts with continuity regression, never silently regenerated. (§3.9, §5)

3. **The build process becomes: populate records, pass machine gates, then review content.** The dominant defect class in all six worlds — a fix landing where the reviewer looked while the same fact stayed stale in three other places — becomes structurally impossible for everything downstream of the records, and the review effort that used to police synchronization is redirected at the two things machines can't check: whether the content is true and whether the world is honestly represented. Every gate that has ever failed as a written rule becomes an executable check or a required saved artifact. (§4)

4. **Representative construction becomes context engineering over the record set** — a specified assembly of always-present, session-loaded, and retrieved-on-demand material, with an explicit anti-parroting guard, voice modeled as situation-conditioned trait intensities against a fixed rubric, and demonstrations judged against that rubric rather than counted. (§5)

5. **Facilitator governance becomes one engine-level layer both endpoints traverse**, implementing the three measured fixes the research identified: a direct-address rule ahead of holistic speaker selection, a positive-evidence grounding mechanism (the restricted offer), and an evidence-conditioned response to participant pushback that can tell a grounded correction from an ungrounded one. The public transcript gains the Facilitator's own spoken words — which the isolation boundary as written never excluded. (§6)

6. **Retrieval is rebuilt from the index up** — but only after a deterministic, zero-API-cost evaluation harness is built and a baseline committed, so every retrieval change in this document is falsifiable. The single biggest quality-and-cost item: the always-present Quick Meaning layer rides in the cached prefix, making every term reachable every turn at roughly a tenth of today's per-turn retrieval cost, while the scholarly apparatus that currently leaks "documentation voice" into every turn stops entering the generation context at all. (§5.4, §8)

The rest of this document specifies each piece, then accounts for what is preserved from §4 of the brief (§7), the cost comparison (§8), the transcript pressure test (§9), the measurement plan (§10), and the world-build completion standard (§11).

**Naming note.** "World Record Set" (WRS) is used throughout as a working name for the per-world dataset. Rename freely; nothing hangs on the label.

---

## 2. The eight jobs, restated as design obligations

Brief §6 defines eight jobs every piece of information must serve. This design assigns every job at least one owning structure, and the schema tables in §3 carry a `jobs` column so the mapping is checkable per field rather than asserted globally:

| # | Job | Owning structure(s) in this design |
|---|---|---|
| 1 | Rigor/grounding | The three-axis confidence block on every record; per-claim source licensing; the fabrication adjudicator's intrinsic/extrinsic split |
| 2 | Repository/reference | The record set itself plus the repository view (§3.9, §5.6); rights fields gate public display |
| 3 | Representative voice-construction | `voice_surface` fields on term/story records; `text_translation` + `license` on quote records (§3.4); the Voice Profile record; the assembly spec (§5) |
| 4 | Runtime retrieval | The retrieval block on every retrievable record; the rebuilt index (§5.4) |
| 5 | Cross-reference/consistency | Typed, directional `relations[]` on every record; referential-integrity machine gates (§4.2) |
| 6 | Participant-facing translation | `quick_meaning`, `plain_explanation` (Level 2), `conceptual_distance_note`; the confirmed-gloss list as record data |
| 7 | Anachronism boundary | `period_sense`/`prior_sense`/`modern_sense`, `register`, world time-window fields; the modern-term bridge's `distinguishing_claim` (§6.6) |
| 8 | Contestation/pressure-holding | The `contested_claim` record type (§3.7) — a first-class record, not just a runtime mechanism and a metric |

---

## 3. Deliverable 1 — The schema: record types, fields, and the eight jobs

### 3.0 Conventions that apply to every record

Every record, regardless of type, carries this envelope. Fields marked ▲ are new to this design; unmarked fields formalize something CiC already does.

| Field | Type / values | Jobs (§2) | What it captures |
|---|---|---|---|
| `id` | stable, never reused (`syrlex002`, `srcSYR010`) | 2, 5 | CiC already has this discipline; it is why ID-based evaluation and session exclusion sets are cheap |
| `world_id` | manifest key; `facilitator` for Facilitator-owned assets | all | Ownership. The modern glossary and bridge dictionary are `facilitator` assets; a world's glossary belongs to the world — the standing rule, now a field |
| `record_type` | `source · term · story · quote · gravity · force · figure · contested_claim · voice_profile · demonstration · world_core · modern_term · search_record` | 2 | |
| `jobs[]` ▲ | subset of the eight jobs (§2) | — | Which jobs this record serves — makes "a job with no field responsible for it" a queryable failure instead of a discovered one |
| `register` ▲ | `emic / etic / emic-unavailable` | 3, 7 | Whether this content is the world's own categories or the analyst's comparative ones (doc 13 §2). `emic-unavailable` records an honest absence — a builder's stand-in label can never quietly become the world's own word again (the *Apophthegmata Patrum* lesson) |
| `confidence` ▲ | three axes, replacing today's single grade: `citation_specificity` (A–E, today's definitions narrowed to pointer precision), `verification_state` (`verified-direct / verified-via-authority / named-not-rechecked / unverified`) + `verification_date`, `evidentiary_weight` (`load-bearing / corroborating / illustrative / contested`) | 1 | The three things today's single grade conflates (doc 12 finding 4). The outward A–E letter is *derived* so nothing downstream breaks. The constitutional five-level formation-confidence vocabulary (Documented … Inferential/Thin) is a **separate axis** grading the reconstruction claim, not the citation — kept distinct, rendered participant-facing, and given the canonical home Article 17's delegation clause is still waiting on. `disposition` (`in-use / removed-from-use`) becomes an explicit field — today it exists only in the living-document protocol's prose, not the entry schema |
| `grade_criteria_version` ▲ | version string | 1 | UBS3→UBS4 drift control (doc 12): grading criteria are versioned, and §10's measurement plan includes a periodic re-grade audit of sampled old records |
| `sources[]` | list of `{source_id, locus, licensed_for}` | 1 | Per-claim traceability — the Checkpoint rule carried forward: no claim without a source reference, no source reference without a source record |
| `relations[]` ▲ | typed, directional: `{type, target_id, note}` | 5 | The envelope concept. Each record type implements it under its own name and vocabulary below — `field_relations[]` on `term` (§3.2), `interaction[]` on `gravity` (§3.5), `connections[]` on `force` (§3.5) — but all three are `relations[]` for gate purposes: every one is directional, every one is reciprocity-checked by the same §4.2 gate. Direction is **required** on all of them — the verb-shaped/noun-shaped finding (doc 07: Desert 9/9 genuine vs HAL 3/9) becomes a schema constraint, not a style accident |
| `eviction_priority` ▲ | integer rank | 4 | What drops first under token pressure (doc 09's `truncation_priority`) |
| `cache_stability` ▲ | `static / session / turn` | 4 | Whether the field can change turn-to-turn without breaking the cached prefix. Deliberately separate from `eviction_priority` — the two can pull opposite ways (brief §7) |
| `grounding_criterion` ▲ | derived: `low / standard / high` | 6 | How sure the system must be that this content was *understood*, not just said (§6.4). Derived — a term with a sharp `conceptual_distance_note` gap, a `contested` weight, or `emic-unavailable` register is high-criterion by rule, not by hand-tagging |
| `review_state` | `draft / cleared-review / approved-to-proceed / frozen` | 2 | CO-021's three-tier vocabulary, on the record itself. A review that clears a record names the saved review artifact (CO-020: no self-certified state transitions) |
| `schema_version` | integer | 2 | Doc 12's sequencing rule for a living dataset: existing content migrates in marked, not silently rewritten |

**Append-only discipline.** The record set inherits the Source Registry's own rule: never renumber, never delete. A discredited record moves to a terminal state and stays as a record of what was tried. (This is also the same discipline §6.7 adopts for conversation state — one principle, both layers.)

### 3.1 `source` — the Source Registry, generalized

The ten current fields all survive; the additions are doc 12's Tier 1 and Tier 2 recommendations plus doc 14's discovery block, adopted essentially as specified there — those two documents did the field-level design work and this design takes it rather than re-deriving it.

| Field | Values | Jobs | Notes |
|---|---|---|---|
| `attribution_status` ▲ | `genuine / dubium / spurium / anonymous / pseudonymous / attributed-later` | 1, 2 | Required on every primary-type row. The CPG convention (doc 12's highest-severity gap; verify the printed Clavis's exact editorial language before citing it externally — doc 12 rates it Medium). Row 33's Ephrem/bnat-qyama judgment — made correctly, stored in free text — becomes queryable |
| `attribution_note` ▲ | free text | 1 | Whose attribution, in what source, how late ("Jacob of Serugh, 6th-c. *Vita Ephraemi*") |
| `level_of_description` ▲ | `item / work / corpus / aggregate-attestation` | 2 | ISAD(G) 3.1.4 — fixes item-level rows and aggregate rows (Syriac rows 10 vs 13) sitting at the same apparent level |
| `work_author`, `work_title`, `work_locus` ▲ | split from the `Source` string | 1, 2 | |
| `edition`, `translation`, `edition_status` ▲ | `critical / standard-pre-critical / uncritical-reprint / superseded / none-consulted` | 1 | Chicago-completeness: edition and translator named. "1894 edition still the critical standard" (Parisot) distinguishable from "1894 edition superseded in 1962" |
| `consulted_as` ▲ | `original-critical / original-uncritical / translation / secondary-report-only` | 1 | The "quoted in" disclosure as a controlled value |
| `language` / `script` ▲ | ISO 639-3 / ISO 15924 | 1, 2 | DACS Single-Level Required; a registry spanning Syriac, Greek, and Latin can finally answer "which sources did we read in the original" |
| `genre_form` ▲ | `letter / homily / conciliar-act / liturgical-text / hagiography / chronicle / legal-rescript / polemic / monastic-rule / apophthegm-collection / commentary / monograph / journal-article / reference-work` | 1 | Presnell's audience-and-purpose criterion — the one classic source-criticism category with no home today |
| `purpose_audience` ▲ | one sentence | 1 | Why made, for whom — different genres license different inferences from identical content |
| `discovery_channel` ▲ | `field-bibliography / database-search / library-catalogue / backward-snowball / forward-snowball / cited-in-another-row / step0-seed-list / prior-world-build / builder-prior-knowledge / reviewer-supplied / participant-question` | 1, 2 | Required on every row, Native and Excluded alike. `builder-prior-knowledge` is a neutral, stateable value (Greenhalgh & Peacock: 24% of a field-leading review's sources came from exactly there) — but it is also, per the Syriac Round 1 review, the fabricated-precision risk map, so a reviewer can sort by it |
| `discovery_instrument`, `discovery_date` ▲ | free text + ISO date | 1 | "BIBP, searched 2026-07-26, subject=Aphrahat"; "builder prior knowledge, no instrument" |
| `snowball_parent` ▲ | source id | 5 | Makes "how many levels did we snowball" answerable for the first time |
| `external_ids[]` ▲ | `{scheme: syriaca / cpg / cpl / bhg / bhl / bhse / cts-urn / viaf / doi, value, uri}` | 2 | FAIR F1; the Syriac infrastructure is free and already covers Aphrahat, Ephrem, Griffith, Brock, Harvey, Malki |
| `transmission_path` ▲ | structured note | 1, 2 | Transmission history as a per-row field, not per-author prose — surfaceable in the repository view |
| `field_state` ▲ | `majority / minority / contested / superseded / n-a` | 1 | State of the question — distinct from author bias, which Author Gravity already covers well |
| `rights_status`, `license`, `display_permitted` ▲ | controlled | 2 | Blocking the moment the public repository shows translated text; recorded now, enforced by the repository view |
| *(carried forward unchanged)* | `Type` (P/S/M/L), `Boundary Status` (Native/Excluded), `Exclusion Reason` (Out-of-Boundary / Named Comparandum), `Comparandum Note`, `Licensed For`, `Verification Note`, `Added` | | `Licensed For` is CiC's own contribution (no counterpart in any standard surveyed) and the thing that makes the registry a control rather than a bibliography. The `Added` + `Verification Note` pair is renamed a **Description Control** block, citing ISAD(G) — content unchanged, recognition gained for free |

**Backfill rule** (doc 12/14, adopted verbatim): version the schema; existing rows become `schema_version: 1`; backfill only `attribution_status`, `level_of_description`, `language`/`script`, and coarse block-level `discovery_channel` (the IJC registry's own limits section already identifies rows 27–35 as builder-prior-knowledge). Never backfill `discovery_instrument` or `discovery_date` — that information is gone, and inventing it would reproduce the exact fabricated-precision failure the Syriac review caught.

### 3.2 `term` — the lexicon record

The record absorbs everything the current chunk carries, restructures the parts the research showed were stranded or leaking, and adds the diachronic/synchronic axes from brief §9.

| Field | Jobs | Notes |
|---|---|---|
| `term`, `aliases[]`, `original_script` | 4, 6 | Aliases parsed as today (glosses and transliterations separately) — an unusually good sparse-index field that the new index actually searches (§5.4) |
| `period_sense` ▲ | 1, 7, 6 | The term's meaning strictly inside this world's own conceptual universe. **This is what the Representative speaks from — Level 1 draws on `period_sense` only** |
| `prior_sense` ▲ | 7 | Classical/pre-existing sense where one exists, so the contrast is visible rather than assumed |
| `modern_sense` ▲ | 7, 6 | Current usage — what a participant's own use of the "same word" is checked against; formalizes what the anachronism bridge does live, as data |
| `conceptual_distance_note` ▲ | 7, 6 | Why the senses diverge despite sharing a word. Doubles as the input to `grounding_criterion`: a sharp then-vs-now gap is a high-criterion case by rule (§6.4). The named hazards this four-field block guards against are Barr's *illegitimate totality transfer* and the root fallacy (cite the terms and their standard target, Kittel's *TDNT*; doc 13 did not read Barr directly) |
| `semantic_domain` ▲ | 5 | The synchronic axis: the term's place among its neighbors, organized on the Louw & Nida *principle* (domain-based organization), not any single published instrument — no one lexicon covers six worlds' mixed Greek/Latin/Syriac vocabulary |
| `field_relations[]` ▲ | 5 | Typed, directional: `presupposes / presupposed-by / precondition-for / material-source-of / mechanism-behind / tension-with` — the vocabulary CiC's own best entries already reach for. This absorbs what "Ecological Function" holds as prose (genuine 26/38 times, read by nothing downstream) and what Related-Terms holds as an untyped list (structured, and it traveled). The reciprocity audit becomes a machine gate: every directional edge checked for its inverse (§4.2) |
| `quick_meaning` | 4, 6 | One sentence, **written in plain register, not the world's own distinctive phrasing** — this is a reachability index card, not voice material; see the parroting guard (§5.3). Authored for all 6 worlds; silently dropped by the parser for 4 of them (Alexandria, PAHC, Imperial-Juridical, Syriac — fenced front matter). Hieronymian's and Desert's both survive today only by formatting accident, not design — see §0 item 1 |
| `voice_surface` ▲ | 3 | What the Representative may actually say and how — emic register, first-person-plural framing, natural usage. Distinct from the scholarly body: **only this field and `quick_meaning` ever enter generation context.** `world_meaning` (below) feeds it but is not injected raw |
| `world_meaning` | 1, 2 | The full scholarly treatment — the current chunk's World Meaning, kept and grown. Lives in Levels 2/3 and the repository, never in the per-turn generation payload (this single routing change removes the largest live supply line of "documentation voice" — doc 08 §4.3) |
| `distortion_risk` / `modern_hearing` | 6, 7 | Kept — feeds Level 2 and the Facilitator, not the generation context |
| `retrieval` ▲ | 4 | Structured block replacing free-text conditions: `tier`, `retrieve_when[]` (participant-observable triggers only), `do_not_retrieve_when[]` (typed: `sense-disambiguation / anachronism-guard` — the two classes the runtime can actually evaluate), `force_llm_vote`. The two condition classes the runtime can never evaluate are retired deliberately: cross-world guards (each world has its own index; the invariant is structural) and Capsule-Core-state / Representative-internal-need conditions (replaced by the deterministic session exclusion set, §5.4). Empty is a typed null — never an em-dash |
| `key_sources` → `sources[]` | 1 | Per-claim, via the envelope; Author Gravity risk notes ride on the source link, not as injected prose |
| `contested_claim_ids[]` ▲ | 8 | Links to the contested-claim records this term is implicated in |

### 3.3 `story` — the story record

Two live failures shape two fields: the Amma Sarah saying told with the right content and the wrong occasion, and the leaking-jug story detached from Abba Moses. Both were organization failures — the information existed and had no field.

| Field | Jobs | Notes |
|---|---|---|
| `title`, `narrative_tier` | 1, 2 | Doc_09's tiers carried forward; tier justification is a required field, not prose |
| `text` | 2, 3 | The story itself, at full depth — depth stays and grows; it becomes reachable instead of stranded |
| `owner_figure_id` ▲ | 1, 3 | Whose story this is — a link to a `figure` record, so attribution is a lookup, not a memory. "The jug that leaked was Moses's own" becomes data |
| `attested_occasion` ▲ | 1, 3 | The occasion the sources actually attest ("elders coming to test her about being a woman") — so the right content can't be told on an invented occasion without contradicting a field |
| `tellable_as` ▲ | 3 | `scene / background-fact / allusion-only` — reconciling the prompt's licensing model with the data's tier model, which were never reconciled (the Papnoute whitelist blocked his three best-attested stories from ever being narrated) |
| `voice_surface` ▲ | 3 | How this world tells it, when it tells it |
| `retrieval` ▲ | 4 | As per term records |
| `sources[]`, tier-4 rule | 1 | Every element sourced or removed — carried forward |

### 3.4 `quote` — first-class, per doc 12

Plus the full envelope (§3.0) — including `sources[]`, `register`, and confidence.

| Field | Jobs | Notes |
|---|---|---|
| `text_original` | 1, 2 | The quote as attested, original language/script |
| `text_translation` | 2, 3, 6 | The rendering actually usable in Levels 1–2 and voice |
| `translation_used` | 1 | Source id of the translation edition — Chicago-completeness, per §3.1's `edition`/`translation` fields on the source itself |
| `locus` | 1 | Precise reference within the work |
| `speaker_or_author` | 1, 3 | Figure id — link to `figure` (§3.6), not a name string |
| `license` ▲ | 3 | `verbatim / paraphrase-only / do-not-voice`. The two genuine Brock quotations with page numbers, versus the unattributed paraphrase the Syriac registry warns against, become different `license` values instead of a verification note someone must reread |

### 3.5 `gravity` and `force` — with the missing fourth layer

`gravity`: the six-test results (each test's verdict its own field — the Doc_04 index table, now the record itself), `classification` (Primary/Supporting/Tensional/not-advanced, with "Candidates Considered and Not Advanced" kept as required records, not prose), `confidence_crosscheck`, and typed `interaction[]` edges: `reinforcing / competing / reshaping`, directional, with the Alexandria `C→X` type-change-over-time notation supported (`changes_to`, `at`).

`force`: the six-cell position and the three existing layers (Historical Event / World's Own Experience / Formation Impact), plus:

| Field | Jobs | Notes |
|---|---|---|
| `elaboration` ▲ (Layer 4) | 1, 5 | What changed in the world's own conditions as a result of living through this force — **including the explicit possibility that nothing changed** (`stasis: true` is a valid, complete answer). Modeled on Archer's morphogenetic sequence (conditioning → interaction → elaboration *or stasis*), borrowed as a documentation shape only — cite the cycle, don't adopt critical realism as a philosophy of history (doc 13's own caution, Medium-High confidence, source not read directly) |
| `connections[]` | 5 | Typed and directional, now including `world-response-reshapes` — the relationship Syriac's Connection 8 had to smuggle in as force-to-force with an apology attached, and HAL 3A-2's demoted observation, both get a legitimate home |

### 3.6 `figure` — named persons

Lightweight but load-bearing: `names[]` (with the in-world vs scholarly name distinction — emic/etic on the name itself), `narratable` (boolean — does this world hold any tellable story for this figure), `story_ids[]`, `sources[]`, `attribution_note`. Mar Yausep's grief list pointing at six names "the Representative is explicitly forbidden from narrating a story for," while the one narratable Persian martyrdom sat unbuilt into the prompt, becomes a query: *figures referenced in voice materials where `narratable = false` and no allusion-licensed story exists* — a machine gate, not a live-test discovery.

### 3.7 `contested_claim` — job 8's record

The one job (§2) that today is served only by a runtime mechanism (the over-settling screen) and a metric. Now a record:

| Field | Notes |
|---|---|
| `claim` | What the world actually holds, stated in the world's own terms |
| `held_against[]` | The challenges this world met and did not concede — with sources: what was actually contested in the record, by whom |
| `concedes` | What the world genuinely left unsettled or conceded — "our own record does not tell us" as data. The over-settling screen's six shapes are all detectable against this field |
| `pressure_response` | How this world characteristically responds when pushed here (argues from scripture? from practice? goes silent?) — voice-construction input |
| `divergence_partners[]` ▲ | Which other worlds genuinely diverge on this claim — this is what makes a *good table question* computable (§6.5, §9.4) and gives the Table Readiness Round its question bank (§4.4) |

This record feeds three consumers at once: the Representative's capacity to *enact* disagreement rather than state character (doc 10's deepest persona failure), the repair-initiation mechanism's held-position/concede decision (§6.3), and the measurement plan's held-position and concession rates (§10) — which need exactly this data to be computable.

### 3.8 `voice_profile` and `demonstration` — how a world sounds

**`voice_profile`** (one per world), plus the envelope:

| Field | Jobs | Notes |
|---|---|---|
| `speaking_model` ▲ | 3 | Setting, Participants, Ends, Act sequence, Key, Instrumentalities, Norms, Genre — the one surveyed framework whose theoretical unit is a speech community, not an individual |
| `trait_rubric[]` ▲ | 3 | 4–6 named traits per world, each with **situation-conditioned intensities** — the same tradition speaks differently about death than about food. Microsoft's TRAITS matrix, the most transferable structure doc 09 found |
| `register_determination` | 3, 7 | The world's register call and its evidence — feeds `register` (§3.0) at the per-record level |
| `native_measure` ▲ | 3 | Length discipline as data, not convention (Desert's 60 words, HAL's 180) |
| `reading_level_check` | 6 | The floor a profile inherits, not restates — see §5.6 Level 2 for the actual FK/FRE mechanics |

**`demonstration`** records, plus the envelope:

| Field | Jobs | Notes |
|---|---|---|
| `dialogue` | 3 | The calibration exchange itself, using the `{{random_user}}` convention so it reads as *a* conversation, never *the* conversation |
| `trait_scores` ▲ | 3 | Judged against the world's `trait_rubric` — the rubric is the deliverable; examples are calibration, the one unanimous finding across every surveyed framework |
| `situation_tag` ▲ | 3 | Which high-intensity situation this demonstration covers — "how many" is answered by rubric coverage, reviewed for **diversity against parroting** (doc 09's PersonaChat warning), typically landing in the 3–5 range Anthropic's own guidance suggests, but the count is a consequence of coverage, not a target |

**Negative constraints:** the rubric carries paired trait vocabulary (traits we embody / traits we avoid) as an author- and reviewer-facing instrument. But per the brief's own caution — Desert's *soft* anti-fabrication instruction failed on retest while categorical guards held — fabrication-class guards specifically remain direct, categorical model input. Rubric for style; categorical instruction for safety-class prohibitions. Both, on purpose, with the line between them stated.

### 3.9 Views — generated, versioned, never hand-synced

Every deployment artifact becomes a named view spec over the record set:

| View | Replaces | Notes |
|---|---|---|
| Permanent Prompt | hand-authored prompt | Assembled per §5; **versioned** — a regenerated prompt is a new version that must pass continuity regression (same probes, old vs new, diff the voice) before reaching a returning participant (doc 10's Replika lesson) |
| Capsule Core / Priority Layer / retrieval chunks | hand-authored tiers | The three-tier progressive-disclosure architecture is kept exactly — it is convergent with three independent industry patterns and ordered by change frequency, which is the cache-correct ordering |
| Lexicon/story/force indexes | companion spreadsheets | The entire "derived index view not regenerated" defect class (the single most recurrent review failure across all six worlds) ceases to exist: indexes are queries |
| World Facilitation Brief | the least-finished artifact in the pipeline | Generated from `voice_profile`, `contested_claim.divergence_partners`, gravities, forces, and per-world cautions. What still needs a human is Section B's judgment calls — authored *as records* (pairing guidance with evidence links), early in the build, not as an end-of-sequence document (§4.5) |
| Repository + Levels 1–3 | (new) | §5.6 |
| Operational parameters | numbers restated inline across documents | One canonical parameters file (`table_size_ceiling`, turn floors/ceilings, token budgets, cost thresholds, drift-signal count…), everything else references it. The table-size ceiling becomes one number in one place with per-phase overrides — resolving three live values across current governance documents. The drift-signal count (17 emitted today — 10 monitor + anachronism alias + over_settling + 5 table-level; verified in code) lives here too |

### 3.10 `world_core` — job 7's missing home, part one

One record per world. Referenced throughout (§5.1's "the world's own ground" segment, §6.6's per-seated-world anachronism logic) but never previously specified — this closes that gap.

| Field | Jobs | Notes |
|---|---|---|
| `time_window` ▲ | 7 | Structured start/end era for this world's own historical setting — what "native to the other's window" (§6.6) actually checks against |
| `horizon` ▲ | 7, 3 | The world's geographic and cultural scope — bounds what a Representative can plausibly have encountered |
| `formation_logic` | 1, 3 | Prose: the underlying account of what shaped this world into what it is — the always-present "world's own ground" material in §5.1's assembly, rendered emic |
| `gravities[]` | 5 | Pointer to this world's `gravity` records (§3.5) — `world_core` doesn't duplicate gravity content, it anchors the world-level context those records are read into |

### 3.11 `modern_term` — job 7's missing home, part two

Facilitator-owned (§3.0's `world_id: facilitator`), one record per bridgeable modern term. Named twice in §6.6 prose and used as the structural fix for the "what is faith" bug class in §9.4, but never given a field table until now.

| Field | Jobs | Notes |
|---|---|---|
| `term` | 6, 7 | The modern word or phrase the bridge watches for |
| `display_phrases[]` | 7 | Kept as today — the surface forms the classifier currently matches against |
| `distinguishing_claim` ▲ | 7 | The specific claim that separates a narrow, period-specific sense (e.g. *sola fide*) from the universal root word it's built on — the field today's classifier never sees, since it sees only `display_phrases`. This is §9.4's structural fix: "what is faith" is classifiable as NONE because no distinguishing formula is present, not by a hand-written example for one term |
| `native_subject_map` ▲ | 7 | Per-world map of the underlying subject's native record — lets the bridge answer per seated world rather than against the first-seated world only (§6.6) |

**The confirmed-gloss list** is Facilitator-owned data of the same kind, not a separate schema record type: each entry is `{world_term, approved_gloss, exact_wording_required: true}`, curated with the same discipline as today's whitelist. Small enough that it lives as a keyed list within the parameters/Facilitator-asset store (§3.9) rather than as its own `record_type` — named here so "record data" (§2, §7) points at something specific instead of an implied schema that doesn't exist.

### 3.12 `search_record` — the source-discovery record, per deliverable 1

One per world, STARLITE-shaped (adopted from doc 14, §4.3). Specified here as part of the schema deliverable; §4.3 covers the process this record supports.

| Field | Jobs | Notes |
|---|---|---|
| `sampling_strategy` ▲ | 1 | Declared purposive, not comprehensive — Booth's standard, the one CiC should be held to |
| `types_sought` ▲ | 1 | What kinds of sources the search targeted |
| `approaches` ▲ | 1 | Derived from `discovery_channel` counts on the world's `source` records — a view, not new authoring work |
| `years_searched` ▲ | 1 | The range of publication years actually searched — needed precisely because the Boundary Check rightly refuses to filter sources *by* publication date, so this is the only place the search's own window is recorded |
| `languages_searched` ▲ | 1 | Languages of scholarship searched — a Syriac world searched only in English has a coverage limit nothing else records |
| `inclusion_exclusions` ▲ | 1 | Already best-in-class in CiC's current practice; formalized here |
| `terms_tried[]` ▲ | 1 | Including terms that returned nothing — where the search record and the Missing Voices duty meet |
| `instruments[]` ▲ | 1 | Named search instruments used (BIBP, L'Année philologique, syri.ac, etc. — per §4.3) |

---

## 4. Deliverable 3 — Build process: templates, gates, and the Table Readiness Round

### 4.1 What actually changes about building a world

The step sequence does not reorder. Doc 17 checked four fields and none recommends reordering world → representative → table; the firewall (CO-003, Article 3) stays hard. What changes is what a "document" is and what a "gate" is:

- **Steps produce records, not prose-plus-companions.** Doc_02 populates `source` records; Doc_03/06 populate `term` records; Doc_04 `gravity`; Doc_08 `force`; Doc_09 `story`/`quote`/`figure`. Each step's narrative synthesis survives as the step's *analysis document* — prose arguing from the records, referencing them by id — but the facts live in the records. A reviewer checks the analysis for judgment and the machine checks the records for consistency.
- **The lens work (Doc_05/07) keeps its own governing fix:** the lens set is standardized on Smart's seven dimensions as the fixed spine that is always *asked*, with per-world yield stated as a finding (a thin dimension is a result, not a coverage failure — the same discipline Doc_04 already applies to candidates not advanced). Material Culture is promoted to required; an ethical/legal lens is added (the one Smart dimension with no CiC lens — for a portfolio containing Imperial-Juridical Christianity, a real omission); Boundary Structures and Formation Logic stay as CiC's own two additions, named as additions. This resolves the template-vs-Framework fixed-vs-derived contradiction without either side losing.
- **The lens synthesis reaches the Representative by design.** The Article 3 firewall stays — but the firewall governs *when* Representative-construction work happens, not *whether relational insight survives*. The "what the cross-lens synthesis gives the Representative" content that Alexandria's build stripped on Article 3 grounds gets a home that is legal on both sides of the wall: it lands in `field_relations`, `contested_claim`, and `voice_profile` inputs — world-side records, written at world-build time, consumed at Step 10. Nothing Representative-shaped is authored before Step 10; everything the Representative will need is queryable when Step 10 arrives.

### 4.2 Machine gates — checks, not rules

CO-020's lesson is quantified in the corpus: a written-only standing rule against self-certified dismissal was adopted at the second world built and the identical pattern recurred in the third, fourth, and three more times in the sixth. **A written rule alone has a demonstrated failure rate; this design converts every gate that can be a program into a program**, and requires a saved artifact for every gate that can't:

| Gate | Kind | What it catches (with the historical defect it would have caught) |
|---|---|---|
| Referential integrity | machine | Every `sources[]` entry resolves; every relation target exists; every gravity's force links resolve (the Checkpoint rule, executed instead of asserted) |
| Reciprocity | machine | Every directional relation — `relations[]`, `field_relations[]`, `interaction[]`, and `connections[]` alike (§3.0) — has its inverse or an explicit `one-directional` marker (Alexandria's reciprocity sheet that "falsely reported non-mutual pairs as reciprocal" — a QC deliverable lying about its own output — becomes impossible; the QC *is* the query) |
| Field completion | machine | Required fields per tier populated, per §11's standard (the 7%–100% Author-Gravity variance — caught at build, not by a cross-world audit a week later) |
| Quote fidelity | machine-assisted | Every `quote.text` verified against `translation_used` at entry, verification recorded (the fabricated Jerome gloss circulating in AI search summaries — the check is "pull from the critical edition," now a field the gate demands) |
| Figure narratability | machine | No voice material references a figure with `narratable=false` unless allusion-licensed (Simeon bar Sabbae / grief-list defect) |
| Readability | machine | Flesch-Kincaid 8–10 / FRE ≥ 60 on every `plain_explanation` and on the assembled prompt's prose — **computed, not manually checked**; today this floor has zero runtime implementation anywhere (verified), and it is a deterministic formula |
| Retrieval regression | machine | The §5.4 harness runs against the world's golden set before freeze; `do_not_retrieve_when` violations = 0 |
| Anti-parroting | machine-assisted | N-gram overlap between assembled prompt materials and validation-probe outputs, per §5.3 |
| Content truth, register, world honesty | human + adversarial review | What review is *for* once synchronization stops consuming it. Every round saved as an artifact; no self-certified dismissals (CO-020/CO-022 carried forward — now with much less surface to police) |

### 4.3 Source discovery — the prospective standard

Adopted from doc 14, as specified there (it is the best-worked-out piece of the corpus):

1. **A `search_record` per world** (deliverable 1's search-strategy record, specified in §3.12): STARLITE-shaped, adopted from doc 14 as specified there — it is the best-worked-out piece of the corpus.
2. **A field-bibliography sweep as a required Step 2 gate:** BIBP and L'Année philologique for patristics; Brock's classified bibliography via syri.ac for Syriac; Bibliographia Iuris Synodalis Antiqui for conciliar material; Biblindex for scriptural engagement; the relevant Oxford Bibliographies article as the current-scholarship check; CPG/CPL as an author-corpus completeness checklist. Deliverable: the short list of works the sweep surfaced that the registry did not hold, each dispositioned. **That list is CiC's PRISMA flow diagram.**
3. **A supply-side saturation criterion for Step 2** — the project's own Lexicon Development Framework sentence, lifted and adapted: complete when the named bibliographies are swept, all six evidence streams searched rather than assessed, backward snowballing run on the highest-weight Native rows, and continued search produces diminishing returns *stated with examples of what the last unproductive searches turned up*. This replaces "every source currently known to the builder" — a possession test satisfiable by a builder who looked nowhere.
4. **Reviewer-side coverage checks:** the ten-item relative-recall test (reviewer names ten works a specialist would expect, from an instrument independent of the build; recall = found/10, logged — doc 14 rates the method's source Medium; the practice is cheap regardless), and the PRESS question added verbatim to Doc_02 review: *"Name up to three sources you would expect a bibliography of this world to contain that this registry does not hold. If you can name none, say so explicitly."*
5. **W1 §1.8 generalized:** the single-source dependency audit becomes a derived view (source × downstream artifact concentration counts), visible at Step 2 instead of discovered at Step 9 in one world of six.

This is the brief's §8-objective-1 "prospective, not just disciplined" standard: all five items exist before the next world is built, none is a reaction to that world's own defects.

### 4.4 The Table Readiness Round — Phase Eight, with a way back

Adopted from doc 17 recommendation 1, with the brief's own additions:

- **What it is:** before a world freezes its Representative, seat the newly-built Representative with one already-live Representative from a different world, on one question where the two worlds genuinely diverge — drawn from `contested_claim.divergence_partners`, so the question bank is data, not improvisation ("what is faith" would not qualify; "what is salvation in your world" — PART II's actual question — would).
- **What it grades:** cross-world vocabulary borrowing (as *entrainment that overwrites a world's own sense*, not mere word appearance — §6.5); anachronistic reach under multi-voice pressure (the "schoolmen" class of defect, which no solo probe ever caught); and whether the world holds its own position rather than converging (scored against its `contested_claim` records — held-position and concession rates, the same two numbers §10 tracks live).
- **The backward path, explicitly:** a Table Readiness failure is classified at the moment it is found as (a) a runtime/Facilitator matter, (b) a per-world record defect — fix the records, regenerate the views, rerun; or (c) a framework/template change, with (b) and (c) carrying CO-022's propagation discipline. The per-world loop stops being strictly forward-only — the Construction Framework's own "the workflow is not strictly linear" finally gets a mechanism.
- **Two one-line ordering fixes ride along** (doc 17 rec 2): RCF Phase Seven ("Encounter Ecology Mapping"), whose own text begins "Before Representative construction begins," moves to where its text says it runs — a Step 9 deliverable. And the Freeze Criteria split into **world-freeze** criteria and **representative-freeze** criteria, so "encounter testing is successful" stops being unsatisfiable at the point it is stated. §11's completion standard is written around this split; deliverable 3's gates and deliverable 10's standard are one system, not two competing definitions of "frozen."

### 4.5 End-of-sequence attrition — designed against, not caught

The World Facilitation Brief failed by *position* (a hand-authored artifact at the end of a 17-step sequence), not by synchronization. Three moves: it becomes a generated view (§3.9); its genuinely human parts (pairing guidance, cautions) are authored as records during Steps 4–8 while the material is live in the builder's hands, not recalled at Phase Six; and §11 makes its render a freeze gate, so a world without one cannot be called finished. The same pattern applies to any future artifact that would otherwise be hand-authored last.

---

## 5. Deliverable 4 — Representative construction as context engineering

### 5.1 The assembly, specified

A Permanent Prompt stops being hand-authored prose and becomes a **specified assembly** — every part named, sourced from records, carrying `eviction_priority` and `cache_stability`, ordered by change frequency (static → session → turn), which is both the cache-correct and the quality-correct ordering:

| Segment | Contents (record sources) | Cache | Notes |
|---|---|---|---|
| **Identity & register** | `voice_profile`: the world's name, the "I represent the world, then 'we'" opening discipline, trait rubric summary, native measure, register determination | static | The single self-identifying line stays the only licensed exception to "we" |
| **The world's own ground** | Capsule-Core view: gravities (Primary first), the world's time-window and horizon, formation logic — rendered emic, from `period_sense`/`voice_surface` fields only | static | 3,000–5,000 tokens, as today |
| **Contestation** | `contested_claim` renders: what we hold when pushed, what we concede, how we characteristically respond | static | New as always-present material — this is what lets the voice *enact* its character under disagreement instead of stating it (doc 10's headline finding); doc 13's attention-decay note argues identity-critical instruction also lands in the post-history slot, per below |
| **Grounding anchor** | The approved-source anchoring paragraph, generated from `sources[]` where `evidentiary_weight = load-bearing` and `attribution_status = genuine` | static | CO-016's mechanism, now derived — it can never again exist for five worlds only as an unwritten convention |
| **Quick-reach layer** | Every term's `quick_meaning` + id for the seated world | static | The §5.4 cost-and-quality move: all terms reachable every turn, in plain register (parroting guard), at cache-read rates |
| **Demonstrations** | `demonstration` records selected against the rubric | static | Pruned first under token pressure (low eviction rank), per the universal permanent-vs-evicted split |
| **Categorical guards** | Anti-fabrication (absolute form), safety-class prohibitions | static + **post-history** | Position as a field property: the guards that must survive attention decay ride closest to generation (doc 09's `post_history_instructions` finding) |
| **Session layer** | Priority-Layer view; table composition; other seated worlds' term lists (for divergence, §6.5) | session | Loaded once, held all session |
| **Turn layer** | Retrieved `voice_surface` bodies (deep material only, when the participant actually goes deep); `pending_guidance` queue head; reactive-turn guidance | turn | The only uncached segment, kept deliberately small |

**What no longer enters generation context, ever:** `world_meaning` scholarly bodies, `key_sources` apparatus, Author-Gravity notes, gravity codes, "Modern Hearing" analysis. All of it remains one hop away in Levels 2/3 and the audit trail. (Resolved registry rows themselves — including verification-note language like "confirmed directly against publisher page" — are already citation-chip-only today, attached via `resolve_references(...)` rather than serialized into the prompt; that part isn't a new removal.) What *is* new: in the one real two-world session on disk, the chunk's own `## Key Sources` section — carrying language like "rests on later hagiographic attribution" plus raw `(Source Registry #...)` pointers — was serialized into the generation context twice in four turns. Under this design that section is removed from voice materials, and the participant-facing citation chip (which already exists for the registry side) becomes the only place that apparatus surfaces. This is the same decision as the cost fix in §8, made once — smaller than it first looked, but real.

### 5.2 Voice as versioned artifact

Every assembled prompt version is retained; a regeneration (new records, changed view spec, changed guidance) produces a version that must pass **continuity regression** — the world's validation probe set run against old and new, voice diffed — before it reaches returning participants. A prompt-guidance change alters personality, not just formatting; users reject an "improved" personality when their relationship was with the specific voice (doc 10: Replika, and a 2026 rollout backlash, independently).

### 5.3 The parroting guard — named, mechanical, and blocking

Doc 09's single most important verdict: original, verbatim personas produce models that "unwittingly repeat profile information either verbatim or with significant word overlap," and a world's own distinctive vocabulary in the always-present slot is the highest-parroting-risk configuration there is. §3.2's four-field sense block and §5.1's quick-reach layer both expand exactly that surface, so the guard is designed with them, not after them:

1. **Register separation by construction:** `quick_meaning` (always present) is plain-register pointer text; `voice_surface` (emic, distinctive) is retrieved only when the term is genuinely in play; demonstrations are diversity-reviewed. The always-present surface is deliberately the *least* parrotable form of each record.
2. **A parroting metric:** n-gram overlap between assembled prompt material and generated turns, measured across the validation battery and sampled live turns. (PersonaChat's revised-persona discipline, operationalized; RAGs-to-Riches used the same overlap measure in the other direction.) Baseline first, threshold after — same rule as every other new metric (§10).
3. **A validation probe category:** probes that bait the voice into reciting its own materials (ask "what is qyama?" five ways), graded for paraphrase-vs-recital against the rubric.
4. **R7 is contingent on this guard** — the quick-reach layer does not ship ahead of the metric existing. (Doc 15 attached the same condition; it is kept.)

### 5.4 Retrieval, rebuilt — harness first

Adopted from doc 15, order preserved deliberately (measure → fix index → cheap mechanical fixes → ranking → query):

- **R0 (before anything else):** the ID-based evaluation harness — 12–20 golden cases per world across doc 15's six case categories (verbatim-term, thematic, de-dup, negative-condition, reactive-turn, cross-world isolation), computed from chunk IDs against the audit trail CiC already logs. No judge model, no API cost, deterministic, committed baseline. **Run against the current system before any change ships**, so every claim in this section becomes falsifiable. (~1 day of code, ~1 day per world of case authoring.)
- **R1/R2:** embed the *retrieval surface* (`term` + aliases + related + `retrieve_when` + `quick_meaning` — the fields authors actually write for retrieval), not the chunk body; keep the body as payload. Today the embedding model never sees `Retrieve-When` at all and truncates roughly 85% of an Alexandria chunk (verified mechanism; Medium-confidence exact cutoff — R2's first step is to tokenize all 104 chunks and publish the real distribution). Then, only if needed, swap the embedding model against R0's numbers.
- **R3/R4/R5:** hybrid BM25 + dense with weighted reciprocal-rank fusion (the participant who says *qyama* finally has a lexical path to `syrlex002`); an ID-keyed session exclusion set plus MMR replacing both broken substring de-dup guards (this also deterministically replaces the entire "Capsule-Core has already surfaced this" condition class); sentinel-value and relevance-floor one-liners.
- **R6:** a local CPU cross-encoder replaces the batched LLM relevance vote — the Tier-2/3 batch-dilution failure the code has fought three times becomes structurally impossible, and ~2 Haiku calls per world per turn leave the latency path. One Haiku call remains, invoked only for candidates carrying a genuinely evaluable negative condition.
- **R7:** the quick-reach layer itself — every world's `quick_meaning` set moves into the assembled prompt's cached prefix (§5.1) instead of being retrieved per turn, so every term is reachable every turn at cache-read rates. This is the document's own headline change (§1 item 6, §8's largest cost row); doc 15 attaches one condition, kept here: **contingent on the anti-parroting metric (§5.3) existing first** — R7 does not ship ahead of the check that confirms it isn't being recited.
- **R8:** one-hop `field_relations` traversal as candidate expansion (~10 lines against metadata already in the index). GraphRAG's platform is explicitly rejected: CiC's graph is hand-authored and reciprocity-audited; paying an LLM to extract a worse one buys nothing, and global search's 40k-token prompts and generated summaries run against both the cost requirement and the register-leak finding.
- **R9:** conversational query rewriting — one Haiku call producing a standalone, world-appropriate retrieval query, replacing both the reactive-turn concatenation (another world's full turn currently drives this world's vector search) and the bridge's query replacement (a false-positive bridge currently searches the world's lexicon against text written for no world in particular).

### 5.5 What Step 10 looks like end-to-end

Ecology assessment and formation calibration become *reads* of the record set with a written finding; voice construction produces the `voice_profile` and `demonstration` records; artifact construction is a **render** plus human review of the rendered whole; boundary testing keeps RCF Part Eight's eight probe categories (plus Register-Fidelity, which today lives only in the Construction Notes Template, not RCF Part Eight itself — Appendix B) plus the new parroting and pushback categories; V7.4's Validation Protocol Rigor (two independent trials, held-out probes, fresh-context generation, blind grading) applies to all of it; then the Table Readiness Round (§4.4); then representative-freeze per §11. The 3–5-terms-in-a-prompt bottleneck is gone — the prompt names the *organizing* vocabulary while the quick-reach layer carries all of it.

### 5.6 Deliverable 2 — Three-level access and the browsable repository

All four surfaces are views over the same records — none is separately maintained, so none can drift:

| Level | Contents (field-level, per the brief's spec) | Mechanics |
|---|---|---|
| **Level 1 — the conversation** | `period_sense` / `voice_surface` only. Never `modern_sense`, never raw citation apparatus. Confirmed glosses render from the gloss list (a Facilitator asset, per the standing glossary-ownership rule) | The conversation itself; citation chips link downward |
| **Level 2 — on-request plain explanation** | `plain_explanation` render: `period_sense` stated plainly + a plain-language confidence statement (the constitutional five-level vocabulary, rendered in ordinary words) + `conceptual_distance_note` **wherever a then-vs-now gap exists** — the exact place a participant needs to be told a word meant something different then | Generated at the reading floor and **machine-checked**: FK 8–10 / FRE ≥ 60, computed at render time (sentence structure only, never vocabulary — RCF Part Five's own line). Note the floor's constitutional status precisely: Article 30 itself carries no reading-level number; the numeric floor lives in RCF V3.2 Part Five and Final Assembly 5c. This design keeps the number in the operational-parameters file and has both documents point at it. Same content for every participant; registers never gate access |
| **Level 3 — full scholarly apparatus** | The complete record: attribution status, edition and translation, evidentiary weight, Author Gravity (an existing CiC strength — doc 12's own baseline, not an addition), transmission path, field state, the full source rows, the retrieval audit for this conversation | Presented as a scaffold, not a field dump: an Observe → Reflect → Question layer sits on top (the LC model — doc 12 claims a stated design intent for it, not a tested shape; adopted as a starting shape to be tested, said plainly), with the full record reachable beneath. The `/audit` endpoint's positive apparatus is the Level 3 backbone for *this conversation's* claims — it already exists; this gives it a participant-facing face |
| **Repository** | Browse/search across worlds with no conversation running: by domain, by source, by figure, by contested claim; every record renders its Level 2 and Level 3 faces; `display_permitted` and rights fields gate what text is shown publicly | This is §8-objective-3's double duty: the same records the Representative speaks from, browsable as a real scholarly library. FAIR follows nearly for free: stable ids, machine-readable export (`sources.json` per world), external identifiers, stated rights — plus the one-page Conformance and Deviation Statement (doc 12 Tier 3) and, when Mark wants outside eyes, *Reviews in Digital Humanities* accepts projects mid-development |

All three levels always present, none ever gated by participant type — Article 30, unchanged, now with the per-level content specified instead of implied.

---

## 6. Deliverable 5 — Facilitator governance and table dynamics

### 6.0 The frame

The Facilitator's jobs are already well named by governance: bridging a world and a modern participant, translating without flattening, holding safety and rigor, and deciding who speaks next and why. What the research adds is a vocabulary that makes the design checkable — the Facilitator is the **etic** voice and the Representative the **emic** voice; the anachronism bridge is a governed etic intervention on an emic turn — and three measured findings that turn "needs design attention" into specific mechanisms. The near-silent-room conviction (Facilitator Governance §12: "if the Facilitator is present in the middle of a rich encounter, the governance is too loud") is preserved throughout: every mechanism below either acts before a voice speaks, rides inside a Representative's own turn, or is delivered as a private directive. None adds a spoken Facilitator turn to a healthy conversation.

### 6.1 One governance engine, both endpoints

The reason the plain endpoint has none of the streaming endpoint's dominance/convergence/vocabulary/length/question-stacking checks is not a decision — it is that the checks are hand-wired into one endpoint's body. Governance is extracted to a single layer both paths traverse (RavenClaw's decoupling pattern: error handling lives in the engine, not the dialog logic), which makes the brief's "unify or account for both" a non-question and means any future endpoint inherits governance by construction. The intercept chain (frame-breaker → relational safety → epistemology bridge → modern-term bridge → repair classifier, §6.3) runs in this layer, in this order — safety intercepts always ahead of everything else, exactly as today.

### 6.2 Turn selection: enforce Rule 1 first, then judge

1. **Direct-address detection runs before the holistic selector.** A cheap check over the previous turn: did it name or clearly designate a specific world (participant → Representative, or Representative → Representative as a direct question)? If yes and the designated party is eligible — select them, without an LLM call. This enforces Facilitator Governance §8 Rule 1, which the streaming path currently cannot honor; it is also the multi-agent literature's strongest measured turn-taking result (p<0.001 against both fixed rotation and pure self-selection, doc 16 §3b). It is *also* a cost saving: the selector call disappears on exactly the turns where selection is already determined.
2. **The two-turn floor becomes a per-conversation contract, not a per-turn one.** The multi-world promise ("more than one voice heard") is guaranteed across the session: a directly-addressed question gets a single-voice answer, and the Facilitator draws the second world in on a later turn where it genuinely serves — which is what governance Rule 4 already describes. `MIN_MULTI_WORLD_TURNS` as a hard per-round floor is retired.
3. **The holistic selector stays for open-to-the-table questions** — it operates in the one regime where LLM next-speaker judgment is genuinely strong (better than human F1 on the published benchmark) — with two upgrades: the transcript window moves from a naive last-10-lines slice to block truncation with a stable prefix (the cached-prefix rule, and the long-context resource the selector's own strength depends on), and the selector's currently-discarded `REASON:` line becomes a **private directive** to the selected speaker ("you are being called on because Chloe named your world's handling of X — engage that specifically"). That is the moderation literature's *Confronting* act — the one act that turns parallel monologues into an exchange — delivered without the room ever acquiring a voice.
4. **Question-stacking is rebuilt on outstanding first-pair-parts.** The state tracks unanswered direct questions; the check fires on genuinely unanswered ones rather than on turns ending in "?" — which also ends the internal contradiction where `REACTIVE_TURN_GUIDANCE`'s "Ask, Don't Just Answer" licenses exactly the act the current check penalizes.
5. **Deferred, deliberately:** sealed-bid self-selection (each Representative computes a private interest scalar; only the scalar crosses the boundary — content-preserving by construction) is recorded as a future option, not built now: it adds N Haiku calls per turn for a signal the two mechanisms above mostly supply.

### 6.3 Pushback: tell a grounded correction from an ungrounded one

The model this system runs has a measured tendency to reverse previously-correct answers under bare pushback ("are you sure?") — doc 16 reports roughly a quarter of correct answers reversed, a figure carried at Medium confidence, but the vulnerability it names is the exact structural risk to CiC's core conviction: a world talked out of its own position by nothing but social pressure. The mirror failure — resisting all correction — would be worse, because a fabrication that survives every challenge is the cardinal sin the fabrication guard exists for. So the design never instructs "resist pushback"; it distinguishes:

- **A repair-initiation classifier** joins the intercept chain (same architecture as the other five: Haiku, narrow, fails open to substantive). It answers one question about the participant's turn: is this a repair initiation on a Representative's prior claim — open request, restricted request, or restricted offer?
- **On a hit, the direction is decided by evidence, not policy:** reuse `_gather_world_evidence` (the same machinery the two adjudicators already share) to ask whether the challenged claim is supported by the world's own record. **Supported → hold the position and say why, from inside the world** — job 8 enacted, with the `contested_claim` record supplying *how this world characteristically holds it*. **Unsupported → concede plainly** — the fabrication guard working as designed. The guidance delivered is selected from a small closed set of strategies, never composed free-form: the one recorded incident of a reroot model *inventing sources to fix an over-confidence flag* is the standing argument for selecting rather than composing corrections.
- The two adjudicators keep their deliberately opposite biases exactly as built (§7). The one change inside them: the FABRICATED verdict splits into **intrinsic** (contradicts the world's own record — settled, severe) and **extrinsic** (unsupported by what was retrieved — provisional), the distinction the adjudicator's own prompt already draws in prose and discards in its output format. The two verdicts get different severities in the priority ordering and different corrective strategies, since "you contradicted your own capsule" and "nothing we retrieved supports that" are different repairs.

### 6.4 Grounding: one positive-evidence mechanism, riding inside the turn

Every drift signal in the system is negative evidence — trouble detection — and the founding grounding-theory result is that negative evidence alone is not enough to trust that two parties understood each other. The fix is one mechanism, sited where four independent research areas converge:

- **Per-record grounding criteria, derived not authored** (§3.0): a term whose senses diverge sharply then-vs-now, a contested claim, an `emic-unavailable` absence — high criterion. Ordinary content — low. No new authoring burden.
- **When a high-criterion record is in play and the participant's next turn shows no positive evidence of understanding** (no acknowledgment, no relevant next contribution), the *next Representative or Facilitator turn opens with a restricted offer* — a candidate understanding put forward for confirmation ("You asked about monks — what we kept was a covenant sworn in the town, not a withdrawal from it. Is that the thing you're asking after?"). Roughly 86% of real human other-initiated repair takes exactly this form; the one evaluated grounding architecture prepends exactly this and improved response appropriateness in controlled tests (p<0.01/p<0.05); and because it rides inside the answering turn, the near-silent room is preserved.
- This is also the modern-term bridge's repair path (§6.6): a bridge misfire becomes correctable in one turn instead of invisibly steering the round.

### 6.5 The table-level checks, re-founded

- **`check_convergence` splits into its two unrelated halves.** Vocabulary blending is *lexical entrainment* — the most robust finding about how humans in conversation actually behave, suppressed here deliberately and for a stated reason. The check's real target is narrower: **a conceptual pact that overwrites a world's own sense** — detected against the term's own `period_sense`, which is what the code's own best instinct (the Syriac "Mar" pre-filter design) already reached for. "Manufactured resolution" is a different phenomenon (group-level sycophancy; the persona-enactment failure) and becomes its own check, scored against the seated worlds' `contested_claim.divergence_partners`: if the worlds genuinely diverge here and the round is converging on a tidy synthesis, flag it. The positive framing goes to the prompt layer: Representatives are instructed in *divergence* — actively maintaining distinctive vocabulary as identity — a documented communicative act, not merely the absence of drift.
- **Dominance keeps its cumulative word-share backstop and gains the floor-allocation view** (a world selected every round can dominate at 40% of the words); mode-dominance gets its first mechanism — the six modes the governance document already enumerates (precision, argument, certainty, abstraction, image, silence) become a per-round register classification, held against the participant's discerned register-of-wound, with the correction being the selector calling the absent register: a selection input, not a spoken intervention.
- **The closing-speaker rule:** whoever speaks last gains unearned authority to characterize consensus (the roundtable's own reviewer finding). Multi-world rounds either rotate closing order or the Facilitator delivers any closing summary. One sentence of governance; §9.2 shows exactly where it would have fired.
- **A misattribution signal is added** ("Name What They Actually Said" is currently instructed but never verified): when a Representative characterizes another's position, a cheap check against the named world's actual prior turn. This is the grounding gap's Representative-to-Representative face, and no current signal covers it.
- **`pending_guidance` becomes a per-world priority queue behind a gate.** Today five table checks and the drift loop all write one string per world, last-writer-wins — which structurally deprioritizes exactly the multi-party signals, purely by statement order in a background block. One ordering (the existing priority list, extended to the table signals) governs both bottlenecks. The signal-type declaration lists all emitted types — today two of the most governance-critical (`over_settling`, `self_narration`) are emitted but undeclared.

### 6.6 The two boundaries, corrected as stated

- **Facilitator turns enter the public transcript.** The constitutional line is "only spoken words cross" — the Facilitator's words are spoken; excluding them was never what the boundary required, and it silently breaks the bridge's own repair mechanism (a Representative currently sees answers to questions that no longer exist in the record). The bridge's reframed question is persisted as a distinct event type all Representatives read as the question actually asked — which also ends the current asymmetry where world 1 answers the reframe while worlds 2..n answer the raw modern-term question, so the table stops giving two treatments of one question depending on speaking order.
- **The modern-term bridge gets the field it has been missing:** `distinguishing_claim` — the thing that separates asking about *sola fide* from asking about faith — as first-class data per term, passed to the classifier (today the classifier sees only display phrases, in which the universal root word appears four times and the distinguishing feature nowhere). Anachronism is evaluated against **every seated world**, not the first-seated one — at a PAHC + Imperial-Juridical table, "the Trinity" is later vocabulary for one world and native to the other's window, and the bridge should say exactly that, which is a better formation moment than either wrong answer. Each modern term also carries a `native_subject_map`: the underlying subject's native record per world (a house-church participant asking whether Christ is really present in the bread is asking a *native* question with a Tier-1 answer, not a 1215 anachronism).
- **The isolation boundary is restated as a deliberate constraint specification** — CiC selects {reviewability, sequentiality} on purpose, and the known costs of that selection (expensive speaker change; prevention-before-sending as the only affordable repair) are named in governance rather than discovered. One consequence is surfaced as an open product decision rather than decided here (§12): streaming means the two most expensive quality mechanisms — the adjudicators — can only annotate, never prevent. A middle path exists (buffer only high-risk turns: first-time claims on high-criterion records, low-confidence material; stream the rest), and doc 10's own verification *refuted* the claim that response latency is a first-order naturalness driver, so the case for full streaming is product intuition, honestly labeled.

### 6.7 Conversation state becomes an event log

The mutable in-memory conversation state (with its hand-patched read-modify-write race) is replaced by an append-only event log; state is a derived projection. This is the same discipline the Source Registry already chose — never renumber, never delete — applied to the conversation layer: the race disappears; the audit endpoint gains persistence and real temporal query (today it is unauthenticated and dies with the process — it becomes authenticated and durable, since it is Level 3's backbone for live conversations); corrections become events that reference what they correct; and the public transcript finally gets a specified data shape, which neither governing document supplies today (verified): an ordered log of spoken events — speaker, text, designated addressee where one exists, bridge-reframe events included — from which each Representative's view is a deterministic render.

---

## 7. Deliverable 6 — What is preserved from brief §4, and what is served differently

| §4 purpose (non-negotiable) | Verdict | How it is served in this design |
|---|---|---|
| **The world's collective voice, never an invented individual** | **Preserved, strengthened** | Pronoun discipline and adversarial testing carry forward unchanged ("I represent the world, then 'we' from then on" stays the standing rule). Strengthened: the voice is assembled from records that are themselves collective (the SPEAKING model's unit is a speech community; the persona-fact dimensions are adapted to "we"), and the `figure` record keeps named individuals as *persons the world remembers*, never as the speaker |
| **No claim spoken without a traceable source and honest confidence** | **Preserved, generalized** | The Source Registry pattern generalizes to every record type — per-claim `sources[]` with licensing, three-axis confidence, the Checkpoint rule as a machine gate. The registry's own honest-scope note still governs: a registry classifies proposed candidates; the *wall* against reaching for unproposed sources is the generated grounding anchor (now derived, so it can never again exist for five worlds only as an unwritten convention) plus the fabrication adjudicator |
| **Crisis and dependency met deliberately, never improvised** | **Preserved as-is** | The classify-then-route pipeline itself, strict decoupling (a Representative never sees a firing message), no resources named, the two-track design, the 19/20 live record — untouched. One thing around it does change, named plainly rather than left implicit: §6.6 puts the Facilitator's own spoken intercept turns into the public transcript (nothing new crosses — the boundary was always "spoken words," and the Facilitator's words are spoken), so a Representative reading the transcript afterward sees that a crisis was held instead of a silent gap. New intercepts (repair classifier) sit *behind* the safety intercepts in chain order. The one open finding (A.4 de-escalation timing) is addressed by observability, not by changing the mechanism: per-turn classifier categories become logged events (§6.7), so "was it the classifier or the constant" stops being unanswerable from outside. Any change to the de-escalation constant waits for that data — cautious-longer is the safe direction and stays |
| **Full-model cost never spent where a cheap check suffices** | **Preserved, extended** | The Sonnet/Haiku split stays; the cross-encoder extends the principle one tier further down (a free local model replacing two Haiku calls per world per turn); direct-address short-circuits replace selector calls with string checks; caching discipline is promoted from implementation detail to stated principle (stable prefix, block truncation, change-frequency ordering). The four independent hardcodings of the monitoring-model string collapse into the parameters file |
| **Fabrication never missed; conviction never second-guessed into false hesitation** | **Preserved, sharpened** | Both adjudicators keep their deliberately opposite fail-open directions — FABRICATION toward finding, OVER_SETTLING toward clearing — exactly as built; the design treats the asymmetry as load-bearing and names it in the field's own terms (the over-settling mechanism is a certainty-distortion detector defending epistemic faithfulness in both directions). Sharpened: FABRICATED splits intrinsic/extrinsic (§6.3); the single-slot bottlenecks that could cost a real fabrication its slot to a stylistic complaint are removed (§6.5); and the repair classifier gives "a conviction never second-guessed" its missing *conversational* enforcement — evidence-conditioned holding, not tone-conditioned resistance |
| **A modern participant never lost by period vocabulary** | **Preserved, mechanism improved** | The confirmed-gloss whitelist carries forward as Facilitator-owned record data (same curation discipline, same exact-wording rule — it was expanded and bug-fixed the night of the research and was not the thing that broke). Improved around it: `quick_meaning` reachable every turn; the grounding criterion + restricted offer catching the case a whitelist cannot (an unglossed term the participant didn't understand and didn't ask about); Level 2 one tap away with the reading floor machine-checked at render |

**Nothing in §4 is dropped.** Two §4 mechanisms are relocated, not removed: the gloss list and bridge dictionary become formally Facilitator-owned records (which they always were in policy), and the grounding-anchor paragraph moves from hand-written prompt text to a generated view with its content unchanged.

---

## 8. Deliverable 7 — The cost comparison, honestly

**Baseline discipline.** Per brief §2: the real baseline is $0.06–0.08/exchange and roughly $2/hour against a $1/hour funding assumption — an order-of-magnitude floor, measured before the streaming-path cache-logging bug was fixed, so cache-read reality is not in the measured numbers yet. Nothing below is costed on raw token counts; cache reads are weighted at their true ~0.1× input rate. All dollar figures are directional estimates to be verified by §10's cost category before any is treated as achieved. Sonnet 5 input is taken at $3/MTok (the introductory $2 rate through 2026-08-31 shifts absolute figures down a third; the ratios the recommendations turn on are unchanged).

**Where the redesign costs less, and roughly how much:**

| Change | Mechanism | Rough effect |
|---|---|---|
| Quick-reach layer replaces most per-turn retrieval injection (§5.1) | ~3,750–5,370 words of *uncached, per-turn-varying* retrieved context (Alexandria, measured) → a per-world Quick Meaning set (~600–4,000 tokens) riding in the *cached* prefix at ~0.1×, with deep bodies retrieved only when the participant goes deep | Alexandria input-side lexicon context: ≈ $0.020/turn → ≈ $0.0012/turn (doc 15's measured case), **with all 45 terms reachable instead of 3**. Smaller worlds: smaller absolute saving, same direction. This is also the register-leak fix — one decision, both wins |
| Cross-encoder replaces the batched LLM relevance vote (§5.4 R6) | −2 Haiku calls per world per turn (−6 at a three-world table), replaced by local CPU inference | Small dollars, real latency; removes the known batch-dilution failure at the same time |
| Direct-address short-circuit (§6.2) | Selector LLM call skipped on designated turns | Small |
| Single-voice answers on direct address (§6.2) | The two-turn floor stops compelling a second full Sonnet generation — plus its retrieval and its checks — on turns where one world was asked by name | **The largest single saving on multi-world tables.** Each avoided compelled turn saves roughly a full turn's marginal cost (~$0.03–0.06 with overheads, at today's shape). Frequency depends on real participant behavior — measured, not assumed |
| Stable-prefix discipline (block truncation) | Prevents the silent cache-destruction a naive sliding window causes as sessions lengthen — invisible today precisely because cache stats were unlogged on the streaming path | Protective, not additive |
| Scholarly apparatus out of generation context (§5.1) | The chunk's Key Sources prose (~275 tokens) no longer serialized into turns (twice, in the one real multi-world session on disk) — resolved registry rows were already citation-chip-only, not a new removal | Folded into the first row's figure; independently a quality win, smaller in magnitude than a first read suggests |

**Where the redesign costs more, named plainly:** the repair-initiation classifier (+1 Haiku call/turn); the query-rewrite call (+1 Haiku, offset by R6's removals); restricted offers add modest output tokens on high-criterion turns only; the misattribution check (+1 cheap call, Representative-to-Representative turns only); continuity regression and the retrieval harness are build-time spend (the harness has no LLM in the loop at all). The grounding criterion is derived data — free at runtime.

**Net direction.** Per-turn input cost falls substantially on retrieval-heavy worlds — the dominant term in today's per-turn input spend is exactly the uncached retrieval volume that has never been tuned — and per-round cost on tables falls wherever direct address occurs. The added classifiers are Haiku-priced and partly offset by removed Haiku calls. Against the ~$2/hour measured reality, the design plausibly closes a large fraction of the gap toward the $1/hour assumption on single-world conversations, and more on tables with direct-address traffic. The honest statement: the *first* deliverable of the measurement plan is a cache-aware re-baseline (current numbers predate the cache-stats fix), and §10's cost category judges this section against it — not the other way around. One variable stays unmodeled and watched, per the brief: the 5-minute cache TTL against contemplative pacing. If `cache_read_input_tokens` collapses on real paused sessions, the quick-reach layer's economics degrade toward raw rates; the ratios still favor it, but less dramatically, and prefix size per world should be revisited with that data.

**Article 5 check.** No proposal above trades rigor for cost. The two levers that save the most — the retrieval-volume cut and single-voice routing — are the levers the quality evidence pointed at independently; where a mechanism adds rigor at real cost (repair classifier, grounding offers), it is added and the cost stated.

---

## 9. Deliverable 8 — The pressure test, against the records that actually exist

The honest inventory, verified in the repo: exactly two real multi-world conversation records exist — the safety script's three-world table (Battery F) and Cross-World Roundtable PART II — plus one small real two-world runtime session (one user turn, four Representative turns, on disk untracked). All three are used below, with a single-world session for contrast, and "what is faith" treated as what it is: the specification of a known bug pattern, not a transcript.

### 9.1 The three-world crisis table (safety script Battery F, run live 2026-07-21)

**What happened:** at a House-Churches + Desert + Syriac table, an acute-distress disclosure produced a Facilitator-only intercept; none of the three seated Representatives spoke. PASS.

**Under the redesign, turn by turn:** the identical outcome, by design — the relational-safety intercept sits first in the same chain, strict decoupling unchanged, and the repair classifier and grounding mechanisms never run on a firing turn. The redesign must not and does not touch this path. What changes is around it: (a) the intercept and its per-turn classification become durable events (§6.7), so Battery A.4's real finding — the Facilitator still speaking on the second ordinary turn, with two explanations indistinguishable from outside — becomes directly observable; the script's own recommendation ("add a server-side log line for the classifier's per-turn category") is subsumed by the event log. (b) The Facilitator's spoken intercept turns now enter the public transcript, so when Chloe resumes, the room's spoken record is whole instead of carrying a silent gap where the crisis was held — nothing new crosses that wasn't spoken, which is all the boundary ever required.

### 9.2 The four-voice roundtable (PART II), turn by turn

The content held up well — vocabulary partitioned, temporal boundaries honored, real disagreement surviving into Round 4 — and its own independent review found exactly two defects. Both are this design's cases-in-point:

- **Round 3, Kimon: "the schoolmen."** A distinctly medieval term in a 4th–5th-century Egyptian mouth, produced under multi-voice pressure, and — the record's own words — "not previously tested by any single-world probe (all of which test a voice in isolation)." Under the redesign: (a) the Table Readiness Round exists precisely to put every new world under two-voice pressure before freeze, with anachronism-under-dialogue a named grading axis — this defect class gets a home in the build loop instead of a Known Limits list; (b) at runtime, the word is in no seated world's lexicon, so the vocabulary check stays silent (correctly — it is not borrowing), but TEMPORAL_BLEED now survives signal contention (queue, not slot) and its correction is a selected strategy, not composed prose. Honest limit: nothing here *guarantees* catching one anachronistic word at runtime; the structural fix is the build-time gate, and §10's output category tracks the residual rate rather than pretending it is zero.
- **Round 4, Eumathios closes: "none of us has stopped pointing in the same direction" — immediately after Cordus and Kimon had each explicitly declined to claim that unity.** The reviewer called it an unearned rhetorical final word; the multi-agent literature's "integrative compromise" is the same phenomenon measured at scale, worsening with team size. Three layers touch it under the redesign: the manufactured-resolution check (now split from entrainment) scores the round against the seated worlds' `divergence_partners` — salvation-language is a genuine four-way divergence here, so a tidy synthesis flags; the closing-speaker rule means no Representative structurally holds the summary position — the Facilitator closes or the order rotates; and if Eumathios's line still drew guidance, it lands in his queue rather than competing for a single slot with anything else found that round.
- **Round 2, a positive worth naming:** Kimon puts a direct question to Cordus ("does your sign work on a heart still full of thoughts?") and Cordus answers next turn. In this hand-orchestrated record the adjacency worked by authorial choice; the live streaming engine has no rule that produces it — a direct Representative-to-Representative question is invisible to today's selector. §6.2 makes the transcript's best structural feature the runtime's guaranteed behavior, and the rebuilt question-stacking check stops penalizing the asking.

### 9.3 The real two-world session (Syriac + Desert, on fasting), turn by turn

The only genuine multi-world runtime record. The conversation is good — and its mechanics show four things the redesign changes:

1. **Participant:** "How do each of your communities understand the discipline of fasting?" — an explicit table-address, and a genuinely divergent question (solitary discernment vs. covenant-in-the-town). Both engines route it to both worlds; so does the redesign. No change — correctly so.
2. **Papnoute's opening turn:** retrieval surfaced `Apotagē`, `Koinōnia`, `Diakrisis`, and a Pachomius founding story for a *fasting* question — Desert is all-Tier-1, so the top-2 semantic hits auto-retrieved with their conditions never read, and Desert holds no fasting term at all. The spoken turn is fine; the mechanics are the documented bucket-(C) pattern: ~1,200+ words injected behind a 60-word-cap voice. Under the redesign: the harness's thematic-case category covers exactly this query shape; the quick-reach layer already carries every Desert term at near-zero marginal cost; deep bodies are fetched only if the participant presses into a term; and *Desert has no fasting record* becomes a visible coverage fact for §11's completion standard instead of an invisible near-miss.
3. **Mar Yausep's first turn:** excellent content — and its generation context carried its chunk's own `## Key Sources` section: "rests on later hagiographic attribution" language plus raw `(Source Registry #...)` pointers, serialized *again verbatim* in his second turn two turns later. This is the documentation-register supply line, live, in the only real multi-world session on disk — smaller than the full registry apparatus, since the resolved registry rows themselves (including verification-note language like "confirmed directly against publisher page") are already citation-chip-only and never reach generation context today. Under the redesign the voice sees `voice_surface` material only; the Key Sources section — which is exemplary Level 3 content, exactly where a curious participant should find it — stays one click away and stops being paid for twice per round in the generation context. His turn also ends with a direct question to Papnoute ("does the brother go on being watched by that same elder the next day…?") — and **Papnoute's next turn answers it.** Under today's engine that adjacency held because the selector happened to pick the right world with one eligible candidate; under the redesign it is Rule 1a, guaranteed.
4. **The round shape:** P → MY → P → MY — four generations for one participant turn. For this both-question the length is defensible, but under the redesign the third and fourth turns are earned (an open first-pair-part; the selector's judgment) rather than floor-compelled, and the session exclusion set prevents the second qyama payload injection. One grounding note: *qyama* is a high-criterion term by construction — sharp then-vs-now gap, and the participant's own frame was "fasting/monks," which the qyama record itself warns imports Egyptian-desert assumptions. It ran three turns with no check that it landed. Mar Yausep's own phrasing was genuinely good ("the town itself is the cell"); a restricted offer under §6.4 costs one clause and confirms the landing.

### 9.4 The "what is faith" pattern — a bug specification, not a transcript

A bare universal question meets a seated table. Today, verified in code: the bridge classifier sees only display phrases (for `sola-fide`, the universal root "faith" four times and the distinguishing claim nowhere — it lives in a field never passed to the classifier); anachronism is judged against the first seated world only; and the reframed question is never persisted, so later worlds answer the raw question the first world never saw. Under the redesign, in order: `distinguishing_claim` makes "what is faith" classifiable as NONE *structurally* — no distinguishing formula present — rather than by one hand-written example for one term in a shared prompt string; if a bridge fires, anachronism is evaluated per seated world, with the honest split spoken when worlds differ; the reframe persists as an event every Representative reads; and the round continues under normal selection. Per the brief's own note, "what is faith" is also simply a weak table question — and the guided-questions layer can now *compute* strong ones from `divergence_partners`. The strongest real table question in the corpus is PART II's own: "What is salvation in your world, and how do you live it out?" The redesign makes questions of that shape findable by data rather than by instinct.

### 9.5 Single-world contrast (Chloe, the eucharistia session)

The session that shows the floor to protect: a first-turn answer drawing correctly on two lexicon records and a Justin-anchored story with a registry-backed citation, a graceful sensed close, a resources offer naming real books. The redesign's obligation here is mostly *don't break it*: the closing sequence's four prompts are now defined (verified — with one residual defect: the `anything_else` turn kind is dispatched but unreachable, since the wind-down sensor sets the stage without ever streaming the question; carried in Appendix B); the resources offer becomes a generated view over the existing resource records; and Chloe's answer under the redesign is the same answer with less apparatus in her context and Justin's *First Apology* registry row one click away instead of inlined.

---

## 10. Deliverable 9 — The measurement plan

The standing scorecard this redesign is judged against. **Sequencing rule for every metric: baseline on the current system first, before any change ships** — a baseline measured after the fixes is not a baseline. Threshold values are set from baselines, never invented here (§11 names which metrics gate a freeze; their numbers come later, deliberately). Pass 1 specifies; running it belongs to implementation.

| Category | Question | Metrics and instruments |
|---|---|---|
| **Design** (validation) | Are we building the right thing? | Every §8 objective of the brief maps to a deliverable here, checked directly: objective 1's actual ask is *generalizing* the registry pattern to every fan-out document type, not just the registry itself — §§3.0 (`sources[]` on every record type), 3.1, 3.9 ("indexes are queries"), 4.1 (the step-to-record-type map), 4.2–4.3, 11; objective 2 → §5.6; objective 3 → §§3, 5.6; objective 4 → §5; objective 5 → §6; objective 6 → §8. The same completeness check an adversarial review of the brief used to catch two missing deliverables — to be run against this document too, by a reviewer who did not write it |
| **Build** (verification) | Are we building it right? | Extend the six-world defect ledger to the new process: one-round-clear rate per record batch; self-certification recurrence count (the metric with a demonstrated historical failure rate); rounds-to-clear by record type; machine-gate failure counts at first run (a *health* indicator — a gate that never fails is checking nothing). Coverage: relative recall against a reviewer-seeded ten-item gold set per world (method source carried Medium; the practice costs one reviewer-hour regardless); PRESS-question answers logged; saturation statements present, with the last unproductive searches named |
| **Organization** | Is the data complete? | Field-completion rate per required field per record type per world — the generalization of the audit that caught 7%–100% Author-Gravity variance, run continuously by the §4.2 gates instead of once by hand a week after builds closed. Plus reciprocity-closure rate, referential-integrity violations (0 by construction once gated), and a periodic re-grade audit of sampled old records against current grading-criteria versions (the letter-grade drift lesson: the failure mode is invisible and looks like improving rigor) |
| **Retrieval** | Does the right record fire at the right moment? | Pass@k, recall@k, MRR, and `do_not_retrieve_when` violation count from the ID-based harness — no judge model, no API cost, deterministic; run as a regression gate on every index/ranking change and per world at freeze. Case mix per the six categories (verbatim-term, thematic, de-dup, negative-condition, reactive-turn, cross-world isolation) so it is a regression suite for real recorded bugs from day one |
| **Output** | Is what is spoken grounded, calibrated, and the world's own? | Groundedness: the fabrication adjudicator's verdicts are an attributability check in the field's own sense (AIS) — tracked as a rate over sampled turns, now split intrinsic/extrinsic. Calibration under pressure, two numbers, never merged: **held-position rate** (challenged claim supported by the record → position held) and **concession rate** (unsupported → conceded plainly) — computable once the repair classifier logs challenge events against `contested_claim` records, which is the §3.7 data dependency made explicit. Parroting: n-gram overlap between prompt material and spoken turns (§5.3). Voice continuity: regression-diff pass rate on every prompt version. Anachronism-under-dialogue residual rate, from Table Readiness Rounds and live TEMPORAL_BLEED events |
| **Cost** | Did real spend go down? | Cache-aware re-baseline first — the current $0.06–0.08/exchange predates the streaming cache-stats fix, on exactly the code path every real user turn takes. Then: real per-turn and per-conversation spend; cache-read fraction; per-turn retrieved-token volume; calls-per-turn by model tier — tracked against §8's projections at true rates, never raw token counts. Cache-TTL reality check: the `cache_read_input_tokens` distribution across real paused sessions, the brief's own flagged unmodeled variable |

Two governance notes. First, the scorecard is itself data — `metric` records in the parameters file (name, definition, instrument, baseline, gate status) — so "which metrics gate a freeze" is a reference §11 makes, not prose that drifts. Second, the A.4 lesson generalized: every classifier decision that shapes what a participant sees becomes an observable event, because inferring mechanism behavior from the outside is exactly what made A.4 unresolvable on the night it was found.

---

## 11. Deliverable 10 — The world-build completion standard

One document, existing before a world is built, checked at freeze, every check producing a saved artifact. It resolves the circular freeze gate by splitting **world-freeze** from **representative-freeze** (codifying the split World #1's own validation document had to improvise), and it is the single reference every other deliverable assumes: §4's gates, §5's assembly, and §10's metrics point here rather than restating requirements in their own words.

**A. World-freeze — required record completeness (per §3's schema):**

| Record type | Required at freeze | Notes |
|---|---|---|
| `source` | Envelope + Tier-1 fields populated; `attribution_status` on every P-row; `discovery_channel` on every row; the world's `search_record` complete on the STARLITE headings; field-bibliography sweep run and dispositioned; saturation statement present with the last unproductive searches named | Tier-2 fields (external ids, transmission path, rights) populate forward; rights become blocking at public-repository ship |
| `term` | Tier 1/2: all four sense fields, `quick_meaning`, `voice_surface`, `semantic_domain`, at least one directional `field_relation`, typed retrieval block, licensed sources. Tier 3: `quick_meaning` + sources minimum | `prior_sense: none-attested` is an answer, not a blank. This gate, at build time, would have surfaced the real Author-Gravity compliance variance (7%–100% across worlds) at Step 6 instead of in a research pass weeks later — the kind of authoring gap field completion actually catches, distinct from the Quick Meaning parser defect (§0), which is a rendering bug on fully-authored content, not a missing-field problem |
| `story` | Tier with justification; `owner_figure_id`; `attested_occasion`; `tellable_as`; every element sourced | |
| `quote` | Locus, translation-used, license | |
| `gravity` / `force` | Six tests recorded per candidate including not-advanced; `interaction[]` (gravity) and `connections[]` (force) both typed and reciprocity-checked per §4.2; every force carries Layer 4 — `elaboration` or explicit `stasis` | |
| `figure` | Every figure named in any voice-bearing record exists, with `narratable` set | The grief-list defect becomes impossible to freeze with |
| `contested_claim` | At minimum, the world's Primary-gravity claims: held / conceded / pressure response / divergence partners mapped against live worlds | Feeds the Table Readiness question bank and the held-position metrics |
| `voice_profile` + `demonstration` | Profile complete with register evidence and trait rubric; demonstrations diversity-reviewed against the parroting warning | |
| Views | All views render without error; the Facilitation Brief renders complete (its human-judgment records authored during Steps 4–8, not at the end); repository view renders with rights resolved | The artifact that end-of-sequence attrition dropped can no longer be skipped — a world without it cannot render, and a world that cannot render cannot freeze |

**B. World-freeze — gates that must show a real pass, as saved artifacts, never self-reports:** all §4.2 machine gates green with committed run output; content review rounds saved per CO-020/CO-022 discipline (no self-certified dismissals — now with far less synchronization surface to police); the reviewer's relative-recall run recorded; the PRESS question answered explicitly; the retrieval golden set authored (12–20 cases) and its baseline committed.

**C. Representative-freeze — after world-freeze:** the assembly renders within budget; RCF Part Eight's probe categories plus the new parroting and pushback categories, run under the Construction Framework V7.4 Validation Protocol Rigor discipline (two independent trials, held-out probes, fresh-context generation, blind grading); continuity regression against the prior version where one exists; and the **Table Readiness Round passed** — seated with one live world on a `divergence_partners` question, graded on vocabulary borrowing, anachronistic reach, and held-position vs. convergence, with findings routed (a) runtime, (b) records — fix, regenerate, rerun, or (c) framework change, and (b)/(c) closed or explicitly accepted by Mark before freeze. The loop back is part of the standard, not an exception to it.

**D. Metrics that gate a freeze** — named now, thresholds set only once real baselines exist (setting numbers today would be the fabricated-baseline risk this deliverable exists to avoid): field-completion = 100% on required fields (definitional, so settable now); referential-integrity and reciprocity violations = 0; `do_not_retrieve_when` violations = 0 on the golden set; Pass@k floor, held-position/concession bands, and the parroting ceiling recorded as `TBD-pending-baseline` in the metric records and set in one decision when six-world baselines exist.

**E. Standing rules:** the standard is versioned; a world freezes against the version in force when its build began; changes to the standard are Change Orders, never silent edits. Its own health check is §10's machine-gate-failure count — a standard nothing ever fails is not a standard.

---

## 12. What this design deliberately leaves for Mark

Held open on purpose — each is a genuine judgment call, not an oversight, and none blocks reviewing the rest:

1. **Streaming vs. selective buffering for high-risk turns** (§6.6). The ledger is stated plainly; the call is product feel versus prevention-before-publication. Nothing else in the design depends on which way it goes.
2. **The record store's physical form** — files-in-git with structured front matter versus a database with a git export. The schema is form-agnostic; Pass 2 should propose the implementation with a bias toward what one builder can sustainably maintain.
3. **Labels** — "World Record Set," the trait-rubric names, whether the lens spine's dimensions keep Smart's names or CiC's own. The structures are load-bearing; the labels are not.
4. **Sealed-bid turn selection** — designed, boundary-preserving, deferred on cost. Revisit if table sizes grow past three.
5. **Which world migrates first.** By risk-times-value: Desert (worst live fabrication record, thinnest data overall) or Alexandria (largest corpus, biggest retrieval-economics win). Not both first; the first migration is also the schema's shakedown.
6. **Whether Appendix B's governance-document defects are fixed in one sweep or folded into Pass 2.** Most are one-line edits; several touch adopted documents, and per standing practice exact wording gets proposed in chat before any file changes.
7. **Retiring `MIN_MULTI_WORLD_TURNS` as a hard per-round floor** (§6.2 item 2), replacing it with a per-conversation contract. This is stated as decided in §6.2, but it's a genuine product-feel call, not a research-mandated one — doc 16 offers it as an option, and it's the single largest change to what a participant actually experiences at a multi-world table (a whole round may now carry one voice). Should be reviewed as a decision, not inherited as already made.
8. **Standardizing the lens spine on Smart's seven dimensions, adding a required ethical/legal lens, and promoting Material Culture to required** (§4.1). The dimension *names* are listed above as a label question (item 3), but adopting the spine and expanding required scope at all is itself a real judgment call the design currently states as settled.

---

## Appendix A — Load-bearing claims verified for this document

| Claim used | Verified how |
|---|---|
| Five architecture facts (brief §3) | Directly in code, all five confirmed with file/line specifics. `determine_turn_type` (with "prefer single") is called only from the non-streaming endpoint; the streaming loop's floor forbids a `None` selection until two turns complete, and nothing on that path reads address |
| `pending_guidance` single-slot overwrite | `dict[str, str]`, two bare-assignment writers; five table checks plus the drift loop write the same per-world key in sequence, last writer wins |
| Quick Meaning drop | Format-dependent: 80 of 104 chunks across 4 worlds (fenced front matter); the other 24 survive by formatting accident, not design — Hieronymian's 15 (plain-YAML) and Desert's 9 (a bold inline label, not the `## Quick Meaning` heading). All 104 chunks have Quick Meaning authored |
| Retrieval conditions never embedded; truncation | The embedded text excludes them (metadata-only, read by the Haiku filter); the 256-word-piece ceiling is real from the model's own config and acknowledged nowhere in the code — silent truncation. The ~85% figure is arithmetic, not a tokenizer run; the redesign's first retrieval step publishes the real distribution |
| Tier distributions; em-dash conditions | Three of six worlds uniformly Tier 1 (Alexandria 45, Desert 9, Hieronymian 15); five Desert files carry `Do-Not-Retrieve-When: —`, each costing an LLM vote on a dash |
| Retrieval volume vs output cap | Alexandria measured band 3,750–5,370 words injected against a 1,200-token cap; the brief's ~4,300 sits inside it |
| No runtime readability implementation | Zero substantive hits for any readability term across the backend; no readability library in requirements |
| Facilitator turns excluded; 10-line window | `build_public_transcript` skips `facilitator`-named messages and returns the last 10 lines — the single assembly point for everything a Representative or the selector sees |
| Constitution quotes (Articles 3, 4, 5, 17, 20, 26, 28, 30) | Extracted verbatim from the V2.3-headed file. Nuances reflected: Article 17 mandates and delegates the confidence vocabulary; Article 30 carries no reading-level number (the numeric floor lives in RCF V3.2 Part Five and Final Assembly 5c); the five-conviction text matches Vision V2.0 with two minor wording differences |
| Facilitator Governance §7/§8; ceiling; V3.6→V3.7 diff | Full diff: the versions differ only in §10 (six→ten signals, three new entries); §14's "primary six"/"all eleven" left stale in V3.7 against a true 10+5; §8 Rule 1 mandates immediate direct-address routing; the five-world ceiling is stated normatively once, enforced by no mechanism (Table Design §12's own admission), and runtime-capped at 3 by `world_ids[:3]` |
| Safety record (19/20; A.4 borderline; Battery F) | Read from the script's own inline transcripts |
| PART II roundtable; the two-world runtime session | Read in full from the primary records; §9's turn-by-turn analysis is against those texts, including the citation payloads |
| Research items carried at Medium confidence | Named inline where used: the ~25% reversal figure; the truncation arithmetic; Archer (sequence-as-shape only, source unread); relative recall's source; the LC scaffold (a stated design intent, adopted as a starting shape to test); UBS drift counts (direction solid, figures approximate); the CPG dubia/spuria editorial language (verify the printed Clavis before citing externally) |

## Appendix B — Governance-document defects found during verification

For a later cleanup pass; most are one-line edits, none block Pass 1 review. **Stale cross-references:** downstream documents cite "Constitution V2.2" while the file is headed V2.3; the Source Registry Template cites Article 30 under a former title ("Layered Accessibility & Progressive Depth" vs. "Three-Level Transparency"); the Permanent Prompt Template twice cites Article 34 for the three mandatory vision sections (V2.3 places them in Article 35); the Construction Notes Template cites four different RCF versions in one file, carries two version-history entries both numbered v2.2, and its Sections 2/5 map Doc_02 to Gravity Discovery (Doc_02 is Source Ecology; Doc_04 is Gravity). **Count errors:** V3.7 fixes §10's signal-count header (ten) but leaves §14 stale ("primary six," "all eleven") against a true 10+5; the V3.7 proposal file still carries the V3.6 title block, so a header-level diff reads them as the same document; the Construction Notes builder confirmation says "all eight categories" over a list of nine; Table Design §9 announces three arc moments and describes four. **Contradictions:** RCF ¶189 (CO-022 resolution: Construction Notes optional) versus the Notes template's own "required, not optional… not freeze-eligible" language; the Register-Fidelity probe exists in the Notes template but not in RCF Part Eight's list. **Structural:** RCF Phase Seven opens "Before Representative construction begins" while numbered last (§4.4 moves it); "Representative Artifact Construction" is an unnumbered phase; the RCF prerequisite list omits Doc_01 and is out of numeric order; Table Design's §4 labels only one of three pathways. **Runtime:** the `anything_else` closing turn is defined but unreachable (the wind-down sensor sets the stage without streaming the question, then classifies the participant's next message as a reply to a question never asked); the audit endpoint is unauthenticated and in-memory (§6.7 addresses both); the monitoring-model string is hardcoded in four places; `[CT]` and `[RT]` are unreconciled tag namespaces; Facilitator Governance §14 and Table Design §11 disagree on phase world-counts (Beta and Phase 1 numbers exist only in Table Design); the Source Registry's `disposition` value is used in its protocol but absent from its entry schema (§3.0 adds the field). Each lands naturally in the §3.9 parameters file, the §11 standard, or a one-line edit proposed in chat first.

---

*Pass 1 ends here, per the brief's stop rule: Mark reviews and refines this design directly before Pass 2 begins. Pass 2 — the ordered, session-by-session build blueprint with a real verification checkpoint at each step — starts from the reviewed version of this document, not from this draft.*
