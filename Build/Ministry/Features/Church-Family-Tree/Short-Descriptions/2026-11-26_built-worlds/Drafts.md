# Short descriptions for the 12 built worlds: drafts

Card writer drafts, 2026-11-26, for Mark's ruling of that day ("a short one or two sentance description like the other cards, but the player stays on the page", simpler than the Montanism example). Each draft is written fresh from the entry's brief (`longDescription` in `cic-website/data/world-census.json`), the world's compiled orientation (`orientation.story` in `cic-website/data/worlds/<id>.json`) and, for the dates, the world's own core record in `records/` and the world-narration grounding sheets in `Build/Ministry/Features/Church-Family-Tree/World-Narration/<id>/story.sheet.md`. Nothing rests on the earlier `tile`, `teaser` or `why` alone.

Below, "brief ¶n" means paragraph n of the entry's `longDescription`, and "story[n]" means item n (counting from 0) of `orientation.story`. The scores come from the project's own scorer, `engine.m1.gates.grade_text`: FK is the Flesch-Kincaid grade and FRE is Flesch Reading Ease. Every draft is between 26 and 35 words, every sentence is under 20 words, and every score is inside grade 10 and FRE 60.

Proposed dates use the census's own short form ("2nd-6th c.", as `montanism-the-new-prophecy` holds it). `start` and `end` are not touched.

---

## 1. Post-Apostolic Household-Church Christianity (`post-apostolic-house-church`)

**Dates line now:** 70–200 CE · Antioch · Asia Minor and beyond
**Proposed:** Late 1st-2nd c.

**Why the change.** No old source sets either year. The world's core record says "The year 70 marks the opening only loosely: the lived transition out of the apostles' own generation firmed up gradually across c. 64-100 rather than at any single date. The c. 200 close is directional, not universal" (`records/pahc/world_core/pahc.core.house-church.md`, `horizon`). The brief itself dates only roughly: "In the hundred years after the apostles" (¶2), "Near the end of the first century" (¶4, Corinth), and "Near the end of the century" (¶8, the Easter quarrel in the second century). "Late 1st-2nd c." is as rough as those allow.

**Short description:**
> Christians met in households and gave thanks over bread and a cup on the Lord's day. Letters and messengers carried between their churches held them together.

| Claim | Evidence |
|---|---|
| Christians met in households | story[0]: "Christians gathered in households"; brief ¶2: "their letters greet one another household by household" |
| gave thanks over bread and a cup on the Lord's day | brief ¶2: "gave thanks over bread and a cup on the Lord's day" |
| letters and messengers held their churches together | brief ¶2: "Letters and messengers carried between their churches held them together"; story[3]: "Letters held these scattered households together" |

**Words:** 26 (16, 10). FK 6.7, FRE 70.0.

**Left out.** Pliny's report that they met before dawn and sang a hymn to Christ "as to a god" (brief ¶1) is the most vivid image, but it is a hostile governor's report of what lapsed Christians in one province told him. It could not be joined to the thanksgiving without merging two witnesses' scenes into one.

---

## 2. Alexandrian Catechetical / Christian-Platonist Tradition (`alexandria-catechetical`)

**Dates line now:** c. 150–400 CE · Alexandria · Egypt
**Proposed:** Late 2nd-4th c.

**Why the change.** 150 and 400 are the world's frame (`records/alx/world_core/alx.core.alexandria.md`, `time_window` 150 to 400), and no old source gives either year. The record notes the open question "150-400 evenly vs 'richest 180-260'". The brief's own span is "From about 180 to the middle of the next century" (¶2), resting on Eusebius. The latest figure is Didymus, who "died about 398, at eighty-five" (story[8]). "Late 2nd-4th c." is as rough as those allow.

**Short description:**
> Teachers led learners through Scripture, reading for a deeper sense beneath the plain story. Origen wrote that Scripture, like a person, has a body, a soul and a spirit.

