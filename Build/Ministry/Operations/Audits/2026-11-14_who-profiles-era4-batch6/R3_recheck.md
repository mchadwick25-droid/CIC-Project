# R3 recheck: era 4 batch 6

Round 3, the last review round, a targeted recheck of the round 2 changes, by two fresh Opus agents that had not seen the drafting or the earlier rounds, at full effort. Part 1 covers Agathon, John III, Isaac and Simon I. Part 2 covers Alexander II, Michael I, Joseph I, Severus ibn al-Muqaffa and the README. Each part is given as its reviewer wrote it. Part 1 found one blocking point (R3-1-B1), which is open and goes to Mark for a cap ruling.

## Era 4 Who batch 6, round 3 review: PART 1 (last targeted recheck)

**Scope.** agathon-of-alexandria, john-iii-of-samannud, isaac-of-alexandria, simon-i-of-alexandria: brief, card, audio script, records.json entries. Round 2 findings R2-1-B1 and R2-1-M1 to R2-1-M11, and A-M27 (PARTLY in round 2).

**Method.** I read CLAUDE.md, Who_Profile_Pattern.md (14-point checklist), R1_review.md, R1_changes.md, R2_recheck.md and R2_changes.md. I ran `git diff --word-diff d70de91c b2e4318a` on the four profiles, their audio, and records.json. For each changed string I reopened its source lines in cic/texts/ and read them in context. I checked quotations word for word. I diffed each audio script against its brief with the two tags removed. I rescored each brief with `grade_text`, and checked brief and card sentence lengths by script. I read each brief once, start to end, as a listener would. Every replacement below was checked against its source line. Where it touches a brief, it was rescored.

**Files (cic/texts/).** PO5 = chronicle-of-seert_..._scher-dib1910.txt (Evetts's History, PO 5). SEV = severus-al-muqaffa_..._evetts1904.txt. REN = renaudot_..._1713.txt. PO11 = synaxaire-arabe-jacobite_po11-... (Porcher's Mina). PO17 = john-ephesus_lives-eastern-saints-po17_brooks1923.txt (Basset, 24 Abib, bound in). BUD1 = ethiopian-synaxarium_...-v1-.... BUDM = ethiopian-synaxarium_...-v2-v4-microform_budge1928.txt. ABU = abu-salih_....

**Audio.** All four scripts equal their briefs once `[calmly] ` and `[warmly] ` are removed. `[calmly]` opens line 1 and `[warmly]` opens the last paragraph in each. Checklist 13 passes.

---

### agathon-of-alexandria

**Verdict: pass after two minor fixes. R2-1-B1 is correctly applied.**

| R2 finding | Status | Note |
|---|---|---|
| R2-1-B1 | APPLIED | "Benjamin's life in the History holds an account told in Agathon's voice." SEV l.45958 "Abba Agathon says"; l.45965 and l.46143-46144 for the quote (OCR "I he sinner Agatbon"). "its writer names himself" takes no side, and Renaudot's view (REN l.11546-11549, "in longa illa sub Agathonis nomine fabula") sits beside it. Quote verbatim. |
| R2-1-M1 | APPLIED | PO5 l.503 "In the days of Abba Agathon was built the church which was dedicated in the name of the Father Macarius". The card no longer seems to contradict the brief. |
| R2-1-M2 | APPLIED | REN l.8589-8590 "de haereticis illis Patriarchis" and l.18609-18612 support "heretics". The new sentence leaves "these patriarchs" with nothing to refer to. See R3-1-M1. |

**R3-1-M1 (card, uncertain[1]: "these patriarchs" has no antecedent, and the label still settles authorship; checklists 4 and 7).** The item reads: "His own account in Benjamin's life. Eusèbe Renaudot, a Catholic scholar writing in 1713, calls these patriarchs heretics. ..." No patriarchs are named in the item, so "these" points at nothing. "His own account" is the claim R2-1-B1 removed from the brief, and the contested claim in records ("Whether the account of the Macarius consecration is Agathon's") is still open. Evidence: REN l.8589-8590, l.18609-18612 (see above); SEV l.45958. Replacement:

> The account told in his voice in Benjamin's life. Eusèbe Renaudot, a Catholic scholar writing in 1713, calls the Coptic patriarchs heretics. He calls the account a fable under Agathon's name, and judges Benjamin's canons in it the work of later Copts.

(REN l.11542-11543 "a Coptitis recentioribus inventa esse non dubitamus" for the canons. That part is unchanged.)

