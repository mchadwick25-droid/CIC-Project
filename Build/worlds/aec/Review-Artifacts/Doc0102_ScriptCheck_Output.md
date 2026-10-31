# Doc_01, Doc_02 and Source Registry: script check (`aec`)

Command: `python tools/verify_world_source_citations.py aec` (`tools/verify_world_source_citations.py`, written on this branch before the rcg worker's script was available). Run 2026-10-29.

Scope: named `cic/texts` files exist; no document says "not vendored" for a file that exists; Registry row cross-references and one status per letter locus; every quotation of 6 or more words is found verbatim (whitespace and tag normalized) in a cited vendored file, the corpus map or a project document, at the cited XML paragraph id or inside the cited file lines; Table D buckets match the corpus map.

## Before the fixes (documents as on `origin/main` at `aa6adda5`)

```
verify_world_source_docs: world aec, texts /home/user/CIC-Project/cic/texts, 94 Table-D-style rows checked
1 named files exist: PASS
2 'not vendored' claims: PASS
3 row cross-references: PASS
4 quotations verbatim: FAIL (4)
   - Doc_01: "Arius, Eunomius, Macedonius, Apollinaris, Nestorius, Eutyches and Orig" is cited to xii.vii-p26 but is not in that paragraph of npnf214_seven-ecumenical-councils.xml
   - Doc_01: quotation not found in any cited vendored file, the corpus map or the project documents: "must have been written by Nestorius in the year 451 or 452"
   - Doc_01: quotation not found in any cited vendored file, the corpus map or the project documents: "as a defence against those who blamed him for having wanted a council to be held"
   - Registry: "as well as their impious writings" is cited to xii.vii-p26 but is not in that paragraph of npnf214_seven-ecumenical-councils.xml
5 bucket tables: FAIL (4)
   - chronicle-of-edessa_cowper.txt: Table lists ['syriac-edessa-nisibis', 'syriac-orthodox-west-syriac-christianity']; the corpus map assigns ['syriac-edessa-nisibis', 'syriac-orthodox-west-syriac-christianity', 'the-church-of-the-east-under-persia'] (missing ['the-church-of-the-east-under-persia'], extra [])
   - npnf204_athanasius-select-works-letters.xml: Table lists ['alexandria-catechetical', 'desert-monasticism', 'homoian-arian-christianity', 'imperial-juridical-christianity', 'post-apostolic-house-church']; the corpus map assigns ['aksumite-christianity', 'alexandria-catechetical', 'desert-monasticism', 'homoian-arian-christianity', 'imperial-juridical-christianity', 'post-apostolic-house-church'] (missing ['aksumite-christianity'], extra [])
   - npnf212_leo-great-gregory-great.xml: Table lists ['anglo-saxon-christianity', 'byzantine-imperial-church-justinianic', 'cyrilline-miaphysite-egyptian-tradition', 'early-benedictine-italian-monasticism', 'imperial-juridical-christianity', 'merovingian-gallic-christianity', 'roman-church-gregorian']; the corpus map assigns ['anglo-saxon-christianity', 'byzantine-imperial-church-justinianic', 'cyrilline-miaphysite-egyptian-christianity', 'cyrilline-miaphysite-egyptian-tradition', 'early-benedictine-italian-monasticism', 'imperial-juridical-christianity', 'latin-africa-under-byzantium', 'merovingian-gallic-christianity', 'nicene-visigothic-iberia', 'roman-church-gregorian'] (missing ['cyrilline-miaphysite-egyptian-christianity', 'latin-africa-under-byzantium', 'nicene-visigothic-iberia'], extra [])
   - npnf213_gregory-great-ephraim-syrus-aphrahat.xml: Table lists ['anglo-saxon-christianity', 'byzantine-imperial-church-justinianic', 'early-benedictine-italian-monasticism', 'merovingian-gallic-christianity', 'persian-church-of-the-east-early', 'roman-church-gregorian', 'syriac-edessa-nisibis']; the corpus map assigns ['anglo-saxon-christianity', 'british-welsh-christianity', 'byzantine-imperial-church-justinianic', 'cyrilline-miaphysite-egyptian-christianity', 'early-benedictine-italian-monasticism', 'gothic-and-vandal-homoian-christianity', 'insular-irish-monastic-christianity', 'latin-africa-under-byzantium', 'merovingian-gallic-christianity', 'nicene-visigothic-iberia', 'persian-church-of-the-east-early', 'roman-church-gregorian', 'syriac-edessa-nisibis'] (missing ['british-welsh-christianity', 'cyrilline-miaphysite-egyptian-christianity', 'gothic-and-vandal-homoian-christianity', 'insular-irish-monastic-christianity', 'latin-africa-under-byzantium', 'nicene-visigothic-iberia'], extra [])
```

## After the fixes

```
verify_world_source_docs: world aec, texts /home/user/CIC-Project/cic/texts, 94 Table-D-style rows checked
1 named files exist: PASS
2 'not vendored' claims: PASS
3 row cross-references: PASS
4 quotations verbatim: PASS
5 bucket tables: PASS
```

Not mechanically detectable, and checked by hand against the vendored files instead: the Evagrius attribution (Nau file lines 899 to 960), the dating of `iv.x.clxxiii` (Mansi file lines 88713 to 88724 and 88748 to 88766), canon XII's naming of the *Commentary on the Acts of the Apostles* (`xii.vii-p34`), the *Bazaar* dating range, and the Row 26 English coverage (no `Saturninus` or `Aurelian` in `npnf109`; no division on compunction).

## The rcg script, run unchanged

`tools/verify_world_source_docs.py` from `origin/claude/rcg-doc02-final-fixes` (commit `58f03aa86`), run as `python tools/verify_world_source_docs.py aec --texts cic/texts --window 350-430`, before the fixes (documents at `origin/main`) and after. Both runs exit 1 with 5 of 8 checks passing (`texts-exist`, `cross-refs`, `same-volume`, `universal-claims`, `doc-vs-registry`) and 3 failing:

- `registry-vocab`: 47 rows fail "row has 11 cells, expected 10". The aec Registry has an 11th column (Discovery). Not a document defect.
- `absence-claims`: Doc_02 lines 55 and 67 say the *Adversus Judaeos* homilies are not vendored; the script finds the phrase in `augustine_in-ioannis-evangelium-tractatus-lat_migne-garnier1902-t3-pt2.txt`. That file is Augustine's tract, a mention and not the homilies. A judgment for the project lead.
- `quotes`: 5 Registry quotations (lines 41, 44, 46, 47, 49) are notes quoted from the corpus-map file, which the script does not search. Before the fixes, it also reported the canon XI quotation as informational only (found in the file, not at the cited locus).

Under the ruling, approval is recorded only if the script passes, so Doc_01, Doc_02 and the Source Registry stay not approved to proceed.