| Claim | Evidence |
|---|---|
| teachers led learners through Scripture, reading for a deeper sense beneath the plain story | brief ¶2: "Teachers took pagans and catechumens through Scripture, read for a deeper sense beneath the plain story" |
| Origen: Scripture, like a person, has body, soul and spirit | brief ¶4: "Scripture, Origen wrote before he left the city, has a body, a soul and a spirit, as a person does"; story[2]: "Origen taught that Scripture, like a person, has body, soul and spirit" |

**Words:** 29 (14, 15). FK 7.2, FRE 69.6.

**Left out.** That Greek philosophy could serve Christ (the census `why`). Neither the brief nor the orientation says it in those terms.

---

## 3. Syriac Christianity (Edessa/Nisibis) (`syriac-edessa-nisibis`)

**Dates line now:** 200–410 CE · Edessa · Nisibis
**Proposed:** 201-410 CE

**Why the change.** The brief sets the span "from the flood to the year 410" (¶2). The old source fixes the flood: "In November 201 ... the river rose against Edessa" (¶1), from the Chronicle of Edessa's entry for the year 513 of the Greeks (`records/syr/story/syr.story.edessa-flood-201.md`, `sources` locus "the year-513 entry", rated Widely Accepted). The synod of 410 is dated by the bishops' own acts (brief ¶9). "200" is a rounding that no source gives. Only the church-destruction line in the Chronicle is disputed (story[0]), not the flood or its year.

**Short description:**
> These Christians sang their teaching in hymns, each with a refrain that came back after every verse. Some men and women vowed before baptism to live unmarried and holy for God.

| Claim | Evidence |
|---|---|
| sang their teaching in hymns | brief ¶2: "In the 300s they sang their teaching in hymns" |
| each with a refrain that came back after every verse | brief ¶5: "Ephrem taught in hymns, each with a refrain, a line that came back after every verse"; story[1]: "Each had a refrain, so a congregation learned the faith by singing it" |
| some men and women vowed before baptism to live unmarried and holy for God | brief ¶3: "Some men and women took a vow, before baptism, to live unmarried and holy for God" (Aphrahat) |

**Words:** 31 (17, 14). FK 7.2, FRE 71.0.

**Left out.** That the covenant members lived in town among their own families (story[4]). It is supported, but it would make a third idea.

---

## 4. Desert Monasticism (`desert-monasticism`)

**Dates line now:** c. 320–430 CE · Nile Valley & Desert · Egypt
**Proposed:** 4th-early 5th c.

**Why the change.** The brief opens "By the early fourth century" (¶1) and gives Pachomius's founding only as "Around 320" (¶2). No event in the brief or the orientation falls at 430. The latest dated events are Evagrius's death "in January 399" (¶3, story[7]) and the council of 400 (story[8]), with Cassian writing "decades later" (story[7]). 430 is the world's frame end (`records/desert/world_core/desert.core.desert.md`, `time_window`), not a source's year. "4th-early 5th c." is as rough as the sources allow.

**Short description:**
> These Christians left their villages for the desert, to fight demons and the tempting thoughts they whispered. A younger monk asked an elder for a word, and the elder answered in one sentence.

| Claim | Evidence |
|---|---|
| left their villages for the desert | story[0]: "Christians in Egypt left their villages for the edge of the desert" |
| to fight demons and the tempting thoughts they whispered | brief ¶1: "now fought against demons and the thoughts they whispered, from within"; story[0]: "the fight was against demons, and the tempting thoughts they stirred" |
| a younger monk asked an elder for a word; one sentence | brief ¶1: "a younger monk asked an elder for 'a word,' and the elder answered in one sentence, no more" |

**Words:** 33 (17, 16). FK 8.0, FRE 67.0.

**Note.** "The desert" is the world's own image, not a named place. If it counts as a place under the ruling, the first sentence could read "left their villages to fight demons..." instead.

**Left out.** Discernment, the skill of judging how much discipline one person could bear (brief ¶3). It is supported, but it would make a third idea.

---

## 5. Cappadocian Christianity (`cappadocian-nicene-pastoral-monastic-tradition`)

**Dates line now:** c. 325-394 CE · Cappadocia · Anatolia
**Proposed:** 4th c.

