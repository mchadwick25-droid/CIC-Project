# Rendering Review: cappadocian quote records, batch 1 (21 records)

- **Reviewer:** Opus 5.5 (independent; did not draft or render any of these records)
- **Date:** 2026-11-03
- **Subject:** the `text` and `modern_rendering` of 21 `cappadocian.quote` records.

## Method

Each record's `text` is matched against the vendored file named in `sources[].locus`. The match is done by a script that removes `<note>` elements and other XML tags, rejoins line-end hyphens, and folds all whitespace (U+00A0 included). Segments are split at `[...]`. Line spans run from the line that holds the quote's first word to the line that holds its last word. Remaining differences were read by eye in the raw file. Typographic quotation marks (curly against straight), page-break tags and footnote markers count as apparatus, not text.

Each `modern_rendering` is read clause by clause against the edition text, and checked against `confidence.divergence_note` and `use_note.not_for`. Sentence lengths come from a script that splits at end punctuation and counts space-separated words. Quoted matter counts toward its sentence. A sentence of 28 words or more is over the bar of about 25 words. Bracketed or parenthetical supplements in `text` are checked so that none is voiced as the source's own words. Reported claims are checked to stay inside their reported-speech frame.

Files read: `cic/texts/npnf208_basil-letters-select-works.xml`, `cic/texts/basil_ascetic-works-longer-shorter-rules_clarke1925.txt`, `cic/texts/npnf205_gregory-nyssa-dogmatic-treatises.txt`, `cic/texts/julian_letters-1-73_wright1923.txt`, `cic/texts/gregory-nyssa_life-of-macrina_clarke1916.txt`.

## Results
**21 records: 9 PASS, 12 FAIL (2 P1, 10 P2).**

| Record id (cappadocian.quote.…) | Edition text at (file, lines) | Text check | Rendering check | Verdict |
|---|---|---|---|---|
| baptize-believe-glorify-in-sequence | cic/texts/npnf208_basil-letters-select-works.xml, lines 14168-14170 | pass | all three limbs of the dilemma kept; "as we have received" read as baptism handed down; longest 13 | PASS |
| basil-against-delaying-baptism | cic/texts/npnf208_basil-letters-select-works.xml, lines 7018-7024 | pass | all clauses; "viaticum" left as unglossed Latin whose modern sense (last communion for the dying) misleads here; longest 17 | FAIL P2 |
| basil-against-eunomius-ant | cic/texts/npnf208_basil-letters-select-works.xml, lines 24124-24133 and 24145-24151 | pass | all clauses both sides of the elision; "physiological" as "account of nature"; longest 21 | PASS |
| basil-canon-on-digamy | cic/texts/npnf208_basil-letters-select-works.xml, lines 35030-35035 | pass | all clauses; "polygamy" left bare in the closing sentence, where the modern sense (several spouses at once) misleads; longest 18 | FAIL P2 |
| basil-canon-to-amphilochius | cic/texts/npnf208_basil-letters-select-works.xml, lines 36336-36343 | pass | all four stages and the final admission kept; longest 20 | PASS |
| basil-on-antiphonal-psalmody | cic/texts/npnf208_basil-letters-select-works.xml, lines 37288-37302 | pass | all clauses; one sentence of 34 words joins the night of psalmody and the dawn psalm | FAIL P2 |
| basil-on-common-life | cic/texts/basil_ascetic-works-longer-shorter-rules_clarke1925.txt, lines 13190-13208 | FAIL: `text` reads "For just as", scan reads "Tor just as" (OCR misread, disclosed in divergence_note); stray "‘" before "To begin" and markers "1", "D", "?", "®" are apparatus | all clauses; "as it is written" kept; foot analogy whole; longest 24 | PASS |
| basil-on-eustathius-rupture | cic/texts/npnf208_basil-letters-select-works.xml, lines 39744-39753 | pass | all clauses; "they falsely accuse" frame kept; longest 24 | PASS |
| basil-on-his-retreat | cic/texts/npnf208_basil-letters-select-works.xml, lines 24024-24032 | pass | "admire the multitude of flowers" becomes "go on about the flowers" ("multitude" dropped, verb changed); "exhalations" becomes "scents"; longest 25 | FAIL P1 |
| basil-on-the-doxology-challenge | cic/texts/npnf208_basil-letters-select-works.xml, lines 8793-8822 | pass (curly quotation marks in the edition) | both doxology forms; objectors' charge kept inside "They said"; both purposes of the request; longest 23 | PASS |
| basil-on-work-and-prayer | cic/texts/basil_ascetic-works-longer-shorter-rules_clarke1925.txt, lines 17072-17096 | pass (quotation marks, line-end "every- thing", markers "®", "»", "E", "383A" are apparatus) | one sentence of 69 words; "some" becomes "some of you"; "the mark of pleasing God" thinned | FAIL P2 |
| basil-to-the-chorepiscopi | cic/texts/npnf208_basil-letters-select-works.xml, lines 27548-27555 | pass | one sentence of 30 words; "wish in ignorance to buy" becomes "try" | FAIL P2 |
| gregory-nyssa-on-becoming-god | cic/texts/npnf205_gregory-nyssa-dogmatic-treatises.txt, lines 44319-44337 | pass (footnote marker "[2002]" is apparatus) | all clauses; sentences of 28, 28 and 37 words | FAIL P2 |
| julian-galilaeans | cic/texts/julian_letters-1-73_wright1923.txt, line 556 | pass | all clauses; "Galilaeans" kept; opening sentence 28 words | FAIL P2 |
| macrina-refuses-remarriage | cic/texts/gregory-nyssa_life-of-macrina_clarke1916.txt, line 128 | pass (markers "\|25" and "[964D]" are apparatus) | "To be compelled to consider another was just as absurd and unlawful" stands outside "she would say", voiced as narrator's fact; "fame of her beauty" thinned; longest 22 | FAIL P1 |
| macrina-the-elder-taught-me | cic/texts/npnf208_basil-letters-select-works.xml, lines 37060-37068 | pass (the stray "]" after "fathers," is in the edition and is not voiced); note: `text` ends mid-sentence, before "and made them my soul's guides in my journey to God", though divergence_note says it runs to its full stop | all clauses of `text`; "delivered" as "handed down"; longest 21 | PASS |
| ousia-and-hypostasis | cic/texts/npnf208_basil-letters-select-works.xml, lines 25461-25468 | pass (curly quotation marks in the edition) | all clauses; "a man"/"Paul" contrast kept; longest 22 | PASS |
| reading-scripture-hexaemeron | cic/texts/npnf208_basil-letters-select-works.xml, lines 21217-21224 | pass (curly quotation marks in the edition) | all clauses; opening sentence 33 words with the verse inside it; "flying creatures that fly" | FAIL P2 |
| spirit-numbered-with-father-and-son | cic/texts/npnf208_basil-letters-select-works.xml, lines 10636-10645 | pass (page-break tag inside "de-fence" is apparatus) | all clauses; "ranked with the Father" kept, not raised to "is God"; longest 23 | PASS |
| we-look-to-the-east | cic/texts/npnf208_basil-letters-select-works.xml, lines 14068-14081 | pass | all clauses; opening sentence 33 words | FAIL P2 |
| what-is-the-written-source | cic/texts/npnf208_basil-letters-select-works.xml, lines 14128-14139 | pass | all clauses; sentences of 28 and 35 words | FAIL P2 |

