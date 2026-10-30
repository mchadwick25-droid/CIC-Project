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
| `divisions` | rules or divisions | Explicit divisions, below. Use when no pattern can work. An explicit division wins over a rule on the same line. |
| `page_splits` | no | Splits at a printed running head, below. |
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
- `number`: the name of a group that holds the edition's numeral. The checker then reports repeats, backward steps, gaps and unreadable numerals in that series. It is a prompt to look, not a failure. `check` lists every repeat, backward step, gap and unreadable numeral in the series, and a step the curation does not explain fails the check (see `expected_gaps`). A numeral under a `parent` counts again from the start whenever the parent changes.
- `ocr_map`: single characters to replace before reading a numeral, for example `{'l': 'I', '1': 'I', 'Y': 'V'}`. Each entry is a claim about how this scan mangles type, so keep the list short. The map never touches a value that a `fix` sets.
- `fixes`: `line` and `set` of group values, for a heading whose OCR is beyond a map. Without a `quote` the line must match the rule. With a `quote` (text that must appear on that line) the rule applies to that line whether or not the pattern matches it, so a heading with no punctuation needs no looser pattern. The unset groups are empty.
- `context`: conditions on the lines around the match, all of which must hold. `prev_blank` and `next_blank` (true or false) test the neighbouring line; a line that is blank, declared furniture or outside the body counts as blank. `prev_short: {lines: N, words: M}` requires each of the N lines before to be blank or at most M words long. This expresses a gazetteer headword or a heading set off by blank lines.
- `language`: a language code or a list of codes. The rule applies only to lines whose detected language is one of them. Detection uses the file's language codes (from the filename or the curation's `language`) and the line's script, so a rule can take the Latin lines of a Latin and Greek parallel text and leave the Greek.
- `allow_oversize`: a sentence of evidence that this level is the finest the edition prints. It lets divisions over 5,000 words stand.

Template fields: the pattern's groups, `{line}` (the 1-based line), `{next}` (the next non-blank line), `{parent}`. Filters, chained with `|`: `int` (read a roman, arabic or ordinal-word numeral; `int:3` pads to three digits), `slug`, `lower`, `upper`. The first matching rule on a line wins.

### Numerals the `int` filter reads

- Roman numerals up to MMMCMXCIX, upper or lower case, to the longest form (MMMDCCCLXXXVIII, 15 letters). Additive forms such as IIII and XXXX count. Letter strings that are not shaped like a numeral (VX, IIX, MIXLCD) do not read.
- Arabic numbers, with an optional trailing letter (`12a` reads as 12).
- Greek letter numerals with a keraia (`α'`, `ιβ'`).
- Ordinal words from fixed tables: English first to twelfth; Latin primus to decimus (`-us`, `-a`, `-um`); Italian primo to decimo (`-o`, `-a`, `-i`, `-e`); German erste to neunhundertneunundneunzigste, with the endings `-e`, `-er`, `-es`, `-en`, `-em` (Erstes, Achtunddreissigster); French premier, second and deuxième to quatre-vingt-dix-neuvième, and centième (Deuxieme, Vingt-et-unième). Accents and umlauts are optional, so `Deuxieme`, `Funfte`, `fuenfte` and `Achtunddreißigster` all read. A word outside the tables has no value, and the checker reports it as unreadable.

### Explicit divisions

An entry in `divisions` has `start_line`, `locus`, `title` and optional `allow_oversize`, and these optional fields:

- `parent`: a rule id or another division's `id`. The address becomes the parent's current address, a slash, then `locus`. The parent must already have matched.
- `id`: names this entry as a level. Rules and later entries may use it as their `parent`, so chapters inside an explicit letter get `letter3/ch2` without a literal prefix. Entries with the same `id` share one level and must share one `parent`.
- `number` and `series`: the edition's numeral for this division (a number, or a numeral the `int` filter reads). The checker adds it to the numbers read by the rule named in `series`, or to a series called `divisions`, so repeats, backward steps and gaps show across rule-found and explicit divisions together. `series` names a rule that has `number`.
- `takes_context: true`: the division starts at the heading of a waiting `division: false` rule, as a rule-found division does. Without it the division starts at `start_line` and the heading stays waiting for the next rule-found division.

### Page splits

For a stretch with no printed divisions, `page_splits` starts a division at each printed running head:

- `pattern` and `number`: the pattern has a named group holding the page number, and `number` names it.
- `locus`: a template, `p{<number>|int}` by default. `{enclosing}` is the address of the division the head falls in.
- `lines`, `skip_repeat`, `ocr_map`, `flags`: as for rules.
- `only_oversize: true`: split only inside divisions that are over the size limit and have no `allow_oversize`.

The running head may also be declared in `ignore`. It then stays out of passage text and still starts a division. `check` reports the page heads used, the numbers read in the series `page_splits[0]`, and a warning when the split also divides more text that was not oversize than oversize text it fixes. A split that matches no head is a failed check.

### What `check` warns about

Lines beginning `warn` do not change the result. They show what the curation would otherwise hide:

- an `ignore` pattern that declares furniture a line which a rule also matches, so a real heading cannot be silently dropped;
- a `division: false` rule that matches again with an unchanged address (usually a running head: add `skip_repeat` or narrow `lines`);
- words between a waiting context heading and the division it joins, which go to that division;
- a page split that divides more than the oversize it fixes.

### Expected gaps

An edition sometimes skips a number, repeats one or prints sections out of order. Each such step in a numbered series (a rule with `number`, the `divisions` series of explicit entries, or a named `series`) must be listed, with a reason the checker can verify:

```
expected_gaps:
  - series: sermon
    line: 4821
    quote: 'SERMO XXVI'
    reason:
      leaf_missing: {between: [4790, 4821]}
```

`series` is the rule id (or `divisions`). `line` is the line of the reading that shows the step: the first number after a gap, the repeat, or the number that runs backward. `quote` is text that appears on that line, such as the printed heading that shows the edition has no XXV. A step that is not listed fails the check and the file does not reach class `curated`. An entry that matches no step, or whose quote is not on its line, also fails. Page-split series are reported but not held to this rule.

`reason` is required and holds exactly one of these four forms. Free text is not accepted, alone or beside a form. An entry with no reason, or a reason that does not verify, fails the check, and the message names the series and line of the entry.

| Form | Explains | What the checker verifies |
|---|---|---|
| `leaf_missing: {between: [A, B]}` | a gap | `A` and `B` are the lines of the two readings of the series on either side of the gap: `A` is the previous reading, `B` is the entry's `line`. The numerals missing from the gap fall between them. Use it where a leaf, page or section is absent from the edition or from the scan. |
| `counterpart: {line: N}` | a gap, a repeat or a backward step | Line `N` is inside the file, is not the entry's own line, and is a division start or a head the series read. Use it in a parallel-text edition where the head that carries the number is the other language's counterpart at line `N`. |
| `edition_unnumbered: {line: N, quote: '...'}` | a gap | The quote is on line `N`, and `N` lies between the two neighbours. Use it where the edition prints a head at `N` with no numeral. |
| `as_printed: {line: P, quote: '...'}` | a repeat or a backward step | `P` is the previous reading of the series, and the quote is on line `P`. The two quotes (the entry's and this one) show the edition prints the repeated or out-of-order numeral itself. |

A reason of the wrong kind for the step fails: `leaf_missing` and `edition_unnumbered` do not explain a repeat, and `as_printed` does not explain a gap.

For every entry, whatever its form, the checker also scans the lines strictly between the two neighbours for a look-alike heading of the series, including lines a hand-listed rule's `lines` leave out: a line the rule's pattern does not match but whose numeral is a short run of numeral letters, digits and the letters the scan confuses with them (`VIL` for `VII`), or which has a margin number in front of the heading. Furniture lines, apparatus ranges and lines inside a `fixes` entry of the curation are left out, and so is the line an `edition_unnumbered` or `counterpart` reason names. Any other look-alike fails the check and is printed with its line. A printed numeral that is damaged is not a gap: read it with a `fix` that carries a `quote`, or an `ocr_map` entry, and the step goes away.

### Checks on `allow_oversize`

`allow_oversize` says a level is the finest the edition prints. The checker tests it: it scans each such division for lines that look like numbered sub-headings by the segmenter's own marker families (keyword headings such as CAPUT or Caput, bare Roman numerals, numbered titles and paragraphs, section signs; footnote lines such as `1)` and the division's own first line do not count). More than 10 such lines fails the check and prints them. Remove the justification and divide the level, or show that the lines are not headings by changing the rule.

### Lines that are not sub-headings

Some lines the oversize scan flags are not sub-headings of the edition: footnote numbers, running heads with a page number, OCR debris such as a lone `I`, or a list of chapter titles the author quotes. List them by line number so the scan leaves them out of its count:

```
not_subheadings:
  - lines: [21737, [21790, 21802]]
    kind: ocr-debris
    quote: 'I'
```

- `lines`: line numbers or `[first, last]` ranges.
- `kind`: `footnote`, `running-head`, `ocr-debris` or `quoted-list`. Any other kind is an error.
- `quote`: text that appears on the first listed line. There is no pattern form.

An entry fails the check when its quote is not on its first line, or when it lists a line that the scan does not flag (a line outside a division with `allow_oversize`, or one that is not heading-like). The limit of 10 sub-heading lines per division is unchanged and applies to the lines left after the listed ones are removed.

### Hand-listed lines

A rule with `lines` is limited to those ranges. `check` prints a `warn` for every line inside them that looks like the rule's heading but did not match: a margin line number in front of the heading, or a numeral the pattern does not read (Greek letters, a dropped I, OCR damage). The warning gives the count of each kind on one line (`4 numeral in a form the pattern does not read; 3 a margin number comes first`) and lists each line beneath it. A line that a `fix` in the same curation already covers is not listed. Read each one: add a `fix` with a `quote`, an `ocr_map` entry, or widen the pattern.

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
