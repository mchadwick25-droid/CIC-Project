# Rendering Review: desert quote records, batch 2 (20 records)

- **Reviewer:** Opus 5.5 (independent; did not draft or render any of these records)
- **Date:** 2026-11-03
- **Subject:** the `text` and `modern_rendering` of 20 `desert.quote` records.

## Method

Each record's `text` is checked against the vendored edition in `cic/texts/` at the record's locus. Where the locus gives no file or line, the passage is found by searching a distinctive phrase in the file for that work. The check strips `<note>…</note>` and other tags in the XML editions, rejoins line-end hyphens, folds whitespace (including U+00A0) and quotation-mark glyphs, and treats "..." as an elision. A script does the matching, and every span is then read by eye. Printed page markers inside a quote ("[p. 687]", "|113") are treated as apparatus, not text.

Each `modern_rendering` is read clause by clause against the edition text, not against the record's `text` alone. Sentence length is a hand count of words between sentence-ending marks; a colon that opens quoted speech does not end a sentence. Each rendering is also read against its record's `confidence.divergence_note` and `use_note.not_for`.

Sources read: `npnf211_sulpitius-severus-vincent-lerins-cassian.xml`, `npnf204_athanasius-select-works-letters.xml`, `anf09_gospel-of-peter-diatessaron-origen-commentaries.xml`, `macarius_fifty-spiritual-homilies_mason1921.txt`, `palladius_paradise-v1-syriac_budge1907.txt`, `anan-isho_paradise-v2-sayings_budge1907.txt`, `pachomius_rules-ethiopic_schodde1885.txt`, `palladius_lausiac-history_clarke1918.txt`, `origen_philocalia_lewis1911.txt`.

## Results

**20 records: 14 PASS, 6 FAIL (1 P1, 5 P2).**

| Record id (desert.quote.…) | Edition text at (file, lines) | Text check | Rendering check | Verdict |
|---|---|---|---|---|
| he-puts-into-us-the-beginnings | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 38582-38586 | pass | all three "now" clauses kept; "men" to "people" sound; longest 25 | PASS |
| in-real-experience-and-feeling | cic/texts/macarius_fifty-spiritual-homilies_mason1921.txt, lines 2336-2343 | pass | "Then, in real experience…" runs 29 words and joins two thoughts; "even" tying the Spirit to the riches is lost | FAIL P2 |
| ladder-from-compunction | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 20064-20073 | pass | all nine steps kept; bare "compunction" carries the modern sense of a twinge of guilt, which `not_for` rules out | FAIL P2 |
| melania-to-the-governor | cic/texts/palladius_paradise-v1-syriac_budge1907.txt, line 1151 | pass | Budge's bracketed supplement "[and the wife of such and such a man]" is given unbracketed as her own words | FAIL P1 |
| monks-like-hyenas | cic/texts/pachomius_rules-ethiopic_schodde1885.txt, lines 224-228 (page marker "[p. 687]" at 226) | pass | "in name only" renders "as far as their names are concerned"; all clauses; longest 23 | PASS |
| moses-sins-run-out | cic/texts/anan-isho_paradise-v2-sayings_budge1907.txt, line 1160 | pass | Budge's bracket "[The sands are]" kept; "I, even I" kept; all clauses | PASS |
| never-held-communion-with-the-schismatics | cic/texts/npnf204_athanasius-select-works-letters.xml, lines 32908-32914 | pass | the advice exception kept; "intercourse" made "contact"; longest 24 | PASS |
| never-kneel-saturday-to-sunday | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 17735-17743 | pass | all clauses; "Whitsuntide" made "Pentecost"; Egyptians kept as subject | PASS |
| no-one-seize-the-hand | cic/texts/pachomius_rules-ethiopic_schodde1885.txt, line 200 | pass | all five prohibitions; stops before "there shall be distance" as the record says | PASS |
| origen-on-the-sinning-brother | cic/texts/anf09_gospel-of-peter-diatessaron-origen-commentaries.xml, lines 36234-36239 | pass | hedges "would seem" and "I do not think" kept; every listed sin kept | PASS |
| origen-to-gregory-handmaidens | cic/texts/origen_philocalia_lewis1911.txt, line 149 | pass | handmaid analogy kept whole; all subjects named; longest 21 | PASS |
| pachomian-rule-opening-superscription | cic/texts/pachomius_rules-ethiopic_schodde1885.txt, line 168 | pass | "ordinance… commanded" made "rule… gave… as a command"; nothing added | PASS |
| pachomius-angel-tablet | cic/texts/palladius_lausiac-history_clarke1918.txt, line 401 (ch. XXXII; page marker "\|113" inside) | pass | all three commands kept; elision kept | PASS |
| piamon-judge-of-the-earth | cic/texts/palladius_paradise-v1-syriac_budge1907.txt, line 1125 | pass | "Instead she climbed…unjust." runs 34 words across narration and prayer; "where they stand" adds to "wherein they are" | FAIL P2 |
| rule-for-the-weak | cic/texts/pachomius_rules-ethiopic_schodde1885.txt, line 176 | pass | angel's answer left unquoted as the scan has it; all clauses; longest 20 | PASS |
| sarah-man-among-you | cic/texts/anan-isho_paradise-v2-sayings_budge1907.txt, line 2438 | pass | exact; "brethren" made "brothers" | PASS |
| sin-and-grace-in-one-soul | cic/texts/macarius_fifty-spiritual-homilies_mason1921.txt, lines 7716-7723 | pass | question recast in three short sentences with nothing lost; "hate it, is" spelled out | PASS |
| so-perfectly-silent | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 17397-17409 | pass | second sentence runs 35 words; Cassian's present-tense report of a standing custom shifted to past narrative | FAIL P2 |
| talida-key-never-taken | cic/texts/palladius_paradise-v1-syriac_budge1907.txt, line 1129 | pass | "This old woman reached… shoulders" runs 32 words; otherwise all clauses, key custom read as in `not_for` | FAIL P2 |
| taor-not-compelled-to-market | cic/texts/palladius_paradise-v1-syriac_budge1907.txt, line 1133 | pass | both clauses; "[them]" is a grammatical supplement and needs no bracket in modern English | PASS |

