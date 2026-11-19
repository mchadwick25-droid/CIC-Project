# R3 changes: era 3 batch 8

Every round 3 finding was applied as worded by the drafter of those profiles, after confirming its cited lines. The parts follow, unchanged.

## R3 changes, part A: John Climacus, Liberatus of Carthage (era 3 batch 8)

All six minors were applied exactly as the reviewer worded them, and nothing else was changed. I opened each cited line again before changing it. The audio scripts were rebuilt by script from their briefs and checked by script against them (`[calmly] ` at the start, `[warmly] ` before the closing paragraph). `records.json` was not changed. No records string quotes the changed text. The one hit for "so that wise men" is the source quote from Thomas, which is unchanged.

| Finding | Done |
|---|---|
| R3-A-M1 (Climacus brief: "His English translator") | Taken as worded in brief and audio: "Gregory's English translator, James Barmby, takes this John to be Climacus, still alive then." Barmby as Gregory's translator confirmed (npnf213 l.5356-5358). |
| R3-A-M2 (Climacus card `legacy.remembered` 0: witness dropped) | Taken as worded: 'Ketel "expounded therefrom sentiments full of spiritual truth", Thomas says, so that wise men marveled at how well he understood the book.' kempis l.12188-12190 confirmed. The card already had the comma outside the quotation marks, so the merge was made on that text. |
| R3-A-M3 (Climacus brief: comma inside the quote) | Taken as worded in brief and audio: '"Sometimes he read the book of John Climacus", Thomas writes.' kempis l.12186-12187 ("Climacusr" then the title, no comma) confirmed. |
| R3-A-M4 (Liberatus brief: "which he shared") | Taken as worded in brief and audio: "...to be this exile, which Liberatus shared until his bishop died." PL68 l.75566-75568 confirmed. |
| R3-A-M5 (Liberatus card `uncertain` 2: "he says") | Taken as worded: "Garnier says the envoys named in Agapetus's letter left Africa only after Pope John had died." PL68 l.81394-81396 confirmed. |
| R3-A-M6 (Liberatus card `dates`: Mommsen's grounds cut loose) | Taken as worded: "Theodor Mommsen dates the Breviarium between 555 and 567, since it tells of the death of Pope Vigilius. He adds that Liberatus wrote while Theodosius, once bishop of Alexandria, and Apollinaris of Alexandria were alive." mommsen1894 l.17568-17571 ("nam ... nam") confirmed. |

| Profile | Words | Time at 162 wpm | FK | Flesch |
|---|---|---|---|---|
| john-climacus (major, cap about 405) | 404 | 2:30 | 6.6 | 75.6 |
| liberatus-of-carthage (recorder) | 325 | 2:00 | 8.5 | 60.1 |

---

## R3 changes, A2: Dionysius Exiguus card

Both findings were taken exactly as worded, and nothing else was changed. I opened the cited lines before each change. No records string quotes the changed text, so `records.json` is unchanged. After the edit, `longsent.py` lists no long sentence for Dionysius.

| Finding | Done |
|---|---|
| R3-A-M7 (card `uncertain[1]`: "he says" could be read as Dionysius) | Taken as worded. The sentence now reads "Duchesne says Dionysius drew it from the letter of Proterius of Alexandria to Pope Leo." Confirmed at LP1 l.16343-16346: "c'est Denys qui l'a déduite, par une exégèse habile, de la lettre de Proterius d'Alexandrie au pape saint Léon". |
| R3-A-M8 (card `legacy.traces[1]`: a garden path) | Taken as worded. It now reads "Abbot Ceolfrid wrote a letter that Bede gives in his Ecclesiastical History. In it he says that after Cyril of Alexandria, Dionysius added as many cycles again, reaching down to Ceolfrid's own time." Confirmed at plummer1896 l.28824-28825 ("Ceolfrid abbas in Domino salutem") and l.29186-29189 ("post quem Dionysius Exiguus totidem alios ex ordine pari schemate subnexuit, qui ad nostra usque tempora pertingebant", read through the OCR noise). |

---

## R3 changes, part B1: Martin of Braga, Brendan of Clonfert (era 3 Who batch 8)

This table gives each finding and what was done. Every cited line was opened first. No brief or audio changed. `records.json` was re-loaded just before writing, and only `brendan-of-clonfert` was edited (indent=1, ensure_ascii False). No git.

| Finding | Done |
|---|---|
| R3-B-M1 (Martin `knownFor`: "He" reads as Isidore) | Applied as worded: "Martin led the Second Council of Braga and wrote a sermon against the pagan customs of country people." |
| R3-B-M2 (Martin `uncertain` 2: Krusch's "coniecerunt") | Confirmed: arndt-krusch1885 l.45634-45636 ("unde plerique Chararicum eundem ac Theudemirum fuisse coniecerunt"). Applied as worded: "Many, Krusch says, have guessed that Chararic and Theudemir were one man." |
| R3-B-B1 (Brendan `uncertain` 4: "their editor") | Confirmed: annales-cambriae l.263 ("THE REV. JOHN WILLIAMS AB ITHEL") and l.892-893 ("the death of Brenda, abbot of Birre"). Applied as worded: "…whom John Williams ab Ithel, who edited them, takes for Brendan of Birr." |
| R3-B-M3 (Brendan records: the Bollandist note on the contested side) | Confirmed: acta-sanctorum augusti-1 l.58935-58941 ("Cluain ferta … a S. Brandano conditum"), which says nothing of Adomnan or Mocu Alti; stokes lismore1890 l.878-881 confirmed. Applied as worded. The side now reads "Book of Lismore story: 'Brenainn maccu Altai was in Clonfert' (stokes lismore1890 l.878-881)". The note was added as a plain claim beside Williams's: "Bollandist note: Cluain ferta founded by S. Brandano; says nothing of Adomnan's Brendan Mocu Alti". |

---

## R3 changes, part B: Barhadbeshabba 'Arbaia of Halwan

I opened each cited line in its vendored file before making the change. Nothing else was changed. No records string quotes either sentence, so `records.json` is unchanged.

| Finding | Done |
|---|---|
| R3-B-M4 (card `uncertain` 4; a hedge firmed up) | Taken as worded. po09 l.31601-31607 ("Il suffit de supposer qu'il a ecrit « l'Histoire des saints Peres » dans sa jeunesse ... dans sa vieillesse") confirmed. "If so, he wrote the History young and the Cause in old age." became "For that, Nau says, it is enough to suppose he wrote the History young and the Cause in old age." |
| R3-B-M5 (card `uncertain` 9; the chronicles cut off from their claim) | Taken as worded. Seert scher1919 l.29180-29181 ("avait recommande aux fideles de choisir Barhadbsabba le moine") and Mari gismondi1899 l.13591-13592 ("mandavisset in patriarcham assumi Barhadbsabba monachum") confirmed. "Sabrisho of Lashom, head of the church, wanted him as his successor." became "They say Sabrisho of Lashom, head of the church, wanted him as his successor." |

---

## R3 changes, part B: Theopistus (era 3 batch 8)

| Finding | Done |
|---|---|
| R3-B-M6 (card `legacy.traces` 2: "is said" with no owner) | Taken as worded. I confirmed Nau l.798-801 first: "Eloge que prononça notre patriarche saint ... le saint Dioscore. Il le prononça sur l'abbé Macaire, l'évêque de la ville de Tkoou, du temps que le roi Marcien l'avait exilé à Gangres". The sentence now reads: "A Coptic sermon in praise of Macarius, bishop of Tkow, says in its heading that Dioscorus spoke it in exile." Nothing else was changed. No string in `records.json` quotes the changed text, so the records were not edited. |

---