## Failed renderings: corrected text

**basil-against-delaying-baptism.** "Viaticum" is left as an unglossed Latin term. To a modern reader it names the last communion given to the dying, but here Basil means baptism as the traveller's provision.

Corrected rendering:
> Are you young? Guard your youth with the bridle of baptism. Has your prime passed by? Do not go without your provision for the journey. Do not lose your safeguard. Do not treat the eleventh hour as if it were the first. Even at the beginning of life, it is fitting that we keep the end in view.

**basil-canon-on-digamy.** The closing sentence leaves "polygamy" bare, so a modern reader hears several spouses at once. The canon means many successive marriages.

Corrected rendering:
> For third marriages and more, they laid down the same rule as for a second marriage, in proportion. A second marriage carries one year (some authorities say two). For a third marriage, men are separated for three years, and often for four. But this is no longer called marriage at all. It is called polygamy, meaning many marriages, or rather, limited fornication.

**basil-on-antiphonal-psalmody.** One sentence runs to 34 words and joins two thoughts: the night of psalmody and the shared psalm at dawn.

Corrected rendering:
> Among us, the people go to the house of prayer at night. In distress, affliction, and continual tears, they make confession to God. At last they rise from their prayers and begin to sing psalms. Then they divide into two parts and sing antiphonally, answering one another. In this way they confirm their study of the Gospels. At the same time, they produce in themselves an attentive temper and a heart free from distraction. Afterwards they again hand the opening of the chant to one person, and the rest take it up. So they pass the night in varied psalmody, praying at intervals. As the day begins to dawn, all of them together, as with one voice and one heart, raise the psalm of confession to the Lord. Each one forms for himself his own words of penitence.

**basil-on-his-retreat.** "Another might admire the multitude of flowers" becomes "go on about the flowers". This drops "multitude" and turns admiring into talking at length. "Exhalations from the earth" becomes "scents", which adds a sense of smell the edition does not state.

Corrected rendering:
> Why should I tell of the vapours rising from the earth, or the breezes from the river? Another person might admire the many flowers and the singing birds. But I have no leisure for such thoughts. Still, the chief praise of the place is this. Being well suited to produce of every kind, it grows what is to me the sweetest produce of all: quiet. It is not only free of the city's bustle. Even travellers seldom pass that way, apart from a chance hunter.

**basil-on-work-and-prayer.** One sentence runs to 69 words. The rendering also turns "some" into "some of you", which names an addressee the edition does not, and it thins "the mark of pleasing God" to "pleasing him".

