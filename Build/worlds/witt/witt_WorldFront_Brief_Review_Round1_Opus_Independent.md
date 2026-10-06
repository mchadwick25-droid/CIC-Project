Simulated review — informational only, not an Article 31 substitute.

# Independent Review — Round 1 (Opus, full review)
## Target documents: `witt.front.lutheran-wittenberg-and-its-congregations` and `witt.facilitator_brief.lutheran-wittenberg-and-its-congregations`

- **Reviewer model:** claude-opus-5-5
- **Drafter model:** withheld until the mapping is revealed
- **Reviewer agent:** independent-review subagent, fresh context. It did not draft, revise, or previously review either record.
- **Drafter agent:** withheld until the mapping is revealed
- **Round:** 1
- **Truncation check, method 1:** structural parse. Both files parse as YAML front matter and close on a `---` line. The front carries `skim`, `orientation` (12 story units, 3 documented stories, 4 voices, floor note, 2 legacy units, relations, sourcing, 3 read-first) and `narrative` (who_speaks, quiet, 3 questions, 3 pull quotes, 5 glossary terms). The brief carries all eight body fields: 5 strengths, 7 limitations, 4 participant-fit units, pairing, 6 cautions, living-tradition handling, redirect notes. Every unit ends on a complete sentence.
- **Truncation check, method 2:** byte and hash count. Front: 357 lines, 20,614 bytes, `git hash-object` d8be499a. Brief: 244 lines, 15,438 bytes, `git hash-object` 41369d5d. Both are untracked at HEAD `ad07218b9`. The last 60 bytes of each end in `]\n---\n`.
- **Date:** 2026-10-02
- **Truth source:** every record under `records/witt/`, plus `records/worlds/witt.yaml`. Constraints: `Build/worlds/witt/Open_Gaps_Tracking.md` OG-36, OG-37, OG-49, OG-51.

**What this review is.** A full first-round review of two new, uncommitted records. Every factual sentence was traced to the records named in its own unit's `grounded_in`, and those records were opened and read. Nothing was taken on the strength of an id. The three pull quotes were re-verified verbatim against the vendored texts. The gates were run locally. No model was called and nothing was spent.

**Verdict: SUBSTANTIAL.** There are five blocking findings, F1 to F5. All five have exact, narrow fixes. None needs new research. The drafting is otherwise strong. Readability passes everywhere, the 1525/1543 discipline holds, no quote is mis-voiced, and the world's own imagery survives.

---

## Section 1 — What was checked

- **Grounding.** All 61 ids cited in the two records resolve. Each unit's sentences were checked against the cited records' own text and `formation_confidence`, not against their titles.
- **Quotes.** `witt.quote.second-article-of-the-creed`, `witt.quote.congregation-of-saints` and `witt.quote.the-poor-man-who-comes-to-you` were checked. Each record's `text` was found verbatim, whitespace-normalised, in `cic/texts/luther_small-catechism_smith1994.txt` (from line 186), `cic/texts/melanchthon_augsburg-confession_anon-pg275.txt` (from line 275) and `cic/texts/luther_large-catechism_bente-dau1921.txt` (from line 1946). Neither record contains a double-quoted span. The single-quoted spans ('Here I stand', 'sin boldly', 'Catholic', 'must', 'free', 'for you', 'we') are mentions, not voicings. None matches 8 or more characters of any quote record's `text`. The floor note follows the quote's `modern_rendering` ("born of the Father before time began").
- **Ballad check for F3.** `cic/texts/luther_hymns_bacon-allen.txt` lines 1789–1803 were read directly.
- **Gates, all local, no model calls:**
  - `engine.m1.gates.run_all` on witt: 0 findings on either target in any gate. Readability total is 194, which equals the pinned waiver.
  - `python -m engine.m10.cli records witt`: PASS.
  - `python -m engine.m10.cli regate witt`: PASS (it picks up untracked files via `ls-files --others`).
  - `python -m engine.m10.cli citations <both files>`: PASS.
  - `python -m engine.m9.cli check`: clean, exit 0.
  - `python -m engine.m1.cross_world`: 0 new defects.
  - `tools/check_live_commentary.py --surface records`: no hit on either file.
  - `pytest engine/m1/tests/test_cross_world.py`: **fails** (see F5).
