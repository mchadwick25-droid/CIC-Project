# Short descriptions for the 12 built worlds: check

Card checker, 2026-11-26. I checked `Drafts.md` and `drafts.json` against the evidence each draft cites. For every card I opened the entry's `longDescription` in `cic-website/data/world-census.json` (cited below as "brief ¶n") and `orientation.story` in `cic-website/data/worlds/<id>.json` (cited as "story[n]"). For dates I also opened the world's core record in `records/`. Scores come from `engine.m1.gates.grade_text`.

The coordinator reads Mark's ruling as asking for one main idea. Where a draft carries two separate ideas, I say which one to keep and why, and the fix keeps only that one. Mark's own words allow "one or two sentence[s]", so this reading is listed for his ruling at the end.

---

## 1. `post-apostolic-house-church`: FIX

**Trust.** Every claim holds. Brief ¶2 gives "gave thanks over bread and a cup on the Lord's day" and "Letters and messengers carried between their churches held them together". Story[0] gives "Christians gathered in households". Pliny's hostile report is rightly left out.

**Dates `Late 1st-2nd c.`: holds.** The core record says "The year 70 marks the opening only loosely ... The c. 200 close is directional, not universal" (`records/pahc/world_core/pahc.core.house-church.md`, `horizon`). The brief dates only roughly: "In the hundred years after the apostles" (¶2), "Near the end of the first century" (¶4).

**Simplicity.** There is one idea: households held together. But "Letters and messengers carried between their churches" reads first as "messengers carried [something]". A listener in a second language will trip on it.

- Field `shortDescription`. Old: `Letters and messengers carried between their churches held them together.` New: `Letters and messengers passing between their churches held them together.` Evidence: brief ¶2, the same claim; story[0], "Letters and travelers kept them joined as one."

**Final:** Christians met in households and gave thanks over bread and a cup on the Lord's day. Letters and messengers passing between their churches held them together. (26 words; FK 6.7, FRE 70.0)

---

## 2. `alexandria-catechetical`: PASS

**Trust.** Brief ¶2: "Teachers took pagans and catechumens through Scripture, read for a deeper sense beneath the plain story." Brief ¶4: "Scripture, Origen wrote ... has a body, a soul and a spirit, as a person does." Both claims hold, and Origen's words are given as he wrote them.

**Dates `Late 2nd-4th c.`: holds.** 150 and 400 are the world's frame (`records/alx/world_core/alx.core.alexandria.md`, `time_window`). The brief's span is "From about 180 to the middle of the next century" (¶2). Story[3] has Clement teaching "from about 180", and story[8] has Didymus dying "about 398".

**Simplicity.** There is one idea, reading Scripture for its deeper sense, and the second sentence shows it.

**Final:** Teachers led learners through Scripture, reading for a deeper sense beneath the plain story. Origen wrote that Scripture, like a person, has a body, a soul and a spirit. (29 words; FK 7.2, FRE 69.6)

---

## 3. `syriac-edessa-nisibis`: FIX

**Trust.** "Each with a refrain" is said of all their hymns, which goes further than the source. Brief ¶5 and story[1] give the refrain to Ephrem's hymns ("Ephrem taught in hymns, each with a refrain"). Brief ¶2 says only that "they sang their teaching in hymns". The vow before baptism holds (brief ¶3).

**Dates `201-410 CE`: does not hold.** The flood record's own `use_note.not_for` bars "a claim that the date is certainly 201, as the edition's footnote computes 202". Its `telling` says "the year 513 of the Greeks, around the year 201", and its note calls it "an era-convention difference" (`records/syr/story/syr.story.edessa-flood-201.md`). Turning "513 of the Greeks" into 201 rather than 202 is an editor's reckoning, so the plain "201" claims more than the old source fixes. The world's own record and orientation give it roughly. The core record has "c. 200-410 CE" (`records/syr/world_core/*.md`, `horizon`) and its cautions say "Church life at Edessa is attested only from about 200". Story[0] has "From about 200 to 410 CE". 410 is fixed by the synod's acts (brief ¶9).

- Field `dates`. Old: `201-410 CE`. New: `c. 200–410 CE`. Evidence: the flood record's `not_for` and `telling` quoted above; the core record's `horizon`; story[0].

**Simplicity.** The draft has two ideas: hymns, and the covenant vow. Keep the hymns. The brief leads with them (¶2). The core record's `formation_logic` opens "Doctrine is taught by singing it". And sung teaching is what sets this world apart from the others on the tree, several of which also have vowed celibate lives.

