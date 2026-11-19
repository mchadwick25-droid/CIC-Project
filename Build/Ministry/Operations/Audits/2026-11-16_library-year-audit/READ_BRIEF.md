# Brief: read the printed year of each item on its page image (year audit, read-only)

Each item in your batch is a text file held in /home/user/CIC-Project/cic/texts/ whose header gives one
publication year while the host (archive.org) record for the same scan gives another. Your job: read the year
that is PRINTED on the scan's title page (or, for a periodical or a volume without a dated title page, on the
imprint, the verso, the colophon, the cover or the preface date), on the PAGE IMAGE, and report it.
Change no file in the repository. No web search. No model or API calls. Only archive.org page images and
metadata, through the two tools below.

Tools (run from any directory; pass absolute paths):
- python3 -I <scratch>/leaves.py <ident>
  prints the host title/date/volume and the n-index of leaves typed Title or Cover.
- python3 /home/user/CIC-Project/Build/Ministry/Operations/Audits/2026-11-16_library-era9-located/tools/crop.py <ident> <n> <top> <bottom> <out.jpg> 1400
  saves leaf n cropped between fractions top and bottom of the page height (0 1 = whole page; 0.6 1 = the
  lower part, where an imprint usually is). Save images under
  <scratch>/img/ with the
  ident in the name. Then open the image with the Read tool and read it.
If no leaf is typed Title, look at leaves n=1 to n=12 (whole page, then crop the imprint). If the title page
has no date, look at its verso, the half-title, the end of the preface and the last leaves (colophon).
Roman-numeral dates: convert and give both. If a date is hard to read at full page, crop tighter.

Also read the first 12 lines of the held file (its header) and, where the header cites a line for the date
("line 42, on the title page"), read that line of the file: note whether the file's own text gives the same
year. Where a held file's header names several host items, check the one(s) given in your batch.

Things that explain a difference, to report in plain words when you see them: the host record gives the
date of volume 1 or of the series for a later volume; the host gives a date range for a set; the host gives a
reprint's or the original edition's date while the scan is another edition or a facsimile (say which the
title page shows: e.g. a 1966 reprint's own title page or imprint); the host date is an upload date; the
scan is a different volume or edition from the one the header describes.

Output JSON to the path you are given: [{"file":"...","ident":"...","leaf_n":N,
 "printed":"exactly what the page prints for place/publisher/date, short, e.g. 'PHILADELPHIA / THE HEIDELBERG PRESS / 1929'",
 "printed_year":"1929" (or "none found", or two years if the page prints two, with what each is),
 "header_year":"...","host_date":"...",
 "verdict":"header right|header wrong|unclear",
 "why_host_differs":"one plain sentence",
 "reprint_or_later_printing":"no|yes: what the page says",
 "note":"anything else a rights reader must know, e.g. a later copyright notice, a reprint imprint, a film or library stamp with a date; else empty"}]
"header wrong" only when the page image clearly prints a different year for THIS volume than the header
gives. "unclear" when you could not find or read a printed year: say what you looked at. Never guess a year.
Reply with only: the path, counts by verdict, and one line for each "header wrong" or "unclear".