**Why the change.** 394 is a modern reckoning. The world's core record says the window "runs to c. 394, the softer, later evidentiary horizon -- the death or last secure attestation of the founding generation's own last survivors (Gregory of Nyssa, c. 394...)" (`records/cappadocian/world_core/cappadocian.core.cappadocian.md`, `horizon`). Its opening is "c. 325 as the empire-wide persecutions end and Nicaea frames the confession", which is a frame, not a founding. The brief dates its span only in words: "from the years after the last empire-wide persecutions to the death of the last of a remarkable generation" (¶1). "4th c." is as rough as those allow.

**Short description:**
> One family and its friends argued whether the Son and the Spirit are fully God, as the Father is. Basil preached against grain hoarders in a famine, then built a poorhouse that nursed the sick.

| Claim | Evidence |
|---|---|
| one family and its friends | brief ¶1: "one extended family and the friends around it" |
| argued whether the Son and the Spirit are God as the Father is | brief ¶1: "argued the hardest question of the century — whether the Son and the Spirit are God in the same sense the Father is"; story[1]: "the Son is fully what the Father is" |
| Basil preached against grain hoarders in a famine | brief ¶2: "Basil's own preaching indicted the region's grain-hoarders"; story[2]: "About 368, drought ... Basil, then a priest, preached against them" |
| then built a poorhouse that nursed the sick | brief ¶2: "After the famine of 368, he built a complex outside Caesarea with a hospital, a hostel, and a workhouse"; story[3]: "a poorhouse outside the city walls ... an infirmary ... and ascetics served there as nurses" |

**Words:** 35 (19, 16). FK 7.8, FRE 70.6.

**Left out.** That the hoarders opened their stores (brief ¶2, story[2]). It is supported, but no words were left. Macrina's household (brief ¶2) is left out for the same reason. Her inclusion under "one family" holds.

---

## 6. Imperial and Juridical Christianity (`imperial-juridical-christianity`)

**Dates line now:** c. 312-451 · Rome · Constantinople and beyond
**Proposed:** unchanged

**Why it holds.** Both ends are events the old sources fix: the battle at the Milvian Bridge in 312 (story[1], from Eusebius and Lactantius) and the Council of Chalcedon in 451 (brief ¶2, story[7], from its acts). The world's core record frames it on exactly these events (`records/ijc/world_core/ijc.core.imperial-juridical.md`, `horizon`). One small point for Mark: the "c." is not needed, since both years are fixed. This is a matter of form, not of the date rule.

**Short description:**
> Bishops of a church once outlawed now judged lawsuits and went to councils the emperor paid for. One bishop would not give an emperor the sacrament until he repented of a massacre.

| Claim | Evidence |
|---|---|
| a church once outlawed | brief ¶1: "For nearly three centuries the church had been an illegal association" |
| bishops judged lawsuits and went to councils the emperor paid for | brief ¶1: "Bishops found themselves hearing civil lawsuits ... and traveling to councils at imperial expense" |
| one bishop would not give an emperor the sacrament until he repented of a massacre | brief ¶2: "He refused the emperor the sacrament until he did public penance for a massacre at Thessalonica" (Ambrose); story[6]: "'I dare not offer the sacrifice if you intend to be present' ... He asked the emperor to repent before he stood at the altar again" |

**Words:** 32 (17, 15). FK 8.7, FRE 61.1.

**Note.** The second sentence says "repented", as Ambrose's letter asks, and not "did public penance". Story[6] gives the public penance as Sozomen and Theodoret's report decades later.

**Left out.** That the same refusal had shielded the men who burned the synagogue at Callinicum (brief ¶3, story[5]). It is the record's own counterweight, and it could not fit without a third idea. The card's fuller text carries it.

---

## 7. Hieronymian Ascetic-Literary Christianity (`hieronymian-ascetic-literary`)

**Dates line now:** c. 382–420 CE · Rome · Bethlehem
**Proposed:** unchanged

**Why it holds.** Jerome's arrival in Rome in 382 is rated Widely Accepted (`hal.force.jerome-arrival`, `Build/Ministry/Features/Church-Family-Tree/World-Narration/hieronymian-ascetic-literary/story.sheet.md`). The world's contested-dates record says of the close that "only the year 420 is widely accepted" for Jerome's death, with the day and Eustochium's year in dispute (`records/hal/contested_claim/hal.contested.chronology.md`, `held_against`). The "c." covers the brief's rougher "In the early 380s" (¶1).

