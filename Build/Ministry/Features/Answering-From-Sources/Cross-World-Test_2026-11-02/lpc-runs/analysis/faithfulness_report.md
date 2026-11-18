# Faithfulness check: telling_short / telling_medium, records/lpc/story (branch claude/engine-faithfulness)

All passages were read from the vendored files at the cited line ranges, with markup and notes stripped. Where a detail sits in the same file but outside the cited range, I give its line numbers.

## Summary

| Story | telling_short | telling_medium | Short T1/T2/T3 | Medium T1/T2/T3 |
|---|---|---|---|---|
| celerinus-writes-to-lucian | faithful (craft note) | faithful (craft notes) | 0/0/1 | 0/0/2 |
| election-of-cyprian | FAIL | FAIL | 0/1/1 | 1/0/0 |
| hundred-thousand-sesterces | faithful | faithful | 0/0/0 | 0/0/0 |
| numidicus | faithful (craft note) | faithful | 0/0/1 | 0/0/0 |
| the-death-of-cyprian | FAIL | FAIL | 1/0/1 | 1/0/1 |
| the-plague-and-the-enemies | faithful (craft note) | faithful (craft notes) | 0/0/1 | 0/0/2 |
| the-psalms-on-the-wall | faithful | FAIL | 0/0/0 | 0/1/0 |

Lower-tier issues in the full `telling`, which the shortened tellings inherit, are listed separately at the end. The most important is in hundred-thousand-sesterces. Its "not about charity" line appears in all three tellings, and the passage contradicts it.

---

## celerinus-writes-to-lucian

**telling_short: faithful.** Every essential event is kept in order: the plea for the sister, the request for Numeria and Candida, and the grant with its bishop condition.
- T3 (a, scope): short has "Then, he asked, let the women have peace." The full telling has "let not only these women have peace, but also those whom you know to be dear to our heart". The passage (l.30731-30732) has "I ask that not only these may have peace, but also (all) those whom you know to be very near to our heart." The short version drops the wider scope of Lucian's grant. It does not falsify anything.

**telling_medium: faithful.**
- T3 (a, scope): the same "let the women have peace" narrowing as in the short telling.
- T3 (d, reasoning order): the medium telling drops the Tria Fata sentence. Now "So I know she has not sacrificed" follows straight after "Candida had given gifts so that she would not have to sacrifice." In the passage, "I know, therefore" follows "she appears only to have ascended to the Tria Fata, and thence to have descended". The "so" now rests on a different premise.

## election-of-cyprian

**telling_short: FAIL.**
- T2 (d, addressee): short has "Later, answering rivals, Cyprian called it our suffrage...". The full telling has "Cyprian answered them in a letter to us." The passage is Ep. XXXIX, headed "To the People", and it speaks about "certain of the presbyters" in the third person. Without "in a letter to us", the short telling reads as Cyprian addressing the rivals. The addressee has changed.
- T3 (c): short has "our suffrage, the support of the people, joined to God's judgment". The full telling has "against your suffrage and against God's judgment". The passage has "that is, against your suffrage and God's judgment". Two things the passage only pairs with "and" become "joined to" in Cyprian's mouth. Also, "the support of the people" is the narrator's gloss in the full telling ("By suffrage he meant..."), and the short telling folds it into what Cyprian "called it".
- The non-essential withdrawal/besieged-doors event is dropped. That is acceptable, though the record's own tellable_as is "over his reluctance".

**telling_medium: FAIL.**
- T1 (b, added meaning attributed to Cyprian): medium has "By suffrage he meant the support of the people, joined to God's judgment." The full telling has "By suffrage he meant the support of the people." In the passage, suffrage and God's judgment are two separate objects ("your suffrage and God's judgment"). The medium telling makes God's judgment part of what Cyprian meant by "suffrage". That fact is not in the full telling or the passage. It also puts into Cyprian's words the relation that the claim_guard marks as our own Inferential-Thin reading.
- The rest is faithful. The addressee is kept ("Cyprian wrote to us").

## hundred-thousand-sesterces

**telling_short: faithful.** It keeps the captivity, the eight bishops' letter, the Pauline argument, the conclusion and the sum, in order, with nothing added. It does inherit the lower-tier "not about charity" defect below.

