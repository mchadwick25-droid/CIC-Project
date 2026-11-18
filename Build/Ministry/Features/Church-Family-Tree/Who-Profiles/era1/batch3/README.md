# Who profiles: era 1, batch 3

Four profiles, one id each: `peter-of-alexandria`, `anatolius-of-alexandria-and-laodicea`, `polycrates-of-ephesus`, `pliny-the-younger`.

These are the three era 1 WHO rows from the supplement Who scan that were in neither batch 1 nor batch 2 (Peter of Alexandria, Anatolius of Alexandria and Laodicea, Polycrates of Ephesus), plus Pliny the Younger, ruled a Who as an outside witness, not major (Mark, 2026-11-12; Open-Gaps 233). Mark confirmed the major marks on 2026-11-13 (picked from options, relayed by the coordinator): Peter of Alexandria is major; Anatolius, Polycrates and Pliny are not. Tacitus and Suetonius in batch 2 set the outside-witness form that Pliny follows.

| File | Holds |
|---|---|
| `<id>.brief.txt` | The brief as text, with no audio tags. Paragraphs are separated by a blank line. |
| `<id>.card.json` | The card. Its fields are `name`, `otherNames`, `label` (outside witness only), `knownFor`, `dates`, `place`, `tradition`, `role`, `briefLength`, `keyWorks` (title, about), `legacy` (`traces`, `remembered`), `uncertain`, and `sources` (`ownWords`, `about`; each entry gives a title, an author where one applies, a language and its file under `cic/texts/`). A field with no content is left out. |
| `audio/<id>.audio.txt` | The text sent to the voice: the brief with `[calmly]` at the start and `[warmly]` before the closing line. |
| `records.json` | For each id, `claims` (claim, witness, `formation_confidence`), `contested_claims` (claim, sides), and `absent_details` (detail, note) for the honest limits. |
