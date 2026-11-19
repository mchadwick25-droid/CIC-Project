# R3 recheck: era 4 Who batch 7

This is round 3, the last of the three review rounds. A fresh Opus agent did it as a targeted recheck at full effort. The agent had not seen the drafting or the earlier rounds while they were under way. The recheck covers all seven profiles, `records.json` and the README.

## Method

Reviewer: independent Opus, first sight of these files. I edited no profile file. I made no git write and no web, paid or model call, and used local scripts and read-only git only. Inputs: `CLAUDE.md` in full, the review brief, `R1_review.md`, `R1_changes.md`, `R2_recheck.md`, `R2_changes.md`, era 4 batch 5's `R3_recheck.md` for form, the Decision-Log Who entries of 2026-11-12 to 2026-11-14 (among them "Minor round 3 fixes to reader-facing text get one targeted check without asking Mark"), and `git diff --word-diff 26e37f67~1 HEAD` over `Who-Profiles/era4/batch7/` (26e37f67 is "round 2 recheck and changes"; its parent dfcbeba6 is "README, pair length as the coordinator's call"). The working tree is clean for this folder.

For every R2 finding and every string changed in 26e37f67, I opened the cited lines again in the vendored file under `cic/texts/` and read them in context: what the line says, who says it, and when. While reading I folded OCR noise, hyphen breaks and Migne's two columns. I then read each brief whole, as a listener would, and each card against its sources. Short names follow R2: PG152, PHIL2, WILL, PAISIUS, GILES, PLUMMER, RAINE (Stephen's Life of Wilfrid in Raine's York volume 1), FOULKE, BUDGE13, CRUM. No brief fix is proposed, so no brief needed scoring on a scratch copy. The scripts are in `/tmp/claude-0/-home-user-CIC-Project/c61097dc-d787-5983-8ed0-252e6ba75c23/scratchpad/r3/`.

---

## 1. R2 findings

