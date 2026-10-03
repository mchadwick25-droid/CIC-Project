Simulated review — informational only, not an Article 31 substitute.

# Independent Review — Round 2 (Opus, targeted recheck)
## Target documents: `witt.front.lutheran-wittenberg-and-its-congregations` and `witt.facilitator_brief.lutheran-wittenberg-and-its-congregations`

- **Reviewer model:** claude-opus-5-5
- **Drafter model:** withheld until the mapping is revealed
- **Reviewer agent:** independent-review subagent, fresh context. It did not draft or revise either record, and it did not write the round-1 review.
- **Drafter agent:** withheld until the mapping is revealed
- **Round:** 2 of the 3-round cap (targeted recheck, lower effort)
- **Revision under review:** commit `1441f0dfe` against the first draft `ad07218b9`. PyYAML re-dumped both files, so the line diff is large. The text of each unit was compared directly by parsing both versions and diffing field by field.
- **Truncation check, method 1:** structural parse. Both files parse as YAML front matter and close on a `---` line. The front carries `id` through `narrative` (12 story units, 3 documented stories, 4 voices, floor note, 2 legacy units, relations, sourcing, 3 read-first, who_speaks, quiet, 3 questions, 3 pull quotes, 5 glossary terms). The brief carries `world_identity` through `redirect_notes`, all eight body fields. Every unit ends on a complete sentence.
- **Truncation check, method 2:** byte and hash count at HEAD `1441f0dfe`. Front: 326 lines, 20,835 bytes, `git hash-object` 576b3482. Brief: 237 lines, 15,389 bytes, `git hash-object` 35fa40b6. The last bytes of each end in `]\n---\n`.
- **Date:** 2026-10-02
- **Truth source:** every record under `records/witt/`, plus `records/worlds/witt.yaml`. Constraints: `Build/worlds/witt/Open_Gaps_Tracking.md` OG-37, OG-51 item 4, OG-54, OG-55, OG-57. Prior review: `Build/worlds/witt/witt_WorldFront_Brief_Review_Round1_Opus_Independent.md`.

**What this review is.** A targeted recheck of the revision only. It checks that F1 to F5 are actually resolved, that every changed sentence is still supported by the records its unit cites, and that the Register Bar and CLAUDE.md craft rules hold across both records in full. Every newly cited record was opened and read. The ballad was read directly in the vendored text. The gates were re-run locally. No model was called and nothing was spent.

**Verdict: SUBSTANTIAL, narrowly.** There is one blocking finding, R2-1. It is a rhythm regression the revision introduced into one front story unit, and it has an exact one-unit fix. F1 to F5 are all resolved. Every changed sentence is supported. Every gate passes.

---

## Section 1 — What was checked

- **F1 (OG-51 item 4).** The two brief sentences on visiting a church today are gone. `witt.dw.one-holy-church-forever` is gone from `living_tradition_handling.grounded_in`. Two units still cite that record:
  - Brief `participant_type_fit[0]` uses it only for the world's own sense of "catholic" ("This world applies the word catholic to the whole community of the faithful, and the voice uses it in that sense"). Nothing about a present-day church.
  - Front `orientation.story[9]` uses it only for the Marburg break and its thinness. Nothing about a present-day church.

  The front `legacy[0]` and the brief `living_tradition_handling` restate the approved Version A text ("still teaches a catechism like this world's own … under many names"). Both drop the core's "in many lands today". Neither says or implies that a participant could find or visit such a church, and both state that the record makes no claim about what any community teaches or practices now. The tension is neither settled nor hinted. **Resolved.**
- **F2 (library limits as history).** Every instance named in round 1 is now scoped: "No woman's own text survives in this library" (front story[11], sourcing; brief limitations[1]); "this library holds no woman's own text" (tile); "No outsider's own account of this world is held here either"; "This record holds nothing else of her words…"; "This library holds no building, object, wedding, order of service, or pastor's own voice"; "has not come down to this record" (story[9], sourcing); brief limitations[4] "No outsider's own account survives in this library". A full search of both records for "surviv", "come down" and similar forms found no unscoped instance. One leftover borderline sentence is in Section 3. **Resolved.**
- **F3 (Brussels).** Front story[7] and brief cautions[3] now both say "the only case in this record". That matches `witt.story.brussels-martyrs` ("in this whole inventory"), `witt.figure.brussels-martyrs-john-and-henry` ("in this whole library's record") and `witt.dw.true-priests-of-gods-own-making` ("the only case in our own record"). The ballad line now reads "The ballad says that, stripped of their habits and their ordination, they became true priests of God's own making." Against `cic/texts/luther_hymns_bacon-allen.txt` lines 1789–1803: stanza 5, "Their monkish garb from them they take, / And gown of ordination"; stanza 6, "Thus by the power of grace they were / True priests of God's own making, … Christ's holy orders taking". The paraphrase is faithful. "Stripped of … their ordination" condenses "gown of ordination", and "became" carries the ballad's "Thus … they were". It no longer says they had no ordination. **Resolved.**
- **F4 (grounding).** Each added id was opened:
  - `witt.term.confession-and-absolution` ("hearing forgiveness as though from God himself") supports story[5]'s absolution sentence.
  - `witt.gravity.bodily-presence` ("in and under", "truly present") and `witt.term.transubstantiation` ("We refuse to explain how Christ is present in the bread") support story[5]'s presence sentence.
  - `witt.dw.true-priests-of-gods-own-making` supports story[7]'s ballad line and its "only case in our own record" scope.
  - `witt.term.we-are-all-priests` ("A father is a priest in his own home. Still, no one may preach in public without being properly called") supports brief strengths[2].
  - `witt.term.good-works` ("not just prayer, fasting, and giving alms … ordinary things done in faith") supports brief fit[1].
  - `witt.term.assurance` supports brief fit[3]'s "assurance", and also strengths[0], where it was added as well.

  **Resolved.**
