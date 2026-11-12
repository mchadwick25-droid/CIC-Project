# R3 recheck: eight Who profiles, era 1 batch 2

Scope: round 3, the last allowed. A targeted recheck of the round 2 changes only, against `R2_recheck.md` and `R2_changes.md`. Unchanged text was not re-reviewed. Each changed line was searched in its vendored file and read in context. No drafts were edited and no paid calls were made.

## 1. The 3 R2 blocking findings

| Finding | Status | Check against source |
|---|---|---|
| NB1 Bardaisan, brief: Avida heard as one of Philip and Baryama | RESOLVED | Brief now reads "Avida, who was with them, had asked why God did not make people unable to do wrong." The dialogue has the narrators say "'Avida here,' said we to him, 'was saying to us, ... why did He not so create men that they should not be able to do wrong ...'" (anf08 l.67921–67926), and Bardaisan answers "my son Avida" (l.67927). Avida is present and separate from the narrators. The paraphrase of his question is fair. |
| NB2 Pontius, card: Ritschl's doubt given without Benson's verdict | RESOLVED | Card: "Otto Ritschl thought they were confiscated later and that Pontius mistook this for a sale. Archbishop Benson reports that view and follows Pontius." Benson's footnote: "O. Ritschl ... conceives that the Horti must have been confiscated later and that Pontius mistakes this for charitable sale now" (Benson l.2896–2903). His main text follows Pontius: "To the sacrifice of his farms ... Cyprian did not hesitate to add that of his delightful Gardens. Friends bought them in" (l.2876–2878). The named witness's verdict now has the last word. See m1 for a small wording point. |
| NB3 Bardaisan, card: "a note in the English edition" as witness | RESOLVED | The Abgar Bar Manu line is gone. No "Neander", "Bar Manu" or "Pratten" remains in the Bardaisan card, brief or records. The brief's "close to Abgar, the ruler of Edessa" rests on Epiphanius and was accepted in R2. Removing an unsupportable line is a correct fix. |

**All 3 are resolved.**

## 2. Changed sentences (R2_changes.md minor list)

**Tacitus**
- "a century later" is gone. The paragraph now opens "Tacitus was not a Christian." This states a fact, not a verdict on his tone. Accepted.

**Tatian**
- Brief: "Hope Hogg ... says Tatian left Rome for Mesopotamia after Justin's death." Hogg: "after Justin's death left Rome and returned to Mesopotamia" (anf09 l.1961). Accurate. "Returned" is lost, but the brief has already placed his birth among the Assyrians. Accepted.
- Brief: "Irenaeus's Encratites came from Saturninus and Marcion of Pontus. So Tatian found them already in being." McGiffert: "As to the particular sect which Irenæus describes ... they sprung from Marcion and Saturninus, evidently implying that they were not founded by Tatian, but that he found them already in existence" (npnf201 l.26308–26314). Accurate. This resolves R2's Tatian M2 in the brief.
- Card: McGiffert thought Harnack's arguments "seem fully to establish his main positions." Exact (npnf201 l.26234). The hedge is restored (R2 N3).
- Card legacy: "It would seem, writes Hope Hogg ..." keeps the hedge. Ephrem now appears once only (R2 N10 fixed).
- records.json: Hogg is in the life contested_claim. Accurate. The `sides` string reads "Harnack (...), which McGiffert says his arguments seem fully to establish" and is ungrammatical (m3).

**Dionysius**
- Card: "Basil of Caesarea" now has its identifier. "Jackson adds that Lumper put the charge down to Basil's imperfect knowledge of his writings, and that elsewhere Basil calls him 'the Great.'" Jackson: "Bp. Westcott ... quotes Lumper ... as supposing that Basil's charge ... was due to imperfect acquaintance with his writings. In Letter clxxxviii. Basil calls him 'the Great'" (npnf208 l.14429). Accurate, though Westcott, who comes between Jackson and Lumper, is skipped. "The Great" is exact. "Anomoean" still has no context. This is card text, so it is minor and carried over.
- records.json: the claim "The apostle John did not write the Revelation" now puts the Cerinthus group on Dionysius's side. That fixes R2 N6. The new "against" side is "the many brethren who held it in high esteem". Dionysius cites them only for not rejecting the book. He does not report what they thought about who wrote it (m4).

