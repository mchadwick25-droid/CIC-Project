# Short descriptions for the 12 built worlds: check, round 2

Card checker, 2026-11-26. I checked `Drafts_v2.md` and `drafts_v2.json` against Mark's rulings of that day, Part 1 of the kit and the evidence. This is the one check of a one-round rewrite, so it gives exact fixes only. "Brief ¶n" is paragraph n of the entry's `longDescription` in `cic-website/data/world-census.json`. "Story[n]" is item n, from 0, of `orientation.story` in `cic-website/data/worlds/<id>.json`. I opened the evidence for every claim that is new since `Check.md`. Scores come from `engine.m1.gates.grade_text`. The draft's scores match mine.

The two drafts agree word for word. Every sentence is free of places and dates, every spelling is American, and the dates lines are unchanged from `final.json`.

---

## 1. `post-apostolic-house-church`: PASS

The fix changes only "Their" to "A bishop's" and "one another" to "a church". Everything else is Mark's wording.

- **"A bishop's":** Ignatius calls himself "the bishop of Syria" (Romans 2, `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml`, lines 6962 and 6976). Brief ¶5 gives "Ignatius, bishop of Antioch".
- **"greeted a church household by household":** this holds. Both held letters that greet households go to one church, Smyrna. Smyrnaeans 13 reads "I salute the families of my brethren, with their wives and children ... I salute the house of Tavias" (anf01, line 8503 onward). Polycarp 8 reads "the wife of Epitropus, with all her house and children" (line 8869). So the singular "a church" is exact, not loose.
- **"messengers carried them between the churches":** this holds. Polycarp 8 gives "sending messengers, and the others transmitting letters" (line 8856 onward). Story[3] gives "Polycarp sent the Philippians the letters of Ignatius that his church held". "Them" now points only to the letters.

The fix is the smallest true change. Scores: 30 words, FK 8.4, FRE 61.9.

## 2. `alexandria-catechetical`: PASS

This card is unchanged and passed in `Check.md`. It has no negative or contrast, and it opens on who they were.

## 3. `syriac-edessa-nisibis`: PASS

"Syriac-speaking Christians" stands on brief ¶2, "Those Christians spoke Syriac", and story[0], "Syriac-speaking Christians lived on the frontier". It names what they were at the time, and it holds no place. The rest passed in `Check.md`.

## 4. `desert-monasticism`: PASS

- **Rulings:** the card opens on Antony as he was when he left, a young landowner, and it does not call him a monk. It has no negative and no contrast.
- **Trust:** "A young landowner heard one Gospel reading" stands on brief ¶1. "Withdrew into the desert" also stands on brief ¶1. "Others left their villages too" stands on story[0], and it claims no link to Antony. The fight is told as their purpose, so the demons stay in the tradition's voice (story[0], "The tradition describes its own struggle"; brief ¶1).
- **"His land":** I weighed this against brief ¶1, "his family's land". Story[1] says his parents died before he gave the family land away, so the land was his inheritance, and "his land" is true. The exact phrase would push the card past a hard limit (FRE 58.4), so it stays as drafted.

Scores: 31 words, FK 8.3, FRE 62.8.

## 5. `cappadocian-nicene-pastoral-monastic-tradition`: PASS

"At the same time they ran churches and fed the hungry through famine" stands on brief ¶1, "while running dioceses, burying relatives, and feeding the hungry through famine". It has concrete verbs, no filler, and one idea per sentence.

## 6. `imperial-juridical-christianity`: PASS

- **"The newly favored church":** this is a time phrase, not a contrast, and nothing in it says what the church was before. It stands on brief ¶1, "first protected, then privileged", and story[3], "Imperial favor".
- **"Heard lawsuits and went to councils the emperor paid for":** brief ¶1.
- **"One bishop asked an emperor to repent of a massacre before he stood at the altar again":** this is story[6], nearly word for word. It follows Ambrose's own letter, and it rightly leaves off the public penance, which only later writers report. The refusal ("would not give") is gone, as the rulings require.

Scores: 33 words, FK 8.7, FRE 61.9.

## 7. `hieronymian-ascetic-literary`: PASS

This card is unchanged and passed in `Check.md`. "Gave up wealth and rank" tells something they did (story[1]). It is not a description of what they were not.

## 8. `gallic-monastic-ascetic-christianity`: PASS

This card is unchanged and passed in `Check.md`. It opens on Martin as he was at that moment, a soldier.

## 9. `the-reformed-cities-zurich-and-geneva`: PASS

- **The "demanded nothing" clause:** it is gone, as Mark ruled. "Two cities rebuilt their churches from Scripture" stands on brief ¶1.
- **"Absent husbands and missed church":** this does not break the no-negatives ruling. The ruling governs how a card describes its own subject, and here that subject is the pastors and elders. The sentence tells what they did, which was to meet each week over cases. The three cases are what the register records, given in its own words (brief ¶1, "quarrels between neighbors, absent husbands, people who had not been to church"). Rewording them positively would go past the register. "Deserting husbands", for example, makes a charge the brief does not make. No fix.

