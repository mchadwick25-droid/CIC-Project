# R3 recheck: era 4 batch 2

Round 3, the last, ran in two parts, each a targeted recheck by a fresh Opus agent that had not seen the drafting or the earlier rounds, at full effort. The parts follow, unchanged.

## R3 recheck, part 1: Dionysius of Tel Mahre, Jacob of Edessa, Benjamin I of Alexandria, Gregory of Narek

Reviewer: independent Opus, first sight of these files, at full effort. I edited no profile, records or notes file. I made no git writes and no web, paid or model calls, and used local scripts and reads only. Inputs: R1_partB.md, R1_changes_partB.md, R1_partD.md, R1_changes_partD.md, R2_part1.md, R2_changes_partB.md, R2_changes_partD.md, the current batch 2 briefs, cards and audio, and the scratchpad records and notes. I found the round 2 changes by diffing the current briefs against R2's scored copies in `review/fixR2p1/` (all three are identical to the current briefs; the Jacob brief is unchanged since round 1) and by comparing cards, records and notes with the wording R2 quotes. For every finding and every changed string I opened the cited lines in the vendored file and read them in context, folding OCR noise, long s, double spaces and hyphen breaks.

Short names as in R1 and R2. Line numbers for briefs are file lines (paragraphs sit on odd lines).

**Mechanical (all four), by script.** `engine.m1.gates.grade_text`, run from the repo root. Audio compared with the brief once `[calmly] ` (start) and `[warmly] ` (start of the last paragraph) are removed.

| Profile | Words | Time @162 | FK | Flesch | Audio = brief + tags | Card parses, no empty fields | Longest brief sentence |
|---|---|---|---|---|---|---|---|
| dionysius-of-tel-mahre (major) | 404 | 2:30 | 7.68 | 66.76 | yes (1 calmly, 1 warmly) | yes | 22 |
| jacob-of-edessa (major) | 404 | 2:30 | 7.11 | 68.81 | yes | yes | 21 |
| benjamin-i-of-alexandria (major) | 404 | 2:30 | 8.18 | 60.40 | yes | yes (no `otherNames`, as R1 noted) | 24 |
| gregory-of-narek (major) | 405 | 2:30 | 8.03 | 61.53 | yes | yes | 25 (P6, unchanged since R1) |

No tag is in a brief or card. Every card is in batch 1's order with at most three `keyWorks`. Every `sources` file exists. No card sentence outside `sources` runs past 25 words (the one script hit, Gregory `remembered` 1, is two sentences the splitter joined at `."`). All four records parse; every `formation_confidence` is one of the five levels (Dionysius 32 claims, Jacob 36, Benjamin 34, Gregory 35), and every `contested_claims` entry has two or more sides with witnesses. The two brief fixes below, applied to scratch copies in `/tmp/claude-0/-home-user-CIC-Project/46148d77-0e3f-56b5-a386-901106a72590/scratchpad/review/fixR3p1/`, score: Benjamin 405 words, FK 8.23, Flesch 60.07; Gregory 405 words, FK 8.09, Flesch 61.11.

---

### Dionysius of Tel Mahre

| Finding | Verdict | Evidence |
|---|---|---|
| B-M7 / R2-B-B1 (false absence of where Tel Mahre was) | RESOLVED, with a new label fault (R3-B-M1) | WRIGHT l.292-295, "Dionysius of Tell-Mahré*, patriarch of the Jacobites (ob. A. Gr. 1156, A.D. 845)"; the footnote at l.314-316, "a small town on the river Balikh, between ar-Rakkah and Hisn Maslamah, according to Yáküàt in the Mujam al-Buldan". The new Documented claim quotes it faithfully with the OCR marked. "No held source says Dionysius was born there" is true to what Wright says. Charon's "Tell-Mahrê (Macédonopolis ?)" is at CHARON l.33957, and the tail "no held line ties that see to Dionysius" holds. |
| R2-B-M1 (brief P6, "ignored") | RESOLVED | Brief l.11 and audio: "John overlooked his old age and the contempt of waiting at princes' doors". MICHAEL2 l.27490-27508: "tu n'as pas considéré la vieillesse ... des stations et des prostrations à la porte des princes avec le mépris". |
| R2-B-M2 (card `uncertain` 3, the Wright sentence) | RESOLVED | Card: "W. Wright ... also gives this chronicle to Dionysius. He says Dionysius took Joshua's short chronicle into his own larger work." WRIGHT l.292-298: "who incorporated it with his own larger work ... The solitary manuscript of this work ... is preserved in the Vatican Library", tied to Assemani "Bibl. Orient., t. ii, p. 98 sqq." (l.300-301, 318) and to the Nitrian desert (l.301), which is the Scete chronicle the card names first (BH1 l.22351-22366). 15 and 13 words. |

