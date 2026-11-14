# R2 recheck: era 4 batch 6

Round 2, a targeted recheck of the round 1 changes, by two fresh Opus agents that had not seen the drafting or round 1, at full effort. Part 1 covers Agathon, John III, Isaac and Simon I. Part 2 covers Alexander II, Michael I, Joseph I, Severus ibn al-Muqaffa and the README. Each part is given as its reviewer wrote it.

## Era 4 Who batch 6, round 2 review: PART 1

**Scope.** agathon-of-alexandria, john-iii-of-samannud, isaac-of-alexandria, simon-i-of-alexandria: brief, card, audio script, records.json entries. Round 1 findings A-B1, A-B2, A-M1 to A-M33.

**Method.** Targeted recheck, as the brief sets. I read CLAUDE.md, Who_Profile_Pattern.md (14-point checklist), R1_review.md (Part A) and R1_changes.md, and ran `git diff --word-diff ed936fc6 d70de91c` on the four profiles and records.json. For each changed string I reopened the cited lines in cic/texts/ and read them in context. Quotations in changed strings were checked word for word. Audio scripts were diffed against the briefs once `[calmly] ` and `[warmly] ` were removed. Briefs were rescored with `grade_text`. Sentence lengths were checked by script across briefs and cards. Every replacement wording below was rescored where it touches a brief.

**Files opened (cic/texts/).** PO5 = chronicle-of-seert_..._scher-dib1910.txt (Evetts's History, PO 5). SEV = severus-al-muqaffa_..._evetts1904.txt. REN = renaudot_..._1713.txt. BAS1 = synaxaire-arabe-jacobite_po1-.... PO11 = synaxaire-arabe-jacobite_po11-... (Porcher's Mina). PO17 = john-ephesus_lives-eastern-saints-po17_brooks1923.txt (Basset, 24 Abib, bound in). BUD1 = ethiopian-synaxarium_...-v1-.... BUDM = ethiopian-synaxarium_...-v2-v4-microform_.... ABU = abu-salih_....

**Audio.** All four scripts equal their briefs once the two tags are removed. `[calmly]` is on line 1 and `[warmly]` starts the last paragraph in each. Checklist 13 passes.

---

### agathon-of-alexandria

**Verdict: one blocking finding (R2-1-B1). Otherwise sound.**

| R1 finding | Status | Note |
|---|---|---|
| A-M1 | APPLIED | "Early in the account, Agathon writes:" fixes the antecedent, but now settles authorship in the narrator's voice. See R2-1-B1. |
| A-M2 | APPLIED | Brief, two sentences. REN l.18609-18612 ("ab Patriarchis hæreticis ... Ita ab Alexandrinis Patriar[chis]") supports "calls their line heretical". The card is not changed. See R2-1-M2. |
| A-M3 | APPLIED | PO5 l.346-347 "the impure Chalcedonian Council". |
| A-M4 | APPLIED | PO5 l.451-453. |
| A-M5 | APPLIED | SEV l.45705-45707 "that the heretics might not hinder him ... entering the houses or lodgings of the orthodox". |
| A-M6 | APPLIED | BUD1 l.13571-13572 "fully nineteen years". |
| A-M7 | APPLIED | PO5 l.642-645. |
| A-M8 | APPLIED | Reworded in place. See R2-1-M1 on "the church". |
| A-M9 | APPLIED | |
| A-M10 | APPLIED | ABU l.11311-11335. "Sent by the governor" rests on l.11311 "wished to cut it down" and l.11335 "never again gave orders that the tree should be cut down". Supported. |
| A-M11 | APPLIED | PO5 l.411, 441-442. |
| A-M31, A-M32, A-M33 | APPLIED | Retag, REN l.986 claim and fleet contested claim are in records. The fleet line PO5 l.495 is right. |

Cuts made for length (the vision naming John, the fleet sentence) leave nothing dangling in the brief. John of Samannud is not mentioned elsewhere in it.

**R2-1-B1 (brief, para 6: authorship told as settled; checklist 7).** Location: "In Benjamin's life, Agathon tells in his own voice how Benjamin consecrated a church of Saint Macarius in the desert. ... Early in the account, Agathon writes: ..." Evidence: records.json, agathon, contested_claims, "Whether the account of the Macarius consecration is Agathon's", with the History's first person (SEV l.46143) on one side and Renaudot (REN l.11546-11563, "in longa illa sub Agathonis nomine fabula") on the other. The brief names Renaudot's doubt and then answers it in the narrator's voice: "Agathon writes". Round 1's "he writes" was ambiguous. The A-M1 fix, "Agathon writes", takes a side. SEV l.45958 shows what the History itself says: "Abba Agathon says". Replacement (para 6):