- **Readability, own run** (`engine.m1.gates.grade_text` on every prose field of 12+ words). Every participant-facing field clears FK ≤ 10 and FRE ≥ 60. Front story units score FK 3.9–7.2. Brief fields score FK 5.1–9.9. The only sub-60 FRE is the front's `confidence.divergence_note` (57.9), which is not a gated public field.
- **OG constraints.** No `experience_today` field. No census field invented; `census_id` matches the registry and the rzg precedent. No revision-history or process language. The name "Nikolaus" appears in neither record. The 1525 and 1543 texts are disclosed as existing only, never quoted, never argued. The Marburg experience is stated as thin. The OG-51 tension is handled in F1.

---

## Section 2 — Blocking findings

### F1. The brief settles the held "church today" tension (OG-51 item 4)

- **Where:** brief, `living_tradition_handling`.
- **Text:** "The record also cannot say whether a participant could find a church of this tradition to visit today. The voice says so plainly, and a facilitator should hold that question and not answer it from this record." It also cites `witt.dw.one-holy-church-forever` in `grounded_in`.
- **Why it fails:** OG-51 item 4 records two live answers. The Living Traditions section says a confessional family "still teaches a catechism like our own … today". `witt.dw.one-holy-church-forever` says "A church today you could visit that's ours -- we cannot answer that". OG-54, OG-55 and the OG-53 status line all hold this as an open project-lead decision. This unit picks the second answer, states it as the voice's settled behaviour ("The voice says so plainly"), and tells the facilitator to act on it. That is the settlement the constraint forbids. It also sits two sentences after "still teaching … under many names", so the unit carries the tension inside itself. The front's `legacy` units do not do this. They restate the approved Version A text and make no visiting claim. They are fine.
- **Fix:** delete both sentences. Remove `witt.dw.one-holy-church-forever` from that unit's `grounded_in`. Add nothing in their place. The question stays with the project lead's held decision.

### F2. Library limits are stated as facts about history ("survives", "has not come down to us")

- **Where, with text:**
  - Front `skim.tile`: "no woman's own text survives".
  - Front `orientation.story[11]`: "No woman's own text survives." and "No outsider's account of this world survives either."
  - Front `sourcing`: "No woman's own text survives." and "The felt experience of the 1529 break at Marburg has not come down to us."
  - Front `voices[2].hedge`: "Nothing else of her words, her days, or her convictions survives."
  - Brief `formation_limitations[1]`: "No woman's own text survives."
  - Brief `formation_limitations[6]`: "No building, object, wedding, order of service, or pastor's own voice survives."
- **Why it fails:** each of these is scoped in its source record. The registry's thinness statement says "no text a woman wrote survives **here**". `witt.limit.no-outsider-witness` says "No outsider's own independent account survives **in our own library**". `witt.story.household-and-kate-on-prayer` says "This library holds no other recorded words from Katharina von Bora". `witt.story.first-german-mass-sung` says "no vendored order of service". `witt.dw.the-household-we-can-describe` says "No source **in our own library** describes a building".

  Both records are `register: etic`. Without the scope, each sentence becomes a historical claim the world cannot support, and several are false outside this library. Women's own texts from this movement and decade are generally held to survive, for example Argula von Grumbach's 1523 letters and Elisabeth Cruciger's 1524 hymn. Letters by Katharina von Bora are generally held to survive. Luther's German Mass order of 1526 survives. The Confutation and Catholic polemics survive. Luther's letters from Marburg survive. These are reviewer's general knowledge, not record claims, and none of it belongs in the records. The point is only that the unscoped sentence is not derivable from the world, and stating it is the overreach CLAUDE.md treats as fabrication-adjacent.

  The emic "No woman among us left her own word" (core, voice_craft) is the world speaking of itself. That is a different case and is not touched here.
