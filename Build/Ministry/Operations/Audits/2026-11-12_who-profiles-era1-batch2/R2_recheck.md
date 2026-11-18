# R2 recheck: eight Who profiles, era 1 batch 2

Scope: only what changed, checked against `R1_review.md` and `R1_changes.md`. Unchanged text was not re-reviewed. Every new or changed quotation and every new factual claim the changes brought in was searched again in its vendored file with `wsfind.py` and read in context. No drafts were edited and no paid calls were made.

Mechanical checks, all eight:
- Each audio script matches its brief word for word once tags are removed. `[calmly]` opens and `[warmly]` comes before the closing line. No tags appear in the briefs or cards.
- `grade_text` passes for all eight. The highest FK is Tatian at 8.2. The lowest Flesch is Tacitus at 61.5.
- No sentence of the narrator's own prose in a brief runs past 25 words. The two long sentences are quotations, as in R1. Several new or changed card sentences run 26 to 33 words (N8).
- No new "not X but Y" construction appears in any brief or card.

| Profile | Words | Est. length | FK | Flesch | Cap |
|---|---|---|---|---|---|
| Tacitus | 311 | 1:55 | 7.9 | 61.5 | 324, within |
| Suetonius | 322 | 1:59 | 7.7 | 65.5 | 324, within |
| Tatian (major) | 405 | 2:30 | 8.2 | 61.7 | 405, at the cap |
| Bardaisan of Edessa | 320 | 1:59 | 8.0 | 63.3 | 324, within |
| Hippolytus of Rome (major) | 403 | 2:29 | 7.6 | 63.0 | 405, within |
| Novatian (major) | 400 | 2:28 | 8.0 | 62.7 | 405, within |
| Pontius the Deacon | 318 | 1:58 | 6.7 | 71.8 | 324, within |
| Dionysius of Alexandria (major) | 401 | 2:29 | 7.4 | 66.6 | 405, within |

Length assumes 162 words a minute. The Suetonius card's `briefLength` says "about 1 minute 55 seconds", but the brief now runs about 1:59 (N9).

## 1. The 6 R1 blocking findings

