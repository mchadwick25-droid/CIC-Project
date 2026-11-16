# Library search log: era 10 batch 2's follow-on, the periodicals, 2026-11-16

The record for the first part of the follow-on to era 10 batch 2
(`../2026-11-15_library-era10-b2/Handover.md`, "The follow-on (batch 2b): what to take"): the three periodicals.
Forty-five files were vendored (4,325,430 words): 31 numbers of The Christian East (761,254 words) and 14
volumes of The International Review of Missions (3,564,176 words). Thirteen listed items were not taken: the twelve volumes of the Proceedings of the Church Missionary Society,
which Mark has ruled out, and one number of The Christian East, which is past the line. The files and their shelves are in `Build/Ministry/Features/Source-Library/CFT-Wants.md` ("Era
10, batch 2b, the periodicals"). The books of the follow-on are a batch of their own. No quote, story or
lexicon entry was rendered.

## The check before the fetch

Run on 16 November against `cic/texts/REGISTRY.yaml`, `Build/worlds/_cross-world/download-queue-seed.yaml`,
`Build/worlds/_cross-world/WANTS-REGISTER.md`, `Build/worlds/_cross-world/CORPUS-USE.md` and
`Build/worlds/_cross-world/DOWNLOAD-QUEUE.md`, by archive.org identifier and by title. Run again against
`origin/main` just before intake.

- Twelve numbers of The Christian East and three volumes of the International Review (1922, 1923, 1928) are
  held. None of the 58 listed items is among them, and none is in the queue.
- Nothing of the Proceedings of the Church Missionary Society is held or queued.
- Neither register names any of the three periodicals.

## Searches

One search of archive.org's catalog for each periodical, by identifier prefix, to list what the host holds.

- **The Christian East**: 44 numbers to 1930, vols. I-XI. Twelve are held; the other 32 are the list.
- **The International Review of Missions**: yearly volumes for 1913 to 1930, three separate numbers of 1912
  (January, July, October), and index items. The list is 1914-1921, 1924-1927, 1929 and 1930.
- **Proceedings of the Church Missionary Society**: yearly volumes to 1921, and the early anniversary sermons
  as items of their own. The list is 1910-1921.

Located and left, by the coordinator's instruction of 16 November: the International Review for 1912 and 1913
and the Proceedings for 1906 to 1909 are a later batch of era 10 (Open-Gaps 303). The Proceedings before 1906
belong to era 9 and were not fetched. All of the Proceedings wait on the ruling asked for in call 1.

## Rights rule used

A printed date of 1930 or earlier: the masthead or cover of each number of The Christian East, and the title
leaf of each volume of the International Review. No file taken carries a permission notice, a copyright line or
a license. Nothing was taken under the rule for American books of 1931-1963.

Calls made here, which the coordinator or Mark may overrule:

1. **The Proceedings of the Church Missionary Society, 1910-1921: not taken; Mark has since ruled them out.** The twelve
   volumes are archive.org's scans of one microfilm (its source reels IA40329919-25 to -30). The item for 1912
   opens with the film's own target leaf, read on the page image (leaf n0): "FILM NO 96566 / PROCEEDINGS OF THE
   CHURCH MISSIONARY SOCIETY FOR AFRICA & THE EAST / 1801-1920 / © MM 1967 / REPRODUCTION OF THIS FILM
   PROHIBITED". The OCR carries it at host lines 1-9. Each volume's title page prints a year from 1910 to 1921
   (read in the OCR; 1913, 1917 and 1921 read on the page image), so the date rule is met by the prints. But a
   film maker's copyright line and a prohibition on the scan is not a basis the rights rule or rulings R1 to R12
   list, and era 8 left out a scan for a weaker line ("Reproductions may not be made without permission"). The
   question for Mark: does a microfilm publisher's notice of 1967 on the film bar the text of a print of 1930 or
   earlier taken from it? The same question governs the volumes of 1906-1909 and those before 1906. His answer,
   as the coordinator passed it on the same day (ruling R15): "Yes, keep them held (Recommended)". A microfilm maker's notice
   on a scan blocks taking it; another scan of the same print with no notice may be taken. A search for one
   found none: archive.org has only Google scans of volumes of 1819 to 1834 and one of 1855-56; HathiTrust's
   catalog search refused the request (HTTP 403) and the Google Books search refused it for quota (HTTP 429).
2. **The Christian East, vol. XI, no. 4: not taken, held for Mark.** Its cover and its masthead both print
   "Winter, 1930-31" (page images, leaves n0 and n2). A footnote at host line 1544 speaks of a letter "dated
   March 11th, 1931", and one at 1816 cites a book of "Faith Press, 1931". So the number was printed in 1931 and
   is past the line until January 2027.
3. **No film notice was found on The Christian East or the International Review.** No leaf and no OCR line of
   any of their items carries one, the first leaves of The Christian East for March 1920 (the first item of its
   reel) and of the International Review for 1914 included. The first leaves of the International Review for
   January 1912, which opens its reel, are too dark to read. The raw reel scans behind them
   (`sim_raw_scan_IA40806106-17`, `sim_raw_scan_IA1631424-02`) are access-restricted on the host, so the reel
   leaders themselves could not be looked at.
4. **The International Review for 1914 to 1920 is shelved on the Student Volunteer Movement and Edinburgh 1910
   entry**, which closes in 1920; the volumes from 1921 are on the ecumenical movement entry, which opens in
   1921, as the held volumes are. The title leaves of 1916 to 1920 name the Continuation Committee; the volumes
   from 1924 say the review "is published by the International Missionary Council".
5. **A shelf row for a writer rests on who the writer is, where the print does not say.** Bulgakov, Kartashev
   and Fedotov are placed on the émigré Orthodoxy entry, and Zankov and Parenta on the Balkan entry, by this
   thread's knowledge of the writers; the print gives a name and, for Parenta, the paper (Glasnik). The headers
   and row notes say only what the print says.
6. **Documents of the patriarchates of Alexandria and Jerusalem, of the Old Catholics and of the Church of the
   East's Indian metropolitan get no shelf row.** No census entry holds them. They are named in the content
   notes with their lines.
7. **A plan of union printed in 1920 is placed as context on the Chinese church entry**, whose window opens in
   the 1920s; the Mar Thoma statement of 1919 is placed as tradition on the Mar Thoma entry.

## How each file was checked

Fifty-eight djvu.txt files were fetched on 16 November (`fetch.py`, `candidate_ids.txt`); each byte count
equals the size archive.org lists (`fetch_manifest.json`). No record carries a rights field, a license or a
lending restriction. Nine Sonnet mappers mapped the contents under `MAPPER_BRIEF.md` (`mapper-reports/`; the
three reports on the Proceedings are kept for whoever takes them up after a ruling). The Library thread read
the masthead or title-leaf year of every file in the OCR, and read the page image wherever the OCR year was
garbled or missing, or the season spanned two years:

| file | leaf | what the page image prints | what the OCR reads |
|---|---|---|---|
| The Christian East, I.4 | n0 | "December, 1920] [Vol. I. No. 4." | the volume number is lost |
| The Christian East, II.4 | n0 | "December, 1921] [Vol. II. No. 4" | "192T" |
| The Christian East, III.4 | n0 | "December, 1922] [Vol. III. No. 4" | the volume number is lost |
| The Christian East, VIII.3 | n0, n4 | cover "Autumn, 1927. Vol. VIII. No. 3."; masthead the same | "Vor. VII." |
| The Christian East, IX.2 | n0 | "Summer, 1928.] [Vol. IX. No 2" | the year is lost |
| The Christian East, X.3 | n0 | "Autumn 1929.] [Vol. X. No. 3." | "1949" |
| The Christian East, XI.4 (not taken) | n0, n2 | "Winter, 1930-31" on the cover and the masthead | "1930-31" |
| Proceedings, 1912-13 (not taken) | n1 | "Church Missionary Society, Salisbury Square, London, 1913" | the year is missing |
| Proceedings, 1916-17 (not taken) | n0 | "... London, E.C.4, 1917" | the year is missing |
| Proceedings, 1920-1 (not taken) | n0 | "... London, E.C.4, 1921" | garbled |
| Proceedings, 1911-12 (not taken) | n0 | the film's target leaf (call 1) | host lines 1-9 |

The first leaf of each of the 31 numbers of The Christian East was looked at (`tools/grid.py` makes the sheet).
Eleven numbers were filmed with their cover, which prints the editors and "Published for the Anglican & Eastern
Churches Assocn. by the Faith Press, Ltd."; four dark covers were read after raising the contrast (March, June
and September 1925, Autumn 1927). The other twenty were filmed without a cover, and their headers say that no
publisher or editor is printed in the number as scanned. The first leaves of the International Review for 1914
were read on the page image; its title leaf agrees with the OCR. The other thirteen title-leaf years were taken
from the OCR, which is clean there and agrees with the host's date.