- **Fix:** scope every instance to this record or library. Use "survives in this library" or "this record holds no …". For example:
  - "No woman's own text survives in this library."
  - "No outsider's own account of this world is held here either."
  - "This record holds nothing else of her words, her days, or her convictions."
  - "This library holds no building, object, wedding, order of service, or pastor's own voice."
  - "…has not come down to this record."

### F3. The Brussels martyrs: an unscoped "only case", and a misreading of the ballad

- **Where, with text:**
  - Front `orientation.story[7]`: "It is also the only case where the movement's teaching cost lives."
  - Front `orientation.story[7]`: "The ballad says their refusal made them priests without any ordination."
  - Brief `cautions[3]`: "They are the only case where this teaching cost lives, so the voice should not speak of a martyr tradition."
- **Why it fails, part (a):** the records scope this claim every time. `witt.story.brussels-martyrs` says "the only story **in this whole inventory**". `witt.figure.brussels-martyrs-john-and-henry` says "the only two people **in this whole library's record** whom the movement's own teaching is **shown** to have cost their lives". `witt.dw.true-priests-of-gods-own-making` says "the only case **in our own record**". As written, both units state a historical fact that is not in the records and is false: others were executed for evangelical teaching in this window.
- **Why it fails, part (b):** the ballad, at `luther_hymns_bacon-allen.txt` lines 1789–1803, says they were stripped of their "monkish garb … And gown of ordination" and then became "True priests of God's own making, … Christ's holy orders taking". "Without any ordination" reads as if they had none, and it drops the ballad's own image of Christ's orders. Neither cited record (`witt.story.brussels-martyrs`, `witt.figure.brussels-martyrs-john-and-henry`) says "without any ordination".
- **Fix:**
  - Front: "It is also the only case in this record where the movement's teaching cost lives."
  - Front: "The ballad says that, stripped of their habits and their ordination, they became true priests of God's own making."
  - Brief: "They are the only case in this record where this teaching cost lives, so the voice should not speak of a martyr tradition."

### F4. Claims whose cited `grounded_in` does not support them

Both envelopes state that "the confidence of any single claim lives in the records named in that unit's own grounded_in". That makes the citation load-bearing. In each case below, the claim is true elsewhere in the world, but a reader following the cited ids cannot find it.

| Unit | Sentence | Cited records say | Add |
|---|---|---|---|
| Front `story[5]` | "Absolution is given as though from God himself." | Not in the three cited gravities. | `witt.term.confession-and-absolution` |
| Front `story[5]` | "…in and under the bread and wine. This world refuses to explain how." | Not in the cited gravities. | `witt.gravity.bodily-presence`, `witt.term.transubstantiation` |
| Front `story[7]` | the ballad's priesthood line (see F3) | Not in the cited records. | `witt.dw.true-priests-of-gods-own-making` |
| Brief `formation_strengths[2]` | "a father is a priest in his own house" | Not in the cited records. | `witt.term.we-are-all-priests` |
| Brief `participant_type_fit[1]` | "Good works are the ordinary things done in faith, not only prayer, fasting, and alms." | Not in the cited records. | `witt.term.good-works` |
| Brief `participant_type_fit[3]` | "where the question is about guilt, assurance…" | No assurance record cited. | `witt.term.assurance` |

**Fix:** add the ids shown. No text change is needed.

### F5. Two `ACCEPTED_OPEN` waivers go stale when these records land, and CI fails

- **Where:** `engine/m1/cross_world.py`, `ACCEPTED_OPEN` keys `required-record-type/witt/world_front` and `required-record-type/witt/facilitator_brief` (lines ~84–93). OG-37 is the owning entry.
- **Evidence:** `pytest engine/m1/tests/test_cross_world.py::test_every_accepted_open_entry_still_describes_a_real_finding` fails with "ACCEPTED_OPEN names findings that no longer fire - delete them: ['required-record-type/witt/facilitator_brief', 'required-record-type/witt/world_front']".
- **Why it fails:** CLAUDE.md says "a stale waiver for something already fixed also fails — remove it." These records cannot land without the waivers going.
- **Fix:** in the same change, delete both keys and the part of the comment block that describes them. Keep `required-site-json/witt`, which still fires because no site JSON is compiled. Then append a new OG entry recording that OG-37's two record-type waivers are closed. OG entries are append-only, so OG-37 itself is not edited. This is a "CI/infra mechanical fix", which the defaults table says to just do.

