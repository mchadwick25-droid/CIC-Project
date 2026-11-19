# Rendering Review: gallic quote records, batch 4 (26 records)

- **Reviewer:** Opus 5.5 (independent; did not draft or render any of these records)
- **Date:** 2026-11-03
- **Subject:** the `text` and `modern_rendering` of 26 `gallic.quote` records.

## Method

Each record's `text` is checked against the vendored edition at its locus. Two files are read: `cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml` (Sulpitius, Vincent, Cassian) and `cic/texts/salvian_on-the-government-of-god_sanford1930.txt` (Salvian, Sanford 1930). For the XML, `<note>…</note>` and all tags are stripped, entities decoded, line-end hyphens rejoined and whitespace (incl. U+00A0) folded. Each segment between "..." elisions is then searched for in order. For the Salvian OCR text, the matching spans are read line by line; the OCR footnote markers (`**`, `*®`, `”`) are footnote numbers, not words, and are disregarded. The span given is tight: the first line holding the quote's first word to the line holding its last word.

Each `modern_rendering` is read clause by clause against the edition text, and against `confidence.divergence_note` and `use_note.not_for`. Sentence lengths are counted by splitting at sentence-final punctuation and at elision marks, then counting space-separated words; the longest sentence per record is given.

## Results

**26 records: 25 PASS, 1 FAIL (1 P1, 0 P2).**

| Record id (gallic.quote.…) | Edition text at (file, lines) | Text check | Rendering check | Verdict |
|---|---|---|---|---|
| profane-notion-attribute-everything-to-free-will | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 38459-38464 | pass | all clauses; "according to the profane notion" kept as "would fit the profane notion"; desert as "what each person deserves"; longest 25 | PASS |
| readier-to-require-our-own-inventions | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 17092-17098 | pass | all clauses; "as we ought" kept; "professed ourselves disciples" as "formally bound ourselves as disciples"; longest 23 | PASS |
| receiving-christ-in-you | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 21017-21027 | pass | all clauses; free-will offering vs command kept; "children of the bridegroom" as "the bridegroom's friends" (the wedding-guest sense); longest 25 | PASS |
| roused-to-heavenly-warfare | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 594-598 | pass | all clauses; "I think" kept; warfare kept in the list of three; longest 25 | PASS |
| ruricius-and-the-vote-for-tours | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 1059-1083 | pass | all clauses; "pretending", "forsooth" ("if you please"), "they said" kept; "priest" rightly as "bishop"; longest 17 | PASS |
| salvian-ever-present-judgment-gallic-provinces | cic/texts/salvian_on-the-government-of-god_sanford1930.txt, lines 9144-9152 | pass | all clauses; elided verb "burst into flames" supplied for Aquitaine and the provinces, nothing new; longest 17 | PASS |
| salvian-free-men-in-seeming-captivity | cic/texts/salvian_on-the-government-of-god_sanford1930.txt, lines 6457-6459 | pass | whole antithesis kept; "liberty" as "freedom"; longest 18 | PASS |
| salvian-on-the-demand-for-circuses | cic/texts/salvian_on-the-government-of-god_sanford1930.txt, lines 8264-8306 | pass | all clauses; petitioners kept as "the few men of rank"; "Tréves" as "Trier"; longest 25 | PASS |
| salvian-on-the-unburied-dead | cic/texts/salvian_on-the-government-of-god_sanford1930.txt, lines 8241-8259 | pass | all clauses; "three times" kept; "a sight that I myself endured" kept first-person; longest 18 | PASS |
| salvian-on-treves-ruined-elite | cic/texts/salvian_on-the-government-of-god_sanford1930.txt, lines 8093-8127 | pass | all clauses; "I myself have seen" kept; "no less than four times" kept; longest 21 | PASS |
| salvian-present-judgment-clearly-shown | cic/texts/salvian_on-the-government-of-god_sanford1930.txt, lines 9009-9010 | pass | "present judgment" as "judgment here and now"; "in addition to his actual misfortune" kept; longest 11 | PASS |
| salvian-rich-murdering-the-poor | cic/texts/salvian_on-the-government-of-god_sanford1930.txt, lines 5063-5066 | pass | all clauses; "so-called remedies" kept; "general panacea" as "the cure meant for everyone"; longest 22 | PASS |
| secular-ruler-judge-in-ecclesiastical-cause | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 11655-11660 | pass | all clauses; indirect speech kept ("He held"); bishops' sentence kept; longest 23 | PASS |
| sulpitius-on-the-secular-judge-in-an-ecclesiastical-cause | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 11655-11660 | pass | all clauses; indirect speech kept ("he said", "he held"); "unheard-of" kept; longest 19 | PASS |
| sulpitius-weariness-of-the-present-world | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 2148-2154 | pass | all clauses; "as often happens" kept; remembrance of sins kept as consequence and as source; longest 18 | PASS |
| the-catechumens-testimony | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 1007-1025 | pass | all clauses; "virtues" rightly as "powers"; "deemed" as "thought"; longest 24 | PASS |
| the-cloak-divided-and-the-vision-of-christ | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 766-802 | pass | all clauses; "catechumen" as "candidate for baptism"; Matthew 25 citation kept; longest 24 | PASS |
| the-fathers-and-the-angels-twelve | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 17141-17232 | FAIL (case only: record "One rose up" after an elision; edition line 17197 has "one rose up") | all clauses across elisions; "understood ... through the angel's direction" kept as the fathers' reading; "of their own appointment" kept; longest 20 | PASS |
| the-psalm-that-answered-defensor | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 1088-1108 | pass | "It was believed" frame does not reach the closing "because" clause, which reads as fact; "Martin" added as object of the opposition | FAIL P1 |
| the-soldier-who-served-his-servant | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 728-740 | pass | all clauses; "changing places as it were" kept; "regarded ... as a monk" kept; longest 23 | PASS |
| three-lentils-and-the-lords-things | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 19227-19248 | pass | all clauses; "they believe", "they hold" frames kept; conditionals kept as "Suppose ..."; longest 25 | PASS |
| vincent-awful-expectation-of-judgment | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 12086-12092 | pass | all clauses; "a certain" kept; "especially since" as "all the more needed. For ..."; longest 17 | PASS |
| vincent-celestines-letter-and-its-reading | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 14615-14631 | pass | all clauses; "certain persons complain" kept inside the letter; double "if the case be so" kept; longest 23 | PASS |
| vincent-tempests-of-secular-warfare | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 12112-12120 | pass | all clauses; harbour and shipwreck imagery kept; "propitiating" as "seek God's favour"; longest 25 | PASS |
| weekly-service-and-sacred-vessels | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 19172-19200 | pass | all clauses; "all the East" kept as Cassian's own reach; "they believe" kept; longest 22 | PASS |
| without-grievous-blasphemy-all-men-to-be-saved | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 37756-37759 | pass | all clauses; "without grievous blasphemy" kept; "generally" carried as "all people in general"; longest 25 | PASS |

