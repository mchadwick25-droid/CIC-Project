# Curation how-to: Library thread

For workers who hand-curate one source file's division scheme. Read this once, then work one file at a time.

## What curation is for

The segmenter finds divisions by guessing at headings. For 237 of the 305 plain-text files that guess is not good enough (Stage 2 report, section 5). A curation file replaces the guess for one file. It says, from the edition itself, where each division starts and what its address is.

Three promises hold for every curation:

- Every passage stays addressable back to the vendored file and a byte range in it.
- A curation never drops text and never changes the vendored file. Text that a curation does not want shown is declared as furniture or apparatus. It is still counted, and still in the file.
- An address is a number or name the edition prints. Where the edition prints none, the address is the heading text plus the line number, and `scheme` says so.

## Files and commands

One curation per file, at `Sandbox/answering-library/curation/<file-stem>.yaml`. The stem is the vendored file name without `.txt`.

Run these from `Sandbox/answering-library`:

```
python -m answering_library.curate check  <file-stem>
python -m answering_library.curate sample <file-stem> --n 12
```

`check` prints the class before and after, the divisions, every threshold, and twelve sampled divisions. It exits 0 on pass, 1 on a failed check, 2 when the YAML cannot be loaded or applied. `sample` writes a review packet to `out/review/<file-stem>.md` (gitignored) for the second reader. Both read the file straight from `cic/texts`, so they take a second or two on most files.

## The format

Line numbers are 1-based, as in an editor. Patterns are Python regular expressions matched against each line with its spaces collapsed to one and both ends trimmed. In YAML, put patterns in single quotes so backslashes survive.

| Field | Required | Meaning |
|---|---|---|
| `file` | yes | Vendored file name, with `.txt`. |
| `scheme` | yes | One line naming the edition's own citation scheme. |
| `curator` | yes | Who drafted it, for example `Sonnet 5.5`. |
| `status` | yes | `drafted`, `sampled-ok` or `needs-redo`. Only the second reader changes it from `drafted`. A `needs-redo` file is not applied: the segmenter goes back to its own guess. |
| `rules` | rules or divisions | Ordered division-start rules, below. |
| `divisions` | rules or divisions | Explicit divisions: `start_line`, `locus`, `title`, optional `allow_oversize`. Use when no pattern can work. An explicit division wins over a rule on the same line. |
| `ignore` | no | Page furniture and running heads: `pattern`, optional `kind` and `lines`. A matching line is declared furniture. It stays in the file and in the word count, and is left out of passage text. |
| `apparatus` | no | Ranges that are not body text: `lines: [first, last]`, `kind` (front, index, notes), optional `locus`. Divisions in a range are flagged apparatus. |
| `language` | no | One language code for the whole file, when the filename gives none. |
| `languages` | no | Per-range override: `lines`, `language`, `evidence`. |
| `speakers` | no | Per-range override: `lines`, `state` (`known`, `mixed`, `unknown`), `voice` (only with `known`, and it must be an author of the file), `evidence`. |
| `evidence` | yes | List of `line` and `quote`. Each quote must appear on its line. See below. |

### Rules

Each rule has:

- `id` and `pattern`. Named groups in the pattern, such as `(?P<n>\d+)`, feed the templates.
- `locus`: a template for this level's part of the address, for example `chapter{n|int}`. No spaces and no `#`.
- `title`: a template, empty by default. Never write a title the edition does not print.
- `lines`: restrict the rule to `[first, last]`, or a list of such ranges.
- `parent`: the id of a higher rule. The full address is the parent's address, a slash, then this rule's part, so `book2/ch1`. The parent must have matched earlier. A rule with `division: false` only sets context and closes the division before it; its heading line goes with the next division.
- `skip_repeat: true`: a match whose address equals the previous match of the same rule is not a new division. This removes running heads that repeat a sermon or chapter number.
- `number`: the name of a group that holds the edition's numeral. The checker then reports repeats, backward steps, gaps and unreadable numerals in that series. It is a prompt to look, not a failure.
- `ocr_map`: single characters to replace before reading a numeral, for example `{'l': 'I', '1': 'I', 'Y': 'V'}`. Each entry is a claim about how this scan mangles type, so keep the list short.
- `fixes`: `line` and `set` of group values, for a heading whose OCR is beyond a map. The line must match the rule.
- `allow_oversize`: a sentence of evidence that this level is the finest the edition prints. It lets divisions over 5,000 words stand.