**Short description:**
> A circle of women gave up wealth and rank to fast and study Scripture, with Jerome as their teacher. Paula's fortune paid his Hebrew teachers as he turned the Bible into Latin.

| Claim | Evidence |
|---|---|
| a circle of women, serious about Scripture, with Jerome as their teacher | brief ¶1: "a circle of ascetic women, serious about Scripture ... All of them took Jerome as their teacher" |
| gave up wealth and rank | story[1]: "The women of the circle gave up wealth, marriage prospects, and rank on purpose, as devotion to Christ" |
| to fast | story[0]: "Marcella had made her house on the Aventine hill a place of fasting and scripture study" |
| Paula's fortune paid his Hebrew teachers | story[4]: "By Jerome's account, Paula's fortune also paid for his Hebrew teachers" |
| he turned the Bible into Latin | brief ¶2: "a Latin Bible rendered book by book from the Hebrew"; story[4]: "he spent years turning the Old Testament into Latin from the Hebrew, book by book" |

**Words:** 32 (19, 13). FK 7.6, FRE 69.0.

**Note.** Like everything known of the circle, the claim about Paula's fortune rests on Jerome (brief ¶3). The card's fuller text names him as the one witness.

**Left out.** That none of the women's own writing survives (brief ¶3). It is the record's central limit, but a sentence that only says what is missing is barred by Part 1.

---

## 8. Gallic Monastic-Ascetic Christianity (`gallic-monastic-ascetic-christianity`)

**Dates line now:** c. 360-450 · Tours · Lérins and beyond
**Proposed:** Mid-4th-mid-5th c.

**Why the change.** Sulpitius gives no year for Martin's discharge, only that he asked it of Julian Caesar (story[1]). The brief's "About 360" (¶1) is as close as that allows. The close is the world's own frame: "It closes in the years after the council at Ephesus, when Vincent had written his remembrancer" (`records/gallic/world_core/gallic.core.gallic.md`, `horizon`). No source event falls at 450. "Mid-4th-mid-5th c." is as rough as the sources allow.

**Short description:**
> A soldier named Martin asked to leave the army to serve Christ. Seized and made a bishop, he kept living as a monk, and monks after him did the same.

| Claim | Evidence |
|---|---|
| a soldier named Martin asked to leave the army to serve Christ | brief ¶1: "a soldier named Martin ... told Caesar he was now a soldier of Christ, and asked to leave the army"; story[1]: "he asked his commander, Julian Caesar, for his discharge, to serve Christ instead" |
| seized and made a bishop | brief ¶1: "the people of Tours seized him and made him their bishop"; story[1]: "drew him out of his monastery by a trick and made him their bishop" |
| he kept living as a monk | brief ¶1: "he kept the habits of a monk even in that office" |
| monks after him did the same | story[0]: "In both, a monk who was made a bishop went on living as a monk"; story[1]: "many of the monks he trained were later made bishops"; brief ¶1: Honoratus of Lérins "became bishop of Arles", Faustus "bishop of Riez" |

**Words:** 30 (12, 18). FK 5.6, FRE 81.6.

**Note.** "Monks after him" means later in time, not his disciples only. Story[0] says no evidence shows that Tours and Lérins ever wrote to each other, so the draft does not say that the Lérins monks followed Martin.

**Left out.** Cassian bringing Egypt's customs to Gaul (brief ¶1, story[3]), and the quarrel over grace and effort (brief ¶1, story[6]). Both are supported, but they would make a third and fourth idea.

---

## 9. The Reformed Cities - Zurich & Geneva (`the-reformed-cities-zurich-and-geneva`)

**Dates line now:** 1519-1650 · Swiss lands and beyond
**Proposed:** From 1519

**Why the change.** 1519 is fixed: Zwingli began on 1 January 1519 (story[1]). 1650 is not a historical date. The world's core record says "The window closes at 1650. The census set that date as its [cap] ... no historical rupture. The Reformed pattern this world rebuilds goes on unbroken past 1650" (`records/rzg/world_core/rzg.core.the-reformed-cities-zurich-and-geneva.md`, `horizon`). The entry's own `tile` says the same. Showing "1650" as an end tells a visitor something no source holds.

