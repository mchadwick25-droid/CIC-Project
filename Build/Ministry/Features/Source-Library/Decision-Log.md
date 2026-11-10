# Source Library — Decision Log

Append-only, workstream-local. One entry per ruling made and per PR merged. The
project-level record of the founding decisions is the 2026-10-14 entry in
`Build/Ministry/Technology/CiC_FrontEnd_Decision_Log.md`; this file does not repeat it.

---

## 2026-10-14 — Founding decisions recorded; design of record filed

**Decided (Mark, 2026-10-14).** Seven questions converged one at a time after a
four-stream research pass. Full text in `Design.md` §2 and in the Front-End Decision
Log entry of the same date.

**Filed.** `Design.md`, `Research.md`, this log, and the workstream row in
`Build/Ministry/Features/README.md`. The 160 citation entries whose loci still show
machine apparatus to participants are logged as a known gap in
`Build/Ministry/Operations/Standing/CiC_Cross_System_Analysis_Tracking.md`, not fixed.

**Not done.** No code, no record edits, no package rebuild. The CCEL letter is Mark's, at
the opening of Stage 1.

### Next action

Nothing before the pilot launches. After it launches: Stage 1 for desert, per
`Design.md` §11, opening with Mark's live read of CCEL's copyright page and the letter.

## 2026-11-06 — Change order: the reader lives on the Church Family Tree's domain

**Decided (Mark, 2026-11-06, Church Family Tree convergence).** `Design.md` §7 places the
reader "on the public site under its own directory", which is Church in Conversation's
site. Under the Church Family Tree plan, the Library is the shelf behind both products, and
its public face is the tree. The reader therefore lives on `https://www.churchfamilytree.com`.
A citation in a conversation opens it in the app's existing side panel. Shelves on movement
pages open when their text assignments pass a Library check, whether or not a world is built.

**Why.** Everything citable then lives under one domain. Nothing is built yet, so the change
costs one section of the design and no code.

**Not changed.** The record shape, anchors, gates, rights, hosting on R2 and the staged plan
all stand. Stage 1 still starts after the pilot launches, desert first.

### Next action

When Stage 1 starts, rewrite `Design.md` §7 and §10 (hosting) to the new home. Full record:
`Build/Ministry/Features/Church-Family-Tree/Decision-Log.md`.

## 2026-11-10 — Church Family Tree wants, batch 1: the later-worlds people gate

**Charter (Mark, 2026-11-10).** A Library thread to find the sources the tree needs, public domain
in any language. The wants list is `CFT-Wants.md` in this folder. It is rendered for Mark as an
Artifact.

**Done.** Seven files vendored: Pamphilus's Apology (Lommatzsch 1846, and Migne PG 17), Priscillian
(CSEL 18), Francis (Robinson 1906 and the 1904 Opuscula), Bonaventure (Salter 1904 and Quaracchi
1911). For each, the rights were read on the archive.org record, the title page was read, and the
work was located inside. Truncation was checked two ways: the byte count against the host's listed
size, and the end of the volume read. The Ecthesis was found already held in Mansi X and is now
shelved. Shelf defects from Open-Gaps were fixed where the fix was the Library's own; two
cross-world moves are listed for the coordinator.

**Decided here.** Where a text was in two scans, both are vendored if one scan is garbled where the
other is clean (the Apology: Lommatzsch's end of Book I is garbled, Migne's is clean). The large
Quaracchi Bonaventure volumes (4-6 MB) were located but not vendored, because the English Legenda
and the 1911 Latin opuscula serve the want. Each is a seed row.

**Searches.** Sonnet workers searched in their own scratch directories; the coordinator re-read every
host record, title page, boundary and ending before vendoring. No model was called outside this
conversation. Nothing was paid for.

### Next action

Batch 2, on a fresh branch from main: the eras 8-9 holds and the Brosset chronicle volumes.

## 2026-11-10 — Ruling: Bell Part II and the Pedalion, as carried out