Template fields: the pattern's groups, `{line}` (the 1-based line), `{next}` (the next non-blank line), `{parent}`. Filters, chained with `|`: `int` (read a roman, arabic or word numeral; `int:3` pads to three digits), `slug`, `lower`, `upper`. The first matching rule on a line wins.

### Evidence

Evidence shows the scheme is the edition's own. List the first division, one or two from the middle, the last, and any heading you had to read through OCR damage. Quote the line as printed, damage included. `check` fails if a quote is not on its line.

## Workflow

1. Open the file. Read the library header, the front matter, the table of contents if there is one, and a few pages of body. Find how the edition numbers its divisions and what its running heads look like.
2. Write the `scheme` line and the first rule. Run `check`.
3. Read the numbers `check` reports. Look at every repeat, backward step and gap. Add `skip_repeat`, an `ocr_map` or a `fix`, or add a rule for a heading shape you missed.
4. Declare furniture (`ignore`) and apparatus ranges until coverage and word completeness pass.
5. Read the twelve sampled divisions in the output. Each should begin at its heading. If one begins in the middle of a thought, the rule is wrong.
6. Write the evidence list.
7. Run `check` until it exits 0. Run `sample` and leave the packet for the second reader.

Do not run the full segmenter for a single file. `check` does the same work for one file.

## What counts as curated

All of these must hold:

- Every address is unique.
- Divisions and declared apparatus cover at least 95% of the text that is neither library header nor declared furniture.
- No body division is over 5,000 words, unless its rule or entry carries `allow_oversize`. Apparatus divisions are exempt.
- Every rule matched, every fix landed on a match, every evidence quote is on its line.
- Passage words plus furniture words equal the words of the file.
- Every passage byte range, read back from the vendored file, reproduces the passage text, less only words on declared furniture lines.

A file that passes is class `curated` in the manifest. A file that fails keeps its divisions and falls back to `partial` or `none`, with the reasons in the manifest.

## What the second reader samples

The reader gets the packet from `sample`: the scheme, the evidence, twelve evenly spaced divisions with the lines around each start and end, the three smallest and three largest divisions, the apparatus ranges, and the check output. The reader answers five questions:

1. Does each sampled address restate what the printed heading says, with no number the edition does not print?
2. Does each sampled division begin at its heading and end where the next begins?
3. Is any apparatus actually body text, or any body division actually apparatus?
4. Do the evidence quotes show the scheme is the edition's own?
5. Is every `fix`, `ocr_map` entry and `allow_oversize` sentence true to the page?

The reader sets `status` to `sampled-ok` or `needs-redo` and says why in the commit message. A worker does not set `sampled-ok` on its own work.

## Forbidden

- Editing anything under `cic/texts/`. The vendored file is the record.
- Inventing an address. If the edition prints no numbers, use the heading text plus the line number, and say so in `scheme`.
- Reading a missing numeral from the sequence alone. A `fix` needs a printed heading on that line, quoted in `evidence`.
- Titles the edition does not print.
- Using `ignore` or `apparatus` to hide body text so that a check passes.
- Notes, history or review talk inside the YAML. Put them in the commit message or in this folder.
- Changing the segmenter or the thresholds. Ask for a change order.

## Pilot results

| File | Scheme | Class before | Class after | Divisions | Words in passages |
|---|---|---|---|---|---|
| `augustine_de-catechizandis-rudibus-lat_krueger1893.txt` | Maurist chapters 1 to 27 | none | curated | 27 chapters, 2 apparatus | 27,046 + 541 furniture = 27,587 |
| `koch_cyprian-und-der-roemische-primat-deu_1910.txt` | Koch's chapters I to XXI | partial (addresses repeat) | curated | 21 chapters, 2 apparatus | 63,646 + 390 furniture = 64,036 |

Two lessons for the larger files. A Migne sermon volume (for example PL38) marks true sermon headings with a footnote letter or a star, while running heads repeat the number bare; its numerals need an `ocr_map` and about fifty `fixes`, and some sermons print no marker at all, so they need explicit divisions. Measure the gaps with `number` before drafting fixes.
