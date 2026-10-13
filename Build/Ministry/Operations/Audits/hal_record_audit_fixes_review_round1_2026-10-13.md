Review round 1, hal record audit fixes, 2026-10-13, reviewer: independent Opus subagent

Verdict: NOT PASSED - 1 BLOCKING, 14 NON-BLOCKING

Scope: `git diff origin/main -- records/hal` on branch records/hal-audit-fixes. That is commits c289f0a (source citation lines), 17e5390 (wording pass), 4bfd8de (sin-grace source placement, oea-gourd locus, someone-like-me wording), plus the uncommitted edit to hal.dw.sin-grace. 116 files: 10 demonstrations, 12 doctrinal witnesses, 11 figures, 3 honest limits, 18 quotes, 28 source records, 11 stories, 19 terms. Facts were checked by grep against cic/texts/ (npnf206 Jerome, npnf203 Jerome's and Rufinus's Apologies, npnf101 Augustine's letters, npnf211 Sulpitius, anf04 Rufinus's prologue). Every changed spoken field was scored with grade_text.

Mechanical checks, all clean:
- YAML parses in all 116 files. No body paragraph changed. Changed keys are only spoken fields, `sources[]` entries/loci, figure `names`, and source `citation`. The sin-grace source entry now sits under `sources`. No other misplaced key was found.
- Readability: every changed spoken field passes (FK 1.6-9.6, FRE 60.2-96.4). The gate's remaining hal failures are all in `positions`, force, gravity, contested, core and voice fields, which are out of scope.
- Citation lines: all 28 source records have one. None matches a banned pattern. Apart from spelling out "NPNF2-06" as "Nicene and Post-Nicene Fathers, 2nd series, vol. 6" (the convention syr and rzg already use), every word comes from that record's author, work or edition field.
- New wording verified against the vendored text (sound): Ep22 secs 7, 28, 30, 37; Ep39 secs 6 and the "pardon a mother's tears" line; Ep77 secs 3-6, 10-11 (Fabian family, "storm of censure", Parthia in spring / Britain in summer, carrying the sick on her shoulders); Ep108 secs 5, 7, 10, 14-15, 19-20, 27, 29 (relatives remonstrating, ten days with Epiphanius, the miserable hostelry, borrowing and the mass of debt, the three companies, the refectory door, meat for the sick, "some people thought her mad", Palestine's cities at the funeral); Ep127 secs 7, 13-14; Ep139 "leave my pleasant home"; Against the Pelagians I.28 ("mercy is sometimes blended with the threatenings of God", "sit in judgment ... before the day of judgment") and the "penitence which is a copy of the grace of baptism" line; Jerome's Apology I.16 ("my master Donatus"), I.26-27 (the restitution charge and answer), II.4 ("Trinity in one Godhead", "you should rejoice in my invectives" in I); the Ezekiel I preface (the scorpion); the Vita Malchi prologue and close; the Job preface (the paid teacher); Ep57 sec 5 (order of the words a mystery); Sulpitius I.8 (six months); Rufinus's prologue; Augustine Ep71 sec 5 and Ep75 sec 22.
- Quote renderings: all 18 render every clause with nothing added and no sentence over about 25 words. Ellipses are kept where the text has them. The loci that changed were checked: Ep107 sec 13 (let-her-be-brought-up), Ep77 sec 11, Ep108 secs 6-14 / 14, 20, Ep127 secs 2-10, Ep22 sec 37, Apology I.25-27 / II.12-13 / II.3-5 all hold. The exception is oea-gourd (finding 8).

## BLOCKING

1. **hal.story.journey-to-bethlehem, text** (drift / misreading of source)
   - Current: `When winter was over and the sea was open, Paula went down to the harbor with her children on the shore.`
   - Source: npnf206 Ep108 sec 6, l.20967-20970: "And at last when the winter was over and the sea was open, and when the bishops were returning to their churches, she also sailed with them in her prayers and desires. Not to prolong the story, she went down to Portus accompanied by her brother, her kinsfolk and above all her own children..."
   - The spring clause dates the bishops' departure (382-383), when Paula sailed only "in her prayers and desires". Her real departure follows "Not to prolong the story", and Ep108 gives it no season. The new wording, written by the fixer, puts her sailing in a spring the source does not give. It also clashes with hal.story.rome-crisis ("He sailed east, and Paula followed") and Jerome's own date (Apology III.22: he sailed in August 385).
   - Proposed replacement (full field, FK 6.3 / FRE 78.7):
     `Paula went down to the harbor at Portus, with her children on the shore. The account says her eyes were dry, held toward heaven, as the ship pulled out. Her little son stretched out his hands from the beach. She sailed east by way of Cyprus, where the bishop Epiphanius kept her ten days. She went on to Antioch, and then down the whole length of the holy places, scripture in hand at every stop. At the cave in Bethlehem she wept and greeted the town by name, the house of bread where the Bread from heaven was born. She went on into Egypt, to Nitria, where the bishop Isidore came out to meet her with a great crowd of monks. She wished to press deeper into the desert and stay among the monastic settlements. Instead she turned back to Bethlehem. She lived there in a poor lodging at first, then in the monasteries her fortune built, for the rest of her life.`

## NON-BLOCKING

1. **hal.dw.practices text; hal.demo.born-again exchange[1]** (confidence / meaning change)
   - Current: `Born again was our word for baptism.` (both records)
   - Source: npnf206 Against the Pelagians III.15 l.45936-45937: "No sooner do they rise from the baptismal font, and by being born again and incorporated into our Lord..."; III.19 l.46119 quotes John 3:5.
   - The reviewed text this replaces said the opposite ("Born again is not our phrase"). That was wrong, since Jerome uses the phrase. But "our word for baptism" makes it a name for the rite, while the source treats it as what happens in baptism. The record's own position ("carry what 'born again' carries") and use_note ("parallel being born again") still say the old thing.
   - Proposed: dw.practices opens `We spoke of being born again in baptism. Jerome wrote that people rise from the font born again, and he quoted the Lord's words on being born of water and the Spirit.` (full field FK 6.4 / FRE 79.6). demo.born-again opens `We spoke of being born again in baptism, the washing that makes a person new.` (full turn FK 6.1 / FRE 79.6). Narrow the Against the Pelagians locus from `the passages on being born again in baptism` to `Book III secs. 15, 19 (the newly baptized "born again"; John 3:5)`.

2. **hal.demo.born-again, exchange[3]** (tell)
   - Current: `The turn was real, and the old loves stayed with him. He never made the two easy together.`
   - The last sentence is a coined closer added by the fixer. No source says it.
   - Proposed: end at `The turn was real, and the old loves stayed with him.` (full turn FK 6.0 / FRE 74.9).

3. **hal.demo.someone-like-me, exchange[1]** (drift / tell)
   - Current: `One of our own young women died within months of taking up hard fasting.` ... `As we remember them, they were open to the stranger and the sick poor. Nothing we kept speaks of a test at the door. ... But the hostel and the hospital were for strangers and the sick, whoever they were.`
   - Source: Ep39 never says Blaesilla fasted hard. Only the crowd says it (l.8112: "She weeps for her daughter, killed with fasting"). hal.dw.suffering and hal.figure.blaesilla say "soon after / within months of taking up the ascetic life". The "open to the stranger" sentence says the same thing as the closing sentence.
   - Proposed full turn (FK 6.0 / FRE 80.0): `I am a representative of the Bethlehem circle, not here to judge you - only to hand on what we held. The door of full renunciation was narrow, and it cost dearly. One of our own young women died within months of taking up the ascetic life. At her funeral, voices in the crowd said fasting had killed her, and asked why these detestable monks were not driven out of Rome, or stoned, or thrown into the Tiber. That was said of us, and we will not soften it. But renunciation - renuntiatio, our word for laying wealth and rank down - was never the whole of us. What we built with what we gave up reached past our own circle. A hostel stood for travelers on the road near Bethlehem. At Rome's own port there was a home for strangers. Jerome wrote that the whole world knew of it: Egypt and Parthia heard of it in the spring, and Britain by the summer. A hospital gathered the sick in from the streets. Nothing we kept speaks of a test at the door. Some of what we held about how a life should be given up will sound hard to you, and we held it firmly. But the hostel and the hospital were for strangers and the sick, whoever they were.`

4. **hal.dw.was-jesus-god, text and sources** (attribution / locus)
   - Current: `We also called him the true physician who restores the church to health.`, sourced to `Book I sec. 26 (Christ the true physician)`.
   - Source: npnf203 Apology I.26 l.52261-52264. These are Jerome's words, but they summarize Origen's exposition of Eph. 4:16 in the restitution passage. This is the very passage Rufinus attacked and that hal.dw.hell now cites as the charge. Giving it as plain community christology reverses that framing.
   - Also: `the blood by which we were bought back` is not in the cited loci. It is in Ep22 sec 39 (l.6871: "redeemed by the blood of Christ"). `a widow greeted his birthplace by name` is Ep108 sec 10, which is not cited.
   - Proposed full field (FK 7.8 / FRE 72.2): `Jesus is God the Son, of one being with the Father; and the Trinity - Father, Son, and Holy Spirit, one God - is simply the faith of the church, which we defended against every heresy we fought. We were born after the great council had settled that, and we never treated it as negotiable. To us it would be strange to hear it asked as an open question. We spoke of his death as redemption: the blood by which we were bought back. That is near to the later language of punishment in our place without being identical to it; the precise formula belongs to a later age. Personal Lord and Savior was not our phrase. But our scholar told a virgin to speak to him as her Bridegroom, and a widow greeted his birthplace by name. The devotion those words carry is close kin to what the modern phrase means.` Set the Ep22 locus to `secs. 1, 25, 39`, add hal.source.jerome-ep108 `sec. 10`, and drop the `Book I sec. 26` locus.

5. **hal.dw.inner-life, text** (drift, pre-existing in a touched field)
   - Current: `Love the knowledge of scripture, he told a young monk, and you will no longer love the sins of the flesh.`
   - Source: these are verbatim words from Ep125 to Rusticus (npnf206 l.25466). The record cites only Ep22 and Ep39, and no hal source record covers Ep125.
   - Proposed: either register Ep125 as a source (a build-record change, so log it in Open_Gaps_Tracking) or cut the sentence. The field still passes readability without it.

6. **hal.dw.empire, text** (drift)
   - Current: `Some of their own class thought they had gone mad, and said so.` and `get up before dawn to make social calls`.
   - Source: Ep108 sec 19 l.21653: a talebearer told Paula "some people thought her mad". It names one woman, not a class. Ep22 sec 28 l.6379: the cleric "rises and goes forth with the sun".
   - Proposed: `Some people thought Paula had gone mad, and said so.` and `get up with the sun to make social calls` (full field FK 7.9 / FRE 68.6).

7. **Demonstrations still carrying wording their ground witness dropped** (consistency; each field was touched in this pass)
   - hal.demo.hell: `Our own scholar had once handled sympathetically the teaching that in the end every creature, even the devil, would be restored - and we publicly renounced it.` hal.dw.hell now gives this as Rufinus's charge, which Jerome answered (Apology I.25-27). Proposed: `Our scholar was charged with favoring the teaching that in the end every creature, even the devil, would be restored. He answered that he had set it out as a heresy, and we publicly renounced it.`
   - hal.demo.suffering: `was burned by fellow Christians` becomes `was pillaged and partly burned by fellow Christians` (npnf206 l.28393, matching hal.dw.suffering). `The account says she lived long enough to give thanks that she died with her poverty complete.` becomes `The account says that before she died, she thanked God that the taking of the city had found her poor, not made her so.` (Ep127 sec 13, l.26369).
   - hal.demo.jesus: `To the penitent he is the doctor who receives the broken.` has no locus in hal.dw.jesus's sources, and this pass removed it from dw.jesus and dw.was-jesus-god. Proposed: cut the sentence. hal.dw.jesus `positions` still says "physician to the penitent", but that field is out of scope, so log it.
   - hal.demo.marriage-ending: `we honored her afterward above almost everyone`. hal.dw.marriage-ending now says only `we honored her afterward`. Proposed: match it.
   - hal.story.rome-crisis: `Paula's eldest daughter`. hal.figure.blaesilla dropped "eldest", and Ep39/Ep108 never state it. Proposed: `Paula's daughter`.

8. **hal.story.oea-gourd, sources[1].locus** (locus)
   - Current: under hal.source.jerome-augustine-letters (NPNF2-06): `Ep. 112 (the reply; Letter LXXV in the Augustine collection, sec. 22)`.
   - Source: Ep112 in npnf206 is a headnote only (l.22428-22446). The reply text, with "ciceion", the shrub, "that I might not differ from all other translators" and "malice or ignorance", is in npnf101 Letter LXXV sec. 22 (l.33966-34003), which is hal.source.augustine-letters. The new spoken sentences are correct, but this locus cannot be checked in the edition it names.
   - Proposed: set the augustine-letters locus to `Ep. 71 sec. 5 (the incident, in Augustine's hand); Ep. 75 sec. 22 (Jerome's reply on the gourd)`. Then either remove the jerome-augustine-letters entry or reduce its locus to `Ep. 112 (headnote only in this edition)`.

9. **hal.figure.marcella, bridge_line** (confidence)
   - Current: `Jerome later wrote that after he left, Roman clergy took their disputed questions about scripture to her`
   - Source: Ep127 sec 7: "recourse was had to her" by "many ... (including sometimes priests)". "Roman clergy" overstates a claim hal.contested.marcella-agency treats as contested.
   - Proposed: `the widow of the Aventine. Her household was already a circle when Jerome came to Rome. Jerome later wrote that after he left, people in Rome, priests sometimes among them, took their disputed questions about scripture to her` (FK 8.0 / FRE 60.4).

10. **hal.term.monasterium, plain_meaning and sources** (readability / locus)
    - Current: `The monastery. At Bethlehem it meant a men's house and a women's house, the women in three companies that prayed together, under one project. Paula, then Eustochium, led the women.` The embedded clause leaves "under one project" hanging.
    - Proposed: `The monastery. At Bethlehem it meant a men's house and a women's house under one project. The women lived in three companies that met to pray. Paula, then Eustochium, led the women.` (FK 5.2 / FRE 71.8).
    - senses.personal (`Jerome wrote that he prayed there himself`) is right, but it rests on Ep108 sec 10 (l.21196: "to pray in the cave"), and the Ep108 locus lists only secs 14, 19-20. Add sec 10.

11. **hal.story.desert-romances, text** (tell)
    - Current ending: `Whether every adventure happened is another matter. We tell them as the stories we told, not as history.`
    - The last sentence repeats tellable_as word for word in a "not X" closer.
    - Proposed: end at `Whether every adventure happened is another matter.` (full field FK 7.5 / FRE 63.5).

12. **hal.term.grammaticus and hal.term.praeceptor, sources[0].locus** (canonical-surface hygiene)
    - Current: `ch. 135, Jerome's own entry listing his works (does not mention Donatus)`.
    - The parenthesis is a reviewer's note inside a live record, and it records that the source does not support the term.
    - Proposed: `ch. 135 (Jerome's own entry and works-list)`. The Apology I.16 entry carries the Donatus claim, and that entry is correct (npnf203 l.51742).

13. **hal.quote.rufinus-writes-because-rome-is-where-the-news-is, modern_rendering** (rendering)
    - Current: `I venture to believe that you have refused to listen to any slanders against a person who is absent.`
    - Text: "any calumnies which may have been directed against an absent person". The rendering drops "which may have been directed", which is Rufinus's own hedge.
    - Proposed: `I venture to believe that you have refused to listen to any slanders that may have been aimed at a person who is absent.`

14. **hal.figure.paula-younger, names[0]** (label, note only)
    - `Paula` became `Paula the younger` under the in-world tag. This keeps her apart from hal.figure.paula and is acceptable. The sources call her "little Paula" (Ep107) or "Paula" (Ep137), never "the younger", so the tag is a convenience, not attested usage. Leave it as it is unless the label convention requires an attested form.

## Checked and sound (no finding)

- Fabiola across dw.believe, dw.marriage-ending, demo.believe, demo.marriage-ending, figure.fabiola and the vidua/nosocomium terms: the Fabian family, the storm of censure, the penance, the sale of her property, the hospital and the Portus hospice all match Ep77. The removal of "senator's daughter" is correct, since no source gives her father's rank.
- Blaesilla's death: "within months" matches the Ep39 headnote ("within three months") and sec 2 ("four months ago, renewed her baptism"). The crowd's words follow l.8110-8115. The one problem is "hard fasting" (NB 3).
- Paula as founder: figure.paula ("By Jerome's account, she paid for it"), xenodochium and monasterium all keep Jerome as the attributing voice. The Palladius quotes stand as the counter-witness.
- Honest limits: f5-enslaved, f5-women-own-words (the Ep46 authorship hedge matches hal.contested.ep46-authorship) and martyrdom are all sound.
- dw.hell, dw.church-failure, dw.doubt, dw.suffering, dw.authority, dw.apostolic (Pammachius and the friends' objection to Against Jovinianus is in that source record's work field), dw.record, dw.sin-grace and dw.jesus: every new sentence was traced to its source.
- Stories: attack-416, ciceronian-dream, day-at-monastery, marcella-death, marcella-standing, paula-epitaph (the corrected debt ending), rufinus-rupture and translating-a-book (the Ep57 correction and "at great cost" from the Job preface) are all verified.
- Figures augustine, blaesilla, damasus (December 384 is in its own dates field), eustochium, jerome, pammachius and rufinus are all sound.
- Terms: no new claim goes beyond the record. The we-voice spoken fields use no "this world" and no "historians/scholars".

## Disposition

Not approved to proceed until BLOCKING 1 is fixed and independently re-confirmed. The non-blocking findings should be applied in the same pass. NB 5 and the out-of-scope dw.jesus `positions` line in NB 7 should be logged in Build/worlds/hal Open_Gaps_Tracking if they are not fixed now.
