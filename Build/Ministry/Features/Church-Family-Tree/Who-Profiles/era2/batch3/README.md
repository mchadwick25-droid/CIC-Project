# Who profiles: era 2, batch 3

Nine profiles, one id each: `ammianus-marcellinus`, `martin-of-tours`, `didymus-the-blind`, `evagrius-ponticus`, `fabiola-of-rome`, `epiphanius-of-salamis`, `olympias-of-constantinople`, `melania-the-elder`, `marcella-of-rome`.

| File | Holds |
|---|---|
| `<id>.brief.txt` | The brief as text, with no audio tags. Paragraphs are separated by a blank line. |
| `<id>.card.json` | The card. Its fields are `name`, `otherNames`, `label` (outside witness only), `knownFor`, `dates`, `place`, `tradition`, `role`, `briefLength`, `keyWorks` (title, about), `legacy` (`traces`, `remembered`), `uncertain`, and `sources` (`ownWords`, `about`; each entry gives a title, an author where one applies, a language and its file under `cic/texts/`). A field with no content is left out. |
| `audio/<id>.audio.txt` | The text sent to the voice: the brief with `[calmly]` at the start and `[warmly]` before the closing line. |
| `records.json` | For each id, `claims` (claim, witness, `formation_confidence`) and `contested_claims` (claim, sides). Where a detail is asked for but has no witness, `absent_details` (detail, note) records the honest limit. |