**For Mark (cross-world).** About twenty other living entries of the same era end on the same census cap (for example `the-anabaptist-movements` "1525-1650", `the-tridentine-church` "1517-1650", `the-society-of-jesus` "1540-1650"). Whether they all change is a cross-world decision and is not proposed here.

**Short description:**
> Two cities rebuilt their churches from Scripture, and kept nothing it did not support. In one, pastors and lay elders met each week over neighbors' quarrels, absent husbands and missed church.

| Claim | Evidence |
|---|---|
| two cities rebuilt their churches from Scripture | brief ¶1: "worked out what a whole town would look like if its church were rebuilt from Scripture" |
| kept nothing it did not support | story[0]: "Both cities held that a church has no standing to demand what Scripture does not support" |
| in one, pastors and lay elders met each week | brief ¶1: "a consistory that met every week" (Geneva); story[6]: "a Consistory of pastors and lay elders" |
| over neighbors' quarrels, absent husbands and missed church | brief ¶1: the registers show "quarrels between neighbors, absent husbands, people who had not been to church" |

**Words:** 31 (14, 17). FK 7.6, FRE 68.3.

**Left out.** The Zurich Disputation of 1523, with six hundred people in the Town Hall (story[2]). It is supported, but it would make a third idea.

---

## 10. Donatism (`donatism`)

**Dates line now:** c. 311-439 CE · Roman North Africa
**Proposed:** unchanged

**Why it holds.** "Caecilian was elected bishop of Carthage in 311 or 312. The sources support both years, and neither can be ruled out" (brief ¶1). The "c." carries that. The world closes "in 439, when a Vandal army took Carthage" (story[7]), an event the old sources fix. The core record frames the window on these two points (`records/don/world_core/don.core.donatism.md`, `time_window` and `horizon`).

**Short description:**
> These Christians held that a bishop who handed the Scriptures to persecutors could give nothing by his hand. Anyone who joined them from the rival church was washed again in baptism.

| Claim | Evidence |
|---|---|
| a bishop who handed the Scriptures to persecutors | brief ¶1: "Felix was accused of handing over the Scriptures to be burned in the recent persecution ... a bishop ordained by the hand of such a traditor"; story[1] |
| could give nothing by his hand | brief ¶1: "So a tainted ordination gives nothing"; glossary entry `don.term.traditor-traditio` (`narrative.glossary` in `cic-website/data/worlds/donatism.json`): "his hand was no longer clean, and ... he could not ordain, baptize, or bless" |
| anyone who joined from the rival church was washed again | story[2]: "anyone who crossed over from the rival church was washed again"; brief ¶1: "everyone it touches must be washed again by a hand that can be trusted" |

**Words:** 31 (18, 13). FK 8.0, FRE 65.6.

**Note.** "Washed again in baptism" follows the record's own words. Story[2] says the Donatists "did not count it as a second baptism", so the draft does not say "baptized twice".

**Left out.** That nearly everything known of them comes from their opponents (brief ¶2, story[8]). It belongs to the fuller text.

---

## 11. Lutheran Wittenberg & Its Congregations (`lutheran-wittenberg-and-its-congregations`)

**Dates line now:** 1517-1580 · Saxony and beyond
**Proposed:** unchanged

**Why it holds.** Both ends are documents the old sources date. Luther wrote to the archbishop "on 31 October 1517" (brief ¶1, story[2]), and the Book of Concord was gathered in 1580 (brief ¶1, story[11]). The core record calls the window "1517-1580, on the strength of the Book of Concord's 1580 gathering of documents already in hand -- Doc_01 SS2.2, Documented" (`records/witt/world_core/witt.core.witt.md`).

**Short description:**
> These Christians held that God's promise, taken in faith, comforts a conscience the commandments have frightened. Each week a father was to question his children and servants on the catechism.

