# Replay of the cut step (apply_net) on fleet graded run 1

## Summary

- **The replay matches the run exactly.** `apply_net` was re-run on every saved draft (`raw_text`). It gives the shipped `answer_text` **byte for byte in 308 of 308 probes** across 11 worlds, and the same citation set in 308 of 308. No model or network call was made.
- **Every sentence missing from a shipped answer was cut by the engine's `apply_net`.** The admission harness cuts nothing itself. There were 297 cuts in all. Every one has a quotation or story reason, and none was cut for the horizon.
- **One reason causes the most cuts and the most damage:** "lead-in to a placed quote does not name its speaker". It accounts for 81 cuts (27%), and 44% of them leave an orphaned next sentence. Each of these cuts also loses the record's own quote, which code would have set in place.
- **The orphan check is a simple rule, and it flags 95 cuts** (that is, 95 places where the next shipped sentence opens with a pronoun, demonstrative or connective). I read 30 of them by hand, and 18 were real damage (a lost referent, or a pronoun now pointing at the wrong person). That puts the number of real orphans at about 55 to 60.
- **Some cuts removed true, well-grounded sentences.** At least 30 removed sentences appear word for word in a record that the sentence itself cites. 44 contain a quoted span that is word for word in the records. 22 of the 28 desert story-retelling cuts are at least 80% grounded in the story record they cite.
- **Whether the live directive would prevent these cuts is mostly unproven.** The code proves only that `apply_net` is the same on both paths. The directive changes the draft, not the cut. For **28 cuts** (desert story retellings), the admission request told the voice to do exactly what the engine then cut. For **4 cuts**, the "no quote offered" rule exists only in the directive. Everything else is unverified. On the live path, the speaker-unnamed reason fired 3 times in 65 turns. In admission it fired 81 times in 308 answers. That is suggestive only.

## 1. Method

Work dir: `/tmp/claude-0/-home-user/233cea43-1945-55ed-85c1-124ce73e9be5/scratchpad/replay/`. The repo checkout was not touched. `engine/`, `records/` and `canon/` were copied to `replay/repo/`, and everything ran from that copy. Every command ran with all `AWS*` and `ANTHROPIC*` variables unset.

1. **Packages** (`build_packages.py`). These were compiled in memory with `engine.m2.compiler.compile_world`, which reads local records only and makes no model call. The `compiled/` files were written to `replay/packages/<world>/`.
   - The `restore` command could not be used, because it needs the stored `packages/<world>/<id>/manifest.json`, and `packages/` is not in the sparse checkout.
   - The rebuilt `compiled_content_hash` **does not match** the run's `package_content_hash` for any world. Records or builders have changed since the run.
   - The checkout has a single commit (`3785a6e`, shallow), so I could not check out the 11 run commits or tell which compiled file differs.
   - `shape_hash` and `seal_hash` **do** match the run for all 11 worlds, so the shape segment and the sealed probes are unchanged.
2. **No-call stubs** (`nocall_stubs.py`). `anthropic`, `httpx`, `boto3` and `botocore` are not installed. Importing `engine.m4.turn` needs them at module level, so they are replaced by stub modules whose client classes raise if anyone builds one.
3. **Replay** (`replay.py`). This copies `LiveModelAnswerer.answer` (`engine/m3/generation.py:178-210`) exactly, minus the voice call. For each probe it:
   - runs `assemble_evidence(message=probe, asks=None, ...)`;
   - on desert, runs `with_placeable_stories`;
   - calls `apply_net(raw_text, quotable_texts=[probe], window_end=frame.time_window.end, placement=PlacementContext.for_evidence(...))`.

   The probe text comes from `engine.m3.sealed_probes.read_probe`, as the harness reads it. No probe text is written to any output.

   The cut reasons are `net_result["reply_shape"]["removed"]`, which admission throws away at `generation.py:203`.
4. **Analysis** (`analyze.py`, `classify_speaker.py`, `live_compare.py`). Each cut was located in the draft, and the next shipped sentence was found. Three further measures were then taken:
   - the orphan rule (§4);
   - the net's own claim test (`grounding_net._claim_verdict`) with the quotation checks set aside;
   - whether the sentence is word for word in a record it cites.

**Not covered:**
- **cappadocian.** Its run kept only `answers.jsonl`, with no `raw_text` (I checked its stdout and ledger too). There is nothing to replay.
- **rzg.** Only `rzg-attempt2.json` was used.