## Failed renderings: corrected text

### in-real-experience-and-feeling (FAIL P2)

The second sentence runs 29 words and joins the seeing to a dash-apposition list. After the elision, the edition's "even the Spirit of the Lord" names what those riches are; the rendering turns it into a separate claim and loses that link.

Corrected rendering:

> Only let a person strive to be God's friend, and to be pleasing to him. Then, in real experience and feeling, that person will truly see the good things of heaven. They will see the delights too great for words, and the infinite riches of the Godhead. ... These are the Spirit of the Lord himself. For worthy souls, he makes himself their rest, their rejoicing, their delight, and their eternal life.

### ladder-from-compunction (FAIL P2)

Bare "compunction" now reads as a slight feeling of guilt, which is the sense the record's `not_for` excludes. "Salutary" is also better as "saving" than "healing", since the chain is about salvation.

Corrected rendering:

> According to Scripture, "the beginning" of our salvation and "of wisdom" is "the fear of the Lord." ... From the fear of the Lord comes saving compunction, a sorrow that pierces the heart. From this compunction of heart springs renunciation -- that is, owning nothing, and holding all possessions in contempt. From owning nothing, humility is born. From humility comes the putting to death of desires. Through the putting to death of desires, all faults are uprooted and wither away. By driving out faults, the virtues sprout up and grow. By the budding of the virtues, purity of heart is gained. By purity of heart, the perfection of apostolic love is won.

### melania-to-the-governor (FAIL P1)

In the edition, "[and the wife of such and such a man]" is Budge's bracketed supplement. The rendering drops the brackets and so gives an editor's clause to Melania as her own words, about a woman Palladius says was a widow. The bracket must stay, as the Moses record keeps its own.

Corrected rendering:

> I am the daughter of such-and-such a man, [and the wife of such-and-such a man], and I am the handmaid of Christ. Do not treat my poor clothing and condition lightly. For I have the power to raise myself up, if it pleases me to do so. And you have no authority either to hinder me like this, or to carry off any of my property.

### piamon-judge-of-the-earth (FAIL P2)

The sentence from "Instead she climbed" to the end of the prayer's first line runs 34 words and joins her night of prayer to the prayer itself. "Where they stand" adds a sense that "the spot wherein they are" does not carry. Budge's "[the enemy]" is a supplement and keeps its brackets, and "handmaiden" keeps her self-naming as a woman.

Corrected rendering:

> The elders of the village were afraid. They fell at her feet and begged her: 'We do not dare go out to meet them. We know how wretched and arrogant they are. But if you want to spare the village and your own house, go out and meet them yourself.' The virgin would not go out. Instead she climbed to the roof and stood there in prayer the whole night, never once kneeling down. She bowed and pleaded with God, saying: 'Lord, Judge of the earth, you take no pleasure in anything unjust. My Lord, when the prayer and pleading of your handmaid reach you, let your power pin [the enemy] to the spot where they are'...

### so-perfectly-silent (FAIL P2)

The second sentence runs 35 words. Cassian reports a standing custom in the present tense ("they meet", "they term", "there is no spitting"); the rendering turns it into past narrative of one occasion.

Corrected rendering:

> When they meet to celebrate these rites, which they call synaxes, a great number of the brethren gather together. Yet they are all so perfectly silent that you would not think anyone was there. The only exception is the one who stands up and chants the psalm in the midst. This is true most of all when the prayer is offered. Then there is no spitting, no clearing of the throat, and no noise of coughing. There is no sleepy yawning with open mouths and gaping. No groans or sighs are uttered that might distract those standing near.

### talida-key-never-taken (FAIL P2)

The sentence "This old woman reached such a state of dispassion that when I came… on my shoulders" runs 32 words. The rest of the rendering meets the bar.

Corrected rendering:

> Sixty virgins lived with her, following the path and rule of the ascetic life in purity. They lived a happy life under the teaching of this good old woman, whom they loved and depended on. They poured out such great affection on her that the key was never taken away from any one of them. This was unlike the custom in other religious houses for women. Through her divine teaching, she changed them into a state of incorruption. This old woman reached such a state of dispassion that she did this. When I came into her presence and sat down beside her, she stretched out her hands and laid them on my shoulders. She acted with the boldness and freedom she had gained in Christ.
