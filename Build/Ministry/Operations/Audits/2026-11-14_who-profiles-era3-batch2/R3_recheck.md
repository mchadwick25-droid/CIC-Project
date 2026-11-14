# R3 recheck: era 3 batch 2

Scope: round 3, the last allowed. This recheck covers only the round 2 changes, read as `git diff --word-diff 05d852ff a1b24b67` under `era3/batch2/`. It checks them against `R2_recheck.md` (N1 to N7) and `R2_changes.md`. Under `era3/batch2/`, eight files changed:
- the Joshua brief, audio and card
- the Zachariah brief, audio and card
- the Severus audio
- `records.json`

The README did not change. Text that did not change was not reviewed again. I opened each changed sentence at its line in the vendored file, to confirm who is speaking there. I edited no drafts, and I made no paid calls, model calls or web requests. Line numbers point to files under `cic/texts/` unless another path is given.

## 1. The R2 findings

| Finding | Status | Check against source |
|---|---|---|
| N1 Joshua brief l.7: "He and … Noeldeke" could be heard as Joshua | RESOLVED | Brief and audio: "Wright and the German scholar Theodor Noeldeke place the writing in the months after." Wright: "I have thought myself justifed in assigning the composition of the work to that winter and the earlier part of the following year, which is also Noeldeke's opinion" (`joshua-the-stylite_chronicle_wright1882.txt` l.340–343). The placing is Wright's, with Noeldeke agreeing, and the sentence now says so. |
| N2 Joshua card: the Chabot passage called his Introduction | RESOLVED | The source title is now "Note on the Chronicle of Michael the Syrian, for the Académie des Inscriptions". The file has "LA CHRONIQUE DE MICHEL LE SYRIEN / NOTE / DE M. L'ABBÉ J.-B. CHABOT / EXTRAIT DES COMPTES RENDUS DE L'ACADÉMIE DES INSCRIPTIONS ET BELLES-LETTRES" (`michael-the-syrian_chronique-tome1-livres-i-vii-fra_chabot1899.txt` l.62857–62869). The notice saying the Introduction "ne pourra être livrée qu'à la fin de la publication" is at l.62759–62760. The cited passage, "la chronique authentique de Denys de Tell-Mahré… Cet ouvrage est perdu, à l'exception d'un seul chapitre", is at l.63094–63099, inside the Note. No "Introduction" for Chabot is left in the card or in `records.json`. |
| N3 Zachariah: Land called the chronicle's "first editor" | RESOLVED | The brief and audio (l.7) and card `uncertain` 4 now read "Land, its editor of 1870". The records contested claim reads "Land, its editor of 1870 (Kugener l.17146-17151)". Kugener: "Elle a été éditée en 1870 par Land" (`zacharias-scholasticus_vie-de-severe-po2-syr-fra_kugener1903.txt` l.17150–17151, OCR). Brooks: the Vatican extracts of "the same work" were "published with a Latin translation by Mai in 1838" (`zachariah-rhetor_chronicle_hamiltonbrooks1899.txt` l.255–259). Brooks's note "Land ascribes bk. 7 to Zachariah" is in the note block just after l.330, as cited. The records witness now names Mai, but its order puts the Kugener citation after the Mai clause (N8). |
| N4 Zachariah brief l.9: "to become bishop" gave a motive | RESOLVED | Brief and audio: "Brooks suggests, with a 'perhaps,' that he had come over to Chalcedon's side when he became bishop." Brooks: "at a later time, conforming perhaps to the Chalcedonian faith, was made bishop of Mitylene" (l.364–366). Brooks gives no motive now. "had come over" differs from R2's "came over", but it says the same and stays inside Brooks's "perhaps". |
| N5 Severus audio: `[warmly]` before the letter count | RESOLVED | `[warmly] ` now stands just before "In the letter to Misael, Severus says God alone is…", the closing sentence. The count sentence carries no tag. The brief is unchanged at this point. |
| N6 Caesaria records: the Fortunatus claim held twice | RESOLVED | The Inferential-Thin copy is gone. One claim remains (`records.json` l.560–561), tagged Dominant Modern Reconstruction, with witness "Krusch, introduction, MGH SRM 3 (l.35667-35668; note 8, l.34757-34758); Fortunatus not held". Krusch: "neque vero Casaria ipsius artem effugit pia soror, quam non semel proposuit exemplum imitandum" (`passiones-vitaeque-sanctorum-merovingici-mgh-srm-3-lat_krusch1896.txt` l.35667–35668). Note 8: "Ita a Fortunato appellatur (Carm. VIII, 3, 39; App. XIII…), quocum cod. B 1 Gregorii, H. Fr. IX, 42, convenit" (l.34757–34758). The separate Fortunatus quotation claim (l.754) is a different claim and stays. |
| N7 Caesaria records claim 2: "until the day of her death" | RESOLVED | It now reads "until the day of their death ('usque diem transitus earum')". Life I,35: "ita retrusae, ut usque diem transitus earum nulli liceat foris ianuam egredi de monasterio" (krusch1896 l.37217–37218, OCR "fons lanuam"). Brief and records now agree. |