| Finding | Status | Note |
|---|---|---|
| Suetonius B1 (birth date told as settled) | RESOLVED | Card dates read "Born about 69 or about 77". The uncertain line gives Mommsen's 77 and Macé's 69 "with somewhat greater probability" (Rolfe l.155–158), and the Thomson-Forester preface's "towards the close of the reign of Vespasian" (l.45–47). records.json tags it Contested. All three match. |
| Tatian B1 (Harnack's outline told as fact; McGiffert's verdict and Hogg's return East left out) | RESOLVED | Card dates now rest on Eusebius's Chronicle (npnf201 l.26218–26222). The uncertain line gives Harnack and Zahn, McGiffert's verdict (l.26230–26233), Hogg's "after Justin's death left Rome and returned to Mesopotamia" (anf09 l.1958–1961), and McGiffert's one trustworthy point in Epiphanius (l.26211–26214). The brief now sends Tatian to Mesopotamia. There is a new contested_claim with both sides. McGiffert's hedge "seem fully to establish" has become "fully established" on the card and in records.json (N3). |
| Bardaisan B1 (dispute ended on Epiphanius; Eusebius cast as hostile) | RESOLVED | "Both writers against heresy" is gone. "A powerful defender of the faith" is exact (npnf201 l.26638). The paragraph now ends with McGiffert: "It is not improbable that he may, as Eusebius says, have been a Valentinian for a time" (l.26562 region). With Hort, McGiffert also says "There is no reason to think that he taught a system of æons like the Gnostics". "May well be right" and "finds no Gnostic system" are fair renderings of these. The card and contested_claim match. Epiphanius is now unmarked in the brief (N5). |
| Bardaisan B2 (opening quote altered) | RESOLVED | "What were you talking about?" he asked, "for I heard your voice outside as I was coming in." This is exact (anf08 l.67915). The sentence that frames it introduces a new error (NB1). |
| Novatian B1 (Acesius source shown as neutral) | RESOLVED | "Auxanon, an aged Novatian presbyter who had gone to Nicaea with Acesius" matches Socrates I.13 (npnf202 l.3855–3857). "Who wrote fairly of it" is gone. The card gives Baronius against Valesius, "followed by most of the more recent writers" (l.1034–1036), and Sozomen telling the story after Socrates. "Held him only impartial" is a slightly odd wording of Valesius's "extreme impartiality". |
| Pontius B1 (a role in place of a named witness) | RESOLVED | The card names "Ernest Cushing Richardson, in a note to his translation of Jerome". The translation is his (npnf203 l.688). The new Benson line on the same card brings in a new blocking fault (NB2). |

**All 6 are resolved.**

## 2. R1 minor findings

**Tacitus**
- M1: fixed. "Even for criminals who deserved the worst, he says, pity arose" follows l.68.
- M2: partly. The paragraph still opens on a verdict: "Tacitus was not a Christian, and he wrote of Christians with contempt." The dangling "them" is fixed.
- M3: fixed in the brief. The card keeps the Library-holding line under uncertain, which is acceptable.
- M4: fixed. "For a tale in his Histories about the Jews" matches anf03 l.10081–10094 and l.2570–2583, and Tertullian's "Cornelius Tacitus" is exact. "A century later" is new (N1).
- M5: fixed. Card `place` is removed.

**Suetonius**
- M1: fixed. Luke (Acts 18:2) and "Dio Cassius" now both appear, matching Thomson-Forester l.20376–20378.
- M2: partly. "Rolfe, for his part, notes" still frames Rolfe as answering Thomson and Forester. His note argues from "the absence of quodam" and does not mention their rendering (Rolfe l.25871). Drop "for his part".
- M3: fixed.
- M4: fixed. The contested_claim names both sides and says no vendored witness holds the other reading.
- M5: fixed.
- M6: fixed, with the gap logged. "Ambrose of Milan" is a Library identifier (npnf203 l.35171). The Betriacum context matches Thomson-Forester l.43–44 and n.744 (l.21345). Rolfe's "Roman writers who give us little information about themselves" (l.150) supports the new "Rolfe notes that he tells us little about himself". On the card, "the Life of Ambrose by his secretary Paulinus" has an unclear "his" after "John Rolfe, his translator" (N7).
- M7: reported, not changed. Correct.

**Tatian**
- M1: fixed.
- M2: fixed on the card. In the brief, "Irenaeus traces that group" refers back to the Encratites in general. McGiffert's point concerns only "the particular sect which Irenaeus describes" (npnf201 l.26305–26312). The card draws the distinction. Minor, since the brief does not misstate it badly.
- M3: fixed. McGiffert's reading is attributed, and Lightfoot appears on the card (l.26426–26432).
- M4: fixed in the brief ("It would seem, Hogg writes"). Partly on the card: legacy `traces` still has "Hogg ... concludes that" without his hedge.
- M5: fixed. Hogg: "an increasing majority of scholars" (anf09 l.1996). McGiffert: Harnack "has given very strong reasons" (l.26461).
- M6: fixed.
- M7: partly. "Marcion of Pontus" is fixed. "Saturninus" and "Harnack" are still bare in the brief.
- M8: fixed. Irenaeus is named for the hearer. Rome rests on Tatian's "when sojourning in the city of the Romans" (anf02 l.7252). Crescens is in Address 19 (l.6550).
- M9: fixed.

**Bardaisan**
- M1: fixed ("is said to have"). The card's new sentence stacks "Sozomen ... says his son Harmonius is said to have", which runs to 30 words (N8).
- M2: replaced by a new error (NB1).
- M3: fixed.
- M4: fixed.
- M5: fixed in part. Sozomen, Valentinus and Hort have context. Neander's "Abgar Bar Manu" matches anf08 l.68961. But it is given through "a note in the English edition", a role where a named witness should be (NB3). "Abgar, the ruler of Edessa" in the brief is acceptable.
- M6: fixed. Holl gives "im Jahr 533 (—221/2 n. Chr.)" (Holl l.26427).
- M7: fixed.

**Hippolytus**
- M1: fixed. "Never recognizes Callistus as bishop" (npnf201 l.35666). "Calls himself one" (l.35672–35676). Apostles' successors (anf05 l.1130).
- M2: fixed ("made away with money left in his bank", anf05 l.13685).
- M3: fixed.
- M4: fixed for the first mention and for Prudentius. "Zephyrinus" is still bare, which is acceptable.
- M5: fixed.
- M6: reported, not changed. Correct.

**Novatian**
- M1: fixed. The Acesius record names Auxanon and Sozomen.
- M2: fixed. The card's "sees no reason to doubt Novatian's word" is also supported: n.2117 reads "There is no reason to doubt, as Cornelius does, Novatian's ..." (npnf201 l.38463). Both lines now stand.
- M3: fixed.
- M4: fixed.
- M5: partly. Cornelius is now placed, and Lardner comes "quoted by Cleveland Coxe". "Neander", "Baronius" and "Valesius" still have no context. The new brief line "Robert Wallis, who translated his works, points this out" is supported by Wallis's Introductory Notice ("only from his enemies, the Roman bishop and his adherents", anf05 l.60349–60362). Neander's ascetic withdrawal is supported (npnf201 l.38717–38720).

**Pontius**
- M1: taken, but incomplete (NB2).
- M2: fixed. It is now in `absent_details`, which is correct.

**Dionysius**
- M1: fixed. "Among his reasons was its Greek" is right.
- M2: rewritten, but the sides are now mismatched (N6).
- M3: fixed. Jackson's note (npnf208 l.14425–14433) supports both "sowing the seeds of the Anomoean heresy" and "the Great". "Blomfield Jackson" is named at l.476. "Basil" has no identifier, and "Anomoean" has no context (N4).
- M4: partly. Origen of Alexandria, the emperor Gallienus, and Germanus's unknown see are fixed. "Sabellius's followers" still gives no gloss of Sabellius. "Nepos" on the card is still bare.
- M5: fixed.
- M6: fixed.

## 3. New or changed quotations, checked word for word

All exact:
- Bardaisan: "What were you talking about? for I heard your voice outside as I was coming in." (anf08 l.67915). "a powerful defender of the faith" (npnf201 l.26638). Card: "Philip and Baryama." (anf08 l.68337).
- Tatian: "It would seem" (anf09 l.1928). "very widely if not universally read in the Syriac churches." was unchanged and is exact. "I know not how." (npnf201 l.26425).
- Novatian: no new quotations. Socrates on Auxanon is paraphrased accurately (npnf202 l.3855–3857).
- Suetonius: no new quotations. "Another form of Christus." still matches Rolfe l.25871.
- Dionysius: card "the Great" (npnf208 l.14432–14433).
- Tacitus, Hippolytus and Pontius: no new quotations. The changed paraphrases are checked in section 2.

## 4. New faults in changed text

### New blocking

- **NB1 BLOCKING (Bardaisan, brief, opening).** "Philip and Baryama were calling on Shemashgram when Bardaisan came in. ... One of them, Avida, had asked why God did not make people unable to do wrong." The only people named before "One of them" are Philip and Baryama, so the listener hears Avida as one of those two. In the dialogue Avida is a third person. The narrators report "'Avida here,' said we to him, 'was saying to us ...'" (anf08 l.67915), and Bardaisan addresses the narrators as "O Philip and Baryama" (l.68337). This is wrong as heard. Fix: "With them was Avida, who had asked why God ...", or "Their companion Avida had asked ...".
- **NB2 BLOCKING (Pontius, card uncertain).** "Pontius says Cyprian sold his gardens for the poor. Archbishop Benson reports Otto Ritschl's view that they were confiscated later, and that Pontius mistook this for a sale." This reports Benson's witness and leaves out Benson's own verdict, which goes the other way. In his main text Benson follows Pontius: "To the sacrifice of his farms in their cause Cyprian did not hesitate to add that of his delightful Gardens. Friends bought them in" (Benson l.2878–2881). In the same footnote he objects to Ritschl: "Pontius' personal knowledge seems to present to him no difficulty, nor yet the question how the confiscation was taken off" (l.2901–2906). As written, the line leaves the doubt with the last word, though the named witness rejects it. This is the R1 dispute-outcome pattern (Tatian B1, Bardaisan B1). Fix: add "Benson rejects this, since Pontius knew Cyprian, and holds with Pontius that the gardens were sold."
- **NB3 BLOCKING (Bardaisan, card uncertain).** "A note in the English edition gives Neander's view that the Abgar named in it is Abgar Bar Manu." A role stands in for a named witness. Item 5 rules this out, and Pontius B1 was blocking in R1 for the same pattern. The Edessa section of anf08 is "Translated by the Rev. B. P. Pratten" (anf08 l.60770). The note is unbracketed, so it is most likely his, not Coxe's (Coxe's notes are bracketed). Confirm, then write "B. P. Pratten, who translated the dialogue, gives Neander's view ...".