- Field `shortDescription`. Old: `These Christians sang their teaching in hymns, each with a refrain that came back after every verse. Some men and women vowed before baptism to live unmarried and holy for God.` New: `These Christians sang their teaching in hymns. In Ephrem's hymns a refrain came back after every verse, so a congregation learned the faith by singing it.` Evidence: brief ¶2, "In the 300s they sang their teaching in hymns"; brief ¶5, "Ephrem taught in hymns, each with a refrain, a line that came back after every verse"; story[1], "Each had a refrain, so a congregation learned the faith by singing it."

**Final:** These Christians sang their teaching in hymns. In Ephrem's hymns a refrain came back after every verse, so a congregation learned the faith by singing it. (26 words; FK 6.7, FRE 70.0)

---

## 4. `desert-monasticism`: FIX

**Trust.** Sentence 1 holds. Story[0] gives "left their villages for the edge of the desert ... the fight was against demons, and the tempting thoughts they stirred", and brief ¶1 gives "the thoughts they whispered". The fight is told as their own purpose, so the demons are not stated as the narrator's fact. Sentence 2 turns a pattern into a single event. Brief ¶1 says teaching "passed mostly in a single exchange": it was a habit, not one monk on one day.

**Dates `4th-early 5th c.`: holds.** The brief says "By the early fourth century" (¶1) and "Around 320" (¶2). The latest dated events are January 399 (¶3, story[7]) and the council of 400 (story[8]). 430 is the world's frame (`records/desert/world_core/desert.core.desert.md`, `time_window`).

**Simplicity.** There are two ideas: withdrawal to fight, and teaching by "a word". Keep the withdrawal. It is the world's essence: the core record's `horizon` calls it "withdrawal as the whole work of formation", and story[0] says the same. The second sentence should deepen that idea rather than start a new one.

- Field `shortDescription`. Old: `A younger monk asked an elder for a word, and the elder answered in one sentence.` New: `They saw the leaving itself as the whole work of a Christian life.` Evidence: story[0], "These Christians saw the leaving itself as the whole work of a Christian life"; core record `horizon`.

If Mark would rather keep the "word" sentence, it needs this fix for the pattern: `A younger monk would ask an elder for a word, and the elder answered in one sentence.` Evidence: brief ¶1.

**Final:** These Christians left their villages for the desert, to fight demons and the tempting thoughts they whispered. They saw the leaving itself as the whole work of a Christian life. (30 words; FK 6.8, FRE 73.2)

---

## 5. `cappadocian-nicene-pastoral-monastic-tradition`: FIX

**Trust.** "Argued whether" is right, and it should stay. Story[6] says Basil "never plainly called the Spirit God", so "argued that" would go past the source. The Basil sentence holds (brief ¶2; story[2], story[3]), but it is a second, separate idea.

**Dates `4th c.`: holds.** The core record calls 394 "the softer, later evidentiary horizon" and 325 a frame (`records/cappadocian/world_core/cappadocian.core.cappadocian.md`, `horizon`). The brief gives the span only in words (¶1).

**Simplicity.** There are two ideas: the argument about God, and Basil's famine relief. Brief ¶1 joins them in one picture: these people argued the question "while running dioceses, burying relatives, and feeding the hungry through famine". The world's name, pastoral and monastic as well as Nicene, rests on that joining. Keep the argument, and let the second sentence show that the same people did both.

- Field `shortDescription`. Old: `Basil preached against grain hoarders in a famine, then built a poorhouse that nursed the sick.` New: `They did this while running churches and feeding the hungry through famine.` Evidence: brief ¶1, "while running dioceses, burying relatives, and feeding the hungry through famine".

**Final:** One family and its friends argued whether the Son and the Spirit are fully God, as the Father is. They did this while running churches and feeding the hungry through famine. (31 words; FK 7.2, FRE 71.0)

---

## 6. `imperial-juridical-christianity`: PASS

**Trust.** Brief ¶1 gives "an illegal association" and "hearing civil lawsuits ... traveling to councils at imperial expense". Brief ¶2 gives the refusal of the sacrament. "Repented" follows Ambrose's own letter (story[6]). Brief ¶2 tells the emperor's penance plainly, so "until he repented" stands on the brief.

**Dates `c. 312-451`: holds.** Both years are fixed (story[1], story[7]; `records/ijc/world_core/ijc.core.imperial-juridical.md`, `horizon`). The "c." understates dates that are fixed. That is a matter of form, not a breach of the date rule, and it is listed for Mark below.

**Simplicity.** Both sentences turn on one thing: bishops and emperors working out a new balance of power (story[0]). The second sentence is the sharpest case of it. It scores at the edge (FRE 61.1), but inside the limit.

