# Short descriptions for the 12 built worlds: drafts, round 2

Card writer, 2026-11-26. This round follows Mark's rulings of that day. Each card says what its people were and what they did. It has no negatives and no contrasts. It opens on who they were at the moment described, never on "These Christians", and never on a name they earned later. The dates lines are copied unchanged from `final.json`.

The evidence is the same as in the first round. "Brief ¶n" means paragraph n of the entry's `longDescription` in `cic-website/data/world-census.json`. "Story[n]" means item n, counting from 0, of `orientation.story` in `cic-website/data/worlds/<id>.json`. Held texts are cited by file and line. Scores come from `engine.m1.gates.grade_text`. Every card scores inside grade 10 and reading ease 60, and every sentence is under 20 words.

---

## 1. `post-apostolic-house-church`

> Christians gathered on the Lord's day and gave thanks over bread and a cup. A bishop's letters greeted a church household by household, and messengers carried them between the churches.

**Words:** 30 (14, 16). FK 8.4, FRE 61.9.

**Flag.** Mark's wording "Their letters greeted one another household by household" does not hold. In the held letters, one writer greets the households of a church: Ignatius, who calls himself "the bishop of Syria" (Romans 2, `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml`, line 6962). No held source shows churches' letters greeting one another household by household. The minimal fix changes two phrases: "Their letters" becomes "A bishop's letters", and "one another" becomes "a church". The rest is Mark's wording. With "a church" singular, "them" now points back to the letters.

| Claim | Evidence |
|---|---|
| gathered on the Lord's day | Didache 14, "every Lord's day do ye gather yourselves together, and break bread, and give thanksgiving" (`cic/texts/anf07_lactantius-apostolic-constitutions-didache-liturgies.xml`, around line 13089); brief ¶2 |
| gave thanks over bread and a cup | brief ¶2, "gave thanks over bread and a cup on the Lord's day"; story[4] |
| a bishop's letters greeted a church household by household | Ignatius to the Smyrnaeans 13, "I salute the families of my brethren, with their wives and children ... I salute the house of Tavias" (anf01, line 8503 onward); to Polycarp 8, "the wife of Epitropus, with all her house and children" (anf01, line 8869); Ignatius as "the bishop of Syria" (anf01, line 6962); brief ¶5, "He greeted households" |
| messengers carried them between the churches | to Polycarp 8, "write to the adjacent Churches ... such as are able to do so sending messengers, and the others transmitting letters through those persons who are sent by thee" (anf01, line 8856 onward); story[3]; brief ¶2 |

---

## 2. `alexandria-catechetical`

> Teachers led learners through Scripture, reading for a deeper sense beneath the plain story. Origen wrote that Scripture, like a person, has a body, a soul and a spirit.

**Words:** 29 (14, 15). FK 7.2, FRE 69.6. Unchanged from `final.json`: it has no negative or contrast, and it opens on who they were.

| Claim | Evidence |
|---|---|
| teachers led learners through Scripture, reading for a deeper sense beneath the plain story | brief ¶2, "Teachers took pagans and catechumens through Scripture, read for a deeper sense beneath the plain story" |
| Origen: Scripture, like a person, has a body, a soul and a spirit | brief ¶4, "Scripture, Origen wrote before he left the city, has a body, a soul and a spirit, as a person does"; story[2] |

---

## 3. `syriac-edessa-nisibis`

> Syriac-speaking Christians sang their teaching in hymns. In Ephrem's hymns a refrain came back after every verse, so a congregation learned the faith by singing it.

**Words:** 26 (7, 19). FK 7.6, FRE 64.7. The opening "These Christians" becomes "Syriac-speaking Christians". A language is who they were, not a place.

| Claim | Evidence |
|---|---|
| Syriac-speaking Christians | brief ¶2, "Those Christians spoke Syriac"; story[0], "Syriac-speaking Christians lived on the frontier" |
| sang their teaching in hymns | brief ¶2, "In the 300s they sang their teaching in hymns" |
| in Ephrem's hymns a refrain came back after every verse | brief ¶5, "Ephrem taught in hymns, each with a refrain, a line that came back after every verse" |
| so a congregation learned the faith by singing it | story[1], "Each had a refrain, so a congregation learned the faith by singing it" |

---

## 4. `desert-monasticism`

> A young landowner heard one Gospel reading, gave away his land and withdrew into the desert. Others left their villages too, to fight demons and the tempting thoughts that demons whispered.

**Words:** 31 (16, 15). FK 8.3, FRE 62.8. The card opens on Antony as he was when he left: a young landowner, not yet a monk. It gives him by role, since the card has no room to explain the name. The fight stays as their own purpose ("to fight"), so the demons stand in the tradition's voice, as in the first round.

