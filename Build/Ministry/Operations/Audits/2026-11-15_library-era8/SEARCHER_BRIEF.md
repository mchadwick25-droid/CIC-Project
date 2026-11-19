# Searcher brief (Library thread). Read all of it before starting.

You find public-domain printed editions on archive.org (and dbnl.org for Dutch) and download their OCR text
for a scholarly source library. You do NOT touch the git repo at /home/user/CIC-Project except to list
filenames in cic/texts/ (ls | grep) to see what is already held. No model calls, no paid services.

## Hard rights rule
Take an item only if ALL hold:
- Its printed imprint year is 1930 or earlier, and you READ that year on the title page in the OCR text itself
  (quote the line). The host's `date` field alone is not enough. A modern reprint or facsimile counts by its
  own date (a 1960s reprint is out). A library stamp is not an imprint.
- The archive.org record is not access-restricted (`access-restricted-item` absent/false; not a lending-only
  book: collections `inlibrary`, `printdisabled`, `internetarchivebooks` lending items are OUT), and a full
  `_djvu.txt` is downloadable.
- No NC/ND licence and no permission notice in the record. If there is one: do not take, report "held for Mark".
- If no imprint can be read in the OCR: do not take; report it as "imprint unreadable" with the identifier
  (the Library thread may check the page image).
Prefer: the tradition's own-language original AND an English translation printed by 1930 where one exists.
Prefer the scan with the cleanest OCR (University of Toronto, Princeton Theological, Harvard scans are often
good; Google-scanned items are often poorer). One good scan per edition; do not take duplicates.

## Allowed commands (use ONLY these shapes; anything else may stall on a permission prompt)
Work only inside the directory given to you as WORKDIR (under the scratchpad). `cd WORKDIR && ...` first.
1. Search:
   curl -sS -m 60 "https://archive.org/advancedsearch.php?q=<urlencoded query>&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=year&fl%5B%5D=creator&rows=30&output=json" | python3 -I -c "import sys,json; [print(d.get('identifier'),'|',d.get('title'),'|',d.get('year'),'|',d.get('creator')) for d in json.load(sys.stdin)['response']['docs']]"
   (query fields: title:(...), creator:(...), mediatype:texts, year:[1600 TO 1930], language:(...))
2. Record:
   curl -sS -m 60 "https://archive.org/metadata/<identifier>" | python3 -I -c "import sys,json; m=json.load(sys.stdin); md=m['metadata']; print({k:md.get(k) for k in ['title','creator','date','publisher','language','licenseurl','possible-copyright-status','access-restricted-item','collection','volume']}); [print(f['name'],f.get('size')) for f in m['files'] if f['name'].endswith('_djvu.txt')]"
3. Download (into WORKDIR, keep the host's filename):
   curl -sS -L -m 600 -o <identifier>_djvu.txt "https://archive.org/download/<identifier>/<name of the _djvu.txt>"
4. Check: wc -c -w <file> ; grep -n -m 20 -i -E "<pattern>" <file> ; sed -n '<a>,<b>p' <file> ; head ; ls ; ls /home/user/CIC-Project/cic/texts | grep -i <pattern>
Never read a whole file. Never pipe to sh. Never use pip, git, rm -r, sudo, wget, or any other host. If a host
refuses or a command is denied, do not work around it: stop that item and report it.
Search at most ~8 queries per want; then report "not found" with the queries you ran.

## For each item you take, verify and report
- byte count from `wc -c` EQUALS the `size` in the metadata record (complete download);
- the title-page lines (quote 3-8 OCR lines with their line numbers, including the year line);
- OCR readability: sample 15 lines from the middle; say plainly if the script is garbled (Greek, Cyrillic,
  Armenian, Syriac, Arabic are often unreadable in OCR: say so; an unreadable own-language text is still worth
  reporting but mark it "OCR unreadable" and do NOT download a second scan unless it is clearly better);
- where the wanted work starts and ends in the file (line numbers), and what else the volume holds;
- where editorial matter sits (preface, introduction, notes, index: line ranges, roughly);
- whether several voices are mixed (incoming letters, dialogues, minutes).

## Hand back (final message), a table, one row per want
want | result (TAKEN / NOT FOUND / NOT TAKEN + why / HELD FOR MARK / ALREADY HELD: filename) | identifier | file path in WORKDIR | bytes (wc = host?) | words | author, title, editor/translator | imprint (place, publisher, year) + quoted title-page line with line number | language(s) | archive.org licence/copyright fields | work start-end lines; other contents | editorial matter lines | OCR quality | cautions for profile writers
Then: the list of every query that found nothing. Keep the report under 1,200 words. Facts only: never guess a
year, an editor or a line number; if you did not read it, say "not read".