> Benjamin's life in the History holds an account told in Agathon's voice. It tells how Benjamin consecrated a church of Saint Macarius in the desert. Eusèbe Renaudot was a Catholic who wrote a Latin history of these patriarchs in 1713. He calls their line heretical, and that account a fable under Agathon's name. Early in the account, its writer names himself: "And as for me, the sinner Agathon, I was the son of the Father Benjamin, and knew much of his virtues through my intimacy with him."

Rescored: 362 words, FK 7.77, Flesch 63.11. The quotation is unchanged: SEV l.45965 "And as for me," and l.46143-46144 (OCR "I he sinner Agatbon").

**R2-1-M1 (card, legacy.traces[1]: "the church" clashes with the brief).** "The History dates the church of Saint Macarius to his days, without saying who built it." The brief (and keyWorks) has Benjamin consecrate "a church of Saint Macarius" before Agathon was patriarch. With "the church" the card seems to contradict the brief. PO5 l.503: "In the days of Abba Agathon was built the church which was dedicated in the name of the Father Macarius". Replacement: "The History dates a church dedicated to Saint Macarius to his days, without saying who built it. The brothers grew so many that they built cells near the Marsh."

**R2-1-M2 (card, uncertain[1]: Renaudot not marked as partisan in the card; checklist 6).** A-M2 marked him in the brief only. The card is a separate text: "Eusèbe Renaudot, a Catholic scholar writing in 1713, calls it a fable under Agathon's name." REN l.18609-18612, and l.11560-11561, where he calls these Copts "juratis Romanæ fidei hostibus". Replacement: "His own account in Benjamin's life. Eusèbe Renaudot, a Catholic scholar writing in 1713, calls these patriarchs heretics. He calls the account a fable under Agathon's name, and judges Benjamin's canons in it the work of later Copts."

**Scores.** 355 words, about 2:11. FK 7.89, Flesch 62.68. Passes. The one brief sentence over 25 words is the closing quotation.

---

### john-iii-of-samannud

**Verdict: no blocking finding. Minor fixes.**

| R1 finding | Status | Note |
|---|---|---|
| A-M3 | APPLIED | |
| A-M12 | APPLIED | PO5 l.1009-1017. Each answer now follows its own sum. |
| A-M13 | APPLIED (taken differently, sound) | The bargaining was moved up instead of Theodore. The Holy Week story now runs in one piece. The Theodore paragraph follows the who-line and reads as the start of his patriarchate, which is where PO5 l.717-726 puts it. "Soon" is gone. Cutting the secretaries' offer and the biscuit mill leaves nothing dangling. |
| A-M14 | APPLIED | PO5 l.718-721; REN l.12086-12087. |
| A-M15 | APPLIED | PO5 l.1318-1323. |
| A-M16 | APPLIED | Merged. |
| A-M27 | PARTLY | The who-line stays in para 4. The reason given (the scene runs three paragraphs) is fair. The first mention of John still has no identifier, which is a separate fail. See R2-1-M3. |
| A-M31, A-M32, A-M33 | APPLIED | Wrong line in the drachmae contested claim. See R2-1-M9. |

**R2-1-M3 (brief, para 1 and para 4: common name at first mention; nested sentence; checklist 8 and 4).** The brief opens "the patriarch John was held at the house of Samad". It does not reach "John III of Samannud" until para 4. Para 4's second sentence nests an appositive inside a relative clause: "B. Evetts, who translated the History, a later Arabic history of the Coptic church, dates his patriarchate 677 to 686." Replacement, para 1, first sentence: "In Holy Week, the patriarch John III of Samannud was held at the house of Samad, the governor of a castle." Para 4, first two sentences: "John followed Agathon as patriarch of Alexandria. The History is a later Arabic history of the Coptic church. B. Evetts, who translated it, dates John's patriarchate 677 to 686." Source for the heading: PO5 l.712 "JOHN III, OF SAMANNUD ... 677-686". Rescored: 352 words, FK 6.12, Flesch 75.33.

**Scores.** 351 words, about 2:10. FK 6.29, Flesch 74.96. Passes. Card sentences are 25 words or fewer.

---

### isaac-of-alexandria

**Verdict: both round 1 blocking findings are correctly applied. No new blocking finding. Minor fixes.**

