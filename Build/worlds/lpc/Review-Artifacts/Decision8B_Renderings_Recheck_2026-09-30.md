Simulated review — informational only, not an Article 31 substitute.

# lpc Decision 8B: targeted recheck of the renderings-check fixes

- **Reviewer model:** claude-opus-5-5
- **Drafter model:** claude-sonnet-5-5
- **Drafter note:** fix commit 7990e4168 carries the Sonnet 5.5 trailer. The rendering wording it applied is the round-1 Opus wording, except where item R2 says otherwise.
- **Reviewer agent:** targeted Opus recheck (fresh context; read the round-1 check, the entry on the renderings-check fixes (OG "Decision 8B renderings check applied, 2026-09-30"), the commit diff and the vendored sources)
- **Drafter agent:** renderings-check fix session (commit 7990e4168)
- **Round:** 2 (targeted recheck at medium effort: only what changed, against the round-1 findings)
- **Truncation check, method 1:** line count and closing marker: `wc -l` on this file returns 93 lines, and `tail -n 1` returns "End of recheck.", both run after the last edit.
- **Truncation check, method 2:** set comparison in Python: the item ids in the "Verdicts" table equal, as a set, the item ids used as `###` headings (R1 to R7); none is missing on either side.
- **Scope:** the changes in `git show 7990e4168 -- records/lpc` (27 files; the 26 record files and the new ledger entry). `git diff 7990e4168 HEAD -- records/lpc` touches none of the records this recheck covers, so HEAD holds the fixes as applied. Records only; nothing was edited.
- **Standards read:** Record-Native Build Process V2.0 section 6 (Decision 8B; the fragment rule; the source-spoken forms rule; the register rule; the rendering-fidelity birth condition); CLAUDE.md (source fidelity; accessible and rigorous; the Opus-authors-renderings rule).
- **Verdict:** every round-1 finding the fix session applied is resolved. No blocking or substantial finding. One note on model provenance for two renderings (R2), resolved here by Opus confirmation of the exact wording, with no text change. One optional precision note on the open host-locus item (R6). The round-1 proposal for B1 (section 9) was wrong; the fixer's section 10 is right.

## Gates and tools run directly

| Check | Result |
|---|---|
| All 22 registered gates (`engine.m1.gates.GATES`) on lpc | 0 findings in every gate except `readability` (1: `lpc.demo.road-back-examined` participant turn, FRE 52.9, unchanged and already carried by the entry on the B-7 voice record and demonstrations review, 2026-09-30) |
| `quote-verbatim`, `quote-mark-fidelity` | 0 findings each |
| `python -m engine.m10.cli records lpc` | PASS |
| `python -m engine.m10.cli regate lpc` | PASS (the one FRE finding is at the base and unchanged) |
| `engine/m1/sentence_completeness.py` on the six changed renderings (calibration clean) | 0 flags. Each sentence also read by hand for its own subject and verb |
| Independent line-range script (own code: endnotes and tags stripped, letters and digits compared, line of first and last matched character) on all 30 quote records | The 11 O1 records now match exactly. 9 others state a wider range that contains the text. None is outside its range |

## Verdicts

| Id | Item | Verdict | Severity |
|---|---|---|---|
| R1 | B1 locus of custom-handed-down-from-the-apostles | resolved | — |
| R2 | The six changed renderings | resolved; provenance note on two | note (no text change) |
| R3 | Changed lens notes and bodies (S3, S4, S5, O8, O9, O10, O11) | resolved | — |
| R4 | The six changed host sentences (H2 to H7) and the Celerinus "began" sentence (S3) | resolved | — |
| R5 | O1 line ranges | resolved | — |
| R6 | Open item H1 as stated in the ledger | correctly stated | optional (precision) |
| R7 | Rendering-fidelity graders | not run; already disclosed | note |

### R1 B1: the quote sits in Book IV, Chapter 6, section 10