**telling_medium: faithful.** It follows the full telling clause for clause. It inherits the lower-tier "not about charity" line and the order issue below.

## numidicus

**telling_short: faithful.** All nine essential events are kept in order.
- T3: short has "We called her death a completion, not a loss." The full telling has "we did not count a martyr's death as a loss ... We named it as a completion". The short telling makes the general stance into a past act about her in particular. This is craft only.

**telling_medium: faithful.** All the quoted lines and the order match the full telling. "Cyprian saw a reason why he survived" keeps the attribution ("as we see" in the passage).

## the-death-of-cyprian

**telling_short: FAIL.**
- T1 (b, quotation not in full telling): short has "So the blessed Cyprian suffered martyrdom." This sentence is not in the full `telling`. It appears only in `text` and `events`, where it is marked essential although the full telling does not contain it. The Acta 6 supports it ("ita beatus Cyprianus passus est", Knopf l.4917). So it is not false, but it fails test (b) as defined. Also, the short telling gives it unattributed, in the narrator's voice.
- T3 (a): the short telling drops the fact that in the Acta Cyprian "covered them with his hand" (passage: "manu sua oculos sibi texit"). It says only "In the Acta, two clergy, both named Julianus, tied them." The difference between the texts can now read as larger than it is. The full telling and use_note limit it to who tied the cloths.
- Otherwise faithful. "Sentenced as an enemy of the gods" is in the Acta ("inimicum te diis Romanis"), and the Deo gratias line and the brothers' cry are kept in order.

**telling_medium: FAIL.**
- T1 (b): medium has "So, in the Acta, the blessed Cyprian suffered martyrdom." The defect is the same as in the short telling: the sentence is absent from the full telling. Here it is at least attributed to the Acta.
- T3 (a): the same dropped detail, that in the Acta he covered his own eyes.
- Pontius's executioner material is correctly attributed ("In his telling..."), which meets the claim_guard. The medium telling also drops "On the sentence, the two texts are not independent witnesses". That is acceptable, because the medium telling no longer claims the two texts agree on the sentence.

## the-plague-and-the-enemies

**telling_short: faithful.**
- T3 (c): the short telling drops "To be perfect, we must do more than the tax collector or the pagan." So "We must love even our enemies" is no longer framed as the way to perfection. The passage has "he might become perfect who would do something more than the publican or the heathen, who ... loved even his enemies". This is a mild loss of the conditional framing. The preceding line about "nothing remarkable" keeps the "more than" logic.

**telling_medium: faithful.**
- T3 (c): the same "To be perfect" drop.
- T3 (attribution): medium has "Tobias gathered the bodies of his own race only. More was done here." The full telling has "Tobias, Pontius says, ...". The attribution carries over from "Then, Pontius says" earlier in the paragraph, but "More was done here" now reads closer to narrator assertion. The medium telling also drops "those the king had killed". That is acceptable.

## the-psalms-on-the-wall

**telling_short: faithful.** It is a strict prefix of the full telling (friend, the teaching, the psalms and weeping), word for word.

**telling_medium: FAIL.**
- T2 (d, order): the medium telling moves "About ten days before the end, he asked that only the doctors and those bringing food come in. The request was kept..." to the very end, after "he slept with his fathers" and "He made no will". In the full telling and in the passage (l.4930-4935), the ten-day request comes before the death. As written, the medium telling tells of a request made "ten days before the end" after the end itself.
- Otherwise faithful ("fell ill with a fever while the Vandals besieged Hippo" matches the full telling).

---

## Lower tier: the full `telling` against the cited passage (inherited by shortened tellings where noted)

**hundred-thousand-sesterces**
- The full telling, the short telling and the medium telling all say "His argument was not about charity but about who the captives were." The passage (l.36006-36020) says "not love only, but also religion, ought to instigate and strengthen us", and "even although love urged us less". Cyprian argues from love *and* religion. The telling turns "not only love" into "not about charity". This is a strengthening (c), and both shortened tellings carry it.
- "Eight bishops in Numidia": in the cited body text (36006-36090), "Numidian" and "bishops" do not appear. The recipients are "his brethren". Those words are only in the heading and Argument, just before l.36006. They are not in the cited passage.
- Order: in the passage, the thanks for "fruitful fields" (l.~36075) comes before "We have then sent you a sum of one hundred thousand sesterces" (l.36082). The full telling and the medium telling reverse this.
- The test is put in quote marks as a direct question ("Will each of us do...?"). The passage has a clause: Christ "suffers these things to happen ... that our faith may be tried, whether each one of us will do...".

