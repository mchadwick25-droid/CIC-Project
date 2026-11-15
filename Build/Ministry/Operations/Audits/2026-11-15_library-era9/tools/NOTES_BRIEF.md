# Checker brief: make every content note true to its file

You are given a JSON list (your input file, named in your task). Each item has: `file` (a vendored text in
/home/user/CIC-Project/cic/texts/), `key`, `title`, `content` (a draft Content note) and `locus` (a draft locus).
Each file is: 9 header lines, a blank line, a row of underscores, a blank line, then the scan's OCR text. So
**OCR line = file line - 12**. Every line number in the notes is an OCR line.

The draft notes were written quickly and some sentences are not supported by the file (a review found claims
from outside knowledge, wrong line numbers and praise words). Your job: for each item, check the draft against
the file and write a corrected `content` and `locus`.

## Rules for `content`

- Plain descriptive sentences about what the file holds. Every statement must be something you saw in the file
  (title page, contents list, headings, prefaces, the text itself). Give OCR line numbers for the main divisions
  you verified (contents list, where the text starts, where it ends, where an index or advertisements begin).
- Delete anything from outside knowledge (what a book was "later titled", what it led to, who someone "was"
  beyond what the title page says), every evaluation ("standard", "leading", "famous", "important", "classic"),
  and every word about the search or this project ("picked", "located", "not taken", "see report", "wanted").
- Keep, when true and visible on the page: the volume and edition statement (vol. 1 of 2; sixth edition), that
  it is a translation and from what language, that the author is not named on the title page, prefaces and
  editors' matter with their line ranges ("Editorial matter: ..."), other voices in the file ("Mixed voices:
  letters to him are printed at ..."; "none seen" is NOT allowed: say nothing instead), and how the text is
  divided ("Divisions: ...").
- If you could not verify a statement and could not find the truth quickly, leave it out. Shorter and true beats
  longer. 40 to 110 words is the right size. No word counts. No line breaks inside the text. American spelling.
- Do not use double quotes inside the text; use single quotes for quoted words.

## Rules for `locus`

Either exactly `the whole volume; not mapped`, or one to three passages you verified, in this form:
`<what> at OCR lines A-B; <what> at OCR lines C-D; add 12 to OCR line numbers; the rest not mapped`.
A passage must start and end where you say. No "throughout", "about", "search for". Names in `<what>` must be
spelled as the file spells them or in plain modern English; do not add facts.

## How to work

- Tools: Read, Grep, and in Bash only `grep -n`, `sed -n 'A,Bp'`, `head`, `wc -l`. Read by line range (60 lines
  at a time at most); never print a whole file. Typical checks per file: lines 13-140 (front matter and title
  page), a grep for CONTENTS / INDEX / PREFACE / CHAPTER (or the language's words), the lines the draft cites,
  and the last 40 lines.
- Write your output with the Write tool to the output path named in your task: a JSON list of
  `{"key": ..., "content": ..., "locus": ...}` for every item, same keys as the input. Valid JSON, UTF-8.
- Your final message: the number of items done, and one line for each item where you removed or changed a
  factual claim (key: what was wrong). Nothing else.
