# Handover: Library era 8, batch 2 (finished 2026-11-16), Thread B

Batch 2 is done on `claude/library-era8-2`: 37 files vendored (5,346,333 words), Open-Gaps 298. The record is
`Search_Log.md` in this folder; the review is `R1_review.md`, `R1_changes.md`, `R2_recheck.md`, `R2_changes.md`.
The coordinator is session_01JMNsSCBTsM2UVaFpDa3BTF; every report goes there.

## How the batch was worked (keep)

- `fetch.py <outdir> <ids file>` fetches each djvu.txt and compares bytes with the host's listed size.
- `mkspec2.py <scratch>` holds every header, registry note and shelf row, and checks about 140 line anchors
  against the host text before it writes `work/spec2.json`. `../2026-11-15_library-era8/intake.py` vendors from
  that spec. Host bytes are kept whole.
- Regenerate, do not patch: to change anything, edit the spec, remove the batch's files, restore `cic/` and the
  seed and queue files from the commit before intake, and run intake and the recipe again.
- `voice_of` is only for non-tradition rows and only for census ids; do not use it for a writer.

## What the review taught

- Read every year on the page image, not only the ones the OCR visibly garbles. Two clean-looking OCR years
  were wrong (Parry "1896" for 1895; Campbell "1906" for 1908), and one title page had no year at all.
- Give a date source only from a line of the file. Edition history from memory (a first edition's year, "printed
  in his lifetime", "the first edition") was caught four times.
- A piece inside a volume takes its own writer's slug, with an `authors_ruled` entry; "by another hand" is an
  anonymous slug.
- Keep shelf and ruling reasons out of row notes; they go in the Decision-Log and Open-Gaps.

## The queue after this batch, with the coordinator's Open-Gaps numbers

1. 299: era 9 batch 2b's "Located, not yet taken" volumes
   (`../2026-11-15_library-era9-b2b/Search_Log.md`). If main shows a number taken at merge time, stop and ask.
2. 300: era 10 batch 2's follow-on list.
3. 301: era 8 batch 3, the groups the era 8 handover lists as not yet searched.
4. Rendering only after Mark has seen a proposal and a sample; the proposal goes to the coordinator first.