| Finding | Status | Evidence |
|---|---|---|
| R2-B1 (Cedd and Chad `knownFor`, Cynebil) | RESOLVED | The card reads "the monastery Cedd founded and Chad ruled after him", as the README does. Bede's preface: "how those fathers lived and died, we learned from the brethren of the monastery, which was built by them, and is called Lastingham" (GILES l.197-204), "them" being Cedd and Ceadda (l.198). The Latin keeps Cedd as subject: "petiit presbyterum suum Cynibillum ... pia coepta conplere. Cui cum ille libenter adquiesceret ... fecit ibi monasterium, quod nunc Laestingaeu uocatur ... ubi educatus erat", and the next "Qui" holds the see (PLUMMER l.20996-21004). The card's `legacy.traces` 1, "the monastery they built", follows the preface; the two do not conflict. A-M23 is settled with it. |
| R2-M1 (Symeon, Manuel Calecas placed) | RESOLVED, with R3-M1 | The PG152 header: "Manuelis Calecae ordinis Fratrum Praedicatorum"; the content note lists his De essentia et operatione among the anti-Palamite works; the note sits inside "DE ESSENTIA ET OPERATIONE" (running heads to l.29181), against "μοναχῶν, ἀρετὴν ὑποκρινομένων, ἀλόγων καὶ πεπλανημένων" and the note "Symeonem notat ejusque discipulos" (l.29294-29305). "a Dominican who wrote against the Palamites" holds. The insertion makes a nested sentence (R3-M1). |
| R2-M2 (Niketas `dates`, the eleventh year) | RESOLVED | WILL note 2: "Quod in aliis exemplis, Anno undecimo imperii Constantini Monomachi legitur, id non forte factum est, sed" (l.14797) "errore chronologico. Multi enim legationem ad a. 1653 [1053] referunt, sed quum anno demum 1054 legati missi sint" (l.14832). Variant "C. undecimo" at l.14779. "Will puts this down to an error in dating, since many placed the embassy in 1053" is Will's own reasoning, said as his. The records addition quotes l.14797 and l.14832 verbatim. A-M15 is settled with it. |
| R2-M3 (Niketas `legacy.traces` 2, the skete) | RESOLVED, with R3-M2 and R3-M3 | The monk lives in the skete of Saint Basil under the hill of Elijah (PAISIUS l.10172-10177); Paisius asks "суть ли въ васъ"; the monk answers "Святаго же Никиты Стифата точно двадесять и двѣ главы, а цѣлая въ насъ, рече, не обрѣтается" (l.10216-10218). "in Greek" holds: Paisius was seeking the fathers "на эллиногречестѣмъ языцѣ" (l.10159-10160), and the monk says such books are written "самымъ чистымъ эллиногреческимъ языкомъ" (l.10224-10225). The older Slavonic "части нѣкоторыя тріехъ сотницъ" is at l.10489-10491. The change lifts the sentence to 29 words (R3-M2), and the records witness does not cover the skete (R3-M3). |
| R2-M4 (Cedd and Chad P4, Theodore) | RESOLVED | "Theodore of Tarsus came as the new archbishop. When he told Chad he had not been properly consecrated, Chad offered to resign, "for I never thought myself worthy of it."" GILES l.8883-8888: "when he upbraided Bishop Chad that he had not been duly consecrated, he, with great humility, answered, "If you know I have not duly received episcopal ordination, I willingly resign the office, for I never thought myself worthy of it"". The quote is Chad's, said to Theodore, and verbatim. "he" in the second sentence can only be Theodore, the first sentence's subject. Longest sentence now 22 words. |
| R2-M5 (Paul the Deacon P3, Foulke owns the homilies) | RESOLVED | "By the king's order, Foulke adds, he gathered a book of the church fathers' sermons, perhaps begun at court and finished at Monte Cassino." FOULKE l.808-812: "the collection and revision of the homilies of the fathers of the church which he made by order of the king, and which was possibly commenced about this time, though not completed until after his return to Monte Cassino." Foulke owns it, and "perhaps" keeps his "possibly". 24 words. |
| R2-M6 (Pisentius P1, "I think") | RESOLVED | "Pisentius said he thought there was water in one of the vessels, which they had forgotten." BUDGE13 l.17231-17233: "he said unto me, 'I think there is water in the water-vessels, in one of them which we have forgotten.'" The speaker is Pisentius, to John, on the mountain of Djeme. The hedge is back in his mouth, and "they" renders his "we". |
| R2-M7 (README, letters to and from) | RESOLVED | "beside letters to and from a bishop of his name among the Epiphanius papers" now matches the card's `keyWorks` and its warning that "not every Pesenthius in them is the bishop". "his name" can only be Pisentius's. |
| R2-M8 (README, the pair-length call) | FELL AWAY, as briefed | The README says: "That pairs may run to the 2:30 cap, which stays a cap and not a target, is the coordinator's call (2026-11-14), which Mark may overrule." It states the call as the coordinator's, open to Mark's overrule. Noted for the coordinator, not a finding: `R2_changes.md` says "the batch's Decision-Log entry records it", but the Decision Log at HEAD has no era 4 batch 7 entry yet. The closing entry should carry the ruling, both halves (pairs to the 2:30 cap; single non-majors about 2:15 at most). |

---

## 2. New findings

### Blocking

None.

### Minor

- **R3-M1 MINOR (`symeon-the-new-theologian` card `legacy.remembered` 2; participant text; nested sentence, made by the R2-M1 wording).** "In a note, Combefis reads the deluded monks that Manuel Calecas, a Dominican who wrote against the Palamites, attacks as Symeon and his disciples." The appositive, with its own relative clause, now sits between "Manuel Calecas" and his verb "attacks", inside a "reads X as Y" frame. A reader loses the verb. That is the nesting CLAUDE.md names. The facts stand (PG152 header; l.29294-29305).
  - Fix: "In a note, Combefis reads the deluded monks that Manuel Calecas, a Dominican who wrote against the Palamites, attacks as Symeon and his disciples." -> "Manuel Calecas, a Dominican, wrote against the Palamites. In a note, Combefis reads the deluded monks that Calecas attacks as Symeon and his disciples." (8 and 16 words.)
