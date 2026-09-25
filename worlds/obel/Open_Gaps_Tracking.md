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
**Correction, 2026-09-25, Round 2 (independent review Finding 11): the
Pomorian Answers' primary authorship is Andrei Denisov, not Semyon
Denisov as this entry's original text names — the misattribution was
this world's own package's error, not the census's; Semyon Denisov and
Trifon Petrov are named participants, not the primary author. Corrected
at Doc_01, Doc_02, the Registry, and the Dossier; this entry's own
original text is left as written above, per the append-only rule, with
this correction appended rather than the text rewritten.**

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
**Correction, 2026-09-25, Round 2 (independent review, Finding 20 and
its own §5): this entry's evidence was independently checked and found
overstated in one respect — this checkout is a shallow (`--depth 50`),
single-branch clone, so a fresh checkout of this branch cannot itself
reproduce `git log --all` surfacing the four commit hashes this entry
names as observed; they were observed in the drafting session's own
environment (which had broader git history available), not necessarily
verifiable from every future checkout of this branch alone. More
seriously: the review reclassified this entry's own disposition.
Building three canonical documents (Doc_01 §6; Doc_02 §3, §5, §9;
this file's own entry 1) against a specification not present in the
checkout makes their compliance with it unauditable by anyone but the
thread that wrote them — a governance/methodology matter (escalation
category 3), not a housekeeping gap, and it should have stopped the
pass before drafting rather than been noted afterward. Doc_01 and
Doc_02 are re-grounded on V1.5 (which IS in this checkout) this
revision; whether V1.8 should govern this build at all, and when it
merges, is escalated to Mark rather than decided by this build thread.**

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
**Correction, 2026-09-25, Round 2 (independent review Finding 22): at
the time Round 1 review ran, this entry's own pointer to "each
document's own review file" named files that did not yet exist — the
review itself caught this as an instance of the exact failure it warns
against ("review content claimed as shown when it wasn't included"),
not a disclosure of it. That has since been corrected: a single combined
review file,
`worlds/obel/obel_Step0_Doc01_Doc02_Review_Round1.md`, now exists and is
the actual Round 1 review artifact for all three documents. The
reviewer also noted that an `Agent` tool was present in its own
environment, which this drafting thread's own environment did not
expose under that name — left as an open, disclosed discrepancy between
the two sessions' tool surfaces, not resolved here.**

**9. (2026-09-25, Doc_02 §3, self-review finding) `row_id`/`voice_of` are
not yet emitted by the real corpus-map tooling for any world — a
fleet-wide gap, not this world's own.** V1.8 §2 explicitly requires
"corpus-map rows with `row_id`, corrected `role` and `voice_of`."
`cic/engine/corpus_map_merge.py`'s own `_KEEP` tuple does not carry
either field, and `cic/corpus-map/fixture-synthetic.yaml`'s own header
confirms this directly: `row_id`, `voice_of`, `locus_ids`, and
`documented_exchange` are named, in-progress schema increments
("CM-1/CM-2/CM-4/CM-8") that "real buckets don't carry yet," proven so
far only against synthetic fixture data by a separate "corpus-map's own
thread." This world's Doc_02 satisfies V1.8's functional intent by
recording own-voice/opponent-voice directly in prose instead (§1.1's
table) — a workaround, not a fix, since the structural requirement
itself cannot be met until that separate thread's migration reaches real
buckets. Not this build thread's own defect to fix, and not escalated
(it is a known, already-disclosed, actively-owned piece of work
elsewhere, not an unresolved tension this pipeline can't close) — flagged
so a future document doesn't assume the gap was specific to `obel`.
**Correction, 2026-09-25, Round 2 (independent review Finding 20):**
this entry's own reasoning cited "V1.8's functional intent" — the same
unreadable specification named at entry 7. The underlying tooling fact
(the fixture-synthetic disclosure) stands independent of which process
document is asked; Doc_02 §3 now states this without leaning on V1.8's
own unverifiable text.

**10. (2026-09-25, Doc_01 §1) Two names in Avvakum's own list of
authorities for the two-fingered sign of the cross are unidentified.**
The vendored file (p. 121, corrected locus below) names, in its own exact
spelling, "Meletina of Antioch" and "the Heart Bishop of Cyrene."
[Original entry's own guesses were wrong — see the 2026-09-25 Round 2
correction immediately below, left in place per the append-only rule
rather than rewritten.]
**Correction, 2026-09-25, Round 2 (independent review Finding 4): this
entry's own guesses were checked against the vendored Russian witness
and found wrong on every point.** "Cyrene" is the faithful reading, not a
corruption — Russian *киринейскаго* plainly means "of Cyrene." The
actual OCR corruption is "Heart," almost certainly a misread of
"Blest"/"Blessed" (Russian *Блаженнаго*). The Russian witness names
"Феодора" (Theodore), not "Феодорит" (Theodoret), as the one figure
carrying both the epithet and the see — and there is no earlier,
separate "Theodoret" anywhere else in this same four-name list for the
English phrase to duplicate, contrary to this entry's own original
guess. The real open question is narrower and better-formed than the
original entry stated: whether the English translators' "Theodoret" for
Russian "Феодора" is their own rendering choice, a transliteration slip,
or reflects a different manuscript reading — and, more substantively,
the identity of the "Феодорит"/"Феодор" whom Old Believers cited as
authority for the two-fingered sign (the pseudepigraphic *Slovo
Feodoritovo*) is itself a live crux in the secondary literature. Both
are registered as `contested_claim` candidates for Doc_02/Doc_03, not
merely thin evidence as this entry originally tagged them
([Inferential-Thin] is corrected to [Contested] at Doc_01 §1).

**11. (2026-09-25, Round 2 revision, independent review Finding 1) The
schism reached the Nicene Creed's own wording, not only ritual practice
— a `contested_claim` candidate, not a settled floor claim.** Round 1
review found that Step 0 §2 and Doc_01 §9's original claim ("no question
of doctrine arises here at all," echoing the census's own `floorNote`)
is contradicted by this world's own vendored primary source: at p. 34,
Avvakum argues that the Nikonian removal of "the True" from the Creed's
own eighth article ("and in the Holy Spirit, the Lord, the True and
Life-giving") empties it of "the essence of God." Both Step 0 and Doc_01
are corrected this revision to state the floor accurately (the movement
clears Article 4's floor test on the Creed's overall shared content, not
on an absolute "no doctrine at all" claim the source itself refutes).
The Creed-wording dispute itself is real, evidenced, and open for a
future `contested_claim` record rather than smoothed over. **Because the
census's own `floorNote` and `statusDescription` carry the same
overstated absolute phrasing, and were cited approvingly at a Frozen
portfolio gate, correcting the census itself is a portfolio-level matter
— escalated to Mark, not resolved by this build thread.**

**12. (2026-09-25, Round 2 revision, independent review Finding 2/3) A
citation to a nonexistent "`cic/texts/INTAKE.md` 2026-09-25 ruling" was
fabricated somewhere upstream of this pass and propagated by this build
thread into six locations** (Doc_01, Doc_02, `cic/corpus-map/the-old-
believers.yaml`, a corpus-map staging file, `cic/texts/REGISTRY.yaml`,
and the Source Readiness Dossier) **before being caught by independent
review.** INTAKE.md contains no 2026-09-25 entry at all; its real,
dated (2026-09-02) rule says the opposite of what was cited — an
original-language text is a second witness only, never itself primary
evidence. This build thread's own original task instructions asserted
this ruling's existence and told this thread to "read that ruling's own
full text before drafting Doc_02" — an instruction this thread should
have treated as something to independently verify by locating the
actual dated text, not as ground truth to cite forward, and did not.
All six locations are corrected this revision to cite INTAKE.md's real,
2026-09-02 rule instead, and the substantive claim that depended on the
fabricated version (Doc_01 §4's use of the Russian opening declaration
as free-standing evidence) is withdrawn rather than reworded. **Where
the fabricated citation actually originated, and whether the underlying
editorial practice (English primary, Russian second-witness for a work
like this one) should become a real, written INTAKE.md rule, is a
governance/methodology question escalated to Mark, not resolved here.**

**13. (2026-09-25, Round 2 revision, independent review Finding 15/17)
The *Zhitie*'s redaction identity is unknown for both vendored
witnesses, and the two witnesses directly contradict each other about
who physically wrote the opening dedication.** The English edition's own
footnote says Epiphanius wrote it; the Russian witness has Avvakum say
he wrote it "by my own sinful hand." This is very likely a redaction
difference (the *Zhitie* survives in several redactions), not a simple
error in either witness, but this world's library does not yet identify
which redaction either file represents. A real bibliographic gap for a
future pass, disclosed at Doc_02 §1.1 and §7 rather than resolved by
preferring either witness.

**14. (2026-09-25, Round 2 revision, independent review Finding 16) The
vendored English edition's own Chronological Table gives Avvakum's
execution as "1681, April" — one year earlier than the correct, widely
attested 14 April 1682 this world's own documents use throughout (from
the census).** This is an error in the vendored edition's own apparatus,
not a claim this world's documents repeat; disclosed at Doc_02 §1.1 as a
caution about this edition's own front/back matter, since a future
thread reading the file directly could otherwise pick it up uncorrected.

**15. (2026-09-25, Round 2 revision, independent review Finding 13) The
vendored Russian-language file's own `orv` (Old East Slavic) language tag
is loose.** The file carries roughly ninety bracketed modern-Russian
editorial glosses interpolated directly into Avvakum's own sentences,
and is in modernized orthography throughout (no final ъ, no ѣ) — an
annotated modern reading edition of a 17th-century text, not an Old East
Slavic diplomatic transcription. Disclosed at Doc_02 §7 and Registry R2.
Not renamed this pass (a rename touches every existing reference to this
file); a future pass should either rename the file to drop the `orv` tag
or determine that a modernized-Russian tag is itself acceptable under
INTAKE.md's own naming convention, and should in any case strip the
bracketed glosses before quoting the file for anything.

**16. (2026-09-25, Round 2 revision, general) Process narration was
found embedded in all three canonical documents (Step 0, Doc_01,
Doc_02) and the Registry, contrary to `CLAUDE.md`'s rule that
`worlds/` holds only what constitutes the finished record.** Independent
review (Finding 29) named roughly a dozen instances, including a full
self-assessment section in Doc_02. Removed this revision; what remains
in each document is a stated fact, a confidence tag, or a disclosed
limit — never commentary about the document's own choices or a defense
of them addressed to a reviewer. That kind of material belongs here and
in the review files, per `CLAUDE.md`'s own exception for this file.
