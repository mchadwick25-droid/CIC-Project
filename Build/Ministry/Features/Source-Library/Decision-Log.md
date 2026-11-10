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