## 2. Reproduction match rate

| World | Probes | answer_text exact | citations exact | Probes with ≥1 cut | Cuts |
|---|---|---|---|---|---|
| lpc | 28 | 28 | 28 | 16 | 45 |
| gallic | 28 | 28 | 28 | 13 | 30 |
| desert | 28 | 28 | 28 | 17 | 50 |
| ijc | 28 | 28 | 28 | 14 | 34 |
| alx | 28 | 28 | 28 | 17 | 24 |
| witt | 28 | 28 | 28 | 14 | 31 |
| rzg (attempt2) | 28 | 28 | 28 | 5 | 7 |
| pahc | 28 | 28 | 28 | 17 | 25 |
| hal | 28 | 28 | 28 | 15 | 26 |
| syr | 28 | 28 | 28 | 13 | 21 |
| don | 28 | 28 | 28 | 4 | 4 |
| **All** | **308** | **308 (100%)** | **308** | 145 | **297** |
| cappadocian | – | not replayable (no draft saved) | | | |

**What the match shows:**
- The text and the citation sets match exactly even though the package content hash does not. So whatever changed in the packages since the run does not touch anything `apply_net` or quote/story placement used on these drafts.
- An exact text match is strong evidence, but not proof, that the *reasons* are the run's own. In principle, older code could have cut the same sentence under another label. I found nothing that suggests it did.
- No answer was emptied. No sentence was cut for the horizon (`window_end` was set for every world).
- FLOW_MAP's per-world "removed" counts are upper bounds that include placed quotes (for example, alx 33 there against 24 actual, and desert 58 against 50).

## 3. Cut reasons by world

The reason strings are the engine's own.

| Reason (exact engine string) | lpc | gallic | desert | ijc | alx | witt | rzg | pahc | hal | syr | don | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| lead-in to a placed quote does not name its speaker | 8 | 8 | 6 | 1 | 4 | 2 | 5 | 18 | 12 | 15 | 2 | **81** |
| quotation typed by the voice | 15 | 1 |  | 8 | 4 | 10 | 2 | 1 |  |  | 1 | **42** |
| tagged to a quote record that has not been placed |  | 6 | 9 | 7 | 5 |  |  | 1 |  | 4 |  | **32** |
| tells an offered story without placing it |  |  | 28 |  |  |  |  |  |  |  |  | **28** |
| words attributed without a placed quote | 5 | 3 | 1 | 4 | 4 | 3 |  | 1 | 2 |  | 1 | **24** |
| placed quote does not match its record | 6 |  |  | 4 | 5 |  |  | 2 | 5 | 1 |  | **23** |
| second placed quote in one reply | 4 | 1 |  | 1 | 1 | 10 |  |  | 5 |  |  | **22** |
| words after an attribution, not a placed quote | 5 | 2 | 3 | 7 | 1 | 4 |  |  |  |  |  | **22** |
| gives a quote record's words without placing it | 2 | 9 | 2 | 2 |  | 2 |  | 2 |  | 1 |  | **20** |
| quote record not in this turn's evidence |  |  |  |  |  |  |  |  | 2 |  |  | **2** |
| second placed story in one reply |  |  | 1 |  |  |  |  |  |  |  |  | **1** |
| **Total** | 45 | 30 | 50 | 34 | 24 | 31 | 7 | 25 | 26 | 21 | 4 | **297** |

**Which stage made each cut:**
- **Placement step:** "lead-in ... does not name its speaker", "placed quote does not match", "second placed quote" and "quote record not in this turn's evidence" are mostly cut here, at `quote_placement.py:156-165` via `placed_quote_refusal`. The marker's whole sentence goes, and with it the quote that code would have set.
- **Story step:** "tells an offered story without placing it" is cut by `story_placement._without_paraphrase` (`story_placement.py:273-288`).
- **Net loop:** the rest are cut there (`turn.py:382-415`, `QUOTATION_DROP_REASONS`).

## 4. Damage: orphans left by each reason

**The orphan rule is a heuristic, not a parser.** A cut is flagged when two things are true:
- the next shipped sentence opens with a pronoun (he, she, it, they, his, her ...), a demonstrative (this, that, these, those, such, here, there), a connective (so, but, yet, and, then, thus, for, also, still ...), or a phrase such as "In that", "By this" or "The same";
- the cut sentence was the last one cut before that shipped sentence. When several sentences in a row are cut, only the last counts.

