# Card check: Apocryphal and Pseudepigraphal Literature (`apocryphal-and-pseudepigraphal-literature`, tradition)

Checker: not the card writer. Read: `CLAUDE.md` (Trust and source fidelity), Kit Part 1, `kinds/tradition.md`, the card role, the brief (final), `Outline.md`, `Review.md`, `Fresh_Trust.md`, `Fresh_Trust_Second.md`, `Fresh_Listen.md` (`Fresh_Read.md` does not exist for this brief), `Card.existing.json`, the card, `Card_Edits.md`. No entry file: the entry exists in the census.

## Verdict: FIX

Nine changes, below. Everything else passes.

## What passes

- **Nothing else moved.** A field-by-field diff of the card against `Card.existing.json` shows only `voices[0]`, `voices[3]` and `legacy` changed, and four keys added at the end, as `Card_Edits.md` lists. `documentedStories`, `why`, `teaser` and `relationsSummary` are word for word in the card file, with their changes under Entry fields.
- **Quotations.** Three `quotationOriginals`, one for each quoted span in the brief, each `modern` exact. Each `printed` re-read: NPNF 2.1 33704-33707 and 33711-33712; CSEL 20 12262-12264 (line breaks folded). `englishPrinted` re-read: ANF 3 57782-57789, with the endnotes left out. Each `original` re-read: Schwartz 2510-2513 (from ἀδελφοί) and 2515-2516, as the scan reads them, with the faults named in `uncertain`; Rufinus 2576-2578 and 2582-2583 re-read for the confirming Latin. Greek checked by hand: ἀδελφοί … Πέτρον καὶ τοὺς ἄλλους ἀποστόλους ἀποδεχόμεθα ὡς Χριστόν, τὰ δὲ ὀνόματι αὐτῶν ψευδεπίγραφα ὡς ἔμπειροι παραιτούμεθα, γινώσκοντες ὅτι τὰ τοιαῦτα οὐ παρελάβομεν, and εἰ τοῦτό ἐστιν μόνον τὸ δοκοῦν ὑμῖν παρέχειν μικροψυχίαν, ἀναγινωσκέσθω. Both renderings hold, every clause, nothing added. Latin of Q3 checked clause by clause: it holds ("conuictum", "was found out"; "loco decessisse", "he left his office"). None runs under six words, so none is "checked at card", and none carries `secondReading`.
- **`legacy` additions** re-read: NPNF 2.4 68714 ("(For 367.)"), 68825 ("an invention of heretics"); NPNF 2.3 39502-39505 ("we reckon among the apocryphal writings"); NPNF 2.6 20705-20710 ("Let her avoid all apocryphal writings", "that it requires infinite discretion to look for gold in the midst of dirt."). Verbatim.
- **`uncertain`** re-read at its lines: ANF 9 30600-30610 (Origen), 435-441 and 784 (Akhmim, "I Simon Peter"); ANF 8 36602-36603 and 36825-36827 (manuscripts; Joseph "I have children, and I am an old man"); ANF 8 48109-48121 and Gebhardt 10558-10559 (Thecla's two ends); McClure 3786-3793, 3815-3819; NPNF 2.1 33712-33743, 33812-33816; NPNF 2.3 39502-39515; CSEL 20 12286 ("conuictum apud Ioannem atque Iun"). Each holds. Every item the outline, review and fresh reads send to the card is on it (Fresh_Trust M4, the identity question: item 3).
- **briefReferences**: eight, one per run of the brief; none names what the brief no longer tells.
- **Entry fields** in `Card_Edits.md`: each justified by its evidence (re-read NPNF 2.1 33690-33693 and Schwartz 2502-2504 for "letter"; ANF 9 435-437 for the grave "supposed to be a monk's"). The two modern works under `sources` move to `modernWorks` word for word; the three editions go to `modernWorks` with notes that say what each covers.
- **Validator.** A scratch census outside the repository with the card fields merged and the brief as `longDescription`: `node tools/validate-census.mjs <copy>` (full run, quotes included): 0 errors, 4 warnings, none on this entry. Re-run with the fixes below applied: 0 errors.
- American spelling throughout, except in printed wording quoted verbatim.

## FIX

### Card fields (the card file)

1. **`voices[0]`.** A modern judgment stated as content, and the same claim the writer rightly removed from `legacy` and `why` (the brief no longer makes it; Part 1, Rigor: a judgment only a modern work makes stays out of the card).
   - Old: "The Protevangelium of James - under James's name, and the source of nearly everything later Christians believed about Mary's childhood"
   - New: "The Protevangelium of James - a book under James's name that tells of Mary's childhood"
   - Evidence: ANF 8 37167; the brief, "One under James's name ... tells of Mary's childhood."

2. **`legacy`.** A modern inference stated as content, in a short text Part 1 governs (the writer's own not-found list; no held source).
   - Old: " Medieval art and legend probably took most of what they knew of those deaths from them."
   - New: "" (delete the sentence; the one before it ends "Philip hung by his ankles.")

3. **`sources.about`.** `uncertain` item 11 (the Muratorian fragment's Apocalypse of Peter line) rests on a file not in `sources` (Source sheet, Set aside: anf05 60160-60185; re-read 60176-60178, "We receive also the Apocalypse of John and that of Peter, though some amongst us will not have this latter read in the Church").
   - Old: (no entry)
   - New, appended after the Athanasius entry: `{"title": "The Muratorian Fragment (Ante-Nicene Fathers 5)", "author": null, "date": "1886", "language": "English", "file": "cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml"}`

### Entry fields (add to `Card_Edits.md` Entry fields for release; each composes with the writer's edits there, since none overlaps them)

4. **`documentedStories[0].text`, first quotation.** Quotation marks around words no held print gives (McGiffert, NPNF 2.1 33711-33712, words it otherwise; none of the vendored files holds this wording). Every quote must stand verbatim in its file.
   - Old: "‘If this is the only thing that seems to make bad blood among you, let it be read.’"
   - New: "‘If this is the only thing that seems to be causing bad feeling among you, let it be read.’"
   - Evidence: the brief's rendering, `quotationOriginals[0].modern`, from Schwartz 2515-2516.

5. **`documentedStories[0].text`, second quotation.** Same fault.
   - Old: "is measured: ‘the most part indeed was in accordance with the true teaching of the Saviour, but some things were added’, and he listed them."
   - New: "is measured: he found ‘many things in accordance with the true doctrine of the Saviour, but some things added to that doctrine’, and he listed them."
   - Evidence: McGiffert, NPNF 2.1 33813-33814, verbatim ("Saviour" is the print's spelling).

6. **`documentedStories[0].text`, third quotation.** Same fault.
   - Old: "‘we receive both Peter and the other apostles as Christ, but the writings that falsely bear their names we reject.’"
   - New: "‘we receive Peter and the other apostles as we receive Christ. But the writings falsely put under their names we refuse.’"
   - Evidence: the brief's rendering, `quotationOriginals[1].modern`, from Schwartz 2510-2512.

7. **`documentedStories[0].text`.** A modern judgment stated as content, the same kind the writer removed from `documentedStories[1]` ("the best-documented case") and from the caveat ("generally accepted").
   - Old: " The episode shows the process by which the second-century church actually sorted its books — not by decree, but by a bishop reading a text against what he already knew of the apostolic teaching and telling a congregation why."
   - New: "" (delete the sentence)

8. **`documentedStories[1].text`, Thecla's veneration (the writer's flag).** Ruling: remove. It is a comparative judgment no held old source makes (the old sources show one shrine, its cells and a reading: McClure 3786-3793, 3815-3819), so under Part 1, Rigor it stays out of the card; and the outline's Do not say bars it in so many words ("Thecla became one of the most venerated women" → "Show only the shrine, the cells and the reading"). That no held source contradicts it does not save it: the bar is support, and the outline's ruling on this claim is explicit.
   - Old: "The Acts of Paul went on circulating for centuries, Thecla became one of the most venerated women in the Eastern church, and the presbyter’s name was never recorded."
   - New: "The Acts of Paul went on circulating for centuries, and the presbyter’s name was never recorded."

9. **`documentedStories[1].caveat`.** A modern judgment of the witness's reliability, the same kind as the "reads as genuine" line the writer removed from `documentedStories[0].caveat`.
   - Old: "Tertullian is polemical but had no reason to invent the confession."
   - New: "Tertullian is polemical."

## Ruling: the entry `dates` "c. 100-900" (`start` 100, `end` 900)

Not changed at the card. No held source gives either year, so it is **not found**, but nothing held contradicts it: the brief tells the second to fourth centuries as its window and the later books only as what came of it, while the entry spans the books' transmission, which held sources show running past the fourth century (Jerome's Letter 107, NPNF 2.6 20705-20710; the eleventh-century Paris manuscript of the Book of James, ANF 8 36602-36603). If anything, the held evidence would put the end later, not earlier. `start`/`end` are timeline data shared by every Atlas surface (census `meta.notes`), so a new span is the census owner's change, not a card fix. Release should record it as an open gap for the census owner: what the span is meant to cover, and a basis for 900 or a new end.

## Not found, left in (checked; none clearly wrong)

- The writer's list stands. Also left in, and noted: `voices[1]` "the register of Greek romance" (a modern genre comparison; not contradicted); `voices[2]` (reports a modern debate as unresolved, not as settled); `documentedStories[1].text` "a text composed by a known man in the recent past" (Tertullian's stated point is that Paul did not let a woman even learn boldly, CSEL 20 12264-12266) and the "whole culture" sentence; "disciplined the author" and the teaser's "loses his office" are borne out by Thelwall's "was removed from his office" (ANF 3 57789) and Jerome's "convicted by John" (NPNF 2.3 39514).
- `uncertain` item 1 "no other writer of his time ties that name to Rhossus" rests on the Source sheet's reading of Clement and Hippolytus (anf02 53018-53021, anf05 12442-12444); it stands as a statement of the record, not of a modern view.
