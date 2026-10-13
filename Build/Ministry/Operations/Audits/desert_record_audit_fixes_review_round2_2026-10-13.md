Review round 2, desert record wording pass (spoken fields), 2026-10-13, reviewer: independent Opus subagent

Verdict: PASS WITH NON-BLOCKING

Scope: targeted recheck of commit a9752c2 ("desert records: fix the review round 1 findings"), 23 files under records/desert. Only the 23 changed fields were rechecked, against the round 1 findings (desert_record_audit_fixes_review_round1_2026-10-13.md) and the vendored sources. The YAML front matter of each file was parsed at HEAD~1 and at HEAD. Exactly 23 fields changed, one per file, and they are the fields round 1 named. No body text and no other key changed. No build record was touched. Every changed exchange turn is a representative turn. All 23 new values pass `grade_text` (FK <= 10, FRE >= 60); the lowest FRE is the-kingdom-is-apatheia at 60.8. Sources grepped: npnf204 (Vita Antonii), npnf211 (Cassian), anf09 (Origen), palladius_lausiac-history_clarke1918 ch. XXII, pachomius_rules-ethiopic_schodde1885, evagrius_praktikos_dysinger, macarius_fifty-spiritual-homilies_mason1921, palladius_paradise-v1-syriac_budge1907, and each quote record's own `text`.

Round 1 resolution: the blocking finding 1 (the-heart-and-the-spirit, "That teacher" pointing to Macarius) is resolved. "Our most systematic teacher" now names the referent, and the contrast with "This other current" holds. Non-blocking findings 2-13 and 15-21 are each resolved as proposed, or with equivalent wording that is checked against the source. Finding 15's new line, "trusted with a case that Antony himself sent on to him", matches Clarke ch. XXII [10] ("this is Paul's business ... led them to Paul"). Finding 14's five sentences are now all within the limit: origen-on-the-sinning-brother (longest sentence now 16 words, and "other things" is closer to "those things which exist in the masses" than the old "sins" was), grace-and-effort (14 and 13), center-coming-to-belief (6 and 21), identity-collision-someone-like-me (6 and 21), angel-hands-the-tablet (12 and 15).

## Findings

1. **desert.story.angel-hands-the-tablet, text**
   - New: `As he sat in his cave, the angel of the Lord came to him. The angel said he himself had become perfect, and that staying on in the cave was now a waste.`
   - Source: Schodde l.170: "said to him: 'With regard to thyself thou hast become perfect and a superfluous abidance dost thou now live in the cave'".
   - NON-BLOCKING. The split brings in a new pronoun problem. The old wording read "told him that he himself had become perfect", so "he" pointed to Pachomius. Now the sentence's subject is "The angel", and "he himself" most naturally points back to the angel. A listener can hear the angel calling himself perfect. Write "The angel told him he had become perfect, and that staying on in the cave was now a waste." That is 17 words.

2. **desert.demo.center-coming-to-belief, exchange[1].text**
   - Old: `...staying in the struggle, without forcing a feeling you do not have, is the closest thing our record shows to how belief was held among us.`
   - New: `What we can tell you is this. The closest thing our record shows to belief is staying in the struggle, without forcing a feeling you do not have.`
   - NON-BLOCKING. The split dropped "how ... was held among us". The line now says that struggle is the nearest thing to belief the record shows. That suggests these people lacked belief, which contradicts the turn's own "people who had already chosen this life". Restore the meaning. For example: "The closest our record comes to showing how belief was held among us is this: staying in the struggle, without forcing a feeling you do not have." Or split it into two sentences, each under 25 words.

3. **desert.demo.center-how-we-know, exchange[1].text**
   - New: `Ask an elder a question, and he might answer with a verse chosen for your one situation, rather than a teaching of his own - the words themselves carried the weight.` (31 words; it was 26 before the fix.)
   - NON-BLOCKING. Adopting the dw's wording (round 1 finding 17) is correct, but it makes the sentence longer than the ~25-word limit. Round 1 finding 14 named a sentence for the same reason (angel-hands-the-tablet, "lengthened by the fix"). Split at the dash: "...rather than a teaching of his own. The words themselves carried the weight."

The other 20 changed fields were checked and need no change. Front matter is intact.