**Decided (Mark, 2026-11-10, relayed by the coordinator).** On the two cross-world moves from
batch 1: "take both recommendations". On Bell Part II, once the gate question came up: "if the
source is consurant of past and they could likcly know it they can point to it". The coordinator
reads this as: if the source is contemporary and the world's people could likely have known it,
the world can point to it.

**How it was carried out.**
- **Bell 1924, Part II.** The first recommendation was to take the row off the `desert` shelf.
  That cannot be done: `engine/m9/confinement.py` (`gate_shelf_row`) requires every vendored
  desert source record to name a row on desert's own shelf. `desert.source.bell-jews-christians-egypt`
  names this row. So the row stays on desert's shelf, now as `context`, which matches the record's
  own `register: etic`. The Melitian community's own-voice row stays `tradition` on
  `melitian-schism`. Under Mark's rule desert may point to it: the papers are contemporary and
  come from the same desert. No desert package went stale (`engine.m2.cli staleness-check`).
- **The Pedalion.** It leaves the 1453-1650 shelf once the census person row for Nikodemos the
  Hagiorite stops pointing at that shelf's row. The people worker moves the pointer to the
  1650-1821 row; the shelf row is removed after that lands on main. Done in batch 2: data release
  32 (#1578) points the census row at the Philokalia rows, so nothing names the 1453-1650 row.

**Flagged, not done.** The desert voice_craft record mentions Bell as "a newly-registered source".
That phrase sits inside a long namesake rationale (five men named Paphnutius) whose other clauses
narrate process the same way. Cutting the one phrase would leave the rest, so the record's own
cleanup goes to its owner (CLAUDE.md: doc hygiene on another thread's content is flagged).

## 2026-11-10 — Church Family Tree wants, batch 2: the eras 8-9 holds

**Done.** Twenty-two files vendored for the eras 8-9 rows held for sources. Whitehouse 1873 was
already held, and a Thrissur row was added to it. The file list, rights and what each fill unblocks
are in `CFT-Wants.md`. Each host record was re-read, the title page read, the wanted passage
located, the byte count matched to the host, and the body confirmed to be the full host text after
the header.

**Decided here.** Where the entry a text serves does not exist yet, the row goes on the nearest
existing entry as `confidence: needs-ruling` (INTAKE §6): the Transylvanian Unitarians on the
anti-Trinitarian entry, Korean Protestants and Holly's Haiti on the missionary-movement entry,
Marsden on the Georgian Church of England. A text is placed on the shelf of its date of writing,
not of its subject: Adoratskii (1887) is on the synodal-century shelf. Ullathorne (1837) was not
vendored, because its only scan is a 1963 facsimile with its own front matter. Lang (1834) was
located but not vendored.

**Corrected before writing.** I had drafted a wrong title for Claret's Apuntes, and places of
printing the title pages do not show for the Historia Bethlehemitica and The Spirit of Missions.
All three were checked against the OCR and corrected. No header carries a date or place the source
does not give.

### Next action

Batch 3: ME-21 (Rabinowitz) by another route, the AP10 Spanish pass, and the first eras of
Open-Gaps 158. Then remove the Pedalion row once the census pointer has moved.

## 2026-11-10 — Church Family Tree wants, batch 3: the earliest named gaps

**Done.** Twenty files vendored for thirteen of Open-Gaps 158's named gaps (the earliest, eras 3-6)
and for AP10 (Hermano Pule). Four gaps are answered by texts already held: Paul of Aleppo for
Antioch and the Arabic Melkites, Dositheus for Jerusalem, and George of Choziba for the Judean
desert. Each host record was re-read and the title page read, and the byte count was matched to
the host. Truncation was checked two ways: the full host text follows each header, and each
volume's end was read where the OCR has one. File by file, with what each unblocks:
`CFT-Wants.md`, batch 3.

**Decided here.** A text that fills a named gap is shelved only where an existing entry covers
its date of writing. Otherwise it is vendored and listed, and the shelf waits for the new entry.
Putting it on the entry that ends before it would repeat the out-of-window fault found in
Nikodemos. By that rule the two Ferencz rows from batch 2 (on the anti-Trinitarian entry,
1517-1650) were wrong, and they are removed rather than patched. Batch 2's other `needs-ruling`
rows (the Korean Repository, Underwood and Holly on the missionary-movement entry, 1793-1906;
Marsden on the Restoration Church of England, 1660-1815) fall within their entries' windows and
stay.

**ME-21.** The six Google Books items are full view, but Google refuses this host's downloads (the
Books API quota is zero, and the PDF and text routes return its "sorry" page). The ids are
-L8pAAAAYAAJ, DBkHAAAAQAAJ and klEWGBQiW44C (Delitzsch, Documente, 1884-85), u5YtAAAAYAAJ (Neue
Documente, with Rabinowitz's autobiography and sermons, 1887), r5YtAAAAYAAJ (Zwei Predigten, 1885)
and nYotAAAAYAAJ (Bikure ta'anah, the Hebrew letters, 1885). Mark could download them in a browser
and push them to `cic/texts/_intake/`.

### Next action

Batch 4, in a fresh session (handover: `HANDOVER-batch4.md` in this folder).

## 2026-11-10 — Church Family Tree wants, batch 4: the religious orders

**Done.** Twenty-seven files were vendored for eleven named gaps of Open-Gaps 158. These are the
orders (Athos, the Carthusians, Cistercians, canons regular, Hospitallers, Carmelites, Franciscans,
Dominicans, Jesuits and Discalced Carmelites) and the Maronites. Five gaps are also answered in part
by texts already held: Georgirenes, the Port-Royal acts, Kempis's Chronicle of Mount St Agnes, Busch
and the Compiegne Carmelites. For each file:
- the host record was re-read;
- the title page was read;
- the wanted passage was located;
- the byte count was matched to the host's listed size.
For the second truncation check, the body after each header was compared byte for byte with the host
text, ending included. File by file, with shelves and what each unblocks: `CFT-Wants.md`, batch 4.

**Decided here.** The batch 3 rule holds: a text is shelved only where an entry covers its date of
writing. For the Latin orders, that entry is the church-wide one of the text's date (Gregorian, Avignon
to Lateran V, Tridentine, ancien regime, long nineteenth century). Those entries run without a break,
and an order is part of that church. The Compiegne history already sat on one this way. For Athos,
the entry is the Ottoman one. The Maronites have no entry after 1517, so al-Duwayhi is vendored with
no shelf. Data release 33 landed while the batch was open and added the Society of
Jesus 1650-1814 and Chinese Catholicism 1650-1906. The Jesuit texts were moved onto those entries,
since an order's own entry comes before the church-wide one. The release's Maronite entry (1815-1906) does not
cover al-Duwayhi's century. Meyer's typikon of 1394 is `needs-ruling` on the hesychast entry: the dates and place fit,
but the tree has not ruled on whether a monastic rule belongs to the hesychast movement.

**Corrected before writing.** Several host records give a date the title page does not: the Dominican
vols. II and VI say 1898, the title pages say 1899 and 1902; the Reforma tome II says 1644 for 1655;
the Memoires de la Chine say 1780 for 1781; the Premonstratensian statutes say 1628, and the title page
says 1626. Each header gives the title page and names the difference. Rance's name is not on his title
page, so his headers say the attribution is the host record's. Al-Duwayhi's printing has no year on
its title page; the header gives the editor's preface (June 189-, last digit lost). I had drafted a
flag that the Port-Royal acts were out of window. They were written in the 1660s, inside it, so the
flag was dropped.

**Flagged for the census owner.** The Compiegne history (1836) is on the ancien-regime shelf (to
1815), where a census story rests on it. It was not moved; the long-nineteenth-century shelf was added
beside it.

### Next action

Batch 5: the rest of Open-Gaps 158's early modern gaps (the St Thomas Christians 1665-1836, the Kongo
church after 1650, Japanese Christians 1650-1865, Chinese Catholics 1650-1906), then the Protestant gaps.
