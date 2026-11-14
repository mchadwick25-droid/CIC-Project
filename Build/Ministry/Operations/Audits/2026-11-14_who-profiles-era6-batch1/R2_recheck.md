# R2 recheck: era 6 batch 1

Round 2, a targeted recheck by two fresh Opus agents that had not seen the drafting or round 1's reviewing, at full effort. Part 1 covers John Wyclif, Thomas à Kempis, Geert Grote and the README (round 1 Parts A and B); Part 2 covers Richard Rolle, Julian of Norwich, Meister Eckhart, Johannes Tauler and Henry Suso (round 1 Parts C and D). Each part is given as its reviewer wrote it. In all, 3 blocking and 33 minor points.

## Era 6 Who batch 1, round 2 recheck: PART 1

**Scope.** `john-wyclif`, `thomas-a-kempis` and `geert-grote` (brief, card, audio script and each `records.json` entry), the batch `README.md`, and every round 1 finding in Parts A and B of R1_review.md (A-B1 to A-B3, A-M1 to A-M31, K-M1 to K-M14, G-B1, G-M1 to G-M6, R-M1 to R-M3). I also checked R1_changes.md's Part A and Part B entries against the diff. I edited no repo file and made no web, paid or model call.

**Method.**
- **Reading.** CLAUDE.md ("Trust and source fidelity", "Accessible and rigorous"), `Who_Profile_Pattern.md` and its 14-item checklist, lessons.md (above all section 14), the era 4 batch 8 R2 form, R1_review.md Parts A and B, and R1_changes.md.
- **Diffs.** `git diff --word-diff d3b9aa04 HEAD` on the batch. For `records.json` I compared the three entries item by item between d3b9aa04 and HEAD by script.
- **Sources.** For every changed string I reopened its lines in context: Vaughan (l.4755-4768, 7262-7264), Shirley (l.2690-2700, 2740-2750), Forshall and Madden (l.1024-1032, 3430-3438, 4068-4077), Knighton (l.6014-6015, 16928-16936), Pollard (l.7200-7208), Matthew (l.378-392), Arnold vol. 3 (l.1-12, 70-76), Foxe vol. 3 (l.4902-4991, 7905-7965, 8018-8046), Mansi 27 (l.95-145, 65540-65565), the Scripta de Sancto Ignatio (l.10060-10072, 24010-24016, 24285-24348), the Chronicle (l.1095-1108, 1976-2030, 2327-2382, 3778-3812), the Lives (l.2080-2096, 3808-3824, 3880-3892, 5980-5992, 4218-4228, 12800-12814), Busch (l.5405-5430), Benham (l.500-512, 620-640), Ingram (l.298-318), Neale (l.3744-3762, 4714-4722), Wesley (l.955-968), Duthoit (l.46-48, 756-778, 920-970), Pohl (l.108-111) and Acquoy (l.1730-1740, 4668-4684).
- **Quotes.** Every new or changed quotation in the briefs, cards and records was checked by script against its file, with whitespace, case, punctuation and hyphen line-breaks allowed for. All match. Two need an OCR allowance, and the records note both: Manare's "s^cretiori" and "libroruro", and Pohl's "lOSEPHVS".
- **Absences.** I searched all of `cic/texts/` with whitespace-tolerant patterns for "most copied", "partridge"/"perdicem", "Bethany"/"Bethania", "Christian Pattern", "Stanhope", "Stuerman", "pestilence"/"plague" in the Kempis files, and "infect"/"caught"/"pulse" in Kempis's Grote chapters.
- **Scores.** `grade_text` on each brief, word counts by `str.split()`, sentence lengths by script on the briefs and on every card string. I also scored each brief with the fixes below applied.
- **Audio.** Each script was compared by script with its brief, plus `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph.
- **Writing.** I read every changed sentence and its neighbors for the section 9 and section 14 patterns.

---

### Round 1 findings

| R1 finding | Status | Note |
|---|---|---|
| A-B1 | RESOLVED | The card now has "His heading for the decree gives A.D. 1425. In Foxe's own English, the council's decree orders the bones dug up and thrown far from any church burial. It says nothing of burning." FOXE3 l.7945-7948 and MANSI27 l.65559-65561 say this. Neither has any word of burning. The records cite both and note that the "not yet commanded" note goes with the 1406 testimonial. |
| A-B2 | RESOLVED | The detail is retitled. Its note names Shirley's judgment, Foxe's 1406 testimonial and its disputed authenticity (FOXE3 l.4914, 4982-4986), and Thorpe. |
| A-B3 | RESOLVED | Manare's trace is on the card, the records claim cites IGN-SCR1 l.24338-24347 and 10068, and the README line is true. On the trace's wording, see R2-1-M11. |
| A-M1 | RESOLVED | "and called his judges the heretics. When Christ's members fail to cry out against them". The records claim matches. |
| A-M2 | RESOLVED | Shirley now carries "drawn from his writings" (SHIRLEY l.2697-2698, "extracted from his writings"). |
| A-M3 | RESOLVED | The who-line is now sentence 2. Its Knighton witness is a new records claim (KNIGHTON l.16932-16934). |
| A-M4 | RESOLVED | "letters, called bulls". The same sentence's "his conclusions" can be heard as the pope's; see R2-1-M1. |
| A-M5 | PARTLY | The brief and card are fixed. The records claim still reads "Knighton a Leicester chronicler, hostile", tagged Documented; see R2-1-M8. |
| A-M6 | RESOLVED | Matches VAUGHAN l.7262-7264. There is a records claim for it. |
| A-M7 | RESOLVED | The text matches SHIRLEY l.2745-2747, VAUGHAN l.4761-4763 and F&M l.1030-1031. To make room, the St Paul's sentence and the two Knighton sentences on the English gospel were cut. That cut left the Wycliffite Bible unexplained; see R2-1-M2. |
| A-M8 | PARTLY | It is attributed now, but "Why should men not do so now, he asked." is a direct question with a full stop; see R2-1-M4. |
| A-M9 | RESOLVED | It is two sentences now. The split leaves "He" (Pollard) just before "a stroke took his speech"; see R2-1-M3. |
| A-M10 | RESOLVED | As worded. It is 25 words. |
| A-M11 | RESOLVED | The item, the contested side and the claim (MATTHEW l.380-390) are all there. "places his birth" can be heard as Matthew's own birth; see R2-1-M6. |
| A-M12 | RESOLVED | "as, it was said, he meant to preach". |
| A-M13 | RESOLVED | The text is as worded, but "Shirley says he appeared" can be heard as Shirley; see R2-1-M6. |
| A-M14 | RESOLVED | "Protestant" is gone. The records claim covers FOXE3 l.7962 and 8023. |
| A-M15 | RESOLVED | Two sentences. |
| A-M16 | RESOLVED | Arnold is placed (ARNOLD3 l.1, 73), and so is Purvey (F&M l.3434-3435, 4071-4075). |
| A-M17 | PARTLY | The gloss is in. The sentence is now 27 words, the bare "Pollard" comes before Alfred Pollard is placed, and "divine" is heard as an adjective; see R2-1-M5. |
| A-M18 | RESOLVED | "modernized" in both places. Mansi is named on the title page (MANSI27 l.101) and dated "VENETIIS MDCCLXXXIV" (l.136) with the 1902 reissue line (l.143), so the author and date are held. |
| A-M19 | RESOLVED | De Civili Dominio is in ownWords, and the brief has "God's gift". |
| A-M20 | RESOLVED | "parish priest" is in knownFor, role and the brief. knownFor's first sentence is now 26 words; see R2-1-M7. |
| A-M21 | RESOLVED | All four labels name a question. |
| A-M22 | PARTLY | The claim is fixed (l.874-875). The contested_claim side "His early Oxford years" still cites "SHIRLEY l.737-805, 870-871, 972-977"; see R2-1-M8. |
| A-M23 | RESOLVED | "The scan's year c.1330". |
| A-M24 | RESOLVED | The Courtenay claim cites KNIGHTON l.6014-6015. |
| A-M25 | NOT RESOLVED | `Open-Gaps.md` at HEAD still has no era 6 batch 1 entry (last entry 262, era 4 batch 8). README l.5 still says the points "are logged in Open-Gaps". R1_changes says the entry "is registered", which is not so. Fix: log the entry now. Otherwise write "those points are to be logged in Open-Gaps for a census fix", the era 4 batch 7 form. |
| A-M26 | RESOLVED | Words 402 to 405, grade 5.5 to 8.1, Flesch 63.8 to 80.9. All three ranges match `grade_text` across the eight briefs (low: Rolle 402, Julian FK 5.53, Wyclif Flesch 63.77; high: Julian 405, Wyclif FK 8.14, Julian Flesch 80.91). |
| A-M27 | PARTLY | The added "Poole's De Civili Dominio" is in the scan row (WYC-CIV, Who_Scan_Era6.md l.80, decoded at l.370); see R2-1-M18. |
| A-M28 | RESOLVED | The Grote reason is as worded. The Eckhart fix left "his trial" named twice in one sentence; see R2-1-M19. |
| A-M29 | RESOLVED | The four Contested items match the Eckhart contested_claims (retraction, birth, Frankfurt, before 1326). |
| A-M30 | PARTLY | Middle English is added, and so are Shirley, Foxe and Neale. The list still leaves out quoted held English on the cards: Benham, Ingram and Wesley on Kempis, and Underhill on Grote and Rolle. It also misses Hodgson's Form of Living in the Rolle brief, Lea, Curnock, Cressy and the 1608 Martyrologe. See R2-1-M20. |
| A-M31 | RESOLVED | It now sets the two sides against each other, and the Knighton sentence matches the brief. |
| K-M1 | RESOLVED | "Thomas à Kempis" at first mention. |
| K-M2 | PARTLY | Book and founder are one sentence now, but "With Florens's help", the link to the choir scene (FOUNDERS l.12809-12810), was cut for length. The paragraph still runs name, lodging, writing with no link. It reads acceptably at the cap. If words are freed, restore it: "With Florens's help he lived about a year in the brothers' house at Deventer." |
| K-M3 | PARTLY | The brief and card say "indulgences". The records claim on 1399 still says "The brief's 'pardons the pope had granted' tells …"; see R2-1-M14. |
| K-M4 | RESOLVED | `"I was received with mercy", he says.` matches CHRON l.1105. |
| K-M5 | PARTLY | The concession is in, but Benham's "somewhat" is dropped, and the brief's "is uncertain" differs from the card's "grows uncertain"; see R2-1-M10. |
| K-M6 | RESOLVED | "Years after that dream" holds: John's death comes under 1432, between 1431 and 1433 (CHRON l.1971, 1981, 2010, 2029). But "Bethany" is now heard with no place; see R2-1-M9. |
| K-M7 | RESOLVED | "His Chronicle records that he was clothed…" (CHRON l.1189-1193). |
| K-M8 | PARTLY | The card is right: CHRON l.2378-2380, "sixty-seven years of age", in Thomas's own part. But the records witness leaves out the line that gives the year, "In the year of the Lord 1448" (CHRON l.2327); see R2-1-M14. |
| K-M9 | RESOLVED | "The day he died" is an item of its own, with both witnesses. |
| K-M10 | RESOLVED | "laboring". |
| K-M11 | RESOLVED | The name "Michael Joseph Pohl" rests on POHL l.110 and DUTHOIT l.47. The header witness is gone. |
| K-M12 | PARTLY | All three names are placed, but the Rosweide fix made "Benham says" twice in one sentence (R2-1-M13), and the Ignatius sentence is 27 words (R2-1-M12). R1_changes calls the Hilton fix "as worded", but it was split into two sentences. The split is sound on its merits. |
| K-M13 | PARTLY | The card is fixed. The records range stops at l.965, but "much sensible comfort in reading him" is at WESLEY l.967-968. No witness yet ties the "Christian Pattern" to the Imitation; see R2-1-M14. |
| K-M14 | RESOLVED | "Which telling of the 1424 dream came first." |
| G-B1 | PARTLY | The brief, the card's first sentence and the records are fixed, and "Busch alone" holds. The card's next sentence, R1's own wording, is a false "only": Kempis's Chronicle records the plague. See R2-1-B1. |
| G-M1 | RESOLVED | "He wrote Grote's Life, he says, from what men and women who knew Grote told him" (FOUNDERS l.2085-2093). |
| G-M2 | RESOLVED | The paragraphs are joined and the witness is named. The new "Kempis's Chronicle says he" is heard as Kempis; see R2-1-M15. |
| G-M3 | RESOLVED | "at the end of Kempis's Life" (FOUNDERS l.4221-4223). On the pronoun "His", see R2-1-M16. |
| G-M4 | RESOLVED | The doublet is gone. |
| G-M5 | RESOLVED | Acquoy's "ex iis … postquam ei interdictum erat praedicare" (GROOTE l.4676-4677) is plural, so "letters written after his preaching was stopped" holds. |
| G-M6 | RESOLVED | The absent_details entry is added (DIEP l.467-468). |
| R-M1 | NOT RESOLVED | As A-M25. |
| R-M2 | RESOLVED | As worded. The Grote card's "John Vos of Heusden" matches. |
| R-M3 | RESOLVED | Both census entries are added, with the right lines (CHRON l.1103-1106, 3419-3421, 1885-1924, 2023-2026). |

### New findings

**R2-1-B1 (geert-grote, card `uncertain[0]`: a false "only", and "smitten"). Blocking.**
- Bad text: "Kempis says only that Grote ruled that those who lived together should earn their living by their hands, and that he was smitten."
- Evidence:
  - Kempis's Chronicle says Grote "died at Deventer, in the time of the pestilence" (CHRON l.3784-3786). The card's own `dates` field says so: "in a time of plague, Thomas à Kempis records." So Kempis says more than "he was smitten".
  - What Kempis does not say is how Grote caught it. Neither his Chronicle nor his Lives has a pulse, a friend or infection near Grote's death (searched CHRON l.3770-3900 and FOUNDERS l.3800-3960).
  - The sentence also drops half of the rule: "they should earn their own living by the labour of their hands, and, as far as might be, live in common" (FOUNDERS l.3818-3821). "Live in common" is the point of the item.
  - A listener hears "smitten" in its modern sense, infatuated. It stands for Arthur's "smitten by the bolt that must fall upon all men" (FOUNDERS l.3886-3888).
  - A false "only" is blocking wherever it sits (lessons, sections 1 and 3).
- Fix: "Kempis gives Grote's rule that those who wished to live together should earn their living by their hands and live in common. He records that Grote died in a time of plague, and does not say how he caught it." (22 and 19 words.)

**R2-1-M1 (john-wyclif, brief para 2: "his conclusions" heard as the pope's).**
- Bad text: "In 1377, Shirley says, Pope Gregory XI sent letters, called bulls, that condemned nineteen of his conclusions and ordered his arrest."
- Evidence: the nearest man is Gregory XI. SHIRLEY l.1835-1842 has the bulls condemn Wyclif's conclusions and order Wyclif's arrest.
- Fix: "…that condemned nineteen of Wyclif's conclusions and ordered his arrest." The word count stays the same.

**R2-1-M2 (john-wyclif, brief para 4: the cut left the Wycliffite Bible unexplained).**
- Bad text: "Josiah Forshall and Frederic Madden, who edited the Wycliffite Bible in 1850, thought its New Testament was probably Wyclif's own."
- Evidence: the A-M7 cut took out Knighton's complaint that Wyclif "turned the gospel into English". That was the brief's only sign that the Wycliffite Bible is a translation into English. A listener now hears "Wyclif's own" with no idea of what.
- F&M's own subject is the English versions ("the versions of the Wycliffite Bible", the card's trace, F&M l.2319). The README promises "The Wycliffite Bible is told as the circle's work", and that work is a translation.
- Fix: "Josiah Forshall and Frederic Madden, who edited the English Wycliffite Bible in 1850, thought its New Testament was probably Wyclif's own translation." This adds 2 words and brings the brief to 405, at the cap.

**R2-1-M3 (john-wyclif, brief para 5: "his speech" after "Shirley says").**
- Bad text: "On 29 December, Shirley says, a stroke took his speech as he heard Mass in his parish church."
- Evidence: the paragraph opens straight after Pollard ("He says historians admit…"). The first man named in it is Shirley. A-M9's split made Pollard the last "He". SHIRLEY l.2745-2747 is about Wyclif.
- Fix: "On 29 December, Shirley says, a stroke took Wyclif's speech as he heard Mass in his parish church." The word count stays the same.

**R2-1-M4 (john-wyclif, brief close: a direct question ended with a full stop).**
- Bad text: "Why should men not do so now, he asked."
- Evidence: this is A-M8's wording. A direct question needs a question mark, and with no quotation marks (Middle English told in modern words) the tag cannot sit after one cleanly. MATTHEW l.35793-35795 is a question.
- Fix: "He asked why men should not do so now." The word count stays the same.

**R2-1-M5 (john-wyclif, card `remembered[0]`: 27 words, Pollard unplaced, and "divine").**
- Bad text: "He told Arundel that Wyclif "was holden of full many men, the greatest Clerk" they then knew, a word Pollard glosses as divine, a scholar of theology. Alfred Pollard printed the Examination in modern spelling in 1903."
- Evidence:
  - The first sentence is 27 words.
  - The bare "Pollard" comes one sentence before he is placed (lessons, section 14, "names left unplaced at first card mention").
  - Spoken, "divine" is heard as the adjective. Pollard's own gloss is the noun "[Divine]" (POLLARD l.7205).
- Fix: "He told Arundel that Wyclif "was holden of full many men, the greatest Clerk" they then knew. Alfred Pollard, who printed the Examination in modern spelling in 1903, glosses "Clerk" as "Divine", a scholar of theology." (16 and 19 words.)

**R2-1-M6 (john-wyclif, card `uncertain`: two pronouns captured by the witness).**
- Bad text 1 ("When he was born"): "F. D. Matthew, in 1880, calls the date and place alike uncertain and places his birth about 1320." It can be heard as Matthew's own birth.
  - Fix: "…and places Wyclif's birth about 1320."
- Bad text 2 ("The date and aim of the St Paul's hearing"): "Shirley says he appeared on 23 February." This was A-M13's wording.
  - Fix: "Shirley says Wyclif appeared on 23 February." (SHIRLEY l.1685-1686.)

**R2-1-M7 (john-wyclif, card `knownFor`: 26 words after the A-M20 change).**
- Bad text: "Oxford doctor of theology and parish priest of Lutterworth whose teaching was denounced in papal letters of 1377 and condemned by a London synod in 1382."
- Evidence: "rector" became "parish priest", which took the sentence from 25 words to 26.
- Fix: "Oxford doctor of theology and parish priest of Lutterworth. His teaching was denounced in papal letters of 1377 and condemned by a London synod in 1382."

**R2-1-M8 (john-wyclif, records: two items not brought into line).**
- The contested_claim "His early Oxford years…", Shirley's side, still cites "SHIRLEY l.737-805, 870-871, 972-977". Lines 870-871 are the page head that A-M22 corrected in the claim. Fix: "SHIRLEY l.737-805, 874-875, 972-977".
- The claim "Knighton a Leicester chronicler, hostile: …" is tagged Documented. It tells Knighton's authorship as settled, while the contested_claim "Whether the Leicester chronicle's account of Wyclif is Henry Knighton's" disputes it. The brief and card were fixed under A-M5; this claim was not. Fix: retitle it "The Leicester chronicle under Knighton's name, hostile: …". Keep Documented for the manuscript title and the hostile lines.

**R2-1-M9 (thomas-a-kempis, brief para 6 and card `place`: "Bethany" with no place).**
- Bad text: brief, "Years after that dream, Thomas was sent to Bethany to keep his aged brother John company." Card `place`, "Bethany, where his brother John died."
- Evidence:
  - The K-M6 fix brought Bethany into the brief. With no place given, a listener hears the Bethany of the Gospels.
  - The Chronicle calls it "the House of Bethany" (CHRON l.2022, 2026-2027) and does not say where it is. William Duthoit, already on the card, places it: John "died in 1432 at one of them, the convent of Bethania near Arnheim" (DUTHOIT l.761-763). He also has Thomas "sent to Bethania, to attend his brother" (l.773).
- Fix, brief: "Years after that dream, Thomas was sent to Bethany, a house near Arnhem, to keep his aged brother John company." This adds 4 words. To stay at the cap:
  - Para 3: "to gain indulgences, remissions of penance that the pope had granted there" becomes "for indulgences, remissions of penance the pope had granted there" (-2).
  - Para 2: "Thomas's own Chronicle names him" becomes "Thomas's Chronicle names him" (-1). That is the form before round 1.
  - Para 4: "One had a dream that, the Chronicle says, foretold the prior's death, but it leaves the dreamer unnamed." becomes "The Chronicle says one had a dream that foretold the prior's death, and leaves the dreamer unnamed." (-1). This also clears the "it", which can be heard as the dream.
  - With R2-1-M10, the brief comes to 405 words, FK 7.18, Flesch 69.86.
- Fix, card: "Bethany, a convent near Arnhem in William Duthoit's account, where his brother John died."
- Records: add DUTHOIT l.761-763, 773 to the Brother John claim (CHRON l.2012-2026).

**R2-1-M10 (thomas-a-kempis, brief para 5 and card `uncertain[1]`: Benham's "somewhat" dropped, and two wordings for one concession).**
- Bad text: brief, "though he grants the ground is uncertain"; card, "though he grants that the ground grows uncertain."
- Evidence: "But when we seek to investigate further, it must be confessed that our ground becomes somewhat uncertain" (BENHAM l.634-636). "Is uncertain" makes his concession stronger than he makes it. The brief and the card should also not give his hedge in two forms (item 9).
- Fix: brief, "though he grants the ground grows somewhat uncertain" (+1, offset under R2-1-M9). Card, "though he grants that the ground grows somewhat uncertain."

**R2-1-M11 (thomas-a-kempis, card `traces[3]`, Manare: "ordinarie" dropped, and "He" heard as Manare).**
- Bad text: "He writes in Latin that Ignatius kept no books on the table of his inner room but the New Testament and Thomas à Kempis. He called Thomas, Manare says, the partridge of spiritual books."
- Evidence:
  - "in cubiculo suo secretiori ordinarie super mensam alios libros non habebat" (IGN-SCR1 l.24342-24345, OCR "s^cretiori"). Manare's "ordinarie", usually, is dropped. The card makes the rule absolute.
  - "solebat appellare", he used to call it (l.24346), is told as a single act.
  - The second "He" comes right after "He writes", where He is Manare. So the listener first hears Manare calling Thomas a partridge, and "Manare says" then reverses it.
- Fix: "He writes in Latin that Ignatius usually kept no books on the table of his inner room but the New Testament and Thomas à Kempis. Ignatius used to call Thomas à Kempis, Manare says, the partridge of spiritual books." (25 and 14 words.)

**R2-1-M12 (thomas-a-kempis, card `traces[1]`: 27 words after the K-M12 fix).**
- Bad text: "Ignatius of Loyola, telling the story of his life to Consalvius de Cámara, said in Spanish that at Manresa he first saw the Gerconzito, the little Gerson."
- Fix: "Ignatius of Loyola told the story of his life to Consalvius de Cámara. In Spanish he said that at Manresa he first saw the Gerconzito, the little Gerson." The editors' "res a se gestas Consalvio enarrans" (IGN l.2600) supports the first sentence.

**R2-1-M13 (thomas-a-kempis, card `uncertain` "The Bible he copied": "Benham says" twice in one sentence).**
- Bad text: "Benham says it took fifteen years, and that one Rosweide, Benham says, saw it at Cologne with a closing note dated 1439."
- Evidence: the K-M12 wording was dropped into a sentence that already opens with "Benham says". BENHAM l.506-510 holds both points.
- Fix: "Benham says it took fifteen years, and that one Rosweide saw it at Cologne with a closing note dated 1439."

**R2-1-M14 (thomas-a-kempis, records: a stale note, short ranges, a missing witness, an over-wide absence, and process wording).**
- The 1399 claim still ends: "The brief's 'pardons the pope had granted' tells 'Indulgences ... by the Apostolic See' in modern words." The brief has said "indulgences" since K-M3.
  - Fix: "The brief keeps 'indulgences' and glosses them as remissions of penance."
- The Wesley claim cites "WESLEY l.961-965", but the new quotation "much sensible comfort in reading him" is at l.966-967. No witness ties "Kempis's Christian Pattern" to the Imitation, as the card now does.
  - Duthoit's preface quotes a translator on "Castalio and Dean Stanhope … in their versions of the 'Imitation of Christ'" (DUTHOIT l.927-929) and "Dr. Stanhope's words in his preface to the 'Christian Pattern'" (l.963-964). Wesley read Kempis "only in Dean Stanhope's translation" (WESLEY l.966).
  - Fix: add the comfort quotation to the claim. Make the witness "WESLEY l.961-968; DUTHOIT l.927-930, 963-964", and note that Stanhope's Christian Pattern is his version of the Imitation.
- The birth claim cites CHRON l.2378-2380 for "sixty-seven" in 1448. The year is at l.2327 ("In the year of the Lord 1448"). Fix: "CHRON l.2327, 2378-2380".
- The absent_details note on "the most copied" twice says that no line "says 'copied'". That is untrue as written: BENHAM l.505 has "He copied the Bible", and the brief itself says "Thomas copied it". The only "most copied" is the Benham file's header (l.14; searched all of `cic/texts/`).
  - Fix: "The census says so; no held line calls it the most copied book. The nearest lines are Neale's 'read more widely' (NEALE l.4717-4719) and Benham's 'most popular' (BENHAM l.663-664). Neale adds that it 'has, it is said, gone through as many editions as there have been months since it first appeared' (NEALE l.4719-4721)."
- The absent_details note on the desk ends "The census wording 'desk' is close enough; its source is now named." That is change narration (lessons, section 11). Fix: "The census's 'desk' is Manare's table."

**R2-1-M15 (geert-grote, brief para 3: "Kempis's Chronicle says he" heard as Kempis).**
- Bad text: "Kempis's Chronicle says he gave his Deventer house to poor sisters he had gathered."
- Evidence: the G-M2 fix put the witness first, so "he" now follows "Kempis's". CHRON l.3803-3809 is about Grote.
- Fix: "Kempis's Chronicle says Grote gave his Deventer house to poor sisters he had gathered." The word count stays the same.

**R2-1-M16 (geert-grote, brief close: "His own notes" after Florens).**
- Bad text: "Both writers say Grote named Florens to lead the brothers. / His own notes, at the end of Kempis's Life, put…"
- Evidence: the last man named is Florens, and the closing paragraph opens on "His". The G-M3 rewrite of this sentence kept the pronoun. FOUNDERS l.4221-4223 gives Gerard's notes.
- Fix: "Grote's own notes, at the end of Kempis's Life, put…" The word count stays the same.

**R2-1-M17 (geert-grote, brief para 7: "tells the talk").**
- Bad text: "Only Busch tells the talk that began the common life."
- Evidence: this is the G-B1 wording. "Tell" takes a story or an account, not a talk. The phrase is heard as a slip.
- Fix: "Only Busch tells of the talk that began the common life." (+1, to 404 words.)

**R2-1-M18 (README, "Held witnesses beyond those the scan cites", Wyclif: Poole is in the scan).**
- Bad text: "…Foxe, with the Oxford testimonial of 1406; Poole's De Civili Dominio."
- Evidence: the scan row lists WYC-CIV among the own corpus (Who_Scan_Era6.md l.80). Line 370 decodes it: "WYC-CIV = wyclif_de-civili-dominio-liber-primus-lat_poole1885.txt".
- Fix: "…Mirbt on Inter cunctas; Foxe, with the Oxford testimonial of 1406." R1_changes lists A-M27 as "Applied as worded", but these two items were added beyond the wording.

**R2-1-M19 (README, "Card traditions", Eckhart: the trial twice in one sentence).**
- Bad text: "Eckhart's trial, 1326 to 1329, and the deaths of Tauler in 1361 and Suso in 1365 or 1366 fall inside its years; Eckhart's birth falls before; his Paris mastership of 1302 and his trial fall inside."
- Fix: "Eckhart's trial, 1326 to 1329, his Paris mastership of 1302, and the deaths of Tauler in 1361 and Suso in 1365 or 1366 fall inside its years; Eckhart's birth falls before."

**R2-1-M20 (README, quotation paragraph: the list of quoted English is still incomplete).**
- Bad text: "Quotation marks are kept for held English: the Chronicle and the Lives in Arthur's English, Knox's Suso, …, Vaughan's, Pollard's, Shirley's and Foxe's Wyclif, Neale's Kempis."
- Evidence: the cards also quote these, each held in English:
  - Benham, Ingram and Wesley on Kempis.
  - Underhill on Grote and on Rolle.
  - Lea on Eckhart.
  - Curnock on Tauler.
  - Cressy's title, and the 1608 Martyrologe in Comper.
  - The Rolle brief quotes Hodgson's Form of Living.
- Fix: "Quotation marks are kept only for lines held in English, among them the Chronicle and the Lives in Arthur's English, Knox's Suso, Warrack's and Harford's Julian, Comper's and Hodgson's Rolle, Winkworth's Tauler, Evans's Eckhart, and Vaughan's, Pollard's, Shirley's and Foxe's Wyclif."

**R2-1-M21 (R1_changes.md: four entries misdescribe the change).**
- A-M7: "two sentences were cut from the brief". Three were cut: the St Paul's sentence and both Knighton sentences ("Knighton also complains…" and "So the gospel's pearl…").
- A-M25 and R-M1: "The Open-Gaps entry is registered". No entry exists at HEAD.
- A-M27: "Applied as worded". Two items were added (R2-1-M18).
- K-M7 to K-M14: "Applied as worded". The K-M12 Hilton fix was split into two sentences.
- Fix: R1_changes.md is a lasting audit file, so do not rewrite it. Record each correction in R2_changes.md.

### Checks that pass, beyond the table

- **Audio.** All three scripts equal their briefs, with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph, and only two tags. The other five scripts also match.
- **Quotations.** Every new or changed quotation matches its file (method above). These include Wesley's four pieces, "I was received with mercy", the Chronicle's 1448 "sixty-seven years of age", Kempis's rule and the "Common table", Matthew's birth sentence, the Foxe decree and editors' note, Vaughan's "agent of insurrection" and "said to have been employed", F&M's "last day of December 1384", and Neale's "editions as … months".
- **False absences.** I re-checked every new "only", "alone" and "nothing" in scope:
  - "Busch alone says Grote caught the plague": Stuerman appears only in Busch and in Arthur's bequest note.
  - "Only Busch tells the talk": FOUNDERS l.1173-1178 is Arthur citing Busch.
  - "It says nothing of burning": neither FOXE3 l.7945-7948 nor MANSI27 l.65559-65561 has one.
  - README "No held line says 'most copied'": only the Benham header has it.
  - The one false "only" I found is R2-1-B1.
- **Witnesses.** Each changed brief sentence keeps its witness. Shirley carries "drawn from his writings". Vaughan carries the bread, as a report. F&M carry the year. Kempis's Chronicle carries the house and the deaconate, and "he writes" follows into the dream paragraph. Pollard is placed in the brief.
- **Cuts.** No scene was lost from the three briefs. The Wyclif cuts take out the St Paul's hearing (one sentence; the card keeps it with all three sides) and Knighton's complaint about the English gospel (the card keeps Knighton's side under "Whose Bible it was"). The story still runs synod, Oxford, the bulls, the sacrament, the rising, the Bible, death, close. Only R2-1-M2 needs mending. The Kempis and Grote cuts are small and leave every turning point.
- **Card form.** Field order is unchanged and every card witness is in `sources`. The new entries (De Civili Dominio, Matthew's introduction, Mansi, Manare's volume) have title, author, date, language and file. "a Jesuit from 1551" rests on IGN-SCR1 l.10067-10068 ("ingressus in Societatem 1551"). American spelling holds outside quotations.
- **README claims.** These are true against the files as they now stand: the Kempis bullet's Manare and Neale lines, the Grote held-witness line on Neale (NEALE l.3753-3754 gives Kampen and Gouda), the Wyclif names line, the Grote tradition reason (BUSCH l.310, 1374), and the Eckhart Contested list.
- **R1_changes.** Apart from R2-1-M21, the Part A and Part B entries match the diff, and the table of scores matches `grade_text` and `str.split()`.

### Scores

| Brief | Words | FK | Flesch | After fixes: words / FK / Flesch | Blocking | Minor |
|---|---|---|---|---|---|---|
| john-wyclif | 403 | 8.14 | 63.77 | 405 / 8.29 / 62.84 | 0 | 8 (M1 to M8) |
| thomas-a-kempis | 404 | 7.09 | 70.44 | 405 / 7.18 / 69.86 | 0 | 6 (M9 to M14) |
| geert-grote | 403 | 5.63 | 79.26 | 404 / 5.66 / 79.09 | 1 | 3 (M15 to M17) |
| README / R1_changes | | | | | 0 | 4 (M18 to M21) |

Every brief passes `grade_text` before and after the fixes. No brief sentence goes past 25 words, except the Kempis close (31 words). That sentence is unchanged and mostly quotation. With the fixes applied, no changed card sentence goes past 25 words. After any edit, rebuild the audio scripts from the briefs.

### Count

- **Round 1 findings in scope: 58.**
  - Resolved: 43.
  - Partly resolved: 13 (A-M5, A-M8, A-M17, A-M22, A-M27, A-M30, K-M2, K-M3, K-M5, K-M8, K-M12, K-M13, G-B1).
  - Not resolved: 2 (A-M25 and R-M1, the Open-Gaps entry).
- **New blocking: 1.** R2-1-B1, Grote: the false "only" on what Kempis says.
- **New minor: 21.** R2-1-M1 to R2-1-M21.

**Files reviewed** (under /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/):
- john-wyclif.brief.txt, john-wyclif.card.json, audio/john-wyclif.audio.txt
- thomas-a-kempis.brief.txt, thomas-a-kempis.card.json, audio/thomas-a-kempis.audio.txt
- geert-grote.brief.txt, geert-grote.card.json, audio/geert-grote.audio.txt
- records.json (john-wyclif, thomas-a-kempis, geert-grote)
- README.md

These were also read: /home/user/CIC-Project/Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era6-batch1/R1_review.md and R1_changes.md; /home/user/CIC-Project/Build/Ministry/Operations/Audits/2026-11-12_who-scan-era6/Who_Scan_Era6.md (l.80, 89, 370); /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md (searched).


---

## Era 6 Who batch 1, round 2 recheck: PART 2

**Scope.** I rechecked `richard-rolle`, `julian-of-norwich`, `meister-eckhart`, `johannes-tauler` and `henry-suso`: the brief, the card, the audio script and the records.json entry for each, with the README lines on them. I checked every round 1 finding in Parts C and D (C-B1, C-M1 to C-M21, D-B1 to D-B3, D-M1 to D-M25). I edited no repo file and made no web, paid or model calls.

**Method.**
- **Reading.** CLAUDE.md ("Trust and source fidelity", "Accessible and rigorous"); Who_Profile_Pattern.md and its 14-item checklist; lessons.md, above all section 14; R1_review.md Parts C and D; R1_changes.md; the era 4 batch 8 R2_recheck.md as the form model.
- **Diffs.** `git diff --word-diff d3b9aa04 HEAD` on the five briefs, the five cards, records.json (the five entries) and README.md.
- **Sources reopened in context.** COMPER l.1740-1800 (Lections II-III), 2036-2110 (Lection VIII), 130-152 and 14185-14205 (the 1914 imprint); HARFORD l.1150-1190; WARRACK l.262-282, 2084-2092, 2600-2610; DALGAIRNS l.205-216, 1770-1830, 2828-2880; GARDNER l.254-257, 575-580; EVANS l.325-382, 445-455, 490-512, 668-700; PFEIFFER l.360-372, 455-462; WINK l.4238-4262, 5120-5180; KNOX l.1330-1346, 3478-3504, 3755-3775, 5363-5367; BIHL l.6655-6680, 8290-8298; LITTLE l.725-760, 870-955; CRAFT l.258-266; SPENER l.114-127; DANIELS l.42-52.
- **Searches.** Every new "alone", "only" and "no ground" was searched across all of `cic/texts/`, case-insensitive and whitespace-tolerant: Tauler with 1361, June, Juni, starb, died, Strasbourg and its spellings; Dalgairns and 1443; "vital and individual"; Preger and Seeberg in Bihlmeyer; Henry of Nördlingen with priest and Priester.
- **Quotes.** I checked every quoted string in the five briefs and cards by script (lowercase, letters and digits only, hyphen line-breaks joined) against the cited files. All match except the two Julian lines with the edition's footnote marks, which the records note (HARFORD l.1161 "unlearned,13"; WARRACK l.3818-3819 "sin;[1]"). The Rolle card's Underhill line has double spacing in its file (UNDERHILL-H l.70) and matches by eye.
- **Scores.** `grade_text` on each brief; word counts; sentence lengths by script for the briefs and every card string.
- **Audio.** I rebuilt each script from its brief and compared.

---

### Round 1 findings

| R1 finding | Status | Note |
|---|---|---|
| C-B1 | RESOLVED | HARFORD l.1158-1168, 1177-1182. The brief now gives her refusal, "But truly charity stirs me to tell you it", and her answer to the woman question. The card's knownFor and a Documented records claim carry it. The README sentence is now true. |
| C-M1 | RESOLVED | The birth lines are gone from the brief. The Office's pulpit scene now sets up Horstman's "not allowed to preach from the pulpit" (COMPER l.1763-1768; HORST l.502-505). The Horstman sentence is 25 words, at the limit. |
| C-M2 | PARTLY | "had died shortly before" no longer says before what. A listener can hear "shortly before the rider came", which is the timing round 1 objected to. See R2-2-M1. |
| C-M3 | RESOLVED | "though only in private, alone before his Maker" (COMPER l.5540-5541). |
| C-M4 | RESOLVED | "appear to date from" and "more likely to be" (FORSHALL-M l.628, 642-645). |
| C-M5 | RESOLVED | All three labels now name a question. |
| C-M6 | RESOLVED | |
| C-M7 | RESOLVED | The day and cause are now Inferential-Thin. The split left a duplicate "Death in 1349" claim that quotes the day under Widely Accepted. See R2-2-M11. |
| C-M8 | RESOLVED | COMPER l.2038-2052 covers l.2047-2048, and l.2088-2108 covers the burial line at l.2107. The gloss is now quoted as the brief has it. |
| C-M9 | RESOLVED | The heading's two claims are together again, and the Harford pair is one sentence. |
| C-M10 | PARTLY | All three gifts are there (WARRACK l.2087-2090). But "They were to have Christ's Passion in mind, a sickness ..., and three wounds" is not parallel, and "They were to have" can be heard as "they were meant to have". See R2-2-M2. |
| C-M11 | RESOLVED | WARRACK l.2315-2316. |
| C-M12 | RESOLVED | |
| C-M13 | RESOLVED | WARRACK l.5559-5560. |
| C-M14 | RESOLVED | HARFORD l.2170-2172. |
| C-M15 | RESOLVED | COMPER l.135-151 is Underhill's introduction. 1914 is supported in the text by the Methuen list "SPRING 1914" (COMPER l.14199). The Hilton 1923 source is now in `about`. |
| C-M16 | RESOLVED | DALGAIRNS l.1777-1780 ("most probable"); WARRACK l.343-345. |
| C-M17 | NOT RESOLVED (the fix states a false absence) | DALGAIRNS l.2876-2878 does give a ground: "Blomfield, 546. All that is known is that she was alive in 1443, but was a hundred years old." See R2-2-B2. |
| C-M18 | RESOLVED | WARRACK l.273-276. "his Latin entry" can only be Poiret's, since Warrack is "she". |
| C-M19 | RESOLVED | DALGAIRNS l.211-214. |
| C-M20 | RESOLVED | |
| C-M21 | RESOLVED | GARDNER l.255-256, 576-579 are as the note says. |
| D-B1 | RESOLVED | WINK l.4251-4254; PFEIFFER l.368-369; DENIFLE-II l.35268-35269. Frankfurt has its own contested_claim. |
| D-B2 | NOT RESOLVED (a new false "alone") | The new sentence says "Winkworth alone gives the year". EVANS l.539, SPENER l.5376, the McCann Cloud (l.16981), GARDNER l.243 and the Luther volume (l.6025) all give 1361. The card itself says "Evans also gives the year 1361", and the records' absent_details names Evans, McCann and Gardner. See R2-2-B1. |
| D-B3 | RESOLVED | BIHL l.11132-11133, 11145-11146. The item is deleted, and the records claim and note are rewritten. |
| D-M1 | PARTLY | The sides are added. But the card sets Pfeiffer's "Strassburg" straight after Evans's "Strassburg in Saxony", so a reader takes Pfeiffer to mean the Saxon town. Pfeiffer means the Alemannic city. See R2-2-M3. |
| D-M2 | RESOLVED | "Eckhart's name first appears, Evans says" and "There Eckhart wrote". |
| D-M3 | RESOLVED | DENIFLE-II l.35309-35311. |
| D-M4 | RESOLVED | DENIFLE-II l.35637-35638. |
| D-M5 | RESOLVED | |
| D-M6 | RESOLVED | |
| D-M7 | RESOLVED | KNOX l.1336-1342 ("in exceeding glory"). |
| D-M8 | RESOLVED | The bibliography at EVANS l.676 and 684 supports the two titles. |
| D-M9 | RESOLVED | |
| D-M10 | RESOLVED | WINK l.7122-7125. |
| D-M11 | RESOLVED | WINK l.5133-5138, 5171-5175. The fix leaves three "she says" in four sentences, and the line has no records witness. See R2-2-M4 and R2-2-M11. |
| D-M12 | PARTLY | Evans is placed alike in all three texts. In the Tauler brief, though, this is the first and only mention of Eckhart, with nothing to say who he was. See R2-2-M5. |
| D-M13 | RESOLVED | The History stays in `about`. |
| D-M14 | RESOLVED | WINK l.966-970. |
| D-M15 | RESOLVED (card) | WINK l.828-829. No records witness. See R2-2-M11. |
| D-M16 | RESOLVED (card) | WINK l.4245-4251; EVANS l.507-508. The records claim still says only "probably", and the item ends on a process phrase. See R2-2-M6 and R2-2-M11. |
| D-M17 | PARTLY | Round 1's "The Life says" was dropped. The Life's own judgment, "inordinate", is now in the narrator's voice, and the paragraph has no witness until its last clause. R1_changes.md does not list this cut. See R2-2-M7. |
| D-M18 | RESOLVED | |
| D-M19 | RESOLVED | Paragraphs 2, 5 and 6 are joined. KNOX l.3769-3772 supports the outcome. |
| D-M20 | RESOLVED | KNOX l.3498-3501. No records witness for "a Dominican master of theology" on the Suso entry. See R2-2-M11. |
| D-M21 | RESOLVED | "Life of the Servant" is gone from both cards and the brief. The closing "he" reads the Little Book's "Servant" as Suso, and the preface supports that (LITTLE l.745-748). |
| D-M22 | PARTLY | Henry of Nördlingen and Denifle are placed. Preger and Seeberg still have no role, though round 1 named that as the fault. See R2-2-M8. |
| D-M23 | PARTLY | The qualifier is restored, but the sentence is now 27 words. See R2-2-M9. |
| D-M24 | PARTLY | The claim texts now cite l.51, l.126 and l.5366, but each quotes an empty «». The three witness fields still give the blank lines 43, 116 and 5365. R1_changes.md says "Applied as worded". See R2-2-M10. |
| D-M25 | RESOLVED | DENIFLE-II l.34914-34916. The Contested list matches the four Eckhart contested_claims. A README line the Tauler cut left stale is at R2-2-M12. |

### New findings

**R2-2-B1 (johannes-tauler, brief paragraph 6: a false "alone" on the year of his death). Blocking.**
- Bad text: "Winkworth alone gives the year, the place and the day of his death, and her account of his last days follows the History."
- Evidence: EVANS l.539 "John Tauler ( 1300 - 1361 )"; SPENER l.5376 "Johann Tauler, geb. 1294, geſt. 1361"; cloud-of-unknowing_cloud-and-other-treatises_mccann1924.txt l.16981 "John Tauler (1300-1361)"; GARDNER l.243 "Johannes Tauler {d. 1361)"; luther_works-v3-selected_various1930.txt l.6025 "(d. 1361)". The card's dates field says "Evans also gives the year 1361". The records' absent_details says "Evans, McCann's Cloud and Gardner give the year 1361 only". My search found no other held file giving the place (Strasbourg) or the day. This is round 1's own fix wording for D-B2, applied as worded.
- Fix: "Winkworth alone gives the place and the day of his death, and her account of his last days follows the History." (20 words.) Make the same change to the records claim "Last illness 1361 at Strasbourg ...", which says "Winkworth alone" of the whole account.

**R2-2-B2 (julian-of-norwich, card uncertain "When she died": a false absence). Blocking.**
- Bad text: "J. B. Dalgairns says she appears to have died in 1443, and so lived to be a hundred. He gives no ground for the year."
- Evidence: DALGAIRNS l.2853-2854: "the close of Mother Juliana's life.*". The footnote, l.2876-2878: "* Blomfield, 546. All that is known is that she was alive in 1443, but was a hundred years old." Dalgairns cites Blomefield for the year. His note says only that she was alive in 1443. This is round 1's own C-M17 wording.
- Fix: "When she died. J. B. Dalgairns says she appears to have died in 1443, and so lived to be a hundred. In a later note, citing Blomefield, he says only that she was alive in 1443, at a hundred." (Second sentence 20 words; Blomefield is placed in the card's dates field.) In the records, add DALGAIRNS l.2853-2854, 2876-2878 to the Dalgairns claim and to the Lampet contested side.

**R2-2-M1 (richard-rolle, brief paragraph 5: "died shortly before" with nothing after "before").**
- Bad text: "When they returned, a rider went to Hampole and learned that Rolle had died shortly before."
- Evidence: COMPER l.2102-2105: "he found that the aforesaid illness had returned to the recluse shortly after the hour of Richard's departure". The fix cut round 1's "the fits came back", so "before" now hangs. It can be heard as before the rider came, which is the timing round 1 corrected.
- Fix: "When they returned, a rider went to Hampole. Rolle, he learned, had died shortly before they began again." (8 and 11 words; the brief becomes 404 words.)

**R2-2-M2 (julian-of-norwich, brief paragraph 3: a list that is not parallel).**
- Bad text: "They were to have Christ's Passion in mind, a sickness near to death at thirty, and three wounds, of contrition, compassion and longing toward God."
- Evidence: WARRACK l.2087-2090: "The First was mind of His Passion; the Second was bodily sickness ...; the Third was to have of God's gift three wounds." "They were to have" sets up an infinitive that the next two items do not continue, and it can be heard as "they were meant to have".
- Fix: "They were the remembrance of Christ's Passion, a sickness near to death at thirty, and three wounds, of contrition, compassion and longing toward God." (24 words; the brief stays at 404 words.)

**R2-2-M3 (meister-eckhart, card dates: Pfeiffer's Strassburg heard as the Saxon one).**
- Bad text: "He adds that some argue for Strassburg in Saxony and others for Hochheim in Thuringia. Franz Pfeiffer, his editor of 1857, calls Strassburg his home and birthplace."
- Evidence: EVANS l.376-380: the oldest MSS "which, consistently with Eckhart's home and birthplace, Strassburg, are written almost entirely in the Alcmanic idiom". PFEIFFER l.457-459: "Eckharts heimats- und geburtsort, Strassburg, fast durchweg in alemannischer mundart". Pfeiffer's Strassburg is the Alemannic city, the Strasbourg of the card's place field. Directly after "Strassburg in Saxony", the same spelling tells the reader he means the Saxon town.
- Fix: "Franz Pfeiffer, his editor of 1857, calls Strasbourg his home and birthplace. He finds its Alemannic dialect in the oldest manuscripts." In the records "His birth" side for Pfeiffer, add "the Alemannic city (PFEIFFER l.457-459)".

**R2-2-M4 (johannes-tauler, brief paragraph 5: a run of "she says").**
- Bad text: "Winkworth writes that most Dominicans left the city in 1338. She says Tauler sided with the emperor and kept working. He also preached, she says, from Cologne to Basel. There his old friend ..."
- Evidence: Three witness tags in four sentences make a choppy run of the kind round 1 flagged in the Rolle brief (C-M1). WINK l.5122-5138 is one passage.
- Fix: "She says Tauler sided with the emperor, kept working and preached from Cologne to Basel. At Basel his old friend Henry of Nördlingen, a priest from Constance, wrote that Tauler ..." (15 and 25 words.)

**R2-2-M5 (johannes-tauler, brief paragraph 3: Eckhart named with no context).**
- Bad text: "C. de B. Evans, an English translator of Eckhart in the 1920s, gives 1300."
- Evidence: This is the brief's only mention of Eckhart. A general listener hears a bare name (the Pattern: "any name a general listener would not know"; lessons section 14, names left unplaced). WINK l.4251-4252: "the celebrated Master Eckart, a brother of his own Order".
- Fix: "Winkworth says he was born there in 1290. C. de B. Evans, who put the sermons of Meister Eckhart, a fellow Dominican, into English in the 1920s, gives 1300." (8 and 21 words.) With R2-2-B1 and R2-2-M4 the brief is 405 words, FK 7.17, Flesch 68.1.

**R2-2-M6 (johannes-tauler, card uncertain "Whether he heard Eckhart": process wording).**
- Bad text: "No source used here shows them meeting."
- Evidence: "used here" narrates the build (round 1 C-M6, C-M20; lessons section 9). The two witnesses the item names say "must have" and "probably" (WINK l.4245-4251, 4563-4566; EVANS l.507-508).
- Fix: "Neither shows the two men meeting."

**R2-2-M7 (henry-suso, brief paragraph 5: the Life's framing dropped again; a changes log that leaves it out).**
- Bad text: "He had been told that his entry into the order came with a gift of worldly goods. This woke in him an inordinate fear of the sin called simony, and for about ten years he saw himself as damned. Then he went to Meister Eckhart ... Later, at a chapter in the Netherlands, two men of high rank charged ..."
- Evidence: KNOX l.3484-3490: "This temptation fell upon him through an inordinate fear." "Inordinate" is the Life's judgment. Round 1's D-M17 fix kept it as the Life's: "The Life says this woke in him an inordinate fear". The applied text has the narrator calling his fear inordinate. The paragraph's first four sentences now name no witness, since the "the Life says" before Eckhart and "the Life goes on" were also cut, and the paragraph opens a new subject. R1_changes.md lists those two cuts but not this one, and calls D-M17 applied.
- Fix: "The Life says this woke in him an inordinate fear of the sin called simony. For about ten years he saw himself as damned." (15 and 10 words; the brief becomes 405 words, FK 5.82, Flesch 78.7.) Record the cut in the R2 changes log.

**R2-2-M8 (henry-suso, card uncertain "The chapter that accused him": Preger and Seeberg still unplaced).**
- Bad text: "Preger and Seeberg, whom he also cites, chose 's-Hertogenbosch in 1335."
- Evidence: BIHL l.6673-6675: "Preger, Mystik II, 33ff. 360 und Seeberg 144". Evans's bibliography gives Preger's title: "Preger (W.), Geschichte der deutschen Mystik im Mittelalter. Leipzig." (EVANS l.684). No held line places Seeberg further.
- Fix: "Preger, in his history of German mysticism, and Seeberg, both cited by Bihlmeyer, chose 's-Hertogenbosch in 1335." (17 words.) Log Seeberg as a name the sources leave unplaced.

**R2-2-M9 (henry-suso, card legacy.traces 3: past the 25-word limit).**
- Bad text: "Comper writes that by the close of the Middle Ages the Horologium had become a favorite book in cloisters in Germany, the Netherlands, France, Italy and England." (27 words.)
- Evidence: CRAFT l.262-265. The words come from round 1's D-M23 fix (lessons section 14, a fix that breaks the limit).
- Fix: "Comper writes that by the close of the Middle Ages the Horologium was a favorite in cloisters in Germany, the Netherlands, France, Italy and England." (25 words.)

**R2-2-M10 (records, three D-M24 citations half-fixed; the changes log says "as worded").**
- Bad text: meister-eckhart: "DANIELS l.51: «»", with the witness "... 653-654, 43, 660-662". johannes-tauler: "SPENER l.126: «»", with the witness "l.5376, 116". henry-suso: "KNOX l.5366: «»", with the witness "KNOX l.5342-5345, 5365, 5380-5384".
- Evidence: DANIELS l.51 "MÜNSTER i. W. 1923"; SPENER l.126 "Leipzig 1841,"; KNOX l.5366 "* Thoss, near Winterthur, in Switzerland,". Lines 43, 116 and 5365 are blank. The claims now cite the right lines but quote nothing, and the witness fields still cite the blank ones.
- Fix: quote «MÜNSTER i. W. 1923», «Leipzig 1841,» and «* Thoss, near Winterthur, in Switzerland,». Change the witnesses to "DANIELS ... l.898-899, 653-654, 51, 660-662", "SPENER ... l.5376, 126" and "KNOX l.5342-5345, 5366, 5380-5384".

**R2-2-M11 (records, ranges short after the round 1 fixes).**
- johannes-tauler: there is no witness for "preached from Cologne to Basel" (add WINK l.5133-5138) or for the Leipzig edition of 1498 (add WINK l.828-829 to the editions claim). The "Card uncertain" claim says only "probably". Add Winkworth's Strasbourg view: WINK l.4245-4251, "he must, on returning from Paris to Strasburg, have come in contact with ... the celebrated Master Eckart".
- henry-suso: the chapter claim stops at KNOX l.3765. The new "He was harshly rebuked and threatened with punishment, though the Life holds he was guiltless" needs KNOX l.3769-3772. There is no claim for the card's "Henry of Nördlingen, a priest and friend of Tauler and Suso": add WINK l.5171-5175 ("a priest from Constance") and BIHL l.8295-8297 ("Freund und Gesinnungsgenosse unseres Mystikers war auch Heinrich von Nördlingen"). There is no claim for the brief's "Meister Eckhart, a Dominican master of theology": add DENIFLE-II l.35292-35293. There is none for the card's "Heinrich Denifle, a Dominican scholar": add DENIFLE-II l.35835.
- richard-rolle: the C-M7 split left two claims headed "Death in 1349". The Horstman one quotes "He died on the 29th of September 1349" and cites l.2160-2161 under Widely Accepted. Delete it, since the Comper and Underhill claim already carries the year, or cut its quotation to the year and its witness to HORST l.134.

**R2-2-M12 (README: a line the Tauler cut left stale; a doubled clause).**
- Bad text: (a) l.46: "Henry of Nördlingen, his friend, and Henry Charles Lea, the historian, are named in full in the brief." (b) l.55: "Eckhart's trial, 1326 to 1329, ... fall inside its years; Eckhart's birth falls before; his Paris mastership of 1302 and his trial fall inside."
- Evidence: (a) The Lea sentence was cut from the Tauler brief (R1_changes.md, Part D, "Other length cuts"). Lea is now only on the card, in remembered. (b) The trial is placed twice in one sentence. EVANS l.497-498 gives a Paris list of professors with "licentiates ... 1302". The card calls this "a Paris list of 1302" and never calls it a mastership.
- Fix: (a) "Henry of Nördlingen, his friend, is named in full in the brief, and Henry Charles Lea, the historian, on the card." (b) "... fall inside its years. Eckhart's birth falls before, and the Paris list of 1302 that first names him falls inside."

### Checks that pass, beyond the table

- **Audio.** All five scripts equal their briefs with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph. Each has two tags and no others.
- **Quotations.** Every new or changed quotation matches its file: "But truly charity stirs me to tell you it" (HARFORD l.1164-1165), "for I would God were known" (l.1165-1166), "I burst out singing what before I said" (COMPER l.5540), "the holy man delivered him" (KNOX l.3500-3501). The comma after "it" in the Julian brief replaces the file's full stop in the dialogue form the batch uses. The words are exact.
- **Cut briefs.** No scene or turning point was lost. The Rolle birth lines live on in the card's "When he was born", and Lea is on the Tauler card. Knox's role and "at thirteen" are on the Suso card, as are the Rolle Misyn date and the closing note. The Eckhart who-line now sits in the opening sentence, and the scene still opens the brief. The Suso brief joins up and is not flattened: the stylus, the cloths, the ten years of dread, Eckhart and the chapter's outcome all remain.
- **Pronouns.** Suso "says Suso was born", Eckhart "articles Eckhart confessed", Julian "his Latin entry" (Poiret) and Rolle "Then, it says" (the Office) all point where they should. "The prologue says Suso added teaching ... in her name" follows Stagel's naming, so "her" is Stagel.
- **Witnesses.** The Rolle paragraph 3 split keeps "it says" on the Dalton sentence. The Tauler "There his old friend" keeps Basel as Henry's place (WINK l.5171).
- **"Only", "alone", "never".** "The History's own text never names the Master" stands (the records search of WINK l.1748-4100). "Winkworth alone gives the day of his death" on the Tauler card stands, since my search found no other day. "Knox has IHS only on the cloths" stands (KNOX l.8417-8420). The Rolle "only HORST l.134 and 2161" note stands.
- **Writing.** In the changed sentences and their neighbors I found no "X, not Y" or "not X but Y" in the narrator's voice, no colon-reveal, no thesis opener and no tail. "That is Evans's judgment" and "Whether any of it happened is disputed" are gone. Spelling is American ("favorite", "gray", "modernized", "defense"). "Favourite" and "honour" spellings appear only inside quotations.
- **Card order and fields.** The order is unchanged on all five cards. The Suso and Eckhart uncertain lists lost only items that held no doubt.
- **README.** The score range (402 to 405 words, grade 5.5 to 8.1, Flesch 63.8 to 80.9) matches all eight briefs as they stand. The Julian, Eckhart, Tauler and Suso held-witness lines match the records.
- **R1_changes.md.** Its descriptions of C-B1, C-M1, C-M2, C-M10, D-B1 to D-B3, D-M2, D-M11, D-M19 to D-M21 and the length cuts match the diff. The exceptions are D-M17 (R2-2-M7) and D-M24 (R2-2-M10). Two small unlisted drops ("heavy" before "punishment" and "that" in D-M19; "Franz" and "his editor of 1857" in D-B1, now carried by the dates field) change no claim.

### Scores

| Brief | Words | FK | Flesch | After fixes: words / FK / Flesch | Blocking | Minor |
|---|---|---|---|---|---|---|
| richard-rolle | 402 | 6.31 | 74.98 | 404 / 6.19 / 75.15 (M1) | 0 | 2 (M1, M11) |
| julian-of-norwich | 405 | 5.53 | 80.91 | 404 / 5.59 / 80.45 (M2) | 1 (B2) | 1 (M2) |
| meister-eckhart | 404 | 7.98 | 63.98 | unchanged | 0 | 2 (M3, M10) |
| johannes-tauler | 404 | 7.02 | 69.07 | 405 / 7.17 / 68.06 (B1, M4, M5) | 1 (B1) | 5 (M4, M5, M6, M10, M11) |
| henry-suso | 403 | 6.01 | 78.08 | 405 / 5.82 / 78.69 (M7) | 0 | 5 (M7, M8, M9, M10, M11) |

All five pass `grade_text` now and after the fixes (FK 10 or below, Flesch 60 or above). All stay at or under the cap of about 405 words. The minor column counts a shared finding (M10, M11) under each profile it touches. R2-2-M12 is the README's.

### Count

- **Blocking: 2.** R2-2-B1 (Tauler, a false "Winkworth alone gives the year"), R2-2-B2 (Julian, a false "He gives no ground for the year"). Both come from round 1's own fix wording, applied as worded.
- **Minor: 12.** R2-2-M1 to R2-2-M12.
- **Round 1 status (Parts C and D, 50 findings):** 40 RESOLVED (D-M15 and D-M16 on the card only, with their records at R2-2-M11), 8 PARTLY (C-M2, C-M10, D-M1, D-M12, D-M17, D-M22, D-M23, D-M24), 2 NOT RESOLVED (C-M17, D-B2).

**Files reviewed**
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/richard-rolle.brief.txt, richard-rolle.card.json, audio/richard-rolle.audio.txt
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/julian-of-norwich.brief.txt, julian-of-norwich.card.json, audio/julian-of-norwich.audio.txt
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/meister-eckhart.brief.txt, meister-eckhart.card.json, audio/meister-eckhart.audio.txt
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/johannes-tauler.brief.txt, johannes-tauler.card.json, audio/johannes-tauler.audio.txt
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/henry-suso.brief.txt, henry-suso.card.json, audio/henry-suso.audio.txt
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/records.json (the five entries)
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/README.md
- /home/user/CIC-Project/Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era6-batch1/R1_review.md (Parts C and D) and R1_changes.md
