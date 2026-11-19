# Drafting brief: re-score of era 4 and era 5 WANTED Who rows (read-only)

The brief given to the four drafting workers of `Rescore.md`, kept as given; only its scratch-file paths are replaced by the names of the files kept here.

Repo: /home/user/CIC-Project. You change NOTHING in the repo. You write only your one output file (a scratch file; the four drafts are kept here as Draft_G1.md to Draft_G4.md).
Never invent. Every claim you make must rest on a line you opened. No paid or model calls.

## Background
The Who scans marked rows WANTED: they would be WHO (or STORY) if the Library held one named source.
The Library has since vendored many of those sources. Your job: for each of your rows, find out whether the
newly held file(s) really carry what the want asked for, and give a new verdict.

Files to read:
- The scan row itself (file:line given in your row list). Read the whole row: Route, Evidence, ruling cell, Source wanted.
- The rulings block of that scan: era 4 `Build/Ministry/Operations/Audits/2026-11-11_who-scan-era4/Who_Scan_Era4.md` lines 15-21;
  era 5 `Build/Ministry/Operations/Audits/2026-11-11_who-scan-era5/Who_Scan_Era5.md` lines 15-23;
  supplement `Build/Ministry/Operations/Audits/2026-11-12_who-scan-supplement/Who_Scan_Supplement.md` lines 35-52.
- The Library's fill record: `Build/Ministry/Features/Source-Library/CFT-Wants.md` lines 203-330 (era 4 table from 203, era 5 from 256).
- The combined list `Build/Ministry/Operations/Audits/2026-11-12_wanted-sources-combined/Wanted_Sources.md` lines 61-155
  (era 4 and era 5 person rows; many carry a bold **HELD ... (lines N)** pointer) and lines 542-548 (outside witnesses 1-4).
- The filled files in `cic/texts/` (find them with `ls cic/texts | grep <slug>`; some may be in subfolders: use `find cic/texts -name '<name>'`).
  These are big OCR files. Use grep -n (case-insensitive, whitespace-tolerant: OCR often doubles spaces or breaks words)
  and sed -n 'A,Bp' to read the relevant stretch. Do not read whole files.

## The rules (Mark's, as the scans state them)
- WHO: church-shaping, with a body of work or a following, and enough life to tell. Paired rows (two people tied
  together in their sources with similar identity) are one WHO.
- Recorders (chroniclers, hagiographers) are WHO with a thin own-life flagged.
- Women are WHO if they founded, taught or led.
- Rulers (and popes acting through official texts) are STORY unless they have their own voice (a personal confession,
  own letters or works in their own person).
- Founders known only through enemies need two witnesses for the teaching; the life may rest on one.
- Later-retelling rule: a life written centuries later, alone, gives LISTED until an early source is held. Length is not the test.
- Melanchthon rule: where a person's own held work, plus a following or held witnesses, carries a tellable life, the row
  is WHO even if no formal Life is held; thin life flagged.
- WANTED rule: stays WANTED only if a named source, not held, would carry a life (not only writing).
  If the held files now carry the life: WHO / STORY as the rules say. If they carry only writing and no life and
  no tellable life can be put together under the Melanchthon rule, say so (WANTED stays if a named life is still not held; LISTED if nothing could carry a life).
- Outside witnesses (historians outside the church, e.g. Muslim, Jewish, secular chroniclers): WHO with the label
  OUTSIDE WITNESS if their own text is held and some life of them can be told (thin life flagged).
- Mark's rights rulings: Hadewijch may be used ONLY in the 1875 dbnl edition (check whether any Hadewijch file is
  held in cic/texts; if not, she stays WANTED: allowed by Mark but not vendored). Anna Komnene in Greek only
  (the Reifferscheid 1884 Greek is held; do not use any English Alexiad).
- A Life the Library shelved `needs-ruling` (date of writing not given in the volume): say so; check whether the held
  volume itself dates it (an editor's note, a Monitum). If the date is truly unknown, the verdict is a judgment call:
  give the verdict you'd propose and say the later-retelling question is open.
- "Filled in Latin" (a translation of a Slavonic/Greek/Georgian life): a faithful old translation of an early Life
  counts as that Life. Say which.

## What to check for each row
1. What CFT-Wants.md says (filled / held already / not found / none survives / located), and the file names.
2. Open each filled file. Find the stretch that carries (a) the person's life (birth/origin, career, death)
   and/or (b) their own words, as the row needs. Cite file name + line numbers, with a 5-15 word quote or a close
   paraphrase of what those lines say (quote the OCR as it reads). At least two cited stretches for a WHO.
3. Is the life early (near the person's own time) or a later retelling? Use the volume's own statements.
4. New verdict and the rule that gives it, with any flag (thin life, recorder, pair, hostile witnesses, Contested, needs-ruling).

## Output (one markdown file, exact format)
For each row, one block:

### <Person> (<scan file short name>:<line>)
- Old verdict: ...
- Library state: ... (quote CFT-Wants briefly)
- Files and lines:
  - `<file name>` l.A-B: "<quote>" — what it carries (life / own words / date of writing)
  - ...
- New verdict: WHO | STORY | LISTED | WANTED | WHO (OUTSIDE WITNESS) [+ flags]
- Rule and reason: one to three sentences.
- Doubt: anything uncertain, or "none".

End your file with a summary line per row: `Person | old | new`.
When done, reply with only: the output path, and the counts (WHO, STORY, LISTED, WANTED).
