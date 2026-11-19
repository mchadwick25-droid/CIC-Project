# R1 changes: Library era 9, batch 1 (2026-11-15)

What was done about `R1_review.md`. Nothing was patched in place: the faults came from the spec the files were
generated from, so the spec was corrected, all the files were removed and every file, shelf row, registry entry
and queue row was generated again from it.

## Blocking findings

- **B1, Eddy's Retrospection.** Not a rights failure. The title page prints 1892 under the publisher's
  address; the OCR dropped the line, and the Library thread had read it on the page image (leaf n8) before
  vendoring. The header wrongly repeated the searcher's "title page undated". The header now cites the page
  image.
- **B2, Offord's Jerry McAuley.** Confirmed: the title page image (leaf n8) prints no year. The file was taken
  out. Mark then ruled the same day that a copyright notice dated 1930 or earlier stands for the date (see the
  Decision-Log), so it was taken back in, with the rights line naming the copyright notice of 1885.
- **B3, de Cock.** The header now says de Cock issued the pieces; the content note names the two writings and
  the two forewords, and says the letters of the second are by others.
- **B4, Kuyper.** The page image (leaf n6) reads "Amsterdam, Höveker & Zoon, 1883". Corrected.

## The content notes and loci

The review found unsupported details in eight of the 41 notes it checked, so the fault was general. Four fresh
Fable checkers then checked every content note and locus of all 99 files against the text, sentence by
sentence, and rewrote each from what the file shows. Claims from outside the file, praise words and search
narration were removed, and line numbers were corrected. Among what they found:

- The Philadelphia Declaration of 1828 is the first of five Friends' pamphlets bound in one scan (1828-1852).
- The One of China's Scholars scan also holds Pastor Hsi: One of China's Christians (twelfth edition), from OCR
  line 7854. Row 205 now has the full Life.
- The Allgemeine Missions-Zeitschrift scan holds two yearly volumes, 1918 and 1919. The file was renamed.
- Stone's own narrative is chapters I to X; chapters XI and XII are Rogers's.
- The Vatican council volume says at OCR line 80 that it is tome VII of the Collectio Lacensis.
- The Philosophy of Revelation is a translation; its preface names the translators.

Search narration now stands only in `Search_Log.md`.

## Other points

- Imprint citations are now computed from the text (the first title-page line that prints the year), or name
  the page image leaf where the Library thread read it.
- Butcher is shelved on the Coptic revival only. One of China's Scholars is `needs-ruling`.
- Der Lutheraner's filename now carries 1844, as its header does.
- Loci without line numbers were replaced by verified passages or by "the whole volume; not mapped".
- The registry and queue wording no longer says "the wanted passages located".

## Added after the ruling on undated title pages

Mark's ruling of 15 November ("Copyright notice yes, preface with a check") let in six more files whose title
pages print no year: McAuley's Transformed (copyright 1876), Booth-Tucker's Life of Catherine Booth, vol. 1
(copyright 1893), The Story of the Welsh Revival (copyright 1905), and Ellis's History of Madagascar in two
volumes (preface of 10 October 1838; the catalogue says 1838). Wayland's Life of Trust came in under the old
rule: its title page image prints 1868 under a library stamp. Vol. 2 of Ellis prints no date of its own and
rests on vol. 1's preface and the catalogue; its header says so.

Still out, for the next batch: Kuyper's Stone Lectures, Hudson Taylor's Retrospect, Walsh on the Uganda
martyrs, Catherine Booth's Aggressive Christianity, and the Kaiserswerth "by a lady" account. Each needs its
dated preface or copyright notice found and checked against the catalogue.