### New minor

- **N1 (Tacitus).** "Tertullian of Carthage, who wrote to defend them a century later". No vendored line gives that interval. On the card's own date ("wrote after 96") the gap to Tertullian's To the Nations is nearer eighty to a hundred years. Write "about a century later", or drop the interval.
- **N2 (Tatian, brief).** "Eusebius of Caesarea dates the break to about 172. Hope Hogg ... says Tatian then left Rome for Mesopotamia." Hogg ties the move to "after Justin's death", not to the 172 break, and he says "returned" (anf09 l.1958–1961). "Then" places it after 172. Write "Hope Hogg ... says that after Justin's death Tatian went back to Mesopotamia."
- **N3 (Tatian, card and records.json).** "McGiffert thought Harnack's main positions fully established" drops the hedge in "seem fully to establish" (npnf201 l.26232). Write "thought Harnack's arguments seemed fully to establish his main positions". The contested_claim on the life also leaves out Hogg, though the claims row cites him.
- **N4 (Dionysius, card).** "Basil, in a letter" has no identifier. The Library form is "Basil of Caesarea" or "Basil the Great". "The Anomoean heresy" has no context. Jackson's note also reports Lumper's view that Basil's charge came from "imperfect acquaintance with his writings" (l.14428–14431). One clause would give the answer to the charge.
- **N5 (Bardaisan, brief).** Removing "both writers against heresy" also removed the only partisan marker on Epiphanius in the brief. The card has one ("who wrote against every heresy"), and the brief should carry it too. The opener "Eusebius ... and Epiphanius ... tell his story in opposite orders" still announces the dispute before telling it. It passes, since the next sentences tell it at once.
- **N6 (Dionysius, records.json).** The contested_claim reads "The apostle John did not write the Revelation". Its "against" side is "those before him who rejected it altogether and gave it to Cerinthus". Those people also denied the apostle wrote it, so they stand on the same side of this claim, not against it. They oppose only Dionysius's view that a holy John wrote it. Either restate the claim as "A holy John, not the apostle, wrote the Revelation", or set the sides against the brethren who esteemed the book. Not participant-facing, so this is minor, but the record should be fixed before it is written.
- **N7 (Suetonius, card legacy).** "John Rolfe, his translator, says ... the Life of Ambrose by his secretary Paulinus". Two "his" in a row point to different people. Write "by Ambrose's secretary Paulinus".
- **N8 (cards, sentence length).** New or changed card sentences run past 25 words: Suetonius legacy (33), Bardaisan traces (30, with a doubled "says ... is said"), Tatian uncertain (30 and 26), Dionysius uncertain (27), Novatian uncertain and remembered (27 each). The briefs are clean.
- **N9 (Suetonius, card).** `briefLength` "about 1 minute 55 seconds" should be about 2 minutes now that the brief is 322 words.
- **N10 (Tatian, card).** "Ephrem the Syrian wrote a commentary on it" now appears in both `traces` and `remembered`. Keep it once.