| Claim | Evidence |
|---|---|
| a young landowner heard one Gospel reading | brief ¶1, "Antony, a young Egyptian landowner, gave away his family's land after hearing one Gospel reading in church"; story[1], "he heard the Gospel read in church as if it had been read for him" |
| gave away his land | brief ¶1, as above; story[1], "He gave the family land to the villagers, and then he gave away the rest" |
| withdrew into the desert | brief ¶1, "withdrew by stages: the village's edge, an abandoned fort, then the desert's inner reaches"; story[2], "a mountain in the inner desert" |
| others left their villages too | story[0], "Christians in Egypt left their villages for the edge of the desert" |
| to fight demons and the tempting thoughts that demons whispered | brief ¶1, "fought against demons and the thoughts they whispered, from within"; story[0], "the fight was against demons, and the tempting thoughts they stirred" |

**Note.** "Others left their villages too" says only that others left. It does not say they followed Antony, which no held line states. As in the first round, the card is told from Athanasius's account, which the brief and story[1] tell plainly; story[1] carries the doubt about its details for the fuller text.

---

## 5. `cappadocian-nicene-pastoral-monastic-tradition`

> One family and its friends argued whether the Son and the Spirit are fully God, as the Father is. At the same time they ran churches and fed the hungry through famine.

**Words:** 32 (19, 13). FK 6.1, FRE 79.6. The first sentence is unchanged. The second drops the filler "They did this while" for concrete verbs.

| Claim | Evidence |
|---|---|
| one family and its friends | brief ¶1, "one extended family and the friends around it" |
| argued whether the Son and the Spirit are fully God, as the Father is | brief ¶1, "whether the Son and the Spirit are God in the same sense the Father is"; story[1]. "Argued whether" stays, since story[6] says Basil "never plainly called the Spirit God" |
| at the same time they ran churches and fed the hungry through famine | brief ¶1, "while running dioceses, burying relatives, and feeding the hungry through famine" |

---

## 6. `imperial-juridical-christianity`

> Bishops of the newly favored church heard lawsuits and went to councils the emperor paid for. One bishop asked an emperor to repent of a massacre before he stood at the altar again.

**Words:** 33 (16, 17). FK 8.7, FRE 61.9. Two lines go. "A church once outlawed now" was a then-and-now contrast. "Would not give an emperor the sacrament until" was a refusal. Both sentences now say what the bishops did.

| Claim | Evidence |
|---|---|
| bishops of the newly favored church | brief ¶1, the church "became first protected, then privileged, then the empire's official religion"; story[3], "Imperial favor" |
| heard lawsuits and went to councils the emperor paid for | brief ¶1, "Bishops found themselves hearing civil lawsuits ... and traveling to councils at imperial expense" |
| one bishop asked an emperor to repent of a massacre before he stood at the altar again | story[6], "his soldiers killed a crowd in the circus with no trial ... He asked the emperor to repent before he stood at the altar again"; brief ¶2, "a massacre at Thessalonica" |

**Note.** "Asked ... to repent" follows Ambrose's own letter (story[6]). The public penance rests on Sozomen and Theodoret decades later, so it stays off the card.

---

## 7. `hieronymian-ascetic-literary`

> A circle of women gave up wealth and rank to fast and study Scripture, with Jerome as their teacher. Paula's fortune paid his Hebrew teachers as he turned the Old Testament into Latin.

**Words:** 33 (19, 14). FK 8.0, FRE 67.0. Unchanged from `final.json`. "Gave up wealth and rank" is an act they did, told as the source tells it.

| Claim | Evidence |
|---|---|
| a circle of women, with Jerome as their teacher | brief ¶1, "a circle of ascetic women, serious about Scripture ... All of them took Jerome as their teacher" |
| gave up wealth and rank | story[1], "The women of the circle gave up wealth, marriage prospects, and rank on purpose, as devotion to Christ" |
| to fast and study Scripture | story[0], "a place of fasting and scripture study" |
| Paula's fortune paid his Hebrew teachers | story[4], "By Jerome's account, Paula's fortune also paid for his Hebrew teachers" |
| he turned the Old Testament into Latin | story[4], "turning the Old Testament into Latin from the Hebrew, book by book"; brief ¶2 |

---

## 8. `gallic-monastic-ascetic-christianity`

> A soldier named Martin asked to leave the army to serve Christ. Seized and made a bishop, he kept living as a monk, and monks after him did the same.

**Words:** 30 (12, 18). FK 5.6, FRE 81.6. Unchanged from `final.json`. Martin is named as he was at the moment: a soldier.

| Claim | Evidence |
|---|---|
| a soldier named Martin asked to leave the army to serve Christ | brief ¶1, "a soldier named Martin ... asked to leave the army"; story[1], "he asked his commander, Julian Caesar, for his discharge, to serve Christ instead" |
| seized and made a bishop | brief ¶1, "the people of Tours seized him and made him their bishop" |
| he kept living as a monk | brief ¶1, "he kept the habits of a monk even in that office" |
| monks after him did the same | story[0], "In both, a monk who was made a bishop went on living as a monk"; brief ¶1, Honoratus of Lérins "became bishop of Arles" |

---

## 9. `the-reformed-cities-zurich-and-geneva`

> Two cities rebuilt their churches from Scripture. In one, pastors and lay elders met each week over neighbors' quarrels, absent husbands and missed church.