| Claim | Evidence |
|---|---|
| the commandments frighten a conscience; God's promise comforts it | story[1]: "At the heart of this tradition sits a frightened conscience. The commandments teach a person to despair of his own powers, and then God's promise comforts him" |
| taken in faith | story[1]: "A sinner is freely justified for Christ's sake, through faith. The sacraments carry that promise" |
| each week a father was to question his children and servants on the catechism | story[8]: "A father was to question his children and servants at least once a week"; brief ¶1: a catechism put "into ordinary German households" |

**Words:** 30 (16, 14). FK 8.0, FRE 64.7.

**Left out.** German hymns sung inside the Mass (story[7]). It is supported, but it would make a third idea.

---

## 12. Latin Pastoral-Congregational Christianity (`latin-pastoral-congregational-christianity`)

**Dates line now:** c. 240s-430 · Carthage · Hippo Regius
**Proposed:** Mid-3rd c.-430

**Why the change.** "c. 240s" rests on a modern year. The orientation's "from about 246" (story[0]) is the core record's date for Cyprian's conversion, "c. 246-249" (`records/lpc/world_core/lpc.core.latin-pastoral-congregational-christianity.md`, `horizon`), and no old source gives it. The brief says "From the 250s to 430" (¶2). Its first dated event is Decius's persecution in 250 (¶3), but Cyprian was already bishop then, "Within two or three years" of his conversion (story[2]). "Mid-3rd c." covers both without a modern year. 430 is fixed: Augustine died on 28 August 430, during the siege, as Possidius tells it (story[13]).

**Short description:**
> Each congregation gathered around one bishop, who taught them, fed their poor and judged their quarrels. With his people, he decided whom to take back after they gave way in persecution.

| Claim | Evidence |
|---|---|
| each congregation gathered around one bishop | brief ¶2: "lived as congregations around one bishop"; story[1]: "a bishop was given a particular people, in one place, and he answered for them" |
| who taught them, fed their poor and judged their quarrels | brief ¶2: "Their bishop taught them, fed their poor, bought back their captives, judged their quarrels" |
| with his people, he decided whom to take back | brief ¶2: "decided with them whom to take back after sin"; brief ¶3: Cyprian, "without your counsel and the people's consent"; story[4]: "the same people who saw the fall received the person home, in the open" |
| after they gave way in persecution | brief ¶4: "Many had given way and sacrificed, and now these fallen Christians asked to come back" |

**Words:** 31 (16, 15). FK 8.3, FRE 62.8.

**Left out.** Cyprian's word in the plague that caring only for their own was nothing great (brief ¶5, story[5]). It is the most vivid line, but it would make a third idea. Note that this entry has no `entry` block (`entry` is null), so it has no earlier `tile` to compare against.

---

## Summary

| id | Words | FK | FRE | Dates |
|---|---|---|---|---|
| post-apostolic-house-church | 26 | 6.7 | 70.0 | 70–200 CE → Late 1st-2nd c. |
| alexandria-catechetical | 29 | 7.2 | 69.6 | c. 150–400 CE → Late 2nd-4th c. |
| syriac-edessa-nisibis | 31 | 7.2 | 71.0 | 200–410 CE → 201-410 CE |
| desert-monasticism | 33 | 8.0 | 67.0 | c. 320–430 CE → 4th-early 5th c. |
| cappadocian-nicene-pastoral-monastic-tradition | 35 | 7.8 | 70.6 | c. 325-394 CE → 4th c. |
| imperial-juridical-christianity | 32 | 8.7 | 61.1 | holds |
| hieronymian-ascetic-literary | 32 | 7.6 | 69.0 | holds |
| gallic-monastic-ascetic-christianity | 30 | 5.6 | 81.6 | c. 360-450 → Mid-4th-mid-5th c. |
| the-reformed-cities-zurich-and-geneva | 31 | 7.6 | 68.3 | 1519-1650 → From 1519 |
| donatism | 31 | 8.0 | 65.6 | holds |
| lutheran-wittenberg-and-its-congregations | 30 | 8.0 | 64.7 | holds |
| latin-pastoral-congregational-christianity | 31 | 8.3 | 62.8 | c. 240s-430 → Mid-3rd c.-430 |
