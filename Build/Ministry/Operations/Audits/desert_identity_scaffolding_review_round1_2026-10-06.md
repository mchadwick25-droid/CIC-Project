# desert — identity-and-scaffolding record pass, adversarial review round 1 (2026-10-06)

Branch `records/identity-scaffolding-desert` (commits 37795947, 893ea78a), diff `origin/main...HEAD`. Reviewer: Opus 5.5. No model spend; no records edited.

**Verdict: REVISE.**

**Oblique disagreement: yes** (partial; for the project lead, not decided here). I agree that `desert.dw.jesus` is oblique by its sources and that its new opener keeps that shape honestly. I do not agree with OG-21's "found oblique throughout, none of it partial", and its stated reason is factually wrong (finding 1). The world's sources also say directly who the Son is. Vita SS69 (`desert.quote.antony-nicene-formula`) gives "the Eternal Word and Wisdom of the Essence of the Father", and `desert.demo.center-jesus-as-god` and `desert.dw.god` already answer from it. Further direct statements are at SS74-75 and SS81, which is inside the `dw.jesus` locus. The world's own demonstration opens "*Mostly*, he was one command". The direct passages are all Athanasius's report, rated Contested as Antony's own words, and found in only a few episodes. So the world is oblique in its dominant shape and partly direct. Two witnesses were left unreordered on the strength of "oblique throughout": `desert.dw.god` (who-question; who arrives in sentence 3) and `desert.dw.the-heart-and-the-spirit` (who-question about the Spirit, drawn from the Macarian homilies, which speak of the Spirit directly). Whether the oblique shape covers them is the project lead's call.

## Key question: the `desert.dw.jesus` opener

- **Shape.** "One command reordered our lives, heard as though it were spoken straight to you: sell what you have, give it to the poor, and follow me." This keeps the source shape. Vita SS2 (line 31244, `cic/texts/npnf204_athanasius-select-works-letters.xml`) narrates the whole life as an answer to Matthew 19:21. The old enumerating frame "Three things. The first..." was scaffolding, and removing it changes no claim: the witness still goes on to the argued Christology and the Cross.
- **"The one who gave it is Christ, the Word of God."** This is sourced and not invented. In SS2 the command-giver is "the Lord", and the same passage says "followed the Saviour". SS74 (line 33023) gives "the Word of God was not changed". The old text already carried both "The Word of God ... took a human body" and "the deeds of Christ prove him to be God", so the identity Christ = the Word was implicit there. The new sentence makes it explicit and adds nothing the record's sources do not carry. The Contested bound survives in the next sentence, "We argued this when we were pressed to."
- Not substantial: "this" in "We argued this" now points to "Christ, the Word of God" and no longer to the incarnation argument. SS74-75 does argue that Christ is God, so the claim holds. Acceptable as is.

## Findings

**1. SUBSTANTIAL — OG-21 oblique reason is inaccurate.** `Build/worlds/desert/Open_Gaps_Tracking.md`, OG-21. The entry says: "A stated account of who Christ is appears only in the SS72-80 disputation" and "found oblique throughout, none of it partial." This is false. SS69 is a direct statement outside SS72-80, and it is carried in `desert.quote.antony-nicene-formula`, `desert.demo.center-jesus-as-god` and `desert.dw.god`. SS81 ("Christ alone the true and Eternal King") is in `dw.jesus`'s own locus. The world's demonstration says "Mostly". **Fix:** replace the reason with: "oblique by its sources, reason: the Life of Antony answers who Jesus was to this world through one command (Matthew 19:21, Vita SS2-3) and the life it ordered; direct statements of who he is exist (Vita SS69 against the Arians, the SS72-80 disputation, SS81), but all are Athanasius's report, Contested as Antony's own words (`desert.dw.jesus` tensions; `desert.quote.antony-nicene-formula` divergence note), and concentrated in a few episodes. Applied to `desert.dw.jesus`; whether it covers `desert.dw.god` and `desert.dw.the-heart-and-the-spirit` is with the project lead." Then delete "found oblique throughout, none of it partial".