## Summary

| Profile | R1 blocking | Resolved | New blocking | New minor | R1 minors partly or not fixed |
|---|---|---|---|---|---|
| Tacitus | 0 | – | 0 | 1 (N1) | M2 partly |
| Suetonius | 1 | 1 | 0 | 2 (N7, N9) | M2 partly |
| Tatian | 1 | 1 | 0 | 3 (N2, N3, N10) | M2, M4, M7 partly |
| Bardaisan of Edessa | 2 | 2 | 2 (NB1, NB3) | 1 (N5) | M2 replaced by NB1 |
| Hippolytus of Rome | 0 | – | 0 | 0 | none |
| Novatian | 1 | 1 | 0 | 0 | M5 partly |
| Pontius the Deacon | 1 | 1 | 1 (NB2) | 0 | M1 incomplete (NB2) |
| Dionysius of Alexandria | 0 | – | 0 | 2 (N4, N6) | M4 partly |
| **Total** | **6** | **6** | **3** | **9 + N8 across cards** | |

All six R1 blocking findings are resolved. Three new blocking findings came in with the changes. Each is a one-sentence fix:
1. NB1 Bardaisan: "One of them, Avida" makes Avida one of Philip and Baryama, but he is a third person in the dialogue.
2. NB2 Pontius: the card gives Ritschl's doubt about the sale of the gardens through Benson, but leaves out that Benson rejects it and follows Pontius.
3. NB3 Bardaisan: "A note in the English edition" is a role where a named witness should be, most likely B. P. Pratten. Pontius B1 in R1 was the same pattern.

Hippolytus and Novatian are clear. Each new blocking fix is limited to one sentence, so a round 3 can be a recheck of those three sentences alone.