**Changed strings checked.** Brief P6 sentence 3, card `uncertain` 3 sentences 3-4, records Wright claim, `absent_details` 1: sourced, quotations verbatim to the OCR, witnesses attached, no count, no editor's view told as settled. The `absent_details` 1 label is the one fault (R3-B-M1).

**Whole brief and card read again.** I re-read every brief sentence against its lines: the decree and Lazarus (BH1 l.21384-21393, 21500-21505), the answer and the ruling (l.21509-21518, 21700-21716), the seizure and the three-day ordination (l.20517-20540, 20612-20620), Abdallah, Mohammed, Tanis and the graded tax ("Patriarcha etiam rogavit pro Tanisiis ... Praecepit igitur Emirus", l.21042-21066, 21159-21181), the Byamites (l.21798-21822), the preface and Theophilus (MICHAEL2 l.27478-27540), and the last letter (BH1 l.22334-22344, 22449-22468). Writing checks: no AI tells, no empty contrast ("for coming instead of writing" is the source's own "quum posses per epistolam"), no tail, aphorism or triad beyond Bar Hebraeus's own sequences, no sentence over 22 words, every common name placed. No new fault.

#### New findings

- **R3-B-M1 MINOR (records `absent_details` 1 label; item 1; a label wider than its note, contradicting a held claim).** The detail is headed "His birth year and family", but the same records, and card `traces` 2, hold his maternal grandfather: "J'ai pris ces choses des histoires de Daniel, fils de Samuel, du Tour 'Abdîn, mon grand-père maternel" (MICHAEL2 l.36788-36791). The note itself is exact ("No held source gives his birth or his parents"), so nothing participant-facing is wrong and no reader of the note is misled. The label alone overstates. Records only.
  - Fix, `detail`: "His birth year and parents".
  - Fix, `note`, add as a second sentence: "His maternal grandfather, Daniel son of Samuel of the Tur Abdin, is named in the passage Michael quotes (MICHAEL2 l.36788-36791)."

**Verdict, Dionysius of Tel Mahre: CLEAR on the brief, audio and card. 0 blocking, 1 minor (R3-B-M1, records).**

---

### Jacob of Edessa

| Finding | Verdict | Evidence |
|---|---|---|
| R2-B-M3 ("Fr. Cumont") | RESOLVED | Card `uncertain` 5, records claim 23 and the teaching-years contested claim read "F. Cumont". PO16 l.45722: "M.-A. KuGENER et F. Cu.MONT, Recherches sur le Manichéisme (Bruxelles, 1912)"; "Fr. Cumont" at l.44831. "in a book of 1912" holds. |
| R2-B-M4 (Nomocanon heading list; the reply to John the Stylite) | RESOLVED, with one line range to fix (R3-B-M2) | See the count check below. The reply is at MAI10 l.41400-41404 ("Iohannes Stylita. inter- rogans religiosissimum Jacobum E.des- sae, responsum accepit: dixit n;.ai- rum : haud ex necessitate fit hoc ie- iunium"). `absent_details` 2 now narrows "letters" correctly. The card trace gives no count, which stays right. |

**The count in the Nomocanon records.** The records claim (claim 32) lists heading lines and states no number; the notes ("After R2") say "28 headings". I ran my own OCR-tolerant sweep of the whole Nomocanon (MAI10 from the title at l.38227 to l.52000), by two methods: a pattern for every `[IlT1J]acob…` + `[EB]d…` form, and a read of every short line under 30 characters that contains "obi", "aco", "ess" or "dess". Both find the same 28 heading lines, exactly those listed: l.38646, 38776, 39368, 39453, 39469, 39681, 39769, 39821, 40175, 40316, 40490, 40599, 40769, 40797, 40878, 41009, 41216, 41563, 41678, 41841, 42146, 42331, 42408, 43636, 43917, 44049, 44700, 44745. No heading was missed. The only other short "Iacob" lines are the two bare "Iacobi." (l.38949, 39540), rightly left out, and "Unus Iacob." / "Una Iacobi." (l.44199, 44221), which are not author headings. Jacob is also named, not as a heading, at l.40853 ("Illud religiosissimi Iacobi convenientius est peragere", a Directio), at l.44337 (a list of church books: "Item lacobi Edesseni septem, et unus theologiae, ac epistolae eiusdem plures"), and at l.45750 (with Dionysius). None of these changes the heading count, and l.44337 names letters without holding their text, so "His letters are otherwise not held as texts" stays true. The count of 28 is fully made.

**Changed strings checked.** Card `uncertain` 5; records claims 23, 32, 34, 35, the teaching-years contested claim and `absent_details` 2; notes "After R2". All sourced, quotations verbatim to the OCR with OCR forms marked. One line range is off (R3-B-M2).

**Whole brief and card read again.** The brief is unchanged since round 1. I re-read it against its lines: the burning (MICHAEL2 l.36392-36400; "Il y établit sa retraite" for "settled", l.36370-36371), 'Ayndaba, Kenneshre and Alexandria (l.36355-36370; BH1 l.17304-17313), the four years and Kaisum (MICHAEL2 l.36374-36402), Eusebona and Tell 'Ada (l.36406-36413), the return, the books and the death (l.36414-36424, 36741-36753; BH1 l.17515-17522), the preface (MICHAEL1 l.56573-56576), the 700/1 revision (PO16 l.45708-45712, 45743-45745) and the gloss (l.49763-49765). No new fault.

#### New findings

- **R3-B-M2 MINOR (records claim 35, `absent_details` 2 and notes "After R2"; item 1; a witness range that misses the reply).** The reply is cited as l.41399-41403. "Iohannes Stylita" begins at l.41400, "ieiunium" ends at l.41404, and the reply runs on to its close, "Ilaec omnia verba sunt reliziosissimi lacobi" (l.41425; OCR for "Haec ... religiosissimi Iacobi"). Records and notes only.
  - Fix, claim 35 witness and the `absent_details` 2 and notes citations: "MAI10 l.41400-41425".
  - Fix, claim 35, add after the quotation: "; it closes 'Haec omnia verba sunt religiosissimi Iacobi' (l.41425; OCR 'Ilaec', 'reliziosissimi lacobi')".

**Verdict, Jacob of Edessa: CLEAR on the brief, audio and card. 0 blocking, 1 minor (R3-B-M2, records and notes).**

---

### Benjamin I of Alexandria

| Finding | Verdict | Evidence |
|---|---|---|
| R2-D-B1 (the Cana homily: codex XV's date, and "Syriac") | RESOLVED | I read ASSEMANI l.123850-124130 in full. Each codex runs number, contents, then size and any date. Codex XIV closes "In fol. membr. 120. Ícript. anno Martyrum 655. (Chrifli 939.)" (l.124041-124052). Codex XV, Ignatius to Gregory Nazianzen's homily, closes "In fol. membr. 313. Ícript. anno Marty- rum 781. ( Chrifli 1065.)" (l.124081-124084; 781 + 284 = 1065). Codex XVI opens "Benjamini Patriarche Alexandrini Homilia de Nuptiis Canz Galilez" (l.124085-124089) and closes "Iu fol. membr. 139." with no date (l.124101); XVII follows (l.124104). The contents (Pisentius, Senutius, Abanub) and the era of the Martyrs mark the list as Coptic, and its heading is "CODICES COPTICI, Quos Auctor ex Oriente advexit". `keyWorks` 2 `about` ("known here only from Joseph Assemani's list of the Coptic manuscripts he brought from the East. It names the homily in an undated parchment volume. The text is not held"), the `sources.about` title, records claim 29, `absent_details` 1 and notes l.29 are all now right: "membr." is parchment, and no date stands in codex XVI. A fresh search of every held file naming Benjamin for Cana, Canae, Nuptiis, noces and wedding finds the homily only here, so "known here only from" holds. The R1 error is undone, not patched over. Two citation details remain in the records (R3-D-M2). |
| D-M7 / R2-D-M3 (the unsigned Abu Salih note given to Evetts) | RESOLVED | ABUSALIH l.131-134: Butler's "contributions to the work are by no means limited to the notes which bear his initials". The Wadi Habib note (l.9662-9665, 9700-9702) and the 622-660 note (l.11738-11742) carry no "(A. J. B.)". The title page names "B. T. A. Evetts" (l.44). `traces` 3 sentence 2 and `uncertain` 5 sentence 3 now name the edition and not the note's author; claim 31 is Inferential-Thin with the reviewer's reason; the contested side reads "an unsigned note in B. T. A. Evetts's 1895 Abu Salih". |
| R2-D-M1 (brief P6, tense) | RESOLVED | Brief l.11 and audio: "He calls the account a fable of later Copts." RENAUDOT l.11542-11547: "hxc omnia a Coptitis recentioribus inventa ede non dubitamus ... in longa illa fub Agathonis nomine fabula". |
| R2 table, Charles's lines | RESOLVED | Claim 11 cites NIKIU l.178-179. |

**Changed strings checked.** Brief P6 last sentence; card `keyWorks` 2 `about`, the Assemani `sources.about` title, `traces` 3 sentence 2, `uncertain` 5 sentence 3; records claims 11, 29, 31, the years contested claim and `absent_details` 1; notes l.29 and l.34. All sourced and faithful, no count given, no false absence. The two records details are R3-D-M2.

**Whole brief and card read again.** I re-read every brief sentence against its lines: Sanutius, the letter and "a man of God like this man" (HIST l.44462-44469, 44586-44588, 44683-44685), Barshut, Theonas and Andronicus (l.42838-42847, 43225-43230), Cyrus, the angel, Wadi Habib, Upper Egypt and Mennas (l.43240-43241, 43420-43447, 43572-43582, 43750-43752), John of Nikiu ("every one said", NIKIU l.12005-12012), Michael (MICHAEL2 l.33096-33125), the gentleness, the canons, the anathemas quotation (HIST l.44831-44833, 47893-47910, 48051-48052, verbatim), Renaudot (RENAUDOT l.10992-10993, 11541-11548), and Agathon's closing words (HIST l.45959-45962, verbatim). One reading fault, present since round 1, was missed by both earlier rounds (R3-D-M1).

#### New findings

- **R3-D-M1 MINOR (brief P2, l.3, and audio; item 4; a pronoun whose nearest antecedent is wrong).** "So says the History of the Patriarchs of Alexandria ... Benjamin I of Alexandria led the Egyptian church that refused the council of Chalcedon. B. Evetts, its translator, heads his life 622 to 661." The round 1 word-budget trim turned "who translated the History" into "its translator" (R1_partD.md, D-M3 budget note), and a sentence now stands between the History and "its". Heard aloud, "its" lands on the council or the church. Evetts translated the History (HIST title, l.1-8; heading l.42834). Fix (11 words; brief 405, FK 8.23, Flesch 60.07): "B. Evetts, the History's translator, heads his life 622 to 661." Carry it into the audio.

- **R3-D-M2 MINOR (records claim 29 and `absent_details` 1; notes l.29; item 2; a heading assembled from lines the citation does not cover, and two OCR forms unmarked).** The claim quotes "CODICES COPTICI, Quos Auctor ex Oriente advexit" at l.123862-123865. Those lines hold only "COPTICI," (l.123862) and "Oriente ad'vexit ." (l.123865). "CODICES" and "Quos Auctor ex" stand at l.123953-123954, where the list of codices I to V begins; the two-column OCR has split the heading. The quoted "advexit" is "ad'vexit" in the OCR, and "In fol. membr. 139." is "Iu fol. membr. 139." Records and notes only.
  - Fix, claim 29: "Assemani's list of the Coptic codices he brought from the East ('CODICES COPTICI, Quos Auctor ex Oriente advexit', split by the two-column OCR across l.123862, 123865 and 123953-123954; OCR 'ad'vexit') gives, as codex XVI, 'Benjamini Patriarchae Alexandrini Homilia de Nuptiis Canae Galilaeae' (l.124085-124089; OCR 'Patriarche', 'Canz Galilez'). The codex is 'In fol. membr. 139.' with no date (l.124101; OCR 'Iu fol.'). The date 1065 at l.124081-124084 closes codex XV." Witness: "ASSEMANI l.123862-123865, 123953-123954, 124081-124101".
  - Fix, `absent_details` 1 and notes l.29: cite "l.123862-123865, 123953-123954" for the list heading.

**Verdict, Benjamin I of Alexandria: NOT CLEAR. 0 blocking, 2 minor (R3-D-M1 in the brief and audio; R3-D-M2 in the records and notes). The Cana homily item is now right in the card, records and notes.**

---

### Gregory of Narek

| Finding | Verdict | Evidence |
|---|---|---|
| R2-D-M2 (brief P4: Stepanos's writing date) | RESOLVED as to the date, with a new reading fault (R3-D-M3) | Brief l.7 and audio: "Stepanos of Taron, of the same century, wrote Armenian history." MACLER l.438-442, book III runs "grosso modo de l'an 887 l'an 1005"; l.835-838 and 863-866, written for the catholicos Sargis in his thirteenth year and stopping in 1004-1005; l.4346-4347, "Dans notre jeunesse, nous avons vu nous-même quelques-uns de ces [Pères]". Records `absent_details` 2 now reads "wrote soon after 1004", with those lines; Macler's l.835-838 and 863-866 carry it. Card `uncertain` 7, "of Gregory's own century", is unchanged and right. |

**Changed strings checked.** Brief P4 sentence 4; records `absent_details` 2; notes l.33. Sourced and faithful. One reading fault (R3-D-M3).

**Whole brief and card read again.** Every quotation was re-checked by script against its file, folding OCR: "We, however, report this merely as an anecdote" and "as it shews the public esteem towards the holy man" (ISSAV), "we implore Thee with out-stretched arms and deep groans" (ISSRIT), "Accept, O powerful Lord God, in thy loving-kindness the prayer of him that has turned again to thee" (CONYBEARE), "regarded as a potent talisman against all kinds of dangers" (ORMANIAN): all verbatim. I re-read the rest against R2's evidence lines and found no other fault. The card is unchanged since round 1 and was cleared by R2; read again as a whole, it shows no fault.

#### New findings

- **R3-D-M3 MINOR (brief P4, l.7, and audio; item 4; "the same century" points to the wrong writer).** P4 names Chamich, Issaverdens, Ormanian and Serpos. The nearest time in the brief is "Giovanni de Serpos, writing at Venice in 1786" (P3, l.5); Gregory's "tenth-century Armenia" is two paragraphs back (P2, l.3). Coming straight after "Serpos says ...", "of the same century" is heard as Serpos's century, and Stepanos becomes an eighteenth-century writer. Fix (same word count; 405 words, FK 8.09, Flesch 61.11), matching card `uncertain` 7: "Stepanos of Taron, of Gregory's own century, wrote Armenian history." Carry it into the audio.

**Verdict, Gregory of Narek: NOT CLEAR. 0 blocking, 1 minor (R3-D-M3, in the brief and audio).**

---

### Writing checks on the whole briefs

I read all four briefs again in full for AI tells, "not X but Y", "X, not Y" and empty contrasts, colon-reveals, tails and beat lines, aphorisms, triads and doublets, undefined terms, sentences over 25 words, and common names without a place at first mention. Beyond R3-D-M1 and R3-D-M3, none remains. Every common name is placed at its first mention in each brief and card ("Joseph, patriarch of Egypt"; "Lazarus, a deposed bishop of Baghdad"; "John, metropolitan of Dara"; "Theophilus of Edessa"; "Julian the Roman"; "Athanasius of Balad"; "Eusebius of Caesarea"; "Severus of Antioch"; "Cyrus, bishop of Phasis"; "John, the Coptic bishop of Nikiu"; "Anania of Narek"). No round 2 string gives a count that was not fully made, tells an editor's view as settled, or cites the wrong work.

### Counts

| Profile | Blocking | Minor | Touches participant text |
|---|---|---|---|
| Dionysius of Tel Mahre | 0 | 1 (R3-B-M1, records) | no |
| Jacob of Edessa | 0 | 1 (R3-B-M2, records and notes) | no |
| Benjamin I of Alexandria | 0 | 2 (R3-D-M1, brief and audio; R3-D-M2, records and notes) | yes, R3-D-M1 |
| Gregory of Narek | 0 | 1 (R3-D-M3, brief and audio) | yes, R3-D-M3 |

No blocking point is open. Two minor fixes touch participant text: R3-D-M1 in the Benjamin brief and audio, and R3-D-M3 in the Gregory brief and audio. Under the brief for this round, any fix to participant text made after round 3 goes to Mark for a cap ruling.


## R3 recheck, part 2: Maximus the Confessor, Martin I of Rome, Timothy I of Baghdad, Photius of Constantinople

Reviewer: independent Opus, first sight of these files. I edited no profile, records or notes file. I made no git writes and no web, paid or model calls, and used local scripts only. Inputs: `review/R1_partA.md`, `R1_changes_partA.md`, `R1_partC.md`, `R1_changes_partC.md`, `R2_part2.md`, `R2_changes_partA.md` and `R2_changes_partC.md`; the current files in `Who-Profiles/era4/batch2/`; the scratchpad records and notes. For every R2 finding, and for every string changed in round 2 (including the drafters' unrequested changes), I opened the cited lines again in the vendored file and read them in context, folding OCR noise, long s, double spaces and hyphen breaks. Short file names are R1's.

**Mechanical (all four), by script.**

| Profile | Words | Time @162 | FK | Flesch | Audio = brief + tags | Card parses, no empty fields | Longest brief sentence |
|---|---|---|---|---|---|---|---|
| maximus-the-confessor (major) | 405 | 2:30 | 8.16 | 61.24 | yes (1 calmly, 1 warmly) | yes | 25 (P5, "One must speak…") |
| martin-i-of-rome (major) | 405 | 2:30 | 6.83 | 71.57 | yes | yes | 25 (P7, Bede) |
| timothy-i-of-baghdad (major) | 405 | 2:30 | 7.27 | 66.89 | yes | yes | 25 (P5, Thomas of Marga) |
| photius-of-constantinople (major) | 404 | 2:30 | 7.11 | 66.98 | yes | yes | 24 (P5, Symeon) |

`[calmly] ` opens each audio file and `[warmly] ` opens its last paragraph; no tag is in a brief or card. Each card is in batch 1's field order with at most three `keyWorks`; Photius has no `otherNames`, rightly absent rather than empty. No card sentence outside `sources` runs past 25 words. Every `sources` file exists. The four scratch records parse, and all 126 `formation_confidence` values (Maximus 34, Martin 35, Timothy 29, Photius 28) are one of the five levels. The brief quotations were re-found verbatim: Bede (GILES l.10402-10403), Mingana (MINGANA l.1690) and Freese (FREESE l.1743-1745; R2 cited l.1740-1741, a drift in the review only, not in the records).

---

### Maximus the Confessor

| Finding | Verdict | Evidence |
|---|---|---|
| R2-A-M1 (brief l.7, stacked appositives) | RESOLVED | Brief l.7: "Later the emperor Constans forbade talk of one will or two in an edict, the Typos." The Typos is "nec unam, nec duas voluntates" (M10 l.89931-89958) and issued "per sextam indictionem" (PG90 l.7540-7541). Same 16 words; the subject now reaches its verb at once, and "the Typos" ends the sentence, where P5 picks it up. |
| R2-A-M2 (card `uncertain` 9, "names") | RESOLVED | Card l.48: "The brief tells of the last two." Brief l.9 names the Typos and tells of the Ekthesis as "an earlier statement by the patriarch Sergius" ("per ecthesim, quae in hac urbe Sergio auctore edita est", PG90 l.7539-7540). True as worded. |

All 13 R1 findings were resolved in round 2 and stay resolved; neither round 2 change touched their lines.

**Changed strings checked.** Brief l.7 and card l.48: PASS. Audio carries l.7. I then read the whole brief and card again. No AI tells, no narrator's contrast, no tails or aphorisms, no undefined term or bare common name. The close, "no teaching of his own, only the common teaching", is Maximus's "dogma proprium non habeo, sed commune" (PG90 l.7507-7508), attributed.

**New findings.** None.

**Verdict: CLEAR** (0 blocking, 0 minor).

---

### Martin I of Rome

| Finding | Verdict | Evidence |
|---|---|---|
| R2-A-B1 and A-M17 ("that council" with no antecedent) | RESOLVED | Card l.31: "for the legates they sent to the council of Constantinople in 680." NPNF heads the letter "The Letter of Agatho and of the Roman Synod of 125 Bishops which was to Serve as an Instruction to the Legates Sent to Attend the Sixth Synod" (l.25510), and "The Sixth Ecumenical Council met on November 7, 680, for its first session" (l.24572). The addressees, "Constantine, the great Emperor, and Heraclius and Tiberius, Augustuses" (l.25520-25521), support "the emperors". 25 words. A-M17 is now closed. |
| R2-A-M3 (keyWorks 3, 105 told as settled) | RESOLVED | Card l.24: "The Book of the Popes and Bede count 105 bishops." The Book of the Popes' "numero centum & quinque" (M10 l.82055) and Bede's "the synod of the blessed Pope Martin and 105 bishops" (GILES l.10402-10403). The count now has its witnesses, and `uncertain` 9 gives 150 and 110. |
| R2-A-M4 ("exarch" undefined) | RESOLVED | Brief l.7: "After Olympius, governor of Italy, failed to seize him, the Book of the Popes says, his successor, Theodore Calliopas, took him." Olympius is sent "cubicularium & exarchum ad regendam omnem Italiam" (M10 l.82124-82126); after he dies of illness, "Deinde directus est ab imperatore Theodorus exarchus, qui cognomento Calliopa dicitur … Qui tollentes sanctissimum Martinum papam … perduxerunt Constantinopolim" (l.82110-82118). Card l.46, "Olympius, the emperor's governor in Italy", rests on the same lines. |

**Unrequested changes, checked against Mansi 10.**
- **`uncertain` 7 (l.47), "pope and governor" and "Nor had he made him governor, he said."** PASS. At his trial, after the witnesses swear he was "unius consilii … cum Olympio" (M10 l.87824), Martin asks, "Quomodo habebam ego tali viro adversus stare, habente praecipue brachium universae militiae Italicae? an potius ego illum feci exarchum?" (l.87839-87841). "Governor" renders "exarchum" in the sense the card has already glossed (l.46), and Duchesne's "le pape et l'exarque" refers to the same man (records l.129). The rhetorical question is fairly told as a denial. "Him" points back to "a man who commanded the army of Italy", which is right.
- **`uncertain` 8 (l.48), "The decree Theodore Calliopas handed to the clergy".** PASS on the fact. Martin's letter: "jussio a Calliopa porrecta est presbyteris et diaconibus, in qua humilitatis meae abjectio continebatur, quod irregulariter & sine lege episcopatum subripuissem" (M10 l.87345, 87424-87426). "Handed" is "porrecta"; "the clergy" fairly covers "presbyteris et diaconibus"; the decree is the emperor's "jussio", and the card does not make it Calliopas's own. Two faults in the same sentence are R3-A-M1.

**Changed strings checked.** Brief l.7 and card l.24, 31, 46, 47 and 48: PASS on the facts, with R3-A-M1 on l.48. Audio carries l.7. I read the whole brief again: no AI tells, contrasts, tails or aphorisms. "His friend Theodore" (l.3) and "Theodore Calliopas" (l.7) are kept apart by the surname and by "his successor".

**New findings.**

- **R3-A-M1 MINOR (card `uncertain` 8, l.48; items 4 and 1; in a string changed in round 2).** "The decree Theodore Calliopas handed to the clergy, as Martin quotes it, said he had seized the see irregularly and without law." Two faults. First, this is the card's only mention of Calliopas. The card never says who he is, and its first `keyWorks` is "Two letters to Theodore", the friend, so a card reader can take the two Theodores for one. Second, Martin does not quote the decree. He reports what it held, in his own first person: "in qua humilitatis meae abjectio continebatur, quod … subripuissem" (M10 l.87424-87426). "Quotes" claims a verbatim citation the letter does not give. Fix, second and third sentences: "Theodore Calliopas, the governor who arrested him, handed the clergy a decree. As Martin reports it, the decree said he had seized the see irregularly and without law." (13 and 16 words.) "Arrested" rests on "Qui tollentes sanctissimum Martinum papam … perduxerunt Constantinopolim" (l.82115-82118), and "governor" matches l.46. Records l.154 can keep its claim unchanged.

**Verdict: CLEAR on blocking points** (0 blocking, 1 minor, R3-A-M1, card only).

---

### Timothy I of Baghdad

| Finding | Verdict | Evidence |
|---|---|---|
| R2-C-M1 and C-M5 (hedge cut from the second clause) | RESOLVED | Card l.30: "Bar Hebraeus reports it was said that … It was also said that they had not obeyed the catholicos of Seleucia." The whole report stands under "Fertur … et praeterea catholico Seleuciae non paruisse" (BH l.9750-9805); Mingana, "It is said that … were not under the jurisdiction of the Catholicos of Seleucia" (MINGANA l.1721-1725). The third sentence keeps "Dicebant enim" as Bar Hebraeus's own report. C-M5 is now closed. |
| R2-C-M2 (punctuation) | RESOLVED | Card l.45: `though "truth acted with subtlety".` The source runs on, "truth acted with subtlety and performed its work" (TM l.17293). The comma in `"by fraud,"` stands on "BY FRAUD, * LIKE JACOB" (l.17242-17245). |
| R2-C-M3 (empty sentence) | RESOLVED | Card l.49: "Joseph Assemani takes Amr's report of debates with al-Hadi to be the same disputation, with al-Hadi in place of al-Mahdi." Assemani: "Amrus … Hadium pro Mohdio legit" (ASSEMANI 3.1 l.29815-29817); Amr: "Saepe admodum eum accersebat Hadi chalipha ut cum eo colloqueretur de religione" (AMR l.13027-13029). 20 words, and it now says something. |
| R2-C-M4 (Bar Hebraeus bare) | RESOLVED | Brief l.9: "The historian Bar Hebraeus puts his death in the Arab year that began in June 819." His Chronicon Ecclesiasticum is the held BH file. |

**Changed strings checked.** Brief l.9 and card l.30, 45 and 49: PASS. Audio carries l.9. I read the whole brief and card again. No AI tells, contrasts, tails or aphorisms. The quotation that closes the brief is verbatim, with ", and in all the provinces" following in the source (MINGANA l.1690), so the period sits rightly outside the marks.

**New findings.**

- **R3-C-M1 MINOR (card `uncertain` 9, l.52; item 4; a heading that names no question; unchanged since R1's C-B1 fix, missed by R2).** "His name. Chabot and Bar Hebraeus place his enthronement at Seleucia, and Amr ibn Matta at Madaina. Joseph Assemani says the patriarchs then lived at Baghdad, Timothy at the monastery of Kelilisho." The item is about why the card calls him "of Baghdad" when every held witness enthrones him at Seleucia or Madaina. "His name" does not say so, and next to `otherNames` ("Mar Timothy", "Timotheus") a reader expects the item to be about those forms. The facts are right: "intronisé à Séleucie" (CHABOT l.40258), "deduxerunt Seleuciam" (BH l.9612), "consecraverunt Modainae" (AMR l.13017), and Assemani on Kelilisho (card `place`, l.9). Fix, first sentence only: 'Why he is called "of Baghdad".' The other two sentences stand.

**Verdict: CLEAR on blocking points** (0 blocking, 1 minor, R3-C-M1, card only).

---

### Photius of Constantinople

| Finding | Verdict | Evidence |
|---|---|---|
| R2-C-M5 and C-M10 ("his rival" read as Nicetas's) | RESOLVED | Brief l.5: "Nicetas the Paphlagonian, who wrote the Life of Photius's rival, the patriarch Ignatius, was an enemy too." Card l.39: "Nicetas the Paphlagonian wrote the Life of Photius's rival Ignatius." The ambiguity is gone in both. C-M10 is now closed. |
| R2-C-M6 ("those"; Mansi heading) | RESOLVED | Card l.43: the note, "postremas istas duas actiones, nempe quae sexta & septima appellantur, confictas esse ab ipsomet Photio", with their "definitionem … nihil videlicet esse adjiciendum symbolo" (MANSI17 l.52604-52628); Nilus headed "Ex Nilo Rhodi metropol. schismatico" (l.38859). Both sentences parse, 21 and 14 words. |
| R2-C-M7 (punctuation) | RESOLVED | Card l.12 and l.45: `"to Assyria"` with the period outside. The source runs on, "ambassador to Assyria ^ had been confirmed" (FREESE l.1705-1706). |
| R2-C-M8 ("spatharius") | RESOLVED | Card l.34: "Basil's envoy, his sword-bearer". LP2 calls him "Basilius legatus imperatoris" (l.53422) and "spatharius" (l.53542). The next sentence's "He" still points to the envoy. |

**Unrequested change, checked.** Card `uncertain` 2 (l.39), "The Lives of the Popes call Photius an invader" (was "him"). PASS, and needed. After the R2-C-M5 fix the sentence before ends on "Ignatius", so "him" would have made Ignatius the invader. The Lives say it of Photius: "vituperando et invasorem Photium collaudando" (LP2 l.49596), "Photius neophitus ac invasor" (l.50734) and "invasorem Photium propulissent" (l.53428). R2's cite of l.49594 is two lines early; the words are at l.49596. The card's `remembered` 2 (l.32), "call him the invader of the see", rests on the same lines.

**Changed strings checked.** Brief l.5 and card l.12, 34, 39, 43 and 45: PASS. Audio carries l.5. I read the whole brief and card again. No AI tells, contrasts, tails or aphorisms. "Yet he calls Photius the first scholar of his age" turns on a real fact, a hostile witness's praise. "Was an enemy too" leans on P2's council that condemned him, which is its natural antecedent.

**New findings.** None.

**Verdict: CLEAR** (0 blocking, 0 minor).

---

### Counts

| Profile | Earlier findings | R3 blocking | R3 minor |
|---|---|---|---|
| Maximus the Confessor | 13 of 13 R1 resolved; R2 2 of 2 resolved | 0 | 0 |
| Martin I of Rome | 8 of 8 R1 resolved (A-M17 closed); R2 3 of 3 resolved | 0 | 1 (R3-A-M1, card) |
| Timothy I of Baghdad | 12 of 12 R1 resolved (C-M5 closed); R2 4 of 4 resolved | 0 | 1 (R3-C-M1, card) |
| Photius of Constantinople | 10 of 10 R1 resolved (C-M10 closed); R2 4 of 4 resolved | 0 | 0 |

### Verdicts

- Maximus the Confessor: CLEAR.
- Martin I of Rome: CLEAR on blocking points; one minor card fix, R3-A-M1, in final wording above. The two unrequested round 2 changes ("governor" in `uncertain` 7 and the Calliopas decree in `uncertain` 8) are faithful to Mansi 10.
- Timothy I of Baghdad: CLEAR on blocking points; one minor card fix, R3-C-M1, in final wording above.
- Photius of Constantinople: CLEAR. The unrequested "him" to "Photius" change is right.

Both minor fixes are in participant text (cards). Neither touches a brief or an audio script, so no readability or timing changes. Under the brief, any fix to participant text after this round goes to Mark for a cap ruling.