- **R3-M2 MINOR (`niketas-stethatos` card `legacy.traces` 2; participant text; a sentence past ~25 words, lengthened by the R2-M3 wording).** "A monk in a skete on Athos told him the skete held only twenty-two in Greek, and Paisius says the older Slavonic had only parts of the three hundreds." runs 29 words, up from 27. It joins two claims from two places in Paisius (l.10216-10218; l.10489-10491).
  - Fix: "A monk in a skete on Athos told him the skete held only twenty-two in Greek, and Paisius says the older Slavonic had only parts of the three hundreds." -> "A monk in a skete on Athos told him the skete held only twenty-two in Greek. Paisius says the older Slavonic had only parts of the three hundreds." (16 and 12 words; "him" follows "Paisius Velichkovsky" in the item's first sentence.)
- **R3-M3 MINOR (`records.json`, `niketas-stethatos`, the claim "A monk in a skete on Athos ..."; records only; witness short of the claim).** The claim now places the monk in a skete and the chapters in Greek, but its witness, "l.10217-10218, 10487-10494", covers neither. The skete is at l.10172-10177; the Greek at l.10159-10160 and l.10224-10225.
  - Fix, `witness`: "PAISIUS (paisius-velichkovsky_zhitie-i-pisaniia-chu_optina1847.txt) l.10217-10218, 10487-10494" -> "PAISIUS (paisius-velichkovsky_zhitie-i-pisaniia-chu_optina1847.txt) l.10159-10160, 10172-10177, 10216-10218, 10224-10225, 10487-10494".
- **R3-M4 MINOR (README, third paragraph; batch text; numbers stale after the fixes).** "His brief runs 405 words, about 2:30" — Symeon's brief has run 404 words since d27451b7 (round 1 part A). "Niketas Stethatos, Paul the Deacon and Paulus Emeritanus run 348 to 363 words, about 2:09 to 2:14" — Paul the Deacon is now 365 words, about 2:15, after R2-M5. "The three paired profiles run 389 to 399 words, about 2:24 to 2:28" — Cedd and Chad is now 392, about 2:25, after R2-M4, and Pisentius 400, about 2:28, after R2-M6 (the batch's own counter, as in `R2_changes.md`; it counts the two dashes inside the closing Budge quotation, so `wc -w` gives 398).
  - Fix: "His brief runs 405 words, about 2:30." -> "His brief runs 404 words, about 2:30."; "run 348 to 363 words, about 2:09 to 2:14." -> "run 348 to 365 words, about 2:09 to 2:15."; "The three paired profiles run 389 to 399 words, about 2:24 to 2:28," -> "The three paired profiles run 392 to 400 words, about 2:25 to 2:28,".

Considered, and not a finding:
- Pisentius P1: after R2-M6, "which they had forgotten" puts "they" (Pisentius and John) just before "John found them full to the brim". "full to the brim" can only be said of the vessels, so no listener takes "them" as the two men. The plural follows Budge's "I found them filled with water up to their brims" (l.17239-17240).
- Cedd and Chad P4: "Even so, Stephen calls him a true and most gentle servant of God." The words are Stephen's for Chad, "Ille vero servus Dei verus et mitissimus" (RAINE l.5630), right after he says Theodore had "Ceaddam" removed (l.5627-5628). The card's "most religious servant of God and an admirable teacher" is a second line of Stephen's (l.5540-5542). Unchanged since R1.
- Symeon P1, "he tells it as another monk's story": PHIL2 has "ὡς περί τινος ἄλλου ... ἤκουσα, φησί, παρά τινος Μοναχοῦ ἱερέως" (l.23058-23062), so the other man is a monk-priest in Symeon's own framing.
- Paul the Deacon P3 has "Foulke says" and then "Foulke adds" in consecutive sentences. Each is a different claim from Foulke (l.740-745, 808-812). This is a wording preference.
- Niketas card `traces` 2, "in Greek": the monk names no language, but the passage is framed by Paisius's search for the Greek books and the monk's word that they are in pure Greek (PAISIUS l.10159-10160, 10224-10225). Supported; R3-M3 adds the lines to the record.
- The Pisentius closing quotation carries two dashes, "whatsoever thou givest — everything — to the poor". They are Budge's, verbatim (BUDGE13 l.18508), and are not narrator dash fragments.