**Final:** Bishops of a church once outlawed now judged lawsuits and went to councils the emperor paid for. One bishop would not give an emperor the sacrament until he repented of a massacre. (32 words; FK 8.7, FRE 61.1)

---

## 7. `hieronymian-ascetic-literary`: FIX

**Trust.** "He turned the Bible into Latin" goes past the source and misleads. The church already had a Latin Bible. Brief ¶2 says Jerome's was "rendered book by book from the Hebrew rather than the Greek everyone was used to". Story[4] says he turned "the Old Testament into Latin from the Hebrew". The rest holds. Story[1] gives the giving up of wealth and rank, story[0] the fasting, and brief ¶1 Jerome as their teacher. Story[4] gives Paula's fortune paying his Hebrew teachers, "By Jerome's account", and the whole record rests on Jerome (brief ¶3).

**Dates `c. 382–420 CE`: holds.** The arrival is Widely Accepted (`hal.force.jerome-arrival`, per `Build/Ministry/Features/Church-Family-Tree/World-Narration/hieronymian-ascetic-literary/story.sheet.md`). The death: "only the year 420 is widely accepted" (`records/hal/contested_claim/hal.contested.chronology.md`, `held_against`).

**Simplicity.** There is one idea, the circle's wealth and Jerome's scholarship bound together. The renunciation and the fortune paying for the work belong to the same story.

- Field `shortDescription`. Old: `as he turned the Bible into Latin.` New: `as he turned the Old Testament into Latin.` Evidence: story[4], "he spent years turning the Old Testament into Latin from the Hebrew, book by book"; brief ¶2.

**Final:** A circle of women gave up wealth and rank to fast and study Scripture, with Jerome as their teacher. Paula's fortune paid his Hebrew teachers as he turned the Old Testament into Latin. (33 words; FK 8.0, FRE 67.0)

---

## 8. `gallic-monastic-ascetic-christianity`: PASS

**Trust.** Brief ¶1 and story[1] give Martin's discharge and his seizure at Tours. Brief ¶1 says "kept the habits of a monk". Story[0] gives "monks after him did the same": "In both, a monk who was made a bishop went on living as a monk". The draft rightly avoids saying that Lérins followed Martin, since story[0] says no link between the two is shown.

**Dates `Mid-4th-mid-5th c.`: holds.** The brief's "About 360" (¶1) ties to Julian Caesar (story[1]). The close falls "in the years after the council at Ephesus, when Vincent had written his remembrancer" (`records/gallic/world_core/gallic.core.gallic.md`, `horizon`). The form "Mid-4th-mid-5th" is hard to read; see the form note below.

**Simplicity.** There is one idea, the monk who stays a monk as bishop.

**Final:** A soldier named Martin asked to leave the army to serve Christ. Seized and made a bishop, he kept living as a monk, and monks after him did the same. (30 words; FK 5.6, FRE 81.6)

---

## 9. `the-reformed-cities-zurich-and-geneva`: FIX

**Trust.** "Kept nothing it did not support" goes past the source. Story[0] says "a church has no standing to demand what Scripture does not support". That is a claim about what a church may demand, not about what it kept. The "it" is also unclear: it could mean Scripture or the city. The consistory sentence holds (brief ¶1; story[6]).

**Dates `From 1519`: holds under the date rule.** 1 January 1519 is fixed (story[1]). The core record says 1650 is the census's cap, with "no historical rupture" (`records/rzg/world_core/rzg.core.the-reformed-cities-zurich-and-geneva.md`). Whether it changes alone is for Mark (below).

**Simplicity.** The two sentences make one idea: a town's church rebuilt from Scripture, and what that church did about daily life, as brief ¶1 frames it.

- Field `shortDescription`. Old: `Two cities rebuilt their churches from Scripture, and kept nothing it did not support.` New: `Two cities rebuilt their churches from Scripture, and demanded nothing that Scripture did not support.` Evidence: story[0], "Both cities held that a church has no standing to demand what Scripture does not support."

**Final:** Two cities rebuilt their churches from Scripture, and demanded nothing that Scripture did not support. In one, pastors and lay elders met each week over neighbors' quarrels, absent husbands and missed church. (32 words; FK 8.7, FRE 61.1)

---

## 10. `donatism`: PASS

**Trust.** Brief ¶1 gives the accused bishop and "a tainted ordination gives nothing". Story[2] gives "anyone who crossed over from the rival church was washed again". The draft is told as what these Christians held, and it keeps their own refusal to call it a second baptism.

**Dates `c. 311-439 CE`: holds.** Brief ¶1 gives "311 or 312 ... neither can be ruled out", which the "c." carries. 439 is fixed (story[7]; `records/don/world_core/don.core.donatism.md`).

