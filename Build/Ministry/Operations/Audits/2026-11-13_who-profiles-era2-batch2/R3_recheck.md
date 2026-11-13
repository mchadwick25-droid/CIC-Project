# R3 recheck: nine Who profiles, era 2 batch 2

Scope: round 3, the last allowed. A targeted recheck of the round 2 changes only (`git show HEAD` on `era2/batch2/`), against `R2_recheck.md` and `R2_changes.md`. Unchanged text was not re-reviewed. Each changed line was read as a word diff, and the new source claims were read in their vendored files. No drafts were edited and no paid or model calls were made.

## 1. The R2 blocking finding

| Finding | Status | Check against source |
|---|---|---|
| NB1 Ulfila, card uncertain #3 and records.json: "No source in the Library names Eusebius's see" | RESOLVED | Card now: "Philostorgius gives no see. Louis Duchesne, in his history of the early church (1907), names him Eusebius of Nicomedia. Kauffmann notes that Eusebius of Nicomedia, by then bishop of Constantinople, was at the synod of 341." Duchesne II: "Eusèbe de Nicomédie le vit, et, augurant bien de ses aptitudes, le consacra évêque pour sa nation" (l.20994–20995). Kauffmann: "Ausserdem war Eusebius von Nikomedien (damals bereits bischof von Constantinopel) anwesend" at the Antioch synod (l.2754–2756), and he ties the consecration to that synod, "wir kennen keine andere Eusebianersynode als die von Antiochia a. 341" (l.3809–3811). Philostorgius gives the bare name (R2 checked, Walford l.120). Each sentence matches its witness. Duchesne is added to the card's sources with the right file. In records.json the false absent_detail is gone, and the new claim is tagged Dominant Modern Reconstruction, which fits: one modern historian states it, and the editor's synod dating supports it. Both JSON files parse. |

## 2. The R2 minor findings

| Finding | Status | Evidence |
|---|---|---|
| N1 Eunomius, brief: unplaced Photius, unclear "His", "hostile" with no object | RESOLVED | "That history survives mainly in a summary by Photius, a later patriarch of Constantinople. He was hostile to it." "That history" follows "Philostorgius, a historian ..." directly. The two words dropped to keep length ("the emperor" before Constantius, "another" before "church historian") remove nothing a claim rests on; "Sozomen, a church historian of the next century" stays true. |
| N3 Priscillian, brief: "His teaching comes to us mostly through his enemies" overstated | RESOLVED | "The teaching he was condemned for comes to us through his enemies." It now sits cleanly after the paragraph on his own treatises. "Orosius, a Spanish priest, wrote to Augustine of Hippo against the Priscillianists" keeps the R2-checked content. |
| N4 Tyconius, brief: "his life" pointing to Burkitt | RESOLVED | "Burkitt says the little known of Tyconius's life comes chiefly from Augustine of Hippo". |
| N5 Damasus, card `dates`: "the Avellana account" before it is explained | RESOLVED | "by the date of the Ursinian account kept in the Collectio Avellana". The account and its party are now named at first mention; the card's sources list it as "Anonymous, from Ursinus's party". |
| N6 Priscillian, brief: 26-word Braga sentence | RESOLVED | "In 561 a council at Braga named him. It cursed the teaching that souls were cast into bodies and bound to the stars." Content unchanged. |

## 3. The two "Not changed" items

- **N2 (Eunomius, Theodoret of Cyrus not backed by a listed source).** Accepted. The see is an identifier; the claim it carries reaches the card through Zenos's note in npnf202, which the card lists. Nothing is wrong or misleading.
- **N6, card sentences of 26–40 words.** Accepted. Cards are read by eye, each long sentence keeps a claim with its witness, and era 1 batch 2 took the same position. The briefs, which are spoken, are now within length.

## 4. Gates on the changed briefs

| Brief | Words | Cap | FK | Flesch | Audio = brief less `[calmly] ` and one `[warmly] ` |
|---|---|---|---|---|---|
| Eunomius of Cyzicus (MAJOR) | 406 | ~405–406 | 7.8 | 60.9 | Yes |
| Priscillian (MAJOR) | 403 | ~405–406 | 7.5 | 63.8 | Yes |
| Tyconius | 323 | ~324 | 7.5 | 64.3 | Yes |

All pass (FK at most 10, Flesch at least 60). Eunomius sits at the top of its cap.

## 5. New findings

None. The new text adds nothing wrong, unsupported, misleading or not verbatim.

## Verdict

NB1 and N1, N3, N4, N5, N6 are all resolved and hold against the sources. The two not-changed items are accepted. No new finding. The batch clears review at round 3.