- **F5 (waivers).** `engine/m1/cross_world.py` drops `required-record-type/witt/world_front` and `required-record-type/witt/facilitator_brief` and keeps `required-site-json/witt`, with a comment and reason rewritten to match. OG-57 is appended to `Open_Gaps_Tracking.md` and OG-37 is untouched (the diff is additions only). `pytest engine/m1/tests/test_cross_world.py`: **20 passed**. `python -m engine.m1.cross_world`: 0 new defects, 8 accepted-open. **Resolved.**
- **Changed sentences, (b).** All changed units were traced. The rewrites beyond F1–F5 are craft rewrites. They remove "not X, but Y" shapes, embedded single-quoted spans and imperative hedges, and they join or split sentences. No new name, date, number or personal detail was found. Specific checks:
  - story[3]'s "a faith without love was not faith at all" matches `witt.story.return-and-the-eight-sermons` word for word in substance.
  - story[2]'s "he was urged to say one word: Revoco" matches `witt.story.augsburg-before-cajetan`, where the Italian go-between urges it.
  - story[2]'s Worms sentence ("absent from his own account as this record holds it, and scholars dispute its authenticity") matches `witt.story.worms-1521`.
  - story[8]'s "takes the form of a loyal address" matches `witt.story.diet-of-augsburg-1530`.
  - story[5]'s "the promise is spoken to each person who receives" paraphrases the "for you" of `witt.gravity.promise-and-sign`.
  - Brief cautions[4]'s "its confidence is Widely Accepted" matches `witt.source.luther-von-den-juden-und-ihren-l` (`formation_confidence: Widely Accepted`).
  - The 1525/1543 disclosure holds in both records: existence only, neither text held, no argument laid out, and the later-effect contest left open. The "no woman's text in this library" scope holds everywhere.
- **Gates, all local, no model calls:**
  - `python -m engine.m10.cli records witt`: PASS (`required-site-json/witt` noted as waived).
  - `python -m engine.m10.cli regate witt`: PASS. No note or finding names either target.
  - `engine.m1.gates.run_all` on witt: 0 findings on either target in any gate. The readability total is 194, which equals the pinned waiver.
  - `python -m engine.m10.cli citations <both files>`: PASS.
  - `tools/check_live_commentary.py --surface records`: no hit on either file.
- **Readability, own run** (`engine.m10.regate.public_fields` + `engine.m1.gates.grade_text`, all 59 public fields). Every field clears FK ≤ 10 and FRE ≥ 60. Front FK runs 4.6–8.2. Brief FK runs 5.3–9.0. The lowest FRE is 60.2 (brief limitations[0]). The longest sentence in either record is 25 words (brief world_identity, brief limitations[0], front story[2], story[5], story[9]). None exceeds 25.
- **Craft scan, (c).** Every sentence in both records containing a negation or contrast word was listed and read. No "not X, but Y" or "It is not X" construction survives. There is no double-quoted span and no single-quoted source span in either record. "Revoco, I recant" is a single-word mention, and "what does this mean?" is the name of a term (`witt.term.what-does-this-mean`). No AI tell, hedging filler or assistant cadence was found. The survivors are R2-1 below and the notes in Section 3.

---

## Section 2 — Blocking findings

### R2-1. Front `orientation.story[1]` was cut into a clipped run the first draft did not have

