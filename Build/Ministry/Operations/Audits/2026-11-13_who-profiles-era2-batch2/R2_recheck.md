# R2 recheck: nine Who profiles, era 2 batch 2

Scope: only what changed, checked against `R1_review.md` and `R1_changes.md`. The text that did not change was not reviewed again. The changes were read as a word diff from `c9cdb724` (the parent of the checkpoint `3df8723a`, the drafts as R1 saw them) to `dca26768` on branch `who-profiles-era2-batch2`. Every new or changed quotation, and every new factual claim the changes brought in, was searched again in its vendored file with a whitespace- and hyphen-tolerant matcher (XML tags stripped) and read in context. Latin (Kauffmann's Auxentius, Bruns's Braga canons, Schepss's Orosius heading) and German (Kauffmann) were read in the original. I did not edit the drafts, and I made no paid calls, model-API calls or web requests. Line numbers point to files under `cic/texts/` unless another path is given.

Mechanical checks, all nine:
- Each audio script equals its brief once the opening `[calmly] ` and the single `[warmly] ` are removed (checked by script). In every script `[warmly]` sits before the closing sentence only. Macrina R1 M3 is fixed.
- `grade_text` passes for all nine (FK at most 10, Flesch at least 60). Eunomius (60.2), Apollinaris (60.3), Damasus (60.4) and Ulfila (60.4) sit just above the Flesch floor.
- Narrator sentences in the briefs: one new sentence runs 26 words (Priscillian, N6). Several new or changed card sentences run 26 to 40 words (N6).
- `briefLength` matches on all nine.

| Profile | Words | Est. length @162 | FK | Flesch | Cap |
|---|---|---|---|---|---|
| Ulfila (MAJOR) | 405 | 2:30 | 8.3 | 60.4 | 405, at the cap |
| Auxentius of Durostorum | 317 | 1:57 | 8.0 | 62.3 | 324, within |
| Eunomius of Cyzicus (MAJOR) | 403 | 2:29 | 8.0 | 60.2 | 405, within |
| Macrina the Younger | 324 | 2:00 | 6.4 | 76.7 | 324, at the cap |
| Damasus of Rome (MAJOR) | 402 | 2:29 | 8.2 | 60.4 | 405, within |
| Priscillian (MAJOR) | 405 | 2:30 | 7.6 | 63.6 | 405, at the cap |
| Tyconius | 323 | 2:00 | 7.4 | 65.1 | 324, within |
| Cyril of Jerusalem (MAJOR) | 405 | 2:30 | 7.3 | 66.0 | 405, at the cap |
| Apollinaris of Laodicea (MAJOR) | 403 | 2:29 | 8.2 | 60.3 | 405, within |

## 1. The 7 R1 blocking findings

| Finding | Status | Evidence |
|---|---|---|
| Macrina B1 (Jackson cited as following Gregory of Nyssa; Gregory of Nazianzus hidden) | RESOLVED | Card trace #1 now gives Gregory of Nyssa, then "Gregory of Nazianzus, Basil's friend, says Basil had already resolved on that life", then Jackson "gives both, and reads Macrina as giving Basil the resolve to carry it out". This matches npnf208 l.1253–1264 ("Basil had already determined to renounce the world ... indebted to the persuasion and example of his sister Macrina for the resolution, with which he now carried out the determination"). records.json tags the claim Contested, and a new contested_claim names all three. |
| Damasus B1 (366 told as settled) | RESOLVED | Brief: "followed Liberius as bishop, in 366 or 367". Card dates give 366 for the Avellana account and 367 for Jerome's Chronicle "as A. C. Zenos cites it". Zenos's note says Jerome "puts the consecration ... in the third year of Valentinian's reign, i.e. in 367" (npnf202 l.14181–14184). knownFor has "366 or 367". Claim 1 in records.json no longer carries a year and points to the contested record. See N5 on "the Avellana account" at first mention. |
| Priscillian B1 (card dates tell the Saragossa condemnation plainly) | RESOLVED | "Sulpicius Severus says he was condemned at Saragossa, which he denied". This matches npnf211 l.11504–11508 and Tractate II (Schepss l.4381–4384). Richardson's "condemned 380" is gone. |
| Priscillian B2 (Orosius and Braga given as neutral; caveat missing from the brief) | RESOLVED | The brief now has "His teaching comes to us mostly through his enemies". Orosius "wrote to Augustine of Hippo against the Priscillianists", which the Commonitorium heading bears out ("DE PRISCILLIANISTIS", Schepss l.10186). Braga is "Long after, in 561". The card's first uncertain item opens on the same sentence. The new sentence raises a smaller problem of its own (N3). |
| Tyconius B1 (Augustine not placed) | RESOLVED | Brief: "Augustine of Hippo, a Catholic bishop who wrote against the Donatists" at first mention. The card places him the same way at its first mention (legacy traces) and in uncertain #1. The record witness matches. See N4 on a pronoun the split brought in. |
| Cyril B1 (Theodoret heading quoted inexactly, from a work not in Sources) | RESOLVED | The quotation marks are gone: "Theodoret of Cyrus, in his Dialogues, cites the fourth lecture as a testimony of Cyril, bishop of Jerusalem." The heading is at npnf203 l.24428–24431, inside Dialogue II, "The Unconfounded" (l.21085–21088). The Theodoret source title now lists the Dialogues. |
| Cyril B2 (false "No source gives his birth, family or schooling") | RESOLVED | "No source used here gives his birth, parents or schooling. Gifford names one relative, his sister's son Gelasius, whom Cyril made bishop of Caesarea." This matches npnf207 l.586–588 ("appointed by Cyril to be Bishop of Cæsarea"). The absent_details record matches. |

**All 7 are resolved.**

## 2. R1 minor findings

**Ulfila**
- M1: RESOLVED. "In 383, by Kauffmann's date, the emperor summoned the bishops to Constantinople. Ulfila went, meaning to debate a rival party, but fell ill there and died." This follows Kauffmann l.3702–3706 ("der kaiserlichen aufforderung an die bischöfe folgend ... mit den ... Pneumatomachen ... zu disputiren"). The record names Sievers against Bessell (n. 2, l.3718–3719).
- M2: RESOLVED. "The span of the saints he followed" renders "quorum sanctorum imitator erat" (Auxentius 60, l.15278–15280).
- M3: RESOLVED. "Who was hostile to it" (Walford l.52).
- M4: RESOLVED in the brief and on the card. The paragraph opens "Socrates, a Nicene historian, says". The card's uncertain #1 opens on Auxentius.
- M5: RESOLVED in form, but the new sentence is false against the Library (NB1).
- Drafter's own fix, the Sozomen hedge: holds. Sozomen gives two reasons, "Compelled by the urgency of the occasion, or, possibly, thinking ..." (npnf202 l.40168–40169), and only the second carries "possibly". The quotation is exact.

**Auxentius of Durostorum**
- M1: RESOLVED.
- M2: RESOLVED. "In the party its foes called Arian" fits Kauffmann's report that the party refused the name "Arianer" (l.3812–3813). Maximinus is "a bishop of the same party".
- M3: RESOLVED. Ambrose's On the Faith in a fifth-century Paris manuscript matches Kauffmann l.509–512 and l.683–692 ("prachtvoller unciale des 5. jh.").
- M4: RESOLVED, as for Ulfila M2.
- M5: RESOLVED. The card now separates Kauffmann's own guess about the Moesian readers from what he shares with Bessell (l.3474–3477).
- M6: RESOLVED. (a) The paragraph opens "In Kauffmann's day, W. Luft held". (b) The one-sided sentence about the readers was cut, and card uncertain #2 gives both sides.

**Eunomius of Cyzicus**
- M1: RESOLVED. "Socrates, a Nicene opponent".
- M2: RESOLVED in the form the reviewer allowed. The brief adds "Philostorgius says he was later moved to Tyana". records.json splits the burial from the move, and "God knows no more" is retagged Documented as one hostile witness. See the not-taken judgments below.
- M3: RESOLVED. "Socrates of Constantinople" in `dates`. Theodoret is "Theodoret of Cyrus, another church historian", and Zenos's note names him (npnf202 l.12485–12488).
- M4: RESOLVED. The bishopric date is now one sentence, and the paragraph reads as an account.
- Drafter's own fix, "Some of his clergy": holds (Walford l.246, "SOME individuals of the clergy").
- The Photius sentence was rewritten and lost its place (N1).

**Macrina the Younger**
- M1: RESOLVED. "Healings" in the brief and on the card. Uncertain #4 adds the soldier's story (Clarke l.348–380) and Gregory's leaving out of more wonders, the corn among them (l.384).
- M2: RESOLVED, with a contested_claim added (see the not-taken judgments).
- M3: RESOLVED.
- M4: RESOLVED. "Peter of Sebaste" (Clarke l.44).
- M5: RESOLVED.

**All five, part B (G-M1)**: RESOLVED. Sozomen is "a church historian of the fifth century" at his first mention on the Damasus, Cyril and Apollinaris cards. The first mentions were checked by searching each card.

**Damasus of Rome**
- M1: RESOLVED. "An account from Ursinus's side". The card author is "Anonymous, from Ursinus's party".
- M2: RESOLVED. "Zenos's note calls him 'a Spaniard by race, native of Mantua'" is exact (npnf202 l.14195, "Damusus was a Spaniard by race, native of Mantua").
- M3: RESOLVED. "A soldier and historian, most likely a pagan" (Yonge l.750–752).
- M4: RESOLVED. "Sozomen ... tells it the same way after him" (Hartranft's note, npnf202 l.38775, "Soc. iv. 29; Ruf.").
- M5: RESOLVED. "One comfort was that".

**Priscillian**
- M1: RESOLVED. "Given himself up to lewd teachings" (npnf211 l.11668). The card's version is exact in substance.
- M2: RESOLVED. "Bold, talkative and given to pleasure".
- M3: RESOLVED. Canons VI and IX each name Priscillian ("sicut Priscillianus dixit"; "sicut pagani et Priscillianus dixerunt", Bruns l.2512–2515, l.2529–2531).
- M4: RESOLVED. Documented, with "Sulpicius II.50 only; hostile; reports the court of Evodius".
- M5: RESOLVED. Martin of Tours was dropped from `remembered`.
- Trims: cutting the Ydacius sentence leaves no dangling reference in the brief. Ydacius stays on the card, placed "of Emerita".

**Tyconius**
- M1: RESOLVED, but the split leaves an unclear "his" (N4).
- M2: RESOLVED.
- M3: RESOLVED. The one-sided contested_claim was removed. Augustine's verdict is a Documented claim in his name, and Tyconius's lost case is an absent detail.

**Cyril of Jerusalem**
- M1: RESOLVED. "Jerome says he held his see eight years under Theodosius" (npnf203 l.41502–41504, "held the episcopate for eight consecutive years, in the reign of Theodosius"). "Gifford dates his death to 386" matches npnf207 l.1361–1363.
- M2: RESOLVED. Both label sentences are gone. "Sozomen, who says he looked into why Acacius deposed him" reads cleanly.

**Apollinaris of Laodicea**
- M1: taken in another form, and right (see below).
- M2: RESOLVED. The card dates have "377, by Lietzmann's date". A new uncertain item gives Hartranft's note, "377 (Rade), 374 (Hefele)" (npnf202 l.39033–39034).
- M3: RESOLVED. "Says were generally counted among his best works" (npnf203 l.41396–41397, "generally considered as among the best of his works").
- M4: RESOLVED. All three items lead with their witnesses.
- Drafter's addition, "Richardson's note gives about 390": exact (npnf203 l.41393, "died about 390"). Richardson is placed earlier on the same card.

## 3. Not taken: judgments

| Item | Drafter's reason | Judgment |
|---|---|---|
| Eunomius M2, no contest over the burial; "Where his body lay" removed | The witnesses tell a sequence, not a conflict | HOLDS. Sozomen has him "interred at Dacora, his birthplace" (npnf202 l.41531–41532). Philostorgius has Eutropius "transfer Eunomius from the Dacoroenian territory to Tyana", and "would not suffer his body even to be laid in the same tomb with the master" (Walford l.410). The move presumes the first burial. The brief gives both in order, each attributed. |
| Eunomius M2, no contested_claim for the Socrates quotation | The Apology's silence is not a counter-witness | HOLDS. The reviewer offered the retag as an alternative, and the record now says the held Apology "does not speak to the point either way". |
| Macrina M2, the family-size item kept | Clarke does not resolve it | HOLDS. Clarke has ten children, nine surviving infancy (l.44). Moore and Wilson have the father "leaving a family of ten children, five of whom were boys and five girls" (npnf205 l.490–491). The two do not agree, so a contested_claim is right. |
| Apollinaris M1, "names only one of them" in place of "names only the son" | Sozomen does not say father or son | HOLDS. Sozomen V.18 says "Apolinarius the Syrian" only (npnf202 l.36685). Taking him for the son is Lietzmann's reading, and the card names Lietzmann for it. The plays and odes are at l.36697–36699. |
| Damasus M4, Rufinus left off the card | Taken in substance; Rufinus would need context | HOLDS. The dependence is shown on the card ("after him"), and the record names Rufinus. |
| Damasus B1, "in 366 or 367" in the brief | The Gesta is not yet introduced at that point | HOLDS. Neither year is told as settled, and both witnesses are named on the card. |
| Priscillian B1, Richardson's "condemned 380" dropped | It restates Sulpicius's side | HOLDS. This is the reviewer's own fix. |

## 4. New or changed quotations, checked word for word

All exact: Sozomen on Ulfila "possibly, thinking that it was better to hold such views concerning the Divine nature" (npnf202 l.40168–40169). Zenos "a Spaniard by race, native of Mantua" (npnf202 l.14195). Theodoret's heading, now unquoted, as above. Sulpicius "given himself up to lewd doctrines", rendered in the brief as "teachings" outside the quotation marks (npnf211 l.11668). No new quotation fails.

## 5. New findings in changed text

### New blocking

- **NB1 (Ulfila, card uncertain #3, `ulfila.card.json` l.40, and records.json `absent_details` l.235).** The changed item reads "No source in the Library names Eusebius's see in this account." The Library does. Louis Duchesne, Histoire ancienne de l'Église, vol. 2, tells the same embassy and consecration: "Eusèbe de Nicomédie le vit, et, augurant bien de ses aptitudes, le consacra évêque pour sa nation" (`duchesne_histoire-ancienne-de-leglise-tome2-fra_3e-ed1907.txt` l.20993–20995). Kauffmann, the card's own editor, ties the consecration to the Eusebian synod of Antioch in 341 (l.3809–3811). He says that Eusebius of Nicomedia, then bishop of Constantinople, was there and led it (l.2754–2756). "In this account" does not save the sentence: Duchesne's is an account of the same event. This is the R1 Cyril B2 type, a false "no source" claim against the Library. It also means R1 M5's identifier was available after all. Fix: "Philostorgius gives no see. Louis Duchesne names him Eusebius of Nicomedia, and Kauffmann's synod of Antioch in 341 was led by Eusebius of Nicomedia." Add Duchesne to the card's sources. Remove the absent_details entry, or rewrite it to say Philostorgius names no see.

### New minor

- **N1 (Eunomius, brief l.3).** "His history survives mainly in a summary by Photius, a later and hostile patriarch." The rewrite dropped "of Constantinople", so Photius has no see at his first and only mention in the brief. "His" now follows a sentence that ends on "Aetius of Antioch" and whose subject "he" is Eunomius, so a listener cannot tell whose history is meant. "Hostile" also has no object. The Ulfila brief has the clean form. Fix: "Philostorgius's history survives mainly in a summary by Photius, a later patriarch of Constantinople who was hostile to it."
- **N2 (Eunomius, card, Theodoret's place).** "Theodoret of Cyrus" rests on npnf203 (l.2337), which is not among the card's sources. The drafter reported this. It is not wrong, but the source list should include the file the identifier comes from. Fix: add npnf203 to the Eunomius card's sources, or let Zenos's note carry the bare reference.
- **N3 (Priscillian, brief l.9 and card uncertain #1, `priscillian.card.json` l.39).** "His teaching comes to us mostly through his enemies" comes straight after the paragraph on the eleven treatises Schepss judged to be Priscillian's own: his book to Damasus, and his curse on Mani. A listener has just heard his own words, then hears that his teaching comes mostly through enemies. What comes through enemies is the teaching he was condemned for: the souls passing through evil powers, and the stars. The wording is R1's own proposal. As placed, though, it overstates the case. Fix: "The teaching he was condemned for comes to us through his enemies." Use the same wording on the card.
- **N4 (Tyconius, brief l.3).** The split reads "F. C. Burkitt edited the Book of Rules. He says the little known of his life comes chiefly from Augustine of Hippo". With "He" now standing for Burkitt, "his life" points to Burkitt. Fix: "He says the little known of Tyconius's life ...".
- **N5 (Damasus, card `dates`, `damasus-of-rome.card.json` l.8).** "By the Avellana account's date" is the card's first mention of the account. The card explains the Collectio Avellana only later, in uncertain #1 (l.40), and `dates` is read first. Fix: "by the date of the anonymous account from Ursinus's party in the Collectio Avellana", or "by the consuls named in the Collectio Avellana".
- **N6 (sentence length).** Brief: Priscillian l.9, "Long after, in 561, a council at Braga named him when it cursed the teaching that souls were cast into bodies and bound to the stars", runs 26 words. Fix: end the sentence after "named him", then "It cursed the teaching ...". Cards, among new or changed sentences only: Apollinaris `dates` (40 words), Damasus `knownFor` (34) and Ammianus trace (32), Auxentius numbers item (29) and manuscript item (29), Priscillian Orosius item (29) and `dates` (27), Macrina Clarke trace (29), Tyconius Augustine trace (28), Cyril Socrates and Sozomen item (28), Sozomen item (27) and `dates` (26), Eunomius `dates` (26). The `dates` fields are semicolon lists and may be left. The prose items should be split at their first clause break.

No other new defect was found in the changed text. The new or changed records.json entries match their briefs and cards, apart from NB1.

## Summary

| Profile | Words | Time @162 | FK | Flesch | R1 blocking resolved | New blocking | New minor |
|---|---|---|---|---|---|---|---|
| Ulfila (MAJOR) | 405 | 2:30 | 8.3 | 60.4 | – (0) | 1 (NB1) | 0 |
| Auxentius of Durostorum | 317 | 1:57 | 8.0 | 62.3 | – (0) | 0 | N6 (card) |
| Eunomius of Cyzicus (MAJOR) | 403 | 2:29 | 8.0 | 60.2 | – (0) | 0 | 2 (N1, N2) + N6 |
| Macrina the Younger | 324 | 2:00 | 6.4 | 76.7 | 1 of 1 | 0 | N6 (card) |
| Damasus of Rome (MAJOR) | 402 | 2:29 | 8.2 | 60.4 | 1 of 1 | 0 | 1 (N5) + N6 |
| Priscillian (MAJOR) | 405 | 2:30 | 7.6 | 63.6 | 2 of 2 | 0 | 1 (N3) + N6 |
| Tyconius | 323 | 2:00 | 7.4 | 65.1 | 1 of 1 | 0 | 1 (N4) + N6 |
| Cyril of Jerusalem (MAJOR) | 405 | 2:30 | 7.3 | 66.0 | 2 of 2 | 0 | N6 (card) |
| Apollinaris of Laodicea (MAJOR) | 403 | 2:29 | 8.2 | 60.3 | – (0) | 0 | N6 (card) |
| **Total** | | | | | **7 of 7** | **1** | **6 (N1 to N6)** |

All 7 R1 blocking findings and all 40 R1 minor findings are resolved, or taken in another form that holds. Every not-taken reason holds against its source. The changes brought in one new blocking finding, NB1: a false "no source in the Library" sentence on the Ulfila card. The fix is one card sentence, one records entry and one source line. A round 3 can recheck NB1 alone. N1 to N6 can be fixed in the same pass without another review.
