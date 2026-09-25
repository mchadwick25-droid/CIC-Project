# Open Gaps Tracking — The Old Believers (obel)

Append-only, numbered. A merged entry's number never changes;
cross-references cite subject + date, not a bare number, per `CLAUDE.md`.

---

**1. (2026-09-25, Doc_01 §6, Step 0 §4) Strand determination
(popovtsy/bezpopovtsy) not decided.** The movement's internal division
between priestly and priestless communities is real and consequential but
not resolved at Steps 0-2. Carried forward to the world-build thread
(Step 3 onward per V1.8) to decide once Doc_03-Doc_09's own research has
built out the evidentiary base for each side. Does not touch the Creed
(Doc_01 §9) but does raise doctrine-adjacent ecclesiological questions
(whether a valid priesthood can be had at all) that a future document
should not treat as settled by this world's own ritual-schism floor claim.

**2. (2026-09-25, Doc_01 §2.1) The 1666-1667 Moscow council's own
proceedings are not independently verified against a primary source.**
This world's current library (Avvakum's autobiography, both languages)
narrates his own life, not the council's own institutional proceedings.
A real acquisition gap, not yet closed — see the Source Readiness
Dossier §4.

**3. (2026-09-25, Doc_01 §2.3) Self-immolation death-toll figures are
Contested, not independently verified.** The census's own sourcing note
states state reports, Old Believer martyrologies, and hostile accounts
"agree on the fact and disagree on the numbers." This world's current
library does not contain a primary account of any specific incident
(Paleostrovsky Monastery, 1687, or otherwise). Any future document citing
a specific death toll must tag it Contested and cite its actual source,
not treat any one figure as settled.

**4. (2026-09-25, Doc_02) Real, unclosed acquisition leads: the
Solovetsky petitions (esp. the Fifth Petition, 1667), the Pomorian
Answers (1723, Semyon Denisov et al.), and Evfrosin's *Otrazitel'noe
pisanie o novoizobretennom puti samoubiistvennykh smertei* (1691).**
None found in a clean, downloadable, full-text form this pass — see the
Source Readiness Dossier §4 ("Checked and closed") for exactly what was
tried and why each remains open, rather than closed as non-existent.

**5. (2026-09-25, Doc_01 §4) English-translation / original-language
opening-passage discrepancy, unresolved.** The vendored 1924 Harrison &
Mirrlees English translation's own narrative opens at "Avvakum, archpriest,
was bidden by the monk Epiphanius... to write down my life" (p. 32). The
vendored original-language (Wikisource) text opens instead with Avvakum's
own rhetorical declaration about plain speech and philosophical verses,
which does not appear at the equivalent point in the English translation
as vendored. This document does not know whether the English translators
abridged, relocated, or otherwise handled this passage differently, and
does not resolve it by assumption. A future document (most likely Doc_02
or Doc_03) should either locate the missing passage elsewhere in the
English text, or record its absence as a documented translation choice,
rather than silently treat the two vendored texts as page-for-page
equivalent.

**6. (2026-09-25, Doc_02) The original-language file's own transcription
chain is not independently verified hop-by-hop.** The vendored
`avvakum_zhitie-protopopa-avvakuma-orv_wikisource-transcription-nd.txt`
descends, by its own Wikisource page's own citation, from az.lib.ru
(Maksim Moshkov's library), whose own source (a specific dated critical
edition) is not stated on the page and was not independently checked —
az.lib.ru itself was unreachable from this session (network egress
allowlist). This is an **honest_limit**: the text is vendored and usable
as a second witness, but its quotability flag is second-witness-only, not
verbatim-ready, until a future session either reaches az.lib.ru directly
or locates the specific critical edition (likely a Soviet-era Academy of
Sciences "Pamyatniki literatury Drevney Rusi" volume, or the Robinson
1963 edition — not confirmed) and checks this transcription against it.

**7. (2026-09-25, Doc_02) `reference/method/CiC_Record_Native_World_
Build_Process_V1.8.md` is not yet merged to `main`.** This world's build
was instructed to follow V1.8 as authoritative, but as of this pass, only
V1.5 exists on this worktree's checked-out branch (`git log --all` shows
V1.8's own commits — `33c0c4f3`, `f85b8080`, `e2ca4dc3`, `a6d4d639` —
exist in the repository's history but are not ancestors of `main`/this
branch's own HEAD, i.e. they sit in one or more still-open, unmerged pull
requests, referenced in that history as `#591`/`#594`/`#595`). This
thread read V1.8's actual content directly via `git show` against the
commit that carries it, rather than work from V1.5 or from memory, and
followed it as instructed — but this is flagged here plainly rather than
silently assumed resolved, since a future thread reading this world's
build from a fresh `main` checkout will not find V1.8 in its own working
tree until those PRs merge. Not treated as a methodology-change
escalation (the content itself was available and followed; this is a
housekeeping/merge-state gap, not a disputed process question) but
worth Mark's attention so the merge actually happens.

**8. (2026-09-25, general) No independent Opus review subagent tool was
available in this session's environment.** The task instructions call for
each draft's review to be run by a freshly spawned subagent on the Opus
model, isolated from the drafting context. This session's tool surface
does not include a same-context "Agent"/"Task" subagent-spawning tool; the
closest available mechanism is spawning a full separate Claude Code
Remote session (`create_session`), which this thread used for each
document's Round 1 review (see each document's own review file for
confirmation of which mechanism was actually used). Flagged here as an
environment/tooling gap, not a methodology dispute — the build-cycle
skill's own review requirement was honored using the best available
mechanism, and this note exists so a later reader does not assume a
same-context Task-tool review happened when it did not.