Checked by structure marker in `cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml`. Line 11995 opens `<div3 type="Book" ... shorttitle="Book IV">`. Line 12150 opens `<div4 type="Chapter" n="6">`. Line 12152 is paragraph `v.iv.vi.vi-p1`, "Chapter 6.—9.". Line 12164 is paragraph `v.iv.vi.vi-p4`, which opens "10. We do not then...". The quote ("But this custom ... handed down from the apostles.") is inside that paragraph at line 12167. Chapter 6 closes before line 12173, which opens Chapter 7 ("Chapter 7.—11."). So the section is 10. The round-1 check proposed section 9; that was wrong, and the fixer was right to keep 10. The record now reads "Book IV, Chapter 6, section 10 ... line 12167". Resolved.

### R2 The six changed renderings

Each was read clause by clause against `text` and the vendored source.

- **christ-in-our-captive-brethren.** "ransomed ... ransomed" keeps the buy-back sense of "redeemed ... redeemed" (ANF05 lines 36038-36039) on both sides of the parallel. Every clause present, nothing added, sentences of 19, 9 and 18 words. Clear.
- **slept-with-his-fathers.** "he died and joined his ancestors" gives the sense of "he slept with his fathers" and cannot be heard as a doze. Every clause present, sentences of 6 and 24 words. Clear. The lens note still names the phrase "slept with his fathers". That is right: the lens note is builder-facing (stripped at compile, `engine/m2/builders.py`) and explains the source's own phrase.
- **no-donatist-bishop-in-the-succession.** "For suppose the line of bishops is to be taken into account. Then how much more surely, and how much more to the Church's good, we count back to Peter himself!" Both sentences have a subject and a finite verb (12 and 19 words). The concession is kept, "certainty and benefit" are both kept, and "reckon back till we reach" is rendered plainly. Clear.
- **lucian-already-weary.** "And we greet all those whose names I have not written, because I am already worn out." "And" is the source's own word (ANF05 line 30740). Nothing added; the rendering scores FRE 60.4. Clear.
- **thirteen-letters-transmitted.** "With the Lord's help, my poor abilities gave all of it as fully as they could, by the law of faith and the fear of God." The subject is clear. "to the full extent that ... my poor abilities could endeavour" is carried by "as fully as they could"; the source also makes "my poor abilities" the subject. The sentence is 26 words, within "about 25". Clear; no fix required.
- **to-answer-to-our-birth.** "counsels and urges" gives the older sense of "admonishes and exhorts" without the threat "warns" added. `text` now ends with the source's closing quotation mark (ANF05 line 27975), and `quote-verbatim` passes. Clear.

**Provenance note.** CLAUDE.md requires every `modern_rendering` and any re-rendering to be authored by Opus. Four of the six carry the round-1 Opus wording exactly (S1, S2, O5, O6). Two differ from it by the fix session's own choice. In O2 the fixer kept the source's "For" ("For suppose..."). In O4 the fixer wrote "And we greet" for the proposed "We also greet". Both changes are faithful and each is argued from the source in the ledger. This Opus recheck has read both, and confirms and adopts the exact wording now in the records as Opus wording. No text change. Recommended: the next ledger entry on this recheck records that the final wording of these two renderings is Opus-confirmed.

### R3 Changed lens notes and bodies

- **S3.** `lpc.quote.celerinus-tribulation-and-sister` `divergence_note` is null. The quote has no divergence of its own. Resolved.
- **S4.** The false body sentence is gone. Pontius's sentence ends at "the priesthood that was coming upon him." (ANF05 line 27825), inside the span. Resolved.
- **S5.** "These words come from the one first-person account we have" is true: the passage runs on in the first person (NPNF101 lines 13733-13735), and the record holds one sentence of it. Resolved.
- **O8.** The body names the mid-sentence start after "as what we in all cases decreed" (ANF05 line 30704), and says the rendering's "That" is the decision to give peace to all. That reading is right: the decree is "have given peace to all" at line 30702. Resolved.
- **O9.** The body names the opening condition, "Now, if this explanation suffices" (NPNF104 line 8128, section 74). Resolved.
- **O10.** The first `retrieve_when` line now fits a prayer about putting off chastity. Resolved.
- **O11.** The lens note now says Pontius names the two together, as one event, not as a count of votes. It no longer goes past the quote. Resolved.

### R4 Host sentences

Each changed sentence was read against its source and the sentence it replaced.