**2. SUBSTANTIAL — claim changed, `desert.story.kellia-day` `absent_detail`.** The old text said "no specific attested passage *could be found* to source that detail" (a search result). The new text says "No specific attested passage *supports* a general note about spare or limited meals" (a flat claim that no such passage exists). That strengthens the claim, which is the same class as the quantifier change caught on don. It is also more exposed than the old wording: the vendored Palladius has specific spare-diet passages, for example Dorotheus's six ounces of bread (ch. II, line 203) and Moses's twelve ounces of dry bread (line 337). **Fix:** "No specific attested passage was found to support a general note about spare or limited meals, so none is given." In addition, log for the project lead, without fixing: the carried claim itself sits uneasily with those Palladius passages. They describe individuals, not a Kellia rule, but a Representative could voice the line as "the sources say nothing about spare meals." Also log, as out-of-scope build history in the same record's frontmatter: `narrative_tier_justification` ("a general diet clause from the prior build's own first draft was removed ... not reinstated here") and `divergence_note` ("per the prior build's cleared Story Repository Chunk Template's own rule").

**3. SUBSTANTIAL — OG-21 misstates the dangling-id state.** OG-21 says: "`desert.dw.judgment-and-resurrection` body no longer says the cell's other questions are carried by `desert.limit.f4-t-born-again-and-tithe` ... the frontmatter references to that id are untouched." There were no frontmatter references. On `origin/main` the id occurs in exactly one place, the removed body sentence (`git grep` over `records/`), and after this pass it occurs nowhere. **Fix:** say that the removed body sentence was the only occurrence, so the third dangling id of OG-19 item 10 no longer appears in any record. OG-19 is not edited (append-only); whoever next works on OG-19 confirms it.

**4. SUBSTANTIAL — OG-21's list of known-wrong claims carried is incomplete for the records this pass edited.** It names `moses-leaking-jug`, `arsenius-flee`, `writings` and `god`, none of which were edited. It omits these OG-19 items, which sit in records the pass did edit and which were carried unchanged:
- item 13: the `judgment-and-resurrection` body still says "the four cited passages", while its locus lists five;
- item 17: the `death-wish` text was reordered and keeps the framing that the inward combat came after persecution ended; `dw.jesus` carries the same framing ("when persecution ended ...");
- item 18: `antony-call` and `antony-tomb-combat` still narrate events before the window, unflagged;
- item 19: the `virgin-who-hid-athanasius` chronology is unchanged;
- item 5: the `pachomius-founding` body still gives "ch. XXXII, line 397", which is the chapter-heading line;
- item 9: the `never-settled` body (not edited, but in an edited file) still calls the Apophthegmata unvendored.

**Fix:** name each as carried unchanged, with its OG-19 item.

**5. SUBSTANTIAL — orphaned reference left in an in-scope witness: `desert.dw.the-heart-and-the-spirit` `text`.** The record opens: "There was another voice among us, and we will not flatten it into the first." In a standalone witness, "the first" has no antecedent. It assumes an earlier turn, which is the dialogue-scaffolding and orphan class, and this witness is in the pass's scope. That holds whatever the project lead rules on who-first. **Fix (no new content; the antecedent comes from the next sentence):** "There was another voice among us besides our most systematic teacher's, and we will not flatten it into his." If the project lead rules that this witness leads with who, the reorder moves the Macarian sentence ("the soul in communion with the Spirit of his light becomes all light ..."). That sentence is quoted source, so it must be re-verified verbatim against the vendored file.

**6. SUBSTANTIAL (live-surface rule) — body commentary kept in `desert.story.virgin-who-hid-athanasius`.** Ruling on the author's doubtful paragraph: **remove** the paragraph beginning "WHY THIS AND NOT A LONGER, BETTER-ATTESTED CHAPTER. ..." It is a curatorial rationale for a build choice (why this story was picked over Melania's chapter), plus an interpretive judgment ("a truer picture of this world's record of its women"). It is not a note on the source. CLAUDE.md treats such text in a live file as corruption, and a PR that edits the file removes it. Trim the closing paragraph to its pointer as well: "The chronology is broken, and the record says so in three places." Drop "because a story this world tells with a known error inside it, marked, is worth more than one it tells cleanly and cannot defend."

