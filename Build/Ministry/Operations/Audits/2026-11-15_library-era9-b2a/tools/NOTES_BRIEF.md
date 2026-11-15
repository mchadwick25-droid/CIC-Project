# Checker brief: write a true header for every file

You are given a JSON list (your input file, named in your task). Each item has: `file` (a vendored text in
/home/user/CIC-Project/cic/texts/), `key`, a draft `title`, `creator`, `publisher`, `year`, the `want` the file
was taken for, and `hints` from the person who found the scan (divisions, editorial matter, other voices, wanted
passages). Each file is: 9 header lines, a blank line, a row of underscores, a blank line, then the scan's OCR
text from line 13. **Every line number you write is a line number of the file itself** (what `grep -n` and
`sed -n` show). The hints' line numbers are from before the file was made and are off by a few lines or a few
dozen: use them only to find the place, then give the file's own numbers.

The hints were written quickly and are not to be trusted: earlier hints carried claims from outside knowledge,
wrong line numbers and praise words. Your job: read the file and write, for each item, `title`, `creator`,
`publisher`, `content`, `locus` and `flags`. You edit nothing in the repository.

## `title`, `creator`, `publisher`

As the title page prints them, in the page's own language and script (correct plain OCR slips in a word only
when the reading is certain from the page; keep old spelling). `title`: the title-page wording down to the
edition or volume statement, one line, no year, no final full stop. `creator`: the author as printed, then
translators or editors as printed, separated by '; '. If the title page names no author, write exactly what
it prints (for example 'by his sister') or 'not named on the title page'. `publisher`: 'Place: Publisher' as
printed. If the title page cannot be read in the OCR, keep the draft value and say so in `flags`.

## `content`

- Plain descriptive sentences about what the file holds. Every statement must be something you saw in the file
  (title page, contents list, headings, prefaces, the text itself). Give line numbers for the main divisions you
  verified (contents list, where the text starts, where it ends, where an index or advertisements begin).
- Nothing from outside knowledge (what a book was 'later titled', what it led to, who someone 'was' beyond what
  the title page says), no evaluation ('standard', 'leading', 'famous', 'important', 'classic'), and no word
  about the search or this project ('picked', 'located', 'not taken', 'wanted').
- Keep, when true and visible on the page: the volume and edition statement; that it is a translation and from
  what language; that the author is not named on the title page; prefaces and editors' matter with line ranges
  ('Editorial matter: ...'); other voices in the file ('Mixed voices: letters to him are printed at ...'; if
  none, say nothing); how the text is divided ('Divisions: ...'); a second work bound in the same scan (look
  for a second title page) with the line where it begins.
- Where the `want` names a person, say in one sentence where the file tells of that person, with line numbers,
  spelled as the file spells the name. If the file does not name the person, say so plainly.
- If you could not verify a statement, leave it out. Shorter and true beats longer. 50 to 120 words. No word
  counts. No line breaks inside the text. American spelling. English, whatever the file's language.
- Do not use double quotes inside the text; use single quotes for quoted words.

## `locus`

Either exactly `the whole volume; not mapped`, or one to three passages you verified, in this form:
`<what> at lines A-B; <what> at lines C-D; the rest not mapped`.
A passage must start and end where you say. No 'throughout', 'about', 'search for'. Names in `<what>` are
spelled as the file spells them or in plain modern English; add no facts.

## `flags`

A short string, or ''. Use it for: a title-page year that differs from `year` or that you could not find; a
reprint or modern-edition sign (a date after 1930, 'reprint', a publisher of reprints); a notice asking for
non-commercial use or permission; a second work in the scan with a different date; text that is not what the
title says; OCR too poor to read (say where).

## How to work

- Tools: Read, Grep, and in Bash only `grep -n`, `sed -n 'A,Bp'`, `head`, `wc -l`. Read by line range (60 lines
  at a time at most); never print a whole file. Typical checks per file: lines 13-140 (front matter and title
  page), a grep for CONTENTS / INDEX / PREFACE / CHAPTER (or the language's words), the places the hints cite,
  a grep for the person the want names, and the last 40 lines.
- Write your output with the Write tool to the output path named in your task: a JSON list of
  `{"key", "title", "creator", "publisher", "content", "locus", "flags"}` for every item, same keys as the input.
  Valid JSON, UTF-8.
- Your final message: the number of items done, and one line for each item with a non-empty `flags`. Nothing else.