- **celerinus-writes-to-lucian (S3).** "He told Lucian that he was in the midst of a great tribulation, and the tribulation was not his own captivity." 21 words. The false "began" is gone; the words open section 2 of Epistle XX (ANF05 line 30569). Facts kept. Resolved.
- **celerinus-writes-to-lucian (H5).** "...and saying they must pardon him." 24 words. Keeps "must" from "Therefore they must pardon me" (ANF05 line 30741). Resolved.
- **election-of-cyprian (H2).** "Pontius did not soften this; he pressed it. Cyprian, he noted, was still in the early days of his faith, at an untaught stage of his spiritual life." The second sentence is 21 words and follows "Although still in the early days of his faith, and in the untaught season of his spiritual life" (ANF05 line 27821). Nothing added. Resolved.
- **the-psalms-on-the-wall (H6).** "Possidius put it in the words of Scripture: he slept with his fathers, well nourished in a good old age." 20 words. The words are now Scripture's own, and the sentence before already says he died. Resolved.
- **congregational-acclamation-overriding-preference (H3).** "By the judgment of God and the favour of the people, he wrote, Cyprian was chosen for the priesthood and the rank of bishop." 23 words. "he" is the deacon named in the sentence before. Faithful to ANF05 lines 27818-27820. Resolved.
- **augustine-engagement-cyprian-conciliar-acts (H7).** "Even among full councils of the whole church, he wrote, the earlier ones are often put right by those that come after." 22 words. Faithful to "even of the plenary Councils, the earlier are often corrected by those which follow them" (NPNF104 line 11303). The source asks this as a rhetorical question, so stating it as what he wrote is faithful. Resolved.
- **apostolic-succession-of-bishops (H4).** "Then they added that no Donatist bishop is found in this line of succession." 14 words. "anywhere" is gone, matching "In this order of succession no Donatist bishop is found." Resolved.

### R5 O1 line ranges

The independent script matches all eleven corrected ranges to the first and last matched character: all-our-power 28426-28429, grant-me-chastity 12744-12750, grief-of-mind 36009-36012, judging-no-man 56868-56871, judgment-of-god 27817-27825, letter-sent-back 28926-28935, plague-and-the-city 27939-27949, thirteen-letters 30188-30195, thousands-of-certificates 30198-30207, wealthy-and-rich-matron 47709-47717, weeping-in-hymns 13731-13733. The nine records the ledger says were left with a wider range (grace-sufficient, later-councils, lucian-hunger, no-donatist, penitential-psalms, restless-till, to-all-men, to-answer-to-our-birth and trees-eyes-and-executioner) each contain their text. (Trees-eyes was checked by hand: the text runs from line 28256 to 28267, inside the stated 28254-28267; the script's letter filter had dropped the "æ" of "Zacchæus".) Resolved.

### R6 Open item H1 as stated in the ledger

The ledger states it correctly. `lpc.witness.baptism-traced-to-the-apostles` `sources[0].locus` still reads "Book II, Chapter 7, SS10" for lines 12163-12169. The correct marker is Book IV, Chapter 6, section 10 (R1). Book II, Chapter 7, section 10 is at line 11394 (Book II's div3 opens at line 11233; Book III's opens at line 11579), a different passage. The ledger rightly says this field held no quotation, so the Decision 8B rule kept this pass from editing it, and it rightly records that the round-1 check had proposed section 9.

One precision point, optional. The ledger says paragraph 10 is at line 12163. Line 12163 is blank; paragraph 10 opens at line 12164 and ends at line 12169. The conclusion does not change. When the next host-record pass corrects the marker, it may also give the range as lines 12164-12169. Proposed `sources[0].locus` opening for that pass: `Book IV, Chapter 6, SS10`, with `lines 12164-12169`. The ledger is append-only, so the entry itself stays as written.

### R7 Rendering-fidelity graders

The Build Process makes `engine/m1/rendering_fidelity.py` a birth condition for a rendering. It was not run on the six re-renderings. It was not run on the original 30 either, which the entry on Decision 8B extraction for `lpc`, 2026-09-30, already discloses. Not a finding against these fixes. Every clause of the six was read by hand here and found present, with nothing added. The grader runs stay with that open disclosure.

End of recheck.
