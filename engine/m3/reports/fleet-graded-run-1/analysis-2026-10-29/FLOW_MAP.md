# CiC engine: map of information flow, and where each failure enters

Question: why do answers fail, and where in the pipeline does each failure enter?

Method: I read the code only, at the checkout `/home/user/fr1-records`. No model was called and no engine code was run. Failure data comes from the 12 `review-<world>.md` files, `reviews.json`, the packets, and the run JSON in `engine/m3/reports/fleet-graded-run-1/` (`raw_text` vs `answer_text`, compared by a small script on the saved data only).

Three facts set the frame for everything below:

1. **The 12-world test did not run the live turn path.** It ran the admission harness: `engine/m3/live_admission_run.py` → `harness.run_battery` → `generation.LiveModelAnswerer.answer`. That path shares evidence assembly, the voice call and `apply_net` with the live path (`engine/m4/turn.py`). It skips the gate, the reader, the per-turn directive and every post-draft repair. Section (d) lists each difference. So some failures belong to both paths and some only to admission. The table in (c) says which.
2. **The automatic checks could not have caught these failures.** Admission grades two things only. `source_boundedness_check` (`engine/m3/grading.py:73`) asks whether each cited id traces to a source record. `register_check` (`:134`) is advisory and always passes. The citations it grades are the ones `apply_net` has already verified (`turn.py:422-426`: only sentences with an `ok` verdict keep their tags). So the first check passes almost by construction. No automatic check reads cut damage, frame breaks, horizon, cautions, readability or false silence.
3. **The worlds ran at different commits.** `run_settings.repo_commit` differs by world: alx c7a64ff, desert 72cceec, don 90c9c7f, gallic 89557cc, hal 0526144, ijc 00b3e5b, lpc c7b0c52, pahc 3c69d7b, rzg 9a3b313, syr 045a70b, witt 6125980. My line numbers are for the current checkout. A mechanism cited here may have been slightly different at a world's own run commit (flagged in (e)).

---

## (a) Stage by stage: from the question to the text the participant reads

L = live path (`engine/api/wiring.py` → `engine/m4/turn.run_turn`). A = admission path (`LiveModelAnswerer`). "Both" means both paths run the stage.