**celerinus-writes-to-lucian**
- The cited range (30528-30720) stops mid-way through the list of martyrs. Lucian's condition ("the case being set forth before the bishop, and confession being made", l.30728-30732) is outside it. So are the "not only these" request and "I am already weary. Therefore they must pardon me" (l.30740-30741). The record's essential condition, which both shortened tellings keep, is not in the cited passage. It is in the same file a few lines later.
- "a man who had been imprisoned": not in the cited passage. Celerinus speaks of his "confession", not of a prison.
- "a death of the spirit" rests on the ANF translator's own parenthesis "(spiritual)". "She was still alive in body" is an inference and is not in the passage.
- "He would weep ... until help came through Lucian or through the martyrs": the passage has "until the aid of our Lord Jesus Christ, and affection manifested through you, or through those my lords who have been crowned". The telling drops Christ as the source of the help. The medium telling inherits this.
- "the sin openly confessed": "openly" is not in the passage ("confession being made"). The condition is also tied to "since the Lord has begun to give peace to the Church itself", which the telling drops. Both shortened tellings inherit "openly".

**election-of-cyprian**
- "a work in praise of his bishop": not in the cited passages. They give the title "By Pontius the Deacon", section 5, and the execution.
- "He gave way to older men": the passage has "men of older standing", which means seniority, not age.
- "rivals who had never accepted him": the passage has "certain of the presbyters ... retaining that ancient venom against my episcopate". "Never" is a slight strengthening. "Cyprian answered them in a letter to us": the letter is to the people *about* them, not a reply to them. This loose phrasing is the root of the short telling's T2 error.

**numidicus**
- The ANF note at "remained unwillingly" reads 'Otherwise, "unconquered."' That is a variant reading (invitus/invictus). The full telling, both shortened tellings and the use/text fields state "Against his will" without that hedge.

**the-death-of-cyprian**
- "14 September 258": the day is in the Acta ("octaua decima kalendarum Octobrium", Knopf l.~4955). The year 258 is not in the cited passages. All three tellings carry it.
- Pontius has "strengthened the hand of the centurion". The full telling ("his hand", after "The executioner") and the medium telling ("the executioner's fingers trembled until ... strengthened his hand") give it as the executioner's hand.
- "On the sentence, the two texts are not independent witnesses" is a scholarly judgment. It is not in the cited passage.
- The quote "Meanwhile the whole people kept watch before the officer's door" leaves out a clause ("in anxiety that nothing should be done throughout the night without their knowledge") without an ellipsis. Both shortened tellings use this quote.

**the-plague-and-the-enemies**
- The cited range (27920-27980) ends at "But if the Gentiles could have heard...". The relief outcome falls outside it: "good was done ... to all men, not to those only who are of the household of faith" (l.27992), the poor's labour (l.~27988) and Tobias (l.27993-27998). The essential final event, which both shortened tellings keep, is not in the cited passage. It is in the same file.
- Order: in the passage, the poor's labour comes before "good was done to all". The full telling and the medium telling reverse this.
- "Our deacon Pontius was there" and "He wrote it in praise of the man who preached": neither is in the cited passage. Both shortened tellings carry them.
- "Our bishop gathered us in one place": the passage has "On the people assembled together in one place". It does not say he gathered them. Both shortened tellings carry this.

**the-psalms-on-the-wall**
- The cited lines (4900-5000) hold only chapter XXXI. The locus label says SS28-31, which contradicts its own line range. The siege and fever ("in the third month of the siege he succumbed to fever", l.4147) and the forty-year friendship (l.5059-5060) are outside the cited lines. Both shortened tellings carry "friend for nearly forty years", and the medium telling carries the siege and fever. Note also that l.4920 says "almost forty" years "as a priest or bishop", which is a different fact.
- "the very few penitential Psalms" is in quote marks, but the cited English (l.4925) says "shortest". The Latin "qui sunt paucissimi" (l.4888-4889, just before the cited span) supports "very few". The quote is therefore not verbatim against the cited English, and the two words make different claims (number against length). Both shortened tellings carry it.
