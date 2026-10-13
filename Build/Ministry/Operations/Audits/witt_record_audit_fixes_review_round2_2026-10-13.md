Review round 2 (targeted recheck), witt record audit fixes, 2026-10-13, reviewer: independent Opus subagent

Verdict: BLOCKING (one item, finding 1). Everything else rechecked is sound or non-blocking.

Scope: only the changes made since round 1 (the round 2 edit sets for terms, loci, demonstrations, doctrinal witnesses, the Walter story and the poor-man quote), read in the working tree with `git diff -U0 --word-diff` and checked against cic/texts/ and the cited witt records. Readability was run with engine.m1.gates.grade_text on every changed spoken field. All pass FK<=10 and FRE>=60. The lowest is witt.story.first-german-mass-sung text at FK 8.7 / FRE 67.3. The splice scan (item 7) covered every changed string field in all 210 changed record files. It looked for repeated sentences, repeated 7-word runs, editing-instruction words, a capitalised sentence after a dash, and doubled words. Every hit was then read by hand.

## Findings

1. **witt.demo.who-held-authority, exchange[1].text**: BLOCKING (ungrammatical join left by the substring editor)
   - Current: `God rules in two ways, we said. Through the Word he makes Christians and governed the conscience alone. Through the civil sword he restrained evil, and the sword did not touch the conscience at all.`
   - Cause: the round 2 edit replaced only `God ruled ... he made Christians`. The rest of the same sentence and the next one kept the past tense. The result is one coordinate verb pair in two tenses ("makes ... and governed"), and the two halves of the two-governments statement now sit in different tenses. This is the same class of defect as round 1 B3 and B4.
   - Fix: `Through the Word he makes Christians and governs the conscience alone. Through the civil sword he restrains evil, and the sword does not touch the conscience at all.` The other round 2 change in this field, `to preach there`, is correct (v2 14778-14779).

2. **witt.dw.cold-and-careless-among-us, text para 1**: NON-BLOCKING
   - The opening sentence now says the faith was failing "among those who taught it and those who heard it". It is followed by `He spoke of pastors and preachers of our own.`, and then by the 1522 "ass" line, which rebukes the congregation (v2 14681-14688). So the old mismatch is still there, one sentence lower. Suggest `He spoke of our own pastors and our own people.` The rest of the paragraph is sound. The 1522 and 1529 attributions are correct.

3. **witt.dw.true-priests-of-gods-own-making, sources[2].locus**: NON-BLOCKING (carried from round 1, finding 2)
   - It still reads `the only trace of an outside voice this library holds, since the Confutation itself is never independently vendored`. That is build vocabulary on a participant source card. Round 1 asked for it to be cleaned while the record was open. Suggest `our own Apology's quotation and answer to Rome's reply -- the only outside voice we have, and only at one remove`.

4. **witt.term.fear-and-love-god, plain_meaning**: NON-BLOCKING (minor redundancy, no splice)
   - `The First Commandment adds trust. So every commandment ties back to trust, the First Commandment's own lesson.` The duplicated sentence is gone. "After the first" and "adds trust" are both correct (SC l.53 "fear, love, and trust"; l.61-143 "fear and love God, so that"). The two closing sentences say "trust" twice. Optional: `So every commandment ties back to the First Commandment's lesson of trust.`

5. **witt.quote.the-poor-man-who-comes-to-you, modern_rendering**: NON-BLOCKING (style note only)
   - The conditional is kept. The rendering carries it as a chain of "When ... And when ... And when ..." clauses, each ending with a full stop, and then resolves it with "Then he will go away wretched". Each "when" clause is therefore a grammatical fragment. Read aloud, this works as Luther's own piling rhetoric, and it does not distort the sense. See the clause table below.

Carried open from round 1, not rechecked here because this round did not change them: the term.the-two-governments sources[3] "(OCR-degraded)" disclosure (round 1 B11); the "barely appear" wording in the positions/tensions of witt.dw.one-holy-church-forever and in witt.limit/demo.record-thinnest (round 1 A8c); "a point in our own confession" in witt.dw.what-we-have-never-settled para 3 (round 1 A9); and the old "no single household's own record survives" line, still quoted in the body prose (build notes) of witt.demo.someone-like-me and witt.demo.the-way-in.

## Poor-man rendering, clause by clause (text: LC l.1946-1956)

- "But beware of this" -> "But beware of this." Complete.
- "When the poor man comes to you" -> kept. "who must buy with the penny of his daily wages and live upon it" -> "the man who must buy ... and live on it." It stays a relative clause about the poor man, so round 1 problem (b) is fixed.
- "(of whom there are so many now)" -> "(There are so many of them now.)" Complete and kept as an aside.
- "and you are harsh to him, as though every one lived by your favor, and you skin and scrape to the bone" -> "And when you are harsh ... to the bone." This is now inside the conditional, so round 1 problem (a) is fixed.
- "and, besides, with pride and haughtiness turn him off to whom you ought to give for nothing" -> "And when, besides, you turn him away with pride and haughtiness, though you ought to give to him for nothing." Complete. "Though" keeps the sense of the relative clause.
- "he will go away wretched and sorrowful" -> "Then he will go away wretched and sorrowful." Complete.
- "and since he can complain to no one he will cry and call to heaven" -> "He can complain to no one, so he will cry and call to heaven." Complete.
- "-- then beware (I say again) as of the devil himself" -> "Then beware, I say again, as of the devil himself." Complete.
- "For such groaning and calling will be no jest, but will have a weight that will prove too heavy for you and all the world" -> two sentences. "Jest" becomes "joke", and "but" is dropped. Nothing is lost.
- "For it will reach Him who takes care of the poor sorrowful hearts, and will not allow them to go unavenged" -> two sentences. "He will not allow" takes "Him" as the subject, which is the natural reading.
- Nothing is added except "the man" (a restated subject) and "Then" (marking the main clause). Nothing is dropped. The longest sentence is 22 words ("When the poor man comes to you, the man who must buy ... live on it."), and none passes 25. Round 1 problem (c) is fixed. FK 4.0 / FRE 89.4.

