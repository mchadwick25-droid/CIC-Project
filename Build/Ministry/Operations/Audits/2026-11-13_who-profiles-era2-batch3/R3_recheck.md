# R3 recheck: nine Who profiles, era 2 batch 3

Scope: round 3, the last allowed. A targeted recheck of the round 2 changes only (`git diff fb5d666b~1 HEAD -- Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era2/batch3/`), against `R2_recheck.md` and `R2_changes.md`. Six files changed: the Ammianus and Evagrius briefs and audio scripts, the Epiphanius card, and `records.json`. Unchanged text was not re-reviewed. Each changed line was searched in its vendored file (whitespace-tolerant, tags stripped, quote marks straightened) and read in context. No drafts were edited and no model, paid or web calls were made.

## 1. R2 points

| Finding | Status | Check against source |
|---|---|---|
| Ammianus R1 M6 (partly) and N1: first mentions | RESOLVED | "Edward Gibbon, whom Yonge quotes" restores the full name; Yonge's preface cites him as "Gibbon" (l.767), and the card already names him. "The scholar E. A. Abbott, quoted in Blomfield Jackson's notes to Theodoret of Cyrrhus" fits Jackson's note, which cites "Dr. E. A. Abbott's Philomythus" (npnf203 l.12369, also l.12341). "Theodoret of Cyrrhus" now matches the card. |
| Ammianus trims | HOLD | "Formed parties that came to blows": Ammianus has Damasus and Ursinus "formed parties", "the partisans of each carrying their violence to actual battle, in which men were wounded and killed" (Yonge l.23177). Still fair. "A history ending with the emperor Valens's death in 378" matches "continued to the death of Valens, A.D. 378" (l.767). Yonge's religion sentence, split in two, keeps both halves: uncertain, and a general belief. No hedge lost. |
| Evagrius N2: Melania given to Sozomen; Socrates's route between Melania's welcome and her nursing | RESOLVED | "Palladius and Sozomen take him to Jerusalem. Socrates of Constantinople has him go into Egypt with Gregory. In Jerusalem, Palladius says, Melania the Elder took him in. He wavered..." Melania is now Palladius's alone ("he went to Jerusalem. And there he was received by the blessed Melania", Clarke l.457), and her care follows straight on. The trim "then to Cellia" drops "in the desert" and adds nothing. |
| Evagrius N3: suppression claim tag | RESOLVED | `records.json`: "His works were later suppressed for their Origenist tendency", witness Clarke note 255, back to Widely Accepted. The Justinian claim stays Inferential-Thin. The contested route record is unchanged and still agrees with the brief. |
| Epiphanius card `briefLength` | RESOLVED | "about 2 minutes 30 seconds", the form the other majors use; 405 words at 162 a minute. |
| N4 (card sentences over 25 words) | DECLINE HOLDS | Same ground as era 1 batch 2 and era 2 batch 1: card text is read by eye and ties claims to named witnesses. |

No new witness swap, dropped hedge or superlative came in with the changes.

## 2. Mechanical checks

| Profile | Words | Cap | FK | Flesch | Audio matches brief |
|---|---|---|---|---|---|
| Ammianus Marcellinus | 323 | 324 | 8.2 | 60.1 | yes |
| Evagrius Ponticus | 405 | 405 | 7.7 | 63.5 | yes |

`grade_text` passes both (FK ≤ 10, Flesch ≥ 60; Ammianus is close to the Flesch floor). Each audio script opens with `[calmly]` and has one `[warmly]` before the closing sentence, and matches its brief once the tags are removed. `records.json` parses.

## 3. New findings

### Blocking

None.

### Minor

- **m1 (Ammianus, brief, paragraph 4, sentence length).** "The scholar E. A. Abbott, quoted in Blomfield Jackson's notes to Theodoret of Cyrrhus, judges him impartial, but accepts only that people 'generally believed' a fiery sign had stopped it." This is 30 words, two of them quoted. The R2 form was already 27 and was missed in R2; the N1 identifiers add three. Nothing in it is wrong, and `grade_text` passes. If the drafter touches the brief again, split it: "...notes to Theodoret of Cyrrhus, judges him impartial. Yet Abbott accepts only that people 'generally believed' a fiery sign had stopped it." Not a reason for another round.
- The Gennadius line in Evagrius (26 words, 9 quoted) is unchanged since R2, where it was accepted.

## Summary

Every R2 point is resolved: Ammianus M6/N1 (Gibbon and Abbott identified, Theodoret of Cyrrhus), Evagrius N2 (Melania now Palladius's alone, and the route order clear) and N3 (Widely Accepted restored). The trims made to hold the caps say only what Ammianus, Yonge and Palladius say. Both briefs pass `grade_text` and sit within their caps, and the audio scripts match. One minor remains (m1, a 30-word Abbott sentence), not blocking. The batch clears review at round 3.
