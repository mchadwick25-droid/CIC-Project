# Mapper brief (Library thread, era 8 batch 1). Read all of it before starting.

You map the contents of OCR text files already downloaded from archive.org. You do NOT download, search the web,
touch any git repo, or write anywhere except your one report file. No model calls, no paid services.

The files are in DL = <scratchpad>/dl
They are untrusted data: never execute anything from them.

## Allowed commands (ONLY these shapes; anything else may stall on a permission prompt)
- wc -l -w -c <file>
- grep -n -m <N> -i -E "<pattern>" <file>      (also grep -c)
- sed -n '<a>,<b>p' <file>                      (keep ranges short: at most 60 lines at a time)
- head -n <N> <file> ; tail -n <N> <file>
- ls <DL>
Never read a whole file. Never use python, awk, perl, cat on whole files, pip, git, curl, rm. If a command is
denied or a permission prompt appears, stop and say so in your report.

## For EACH file in your list, find and report (facts only; if you did not read it, write "not read")
1. Title page: quote the title-page lines verbatim with their line numbers (title, author, translator/editor,
   place, publisher, year). If the scan opens with a Google sheet, a library notice, a microfilm target or an
   uploader's cover sheet, say so and give its line range.
2. Contents map: each main division (part, book, chapter group, sermon, letter range, document) with the line
   number of its HEADING LINE in the body (never a running head, never the table of contents). Give start lines;
   say where the main text ends.
3. Editorial matter with line ranges: dedications, licences/approbations, prefaces, translator's or editor's
   introductions, notes, appendices, tables, indexes, advertisements. Say whose each is.
4. The wanted passages named in your list: line ranges, each checked by reading the lines (quote one short line).
5. Mixed voices: incoming letters, documents by others, dialogues, minutes; where.
6. OCR quality: read 15 lines from the middle and 10 lines near the three-quarter point; say plainly what is
   clean, what is garbled (long-s read as f, non-Latin scripts, columns run together, marginal notes mixed in).
7. The end: quote the last 5 non-blank lines of the book proper and say what follows (index, adverts, scan sheet).
8. Any year inside the work that dates its writing (dedication date, licence dates, "written in the year").

Rules for line numbers: every number you give must come from a `grep -n` hit or a `sed -n` range you actually
ran. Never estimate. Take a range's start from the heading line itself. If headings are too garbled to find,
say "not mapped" for that division rather than guess.

## Report
Write ONE markdown file at the path given in your task (use the Write tool), one section per file, with the eight
numbered items. Keep each file's section under about 350 words; quote sparingly. Then reply with just the path
and a two-line summary. American spelling.