- **Where:** front, `orientation.story[1]` (the 1517 letter).
- **Text:** "He asked the archbishop to withdraw the preachers' instructions. He enclosed ninety-five statements. They were for debate. The letter asks for correction. The scene of a hammer and a church door comes from a much later editor. Scholars dispute it. The letter does not mention it."
- **Why it fails:** the revision split "He enclosed ninety-five statements for debate" into two four-word sentences. It also split "Scholars dispute it, and the letter never mentions it" into two. The unit now averages 7.7 words a sentence, and 8 of its 11 sentences run under 10 words. That is below every other story unit (round 1's range was 8.7–12.6) and far below CLAUDE.md's 12–20-word practical shape. "They were for debate." and "Scholars dispute it." have no content that needs a sentence of its own. The result is the staccato, primer-like rhythm the Register Bar rules out. It is also the opening historical unit a participant reads. Round 1 noted clipped runs as non-blocking, but this one is a regression the revision itself created, and the fix is narrow.
- **Fix:** replace the last six sentences of the unit, from "He enclosed" to the end, with these. They add no new claim and rest on the same records:
  "He sent ninety-five statements with it, to be debated. The letter asks for correction. It says nothing of a hammer or a church door. That scene comes from a much later editor, and scholars dispute it."
  Keep `grounded_in` as it is. The whole unit with this replacement was graded with `engine.m1.gates.grade_text`: FK 7.1, FRE 60.5, which passes. FRE has little margin because the unit's first sentences carry long words. Two tighter joins were tried, "He enclosed ninety-five statements for debate" plus one joined sentence, and both fell to FRE 56–59. So the reviser should re-grade any other wording before committing it.

---

## Section 3 — Non-blocking notes (not findings)

- **One borderline unscoped limit (F2 family).** Front `sourcing` says "No object or outside witness confirms this world's account of itself." The paragraph is framed as the record's own holdings, so it reads as a statement about this library, and round 1 passed the unit. For consistency with the F2 fixes, "No object or outside witness in this library confirms…" would close it fully.
- **Ballad phrase in host prose.** Story[7]'s "true priests of God's own making" is the ballad's own wording, carried without quotation marks. It is five words, below the 8-word embedded-quotation threshold. It is also the world's own established phrase, used as the `witt.dw.true-priests-of-gods-own-making` record name and in `witt.term.we-are-all-priests`. Round 1 prescribed this wording. It is not a Decision 8B defect as the rule is enforced. A future quote record for stanza 6 would give it a verified home.
- **Echo closers.** Brief `participant_type_fit[3]` ends "…and its sharp lines on judgment stay sharp." Brief `cautions[1]` has "A rule should stay a rule, and it should never become a report of success or failure." Both lean on a repeated-word turn that reads slightly crafted. The first draft's plain "it does not soften its sharp lines on judgment" was better on the first. These are facilitator-only fields and mild.
- **Add-on tail.** Brief `cautions[4]`: "The scholarly contest over its later effect stays open here. A facilitator should leave it open." The second sentence repeats the first. It could be dropped or merged ("…stays open here, and a facilitator should leave it open").
- **Clipped rhythm elsewhere, reported only.** Front `story[10]` averages 9.8 words a sentence and `voices[1].text` averages 10.0. Brief `cautions[2]` and `formation_limitations[4]` average 10.5. These read plainly rather than primer-like, and they were not made worse by the revision. They are reported, not failed, under the NorthStar decision.
- **Grammar nit.** Brief `living_tradition_handling`: "The tradition went on for centuries that this record does not tell." This would read better as "The tradition went on for centuries, in ways this record does not tell," which matches front `legacy[1]`.
- **Round-1 non-blocking notes.** The revision took up the Luther hedge ("Many stories…"), Cajetan, Walter, "any conscience", the role label ("a lay voice of the parish churches") and the imperative hedges. All are now consistent with their records.

---

## Section 4 — Cosmetic and propagation fixes applied directly

None. This review is read-only on the records by instruction.

---

## Section 5 — Verdict and disposition

**SUBSTANTIAL, narrowly**, on one blocking finding:
- **R2-1:** the revision cut front `story[1]` into a primer-like run. The fix is one exact replacement of its closing sentences, already graded at FK 7.1 and FRE 60.5.

F1 to F5 are all resolved, and none is merely reworded. The OG-51 "church today" tension is neither settled nor hinted in either record. Every library limit is scoped. The Brussels scope and the ballad line are faithful to the records and to the vendored ballad. Every added `grounded_in` id supports its unit. The stale waivers are gone, and the waiver test passes.

This is round 2 of the three-round cap. The R2-1 fix is a single-unit edit. A round-3 targeted recheck should check only that unit, its readability, and that nothing else changed. If round 3 does not clear, the cap rule applies and the document escalates to the project lead.

**Disagreement with predecessors.** None on substance. Round 1 judged clipped story runs non-blocking. This review keeps that judgment for the units the revision did not worsen, and it blocks only the one unit the revision made clipped.