**R3-1-M2 (card, keyWorks[0].about: "his own voice"; checklist 9, brief and card agree).** "told in his own voice inside the History's life of Benjamin I." The brief now says "told in Agathon's voice". Replacement: "told in his voice inside the History's life of Benjamin I. Benjamin's vision and his rules for the church come through it. Eusèbe Renaudot called it a fable under Agathon's name". (The `ownWords` source keeps `author: Agathon of Alexandria`. That is the pattern's slot, and the doubt sits in uncertain[1].)

**Listener read.** The brief reads cleanly. The close moves from the account to Renaudot's doubt, then to the quote, and nothing in it sounds generated.

**Scores.** 362 words, about 2:14. FK 7.77, Flesch 63.11. Passes. The one sentence over 25 words is the closing quotation.

---

### john-iii-of-samannud

**Verdict: pass after one minor records fix. R2-1-M3 is correctly applied, and A-M27 is now resolved.**

| R2 finding | Status | Note |
|---|---|---|
| R2-1-M3 | APPLIED | Para 1 now has "John III of Samannud" (PO5 l.712, "JOHN III, OF SAMANNUD ... 677-686"). Para 4 is split into three plain sentences, and the nested appositive is gone. "John followed Agathon as patriarch of Alexandria" identifies Agathon at his first mention. |
| A-M27 (PARTLY in R2) | APPLIED | The first mention carries its identifier. The who-line stays in para 4, by the drafter's sound choice. |
| R2-1-M9 (John III part) | APPLIED, but the same string has three more wrong lines | See R3-1-M3. |

**R3-1-M3 (records, john-iii, the Renaudot claim row: three of its four line cites are wrong).** The witness string, changed in round 2, reads "REN ... l.12065-12067, 12084, 12096-12097, 12173-12178". Only 12096-12097 is right ("ne centum quidem drachmas / habere se"). In the vendored file, l.12065 is "Digitized by Google", l.12084 is "ni restituerentur.", and l.12173-12178 tell of Isaac's call to Alexandria. The drafter's numbers run 8 lines short through this page, the same offset R2-1-M9 found. The quoted words are at:
- l.12072 "Joannes Semnudaeus in Agathonis locum suffectus est" (OCR "Semnudarus", "Apthonis") and l.12073-12074 "sed diversae fidei, nam erat Jacobita";
- l.12092 "centum aureorum millia";
- l.12096-12097 "ne centum quidem drachmas habere se";
- l.12198 "debuit an. Heg. 67, J. C. 686" (OCR "^7%").

Replacement: "REN (renaudot_historia-patriarcharum-alexandrinorum-jacobitarum-lat_1713.txt) l.12072-12074, 12092, 12096-12097, 12198 [OCR 'Semnudarus', 'Apthonis', 'Heg. ^7%']".

**Listener read.** The scene runs well. The new para 4 is three short declaratives in a row ("John followed ... The History is ... B. Evetts, who translated it, ..."). It is a little flat, but it is clear and nothing in it is wrong. "A later Arabic history" leaves "later" without an anchor. That phrase is the same in all eight profiles, so it is a fleet wording point and not counted here.

**Scores.** 352 words, about 2:10. FK 6.12, Flesch 75.33. Passes. The one sentence over 25 words (26) is the closing quotation.

---

### isaac-of-alexandria

**Verdict: pass after two minor fixes. The R2-1-M10 split left a pronoun without a clear referent.**

| R2 finding | Status | Note |
|---|---|---|
| R2-1-M10 | APPLIED, with a side effect | PO11 l.21560-21564 "le mirent entre les mains d'un de leurs parents, nommé Meneson, administrateur (chartularius) au service de Georges, qui était éparque au pays d'Égypte, afin que le jeune Isaac devînt secrétaire". The split is accurate. See R3-1-M4. |
| R2-1-M11 | APPLIED | BUD1 l.16507-16508 "Abba JOHN the archbishop was seeking for a learned man to be his disciple and his scribe"; l.16511-16514 for the bad writing on purpose. Accurate. |

**R3-1-M4 (brief, para 3: "called him" now has the wrong nearest referent; checklist 4).** "Meneson served George, the governor of Egypt. The History says John III called him and made him his partner in governing the church." Before the split, Isaac was the object of the sentence ahead ("placed him"). Now the nearest males are Meneson and George, so "called him" can be heard as calling George or Meneson. Evidence: PO5 l.1167-1178. John "wrote and summoned that brother", a monk of Saint Macarius, and "commanded him to become his partner in administering the affairs of the Church". Replacement: "The History says John III called Isaac and made him his partner in governing the church." Rescored: 345 words, FK 6.96, Flesch 68.72.

**R3-1-M5 (brief, paras 3 and 4: two Georges back to back; checklist 4, listener).** The split gives the governor his own sentence, "Meneson served George, the governor of Egypt." The next paragraph opens with "George, a deacon of Sakha", and then "John had not named George". Both are identified, but a listener hears three Georges in five sentences, and the first one plays no part in the story. Replacement for the split sentence: "Meneson served the governor of Egypt." (PO11 l.21562-21563 "au service de Georges, qui était éparque au pays d'Égypte". The name stays in records.) With M4: 344 words, FK 6.96, Flesch 68.64.

**Listener read.** Otherwise clean. The letter scene, Porcher's caveat, the succession and the two accounts of the danger all follow in order.

**Scores.** 345 words, about 2:08. FK 6.93, Flesch 68.97. Passes. No brief sentence runs over 25 words.

---

### simon-i-of-alexandria

**Verdict: one blocking finding, which a round 2 fix exposed. Minor fixes otherwise. R2-1-M4 to R2-1-M8 are applied.**

| R2 finding | Status | Note |
|---|---|---|
| R2-1-M4 | APPLIED | PO5 l.2027-2031: Abd al-Malik writes that "the patriarch of the Christians, who lives at Alexandria, has sent information of the affairs of Egypt to India"; l.2118 "Now this was at night." "He wrote to the Amir" follows "The caliph Abd al-Malik had ...", so "He" is clear. The quote matches l.2120-2121. |
| R2-1-M5 | APPLIED, but loose | "On the second day the Indian priest was found, and the Amir saw ..." joins two days into one clause. See R3-1-M6. |
| R2-1-M6 | APPLIED | BUDM l.42819-42821 "drove into exile the priests". |
| R2-1-M7 | APPLIED | PO5 l.1535 heading. Sound. See R3-1-M8 on "heads". |
| R2-1-M8 | APPLIED, on a premise that was too narrow | See R3-1-M7. |
| R2-1-M9 (Simon part) | APPLIED | PO17 l.58449-58450 and l.58463 are right. BUDM "l.42750-42752" stops one line short; see R3-1-M9. |
| Cuts in R2_changes | Sound | "The Amir Abd al-Aziz liked the man ..." is folded into "the Amir Abd al-Aziz agreed" (PO5 l.1580-1581, 1587: "his heart inclined towards him, because he was a handsome person"; "the appointment of John had been confirmed"). Cutting "Simon kept to himself ..." (PO5 l.1741-1742) leaves nothing dangling. |

**R3-1-B1 (card, uncertain[1], and the records contested row "How far George's history ran": Renaudot's reading misstated; a round 2 fix now contradicts it; checklist 1 and 7).** The card reads: "Who wrote these years. John the deacon gives George's history down to the days of Alexander II. Renaudot reads it as down to Simon." The contested row reads: "To the days of Alexander: John the deacon (PO5 l.4502-4503)" against "To Simon: Renaudot's reading (REN l.13765-13766)".

Evidence. REN l.13765-13772, one sentence: "Praecedentium Patriarcharum historiam a Cyrillo usque ad Simonem scriptam esse testatur a multis, atque praesertim a Georgio Monacho Archidiacono & Secretario Simonis Patriarchae, ... qui persecutus est ea, quae a Marciano Imperatore Jacobitae sustinuerunt, & quae deinde Patriarchae eorum passi sunt, usque ad Solimanum Abdelmelici filium; quibus ipse autor adjecit quae usque ad Theodori mortem, sub Asama ... secuta sunt." Renaudot says that many wrote the lives from Cyril to Simon, George above all, and that George carried his account down to Sulaiman. That is John the deacon's own end point (PO5 l.4534-4535, "down to the time of Sulaiman, son of Abd al-Melik"). The card and the row take his first clause and present it as a disagreement. His same sentence removes that disagreement.

The round 2 fix to R2-2-B1 makes the conflict visible in three places. Simon's own records claim row now quotes Renaudot "usque ad Solimanum" (REN l.13766-13772). The Alexander II card, changed in round 2, says Renaudot "reads him the same way". The Simon card still says he reads it differently.

Why this is blocking, and the case against. "a Cyrillo usque ad Simonem" is in Renaudot's words, so the card is not invented. But it tells a dispute between two named witnesses that the second witness does not hold. That is misleading, and it contradicts a sister card in the same batch.

Replacement, card uncertain[1]:

> Who wrote these years. John the deacon says George's history ran from Cyril to the days of Alexander II, down to the time of the caliph Sulaiman. Renaudot gives George the same end point. He says many wrote the lives from Cyril to Simon, George above all.

(Sentences of 23, 7 and 13 words. PO5 l.4501-4505 and l.4532-4535; REN l.13765-13770. Cyril is named as "Cyril of Alexandria" earlier in the card, at legacy.traces[2]. Renaudot is introduced in `dates`.)

Records: remove the contested row "How far George's history ran", since no witness holds the second side. In the claim row "Renaudot: 'annos septem ...'", replace "George's history 'a Cyrillo usque ad Simonem'" with "the lives 'a Cyrillo usque ad Simonem' written 'a multis, atque praesertim a Georgio', who carried his account 'usque ad Solimanum'" (REN l.13765-13770).

**R3-1-M6 (brief, para 5: two days pressed into one clause, and the finding has no cause; checklist 1 and 4).** "On the second day the Indian priest was found, and the Amir saw that Simon had told the truth." PO5 l.2179-2181 has the priest found "at sunset on the second day" by "his spiritual son, the monk" (l.2210-2211: he "had been a fugitive"). The Amir learns the truth only "when the morning of the third day came" (l.2216-2217), when the priest "made known to him all that had happened" (l.2228-2230). The brief gives one day for both, and a listener does not learn why finding the priest proved anything. Replacement:

> At sunset on the second day, Simon's spiritual son found the Indian priest. The next morning the priest told the Amir all that had happened, and the Amir saw that Simon had told the truth.

Rescored: 375 words, about 2:19, FK 5.84, Flesch 77.11. The sentences run 13 and 23 words.

**R3-1-M7 (card, place: "where" attaches to Alexandria, and "Saint Severus" has no identifier; checklist 4 and 8).** "The synaxaria place his monastery west of Alexandria, where Saint Severus lies." Read as written, Severus lies in Alexandria. "Severus" is also a common name, in a batch with a Severus ibn al-Muqaffa profile. R2-1-M8 said the link between Az-Zajaj and Severus's body rested "on our word". It does not. The History itself makes it: PO5 l.1536-1541 says Simon's parents gave him to the church "for the sake of the body of the holy Saint Severus; for it lies in a shrine in that monastery", which is Abba John's monastery, Az-Zajaj (l.1472, 1503). BUDM l.3448-3451 names him: "they brought the body of Saint Abba Severus, Archbishop of the city of Antioch, to Dabra Zegag which is outside the city of Alexandria". The synaxaria (PO17 l.58449-58450; BUDM l.42752-42753) place the monastery holding his body west of Alexandria. Replacement:

> Born in the East, the History says. Brought up at the monastery of Az-Zajaj, and buried there. The History says the body of Saint Severus lies in a shrine there. Budge's Ethiopic names him Severus of Antioch, and the synaxaria place the monastery west of Alexandria.

**R3-1-M8 (brief, para 3: "heads Simon's life" is opaque aloud; checklist 4 and 9).** "B. Evetts, who translated it, heads Simon's life 689 to 701." A listener does not know that "heads" means "puts a date heading on". John III's brief, changed in the same round, says "dates John's patriarchate 677 to 686", which is clear. Replacement: "B. Evetts, who translated it, dates Simon's patriarchate 689 to 701." (PO5 l.1535 heading "A. D. 689-701".) For one term across the batch, the same change would apply to unchanged lines in Agathon para 2 ("heads his life 661 to 677") and Isaac para 2 ("heads his life there 686 to 689"). Those are reported here and not counted.

**R3-1-M9 (records, simon: the Az-Zajaj row's witnesses).** "BUDM l.42750-42752" stops before "is the body of Saint severus" (l.42753). The row also lacks the History's own link between the monastery and the body, and Budge's name for him, both of which the card will rest on after M7. Replacement witness: "PO5 l.1472, 1536-1541; PO17 l.58449-58450; BUDM l.42752-42753, 3448-3451". Add to the claim: "the History says Saint Severus's body 'lies in a shrine in that monastery' (PO5 l.1540-1541); Budge names him 'Archbishop of the city of Antioch' and his resting place Dabra Zegag (BUDM l.3448-3451)".

**Listener read.** Para 1 opens on the scene and moves well. Para 5 now gives the charge, the night questioning and the quote in order. Only the close of the episode jumps (M6). "John's monastery" in para 3 points back to para 1's "John, head of the monastery of Az-Zajaj", which is clear.

**Scores.** 359 words, about 2:13. FK 5.74, Flesch 77.68. Passes. The one sentence over 25 words (26) carries Simon's quotation. With M6 and M8: 375 words, about 2:19, FK 5.84, Flesch 77.11.

---

### Count

- **Blocking: 1.** R3-1-B1 (Simon card and records: Renaudot's reading of George's history misstated as a dispute; it now contradicts Simon's own records and the Alexander II card after round 2).
- **Minor: 9.** R3-1-M1 to R3-1-M9. Agathon 2, John III 1, Isaac 2, Simon 4.
- **Round 2 findings:** all twelve (R2-1-B1, R2-1-M1 to R2-1-M11) are APPLIED. R2-1-M5 and R2-1-M10 need the follow-ups M6 and M4. R2-1-M8 rested on a premise the History itself corrects (M7). A-M27 is now fully applied.

| Profile | Words | Time @162 | FK | Flesch | Blocking | Minor |
|---|---|---|---|---|---|---|
| agathon-of-alexandria | 362 | 2:14 | 7.77 | 63.11 | 0 | 2 |
| john-iii-of-samannud | 352 | 2:10 | 6.12 | 75.33 | 0 | 1 |
| isaac-of-alexandria | 345 | 2:08 | 6.93 | 68.97 | 0 | 2 |
| simon-i-of-alexandria | 359 | 2:13 | 5.74 | 77.68 | 1 | 4 |

## R3 review, era 4 Who batch 6, PART 2 (last targeted recheck)

**Scope.** alexander-ii-of-alexandria, michael-i-of-alexandria, joseph-i-of-alexandria, severus-ibn-al-muqaffa (brief, card, audio, records.json rows), and the batch README.md. The round 2 findings R2-2-* and the two round 1 PARTLY items (B-B4, B-M1) that R2_changes closes through them.

**Method.** I read CLAUDE.md, Who_Profile_Pattern.md (14-point checklist), R1_review.md, R1_changes.md, R2_recheck.md (Part 2) and R2_changes.md. I took `git diff --word-diff d70de91c b2e4318a` for the batch and read every changed string in my four profiles and their records rows. I reopened each source line behind each changed string and read it in context: PO5 (Evetts's History, PO 5, filed as `chronicle-of-seert_...scher-dib1910.txt`), REN (Renaudot 1713), BAS1 (Basset, Thout to Babeh), BUD1 (Budge, Ethiopic Synaxarium v1) and BH1 (Bar Hebraeus). I checked each quotation word for word, allowing for OCR. I diffed each audio script against its brief with the tags stripped, and checked tag placement. I ran `grade_text` on each brief. By script I checked every brief and card sentence for length over 25 words. I read each brief once, start to end, as a listener would. The README did not change in round 2, and I checked it again only against the changed card strings.

---

### alexander-ii-of-alexandria

**Verdict: pass after minor fixes.** 0 blocking, 2 minor. The round 2 blocking point is fixed in substance. Applying it as two card bullets left the second one with no subject.

| R2 finding | Status | Note |
|---|---|---|
| R2-2-B1 Renaudot on where George's part ends | PARTLY | The wording is right. PO5 l.4534-4537 has George's history running "down to the time of Sulaiman, son of Abd al-Melik, prince of the Muslims". PO5 l.4584-4587 has John's account running "down to the death of the blessed Father Theodore, patriarch of Alexandria". REN l.13767-13772 has "usque ad Solimanum Abdelmelici filium; quibus ipse autor adjecit quae usque ad Theodori mortem, sub Asama & aliis Aegypti Praefectis ... secuta sunt". The records row (witness REN l.13766-13772) is right. The R2 fix was one card item that ended with the Renaudot sentences. The drafter made them a separate array element, which leaves "reads him the same way" with no "him" in its own bullet (R3-2-M1). |
| R2-2-A-M1 "still reigning" | APPLIED | PO5 l.2950-2953: "Anastasius was made prince of the Romans, and is still reigning. (N. B. By saying «still» the writer means at the time of composing the history.)". Evetts's footnote, l.2956: "This note is evidently added by the translator." The card now matches. |
| R2-2-A-M2 brand bore a name | APPLIED | PO5 l.3469-3472: "branded each one of them on his left hand ... adding the name of his church and his monastery". REN l.13440-13442: "manicam ferream in dextra ferre jussit ... inscripto simul nomine Ecclesiae aut Monasterii". |
| R2-2-A-M3 Renaudot introduced late | APPLIED | His introduction is now in the first card string that names him. Item 4 reads "Renaudot says they were counted." |
| R2-2-A-M4 flight restored | APPLIED | "They fled down the river and reached Tarnut by morning, and there he died." This matches PO5 l.3909-3911: "when they had descended the river in their flight, they reached Tarnut by the morning; and at that hour the blessed Alexander went to his rest". |
| R2-2-A-M5 first side named | APPLIED | "The History says that under the governor Usamah, monks were branded..." |
| B-B4, B-M1 (R1 PARTLY) | APPLIED | Closed through R2-2-B1 and R2-2-A-M1. |

**R3-2-M1. The Renaudot sentences are a separate card bullet, so "him" has no antecedent, and the bullet has no topic label (items 4 and 12).** Card `uncertain`, item 3: "Eusèbe Renaudot, a Catholic scholar writing in Latin in 1713, reads him the same way. He puts the years under the governor Usamah in John's part." Every other item in the list opens on its topic ("Who wrote it.", "The brand."). Shown as a bullet of its own, "him" could be Alexander, the subject of the card. R2-2-B1 gave these sentences as the end of the "Who wrote it." item.

**R3-2-M2. "He told what followed himself" puts "himself" where it reads as the object of "followed" (item 4).** Card `uncertain`, item 2: "John says he told what followed himself, down to the death of Theodore, patriarch of Alexandria." This string changed in round 2.

Fix for M1 and M2 together: merge items 2 and 3 into one array element.
"Who wrote it. John the deacon, who wrote the History's life of Michael I, says the archdeacon George's history ran down to the time of the caliph Sulaiman. John says he himself told what followed, down to the death of Theodore, patriarch of Alexandria. Eusèbe Renaudot, a Catholic scholar writing in Latin in 1713, reads John the same way. He puts the years under the governor Usamah in John's part."
The sentences after the label run 25, 16, 15 and 11 words. Source check: PO5 l.4532-4537 and l.4584-4587; REN l.13767-13772. Renaudot does not name John. His "ipse autor" is the contemporary author whom, he says, Severus followed in this life ("Antiquum aliquem & aequalem Autorem ... secutus esse Severus videtur", REN l.13757-13758). PO5 names that author as John, so "John's part" is sound.

Seen in passing, not counted: REN l.13765-13767 (OCR "a multis, atque prarfertim a Georgio") says the earlier history was written "a multis, atque praesertim a Georgio" (by many, and above all by George), and that it ran "a Cyrillo usque ad Simonem". The card says only where George's part ends, and on that point Renaudot does agree, so "the same way" stands.

Audio: equal to the brief, with `[calmly]` at the start and `[warmly]` before the last paragraph. Grade: FK 6.03, Flesch 72.94. No brief or card sentence runs past 25 words.

---

### michael-i-of-alexandria

**Verdict: pass after one minor fix.** 0 blocking, 1 minor.

| R2 finding | Status | Note |
|---|---|---|
| R2-2-M-M1 who heads the life 744 to 768 | APPLIED | Card `uncertain`: "His years. B. Evetts's heading gives 744 to 768, and his volume's title 766." The running heads are Evetts's (PO5 l.4414 "MICHAEL I, THE FORTY-SIXTH PATRIARCH. A. D. 744-768"; l.4422, l.4508). The volume title is too (PO5 l.138 and l.302, "AGATHO TO MICHAEL I (766)"). Brief, card dates and card uncertain now all name Evetts. |

**R3-2-M3. "His" points to two different men in the same item (item 4).** Card `uncertain`: "His years. B. Evetts's heading gives 744 to 768, and his volume's title 766." The label's "His" is Michael, and the next "his" is Evetts, so the listener can read "his volume" as Michael's. The card `dates` has the same problem, which I saw in passing (unchanged in round 2): "B. Evetts heads his life 744 to 768, and his volume's title gives 766." In that sentence "his life" is Michael's and "his volume" is Evetts's.
Fix, card `uncertain`: "His years. B. Evetts's heading gives 744 to 768, and the title of Evetts's volume gives 766. Basset's synaxarium brackets 743 to 767. Renaudot argues for an ordination about 741 or 742."
Fix, card `dates`: "B. Evetts heads the life 744 to 768, and the title of his volume gives 766. The History says a council met in the year 459 of Diocletian, and he was consecrated on the 17th of Tut. He died on the 16th of Barmahat, after twenty-three and a half years by a record at Saint Macarius"
Source: PO5 l.138, 302, 4414.

Audio: matches. Grade: FK 6.59, Flesch 71.70. The only sentence over 25 words is a source title in `sources`, which is a citation.

---

### joseph-i-of-alexandria

**Verdict: pass after minor fixes.** 0 blocking, 2 minor.

| R2 finding | Status | Note |
|---|---|---|
| R2-2-J-M1 pillar in all three accounts | APPLIED | "The sword struck a pillar and broke, both Synaxaria and Renaudot say." Checked: BAS1 l.20400-20401, "le sabre donna contre un pilier et se brisa"; BUD1 l.14701, "his sword struck a pillar, and broke"; REN l.18208, "in columnam marmoream acinacis impactus, in frusta dissiluit" (OCR "im\|>adiis, in fiufta dilll- liit"). The plea is right to be told for the Ethiopic Synaxarium and Renaudot only. It is at BUD1 l.14725-14731 ("I therefore beseech thee to have mercy upon them") and REN l.18214-18215 ("intercessit & obtinuit, ut illis parceretur"). BAS1 l.20431-20439 goes from the dagger to the diploma with no plea. |
| R2-2-J-M2 "He" made "Dionysius" | APPLIED | BH1 l.21905-21907: "De papa Josepho ... patriarcha haec narrat: «eos esse invenimus populum pudicum, sincerum, humilem»". |

**R3-2-M4. The governor becomes "the ruler" two sentences later (item 9).** Brief paragraph 5: "Later two bishops whom Joseph's synod had cut off accused him to the governor. ... In the Ethiopic Synaxarium and in Renaudot, Joseph also begged the ruler to spare the two bishops." It is the same man: Budge's "King of Egypt" (BUD1 l.14695-14697) and Renaudot's prefect Afshin (REN l.18193-18197, 18212-18215; the prefect is "Afschinum Praefectum" at l.18194). The brief has already called him "the governor" for all three witnesses. Now that "also" ties the two sentences together, a listener may take "the ruler" for someone new, such as the caliph.
Fix: "In the Ethiopic Synaxarium and in Renaudot, Joseph also begged the governor to spare the two bishops." Make the same change in the audio script. Rescored: FK 7.07, Flesch 66.65.

**R3-2-M5. Records do not carry the brief's new "both Synaxaria and Renaudot" in full, and one Renaudot line number is wrong.** (a) The sword row ("The sword: Basset 'le sabre donna contre un pilier et se brisa' ...") cites only BAS1 and REN. No Joseph row cites Budge's pillar. (b) The row "Renaudot: the prefect's father sent 'in Ecclesiam'; Afshin ordered punishment and Joseph 'intercessit & obtinuit, ut illis parceretur'" cites REN l.18197-18206. The quoted words are at l.18214-18215. R2's evidence gave l.18205-18206 too.
Fix: in the sword row, add to the claim "; Budge 'his sword struck a pillar, and broke'", and to the witness "; BUD1 (ethiopian-synaxarium_book-of-saints-ethiopian-church-v1-maskaram-khedar_budge1928.txt) l.14697-14701". In the Renaudot plea row, change the witness to "l.18197-18215".

Audio: matches. Grade: FK 7.04, Flesch 66.88. No sentence runs past 25 words.

---

### severus-ibn-al-muqaffa

**Verdict: pass after minor fixes.** 0 blocking, 2 minor (one in records, one seen in passing in unchanged brief text).

| R2 finding | Status | Note |
|---|---|---|
| R2-2-S-M1 "Renaudot's source" | APPLIED | "The History's life of the patriarch Mark, son of Zaraa, as Renaudot gives it, says Severus wrote the life of the patriarch Abraham." REN l.32091-32092 heads "MARCUS FILIUS ZARAA Patriarcha LXXIII". l.32094 says this life's author "alius est ab illis qui praecedentes scripserunt". l.32122-32125: "Ita enim accepisse se Autor testatur ... cujus vitam Severus Aschmonin Episcopus scripsit, Ephrem scilicet". Renaudot gives Ephraem the other name Abraham at REN l.23011-23012. The records row adds the heading at l.32091, and that is right. The sentence runs 23 words. |
| R2-2-S-M2 Wadih given context | APPLIED | "... Wadih, son of Raja, a Muslim of Misr who became a Christian and wrote books in Arabic. Wadih wrote down a miracle story Severus told him." Checked: REN l.23439-23442 ("juvenis inter nobiliores urbis Misrae ... Institutus fuerat diligenter in Muhamedana Religione"); l.23526-23527 ("baptismum petiit & obtinuit"); l.23570-23572 ("magnam cum Severo ... amicitiam coluit"); l.23576-23577 ("Scripsit quoque Vazah filius Reja, libros aliquot lingua Arabica"); l.23644-23646 ("miraculum insigne de Eucharistia, quod acceptum a Severo ... Vazah literis consignavit"). The first sentence runs exactly 25 words. |

**R3-2-M6. The new Wadih records row cites lines that miss two of its own points.** Row: "Wadih son of Raja: 'juvenis inter nobiliores urbis Misrae', raised 'in Muhamedana Religione', became a Christian; ..." with witness "REN l.23439-23441, 23446-23509, 23576-23577". "in Muhamedana Religione" is at l.23442. Range 23446-23509 runs only as far as "affirmavit se velle Christianum fieri" (l.23508), which is a wish to become a Christian. The baptism, which the card's "became a Christian" rests on, is at l.23526-23527.
Fix, witness: "REN (renaudot_historia-patriarcharum-alexandrinorum-jacobitarum-lat_1713.txt) l.23439-23442, 23446-23527, 23576-23577". Add to the claim: "baptised, 'baptismum petiit & obtinuit' (l.23526-23527)".

**R3-2-M7 (unchanged text, seen in passing). Severus's quip loses its "today", so the brief says Muslims do not fast.** Brief paragraph 1: "Today is a fast day, he went on. Christians eat no meat, and in the evening they drink a little wine. Muslims do not fast, and drink no wine." Heard aloud, "Muslims do not fast" is a general statement, and it is false. REN l.23093-23094: "Muslemani non jejunant hodie nec vinum bibunt" (OCR "Mujlemani non jejunant hodte nec vinum btbunt"), that is, they do not fast *today*.
Fix: "Muslims do not fast today, and drink no wine." Make the same change in the audio script. Rescored: FK 6.55, Flesch 71.94, 347 words.

Seen in passing, not counted: the brief's first mention of the subject is a bare "Severus", in the dog scene. "Severus ibn al-Muqaffa" first comes in the eleventh sentence. Under item 8, "Severus" is a name that could mean more than one person (the README itself keeps him apart from Severus of Antioch). The approved Benjamin I brief has the same scene-first, bare-name pattern, so I take it as the batch's convention, not a defect of this round. If Mark wants the identifier in the opening line, use: "A dog walked past while Severus, bishop of al-Ushmunain, stood before the chief judge." (REN l.23087-23090, with the see from REN l.23571 "Episcopo Aschmonin".)

Audio: matches. Grade: FK 6.52, Flesch 72.12. The only brief sentence over 25 words is the closing prayer, at 34 words. It is almost all quotation and is unchanged since round 1.

---

### README.md

The README did not change in round 2, and round 2 gave it no new findings. I checked it against the changed card strings. "John says the archdeacon George ... wrote the history down to the days of Alexander II, and that he himself told the rest of Alexander's chapter, down to the death of the patriarch Theodore" agrees with Alexander's new card text. PO5 l.4501-4504 gives "down to the days of the father and confessor Alexander", and the same sentence also gives "the time of Sulaiman". "The patriarch Theodore" still has no place identifier. The README is not participant-facing, so this is not counted.

**R3-2-M8 (audit trail, not participant-facing). R2_changes.md misstates the Evetts name forms again.** R2_changes, last row of Part 2: "Correct as the reviewer says: the cards use "B. Evetts" at first mention and "Evetts" after". R2 said the opposite: "B. Evetts" appears throughout. In fact the Michael card uses "B. Evetts" in all three prose mentions. The Alexander card uses "B. Evetts" three times and "Evetts's 1895 English" once, in `place`. The card text is acceptable. The audit log, which is a lasting record, describes it wrongly twice.
Fix (in the R3 changes log, since R2_changes is a closed round record): "The R1 and R2 change logs describe the Evetts forms wrongly. The cards use "B. Evetts" in prose throughout, except "Evetts's 1895 English" once in Alexander's place field. "B. T. A. Evetts" stays only in the 1895 source title."

---

### Listener read (all four briefs, start to end)

- Alexander: reads as a story. The restored flight sentence makes the boat quote and the death at Tarnut connect. Nothing generated-sounding.
- Michael: sound. The close, "a martyr who shed no blood", could be heard as "who shed no one's blood". The card has the plainer "a martyr without the shedding of blood". This is unchanged and not counted.
- Joseph: sound apart from R3-2-M4. "Both Synaxaria" is clear, because both have already been named in paragraphs 1 and 2.
- Severus: sound apart from R3-2-M7. "Little else of his life is recorded" is an honest limit tied to Renaudot. It is not a tail.

### Scores

| Brief | Words | FK | Flesch | Approx. time @162 |
|---|---|---|---|---|
| alexander-ii-of-alexandria | 366 | 6.03 | 72.94 | 2:16 |
| michael-i-of-alexandria | 362 | 6.59 | 71.70 | 2:14 |
| joseph-i-of-alexandria | 362 | 7.04 | 66.88 | 2:14 |
| severus-ibn-al-muqaffa | 346 | 6.52 | 72.12 | 2:08 |

All four pass `grade_text`. All four sit below the grade 8 floor, which is a rhythm signal and not a gate failure. All four audio scripts equal their briefs plus `[calmly]` at the start and `[warmly]` before the last paragraph. No tag appears in a brief, card or records row. With the fixes above, Joseph scores FK 7.07 and Flesch 66.65, and Severus FK 6.55 and Flesch 71.94.

### Final counts (Part 2)

- Round 2 findings in scope: 11 (R2-2-B1, R2-2-A-M1 to A-M5, R2-2-M-M1, R2-2-J-M1, J-M2, R2-2-S-M1, S-M2), plus the round 1 PARTLY items B-B4 and B-M1. APPLIED: 10 of the 11, and both PARTLY items are closed. PARTLY: 1 (R2-2-B1: wording right, but its last two sentences were made a separate bullet). NOT APPLIED: 0.
- New blocking: 0.
- New minor: 8 (Alexander 2: M1, M2; Michael 1: M3; Joseph 2: M4, M5; Severus 2: M6, M7; audit log 1: M8). M7 and the `dates` half of M3 are in unchanged text, seen in passing. M5, M6 and M8 are not participant-facing.
