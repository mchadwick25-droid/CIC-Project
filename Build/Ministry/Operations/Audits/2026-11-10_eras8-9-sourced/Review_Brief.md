# P2-G89c review brief (adversarial, Opus)

You review drafted census changes for the Church Family Tree. You did not draft them. Read only;
write only your review file, at the path your task names. No metered model calls. Repo root
`/home/user/CIC-Project`.

The G89b review brief binds you:
`Build/Ministry/Operations/Audits/2026-11-10_eras8-9-rulings/Review_Brief.md` (ruling fidelity,
fabrication and support, contested claims, links, living, prose; the output format). Read it first,
then `Drafting_Brief.md` in this folder for what this chunk changes.

Points for this chunk:

- **The test.** Each held item enters only if its vendored source really supports the line or row
  the gate wrote. Judge that yourself from the source. A line that enters on a source that does not
  carry it is substantial. A hold that a source would in fact carry is minor.
- **Quotes.** Re-open every Library quote at its file lines yourself (not only the drafter's
  checker). For raw online texts, re-fetch the URL with `curl` into your own scratch folder and
  search it. Where a Library header says the OCR is a second witness to be checked against the scan,
  try the archive.org page image (`https://archive.org/download/<id>/page/n<N>.jpg` or the item's
  BookReader) for at least the quotes that carry dates or names; say what you could and could not
  check.
- **Renderings.** Each English rendering of a non-English quote: every clause, nothing added, no word
  whose modern sense misleads.
- **Frames.** A date or claim that rests on a biographer's or editor's frame, not the quoted voice,
  must be said to be the frame's, or cut.
- **Frozen rows.** Only the ruled line is added; nothing else in the row changes.
- Run `python3 Build/Ministry/Operations/Audits/2026-11-10_eras8-9-rulings/check_draft.py <Draft.json> <raw dir>`.

Approve only with no blocking and no substantial findings. "Could be stronger" with nothing wrong
is not a finding.
