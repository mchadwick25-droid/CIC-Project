# Handover — Library thread for the Church Family Tree, batch 7

Written 2026-11-11 at the end of batch 6. Batch 7 starts in a fresh session. Don't start it in the
batch 6 session.

## The charter and the coordinator

Mark's charter (2026-11-10): "launch a library thread that is patterned after previous threads with
full research, organization and render abilities to find the sources you need, public domain in any
language we can find it." The coordinator is session `session_01JMNsSDbFsmawtDvuAiukNQ`; report to it
with `send_message` after each batch. Read CLAUDE.md first, all of it.

## Where things stand

| batch | PR | what it did |
|---|---|---|
| 1-4 | #1577, #1579, #1581, #1584 | the people gate; the eras 8-9 holds; the earliest named gaps; the religious orders |
| 5 | #1587 | ME-21 (Rabinowitz); the early modern mission gaps |
| 6 | #1588 | 25 files for ten Europe 1650-1815 gaps; the Marsden shelf ruling |

- **The record:** `CFT-Wants.md`, one section per batch. **The decisions:** `Decision-Log.md`.
- **Open-Gaps entries:** 170-172, 193, 198 and 199 in `Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md`.
- **The page for Mark:** https://claude.ai/artifact/RTJ2uXC4rjqKEguvt4UiDP. Its source is not in the repo.
  Read it with the Artifact tool's `read` action, then republish to the same `url`.

## How a batch runs

`HANDOVER-batch4.md` holds the procedure (steps 1-10) and `HANDOVER-batch6.md` the points batches 4-5
added (grep the registry by title words and spelling variants; the shelf rule; check main's census
first; PDF intake; nine header lines, so "add 12"). Batch 6 added these:

- **The shelf rule reads by the date the shelved words were written** (Decision-Log, 2026-11-11). A
  book whose own-voice texts span two entries gets one row per entry, each with its own locus: Marsden
  (1810-1814 and 1815-1837), the Acts of the General Assembly (1638-1650 only), the Holy Trinity
  records (to 1786 only).
- **Split the checks.** Two Opus reviewers took 13 files each (title page with line numbers, OCR
  quality, dates of writing, passages, the end, rights) and wrote reports to their own scratch folders.
  Then re-check every doubtful date yourself.
- **Read the page image when the OCR year is doubtful.** `https://archive.org/download/<id>/page/n<k>.jpg`
  works from this host; crop the imprint line with PIL and read it. It settled Helweg I (1851, not 1831)
  and Milner (1818, not 1816).
- **Never write an office, place or role from memory.** Batch 6 caught seven of these in its own drafts
  (a bishop, a town, a church) before writing. Only what the title page or the host record gives.
- **Write the headers from one spec file** and generate the file, the registry entry, the queue row and
  the staging file from it. Then check that every body after its header is byte for byte the host text.
- **A licence on an upload** (CC BY-NC-ND and the like) that does not say what it covers is held for
  Mark, even when the text is public domain by date.

## Batch 7: the gaps after 1815 — not yet searched

Search first. These are named gaps of Open-Gaps 158 whose tradition's entry ends at or before 1815:

- English Dissent; English Unitarians (the entry ends 1813); the New Church (ends 1815);
- the Old Believers; the Brethren; the Moravians; the Shakers;
- Armenian Catholics and the Mekhitarists; the Melkites after 1911;
- New England Congregationalists; Welsh chapels;
- Korean Catholics after 1886; the Haitian church after 1860; the Inner Mission; the Malagasy churches.

Check main's census first: release 33 and 34 added nineteenth-century entries (Methodism, Baptists,
Quakerism, Unitarianism and Universalism, the Confessional Lutherans, the Victorian Church of England),
and some of these gaps may now have an entry to shelve on.

## What is left after batch 7

1. **Open-Gaps 158:** 39 named gaps were left after batch 6. Batch 8 takes those after 1906, where the
   public-domain window is only 1906-1930.
2. **Open-Gaps 159:** Alexandria, Cyprus, the Polish, Czech-Slovak and Macedonian Orthodox churches; the
   ten Eastern Catholic churches the tree never names.
3. **Open-Gaps 162:** the living marks after 2010. Ask the coordinator whether they are the Library's.
4. **The loci pass:** 707 staging files say "whole".
5. **Still open from earlier batches:**
   - the Schwenkfelder sacrament rules, held for Mark's licence call (batch 6);
   - batch 6's not found: an insider Hutterite print before 1931, the 1762 Schwenkfelder hymnal, the
     Church Law of 1686, Pontoppidan, Kingo, Brorson, Kirk's Biographies;
   - the Hebrew letters of Rabinowitz; a clean al-Duwayhi; a Chinese Catholic's own text; a Puthenkoor
     text of its own; Kongolese texts besides the Paiva Manso letters; the Syriac Orthodox Church
     1300-1915 (Wright's catalogue);
   - batch 2's not-found list (AF-8, ME-4, ME-7, RV-9, AP13, the Molokans, Peking after 1808, the 1860
     Concordat).