The spec that wrote the headers (`mkspec300.py`) checks 611 line anchors against the host text before it writes
anything: every heading line a header cites and both ends of every shelf row's range. `intake.py` here is the
era 8 script with the fetch date changed.

## What the mappers got wrong or left open

- A mapper took an advertisement for another periodical (The Christian East, April 1921, host lines 240-264,
  with the S.P.C.K.'s imprint) as a possible publisher line. It is not this journal's; the header says so.
- A mapper named a speaker (Alivisatos, Winter 1929) whose surname the OCR drops. The header quotes the OCR.
- In the International Review for 1914 and 1915 the articles have no by-line; the mapper matched writers to
  articles by the order of the notes on contributors. The headers name no writer on that basis.
- The mappers' line numbers were otherwise exact; the anchors that first failed were OCR garbles of the right
  heading, a running head taken for a heading (June 1927, the notes), and by-line lines given for heading lines.

## Cautions for profile writers

0. **A text batch 2 listed as not found is here.** The Ecumenical Patriarchate's encyclical of January 1920,
   "Unto all the Churches of Christ wheresoever they be", is printed whole in English in The Christian East for
   June 1920 (`christian-east_v1-no2-june-1920.txt`, host lines 155-462), signed by the locum tenens Dorotheus
   and the metropolitans of his synod. The print names no translator.
1. **The Christian East prints Eastern documents in English.** A row says where the print names the translator
   or the paper it was taken from. Where it names none, the English may be the sender's own or the journal's;
   do not call it either.
2. **Three texts are in another language**: the locum tenens's memorial to the League of Nations (December
   1921) and Scriban on Romania (May 1924) in French, with Batiffol's rejoinder (December 1924); the
   Archbishop of Utrecht's letter in Latin (January 1926). Meletios's letter of January 1922 is in Greek and
   English, and the Greek is garbled in the OCR.
