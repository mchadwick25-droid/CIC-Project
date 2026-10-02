# Authoring brief: modern renderings for 12 quote records

You are writing the `modern_rendering` for each of the 12 quote records below. A modern rendering is what a Representative says aloud when it quotes this source to a participant today. The `text` field is the source's own wording; it stays unchanged. Your job is to write its modern-English rendering.

## What you may read

- This brief.
- `reference/method/CiC_Register_Bar_2026-08-29.md` (the register bar: the approved sample of the house register).
- Section 3, "Phase B — Record-store authoring", of `reference/method/CiC_Record_Native_World_Build_Process_V1.5.md`.

Read nothing else. Do not open any file under `records/`, `worlds/`, `packages/`, `engine/` or `Ministry/`. Do not search the repository. Do not use git history. Do not write or edit any file. Everything you need about each record is in this brief.

## The rules

1. **Translation, not summation.** The project lead's words: *"the representitive translates it into modern english, this is translation, not summation."*
2. **Every clause, nothing more.** Every clause of the `text` must be present in the rendering. Add nothing: no explanation, no qualification, no claim, no emphasis the original does not state. Compress nothing: do not merge two claims into one or shorten a passage into a paraphrase.
3. **Everyday modern English.** Keep an original word only where it survives plainly in everyday modern English. Translate an archaic word or idiom into its plain modern equivalent. Do not keep a period form because it sounds dignified.
4. **Whole sentences.** Every sentence has its own subject and verb, and carries one whole thought. You may split a long sentence into shorter ones only if every resulting sentence is whole. There are three source-form exceptions:
   - an interjection or answer the source itself speaks stays as the source has it;
   - a list becomes one sentence;
   - a true ellipsis (a clause the source leaves implied) is finished, so the sentence is whole.
5. **Match the register bar.** Practical, straight, clear modern English; simple sentences; a scholar's term only after its plain meaning.

## Output format

Return exactly this, once per record, in the order given, and nothing else:

```
### <record id>
RENDERING: <the modern rendering, as one paragraph>
NOTE: <one line on the hardest choice you made, or "none">
```

After the 12 records, add one final line:

```
MODEL: <the exact model id you are running as>
```

## The 12 records

Each record's `text` below is copied verbatim from its record file at commit `c057a8c2`.

### cappadocian.quote.basil-canon-to-amphilochius

- World: Cappadocian Christianity (325–394)
- Source: Letter CXCIX (Canonica Secunda), Canon XXII (npnf208_basil-letters-select-works.xml)

text:

> In the case of a man having a wife by seduction, be it secret or by violence, he must be held guilty of fornication. The punishment of fornicators is fixed at four years. In the first year they must be expelled from prayer, and weep at the door of the church; in the second they may be received to sermon; in the third to penance; in the fourth to standing with the people, while they are withheld from the oblation. Finally, they may be admitted to the communion of the good gift.

### cappadocian.quote.basil-on-the-doxology-challenge

- World: Cappadocian Christianity (325–394)
- Source: On the Holy Spirit, ch. 1, sec. 3 (npnf208_basil-letters-select-works.xml)

text:

> Lately when praying with the people, and using the full doxology to God the Father in both forms, at one time "with the Son together with the Holy Ghost," and at another "through the Son in the Holy Ghost," I was attacked by some of those present on the ground that I was introducing novel and at the same time mutually contradictory terms. You, however, chiefly with the view of benefiting them, or, if they are wholly incurable, for the security of such as may fall in with them, have expressed the opinion that some clear instruction ought to be published concerning the force underlying the syllables employed. I will therefore write as concisely as possible, in the endeavour to lay down some admitted principle for the discussion.

### cappadocian.quote.what-is-the-written-source

- World: Cappadocian Christianity (325–394)
- Source: On the Holy Spirit, ch. 27, sec. 67 (npnf208_basil-letters-select-works.xml)

text:

> Time will fail me if I attempt to recount the unwritten mysteries of the Church. Of the rest I say nothing; but of the very confession of our faith in Father, Son, and Holy Ghost, what is the written source? If it be granted that, as we are baptized, so also under the obligation to believe, we make our confession in like terms as our baptism, in accordance with the tradition of our baptism and in conformity with the principles of true religion, let our opponents grant us too the right to be as consistent in our ascription of glory as in our confession of faith. If they deprecate our doxology on the ground that it lacks written authority, let them give us the written evidence for the confession of our faith and the other matters which we have enumerated.

### rzg.quote.signs-and-things-signified

- World: The Reformed Cities - Zurich & Geneva (1519–1650)
- Source: 9th Head of Agreement, lines 768-770

text:

> Wherefore, though we distinguish, as we ought, between the signs and the things signified, yet we do not disjoin the reality from the signs...

### hal.quote.dispute-to-learn

- World: Hieronymian Ascetic-Literary Christianity (382–420)
- Source: sec. 7

text:

> she never came to see me that she did not ask me some question concerning them, nor would she at once acquiesce in my explanations but on the contrary would dispute them; not, however, for argument's sake but to learn the answers to those objections which might, as she saw, be made to my statements.