### Stage 0. Build time: records become a package (both)
- **In:** `records/<world>/<type>/*.md`, the registry entry.
- **Code:** `engine/m1/loader.voiced_records` (`loader.py:120-124`) keeps every record not marked `voice: analytic`. It does **not** filter `status: draft` (don's draft `don.limit.theology-beyond-tyconius` shipped). `engine/m2/builders.build_prompt` (`builders.py:269-478`), `build_repository_json` (`:722`), `build_coverage_json` (`:748`), `build_frame_json` (`:815`).
- **Out:** `compiled/prompt.txt` (the voice's cached system prompt), `repository.json`, `coverage.json` (per canon cell: which records serve it), `frame.json` (time window, story_placement flag).
- **What the prompt carries** (`builders.py:382-473`). Above a "below this line is our record" divider (`_GROUND_LINE`, `:210`), it has the standing instructions from voice_craft. Below the divider are the world_core fields Horizon, Formation logic, Thinness, **Cautions** and Living traditions, each headed "(cite as [[core id]])" (`:411-415`). Then every term, doctrinal witness, honest limit, the gravity names, every story's `tellable_as`, and every demonstration exchange in full (`:464-473`).
- **What it does not carry:** quote records, contested_claim, force and figure records. These reach the voice only through the per-turn evidence block (Stage 5).
- **Information added or distorted here:**
  - Cautions are written as instructions to the builder ("Never convert...", "this world's voice", "the texts this world can draw on"). They are compiled as citable world content, so the voice can read them aloud and cite them.
  - The horizon gate exempts `world_core.horizon` and `world_core.cautions` (`engine/m1/gates.py:1566`, `_EDGE_FIELDS`), so text naming later events ships to the voice.

### Stage 1. Fixed request frame (both)
- **Code:** `engine/m4/voice_request.build_voice_request` (`voice_request.py:47-58`). `system[0]` is the shape segment (`engine/shape/__init__.py:23-43`, built from `engine/shape/records/fleet_voice/_fleet.voice.fleet.md`). `system[1]` is the world prompt. `system[2]` is the turn directive, only when there is one. The final user message is the evidence block plus the question.
- **Added:** the fleet register. It includes "What the ground given for this turn does not support is spoken as our own honest limit" (`limit_discipline`, fleet_voice line 36). It also allows the sentence "I am a representative of..." (`pronoun_rule`, line 33). Both phrases show up in frame breaks (Stage 6).

### Stage 2. Gate and routing (L only)
- **Code:** `turn.run_gate` (`turn.py:113-187`) makes two Haiku calls in parallel: safety and the reader (`engine/m5/live_calls.call_reader`, `live_calls.py:252`; reader prompt `:87-130`). Then `engine/m5/routing.route` (`routing.py:153-215`).
- **Out:** a route and a `Directive` (`routing.py:113-122`): the reader's `asks` (the question restated as asks), `kind` (who / what_is / why / how ...), register note, ambiguity readings, out-of-scope class.
- **A:** skipped entirely. `asks=None`, no kind, no directive (`m3/generation.py:179-186`).

### Stage 3. Kind and the private directive (L only)
- **Code:** `turn_prep.prepare_voice_turn_inputs` (`turn_prep.py:519-645`): `evidence.resolve_kind` (`:579-587`), `asks_for_the_words` (`:588`), `_build_turn_directive` (`:358-494`).
- **Out:** a system block with these parts:
  - "Asks, in order".
  - `CONCISION_DIRECTIVE`: answer first, 120 to 220 words (`:221-226`).
  - A kind line (`:229-258`).
  - Quote lines. Either `NO_QUOTE_LINE` ("Put no one's words in quotation marks or after 'said'...", `:269-272`), or the offered quotes with the speaker name each sentence must carry, plus `QUOTE_SPEAKER_LINE` (`:276-283`).
  - Story lines (`story_placement.story_lines`, `:111-117`, "Never tell the story yourself").
  - `NO_GROUND_LINE` (`:284-287`), the figure gate, `LEXICON_LINE`, the refer-back line, the register note, ambiguity readings, figures already named, and the other-tradition honest-limit rule (`:89-218`).
- **A:** none of this. `stream_voice_turn` is called with no `turn_directive` (`m3/generation.py:193`).

### Stage 4. Evidence assembly: which records get put in front of the voice (both)
- **Code:** `evidence.assemble_evidence` (`evidence.py:1251-1447`).
  - **Stage A, the question → canon cells** (`match_asks_to_cells`, `:493-636`). This is a word-overlap match of the message plus the reader's asks (`_query_words`, `:405-407`) against the fleet canon questions' vocabulary. The hint words, stems, single-word and question-word tiers fill only empty slots. Up to 2 cells, plus one extra slot each for a hint word or an entity (`_add_extra_cells`, `:741-745`).
  - Follow-up inheritance from history (`:1310-1319`). L only, after turn 1.
  - **Stage B, cell → candidates** (`select_cell_candidates`, `:856-957`). Every honest_limit of the matched cell is included unconditionally (`:912-917`). Per-type floors depend on kind (`_FLOORS_BY_KIND`, `:174-184`; A always gets "other"). Ranked within the cell's own `coverage.json` entry.
  - **Stage A2, full-text fallback** (`:1399-1404`, `_fulltext_fallback_candidates`, `:352-402`). Runs only when no real cell matched. It searches **every record type in repository.json, with no type filter**, including `demonstration`, `world_core` and `voice_craft`. Their head text is `all_text(record)` (`_head_text`, `:321`).
  - **Stage C, scope completion** (`:1408-1426`): adds the gravity or contested_claim record that names a tension with a selected record.
  - Offer cap of 12 (`_cap_offered`, `:1429`; `OFFER_CAP`, `:1186-1199`).
  - **Stage E, session exclusion** (`:1430`).
  - **Stage D, thin-topic riders** (`:1436`, `thin_topic_riders`, `:960-982`): keyword hits against `world_core.thin_topics`.
  - Riders (`:1437`, `_with_riders`, `:1450-1464`): `claim_guards` and `use_note.not_for` become "MUST NOT ASSERT", and a story's `absent_detail` becomes "NOT KNOWN".
- **Lost here:**
  - The sealed probe's own cell is known to the harness (`harness.py:84-89`, `answer(cell, probe_text)`), but `LiveModelAnswerer.answer` ignores `cell` and routes on the wording alone.
  - When the wording misses the cell's vocabulary, the cell's own record is not offered. Reviews: don 16 of 28 questions, pahc 13 of 28.
  - `FLEET_FLOOR_LINE` / `degradation_statement` (`evidence.py:78-103`) is the code that would tell the voice "we have no grounded material for that". **It has no caller anywhere in the engine** (grep: no use outside evidence.py). It is dead code.

### Stage 5. Rendering the user message (both)
- **Code:** `render_evidence_block` (`evidence.py:1526-1617`); `turn_prep.py:610-613` (L) and `m3/generation.py:189-190` (A).
- **Out:** a block headed "## Ground for this turn (cite only these; anything beyond them is spoken as our honest limit, never asserted)" (`:1563-1564`). Then one line per candidate, "- [[id]] type, CLASS, confidence — head | means: ... | MUST NOT ASSERT: ... | NOT KNOWN: ...". Quotes appear as "[[quote:id]] quote from <speaker>" (`_quote_line`, `:1502-1523`). Thin topics appear as "- THIN GROUND (do not claim past it): ..." (`:1614-1616`).
- **Lost:** when there are no candidates, the block is omitted entirely and the question goes bare (`turn_prep.py:611`; `m3/generation.py:190`). Any matched THIN GROUND rider is dropped with it.
- **Distorted:** two things contradict each other here. The header says anything beyond the listed ids is "our honest limit". The cached prompt holds every witness and limit (Stage 0). When the block holds the wrong records, the voice is told to treat the right answer as unknown.

### Stage 6. The voice drafts (both)
- **Code:** `generation.stream_voice_turn` (`generation.py:57-124`): Sonnet 4.5, `max_tokens=2048`, temperature left at the API default.
- **Out:** the raw draft: prose with inline `[[record.id]]` tags, `[[quote:id]]` and `[[story:id]]` markers.
- **Added:** everything the model brings on its own.
  - Outside knowledge to fill an empty or wrong ground.
  - Echoes of the evidence block's labels ("this turn's ground", "THIN GROUND", invented `[[thin:liturgy]]` tags).
  - Recited demonstration openings.
  - Typed quotations and quote lead-ins that use epithets ("the sage", "our poet") instead of the listed name.
  - Story retellings in its own words.

### Stage 7. Post-draft guards and regeneration (L only)
- Seat-identity guard, Table only (`turn.py:779-826`).
- **Recitation check:** one regeneration when the reply reads out 20 or more words of a demonstration (`turn.py:833-852`; `recitation.py`).
- **Self-revision:** a second call that trims what tagged records do not carry, only on other_tradition first asks (`turn.py:871-891`; `self_revision.py`).
- **Uncited-claims enforcement:** off by default, `CIC_R27_ENFORCE` (`api/config.py:174`; `turn.py:927-984`).
- **A:** none of these runs. LiveModelAnswerer retries only a failed stream (`m3/generation.py:192-197`).

### Stage 8. `apply_net`: shaping the draft (both; "THE one owner of the voice text shape", `turn.py:315-427`)
1. `grounding_net.strip_markdown` (`grounding_net.py:162`) removes headings, rules, and bold or italic label lines.
2. `story_placement.place_stories` (`story_placement.py:120-188`), on desert only (`frame.story_placement`; `records/worlds/desert.yaml`). A valid `[[story:id]]` becomes the record's `telling`, word for word. A marker that cannot be placed loses its sentence, and the lead-in before it (`:164-169`). Then `_without_paraphrase` (`:273-288`) **removes every sentence the voice wrote that is tagged to an offered story it did not place**.
3. `quote_placement.place_quotes` (`quote_placement.py:118-198`). A valid `[[quote:id]]` becomes "lead-in: “modern_rendering” [[id]]".
   - Not offered, already voiced, a second quote, not settable, or refused by `placed_quote_refusal` (`grounding_net.py:1046`; speaker not named, `REASON_SPEAKER_UNNAMED`, `:693`, checked at `:1004-1005`): **the marker's sentence is removed** (`quote_placement.py:162-165`).
   - When the marker stood alone, the sentence before it is also removed if it reads as a lead-in (`_take_lead_in`, `:201-227`).
4. **The net loop** (`turn.py:382-415`). `check_turn_with_paragraph_coverage` (`grounding_net.py:1577-1694`) gives each sentence a verdict (`verdict_for_sentence`, `:1308`; `_claim_verdict`, `:1367-1456`). Then the neighbour pass `_apply_quotation_context` (`:1148-1194`).
   - Sentences withheld for a **quotation reason** (`QUOTATION_DROP_REASONS`, `:702-706`) are **removed**. Typed quotation, attribution without a placed quote, a lead-in to unplaced words, the words that follow an attribution, quote words given without placement, and so on.
   - Sentences that name something **after the window**, which their own cited records do not also name (`turn.py:395-401` → `output_check.ungrounded_horizon_mentions`, `output_check.py:424-433`), are **removed**.
   - The removal itself is `drop_flagged_sentences` (`grounding_net.py:1524-1570`). Its own docstring (`:1545-1550`) says it does not repair "a semantic dangling fragment".
   - The loop repeats until nothing more goes.
   - **Every other withheld sentence (an untagged specific claim, a claim only 20% grounded) ships with its words intact and only loses its citation** (`turn.py:330-333`; `check_turn` doc, `grounding_net.py:1477-1481`).
   - Sentences with honesty phrasing are exempt from the checks (`SCAFFOLD_MARKERS`, `engine/prose.py:169-175`; `grounding_net.py:1374-1382`). "we cannot", "we do not have" and "I am a representative of" all count.
5. `shown_text` (`grounding_net.py:1197-1213`) → `strip_tags` (`:123-127`). This removes only `[[a-z0-9_.-]]` tags and quote and story markers (`_TAG`, `:68`; `_DISPLAY_TAG`, `:120`). **A malformed tag with a colon or capitals, such as `[[thin:liturgy]]`, `[[THIN GROUND: Bolsec]]` or `[[rzg.quote:rzg.quote.x]]`, is not removed and reaches the reader.**
- **Out:** `(text, citations, net_result)`. `net_result.reply_shape.removed` lists each removed sentence with its reason. **Admission discards `net_result`** (`m3/generation.py:203`, `_net_result`), so the run keeps no record of what was cut or why.
- **Lost here:** whole sentences, with no repair of what depended on them (see `turn.py:660-667`: "No sentence is rewritten and no call is made to mend a reply").

### Stage 9. Settling the reply (L only)
- **Code:** `settle_reply` (`turn.py:482-515`, called at `:991-1004`). A reply that `apply_net` emptied, or one that cited records and kept no verified citation, is replaced by the world's own doctrinal witness, word for word (`_answer_record_fallback`, `:433-459`). With no witness, the ungrounded reply is withheld.
- **A:** not run. Admission ships whatever `apply_net` left.

### Stage 10. Decoration and display (L only)
- Citation attachment (`turn.py:1010-1019`, off unless `CIC_CITATION_ATTACH`).
- Source cards (`:1025`), the figure bridge (`:1032-1033`), term glosses (`:1040`), the transparency plan (`:1056-1059`).
- These change no text.

### Stage 11. Checks after the answer exists
- **L:** `check_horizon` is written to `voice_event.output_defects`, report only (`turn.py:1093`). The display, pronoun (first-person "I"), conversational, guard-proximity and malformed-tag families (`output_check.check_output`) run **only offline** in M7 (`engine/m7/offline_checks.py:13,81`).
- `engine/m7/turn_readability.score_turn` has **no caller on either answer path**. Its only callers are `engine/m10/validation.py:140-153` (validation documents) and `engine/m7/standing_measure.py:127`.
- **A:** `harness.run_battery` → `grading.source_boundedness_check` and the advisory `register_check` (`harness.py:94-100`). Nothing else.

### Stage 12. Streaming (L only, when `on_sentence` is set)
- `sentence_stream.SentenceStream` (`sentence_stream.py`) releases sentences before the reply finishes. It holds back any sentence that quote or story placement or the quotation rules could change (`_reshaped`, `:168-178`).
- **It is not given `window_end`** (constructor call `turn.py:759-764`), and `_reshaped` does not test the horizon. The final `apply_net` can later remove a sentence for horizon (`turn.py:398-401`) that was already streamed, although the module says "No streamed sentence is ever taken back" (`:41`). **Unverified at runtime**; see (e).

---

## (b) Diagram

```
 BUILD TIME (both paths)
 ┌──────────────────────────────────────────────────────────────────────┐
 │ records/<world>/*  ──voiced_records (no draft filter)──► m2 builders  │
 │   prompt.txt: voice_craft | world_core Horizon/Formation/Thinness/   │
 │     CAUTIONS "(cite as [[core]])" | terms | witnesses | limits |     │
 │     gravity names | story tellable_as | DEMONSTRATIONS in full        │
 │   NOT in prompt: quotes, contested_claims, forces                     │
 │   repository.json (all types incl. demo, world_core) | coverage.json  │
 └──────────────────────────────────────────────────────────────────────┘
   [DISTORT] build-facing caution and horizon text becomes citable ground;
             horizon gate exempts those two fields (gates.py:1566)

 PER TURN
 participant question / sealed probe
        │
        ▼
 ┌─────────────────────────┐   A: SKIPPED (asks=None, kind=other,
 │ 2 GATE: safety + reader │      no directive) ............. [LOST]
 │   asks, kind, register  │
 └───────────┬─────────────┘
             ▼
 ┌─────────────────────────┐   A: SKIPPED: no speaker-naming rule,
 │ 3 DIRECTIVE (system[2]) │      no "no quote" rule, no story rule,
 │   asks, concision,      │      no 120-220 words, no NO_GROUND
 │   quote/story lines     │      .......................... [LOST]
 └───────────┬─────────────┘
             ▼
 ┌──────────────────────────────────────────┐
 │ 4 EVIDENCE: words → ≤2 cells → records   │  [LOST] probe's own cell ignored;
 │   B: cell coverage + honest_limit        │         wrong cell → wrong limit
 │   A2: full-text fallback, ANY type       │  [ADDED] demos / world_core can
 │   C: tension partner   D: THIN riders    │          enter as "ground"
 │   cap 12                                 │  [LOST] floor line is dead code
 └───────────┬──────────────────────────────┘
             ▼
 ┌──────────────────────────────────────────┐
 │ 5 RENDER: "Ground for this turn (cite    │  [DISTORT] "anything beyond these
 │   only these; beyond = honest limit)"    │   is our honest limit" vs. full prompt
 │   ids | MUST NOT ASSERT | THIN GROUND    │  [LOST] no candidates → no block,
 └───────────┬──────────────────────────────┘          THIN riders dropped too
             ▼
 ┌──────────────────────────────────────────┐
 │ 6 VOICE DRAFT (Sonnet 4.5)               │  [ADDED] outside knowledge, block
 │   prose + [[id]] + [[quote:]] [[story:]] │   labels ("this turn's ground"),
 └───────────┬──────────────────────────────┘   [[thin:x]], demo openings, epithet
             │                                   lead-ins, own story retellings
             ▼
 ┌─────────────────────────┐   A: SKIPPED (recitation regen,
 │ 7 GUARDS / REGENERATE   │      self-revision) ........... [LOST]
 └───────────┬─────────────┘
             ▼
 ┌────────────────────────────────────────────────────────────┐
 │ 8 apply_net                                                 │
 │  a strip_markdown                                           │
 │  b place_stories ── unplaced story → sentence REMOVED       │  [LOST]
 │                    own retelling of offered story REMOVED   │  [LOST]
 │  c place_quotes ─── bad marker / unnamed speaker → REMOVED  │  [LOST]
 │                    + preceding lead-in REMOVED              │
 │  d net loop ─────── quotation reasons → REMOVED             │  [LOST]
 │                    post-window, uncited by its record → REM │
 │                    other withholds → SHIP, tag dropped      │  [DISTORT]
 │                    scaffold phrases ("we cannot") exempt    │
 │  NO REPAIR of "he", "so", "That is...", announced teaching  │  ◄ cause 1
 │  e strip_tags: [[thin:x]] / [[A B: c]] NOT stripped         │  [ADDED]
 └───────────┬────────────────────────────────────────────────┘
             ▼
 ┌─────────────────────────┐   A: SKIPPED: damaged or empty text
 │ 9 settle_reply          │      ships as graded ......... [LOST]
 │  (fallback to witness)  │
 └───────────┬─────────────┘
             ▼
 ┌─────────────────────────┐
 │ 10 cards/gloss/figures  │  (L only, display, no text change)
 └───────────┬─────────────┘
             ▼
  TEXT THE PARTICIPANT READS
             │
             ▼
 ┌──────────────────────────────────────────────┐
 │ 11 CHECKS                                     │
 │  L: horizon report-only; pronoun/display/tag  │  no readability gate on
 │     families offline (M7)                     │  either path
 │  A: source_boundedness (passes by construction│
 │     on net-verified tags) + advisory register │  → 28/28 auto PASS
 └──────────────────────────────────────────────┘
```

---

## (c) Failure table

"Both" means the mechanism exists on the live path too. Worlds come from the reviews. The removal counts come from my script over `raw_text` vs `answer_text`. That count is an upper bound, because a placed quote rewrites its sentence and so also counts as "removed". Cappadocian has no run JSON (its harness refused to write it, see row 13), so its count comes from the review.

| # | Failure type | Stage where it enters | Mechanism in code (file:line) | Worlds affected (data) | Fix location | General or per-world |
|---|---|---|---|---|---|---|
| 1 | **Removed sentence, dependent sentence left behind**: orphan "he" or "she", a "so" with nothing before it, a lead-in to a quote that is gone, announced teaching never given | 8b, 8c, 8d (both paths); made worse by the missing directive in admission (Stage 3) | Removal: `story_placement.py:157,164-169,273-288`; `quote_placement.py:162-165,201-227`; `turn.py:392-415` → `grounding_net.drop_flagged_sentences` `:1524`. The dangling case is admitted at `:1545-1550`. No repair by design (`turn.py:660-667`). `_apply_quotation_context` (`grounding_net.py:1148-1194`) widens removals forward (followers, lead-ins) but never back-references. | **All 12.** Draft sentences missing from the shipped text: alx 33 (18 probes), desert 58 (18), don 4 (4), gallic 34 (13), hal 27 (15), ijc 38 (14), lpc 53 (16), pahc 32 (18), rzg 7 (5), syr 25 (13), witt 38 (14); cappadocian: residue in F4-E (P1), F6-T, F2-T, F1-E. Quote markers drafted → sentences citing a placed quote: alx 20→9, desert 7→1, don 2→0, gallic 11→2, hal 30→6, ijc 11→5, lpc 22→4, pahc 22→2, rzg 10→5, syr 16→0, witt 16→4. P1 from cuts: desert 4+, ijc 4, pahc 3, hal 2, witt 1, cappadocian 1, gallic 1, rzg 1. | Engine: after a removal, also remove sentences that point back to the removed one (pronoun or demonstrative with no antecedent left, a sentence-initial connective, a colon lead-in), or regenerate once with the removed reasons named (the same append channel as `_append_r27_correction`, `turn.py:285-299`). Harness: keep `net_result.reply_shape` in the transcript. | **General** (engine) |
| 1b | Story retold in the voice's own words, then removed whole | 8b; admission has no story directive | `_without_paraphrase` (`story_placement.py:273-288`); `STORY_PLACE_LINE` ("Never tell the story yourself", `:91-95`) is sent only in the live directive (`turn_prep.py:433`) | desert only (`story_placement: true`). Most removals of any world (58); 4 FAIL rows (c-i, f1-i, f1-e, f5-e) | Harness: send the directive. Engine: the same dependent-sentence rule as row 1 | General (harness), affects story_placement worlds |
| 2a | **Cell's own record not offered** | 4 (both; worse in admission) | Stage A matches the probe's wording only (`evidence.py:493-636`). The harness knows the cell and ignores it (`m3/generation.py:178-186`). No reader asks or kind in admission. Candidates come only from the matched cell's coverage (`:856-957`). | don 16 of 28 (P1 f1-e, f2-e); pahc 13 of 28 (P1 f2-e, f4-t, f5-p, f6-e, f6-p); cappadocian F2-E, F6-I; hal f5-p, f6-p, f3-i; ijc f1-p, c-e, f1-t; syr f6-p; gallic f1-e | Engine: route on the reader's asks plus the cell's own question vocabulary; add hint lines (`retrieval.retrieve_when`) phrased the way probes ask. Records: `retrieve_when` per witness. Harness: optionally report "cell's own record offered: yes/no" per probe. | General (engine). Per-world for hints |
| 2b | **No record for the question type at all** (original sin, fate of outsiders, being born again, apostolic practice, survival today) | 0 (records) → shows at 4/6 | The coverage gate counts a cell as covered by any record tagged to it (`m1/canon.classify_cell`, `canon.py:129-152`). It does not check that the record answers each kind of question the cell holds. Empty ground → bare question (`turn_prep.py:611`, `m3/generation.py:190`). | alx (F4-T, F5-I, F5-P: invented detail); cappadocian (F6-T, F6-E); gallic (f2-p, f4-t); hal (f1-i, f2-i); ijc (f3-t, f5-e, f6-t); rzg (7 cells: F1-T, F4-T, F4-E, F6-T, C-T, F6-P, F3-T); syr f1-e; witt c-t (Augsburg Art. I); pahc f5-p, f3-t | Record: author the witness, contested claim or honest limit, verified against vendored text | **Per-world** |
| 3 | **Voice not told what is unknown**: silence answered with a claim, or a false "our record does not develop that" | 4/5 (both) | (i) An honest limit enters only with its matched cell (`evidence.py:912-917`). A wrong cell gives the wrong limit or none. (ii) The "no ground" floor line is never used (`evidence.py:78-103`, no caller). (iii) Empty candidates → no block, no THIN riders (`turn_prep.py:611`; `m3/generation.py:190`). (iv) The block header "anything beyond them is spoken as our honest limit" (`evidence.py:1563-1564`) and the shape's `limit_discipline` turn a wrong ground into a false silence. (v) `NO_GROUND_LINE` is live-only (`turn_prep.py:434-435`). | gallic (f1-t, f6-t); rzg (f1-t, f4-e, f4-t, f6-t); cappadocian (f6-t false silence, f6-e); ijc (f5-e, f6-i); syr f6-e; hal f3-t; don f1-e (false "we cannot tell you procedures") | Engine: when no cell or a weak cell matched, offer the world's honest limits and thin topics, and drop "beyond these = honest limit" from the header (tell the voice the prompt is also its record). Record: honest limits written per question type. | General (engine) + per-world (limits) |
| 4a | **Frame break: evidence-block vocabulary spoken** ("the ground given for this turn", "the records I am holding", "THIN GROUND notes", "we cite only what is vendored") | 5 → 6 (both); admission lacks the live directive and the recitation retry | The block's labels (`evidence.py:1563-1568,1614-1616`) and the shape (`fleet_voice` lines 34, 36) use "ground" and "this turn". Honesty phrasing exempts a sentence from the net (`grounding_net.py:1374-1382`; `prose.py:169-181`). No live check for this phrase class: output families run offline only (`m7/offline_checks.py`). | Answers with these phrases (script): desert 3, gallic 5, syr 4, lpc 3, ijc 2, pahc 2, witt 2, alx 1, rzg 1, cappadocian (f6-e, f2-e). P1: cappadocian f2-e, f6-e; desert f2-e, f6-e; syr f2-e, f6-e, f6-p; witt f2-e; lpc f2-e; alx f2-e | Engine: rename the block labels to words the voice may never say, and add a live check that holds build words ("this turn", "ground", "record id", "vendored", "the system", "I am holding"). Shape: drop "this turn" from `limit_discipline`. | General |
| 4b | **Raw tags shipped** (`[[thin:liturgy]]`, `[[THIN GROUND: Bolsec]]`, `[[rzg.quote:...]]`) | 6 → 8e (both) | `strip_tags` matches only `\[\[[a-z0-9_.-]+\]\]` and the quote and story markers (`grounding_net.py:68,120,123-127`). The `_ANY_TAG` display check (`output_check.py:78`) runs offline only. | desert (2 tags in f6-e); rzg (2) | Engine: strip any `[[...]]` at display and withhold its sentence; render THIN GROUND without bracket syntax | General |
| 4c | **Demonstration recited / record opening spoken as the answer** ("I am a representative of the desert communities", "You ask who started us", "You have asked us three questions") | 0 + 4 (A2 fallback) → 6; the live-only retry is missing in admission | Every demonstration is in the prompt (`builders.py:464-473`). The full-text fallback can offer a demo or world_core with head `all_text` (`evidence.py:321,352-402`). The recitation retry runs only live (`turn.py:833-852`). "I am a representative of" is sanctioned and exempt (`prose.py:181`). | desert f6-p, f4-e, f1-t, f5-i; don f1-t (limit "three questions"); ijc f6-p; hal f6-p (demo keyed to question not led); syr (demo-sourced wording) | Records: write demonstrations and limit statements so any sentence stands alone. Engine: exclude demo, voice_craft and world_core from the full-text fallback; run the recitation check in admission. | General (engine) + per-world (records) |
| 5 | **After-window knowledge** (later churches, councils, movements, "in later centuries") | 0 (core text) and 6; the 8d check catches only dated items | `m1/horizon.post_window_mentions` knows 29 gazetteer events (`m1/data/gazetteer.yaml`), explicit era years and centuries. It does not know names without dates or time words such as "later" or "never became". The check exempts a sentence whose own cited record names the same thing (`turn.py:398-401`, `output_check.py:424-433`), and `_groundable_text` of world_core includes its horizon and cautions (`grounding_net.py:221-235`), so citing the core clears it. The gate exempts those fields (`gates.py:1566`). The live `check_horizon` is report-only (`turn.py:1093`). | don f3-t (Gregory, 590s, from core horizon); ijc f3-t, f6-i, f5-e (caution 7 lists Leo 461, 476); hal f3-t ("different centuries", "never became"); syr f1-e, f2-e, f3-t (undated later churches); pahc f3-t; lpc (live rows) | Record: move post-window text out of voice-read fields (horizon/caution → `use_note` or an analytic field). Engine: stop exempting world_core as a ground for horizon; widen the scanner to later-church names and time words; make the gate cover horizon and cautions. | Record per-world; engine general |
| 6 | **Admission harness differs from live** (see (d)) | 2, 3, 7, 9, 11 | `m3/generation.py:178-227` vs `turn.py:529-1131` | syr (every quote removed: epithets, no speaker-naming line; 13 answers); don (3 quote lead-ins cut); desert (story retellings removed); readability not gated: alx 2, ijc 2, rzg 7 "gate only" P1s, desert 2, pahc 1; cappadocian (retry broke the report) | Harness: build the request with `prepare_voice_turn_inputs` plus a stored reader result (or a fixed Directive from the probe), call `_run_ordinary_voice_turn` directly, and add readability and output_check to grading. | **General** (harness) |
| 7a | **Cautions too general, or read aloud** | 0 (prompt build) → 6 | Cautions compile as citable ground "(cite as [[core]])" (`builders.py:414`). They are written as imperatives to the builder. Nothing applies a caution to a specific claim at runtime. Riders give `claim_guards`/`not_for` as "MUST NOT ASSERT: <modern sense>" (`evidence.py:1599-1610`), which the voice can misread as a denial. Formation logic is etic text, also citable (`:412`). | alx f2-e, c-e (caution 3 ignored); don f3-t, f1-i, f1-t; ijc caution 6/7 (f1-t, f6-t, f3-t); cappadocian f1-e (formation logic spoken), f4-t (not_for misread as "That phrase is not ours"); gallic f2-e, f3-t; desert f1-t, f5-i, f6-p; lpc caution 17 (f2-e reads tagging rules aloud); witt f1-i (voice_craft "uncommanded"); pahc f3-t (formation_logic build words); syr f2-e, f3-t, f6-e | Record: split cautions into (a) a voice-safe statement, emic and claim-specific, attached to the records it governs as `claim_guards`, and (b) builder notes the prompt never carries. Builder: emit cautions above the line as instruction with no id, or not at all. | Per-world wording, general builder change |
| 8 | **Withheld specific claims ship** (untagged or weakly grounded factual sentences) | 8d (both) | Only quotation and horizon reasons remove a sentence. Other withholds keep their words (`turn.py:330-333`; `grounding_net.py:1436-1456`). | syr f1-e ("twenty-three Demonstrations, each..." 25% grounded); hal f2-i, f2-p, f1-p (invented lead-in detail); don (citations to records that do not hold the sentence, P2) | Engine: a withheld specific claim (proper noun, number) is removed or regenerated, not shipped | General |
| 9 | **Quote words inside witness text** removed as "quote words without placing" | 0 + 8d | `QuotationIndex.quote_words_of` (`grounding_net.py:451`), `_unplaced_quote` (`:1127-1145`) → `REASON_QUOTE_WORDS` in the drop set | witt (residue in c-p, c-t, f2-t, f4-t, f5-i, f6-t; c-i P1); don (Petilian line inside witness) | Record: witness text uses a placeholder, or paraphrase, never a quote record's words | Per-world |
| 10 | **Long answers and paragraphs** (readability, focus) | 3 (admission lacks concision) | `CONCISION_DIRECTIVE` (`turn_prep.py:221-226`) is live-only. No per-turn readability gate anywhere (Stage 11). | All; e.g. don: 22 of 28 answers have a sentence over 30 words and 10 have paragraphs of 8 to 16 sentences; alx up to 474 words | Harness parity, plus a runtime readability gate | General |
| 11 | **Harness drops a world's automatic result after a retry** | A only | `_VOICE_CALL_ATTEMPTS=3` (`m3/generation.py:39,192-195`) makes extra calls, then `_run_world` demands exactly one call per probe (`live_admission_run.py:335-340`) | cappadocian (no `cappadocian.json`) | Harness: count attempts per probe | General |
| 12 | **Live only: streamed sentence could later be removed for horizon** | 12 | `SentenceStream` gets no `window_end` (`turn.py:759-764`); `_reshaped` has no horizon test (`sentence_stream.py:168-178`) | Not observed in this data (admission does not stream). **Unverified** | Engine | General |

---

## (d) Admission harness vs the live path: every difference that changes output

Live: `engine/api/wiring.py:1101-1130` → `turn.run_turn` (`turn.py:1175-1422`) → `_run_ordinary_voice_turn` (`:529-1131`). Admission: `live_admission_run._run_world` (`:315-380`) → `harness.run_battery` (`harness.py:64-111`) → `LiveModelAnswerer.answer` (`m3/generation.py:178-227`). On a first live interview turn (no history, nothing told yet), the two paths differ as follows.

**Inputs to retrieval (Stage 4)**
1. **No reader asks.** Live: `asks=directive.asks` (`turn_prep.py:594`), and asks are added to the query words (`evidence.py:405-407`), which changes cell matching, Stage B scores and thin-topic hits. A: `asks=None` (`m3/generation.py:181`).
2. **No question kind.** Live: `kind=resolve_kind(...)` (`turn_prep.py:579-587`) sets the per-type floors (`evidence.py:174-184`). For example, a "who" question gets 2 witnesses and 0 forces, and a "what_did" question gets 3 stories. A: `kind` is not passed, so the default floors (1, 3, 2, 2, 2, 1, 1) apply.
3. **No `words_asked`.** Live: `asks_for_the_words(kind, message)` (`turn_prep.py:588`) can raise the quote floor. A: False.
4. **The probe's own cell is discarded.** `answer(cell, probe_text)` never reads `cell` (`m3/generation.py:178`). The live path has no cell either, so this is parity, but the harness throws away the one signal that would separate a routing miss from a record gap.
5. Rhythm: live passes `tally_from_transcript(...)` (`wiring.py:1118`). A passes none. On a first turn `quote_due` is True, so the quote floor is the same. **No output difference expected on turn 1** (verified by reading `evidence.py:883`, `rhythm.py:31-36`).

**The request (Stages 3, 5, 6)**

6. **No system[2] directive at all** (`m3/generation.py:193` passes no `turn_directive`; `voice_request.py:54-55`). Each part missing in admission changes output:
   - a. `QUOTE_OFFERS_LINE` with "its sentence naming <speaker_name>" (`turn_prep.py:313-321`), and `QUOTE_SPEAKER_LINE` (`:276-283`). The voice is not given the exact name the net requires (`grounding_net.names_speaker`, `:420-431`), so epithet lead-ins fail `REASON_SPEAKER_UNNAMED` and the quote and its lead-in are removed. (syr: every quote removed; don: c-i, c-t, f3-i.) The shape segment (fleet_voice `citation_contract`) states the rule in general, so the voice is told the rule but not the name to use.
   - b. `NO_QUOTE_LINE` (`:269-272`): "Put no one's words in quotation marks or after 'said', 'wrote' or a colon." Without it, the voice types quotations and attributions, and the net removes them (`QUOTATION_DROP_REASONS`).
   - c. `QUOTE_DUE_LINE` / `QUOTE_OPTIONAL_LINE`: how many quotes to try.
   - d. Story lines (`story_placement.py:111-117`; `turn_prep.py:433`): "Never tell the story yourself". Without them, desert's retellings are removed by `_without_paraphrase`.
   - e. `CONCISION_DIRECTIVE` (`turn_prep.py:221-226`): answer first, 120 to 220 words, never restate the question.
   - f. The kind line (`KIND_DIRECTIVES`, `:229-262`), including the oblique-who rule.
   - g. `NO_GROUND_LINE` (`:284-287`) when no candidates: "tag only with ids printed after 'cite as'".
   - h. `LEXICON_LINE`, `REFER_BACK_LINE`, the register note and `personal_wound` suspension (`:438-444`), ambiguity readings (`:445-458`).
   - i. The other-tradition rule (`_other_tradition_directive`, `:89-218`), including the fixed honest-limit sentence. In admission, a probe naming another tradition gets no such rule.
7. Live can put the directive into the user message instead (`CIC_DIRECTIVE_IN_USER_MESSAGE`, `voice_request.py:33-44`). Not applicable to A.

**After the draft (Stages 7-9)**

8. **No recitation check or retry** (`turn.py:833-852`). Recited demonstration openings ship in A.
9. **No self-revision** on other-tradition questions (`turn.py:871-891`; default on live, `api/config.py:175`).
10. **No `settle_reply`** (`turn.py:991-1004`). Live replaces an emptied reply, or one with no verified citation left, with the world's doctrinal witness word for word. A ships the damaged or empty text.
11. **No routing.** Live can send a message to a Facilitator turn instead of the voice: `system_nature_turn`, `etic_turn`, `bridge_turn` (which rewrites the message to its underlying subject and bars the modern term, `turn.py:1339-1387`), or a safety route. A always asks the voice with the raw probe.
12. Not part of the difference: the uncited-claims enforcement (`r27_enforce`) and citation attachment are off by default on live too (`api/config.py:174,176`), and the seat guard is Table-only.

**Grading and recording (Stage 11)**

13. Live writes `check_horizon` defects (`turn.py:1093`) and runs the M7 output families afterwards. A runs only `source_boundedness` and the advisory `register_check`. **Neither path gates readability per turn.**
14. A discards `net_result` (`m3/generation.py:203`), so removed sentences and their reasons are not in the report.
15. A retries a failed stream up to 3 times (`m3/generation.py:192-195`), which breaks the one-call-per-probe check (`live_admission_run.py:336-340`; cappadocian). Live raises on the first failure (`turn.py:774-775`).
16. Same in both: shape segment, world prompt, model pattern (`us.anthropic.claude-sonnet-4-5`, `api/config.py:16` and `live_admission_run.py:85`), `max_tokens=2048`, temperature default, `OFFER_CAP`, `with_placeable_stories`, `PlacementContext.for_evidence` (the same offered quotes as live `prepared.offered_ids`), and `quotable_texts=[probe_text]` (= live `echo_sources` on turn 1). The `apply_net` code itself is shared.

---

## (e) What I could not determine from code, and a small free experiment for each

1. **Why each sentence was removed.** The harness discards `net_result.reply_shape` (`m3/generation.py:203`). *Experiment (free, deterministic):* re-run `turn.apply_net` on each saved `raw_text` in `engine/m3/reports/fleet-graded-run-1/*.json`, using the same `PlacementContext.for_evidence` from a re-run `assemble_evidence`, and tabulate `reply_shape.removed[*].why` per world. This splits row 1 into speaker-unnamed, typed quotation, story paraphrase, horizon and so on. Run it at each world's own commit (fact 3).
2. **Whether the code I read is the code each world ran.** Eleven different commits (fact 3). *Experiment:* `git diff <run commit>..HEAD -- engine/m4 engine/m3 engine/shape` for each world.
3. **The evidence block each probe actually got**, and how often the full-text fallback offered demonstrations or world_core. *Experiment (free):* run `assemble_evidence(message=probe, asks=None, ...)` for the 336 probes. Count (a) probes whose cell's own coverage records are absent (to confirm don 16 and pahc 13 and extend the count to all worlds), (b) candidates of type demonstration, world_core or voice_craft, (c) probes with empty candidates (bare question, THIN riders lost).
4. **How much the live directive would change outputs.** That needs model calls. *Free part:* build both requests byte for byte (`build_voice_request` with and without `prepare_voice_turn_inputs`' directive, using a hand-set `Directive(asks=[{"text": probe}], kind=<hand label>)`) and diff them. This shows exactly what text admission withholds. The paid part (re-run, e.g., syr and desert with the directive) needs Mark's approval as a named live test.
5. **Whether reader asks and kind would fix routing.** That needs Haiku reader calls (spend). *Free proxy:* hand-label kind for the 28 probes, re-run `assemble_evidence` with `kind=` and `asks=[probe]`, and compare cell hits against item 3.
6. **That `[[thin:...]]` and similar tags survive display.** Inferred from the regex. *Experiment:* `strip_tags("We cannot say [[thin:liturgy]].")` in a REPL. One line, free.
7. **The streaming horizon mismatch (row 12).** Inferred, not observed. *Experiment:* a unit test feeding `SentenceStream` a reply whose second sentence names "the Council of Chalcedon" in a world closing before 451, with a tagged first sentence. Compare the released events with `apply_net`'s text.
8. **Whether `status: draft` records are meant to ship.** No filter in `voiced_records` or `build_repository_json`. I could not find a gate on status for packaging. *Experiment:* grep `engine/m1/gates.py` for "draft", and list draft records per world in `records/*/*/*.md`.
9. **The `CIC_OFFER_CAP`, `CIC_R27_ENFORCE`, `CIC_SELF_REVISION` and `CIC_CITATION_ATTACH` values in the production environment** (deploy config was not in the checkout). The live-path claims above assume the code defaults.
10. **Cappadocian removal counts.** The run JSON was never written (row 13). *Experiment:* run the script used here on `cappadocian.json.answers.jsonl`. It has no `raw_text`, so this needs the stdout log or the ledger, if they kept it. Otherwise this one is not recoverable.

Claims marked "inferred" or "unverified" above are row 12 and items 6 to 9. Everything else is cited to the line that does it.