**Simplicity.** There is one idea, purity of the hand and what follows from it.

**Final:** These Christians held that a bishop who handed the Scriptures to persecutors could give nothing by his hand. Anyone who joined them from the rival church was washed again in baptism. (31 words; FK 8.0, FRE 65.6)

---

## 11. `lutheran-wittenberg-and-its-congregations`: FIX

**Trust.** Both draft sentences hold (story[1]; story[8], "at least once a week").

**Dates `1517-1580`: holds.** The letter of 31 October 1517 is fixed (brief ¶1, story[2]), and so is the Book of Concord of 1580 (story[11]; `records/witt/world_core/witt.core.witt.md`, `horizon`).

**Simplicity.** There are two ideas: the conscience comforted, and the household catechism. Keep the conscience. Story[1] names it as "the heart of this tradition", and the catechism is a means of carrying it. The draft's first sentence also stacks a clause inside a clause ("God's promise, taken in faith, comforts a conscience the commandments have frightened"). Splitting it gives the two sentences to the one idea.

- Field `shortDescription`. Old: `These Christians held that God's promise, taken in faith, comforts a conscience the commandments have frightened. Each week a father was to question his children and servants on the catechism.` New: `At the heart of this tradition sits a frightened conscience. The commandments frighten it, and God's promise, taken in faith, comforts it.` Evidence: story[1], "At the heart of this tradition sits a frightened conscience. The commandments teach a person to despair of his own powers, and then God's promise comforts him. A sinner is freely justified for Christ's sake, through faith."

**Final:** At the heart of this tradition sits a frightened conscience. The commandments frighten it, and God's promise, taken in faith, comforts it. (22 words; FK 6.4, FRE 68.8)

---

## 12. `latin-pastoral-congregational-christianity`: PASS

**Trust.** Brief ¶2: "lived as congregations around one bishop ... taught them, fed their poor ... judged their quarrels and decided with them whom to take back". The narrowing to the lapsed in persecution rests on brief ¶3 ("without your counsel and the people's consent"), brief ¶4 and story[4].

**Dates `Mid-3rd c.-430`: holds.** "C. 240s" rested on the record's "c. 246" (`records/lpc/world_core/lpc.core.latin-pastoral-congregational-christianity.md`, `horizon`), and no old source gives that year. The brief opens "From the 250s" (¶2), and Decius's persecution came in 250 (¶3). 430 is fixed by Possidius (story[13]).

**Simplicity.** There is one idea, a bishop and his own people.

**Final:** Each congregation gathered around one bishop, who taught them, fed their poor and judged their quarrels. With his people, he decided whom to take back after they gave way in persecution. (31 words; FK 8.3, FRE 62.8)

---

## American spelling, places and dates in the sentences

The spelling is American throughout ("neighbors"). No sentence carries a date. No sentence carries a place, with one possible exception: "the desert" in card 4, listed below.

## For Mark's ruling

1. **One idea or two.** Mark's words allow "one or two sentence[s]". The coordinator's reading of "one idea" is what drives the fixes to cards 3, 4, 5 and 11. If Mark accepts two ideas, cards 3, 5 and 11 can keep their drafts, with card 3's refrain still tied to Ephrem. Card 4 would keep its draft with the pattern fix given above.
2. **"The desert" in card 4.** It is the world's own image and part of its name, but the place line also says "Desert". I left it in. Removing it loses where they went.
3. **The 1650 census cap.** `From 1519` follows the date rule. But about twenty living entries of the same era end on the same cap, and changing one alone leaves the tree inconsistent. This is cross-world.
4. **Form of the dates line.** Three points of form, none of them a breach of the date rule:
   - Should a fixed range drop its "c."? This applies to card 6, `c. 312-451`, and on the same reasoning card 7, `c. 382–420 CE`, whose two years are both Widely Accepted.
   - "CE" appears on some lines and not others.
   - Hyphens and en dashes are mixed, which makes `Mid-4th-mid-5th c.` and `Mid-3rd c.-430` hard to read. `Mid-4th to mid-5th c.` and `Mid-3rd c.–430` would be clearer.
5. **Orientation text that conflicts with the new dates line.** The world pages' `orientation.story[0]` still opens on the modern frame years the new dates lines remove: "From about 70 to 200 CE" (pahc), "From about 150 to 400 CE" (alx), "Between about 320 and 430" (desert), "From about 325 to 394" (cappadocian), "between about 360 and 450 CE" (gallic), "between 1519 and 1650" (rzg), "from about 246 to 430" (lpc). A visitor would see one span on the card and another on the world page. That text is outside this batch.
