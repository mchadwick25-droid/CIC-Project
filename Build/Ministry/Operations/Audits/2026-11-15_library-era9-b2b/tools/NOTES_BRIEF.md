# Checker brief: write a true content note for every file

You are given a JSON list (your input file, named in your task). Each item has: `file` (a staged text, to be read
only), `key`, `title`, and draft fields from a quick first pass (`draft`, `draft_divisions`, `draft_editorial`,
`draft_mixed`, `draft_cautions`). Each file is: 9 header lines, a blank line, a row of underscores, a blank line,
then a scan's OCR text from line 13. **All line numbers you write are the file's own line numbers** (what `grep -n`
and `sed -n` show). The drafts cite line numbers of the raw OCR, which are off by 12 or more: never copy a draft
line number; find every line yourself. Do not edit any file.

The drafts were written quickly and are not trusted: they carry claims from outside knowledge, wrong line numbers,
praise words and search narration. For each item, read the file and write a `content` note and a `locus`.

## Rules for `content`

- Plain descriptive sentences about what the file holds. Every statement must be something you saw in the file
  (title page, contents list, headings, prefaces, the text itself). Give line numbers for the main divisions you
  verified (contents list, where the text starts, where it ends, where an index or advertisements begin).
- Nothing from outside knowledge (what a book was later called, what it led to, who someone was beyond what the
  title page says), no evaluation ('standard', 'leading', 'famous', 'important', 'classic'), and no word about
  the search or this project ('picked', 'located', 'not taken', 'wanted', 'row').
- Keep, when true and visible on the page: the volume and edition statement (vol. 1 of 2; fifth edition), that it
  is a translation and from what language, that the author is not named on the title page, a second title page
  or a second work bound in the same scan (say where it starts), prefaces and editors' matter with their line
  ranges ('Editorial matter: ...'), other voices in the file ('Mixed voices: letters to him are printed at ...';
  if you saw none, say nothing), and how the text is divided ('Divisions: ...').
- If the header's Title or Creator line says something the title page in the file contradicts, say so in your
  final message (do not put it in the note).
- If you could not verify a statement, leave it out. Shorter and true beats longer. 40 to 110 words. No word
  counts. No line breaks inside the text. American spelling. No double quotes inside the text: use single quotes.

## Rules for `locus`

Either exactly `the whole volume; not mapped`, or one to three passages you verified, in this form:
`<what> at lines A-B; <what> at lines C-D; the rest not mapped`.
A passage must start and end where you say. No 'throughout', 'about', 'search for'. Names in `<what>` are spelled
as the file spells them or in plain modern English; add no facts. Where your task names a person a file is wanted
for, try to locate one passage on that person (grep the name) and give it as a locus.

## How to work

- Tools: Read, Grep, and in Bash only `grep -n`, `sed -n 'A,Bp'`, `head`, `wc -l`. Read by line range (60 lines at
  a time at most); never print a whole file. Typical checks per file: lines 13-150 (front matter and title page),
  a grep for CONTENTS / INDEX / PREFACE / CHAPTER (or the language's words), and the last 40 lines.
- Write your output with the Write tool to the output path named in your task: a JSON list of
  `{"key": ..., "content": ..., "locus": ...}` for every item, same keys as the input. Valid JSON, UTF-8.
- Your final message: the number of items done, then one line for each item where the draft or the header was
  wrong on a point of fact (key: what was wrong). Nothing else. If a command is refused or a permission prompt
  appears, stop that step and say so.