| R1 finding | Status | Note |
|---|---|---|
| A-B1 | APPLIED | PO11 l.21226-21228: "Il ne faut pas chercher dans cette Vie une œuvre historique, telle qu'on la conçoit de nos jours. Le but de l'auteur est l'édification des lecteurs, ou des auditeurs". Brief and card now keep "as conceived today". The "X, not Y" contrast is gone. The records cite the right lines (round 1's l.21232 was off). |
| A-B2 | APPLIED | PO11 l.21276-21289: three and a half years from "P. O., III, 268". Porcher's notice, l.21210-21212, identifies that as the Synaxarium at 9 Hatour. The Sunday consecration is from Mina ("infra, p. [57]"). The Tuesday death is from "Pierre ibn Rahib, loc. cit.". 684 to 687, and "mais les jours de la semaine sont-ils authentiques? — [F. N.]". The card is accurate. |
| A-M17 | APPLIED | PO11 l.25629, 25636 "Maurotanie". |
| A-M18 | APPLIED | PO11 l.25893-25900, 26019-26021; l.23915-23916 for "the Amir". |
| A-M19 | APPLIED | PO11 l.21560-21564. Correct, but nested. See R2-1-M10. |
| A-M20 | APPLIED | PO11 l.21324-21327 (title, "évêque de la ville de Pchati"); l.21246-21248 (Porcher). |
| A-M21 | APPLIED | |
| A-M22 | APPLIED | BUD1 l.16502-16512. I searched Mina's chapter "Chez l'archevêque" (PO11 l.22989-23180) and the parents' visit (l.22150-22153). The archbishop is never named there, so "Mina does not name him" holds. Wording: see R2-1-M11. |
| A-M31 | APPLIED | |

The cut death days and "from Saint Macarius" leave nothing dangling. "E. Porcher, who edited Mina's Life, says it ..." reads as Mina's Life, the nearest noun.

**R2-1-M10 (brief, para 3: nested sentence; checklist 4).** "His parents placed him with a kinsman, Meneson, who served George, the governor of Egypt, to train as a secretary." Two appositives are stacked, and "to train" lands after George, so it can read as George training. PO11 l.21560-21564: "le mirent entre les mains d'un de leurs parents, nommé Meneson, administrateur (chartularius) au service de Georges, qui était éparque au pays d'Égypte, afin que le jeune Isaac devînt secrétaire". Replacement: "His parents placed him with a kinsman, Meneson, to train as a secretary. Meneson served George, the governor of Egypt." Rescored: FK 6.93, Flesch 68.97.

**R2-1-M11 (card, uncertain[3]: "the same story of Abba John" is unclear).** "Budge's Ethiopic tells the same story of Abba John" can read as a story about John. Budge names John as the archbishop who wanted the scribe. BUD1 l.16507-16512: "Abba JOHN the archbishop was seeking for a learned man to be his disciple and his scribe ... ISAAC made mistakes in his writing wittingly". Replacement: "The archbishop in the letter story. Mina does not name him. Budge's Ethiopic tells the same story and names him Abba John the archbishop."

**Scores.** 345 words, about 2:08. FK 7.06, Flesch 68.92. Passes. Card sentences are 25 words or fewer.

---

### simon-i-of-alexandria

**Verdict: no blocking finding. Minor fixes, mostly from the round 1 edits to para 5.**

| R1 finding | Status | Note |
|---|---|---|
| A-M23 | APPLIED | Brief: PO5 l.1472. Card place: see R2-1-M8. |
| A-M24 | APPLIED | PO5 l.2020-2027. |
| A-M25 | APPLIED | PO5 l.2178-2262. The new sentence has a timing problem; see R2-1-M5. |
| A-M26 | APPLIED | BUDM l.42819-42821. Wording: see R2-1-M6. |
| A-M27 | APPLIED | "Simon I of Alexandria was a Syrian, from the East." The Evetts sentence that replaced the old who-line is nested; see R2-1-M7. |
| A-M28 | APPLIED | |
| A-M29 | APPLIED | REN l.12467-12470 "iterum & tertio". |
| A-M30 | APPLIED | BUDM l.42791-42792 (four days), l.42820-42821 (exile). |
| A-M31, A-M32, A-M33 | APPLIED | Citation lines in two records are wrong. See R2-1-M9. |

The cuts (bread and salt, communion before the cup) and "went to see the monks of Wadi Habib" check against PO5 l.1736-1749 and l.2448-2453. "Some of his own priests poisoned his cup, but it did him no harm" is true to the History, which says "a second time, but it did not hurt him" (l.1748-1749).

**R2-1-M4 (brief, para 5: a pronoun with an unclear antecedent, and a truth with no charge; checklist 4).** The A-M25 edit turned "The Amir questioned Simon at night" into "When the Amir questioned him at night, Simon said:". The nearest "him" candidates are now the new bishop and the caliph Abd al-Malik. The paragraph also never says what Simon was accused of, so "the Amir saw that Simon had told the truth" has no content. PO5 l.2027-2031: Abd al-Malik wrote to Abd al-Aziz, "the patriarch of the Christians, who lives at Alexandria, has sent information of the affairs of Egypt to India". l.2118: "Now this was at night." Replacement, after "...cut off.": "He wrote to the Amir that the patriarch had sent news of Egypt to India. The Amir questioned Simon at night, and Simon said: "If a voice came from heaven, bidding me deviate from the truth, I would say no otherwise."" The quotation is unchanged (PO5 l.2120-2121).

**R2-1-M5 (brief, para 5: "Two days later").** The History has "at sunset on the second day" (PO5 l.2179), counted inside the three-day delay that the Amir granted (l.2173-2174). It also says "the morning of the third day" for the hearing (l.2217). "Two days later" sets no point to count from. Replacement: "On the second day the Indian priest was found, and the Amir saw that Simon had told the truth." PO5 l.2253-2256 "Simon was innocent ... acknowledged his honesty".

**R2-1-M6 (brief, para 4: the exile clause reads as a sequel).** "...and the priests were set free. The Ethiopic Synaxarium, a book of saints' days, says they were sent into exile." Heard aloud, this can sound like what came next. It is a different account. Budge: the Khalifah "drove into exile the priests" in place of burning them (BUDM l.42819-42821). The History has them freed (PO5, with records). Replacement: "The Ethiopic Synaxarium, a book of saints' days, says instead that they were sent into exile."

**R2-1-M7 (brief, para 3: nested sentence; checklist 4).** "B. Evetts, who translated the History, a later Arabic history of the Coptic church, heads his life 689 to 701." This is the A-M27 rewrite. It stacks an appositive inside a relative clause, and "his" comes right after "the Coptic church". Replacement: "The History is a later Arabic history of the Coptic church. B. Evetts, who translated it, heads Simon's life 689 to 701." Source: PO5 l.1535 heading "SIMON I, THE FORTY-SECOND PATRIARCH. A. D. 689-701". With R2-1-M4 to M7 together: 381 words, about 2:21, FK 5.70, Flesch 77.64.

**R2-1-M8 (card, place: two witnesses joined).** "Brought up at the monastery of Az-Zajaj, and buried there. The synaxaria place it west of Alexandria." The synaxaria do not name Az-Zajaj. Each places "the monastery where the body of Saint Severus lies" west of Alexandria: PO17 l.58448-58450 "au couvent où se trouve le corps de saint Sévère (Sâwîros), à l'ouest d'Alexandrie"; BUDM l.42750-42752 "the monastery to the west of the city of Alexandria, wherein is the body of Saint Severus". Saying "it" makes the two the same place on our word. Replacement: "Born in the East, the History says. Brought up at the monastery of Az-Zajaj, and buried there. The synaxaria place his monastery west of Alexandria, where Saint Severus lies."

**Scores.** 361 words, about 2:14. FK 5.81, Flesch 77.31. Passes. Brief sentences over 25 words are quotations. Two card sentences are exactly 25 words.

---

### records.json (all four)

**R2-1-M9 (wrong lines in three new witness strings).** The claims are right. The cited lines do not hold them.
- john-iii, contested "What John said he lacked": "REN l.12088-12089". The words "ne centum quidem drachmas habere se" are at REN l.12096-12097. Replace with "REN l.12096-12097".
- simon-i, the Az-Zajaj claim: "PO17 ... l.58431-58432". Those lines are Arabic. The French "au couvent où se trouve le corps de saint Sévère, à l'ouest d'Alexandrie" is at l.58448-58450. Replace with "l.58448-58450". BUDM l.42751 is right.
- simon-i, contested "How often his cup was poisoned": "Basset (PO17 l.58440-58445)". Those lines are Arabic. "le firent une seconde et une troisième fois" is at l.58462-58463. Replace with "PO17 l.58462-58463". BUDM l.42778-42779 and REN l.12467-12470 are right.

The other new records I opened match their lines: PO5 l.495 (fleet), BAS1 l.19364-19365 (7,000 dinars a year), BUD1 l.13547-13548, PO11 l.21208-21211 and 21276-21289, PO11 l.21560-21564, BUD1 l.16502-16512, PO5 l.1318-1323, ABU l.11311-11335, REN l.986, PO5 l.2178-2262.

---

### Count

- **Blocking: 1.** R2-1-B1 (Agathon, authorship told as settled).
- **Minor: 11.** R2-1-M1 to R2-1-M11. Agathon 2, John III 1, Isaac 2, Simon 5, records 1.
- **Round 1 findings:** A-M27 is PARTLY applied (for John III, by the drafter's judgment, which is sound as far as it goes). Every other A-* finding for these four profiles is APPLIED, and A-B1 and A-B2 are applied correctly.

| Profile | Words | FK | Flesch | Blocking | Minor |
|---|---|---|---|---|---|
| agathon-of-alexandria | 355 | 7.89 | 62.68 | 1 | 2 |
| john-iii-of-samannud | 351 | 6.29 | 74.96 | 0 | 1 |
| isaac-of-alexandria | 345 | 7.06 | 68.92 | 0 | 2 |
| simon-i-of-alexandria | 361 | 5.81 | 77.31 | 0 | 5 |
| records.json | | | | 0 | 1 |

## R2 review, era 4 Who batch 6, PART 2 (targeted recheck)

**Scope.** alexander-ii-of-alexandria, michael-i-of-alexandria, joseph-i-of-alexandria, severus-ibn-al-muqaffa (brief, card, audio, records.json rows), and the batch README.md. Round 1 findings B-*, M-*, J-*, S-*, R-*.

**Method.** I read CLAUDE.md, Who_Profile_Pattern.md (14-point checklist), R1_review.md (Part B) and R1_changes.md. I took the word diff `git diff ed936fc6 d70de91c` for each brief and card, and a JSON row diff of records.json for the four profiles. I reopened every source line behind each changed string and read it in context: PO5 (Evetts's History, PO 5, the file named `chronicle-of-seert_...-patrologia-orientalis-5-...scher-dib1910.txt`), REN (Renaudot 1713), BUD1 (Budge, Ethiopic Synaxarium v1), BAS1 (Basset, Arabic Synaxarium, Thout to Babeh), ABU (Abu Salih, Evetts 1895), and SEV (Evetts 1904). I checked each new quote word for word. I diffed each audio script against its brief and checked the tags. I ran `grade_text` on each brief, and by script I checked every brief and card sentence for length over 25 words. Unchanged text was not re-reviewed, but two things I saw in passing are reported.

Abbreviations for files are as in R1 Part B.

---

### alexander-ii-of-alexandria

**Verdict: revise.** 1 blocking, 5 minor. The round 1 fixes are in place. One round 1 addition says something about Renaudot that he does not say.

| R1 finding | Status | Note |
|---|---|---|
| B-B1 brand vs ring | APPLIED | Brief, card and records now separate the left-hand brand (PO5 l.3469-3472) from Renaudot's ring worn on the right (REN l.13440-13442). The card's wording leaves out that both carry a name (R2-2-A-M2). |
| B-B2 "only Shamul" | APPLIED | "Shamul, bishop of Wasim, was the only bishop with him." matches PO5 l.3908-3909. The drafter also cut "They fled down the river", which the fix did not ask for (R2-2-A-M4). |
| B-B3 asked leave to beg | APPLIED | Brief and knownFor match PO5 l.3003-3008. |
| B-B4 false absence, writer of last years | PARTLY | The absent row is gone, and the claim and README are right. The new card sentence "Renaudot reads him the same way" is not right (R2-2-B1). |
| B-M1 "still reigning" note | PARTLY | There is now context. The quote is moved into the note, but it belongs to the main text (R2-2-A-M1). |
| B-M2 Evetts name forms | APPLIED | The prose now has only "B. Evetts" or "Evetts". "B. T. A." is left only in the source title. R1_changes says the card has "B. Evetts" at first mention and "Evetts" after. In fact "B. Evetts" appears four times. That is one form, so the defect is gone, but the log describes the fix wrongly. |
| B-M3 identifier at first mention | APPLIED | "Alexander II, the Coptic patriarch of Alexandria, went to Misr..." |
| B-M4 people and clergy | APPLIED | Matches PO5 l.3141-3142. |
| B-M5 Renaudot seal in records | APPLIED | REN l.13550-13553 is added. It reads "figillum plumbeum, m quo Iconis figura erat, ex collo pendens". |
| Cross-profile frame | APPLIED in part | "tells it this way" and "gives his years as". |

**R2-2-B1 (blocking). The card's "Renaudot reads him the same way" misstates Renaudot on where George's part ends.** Card, `uncertain` item 2: "John the deacon ... says the archdeacon George's history ran to the removal of the governor Usamah. John says he told what followed himself, down to the death of the patriarch Theodore. Renaudot reads him the same way."
Evidence: PO5 l.4532-4537 says George "informed us of what happened in the time of Marcian ... down to the time of Sulaiman, son of Abd al-Melik, prince of the Muslims, after whom reigned Omar, son of Abd al-Aziz, who drove away Usamah, the unbelieving governor". The line ends George's account at the time of Sulaiman. It names Usamah's removal only to identify Omar. REN l.13766-13769 says George wrote "usque ad Solimanum Abdelmelici filium; quibus ipse autor adjecit quae usque ad Theodori mortem, sub Asama & aliis Aegypti Praefectis ... secuta sunt". So Renaudot puts the years under Usamah in the History author's own addition. The card puts them in George's part and then says Renaudot agrees. That matters here, because the brief tells Usamah's branding. "The patriarch Theodore" also has no identifier (item 8). PO5 l.4586-4587 has "the blessed Father Theodore, patriarch of Alexandria". The removed absent row (PO5 l.4534-4537, "ended at Usamah's removal") had the same overreading; no remaining record row repeats it.
Fix, card: "Who wrote it. John the deacon, who wrote the History's life of Michael I, says the archdeacon George's history ran down to the time of the caliph Sulaiman. John says he told what followed himself, down to the death of Theodore, patriarch of Alexandria. Eusèbe Renaudot, a Catholic scholar writing in Latin in 1713, reads him the same way, and puts the years under the governor Usamah in John's part." (The sentences run 25, 15 and 27 words. To stay under 25, split the last: "Eusèbe Renaudot, a Catholic scholar writing in Latin in 1713, reads him the same way. He puts the years under the governor Usamah in John's part.") Records: in the John-the-deacon claim row, add "George to 'the time of Sulaiman' (PO5 l.4534-4537); Renaudot: 'usque ad Solimanum ... sub Asama' (REN l.13768-13771)". README: "John says the archdeacon George ... wrote the history down to the days of Alexander II" is sound as it stands (PO5 l.4501-4504).

**R2-2-A-M1. "Still reigning" is quoted as if the note said it.** Card, `uncertain` item 1: "A note in it says the emperor Anastasius was "still reigning" when the writer wrote. B. Evetts says a translator added that note."
Evidence: PO5 l.2952-2955. The main text has "Anastasius was made prince of the Romans, and is still reigning." The note reads "(N. B. By saying «still» the writer means at the time of composing the history.)" Evetts's footnote, l.2956: "This note is evidently added by the translator."
Fix: "It says the emperor Anastasius "is still reigning". A note in it explains that the writer means at the time he wrote. B. Evetts says a translator added that note."

**R2-2-A-M2. The card makes it sound as if only Renaudot's ring bore a name.** Card, `uncertain` "The brand": "... Renaudot says they had to wear an iron ring on the right hand, with their church's name on it."
Evidence: in PO5 l.3471-3473 the brand also bore a name: "adding the name of his church and his monastery, without a cross". REN l.13441-13442 has "inscripto simul nomine Ecclesiae aut Monasterii", so church *or* monastery. records.json already says "inscribed with church or monastery".
Fix: "The brand. The History says Usamah branded each monk on the left hand with a ring-shaped iron, adding the name of his church and monastery. Renaudot says they had to wear an iron ring on the right hand, with the name of their church or monastery."

**R2-2-A-M3. Renaudot appears in the card before he is introduced.** Card, `uncertain` item 2 (new in round 1) ends "Renaudot reads him the same way". His introduction ("Eusèbe Renaudot, a Catholic scholar writing in Latin in 1713") is in item 3. No earlier card field names him. The R2-2-B1 fix moves the introduction into item 2. Item 3 then needs only "Renaudot says they were counted."

**R2-2-A-M4. The brief no longer says that he fled, though the card's knownFor rests on it.** Brief, last paragraph: "... he told the brothers. At dawn, at Tarnut, he died." The cut of "They fled down the river" was not part of the B-B2 fix. Now the listener hears "Prepare the boat ... that we may depart" and then a death at Tarnut, with no flight. knownFor says "he died fleeing a branding".
Evidence: PO5 l.3909-3911: "when they had descended the river in their flight, they reached Tarnut bv thc morning; and at that hour the blessed Alexandcr went to his rest at thai place."
Fix: "They fled down the river and reached Tarnut by morning, and there he died. Shamul, bishop of Wasim, was the only bishop with him." (The rescored brief, with this fix and the M5 fix: FK 6.03, Flesch 72.9.)

**R2-2-A-M5. In the brief, only one side of the contested brand is named.** Paragraph 5: "Under the governor Usamah, monks were branded on the left hand with a ring-shaped iron. Eusèbe Renaudot ... says instead ..." The first side has no witness in its sentence. This is a contested claim with a contested_claims row, and item 7 wants both sides named. The previous paragraph ends "the History says", but that sentence is about the Easter clergy.
Fix: "The History says that under the governor Usamah, monks were branded on the left hand with a ring-shaped iron."

Audio: matches the brief, with `[calmly]` at the start and `[warmly]` at the last paragraph. Grade: FK 5.89, Flesch 73.27. No sentence runs past 25 words.

---

### michael-i-of-alexandria

**Verdict: pass after one minor fix.** 0 blocking, 1 minor.

| R1 finding | Status | Note |
|---|---|---|
| M-B1 John's spiritual father | APPLIED | "John, the sinner" matches PO5 l.10511 ("so also did I, John, the sinner"). "Moses, bishop of Wasim, his spiritual father" matches PO5 l.5169 ("my spiritual father, Abba Moses, bishop of Wasim"). Brief, card and README agree. The quote and the man it names are back together. |
| M-M1 priest vs monk | APPLIED | Brief says "priest" (PO5 l.5500). Card place: "the History says ... the synaxaria say". Records cite PO16 l.12449-12450 and BUDM l.20799-20800. |
| M-M2 letters | APPLIED | Split in two sentences. "Letters from Egypt reached Cyriacus ... while Michael was in prison. The governor then seized Michael again, John says." This matches PO5 l.7070-7073 ("Abd al-Malik heard of these communications, and therefore he seized the patriarch"). |
| M-M3 translator named | APPLIED | "B. Evetts, its translator, calls that a copyist's slip." ABU l.13476 has Evetts's unsigned note. ABU l.134 says Butler's notes "bear his initials", so the note is Evetts's. |
| M-M4 Evetts forms | APPLIED | Prose uses "B. Evetts" only. See the note under B-M2. |
| Cross-profile frame | APPLIED | "B. Evetts's English ... sets his years at". |

**R2-2-M-M1. Who heads the life with 744 to 768: the brief, the card's dates and the card's uncertain item give three different answers (item 9).** Brief: "B. Evetts's English ... sets his years at 744 to 768." Card dates: "B. Evetts heads his life 744 to 768, and his volume's title gives 766." Card `uncertain`, "His years": "The History's heading gives 744 to 768, and its title 766." The A.D. dates in the running heads are Evetts's. One example is PO5 l.2577: "PT. I. CH. XVII. ALEXANDER II, A. D. 705-730". The Arabic does not give them. "The History's heading" gives the dating to the wrong witness. The item is unchanged, but the brief's round 1 rewording makes the drift visible.
Fix, card `uncertain`: "His years. B. Evetts's heading gives 744 to 768, and his volume's title 766. Basset's synaxarium brackets 743 to 767. Renaudot argues for an ordination about 741 or 742."

Audio matches. Grade: FK 6.59, Flesch 71.70. No sentence runs past 25 words.

---

### joseph-i-of-alexandria

**Verdict: pass after minor fixes.** 0 blocking, 2 minor.

| R1 finding | Status | Note |
|---|---|---|
| J-M1 Dionysius of Tel Mahre | APPLIED | Brief paragraph 3. |
| J-M2 "Joseph of the city of Manuf" | APPLIED | Brief and card match BUD1 l.14814-14815 ("Salutation to Archbishop JOSEPH of the city of MANUF, unto whom was given the knowledge of Letters"). |
| J-M3 church dropped, Renaudot added to the plea | APPLIED | The plea is in BUD1 l.14723-14733 and REN l.18205-18206 ("intercessit & obtinuit, ut illis parceretur"). It is not in BAS1 (l.20411-20420 go straight from the dagger to the diploma). The split is right. The pillar sentence still names one witness out of three (R2-2-J-M1). |
| J-M4 Ethiopian bishop John | APPLIED | BUD1 l.14743-14775: "send unto us as bishop Abba JOHN" and "brought back Abba JOHN". |
| J-M5 held witness in records | APPLIED | BH1 l.21266. |

**R2-2-J-M1. The pillar is in all three held accounts, but the brief names only the Arabic Synaxarium.** Paragraph 5: "The sword struck a pillar and broke, the Arabic Synaxarium says. In the Ethiopic Synaxarium and in Renaudot, Joseph begged the ruler to spare the two bishops." Placed this way, the first sentence reads as the Arabic Synaxarium's alone, against the other two.
Evidence: BAS1 l.20399-20401: "le sabre donna contre un pilier et se brisa". BUD1 l.14700-14701: "his sword struck a pillar, and broke". REN l.18207-18208: "in columnam marmoream acinacis impactus, in frusta dissiluit" (OCR "im|>adiis, in fiufta dilll- liit").
Fix: "The sword struck a pillar and broke, both Synaxaria and Renaudot say. In the Ethiopic Synaxarium and in Renaudot, Joseph also begged the ruler to spare the two bishops." (Rescored: FK 6.98, Flesch 67.35.) The card's "Who sent the swordsman" item already shows where the three differ.

**R2-2-J-M2 (unchanged text, seen in passing). The pronoun "He" is unclear.** Paragraph 4: "Bar Hebraeus, a thirteenth-century Syriac historian, quotes what Dionysius wrote of Joseph's church. He found the Copts chaste, sincere and humble." The subject of the first sentence is Bar Hebraeus, so "He" reads as Bar Hebraeus. The man who visited was Dionysius (BH1 l.21905-21926).
Fix: "Dionysius found the Copts chaste, sincere and humble."

Audio matches. Grade: FK 6.95, Flesch 67.42. No sentence runs past 25 words.

---

### severus-ibn-al-muqaffa

**Verdict: pass after minor fixes.** 0 blocking, 2 minor.

| R1 finding | Status | Note |
|---|---|---|
| S-B1 false absence, other works | APPLIED | The new note is checked. REN l.23117-23118 has "De quatuor primis Conciliis Synopsis Historica". SEV l.162-163 has "Ce prelat qui a ecrit pour refuter l'historien rival, Eutychius". ASS1 is cited. |
| S-M1 missed witnesses | APPLIED | The REN l.32122-32125 claim is added and placed on the "His" side of the contested extent. The Wadih claim is added (REN l.23570-23573, 23644-23646). The new card strings have two writing defects (R2-2-S-M1, R2-2-S-M2). |
| S-M2 thesis opener, "Even" build-up | APPLIED | The paragraph now opens on the witness, Evetts. "Evetts himself changed his date" is the reviewer's own wording. Its "himself" leans emphatic, but it is not a finding. |
| S-M3 Eutychius beat line | APPLIED differently | The sentence leaves the brief, and the card's keyWorks keeps it with Evetts and Renaudot. That is sound. The pattern says facts the card shows are not repeated, and keeping it would have put Evetts before his introduction. Nothing in the brief points to it. |
| S-M4 Abraham the Syrian | APPLIED | Brief and card dates. REN l.23003 "EPHRAEM SYRUS" and l.23011-23012 "vir Syrus negotiator, nomine Ephraem, qui alio nomine Abrahamus appellatur". |
| S-M5 Moses, friend of the adviser | APPLIED | REN l.23066-23069: Abu Yacoub "consiliarii locum habebat"; "Judaeus alius Moses qui illi familiarissimus erat". |

**R2-2-S-M1. "Renaudot's source" is a role standing in for a named witness (item 5).** Card, `uncertain`, new: "Renaudot's source says Severus himself wrote the life of the patriarch Abraham."
Evidence: REN l.32116-32123, in Renaudot's life of MARCUS FILIUS ZARAA, Patriarcha LXXIII (heading just before l.32114): "Ita enim accepisse se Autor testatur ab illius fratre patrueli; notatque eodem familiae cognomine fuisse jam alium Patriarcham Alexandrinum, cujus vitam Severus Aschmonin Episcopus scripsit, Ephrem scilicet". The witness is the author of the History's life of Mark, son of Zaraa. The card already uses this form for Philotheus ("The History's life of the patriarch Philotheus, as Renaudot gives it"). "Himself" adds emphasis and no fact.
Fix: "The History's life of the patriarch Mark, son of Zaraa, as Renaudot gives it, says Severus wrote the life of the patriarch Abraham." (23 words.)

**R2-2-S-M2. Wadih, son of Raja, is named with no context.** Card, legacy `remembered`, new: "Renaudot says Severus was a close friend of Wadih, son of Raja, who wrote down a miracle story Severus told him." A general reader does not know who Wadih is.
Evidence: REN l.23438-23441 calls Wadih a young noble of Misr raised "in Muhamedana Religione". From l.23441 Renaudot tells his conversion. REN l.23576-23577: "Scripsit quoque Vazah filius Reja, libros aliquot lingua Arabica".
Fix: "Renaudot says Severus was a close friend of Wadih, son of Raja, a Muslim of Misr who became a Christian and wrote books in Arabic. Wadih wrote down a miracle story Severus told him." (The sentences run 25 and 9 words.)

Audio matches. Grade: FK 6.52, Flesch 72.12. The one brief sentence over 25 words is the closing prayer, at 34 words. It is almost all quotation and is unchanged from round 1.

---

### README.md

| R1 finding | Status | Note |
|---|---|---|
| R-B1 | APPLIED | "John says ... he himself told the rest of Alexander's chapter, down to the death of the patriarch Theodore." This is sound against PO5 l.4584-4588. Chapter XVII also holds Cosmas I and Theodore (running heads at PO5 l.4218 and l.4332), so "Alexander's chapter" is loose but not wrong. "The patriarch Theodore" has no place identifier. A README is not participant-facing, so this is not counted. |
| R-M1 | APPLIED | "He calls Moses, bishop of Wasim, his spiritual father." |

The new Simon I line belongs to Part 1's profiles and is not checked here.

---

### Scores

| Brief | Words | FK | Flesch | Approx. time @162 |
|---|---|---|---|---|
| alexander-ii-of-alexandria | 354 | 5.89 | 73.27 | 2:11 |
| michael-i-of-alexandria | 362 | 6.59 | 71.70 | 2:14 |
| joseph-i-of-alexandria | 360 | 6.95 | 67.42 | 2:13 |
| severus-ibn-al-muqaffa | 346 | 6.52 | 72.12 | 2:08 |

All four pass `grade_text`. All four sit below the grade 8 floor CLAUDE.md describes, which is a rhythm signal and not a gate failure. All four audio scripts equal their briefs plus `[calmly]` at the start and `[warmly]` at the last paragraph. No tag appears in a brief, card or records row.

### Final counts (Part 2)

- Round 1 findings in scope: 28 (B-B1 to B-B4, B-M1 to B-M5, M-B1, M-M1 to M-M4, J-M1 to J-M5, S-B1, S-M1 to S-M5, R-B1, R-M1, plus the cross-profile frame note). APPLIED: 26 (counting S-M3, applied differently and sound, and the frame note, applied in part as R1 offered). PARTLY: 2 (B-B4, B-M1). NOT APPLIED: 0. The R1_changes description of the B-M2 and M-M4 fix is inaccurate, but the defect itself is gone.
- New blocking: 1 (R2-2-B1).
- New minor: 10 (Alexander 5, Michael 1, Joseph 2, Severus 2).
