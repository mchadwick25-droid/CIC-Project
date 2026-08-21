# Imperial and Juridical Christianity (`ijc`) — Record-Set Build Log

**Branch:** `world/ijc` (base `build/phase-1`) · **Built:** 2026-08-21 · **Scope:** spec §4.3 steps 2–4 (source ecology → interpretive lexicon → ecology reconstruction → answer canon). **Voice build (step 5), compile (6), admission (7), open (8): intentionally NOT started**, per the standing instruction to stop before voice/demonstration while the live-generation citation design is unproven.

**Settled ground built from (not reopened):** the per-world Step 0 confirmation (2026-07-19, Approved to proceed, Round 3) and Doc_01 (Approved to proceed, Round 2 cosmetic only) — identity ("office-holders, not congregants"), window 312–451, three strands, Homoian recentering, skew disclosure, Living Tradition PENDING.

**Content ground:** the reviewed legacy document suite (Doc_02–Doc_09 with their Review-Artifacts, all Approved to proceed under the prior framework) was used as the content input, with every claim re-anchored to the vendored public-domain corpus and every verbatim quote re-verified character-level against the vendored files. Divergences from the legacy suite are itemized in §3.

## 1. Final state

125 records in `records/ijc/`: 1 world_core · 19 source · 16 search_record · 12 term · 6 gravity · 10 force · 7 contested_claim · 12 figure · 20 quote · 8 story · 7 doctrinal_witness · 7 honest_limit. Registry entry added to `records/worlds.yaml` (state: `building`).

**M1 gate battery: 13/13 clean** (schema, referential, reciprocity, completion, narratability, quote-recording, alias-safety, distribution-health, confidence-crosscheck, rights, readability, canon-coverage, no-build-attribution). **Canon coverage: all 28 cells — 21 substantive, 7 honest-limited** (C-P, F1-T, F2-P, F4-P, F5-I, F5-T, F6-E), each honest limit with in-voice statement, cause, and nearest material.

## 2. Stage discipline

Built one stage at a time with gates run and a self-review pass between stages, committed incrementally (corpus vendor → sources/searches → terms → gravities/forces/claims → figures → quotes/stories → witnesses/limits → consistency pass). This is a records build, not a Doc_XX drafting cycle: the independent-review function the legacy documents received is carried here by (a) the already-reviewed legacy suite as content ground, (b) the mechanical gate battery, and (c) the disclosed verification corrections below — an honest description, not a claim that fresh per-record adversarial review rounds were run. If the project lead wants a cold adversarial review of the record set before step 5, that is a natural next action and nothing here forecloses it.

## 3. Verification findings — corrections made during this build (each disclosed in the affected record)

1. **Legacy Doc_09 story 6 factual error corrected:** "the same council, in the same session" — the Tome's reception (Session II) and Canon 28's passage were days apart. Corrected in `ijc.story.tome-that-would-not-bend` with the separation stated in `absent_detail`.
2. **Egyptian bishops' plea mis-citation caught pre-commit:** first drafted against Percival's Chalcedon extracts; a direct read found the scene absent (it is in the complete acts only). Re-sourced to via-authority in `ijc.force.chalcedon-failed-consensus` with a verification note.
3. **"Countermanded too late" detail dropped:** the often-told countermand of the Thessalonica reprisal is not in the vendored accounts (checked Theodoret V.17, Sozomen VII.25); removed from `ijc.story.emperor-penance`, with the 7,000 figure carried only under Theodoret's own "it is said."
4. **Percival's singular "prerogative of honour"** (not "prerogatives") verified against Canon 3's text and normalized across records.
5. **Legacy Registry row 13's unverified Leo letter numbering (Ep. 104–106) verified** against the edition itself; row 21 (Rufinus HE) found unreproducible in public domain and honestly dropped (search_record); Sozomen VII.4 confirmed as the Thessalonica-law witness with the Damasus/Peter clause read directly.
6. **New source findings beyond the legacy suite:** Theodoret's embedded Damasus synodical letters (a securely-transmitted Damasus documentary voice distinct from the contested decretals); Hilary's De Synodis as vendorable access to the Homoian formulae (registry append, justified in `ijc.search.npnf209-hilary`); npnf210 lacks De obitu Theodosii (penance rests on Ep. 51 + flagged Theodoret).

## 4. Additions beyond the legacy inventory (registry-grounded, disclosed)

- `ijc.story.emperor-penance` (390) and `ijc.story.altar-of-victory` (384) — the latter closes legacy Open_Gaps item 6 (the un-registered Altar of Victory material; Symmachus's Memorial is in vendored npnf210).
- Tension-coverage: the Tensional gravity carries a real matrix-mapped `tension-with` pole (primacy-claiming — the Interaction Matrix's one "competing" cell); its Strand B status stays genuinely open per Doc_04 Open Item 2.
- `canon_cells` populated at authoring time on every gravity/force/contested_claim (the Alexandria retrofit discipline), with deliberately-empty cells reasoned in-body (boundary-condition forces; the bees legend; Nea Rhōmē).

## 5. Flagged for Mark (nothing here decided by this build)

1. **Representative identity under the new spec (step 5a touchpoint):** the registry carries Marius / "Deacon of the Letters" from Mark's own 2026-07-20/22 decisions (Open_Gaps items 13, 15) — carried as his standing decision, explicitly NOT re-confirmed under the new spec.
2. **Living Tradition Status: PENDING** (Doc_01 §1); registry `living_tradition_flag: true` meanwhile, failing toward doorway disclosure.
3. **Open source requests (P3, non-blocking):** Paulinus's Vita in the 1928 Kaniecka translation (would upgrade the bees story's verifiability); Ammianus (Yonge 1862) for the Damasus-election account. See SOURCE-REQUEST-MANIFEST §2.
4. **"Church and Empire"** is the census/card short name (Mark, 2026-07-20); the registry `census_id` maps to the Atlas entry `imperial-juridical-christianity`.
