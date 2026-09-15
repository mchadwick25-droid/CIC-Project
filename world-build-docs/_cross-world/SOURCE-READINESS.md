# Source Readiness Dossier — the pre-flight gate

**Standing rule, added 2026-09-15 (Mark's ruling):** no world's Doc_02 (Source
Ecology) may begin drafting until a Source Readiness Dossier exists for that
world at `world-build-docs/_cross-world/dossiers/<world-slug>_Source_Readiness_Dossier.md`.
If none exists when a build thread reaches Doc_02, it **stops** and asks for
one rather than starting Doc_02 from a cold search.

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
source-research session, run the same way against a new world's
time-window/region as the proactive-acquisition work `CLAUDE.md`'s "Scaling
the build" section already describes). It is not written by the build thread
itself — the whole point is that it reflects the corpus-wide view a
single-world build thread doesn't have. A build thread that reaches Doc_02
with no dossier on file should ask for one rather than write its own
narrower substitute.

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

## What a build thread does with one

Read it before starting Doc_02. It is a starting inventory, not a
substitute for Doc_02's own analytical work — Source Ecology still does the
ecology reasoning (author gravity, screen risk, per-world source
architecture) that a dossier doesn't attempt. Cite it as the dossier's own
findings get folded into the Source Registry, the same way any other
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
