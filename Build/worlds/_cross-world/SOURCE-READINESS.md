# Source Readiness Dossier — the Atlas's own source library

**Standing rule, added 2026-09-15 (Mark's ruling), widened the same day:**
every candidate world on the Atlas gets a Source Readiness Dossier
*independent of whether or when it builds* — sitting in the library at
`Build/worlds/_cross-world/dossiers/<world-slug>_Source_Readiness_Dossier.md`,
ready for whichever build thread eventually needs it. Producing one is not
tied to a build being scheduled; a world can have a dossier years before
anyone drafts its Doc_01. The source-research thread also owns the
world's Step 0, Doc_01 and Doc_02, through review until each is approved
to proceed. The world build starts at Step 3, and only when the handoff
package is complete; it never redoes Steps 0–2 or the library search. If
the package is incomplete, the build thread **stops** and asks for what
is missing. The full rule is in
`Build/reference/method/CiC_Record_Native_World_Build_Process_V1.9.md`, §2.

## Why this exists

Every genuinely new source finding this project has produced — a public-domain
acquisition lead, a cross-link between an already-vendored text and a world
that had never claimed it — came from a dedicated research pass run against
the whole corpus, not from a build thread's own Doc_02 search. Those passes
kept finding the same shape of thing: a text sitting fully vendored and
unread for a world that needed it (Ambrosian Milan's Theodoret Book V, closed
2026-09-13), or a verified public-domain edition nobody had gone looking for
(Jerusalem's Egeria, Antioch/Chrysostom's Palladius, Roman Church 3rd
century's Apostolic Tradition — all closed the same week). Every one of those
worlds could have had that finding *before* its own build started; instead
each was found only because someone thought, after the fact, to ask a
research thread to go check.

That is a process gap, not a research gap: the fleet has one shared corpus
and a research thread that can see all of it, but build threads were
starting Doc_02 from zero anyway, on their own narrower search, because
nothing required the wider pass to happen first. This dossier is what closes
that gap — proactive, not reactive, the same distinction
`DOWNLOAD-QUEUE.md` already draws between its two halves, now applied
*before* a world's construction starts rather than only during it.

## What produces one

A Source Readiness Dossier is written by whichever thread is doing
cross-world source research for the fleet (currently: a dedicated
source-research session, run the same way against a candidate world's
time-window/region as the proactive-acquisition work `CLAUDE.md`'s "Scaling
the build" section already describes). It is not written by the build thread
itself — the whole point is that it reflects the corpus-wide view a
single-world build thread doesn't have. A build thread never writes its own
narrower substitute: it starts at Step 3 from a complete handoff package,
and asks the source-research thread for anything missing.

**Coverage target: every candidate on the Atlas, not just the next three
worlds in line.** Any movement carrying "Possible Future World (on record)"
or "Selected - Not Yet Built" status in `cic-website/data/world-census.json`
is in scope for a dossier now, whether or not a build session exists for it
yet. Work through the backlog in whatever order makes sense (era at a time,
strongest candidates first, whatever a given research pass is already
covering) rather than waiting for a launch announcement to justify writing
one. A world whose own research already happened — because a prior session
checked it for exactly this kind of finding, even before this document
existed — gets its dossier written up from that existing work rather than
re-researched from scratch.

## Required sections

Every dossier answers these, in this order, each one grounded in an actual
file checked — not a general impression:

1. **World identity.** Atlas ID, corpus-map slug, time window, region(s) —
   the exact inputs a corpus-wide search needs.
2. **Already assigned.** Every work `cic/corpus-map/<slug>.yaml` (or its
   `_staging/` sources) currently lists for this world — work, author,
   role, confidence, approximate scale. This is the floor a build thread
   would otherwise have to reconstruct by hand from `cic/texts/`.
3. **Cross-link opportunities.** Texts already vendored elsewhere in the
   corpus that name this world's own figures, region, or controversy but
   aren't yet linked to it — checked the way the Aquileia/Jerome-letters and
   Ambrosian-Milan/Theodoret findings were: read the actual staging file
   content for every plausibly-relevant volume, not just its filename.
   `CORPUS-USE.md`'s own tier method (named-never-opened / same time-place /
   same time-different-region / out-of-window) is the checklist to run.
4. **Verified acquisition leads.** Public-domain editions not yet vendored
   anywhere, each one directly confirmed against its host — exact title,
   translator, year, and an explicit not-in-copyright/public-domain
   determination actually fetched and read, never a title match taken on
   faith and never a guessed archive.org identifier. A lead that hasn't
   cleared that bar goes in the next section instead.
5. **Checked and closed.** Plausible-sounding leads that were run down and
   didn't pan out — no PD translation exists, the only free copy is
   lending-restricted, the text turned out to be scholarship rather than a
   translatable primary source. Recorded so a later pass doesn't spend time
   re-discovering the same dead end (the discipline `download-queue-seed.yaml`
   already keeps for closed rows, applied here before a world exists to have
   its own manifest).
6. **Open cross-world questions.** Anything that touches a sibling world's
   own territory or an unresolved mapping decision — named and left
   unresolved here, the same way this directory's own `NEEDS-RULING.md`
   holds a question rather than deciding it.

## How the dossier is used

The source-research thread accounts for all of it in Doc_02. Doc_02's
Source Registry gives every item in the package a line: every §1 assigned
work, §2 cross-link and §3 acquisition lead is used, deferred with a
reason, or out of scope with a reason (a lead not yet vendored is marked
for acquisition); every §5 open question is named and carried forward,
not decided; every piece of rendered source material is used or set
aside with a reason. The Doc_02 review checks that nothing is missing.
Accounting for every item is not citing every item: a source can be out
of scope for good reason, as long as the reason is written down.

The dossier does not replace Doc_02's own analytical work. Source Ecology
still does the ecology reasoning (author gravity, screen risk, per-world
source architecture) that a dossier doesn't attempt. Cite the dossier as
its findings get folded into the Source Registry, the same way any other
already-established fact gets cited rather than silently re-derived.

If a build thread's own later search finds something the dossier missed,
that's a normal, expected outcome — the dossier lowers the odds of a build
starting blind, it doesn't claim completeness. Report what was missed back
to the source-research thread so the gap closes for the next world too, not
only this one.

## Template

`dossiers/_TEMPLATE_Source_Readiness_Dossier.md` in this same directory —
copy it, don't restructure it per world; the fixed shape is what lets a
build thread find the same information in the same place every time.