**Bardaisan**
- Brief: "Epiphanius, who wrote against every heresy, says ..." This puts the partisan marker back in the brief (R2 N5). The Panarion supports the description. Accepted.

**Suetonius**
- "For his part" is removed (R2 M2 fixed).
- Card legacy: the two "his" now point clearly (R2 N7 fixed). But "wrote his Life of Ambrose on the model of Suetonius" borrows a phrase Rolfe uses for Einhard. On Paulinus, Rolfe says only that Suetonius's influence "is seen in the form of the Life of Ambrosius by his secretary Paulinus" (Rolfe l.385–391). The meaning is close, so this is minor (m2).
- Brief: "Paulinus, secretary to Ambrose of Milan, followed his way of writing a life." The nearest name before "his" is Ambrose, so a listener can hear "Ambrose's way". This is the same fault R2 N7 found on the card, now in the spoken brief (m2).
- briefLength is "about 2 minutes". Correct for 319 words (R2 N9 fixed).

No new verbatim quotation was brought into a brief this round. The quotations checked above are exact.

## 3. Mechanical checks

| Profile | Words | Cap | FK | Flesch | Audio matches brief, tags removed |
|---|---|---|---|---|---|
| Bardaisan of Edessa | 323 | 324, within | 8.1 | 63.1 | yes |
| Tacitus | 302 | 324, within | 7.8 | 61.6 | yes |
| Tatian (major) | 402 | 405, within | 8.1 | 61.4 | yes |
| Suetonius | 319 | 324, within | 7.7 | 65.3 | yes |
| Pontius (card only changed) | 318 | 324 | 6.7 | 71.8 | yes |
| Dionysius (card only changed) | 401 | 405 | 7.4 | 66.6 | yes |

`grade_text` passes for all of them. In every changed audio script, `[calmly]` opens the script and `[warmly]` comes right before the closing line. No other tags appear. No changed narrator sentence in a brief runs past 25 words.

## 4. New findings

### Blocking

None.

### Minor

- **m1 (Pontius, card).** "Reports that view and follows Pontius" is accurate. Benson also objects directly ("Pontius' personal knowledge seems to present to him no difficulty", l.2903–2906). "Reports that view, rejects it, and follows Pontius" would be closer to the source. This is optional.
- **m2 (Suetonius, brief and card).** In the brief, "followed his way" can be heard as Ambrose's way. Write "followed Suetonius's way of writing a life." On the card, "on the model of Suetonius" is Rolfe's phrase for Einhard. For Paulinus, Rolfe says Suetonius's influence "is seen in the form of" the Life.
- **m3 (Tatian, records.json).** The life `sides` string is ungrammatical ("..., which McGiffert says his arguments seem fully to establish"). Write "Harnack (...), whose arguments McGiffert says 'seem fully to establish his main positions'".
- **m4 (Dionysius, records.json).** In the Revelation contested_claim, the "against" side (the brethren who esteemed the book) is inferred. Dionysius does not report their view on who wrote it. Either mark that side as inferred, or name it "those who took the book as the apostle's (not named in Dionysius's letter)". Not participant-facing.
- **Carried over, accepted as reported:** unglossed Saturninus, Harnack, Neander, Baronius, Valesius, Sabellius, Nepos and Anomoean, because the majors are at their cap. Card sentences over 25 words are left as R2_changes.md explains.

## Summary

All 3 R2 blocking findings are resolved, and checked against the source. No new blocking finding came in. Four minor points remain (m1–m4). Two are in records.json, one is optional card wording, and one is a pronoun in the Suetonius brief that is worth fixing before audio is made. None needs another review round.