**Words:** 24 (7, 17). FK 6.8, FRE 67.8. "And demanded nothing that Scripture did not support" goes, as Mark ruled. The first sentence now says only what they did.

| Claim | Evidence |
|---|---|
| two cities rebuilt their churches from Scripture | brief ¶1, "worked out what a whole town would look like if its church were rebuilt from Scripture" |
| in one, pastors and lay elders met each week | brief ¶1, "a consistory that met every week" (Geneva); story[6], "a Consistory of pastors and lay elders" |
| over neighbors' quarrels, absent husbands and missed church | brief ¶1, the registers show "quarrels between neighbors, absent husbands, people who had not been to church" |

**For Mark.** "Absent husbands and missed church" are the cases the elders heard, not things the cities failed to do. I read them as outside the ruling. If Mark reads them as inside it, the second sentence could end "met each week over neighbors' quarrels and family troubles", but "family troubles" goes past the register's own words.

---

## 10. `donatism`

> A rival church held that a sacrament depends on the purity of the hand that gives it. Anyone who crossed over to it was washed again in baptism.

**Words:** 28 (17, 11). FK 7.1, FRE 68.7. "These Christians" becomes "A rival church", which is what they were from the first: a second church set up beside the first. The card does not call them Donatists, a name given later. "Could give nothing by his hand" is a negative, so the claim is now told as what they held a sacrament depends on.

| Claim | Evidence |
|---|---|
| a rival church | brief ¶1, "A rival party ... made Majorinus bishop beside him"; story[0], "two rival churches stood side by side"; story[4], "a full parallel church" |
| held that a sacrament depends on the purity of the hand that gives it | brief ¶1, "A sacrament's validity rises and falls on the giver's own unbroken purity ... washed again by a hand that can be trusted"; story[1], "what a minister did in that moment decided whether his hand could be trusted afterward" |
| anyone who crossed over to it was washed again in baptism | story[2], "anyone who crossed over from the rival church was washed again" |

**Note.** "Washed again in baptism" keeps the record's own words. Story[2] says they did not count it a second baptism, so the card does not say "baptized twice".

---

## 11. `lutheran-wittenberg-and-its-congregations`

> Luther and the movement around him taught that the commandments frighten the conscience. Then God's promise comforts the sinner through faith.

**Words:** 21 (13, 8). FK 6.5, FRE 67.3. "At the heart of this tradition sits" opened on an abstraction. The card now opens on the people who taught it.

| Claim | Evidence |
|---|---|
| Luther and the movement around him | brief ¶1, "Within a few years a movement had grown around him"; story[0], "Martin Luther taught there at the university" |
| taught that the commandments frighten the conscience | story[1], "At the heart of this tradition sits a frightened conscience. The commandments teach a person to despair of his own powers" |
| then God's promise comforts the sinner through faith | story[1], "and then God's promise comforts him. A sinner is freely justified for Christ's sake, through faith" |

---

## 12. `latin-pastoral-congregational-christianity`

> Each congregation gathered around one bishop, who taught them, fed their poor and judged their quarrels. With his people, he decided whom to take back after they gave way in persecution.

**Words:** 31 (16, 15). FK 8.3, FRE 62.8. Unchanged from `final.json`: it has no negative or contrast, and it opens on who they were.

| Claim | Evidence |
|---|---|
| each congregation gathered around one bishop | brief ¶2, "lived as congregations around one bishop" |
| who taught them, fed their poor and judged their quarrels | brief ¶2, "Their bishop taught them, fed their poor, bought back their captives, judged their quarrels" |
| with his people, he decided whom to take back | brief ¶2, "decided with them whom to take back after sin"; brief ¶3, Cyprian, "without your counsel and the people's consent" |
| after they gave way in persecution | brief ¶4, "Many had given way and sacrificed, and now these fallen Christians asked to come back" |

---

## Summary

| id | Words | FK | FRE | Changed |
|---|---|---|---|---|
| post-apostolic-house-church | 30 | 8.4 | 61.9 | minimal fix to Mark's wording |
| alexandria-catechetical | 29 | 7.2 | 69.6 | no |
| syriac-edessa-nisibis | 26 | 7.6 | 64.7 | opening |
| desert-monasticism | 31 | 8.3 | 62.8 | rewritten |
| cappadocian-nicene-pastoral-monastic-tradition | 32 | 6.1 | 79.6 | second sentence |
| imperial-juridical-christianity | 33 | 8.7 | 61.9 | contrast and refusal removed |
| hieronymian-ascetic-literary | 33 | 8.0 | 67.0 | no |
| gallic-monastic-ascetic-christianity | 30 | 5.6 | 81.6 | no |
| the-reformed-cities-zurich-and-geneva | 24 | 6.8 | 67.8 | negative removed |
| donatism | 28 | 7.1 | 68.7 | opening and negative |
| lutheran-wittenberg-and-its-congregations | 21 | 6.5 | 67.3 | opening |
| latin-pastoral-congregational-christianity | 31 | 8.3 | 62.8 | no |
