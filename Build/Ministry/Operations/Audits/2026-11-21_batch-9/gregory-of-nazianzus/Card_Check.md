# Card check: Gregory of Nazianzus (batch 9)

Read: `CLAUDE.md` (Trust and source fidelity), the card role, `gregory-of-nazianzus.brief.txt`, `gregory-of-nazianzus.card.json`, `Card_Edits.md`, `Card.existing.json`, `Review.md`, `2026-11-16_eight-standard-v1/drafts/gregory-of-nazianzus.refs.md`. No census entry is written (the person has one).

## Verdict: FIX

Two changes.

1. **`legacy.traces[3]`.** "His" follows a sentence whose subject is Sozomen, so it reads as Sozomen's translators. Sozomen's translator is Hartranft, as the card's own `briefReferences` say. Browne and Swallow translated Gregory: `sources.about`, Prolegomena; NZ 23172-23173.
   - Old: `His modern translators Browne and Swallow add that after Meletius of Antioch died, Gregory took the chair of the council.`
   - New: `Gregory's modern translators Browne and Swallow add that after Meletius of Antioch died, Gregory took the chair of the council.`

2. **`sources.about`, new last entry.** The new trace and the new `uncertain` entry rest on Socrates V.7 and Sozomen VII.7. The brief also draws on Socrates V.6 and Sozomen VII.5. The file holding them is not in `sources`. The form follows other census cards.
   - Old: (no entry)
   - New: `{"title": "Church History V.6-7 (Socrates); Church History VII.5, VII.7 (Sozomen)", "author": "Socrates of Constantinople; Sozomen", "date": null, "language": "English translation", "file": "cic/texts/npnf202_socrates-sozomen-ecclesiastical-histories.xml"}`

Log both in `Card_Edits.md`.

## The checks

1. **Edits against evidence.**
   - Edit 1 (trace) is held. The chapter heading is at SS 40769-40771. "At first consented ... particularly those of Egypt, objected ... withdrew his consent" is at SS 40812-40815. "Meletius shortly afterwards died, and Gregory assumed the Presidency of the Council" is at NZ 23172-23173. The trace's one wording fault is change 1.
   - Edit 2 (`uncertain`) is held. Socrates V.7, SS 15003-15006: "understanding that some murmured at his preferment because he was a stranger, after expressing his joy at the emperor's arrival, resigned". Sozomen VII.7 is as above.
   - Edits 3 and 4: the brief now reads "Apollinaris". That is the tree's spelling (`apollinaris-of-laodicea`), and Review finding 8 asks for it.
   - Edits 5 to 7 remove quotation marks around printed wording that is not verbatim in the brief, as the role requires. Edit 6's added "his words on keeping" is the fewest words that keep the line readable.
2. **Nothing else moved.** A JSON diff of `Card.existing.json` against the card shows only the seven listed changes. `Card.existing.json` equals the census card.
3. **`briefReferences`.** Every entry names something the brief still tells. None is to be removed.
4. **Census rules.**
   - The keys are allowed, and there is no `briefLength`.
   - The brief has four quoted spans and the card has four entries, matching word for word. The piglets sentence is split around "he wrote to Basil".
   - Each `printed` is verbatim at its lines: NZ 45783-45784, 45784-45785 and 37407-37408, and TJ 41568.
   - Both cited files are in `sources`. No audit file is named, and the spelling is American.
   - The card with its edits passes `tools/validate-census.mjs`, run on a scratch copy of the census: 0 errors. There is no outline, so no rendering from a held original is owed.
5. **Short quotation: Jerome's five words.** "my teacher in the Scriptures," is under six words. It keeps the `"same"` it already carries, and that verdict stands.
   - It came from a real blind reading by two readers (`2026-11-16_eight-standard-v1/renderings/eight/comparison.md`, Q14). Both gave "teacher", and the verdict was "same".
   - The change order of 2026-11-21 (Decision-Log, "Kit change order: reused quotes, fewer blind readings") removes the blind reading for short spans to save cost. It "reopen[s] no finished story". It does not overturn a reading already made, and the validator accepts "same" at any length.
   - My own check: against the print, Richardson's "my instructor in the Scriptures," (TJ 41568), "teacher" for "instructor" changes nothing.
   - Against the original: the Latin is now held, in `jerome_opera-pl23-part1-with-regula-pachomii-lat_migne1883.txt`, 61352-61353: "praeceptor meus, quo Scripturas explanante didici", printed "proceptor" by an OCR fault. It means "my teacher, by whose explaining I learned the Scriptures". The modern wording is faithful to it.
   - The scan is damaged, so the card rightly prints the English alone.
6. **Not found, and left in.**
   - The one claim the writer did not re-check, the 382 Philocalia trace, is held at NZ 47442-47451 (Letter 115): "about Easter a.d. 382 ... the Philocalia of Origen ... useful to students of literature".
   - I found nothing clearly wrong left in.
7. **Census entry:** none written, so there is nothing to check.