**How accurate it is:** I read 30 flagged cases by hand. 18 were real damage: the referent was gone, or a pronoun now pointed at the wrong person. 12 were false positives, where the referent was still in the sentence before. So the true orphan count is about 55 to 60 of the 95 flagged. The rule also misses dependent sentences that open with neither kind of word, such as "Grief itself was allowed."

The grounding columns are explained in §6.

| Reason | Cut | Orphan flag | % flagged | ≥0.8 grounded in own tags | verbatim in own tagged record | quoted span verbatim in records |
|---|---|---|---|---|---|---|
| lead-in to a placed quote does not name its speaker | 81 | **36** | 44% | 3 | 1 | 0 |
| quotation typed by the voice | 42 | **16** | 38% | 25 | 17 | 31 |
| tagged to a quote record that has not been placed | 32 | 10 | 31% | 8 | 1 | 0 |
| tells an offered story without placing it | 28 | 2 | 7% | 22 | 4 | 0 |
| words attributed without a placed quote | 24 | 4 | 17% | 7 | 0 | 0 |
| placed quote does not match its record | 23 | 10 | 43% | 1 | 0 | 13 |
| second placed quote in one reply | 22 | 7 | 32% | 2 | 0 | 0 |
| words after an attribution, not a placed quote | 22 | 2 | 9% | 9 | 6 | 0 |
| gives a quote record's words without placing it | 20 | 8 | 40% | 4 | 1 | 0 |
| quote record not in this turn's evidence | 2 | 0 | – | 0 | 0 | 0 |
| second placed story in one reply | 1 | 0 | – | 0 | 0 | 0 |
| **Total** | 297 | **95** | 32% | | 30 | 44 |

Flagged orphans by world: pahc 18, lpc 16, alx 11, hal 11, desert 9, witt 8, ijc 7, syr 6, gallic 5, rzg 3, don 1.

**Hand-confirmed examples:**

| World / probe | Cut sentence | Next shipped sentence | What went wrong |
|---|---|---|---|
| hal f2-p | "Paula entered that cave and said ..." | "She was not reporting a vision." | "She" has no referent |
| pahc f3-e | "Another writer - a satirist ... said we believed ourselves immortal ..." | "He meant it as mockery." | "He" now points at the man in the sentence before |
| syr c-t | "Our own sage put it plainly: ..." | "He strung Scripture's own names together ..." | "He" has no referent |
| hal f5-i | "Her daughter learned it after her" | "That tells you what they prized ..." | "That" has no referent |
| witt f6-t | the original-sin sentence | "That condition, inherited and real, is where the judgment begins." | the condition is never stated |
| lpc f4-i / f5-i | the Confessions sentence | "But he wrote that down years afterward ..." | "he" and "that" have no referent |
| lpc f3-i | "He wrote:" (marker cut) | "These are real, substantial differences." | "These" has no referent |

The pahc f3-e case shows that a cut can change meaning as well as dangle: the pronoun silently picks up a different antecedent.

## 5. Answers

### Q1. Which cut reasons do the most damage?

1. **"lead-in to a placed quote does not name its speaker"** (81 cuts, 36 orphan flags). It is the largest reason across the fleet, and the top reason in pahc (18), syr (15), hal (12) and rzg (5), tied in don. Elsewhere the top reason is: lpc, typed quotation; gallic, quote words; desert, story; witt, typed quotation and second quote. Each cut loses two things at once: the voice's sentence and the record's own quote. `classify_speaker.py` (a heuristic) sorts the lead-ins into:
   - **34**: no attribution at all. The voice wrote the quote's content in its own words and ended the sentence with the marker, for example "Grace always cooperates with our will ... [[quote:...]]".
   - **17**: a pronoun lead-in ("He wrote:").
   - **17**: an epithet or unnamed source ("Our own founder put it plainly:", "One of our teachers wrote ...", "our poet").
   - **13**: other forms, such as naming someone else or "One of us taught ...".
   - In 11 cases the speaker was named in the sentence just before.