---

## Changed strings checked

Every string changed in 26e37f67, against its lines:

| File, field | Result |
|---|---|
| cedd-and-chad card `knownFor` | PASS (GILES l.197-204; PLUMMER l.20996-21004) |
| cedd-and-chad brief P4, and audio | PASS (GILES l.8883-8888; the quote verbatim) |
| symeon card `legacy.remembered` 2 | PASS for the source; nested sentence (R3-M1) |
| niketas card `dates` | PASS (WILL l.14779, 14797, 14832) |
| niketas card `legacy.traces` 2 | PASS for the source; 29 words (R3-M2) |
| niketas records, recantation claim | PASS (WILL l.14797, 14832, verbatim) |
| niketas records, the skete claim | PASS for the claim; witness short (R3-M3) |
| paul-the-deacon brief P3, and audio | PASS (FOULKE l.808-812) |
| pisentius brief P1, and audio | PASS (BUDGE13 l.17231-17240) |
| README, "The pairs", Pisentius | PASS (the card's `keyWorks`, from CRUM) |
| README, opening, the pair-length call (dfcbeba6) | PASS; word counts stale (R3-M4) |

In the changed strings every witness stays attached: "Foulke adds", "Will puts this down", "said he thought". No hedge is dropped or added. The pronouns resolve. No changed string adds a quotation, a contrast frame, a triad, a colon reveal or a tail. No changed string tells an editor's view as settled. No changed string claims an absence.

---

## Mechanical checks

By script, on the files as they stand.

| Profile | Words | Time @162 | FK | Flesch | `briefLength` | Audio = brief + tags | Longest brief sentence |
|---|---|---|---|---|---|---|---|
| symeon-the-new-theologian (major) | 404 | 2:30 | 7.62 | 66.19 | about 2 minutes 30 seconds | yes (1 calmly, 1 warmly) | 24 |
| niketas-stethatos | 354 | 2:11 | 8.87 | 62.79 | about 2 minutes 15 seconds | yes | 26 (P4, Humbert, unchanged) |
| cedd-and-chad (pair) | 392 | 2:25 | 6.18 | 75.61 | about 2 minutes 30 seconds | yes | 27 (P1, Lent, ends in a quote, unchanged) |
| elipandus-of-toledo-and-felix-of-urgell (pair) | 399 | 2:28 | 6.74 | 73.92 | about 2 minutes 30 seconds | yes | 26 (P6, Agobard, unchanged) |
| paul-the-deacon | 365 | 2:15 | 5.95 | 75.52 | about 2 minutes 15 seconds | yes | 24 |
| paulus-emeritanus | 348 | 2:09 | 6.23 | 75.55 | about 2 minutes | yes | 23 |
| pisentius-of-coptos-and-john-the-elder (pair) | 400 | 2:28 | 6.20 | 78.81 | about 2 minutes 30 seconds | yes | 32 (P4, mostly quotation, unchanged) |

- All seven pass `grade_text` (FK 10 or below, Flesch 60 or above). The figures match `R2_changes.md`. Niketas keeps the thinnest Flesch margin, 62.79. No R3 fix touches a brief.
- Each audio file equals its brief with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph, one of each. No tag is in a brief or card.
- `records.json` and all seven cards parse as JSON. `records.json` holds exactly the seven ids. Every card keeps the batch's field order, with no empty or null field (Cedd and Chad has no `keyWorks`).
- Quotations: 18 double-quoted strings in the briefs (Cedd and Chad 7, Paul the Deacon 3, Pisentius and John 8) and one in a card (Pisentius `dates`, "this fifth year"). A script checked each against the files its card cites, with case, punctuation, line breaks and hyphen breaks folded. All 19 match, in GILES, FOULKE and BUDGE13. Symeon, Niketas, Elipandus and Felix, and Paulus quote nothing; their Greek and Latin are told in modern words without quotation marks.
- Spelling: no British spelling in narrator or card text. "honour" stands only inside a Budge quotation.

---

## Each brief read whole

I read each brief once more as a listener, start to end.

- **Symeon.** The ordination opening keeps Symeon's own telling and Niketas's naming apart. The Stephen paragraph, the exile and Sergius's words are each owned by Niketas. "he thinks" in the close is Symeon's. No new fault; on the card, R3-M1.
- **Niketas.** The 1054 scene, the chapters on tears and humility, Will's suspicion and Le Quien's reasoning are each owned. No new fault; on the card, R3-M2.
- **Cedd and Chad.** The new P4 split reads cleanly: Theodore arrives, then speaks. "He left Lastingham to Chad" follows a paragraph whose subject is Cedd. No new fault.
- **Elipandus and Felix.** Unchanged since R2. The teaching is told from Elipandus's letter and the opponents' reading as theirs. No fault.
- **Paul the Deacon.** The homilies now stay Foulke's. The wolf, the ash tree and the closing quotation hold. No new fault.
- **Paulus Emeritanus.** Unchanged since R2. Tamayo owns the dating. No fault.
- **Pisentius and John.** "said he thought" puts the wonder back in John's eyes. "Some things John only heard, and he says so" and Budge's reading of the letter and the indiction are owned. No new fault.

No brief has hedging filler, a colon reveal outside a quotation, a rhetorical question, an aphorism, a beat line or process narration. No paragraph opens on a thesis.

---

## 3. Verdicts

| Profile | R2 findings | New blocking | New minor | Verdict |
|---|---|---|---|---|
| Symeon the New Theologian | R2-M1 resolved | 0 | 1 (R3-M1, card) | CLEAR |
| Niketas Stethatos | R2-M2, R2-M3 resolved | 0 | 2 (R3-M2, card; R3-M3, records) | CLEAR |
| Cedd and Chad | R2-B1, R2-M4 resolved | 0 | 0 | CLEAR |
| Elipandus of Toledo and Felix of Urgell | none open | 0 | 0 | CLEAR |
| Paul the Deacon | R2-M5 resolved | 0 | 0 | CLEAR |
| Paulus Emeritanus | none open | 0 | 0 | CLEAR |
| Pisentius of Coptos and John the Elder | R2-M6 resolved | 0 | 0 | CLEAR |
| README.md | R2-M7 resolved; R2-M8 fell away, stated as the coordinator's call | 0 | 1 (R3-M4) | CLEAR |

**Totals.**
- Earlier findings resolved: 8 of 8 open R2 findings (R2-B1, R2-M1 to R2-M7). R2-M8 fell away on the coordinator's ruling, and the README states it as the coordinator's call, which Mark may overrule. A-M15 and A-M23, the two R1 items left open in R2, closed with R2-M2 and R2-B1. None is open.
- New blocking: 0.
- New minor: 4. R3-M1 and R3-M2 are participant text on cards; R3-M3 is records only; R3-M4 is the README's word counts.
- Every quotation in the briefs and cards matches its vendored file. Every brief passes `grade_text`. Every audio file equals its brief plus the tags.
- All seven profiles and the README are CLEAR.

**Cap note.** This is round 3, the last of the three review rounds the cap allows on each profile. No blocking finding is open, so nothing has to escalate. Under Mark's standing ruling of 2026-11-14 ("Minor round 3 fixes to reader-facing text get one targeted check without asking Mark"), R3-M1 and R3-M2 are applied as worded, with one targeted Opus check of only those strings by an agent that has not seen the drafting or the earlier rounds; that check does not count toward the cap. R3-M3 (records) and R3-M4 (README numbers) are applied as worded and can be read in the same check. No brief or audio file changes. The batch's Decision-Log entry, when written, should record the coordinator's length ruling. Nothing in this batch closes until Phase Five boundary testing and full-system review are complete.
