# Renderings

Our own English for the Library's texts that are not in modern English. Nothing here edits a vendored
file. Each record points to its file in `cic/texts/` by name and by the file's own lines.

Two kinds of record, one file per vendored text in each folder, named after the text.

## `guides/`: finding guides

A finding guide is our guide to the contents of a text, not a translation. It lets a writer who does not
read the language find where a text treats a subject. It is never quoted.

- One guide per text, in about 20 to 40 sections that follow the text's own chapters or main divisions.
- Each section gives its `lines`, a `label`, what it `covers`, its `notable_footnotes`, a `scan_note`
  where the scanned text is damaged, the `names` the section prints (as printed, each with the first line
  it stands on) and the `quoted_authors`.
- What the author says is reported as the author's claim. Nothing is stated that the section does not
  contain. Where the scan cannot be read, the guide says so.
- Guides are for texts in a language other than English and for older stages of a language.
- A reviewer checks every section against the file before a guide is stored.

## `passages/`: passage renderings

A passage rendering is our modern English of one passage, made when a writer is going to use it.

- `lines` and `original` hold the passage as the vendored file has it, word for word, scanning faults
  included. `scan_faults` lists each fault with what the page image prints. `page_image` names the image.
- `rendering` is the English a card or a profile may carry, labelled as ours. Every clause of the
  original is there, nothing is added, and no sentence runs much past 25 words.
- `second_rendering` was made separately, without sight of the first. Where the two differ in meaning,
  `uncertain` keeps both readings.
- `rendered`, `second_rendered` and `reviewed` say who did each step and when.

The rule for all of this is in `cic/texts/INTAKE.md`. `cic/engine/renderings.py --check` verifies every
record against its file.