2. **"quotation typed by the voice"** (42 cuts, 16 orphan flags; lpc 15, witt 10, ijc 8).
3. **"placed quote does not match its record"** (23 cuts, 10 orphan flags). The lead-in attributes the words to someone other than the record's speaker, or adds its own quotation.
4. **"tagged to a quote record that has not been placed"** (32 cuts, 10 flags) and **"gives a quote record's words without placing it"** (20 cuts, 8 flags).
5. **The story cut on desert** (28 cuts) leaves few pronoun orphans (2). It removes the voice's whole retelling instead, and the content was mostly true (see Q3).

All of this damage happens because a sentence is cut and nothing is repaired afterwards (`grounding_net.drop_flagged_sentences` docstring; `turn.py` "No sentence is rewritten"). **It is engine behaviour, and it would be the same on the live path for the same draft.**

### Q2. How many cuts would not happen if admission sent the live directive?

**What the code proves:**
- `apply_net` is one function shared by both paths. Given the same draft and the same `PlacementContext`, it cuts the same sentences. The directive changes only what the model writes. So **no cut is proven to disappear**. Every avoided cut depends on the model obeying an instruction, which needs a paid run to measure.
- Live evidence assembly would also differ (reader asks and kind change which quotes are offered). That needs a Haiku reader call, so it was not run.

**What the code does prove about the request each cut ran against.** The comparison uses the admission request: shape segment, world prompt, evidence block, no directive.

| Reason (cuts) | Rule in the admission request? | What only the directive adds | Verdict |
|---|---|---|---|
| tells an offered story without placing it (28) | **Contradicted.** The shape's `story_quote_reach` says "Where the question earns a story, tell it from its retelling in the ground, tagged the same way". The evidence block line says "[[story:id]] ... to place (cite as [[id]])" (`evidence.py:1596`). `_without_paraphrase` then cuts every sentence tagged with that id. | `STORY_PLACE_LINE`: "Never tell the story yourself, before or after the marker" (`story_placement.py:91-95`, sent only via `turn_prep.py`) | **Proven:** admission instructed the behaviour that was cut. Whether the directive prevents it is unverified. On the live path it still fired once in desert's turns. |
| typed quotation / tagged quote record when **no quote was offered** (4) | The shape's no-quote clause starts "When the directive says no quote is offered ...", so it never applies without a directive | `NO_QUOTE_LINE` | **Proven** that the rule was missing; the effect is unverified |
| lead-in does not name its speaker (81) | **Present.** `citation_contract` requires a lead-in "that names the quote's speaker ... never follows 'he' or 'she' or an unnamed teacher, and never stands alone after an earlier sentence". The evidence block shows the speaker on every quote line ("quote from Augustine, our bishop at Hippo"): the name the check accepts was inside the shown label for 799 of 799 offers. | "by the name listed with it, exactly as listed", the per-quote "its sentence naming X", and "do not say first, in other words, what it is about to say" | **Unverified.** FLOW_MAP's statement that admission "was not given the exact name" is **not correct**: the name was in the block. The directive's added rule against paraphrasing first matches the 34 no-attribution cuts, but compliance is unmeasured. |
| typed quotation (38 with a quote offered), words attributed (24), words after an attribution (22), quote words (20), tagged quote record (32), placed mismatch (23), second quote (22) | **Present** in `citation_contract`: "We put no words of our own in quotation marks ... no words after a name and 'said', 'wrote' ... or a colon", "at most one quote goes into any one answer" | The same rules, restated per turn | **Unverified** |

**Live-path rows from the same run, for comparison only.** These are `fleet-graded-run-1/replay/*.json`: 66 multi-turn live turns, 65 of them `voice_with_directive`. Tabulated in `live_path_removals.json`.

| Measure | Live path (directive) | Admission (no directive) |
|---|---|---|
| Total cuts | 50 in 65 turns (0.77 per turn) | 297 in 308 answers (0.96 per answer) |
| "does not name its speaker" | 3 in 65 turns | 81 in 308 answers |

The questions, the turn depth and the evidence all differ between the two sets, so this is **not** a controlled comparison.

### Q3. Did any cut remove a sentence that was true and well grounded?

**Yes.** The measures below are code checks on the replay data, and I checked a sample by hand against the records.