3. **Summaries, not the text**: Anthony of Kiev on the papacy (February 1924) is "our translation of his own
   summary"; Parenta's "Penance" (Winter 1928) is "the substance of an article"; Kartashev's speech (Autumn
   1928) is "the substance of a speech".
4. **The scan lacks the end of four numbers**: February 1924 (the Athens Letter breaks off), May 1924 (the
   dedication service), March 1925 ("Remember Russia") and December 1921 (the last book notice).
5. **A leaf of 1921 stands in the number of December 1920**: a memorial card for Dorotheos of Brusa, who "died
   in London, Friday, March 17th, 1921".
6. **The headings of Tikhon's letter of 1918 (June 1920) and its last lines are damaged in the OCR.** Check a
   quotation against the page image.
7. **The survey of 1916 on Garrick Braid** (International Review, 1917) is a few lines and a footnote, drawn
   from the Church Missionary Review; it is an outside account at second hand.
8. **The Bishop of Dornakal's article of 1929 prints his see and not his name.**
9. **In the International Review the OCR often reads a 3 as an 8 in a year** ("1918" for 1913, "1928" for
   1923). Read the year on the page image before dating anything from a footnote.
10. **The "Quarterly Notes" of the International Missionary Council** are bound into each number from 1924.
    Those of October 1930 speak of plans for 1931; the volume itself is of 1930.