Scores: 24 words, FK 6.8, FRE 67.8.

## 10. `donatism`: FIX

**Rulings and trust.** "A rival church" describes them by opposition, defining them only against the other church. It also takes one side's view. In the world's own narration, "the rival church" is the other side: story[2] reads "anyone who crossed over from the rival church was washed again", and brief ¶3 reads "bishops met roughly two hundred and eighty-six from the rival church". So the card turns the narration's own word around, and a reader who goes from the card to the world page meets "rival church" naming the opposite church. That breaks the kit's rule never to carry one side's view forward. Story[0] gives the even-handed fact, "two rival churches stood side by side". Brief ¶1 gives "the larger of the two churches".

- Field: `shortDescription`.
- Old: `A rival church held that a sacrament depends on the purity of the hand that gives it.`
- New: `One of two churches side by side held that a sacrament depends on the purity of the hand that gives it.`
- Evidence: story[0], "From around 311, two rival churches stood side by side"; brief ¶1, "made Majorinus bishop beside him" and "the larger of the two churches". This is true from the first moment, and it avoids "Donatists", a name given later.

The second sentence stands. Story[2] reads "anyone who crossed over from the rival church was washed again", and "to it" now points to the first church named.

**Final:** One of two churches side by side held that a sacrament depends on the purity of the hand that gives it. Anyone who crossed over to it was washed again in baptism. (32 words; FK 7.2, FRE 71.6)

## 11. `lutheran-wittenberg-and-its-congregations`: FIX

**Trust.** The opening now passes the ruling. But the second sentence, "Then God's promise comforts the sinner through faith", stands outside "taught that". So the card states a teaching in the narrator's own voice, as fact. Story[1] can say it plainly because it speaks inside "this tradition". A two-sentence card cannot. Kit Part 1 (Rigor) calls a belief told as the narrator's fact one of the four faults.

- Field: `shortDescription`.
- Old: `Then God's promise comforts the sinner through faith.`
- New: `Then, they taught, God's promise comforts the sinner through faith.`
- Evidence: story[1], "The commandments teach a person to despair of his own powers, and then God's promise comforts him. A sinner is freely justified for Christ's sake, through faith."

**Final:** Luther and the movement around him taught that the commandments frighten the conscience. Then, they taught, God's promise comforts the sinner through faith. (23 words; FK 6.3, FRE 70.1)

## 12. `latin-pastoral-congregational-christianity`: PASS

This card is unchanged and passed in `Check.md`. "After they gave way in persecution" tells something they did (brief ¶4), not something they failed to do.

---

## Final sentences

| id | Verdict | Final |
|---|---|---|
| post-apostolic-house-church | PASS | Christians gathered on the Lord's day and gave thanks over bread and a cup. A bishop's letters greeted a church household by household, and messengers carried them between the churches. |
| alexandria-catechetical | PASS | Teachers led learners through Scripture, reading for a deeper sense beneath the plain story. Origen wrote that Scripture, like a person, has a body, a soul and a spirit. |
| syriac-edessa-nisibis | PASS | Syriac-speaking Christians sang their teaching in hymns. In Ephrem's hymns a refrain came back after every verse, so a congregation learned the faith by singing it. |
| desert-monasticism | PASS | A young landowner heard one Gospel reading, gave away his land and withdrew into the desert. Others left their villages too, to fight demons and the tempting thoughts that demons whispered. |
| cappadocian-nicene-pastoral-monastic-tradition | PASS | One family and its friends argued whether the Son and the Spirit are fully God, as the Father is. At the same time they ran churches and fed the hungry through famine. |
| imperial-juridical-christianity | PASS | Bishops of the newly favored church heard lawsuits and went to councils the emperor paid for. One bishop asked an emperor to repent of a massacre before he stood at the altar again. |
| hieronymian-ascetic-literary | PASS | A circle of women gave up wealth and rank to fast and study Scripture, with Jerome as their teacher. Paula's fortune paid his Hebrew teachers as he turned the Old Testament into Latin. |
| gallic-monastic-ascetic-christianity | PASS | A soldier named Martin asked to leave the army to serve Christ. Seized and made a bishop, he kept living as a monk, and monks after him did the same. |
| the-reformed-cities-zurich-and-geneva | PASS | Two cities rebuilt their churches from Scripture. In one, pastors and lay elders met each week over neighbors' quarrels, absent husbands and missed church. |
| donatism | FIX | One of two churches side by side held that a sacrament depends on the purity of the hand that gives it. Anyone who crossed over to it was washed again in baptism. |
| lutheran-wittenberg-and-its-congregations | FIX | Luther and the movement around him taught that the commandments frighten the conscience. Then, they taught, God's promise comforts the sinner through faith. |
| latin-pastoral-congregational-christianity | PASS | Each congregation gathered around one bishop, who taught them, fed their poor and judged their quarrels. With his people, he decided whom to take back after they gave way in persecution. |