---

## Section 3 — Non-blocking notes (not findings)

- **Luther hedge overstates.** Front `voices[0].hedge` says "Most stories of Luther here reach us through students' notes". Of the eight Luther stories, four rest on Table Talk (Cajetan, Worms, Kate, prayer for rain). The other four are his own texts (the Albrecht letter, the sermons, the Magnificat, the ballad). Suggest "Many stories…".
- **Cajetan.** Front `story[2]` says "Cardinal Cajetan wanted one word from him: Revoco". The record has the Italian go-between saying it would take one word. Suggest "He was urged to say one word: Revoco, I recant."
- **Walter.** Front `story[6]` says "set the Epistle and Gospel to German tones". The tones were the church's Eighth and Sixth. The German was the text. The `voices[3]` wording ("chose how to sing the Epistle and Gospel in German") is right. Use it in both places.
- **Deconstructing participant unit (brief `participant_type_fit[3]`).** It is thin but honest, and it does not overreach on safety. One inconsistency: "It does not say whether its teaching quieted every conscience" implies it quieted some. `formation_strengths[0]` correctly says the record "does not show that the teaching quieted any particular person". Suggest "any". `witt.dw.cold-and-careless-among-us` speaks directly to "the people who taught you the faith turned out to be hypocrites". The unit could name that question, since it is this world's best-fitting answer for this participant. This is a "could be stronger" point and not a defect.
- **Role label in a world record.** The brief's `world_identity` and `cautions[0]` say "a sexton and schoolmaster". `witt.voice.craft` says the persona's role label "never appear[s] in world records". The brief is excluded from the compiled package (`_PACKAGE_EXCLUDED_RECORD_TYPES`), so it cannot cause the voice-prompt collision that rule guards against. The rzg brief also avoids the label. Suggest "a lay voice of the parish churches" for consistency.
- **Readability floor and sentence length.** Front story units average 8.7–12.6 words a sentence. Most score FK 3.9–6, below the report-only grade-8 floor and the 12–20-word guide. A few runs read clipped ("That letter opened a movement. It set Scripture against…"). This is reported, not failed, under the NorthStar decision. Joining one or two pairs per unit would lift it without loss.
- **Imagery survives.** The catechism said at rising, at table and at night; the father's weekly question; food withheld; German hymns inside a kept Mass; "what does this mean?"; the household as school — all are present, concrete and faithful. No AI cadence or filler was found. The hedges are the world's own facts, not disclaimers.
- **Imperatives in participant-facing hedges.** Front `voices[1].hedge` says "Tell the story as…" and `voices[2].hedge` says "Do not build more on it…". These read as facilitator instructions. rzg uses "should not be read…", which is a softer form of the same thing. This is wording, not substance.

---

## Section 4 — Cosmetic and propagation fixes applied directly

None. This review is read-only on the records by instruction. Every fix above is left to the revision.

---

## Section 5 — Verdict and disposition

**SUBSTANTIAL**, on five blocking findings:
- **F1:** OG-51 settled in the brief.
- **F2:** library limits stated as history.
- **F3:** the unscoped Brussels "only case" and the ordination misreading.
- **F4:** six grounding gaps.
- **F5:** two stale waivers that fail CI.

All five are narrow and exact. One revision round should clear them, followed by a targeted recheck of only the changed units. This is round 1 of the three-round cap.

**What passed.** The 1525/1543 discipline holds (existence only, never quoted, never argued, and the later-effect contest is left open). No woman's text is invented. Marburg is marked thin. The household program is always "as taught, never as done". The door and "Here I stand" are both carried with their contests. Johann Walter's and the window anecdote's transmission is honest. No personal detail is invented for any of the four voices. The OG-51 tension is not smuggled in through `legacy` or `relations_summary`. All gates pass except the F5 test.

**Disagreement with predecessors.** One small point. The constraint as briefed to this reviewer reads "no woman's text survives". The registry's own wording is "survives here". F2 restores that scope. It does not loosen the constraint.