- **30 cut sentences appear word for word (normalised) in a record that the sentence itself cites.** Examples:
  - lpc f4-p: "He named that condition in one sentence: "Thou hast formed us for Thyself ..."". This sentence is in `lpc.witness.restless-heart-and-the-unrepentant-enemy` word for word, and was cut as "quotation typed by the voice".
  - lpc f2-i: "A bishop's own letter can be corrected, and a council can be corrected by a later, greater council, but Scripture cannot be corrected that way at all." This is in `lpc.witness.scripture-above-councils`, and was cut as "words after an attribution".
  - gallic c-t: "Grace always co-operates with our will, and assists, protects, and defends it."

  This is the case where a witness record's own text quotes its source. The net treats the voice repeating the record as an unplaced quotation (FLOW_MAP row 9). It is a record/engine interaction.
- **44 cut sentences contain a quoted span of 3 or more words that is word for word in the records**: 31 typed quotations and 13 placed-quote mismatches. Examples: pahc c-i, "Ignatius wrote of 'Jesus Christ our God' ...", which `pahc.witness.jesus-as-god` states; witt, "I did nothing; the Word did it all", 3 times. These are true attributed words, cut by policy because only code may set a quote.
- **Desert story retellings:** 27 of 28 pass the net's own claim test against the story record they cite, and 22 are at least 80% grounded. One example is "The tradition tells that Pachomius, sent by an angel with a brass tablet ...", which matches `desert.story.pachomius-founding`.
- **81 + 23 + 22 cuts lost a quote record**, which is a record's verbatim rendering that code would have set in place. The quote itself was true by construction. What failed was the lead-in.

**Caveat on the grounding measure.** Overall, 99 of the 297 cut sentences are either at least 80% grounded in their own tags, verbatim in a cited record, or carry a verbatim record quotation. But word overlap is not truth. One "verbatim" hit (desert c-p, "Anything further would invent an interiority the source does not give.") is a build note spoken aloud, not a fact.

## 6. Harness or engine?

- **Every cut is the engine's.** `apply_net` reproduces all 308 shipped texts from the drafts, and the harness adds no cutting of its own.
- **The damage mechanism is the engine's.** The engine cuts whole sentences and makes no repair for dependent sentences. The same draft would be cut the same way on the live path.
- **The harness affects how often cuts are triggered.** It sends no directive, which is proven to contradict the story rule (28 cuts) and to drop the no-quote rule (4 cuts). For the other 265 cuts, its effect is plausible but unmeasured. It also runs no `settle_reply`, although no answer was emptied in this run, so that made no difference here.
- **No horizon cut happened.** The "post-window" cuts FLOW_MAP lists did not occur in this run.

## 7. What I could not do

- **cappadocian:** no `raw_text` was saved anywhere, so it could not be replayed.
- **The run commits:** I could not rebuild the run's exact packages or check out the 11 run commits. The checkout is one shallow commit and `packages/` is absent. The content hash differs, but the exact text match makes this immaterial for `apply_net`. Fetching the history from GitHub would have meant writing to the checkout's `.git` or making a new clone, so I did not do it.
- **The live directive's effect** on the draft, and the live evidence differences (reader asks and kind), both need model calls. They were not run.
- **The orphan and grounding measures are heuristics.** The orphan precision of about 60% comes from a sample of 30. Recall was not measured. Truth was judged by hand on samples only, not on all 297.

## Files (all in `replay/`)

- `REPLAY_REPORT.md`: this report.
- `removals.jsonl`: one line per cut sentence (297). Fields:
  - `world`, `probe`, `cell`, `reason`, `removed_sentence`, `draft`, `marker`;
  - `next_shipped`, `prev_shipped`, `next_in_new_paragraph`, `orphan_heuristic`, `next_starts_referring`, `cut_run_reasons`;
  - `claim_test`, `ratio_vs_own_tags`, `verbatim_in_own_tagged_record`, `quoted_spans_verbatim_in_records`, `quote_offers`.
- `replay_results.jsonl`: per probe, the raw draft, the shipped text, the replay text, whether they match, the offered ids, the rendered evidence block, the placed quotes, the cut sentences, and the per-sentence verdicts.
- `stats.json`, `speaker_unnamed_breakdown.json`, `live_path_removals.json`, `package_hashes.json`: the tables above.
- Scripts: `build_packages.py`, `nocall_stubs.py`, `replay.py`, `analyze.py`, `classify_speaker.py`, `live_compare.py`, `shapecheck.py`.
- `repo/` (code copy) and `packages/` (rebuilt compiled files).