## 2. New findings in changed text

- **N8 MINOR (`records.json`, `zachariah-rhetor`, claim on books three to six, witness l.323; a citation placed after the wrong clause).** The witness reads "…Land as editor of the Syriac in 1870; Mai had published extracts in 1838 (Brooks l.255-259): Kugener, Vie de Sévère (l.17146-17151)". With this order, Kugener reads as the witness for the Mai clause. Kugener in fact backs the 1870 edition, and Brooks backs Mai. Every cited line is right; only the order misleads. Fix: "…Land as editor of the Syriac in 1870 (Kugener, Vie de Sévère, l.17146-17151); Mai had published extracts in 1838 (Brooks l.255-259)". This does not block clearing.

No other changed text adds a wrong attribution, a misquotation, an unsupported claim or a contested point told as settled.

## 3. Mechanical checks

- All ten audio scripts equal their briefs once `[calmly] ` and `[warmly] ` are removed (checked by script).
- Each script starts with `[calmly]` and has one `[warmly]`, in its last paragraph, before the closing line. Severus's tag now sits right (N5).
- No tag appears in any brief or card.
- All ten cards and `records.json` parse as JSON. `records.json` holds exactly ten ids, and they match the ten briefs.
- `grade_text` (`engine.m1.gates`) passes on all ten (FK at most 10, Flesch at least 60):

| Profile | Words | FK | Flesch |
|---|---|---|---|
| Joshua the Stylite | 325 | 5.9 | 76.7 |
| John Rufus | 321 | 8.2 | 64.8 |
| Brigid of Kildare | 322 | 6.6 | 70.9 |
| Zachariah Rhetor | 325 | 7.7 | 63.7 |
| Severus of Antioch (MAJOR) | 404 | 7.8 | 62.1 |
| Caesaria of Arles the Elder | 316 | 6.5 | 73.0 |
| Caesarius of Arles (MAJOR) | 403 | 6.7 | 73.7 |
| Julian, missionary to the Nobadae (MAJOR) | 378 | 7.2 | 68.6 |
| Ferrandus of Carthage | 321 | 8.3 | 61.5 |
| Benedict of Nursia (MAJOR) | 405 | 7.0 | 71.2 |

`briefLength` is unchanged and still matches: "about 2 minutes 30 seconds" on Severus, Caesarius and Benedict, "about 2 minutes 20 seconds" on Julian, and "about 2 minutes" on the rest. The changed briefs (Joshua 325 words, Zachariah 325) stay within "about 2 minutes".

## Verdict

All seven R2 findings (N1 to N7) are resolved, and each holds against its source. One new minor point (N8) is a citation-order slip in a `records.json` witness field. It does not block. No change to a card, brief or audio script adds a wrong or unsupported claim.

## Totals

R2 findings: N1 to N7, 7 of 7 RESOLVED. None is PARTLY or NOT RESOLVED. New: 0 blocking, 1 minor (N8, `records.json`, `zachariah-rhetor`).

Verdict: clear.
