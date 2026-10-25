# Decision 8B Quotes Recheck: lpc, 2026-10-25 (round 2)

**Scope.** This is a targeted recheck of commit `69dcfcfe` against the round 1 findings in `Decision_8B_Quotes_Review_2026-10-25.md`. The diff checked is `git diff 04ec1cec HEAD -- records/lpc/quote records/lpc/story records/lpc/gravity Build/worlds/lpc/scripts/wb_lpc_s24.py Build/worlds/lpc/scripts/wb_lpc_s25.py`. Only what changed was checked.

**Not rechecked.** F9, F10 and F13 were set aside, not fixed. The acclamation rewrite was reverted out of this branch under the 8B scope ruling. It goes to its own PR and its own review.

**Reviewer.** Opus 5.5. No model API was called.

**Method.**
- Every new line range was re-read at both ends in the vendored file.
- Every `text` field on the 29 records was re-compared word for word, after stripping notes and tags. All 29 match, and every first and last word falls on the cited first and last line.
- Each changed rendering and host sentence was read against its source lines.

## Per-finding status

| # | Round 1 grade | Status | Notes |
|---|---|---|---|
| F1 | P1 | **Fixed** | Ranges below are as the records now cite them. Each was confirmed at both ends. |
| F2 | P1 | **Fixed** | The ellipsis is gone (details below). |
| F3 | P1 | **Fixed (meaning).** One new P2 on wording, R2-1. | The added clause is gone. The measure is again Cyprian's own abilities, with the Lord's help, under the law of faith and fear of God. That matches *quantum secundum legem fidei et timorem Dei Domino suggerente nostra mediocritas potuit eniti*. See R2-1 for the wording. |
| F4 | P1 | **Fixed** | The plague story now reads "bodies left where they fell, no longer bodies but the corpses of many". This matches Pontius, and the added cause is gone. |
| F5 | P1 | **Fixed** | The death story now reads "...an example to his own people, and said that with his blood discipline would begin to be made firm". The blood is now Cyprian's, as in Hartel 41316-41317. |
| F6 | P2 | **Fixed** | Trees: 41330-41359. Psalms Latin: 4887-4899. People-kept-watch end: 41250. |
| F7 | P2 | **Fixed in the record.** One new P2, R2-2. | The new `divergence_note` quotes *Psalmos Davidicos, qui sunt paucissimi de poenitentia* correctly (Weiskotten 4888-4889). The rendering now says "the very few penitential Psalms of David". The host story still says "shortest" (R2-2). |
| F8 | P2 | **Fixed** | Now "since the whole people had stayed in the street". This matches *omnes*. |
| F11 | P2 | **Partly fixed** | Fixed or logged: the conciliar gravity now relates to `lpc.quote.bishop-of-bishops`, and the quote relates back. The Acta 2.1 and *Retractationes* paraphrases are logged in OG-75, with the reason that every witness has OCR damage. Still open, and neither extracted nor logged: the Celerinus `absent_detail` quotation "that she might not sacrifice" and the quotations in the force `manifestations`. Still P2. |
| F12 | P2 | **Fixed** | Now "I ask that it be done as it is here ... Then let not only these women have peace...". *Sicut hic* now governs the procedure, and peace is its outcome, as in Hartel 3338-3342. |
| F9, F10, F13 | P2 | Set aside | Out of this branch, with its own PR to follow. |

**F1 ranges.**
- **English:** boast 53424-53433; grief 36009-36012; shut-up 30702-30711; such-a-one 29936-29949; earlier-councils 11301-11304. The body note on earlier-councils is aligned with the locus.
- **Latin:** thousands 2992-3012; plague 40782-40791; good-done 40854-40895; it-becomes-us 40837-40843; people-kept-watch 41246-41250.
- **he-slept:** handled under F2.

**F2 detail.**
- The text now begins at "with sight and hearing unimpaired" and matches Weiskotten 4979-4981 exactly.
- The dropped opening clause, "With all the members of his body intact," on line 4938, is disclosed in the body. The body also gives the Latin's full span, 4899-4942.
- The rendering and lens note drop the body clause to match.
- The host story's "his body whole" still rests on the source (4938, and *membris omnibus sui corporis incolumis*), so it says no more than the source.

## Pressing F3: does the new rendering meet the bar?

The new sentence is: "In them nothing lacked, as far as my poor abilities could strive, with the Lord's help, under the law of faith and fear of God."

- **Clauses.** Every clause is kept and nothing is added. Its length, 25 words, is within the bar.
- **Natural English.** Here it falls short.
  - "In them nothing lacked" uses inverted order and an intransitive *lack* that modern English no longer uses this way. It reads as translationese from *nec ... defuit*.
  - "Could strive" with no object is also stiff.
- **Meaning.** It does not mislead, so this is a wording finding, not a meaning finding.

## New findings

| # | Grade | Record | Finding | Fix |
|---|---|---|---|---|
| R2-1 | P2 | lpc.quote.thirteen-letters-sent-to-rome | The F3 rendering is accurate but not natural modern English. "In them nothing lacked ... could strive" reads as translationese. | For example: "Nothing was missing from them, as far as my poor abilities could manage, with the Lord's help, under the law of faith and the fear of God." Authored by Opus, per the rendering rule. |
| R2-2 | P2 | lpc.story.the-psalms-on-the-wall | The host sentence still says "He had the shortest penitential Psalms of David copied out". The quote record it points to now says the Latin means "very few". The host and its own record disagree. | Make the host sentence match, for example "the few penitential Psalms of David". This stays inside the quote's own sentence, so it is within the 8B scope. |

## Verdict

**Approved to proceed.**

- All five P1 findings (F1-F5) are fixed and re-verified at their source lines.
- No new P1 was found.
- The open items are all P2: R2-1, R2-2, and the remainder of F11. Each is a one-line fix or a log entry, and none needs another review round. R2-1 and R2-2 are worth taking before merge, because each is a single sentence.
