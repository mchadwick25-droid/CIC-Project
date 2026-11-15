# R1 changes: Library era 9, batch 2a (2026-11-15)

What was done about `R1_review.md`. Nothing was patched in place: each fault came from the rules the files are
generated from, so the rules were corrected and every file, shelf row, registry entry and queue row was
generated again.

## Blocking findings

- **B1, B2, B3 (the Assam jubilee volume, Darby's Seven Lectures, the Valaam book).** Confirmed. The rule that
  finds the imprint took the first line near the head of the file that prints the year, which was a library
  slip, the year the lectures were given, and a centenary span. The rule now takes first a line that holds
  the year and nothing else, and only then a line that prints it among other words. The three headers and shelf
  rows now cite lines 176, 44 and 58. Every other citation was compared before and after the change: only
  these three moved, with the second volume of Garcia Moreno (its title page is printed twice; the citation
  moved from one printing of it to the other) and Adriaanse (N7).
- **B4, A Guerra de Canudos.** Confirmed: the header contradicted itself. The page image of leaf n6 prints
  "Rio, Typ. Altina, 1902", and the catalogue says 1902. The OCR of that same title page, at line 46 of the
  file, misreads the year as 1903. There is no second leaf with an imprint; the earlier header was wrong to
  speak of a cover. The header now says so, and the caution and the search log were corrected.

## Non-blocking findings

- **N1, Klein.** Corrected. The file names 'Joseph Mkasa'; the content note now gives his passage (lines
  7022-7045), the want is rows 210 and 318, and the caution was rewritten.
- **N2, page marks.** The removal takes only a line that holds the whole mark. Removing the broken forms would
  move the line numbers the checkers verified, so they were left, and the Provenance note of each of the three
  files now says about how many such lines remain. The sentence in `CFT-Wants.md` was corrected.
- **N3, the two Iglesia Filipina Independiente books.** Both headers now say the title page cannot be read in
  the OCR and that the title and publisher are from the catalogue record. The Documentos header names the
  misread "1936" at line 213.
- **N4, Macedo Costa.** "Two prefixed letters", with the plain statement that the front matter was printed
  after the catalogue's year. The "1899" at line 12619 was not added to the header: it could not be checked
  against a page image in this batch.
- **N5, Darby's Dialogues.** The content note now says the second work's title page shows no year in the OCR
  and that the header's year is that of the first work. The shelf note already said the title page names no
  author and that the host record names Darby.
- **N6, the Chronicle of Menelik II.** No change; the finding confirms the cut and the date.
- **N7, Adriaanse.** The citation now points at the whole imprint line, line 80.
- **N8, Sheptytsky.** One sentence added to the search log on the misnamed archive.org item.

## Found by the Library thread while fixing

- The line numbers in four headers (My Life in Christ, Pharmakidis, the Demerara report, Darby's Studies) had
  slipped back to their first-pass values in one regeneration, because the shift for a preamble removed after
  the checkers had read the file was worked out from the file on disk. The shift is now a fixed value in
  `overrides.json`. The review read the corrected files.