## Changes checked and found sound

- **witt.term.household plain_meaning**: the duplicated present-tense sentence is gone. It reads once, in the past tense, as prescription. FK 4.8 / FRE 81.5.
- **witt.term.pastor plain_meaning**: "by name" is removed. It now reads `Our catechism rebukes lazy pastors.` (LC preface l.51). FK 6.2 / FRE 64.8.
- **witt.term.satisfaction senses.translational**: the subject appears once, and the sentence is grammatical.
- **witt.term.the-two-governments senses.personal**: the dash splice is now a full stop. The Fourth Petition is supported by LC l.3500-3504.
- **witt.term.pope-and-antichrist**: the editing instruction is gone from sources[1], which now reads `the Papacy at Rome (1520), the pope and the Roman Church`. sources[3] now carries `THE PAPACY IS THE MIGHTY HUNTING OF THE ROMAN BISHOP`, verbatim in capitals at v2 l.6512-6513, which is the Babylonian Captivity. plain_meaning `did not differ from that Church as its own writers showed it` keeps the limit in AC l.633 ("as known from its writers"). FK 6.6 / FRE 75.7.
- **witt.term.the-turk plain_meaning**: "is reported to have said he would pray against the pope and the Turk as long as he lived" matches TT l.3134 and is properly hedged for a contested table remark. The pairing is no longer turned into community practice. "Our household prayer asked that rulers vanquish him" matches LC l.3502-3504. FK 4.8 / FRE 80.3.
- **witt.gravity.promise-and-sign sources[1].locus**: `v1 2269-2274: baptism as sign, its meaning and faith` sits in the 1519 Baptism treatise ("three things--the sign, the significance thereof, and the faith", v1 l.2270-2272). It now matches its source_id.
- **witt.dw.true-priests-of-gods-own-making sources[0], sources[1]**: "two young monks" and "true priests of God's own making" are both in witt.story.brussels-martyrs (text l.64-81). The "library" phrase is gone. The hymn heading in sources[1] ("Two Christian Martyrs burnt at Brussels by the Sophists of Louvain", hymns l.1744-1745) and "two youths, highly gifted" (stanza 1, l.1756) are verbatim. "A single hymn, a single register ... the weakest evidentiary base of any term we hold" is verbatim in witt.term.martyr evidential.
- **witt.demo.someone-like-me and witt.demo.the-way-in loci**: the stale quotation is removed. "The weekly examination and food withheld until the words are said back" and "the morning sign of the cross and prayer" are both carried by the story (l.31, l.65, l.75).
- **witt.dw.scripture-judges-every-other-voice para 2**: the three repeated sentences are cut. The paragraph now ends at "...nor Rome's own writers." with no orphaned join.
- **witt.dw.one-holy-church-forever para 3**: "the break was real and that we held our ground" removes the repeat, and "our own texts let us tell" removes "library". "Our texts name none of those we broke with" is true: there are zero hits for Zwingli or Marburg in the ten witt-cited Luther and Melanchthon files. The sources[1] locus ("Article X ... 'they reject those that teach otherwise'", AC l.324) is correct.
- **witt.dw.what-we-have-never-settled para 3/4**: `Read in our founder's own words, these are not plainly one doctrine under one name.` no longer puts the judgment in Luther's mouth.
- **witt.dw.truly-god-and-truly-man para 2**: `no saint and no priest of ours beside him` removes the unsourced "scholar" and fits AC/Apology "one Mediator ... High Priest".
- **witt.story.first-german-mass-sung para 3**: `Walter's letter goes on: "The most profitable songs for the common multitude are the plain psalms and hymns ...," while the Latin songs "are useful for the learned and for students."` is verbatim against hymns l.776-779. The ellipsis now marks the dropped "both Luther's and the earlier ones", and the attribution is neutral.
- **Splice scan (item 7)**: apart from finding 1, no doubled sentence, no stray instruction and no dash splice remains in any changed field. Two hits were checked and cleared. The repeated "We can tell you exactly what a ..." in witt.demo.record-thinnest and witt.limit.record-thinnest is deliberate parallel phrasing, not a duplicate. "Instead of" in witt.force.imperial-frame is the LC quotation "a loaf of bread instead of a lion". In the same record, the round 2 join `Archbishop of Magdeburg and Mainz. Christian Nobility is addressed to` reads cleanly, as does the witt.figure.melanchthon bridge_line.

## Resolution

The blocking item (witt.demo.who-held-authority tense splice) was fixed after this round: "makes Christians and governs the conscience alone ... restrains evil, and the sword does not touch the conscience at all". The sources[2] locus of witt.dw.true-priests-of-gods-own-making and the repeated "trust" sentence in witt.term.fear-and-love-god were also fixed. The other non-blocking items are registered in OG-69.