**7. Not substantial — `desert.story.pachomius-founding` body: Doc_01 SS2.1 / AUTHOR GRAVITY paragraph. Ruling: keep.** It is a genuine source note: it says where each population figure comes from (Palladius's present-tense count, as against the death-time estimate attributed to Doc_01 SS2.1 in `divergence_note`) and which hedges the text carries. Optional trim of two compliance-style sentences: "desert.source.rousseau-pachomius is not cited here (koinonia's own citation is not duplicated)" and "This body declares a relation to desert.gravity.authority-tension, which it invokes in prose."

**8. Not substantial — wording changes the author flagged.**
- `angel-hands-the-tablet` `modern_contrast`: the old line "That is what this world had previously assumed" was build history in a spoken field, and a voice would have misread it as the monks' own assumption. The new line, "Palladius and Sozomen can be read as wrapping the angel and the tablet around a plain rule they knew from outside", states the modern reading that the next sentence corrects. Accepted. In the body, "The description is carried in desert.source.pachomian-corpus" lost its referent. Suggest: "The correction, and the earlier description it replaces, are carried in desert.source.pachomian-corpus."
- `kellia-day` `absent_detail`: see finding 2.
- `someone-like-me` opener: "Someone with a past they are ashamed of, or with nothing special to recommend them, had a place among us." This is the same claim as the old conditional "... would have had a place among us ... the answer is yes", and the kept "close to the rule" carries it. Accepted.

**9. Not substantial — other changed records, checked old against new.**
- `born-again`: "spoke of being born again" is attested (Palladius ch. XLV, line 495, verified).
- `death-wish`: reordered; no claim changed.
- `grace-and-effort`: "What we would say plainly is this:" dropped; the Cassian source-event question is kept, correctly.
- `judgment-and-resurrection`: the closing sentence moved to the front; both "developed system" and "developed sequence or shape" are kept.
- `never-settled`: the questions became "One view ... The other ..."; same content.
- `only-true-religion`: reordered; "We told them so plainly" still has its antecedent.
- `antony-call` and `antony-tomb-combat`: the directive "neither should a telling of it" and "does not let a Representative go further" removed, claims kept.
- `pachomius-founding` and `virgin` `modern_contrast`: the stage directions "notice ..." and "as this record's own tellable_as ..." removed, content kept.

No claim was dropped or added. No antecedent is orphaned in the edited texts. In `dw.jesus`, "independently verified" lost "independently" in the body; this is harmless.

**10. Not substantial — leftover scaffolding sweep.** I swept every witness, term and story spoken field for question forms, second-person directions, "notice/note that/you should", restatement openers and build references. Found:
- finding 5 above;
- in `grace-and-effort` and `antony-tomb-combat`, the questions are source speech, correctly kept;
- second-person "you" in terms and stories is generic or quoted source speech;
- internal record ids are embedded in spoken `modern_contrast` fields (`antony-call`, `antony-tomb-combat`, `kellia-day`, `pachomius-founding`, `arsenius-flee`, `antony-withdrawal`; "This world's own record frames ..."). This is outside the brief's scaffolding definition and pre-existing, but it is build vocabulary a voice could speak. Log it in OG-21 next to the `sarah-answer` stray reference; do not fix it in this pass.

**11. Checks passed.**
- (f) The only changes outside `records/desert` and `Build/` are `records/worlds/desert.yaml` (pin to `packages/desert/2026-10-06T23-29-25Z`), that package's `manifest.json`, and `cic-website/data/worlds/desert-monasticism.json`. Compared field by field, the JSON differs only in `_generated_by` (records commit) and the two recompiled cites (`dw.jesus`, `dw.someone-like-me`).
- (g) No quote record was touched. The Philoromus line matches Palladius line 495 (paraphrase unchanged). Vita SS2 line 31244 and SS74 line 33023 confirm the command-giver ("the Lord") and "the Word of God was not changed".
- `regate desert --base origin/main` re-run: PASS, every miss unchanged from base. `check_live_commentary --enforce` exit 0.
- OG-21 is the next free number. Its heading wording "Oblique by its sources, reason:" matches the required phrase, capitalised at sentence start.

## Required for round 2
Findings 1-6 (the record fixes in 2 and 5, the body fix in 6, and the OG-21 corrections in 1, 2, 3, 4 and 10's logging line). Then rebuild the package, repin, and recompile the site if stale. The oblique-scope question in finding 1 and the head of this review goes to the project lead before `desert.dw.god` or `desert.dw.the-heart-and-the-spirit` is reordered.