Corrected rendering:
> Some get out of work on the pretext of prayers and psalmody. Because of this, you must know that each separate task has its own special time. As Ecclesiastes says, 'There is a time for everything.' But for prayer and psalmody, as for many other things, every time is suitable. So we praise God with psalms, hymns, and spiritual songs while our hands move at work. We do it with the tongue, if that is possible and helps build up the faith. If not, we do it in the heart. We give thanks to him who gave strength of hand to work, and wisdom of mind to know how to work. He also gave the means to work, both in the tools we use and the arts we practise, whatever the work may be. We pray, moreover, that the works of our hands may be aimed at the mark of pleasing God.

**basil-to-the-chorepiscopi.** The second sentence runs to 30 words and joins the sale with its result. "Wish in ignorance to buy" becomes "try", which changes a wish into an attempt.

Corrected rendering:
> It is a lighter sin to wish, in ignorance, to buy the gift of God than to sell it. What happened was a sale. If you sell what you received as a free gift, you will be stripped of that gift. It will be as though you yourself were sold to Satan. You are pushing the peddler's trade into spiritual things and into the Church, where we are entrusted with the body and blood of Christ. These things must not be.

**gregory-nyssa-on-becoming-god.** Three sentences run past the bar, at 28, 28 and 37 words. The longest joins the purpose of the second presence with the rescue from death.

Corrected rendering:
> That God should be born in our nature ought not to seem strange to anyone who does not take too narrow a view of things. Who, surveying the universe, is so simple as not to believe that God is in everything? He penetrates it, embraces it, and is seated in it. All things depend on him who is. Nothing can exist that does not have its being in him who is. If, then, all things are in him, and he is in all things, why are people scandalized at the plan of Revelation? It teaches that God was born among men. He is the same God whom we are convinced is even now not outside mankind. This last form of God's presence among us is not the same as that former presence. Still, his existence among us is shown equally, both then and now. Only now, he who holds nature together in existence is transfused in us. At that other time, he was transfused throughout our nature. He did this so that our nature, through this transfusion of the divine, might itself become divine. So our nature was rescued from death and put beyond the reach of the enemy's caprice. For his return from death becomes, for our mortal race, the beginning of our return to immortal life.

**julian-galilaeans.** The opening sentence runs to 28 words, joining the condition with the order that follows from it.

Corrected rendering:
> But suppose they think those writers were wrong about the most honoured gods. Then let them go to the churches of the Galilaeans and expound Matthew and Luke. For you Galilaeans obey those writers when you order people to keep away from temple worship.

**macrina-refuses-remarriage.** "To be compelled to consider another was just as absurd and unlawful" stands outside the "she would say" frame. It reads as the narrator's own judgment, not Macrina's reported claim. "The fame of her beauty" is also thinned to "her beauty".

Corrected rendering:
> But the young man's death shattered the plan made for her. She then said her father's intention was the same as a marriage. So she resolved to stay single from then on, as if the intention had become accomplished fact. Indeed, her resolve was firmer than anyone could have expected at her age. Her parents often brought her proposals of marriage, because many suitors came, drawn by the fame of her beauty. Each time, she said it was absurd and unlawful to break faith with the marriage her father had arranged for her. She said it was just as absurd and unlawful to be forced to consider another. In the nature of things, she said, there is only one marriage, as there is one birth and one death. She insisted that the man joined to her by her parents' arrangement was not dead. Thanks to the hope of the resurrection, she held that he was alive to God, and absent only, not dead. It was wrong, she said, not to keep faith with the bridegroom who was away.

**reading-scripture-hexaemeron.** The opening sentence runs to 33 words because the verse sits inside it. "Flying creatures that fly" also repeats itself where the edition says "fowl that may fly".

Corrected rendering:
> If we simply read the words of Scripture, we find only a few short syllables. "Let the waters bring forth birds that may fly above the earth in the open firmament of heaven." But if we ask what these words mean, the great wonder of the Creator's wisdom appears. What a difference he foresaw among the winged creatures! How he divided them by kinds! How he marked each one with its own distinct qualities!

**we-look-to-the-east.** The opening sentence runs to 33 words, joining the habit of facing east with its forgotten reason.

Corrected rendering:
> So we all look to the East when we pray. But few of us know that we are seeking our own old country. That country is Paradise, which God planted in Eden, in the East. We pray standing on the first day of the week, but not all of us know the reason.

**what-is-the-written-source.** Two sentences run past the bar, at 28 and 35 words. The closing sentence joins the demand for written evidence with the list of matters it covers.

Corrected rendering:
> Time would fail me if I tried to recount the unwritten mysteries of the Church. Of the rest I say nothing. But take the very confession of our faith in Father, Son, and Holy Spirit. What is its written source? Suppose this is granted: as we are baptized, so, bound to believe, we make our confession in the same terms as our baptism. Suppose it is also granted that this follows the tradition of our baptism and agrees with the principles of true religion. Then let our opponents grant us the right to be as consistent in giving glory as in confessing our faith. If they object to our doxology because it lacks written authority, let them give us written evidence. Let them give it for the confession of our faith and for the other matters we have listed.