## Failed renderings: corrected text

### the-psalm-that-answered-defensor (FAIL P1)

In the edition, the closing clause ("because the praise of the Lord was perfected ... in the case of Martin, while the enemy was at the same time both pointed out and destroyed") sits inside the sentence governed by "It was believed". The rendering breaks it into two free-standing sentences ("For in Martin's case, the Lord's praise was perfected ... At the same time, the enemy was both pointed out and destroyed."), which read as Sulpitius's own assertion of fact. That loses the reported-belief frame the `divergence_note` and `use_note.not_for` require. The rendering also adds "Martin" as the object of Defensor's opposition, where the edition says only that he "specially offered opposition".

Corrected rendering:

> Among the bishops who were there, however, one named Defensor is said to have led the opposition. For this reason, people noticed that he was sharply rebuked at that time in the reading from the prophets. It so happened that the reader whose duty it was to read aloud that day was blocked by the crowd and did not appear. The officials were thrown into confusion as they waited for a man who never came. Then one of the bystanders grabbed the book of Psalms and seized on the first verse he came to. The Psalm went like this: "From the mouths of babies and infants you have perfected praise because of your enemies, to destroy the enemy and the avenger." When these words were read, the people raised a shout, and the opposing side was put to shame. People believed that God had ordained the choice of this Psalm, so that Defensor might hear a witness about his own work. As they believed, the Lord's praise was perfected out of the mouths of babies and infants in Martin's case. At the same time, they believed, the enemy was both pointed out and destroyed.