### hal.quote.ever-let-the-bridegroom-sport-with-you

- World: Hieronymian Ascetic-Literary Christianity (382–420)
- Source: Letter XXII (to Eustochium), sec. 25 (npnf206_jerome-principal-works.xml)

text:

> Ever let the privacy of your chamber guard you; ever let the Bridegroom sport with you within. Do you pray? You speak to the Bridegroom. Do you read? He speaks to you. When sleep overtakes you He will come behind and put His hand through the hole of the door, and your heart shall be moved for Him; and you will awake and rise up and say: "I am sick of love."...

### pahc.quote.melito-no-phantom

- World: Post-Apostolic Household-Church Christianity (70–200)
- Source: Melito of Sardis, Fragment VII, 'On the Nature of Christ' (anf08 lines 71176-71206), citing Anastasius of Sinai, The Guide, ch. 13

text:

> For there is no need, to persons of intelligence, to attempt to prove, from the deeds of Christ subsequent to His baptism, that His soul and His body, His human nature like ours, were real, and no phantom of the imagination. For the deeds done by Christ after His baptism, and especially His miracles, gave indication and assurance to the world of the Deity hidden in His flesh. For, being at once both God and perfect man likewise, He gave us sure indications of His two natures: of His Deity, by His miracles during the three years that elapsed after His baptism; of His humanity, during the thirty similar periods which preceded His baptism, in which, by reason of His low estate as regards the flesh, He concealed the signs of His Deity, although He was the true God existing before all ages.

### pahc.quote.ignatius-truly-born

- World: Post-Apostolic Household-Church Christianity (70–200)
- Source: Trallians 9, shorter (middle) recension

text:

> Stop your ears, therefore, when any one speaks to you at variance with Jesus Christ, who was descended from David, and was also of Mary; who was truly born, and did eat and drink. He was truly persecuted under Pontius Pilate; He was truly crucified, and [truly] died, in the sight of beings in heaven, and on earth, and under the earth. He was also truly raised from the dead, His Father quickening Him, even as after the same manner His Father will so raise up us who believe in Him by Christ Jesus, apart from whom we do not possess the true life.

### pahc.quote.polycrates-to-victor

- World: Post-Apostolic Household-Church Christianity (70–200)
- Source: Polycrates of Ephesus, from his Epistle to Victor and the Roman Church (anf08 line 72521; the passage at 72582), preserved in Eusebius HE V.24

text:

> As for us, then, we scrupulously observe the exact day, neither adding nor taking away. For in Asia great luminaries have gone to their rest, who shall rise again in the day of the coming of the Lord... Moreover I also, Polycrates, who am the least of you all, in accordance with the tradition of my relatives, some of whom I have succeeded—seven of my relatives were bishops, and I am the eighth, and my relatives always observed the day when the people put away the leaven—I myself, brethren, I say, who am sixty-five years old in the Lord, and have fallen in with the brethren in all parts of the world, and have read through all Holy Scripture, am not frightened at the things which are said to terrify us. For those who are greater than I have said, "We ought to obey God rather than men."

### syr.quote.warned-before-baptism

- World: Syriac Christianity (Edessa/Nisibis) (200–410)
- Source: Demonstration VII (On Penitents), sec. 20 (cic/texts/aphrahat_demonstrations-2-7_hallock1932.txt)

text:

> For this reason it is fitting for the sounders of trumpets, the preachers of the Church, to warn all (who are in) the covenant of God before baptism, and to those who choose for themselves virginity and holiness, young men and virgins and those (wishing to. become) holy; and for the preachers to warn them and say: "He who sets his heart upon the natural state of fellowship (i.e.~in matrimony), let him become united before baptism lest, perhaps, he fall in the conflict and be killed. And he who is afraid of this part of the struggle let him turn back lest, perhaps, he break the heart of his brethren as well as his own heart. And he who loves possessions let him turn back from the army lest, perhaps, when the battle shall prevail against him he should remember his possessions and turn back to them, for there is disgrace to him who turns back from the conflict".

### syr.quote.tatian-barbaric-writings

- World: Syriac Christianity (Edessa/Nisibis) (200–410)
- Source: ch. XXIX (anf02, line 6972)

text:

> Retiring by myself, I sought how I might be able to discover the truth. And, while I was giving my most earnest attention to the matter, I happened to meet with certain barbaric writings, too old to be compared with the opinions of the Greeks, and too divine to be compared with their errors; and I was led to put faith in these by the unpretending cast of the language, the inartificial character of the writers, the foreknowledge displayed of future events, the excellent quality of the precepts, and the declaration of the government of the universe as centred in one Being.

### alx.quote.the-grades-here-in-the-church

- World: Alexandrian Christianity (150–400)
- Source: Stromateis VI.13 (anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml)

text:

> Since, according to my opinion, the grades here in the Church, of bishops, presbyters, deacons, are imitations of the angelic glory, and of that economy which, the Scriptures say, awaits those who, following the footsteps of the apostles, have lived in perfection of righteousness according to the Gospel.

