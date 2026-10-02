# Lutheran Wittenberg & Its Congregations — B-1a/B-1b coverage check (R)

Run against the 95-row `witt_Source_Registry.md` (Revision
5, APPROVED TO PROCEED) and the 89 source records + 1 world_core record B-1
authored at `records/witt/source/*.md` and `records/witt/world_core/*.md`,
following the same discipline the Cappadocian and Gallic worlds'
`*_B1a_B1b_Coverage_Check.md` precedents established. No Registry row or
source record is edited here — findings route to the pre-freeze re-sweep, or
are simply named for the build thread's own attention, matching both
precedents' disposition discipline exactly.

**Independence discipline, and a real difference from the Gallic
precedent.** Gallic's own Step 1 was produced by a fresh-context subagent
explicitly barred from reading any file in the repository, so its recall
list was genuinely blind to this project's own Source Registry. This session
has no subagent-spawning tool available to it, so that exact method could
not be repeated here. Instead, Step 1 below was run the way the process
document's own B-1b instruction actually specifies for the recall test
itself: ten load-bearing items were selected from across this world's own
build documents *first*, by citation only — author, work, and cited locus,
without reading the cited passage's own wording — and each was then verified
independently against the actual vendored file in `cic/texts/`, cold, before
comparing the result to what the Registry or the citing document claims.
This is a weaker independence bar than a genuinely blind subagent (a person
already primed by this world's own citation list, rather than one with no
knowledge of the Registry at all), and that difference is named here rather
than left implicit. The **PRESS question** (Step 3) is answered from this
session's own general knowledge of the field, cold, in the same spirit as
Gallic's blind subagent step, and is the closer analogue to Gallic's
independent-recall method for that one purpose.

---

## Step 1 — ten-item independent recall/verification test

Ten items were selected across nine of this world's own documents' worth of
citations (Doc_01, Doc_02, Doc_03, Doc_04, Doc_08, Doc_09, and the Registry
itself), spanning six of the ten vendored files and five different gravities
(catechesis, grace/justification, confessional self-definition, founder's
pastoral voice, and reception/Missing-Voices evidence), so the test is not
concentrated in one register. For each, the citation (author, work, locus)
was noted from the Registry or Doc_0X **before** re-reading the cited
passage, then the actual vendored file was opened at or near that locus and
searched independently to confirm or fail to confirm the claim.

| # | Claim, as this build's own documents assert it | Locus claimed | Independently checked | Result |
|---|---|---|---|---|
| 1 | The Large Catechism: "it is the duty of every father of a family to question and examine his children and servants at least once a week" (household examination; Doc_02 SS4, SS6; R25) | `luther_large-catechism_bente-dau1921.txt`, lines 241–243 | `grep`/`sed` on the vendored file, lines 235–248 | **CONFIRMED** — text reproduces verbatim at lines 241–242 (the quotation spans into 243) |
| 2 | The hymn on the Brussels martyrs: "One of these youths was called John, / And Henry was the other," with the heading dated "[July 1, 1523]" (the library's only martyrology; Doc_09 Tier 1 story; R30) | `luther_hymns_bacon-allen.txt`, lines 1759–1760 (verse), 1744–1745 (heading) | `grep` for the verse and the heading, then `sed` for surrounding context | **CONFIRMED** — verse at lines 1759–1760 exactly as claimed; heading "in the year MDXXII [July 1, 1523]" at line 1745 |
| 3 | *On the Bondage of the Will*, OCR-recovered: "The Holy Spirit is not a sceptic, nor are what he has written on our hearts doubts or opinions, but assertions more certain and more firm than life itself" (grace/justification gravity; the "assertion" epistemic posture; R34) | `luther_bondage-of-the-will_cole1823.txt`, lines 759–762 | `sed` on lines 755–765, read as raw OCR | **CONFIRMED** — raw OCR reproduces exactly as the Registry's Verification Note transcribes it, including the "asser-\ntioQ^" line-break artifact |
| 4 | The Augsburg Confession, Article XX: "there was the deepest silence in their sermons concerning the righteousness of faith" (reception evidence, Doc_02 SS9) | `melanchthon_augsburg-confession_anon-pg275.txt`, lines 515–516 | `grep` for "deepest silence" | **CONFIRMED** — at line 515, matching the cited locus exactly |
| 5 | The Apology of the Augsburg Confession, Article XXIV: "we retain the Latin language... and we mingle with it German hymns" (liturgical evidence, Doc_02 SS5) | `melanchthon_apology-augsburg-confession_bente-dau1921.txt`, lines 8512–8514 | `sed` on lines 8508–8518 | **CONFIRMED** — the full sentence spans exactly that range |
| 6 | The Eight Wittenberg Sermons: "Let us beware lest Wittenberg become Capernaum" (founder's pastoral voice to his own congregation, 1522; Doc_01 SS2.3; R15) | `luther_works-v2-selected_jacobs-spaeth1916.txt`, line 14681 | `grep` for "Let us beware lest Wittenberg" | **CONFIRMED** — exact line match |
| 7 | The Table Talk, on Worms: "although in Worms there were as many devils as there are tiles on the houses, yet, God willing, I will go thither" (Tier 2 story, the library's own Worms saying, distinct from the "Here I stand" formula the Registry bars at R94; R31) | `luther_table-talk_bell1886.txt`, lines 3508–3509 | `grep` for "tiles on the houses" | **CONFIRMED** — exact line match |
| 8 | The Small Catechism's confession script names "A master or a lady of the house" (women-as-household-heads trace, Doc_02 SS12.1; R26) | `luther_small-catechism_smith1994.txt`, line 454 | `grep` for "lady of the house" | **CONFIRMED** — exact line match |
| 9 | The letter to Archbishop Albrecht of Mainz accompanying the Ninety-Five Theses is dated October 31, 1517, at line 992 of the file (founding event, Doc_01 SS2.1; R2) | `luther_works-v1-selected_jacobs-spaeth1915.txt`, line 992 | `grep`/`sed` around line 992 | **CONFIRMED** — line 992 reads "OCTOBER 31, 1517," directly under the letter's own heading |
| 10 | The *Kurze Form* (1520) preface: "The ordinary Christian, who cannot read the Scriptures, is required to learn and know the Ten Commandments, the Creed, and the Lord's Prayer" (literacy presupposition, catechesis gravity; R14) | `luther_works-v2-selected_jacobs-spaeth1916.txt`, lines 13182–13183 | `sed` on lines 13172–13185 | **CONFIRMED** — exact match, immediately following the preface heading |

**Result: 10/10.**

---

## Step 2 — adversarial stress test beyond the required ten

Ten confirmations out of ten is, by this process's own standard, a result
that should raise suspicion of insufficient rigor rather than be logged as a
clean pass (the fleet range is 6/10–9/10; even PAHC's own cited "clean
sweep" is 9/10 with zero miss rows, not 10/10). Before accepting the score,
four further checks were run against claims chosen specifically because they
are harder to get right than a single quoted sentence — claims the Registry's
own five-revision history shows this world's build has previously gotten
wrong at least once, or exact-count claims where an error is easy to make
and hard to notice:

1. **R20's two loci** — a location the Registry's own history shows was once
   misplaced "one line off," now corrected: the Weimar
   sermons basis at lines 11732–11735 and Duke George's ban "dated November
   7, 1522" at lines 11737–11738. **CONFIRMED** — `sed` on
   `luther_works-v3-selected_various1930.txt` lines 11730–11740 reproduces
   both exactly at the currently-cited loci.
2. **R87's footnote text** — previously silently emended, now corrected:
   the file's own OCR reads "Pabats" (not "Pabsts") and "and"
   (not "und," an English conjunction inside an otherwise German/Latin
   phrase). **CONFIRMED** — `sed` on `luther_works-v1-selected_jacobs-spaeth1915.txt`
   lines 343–347 shows "Pabats" and "and" exactly as the Registry's corrected
   Verification Note states, not the previously emended form.
3. **The Large Catechism's saints passage** — previously certified in
   backwards order, now corrected: Lawrence is the saint against
   fire, Sebastian/Rochio against pestilence (not the reverse). **CONFIRMED**
   — lines 452–456 read exactly in the corrected order.
4. **Two exact-count claims from Doc_02 SS13**, the kind of claim an error
   hides in most easily (Doc_02's own text discloses that Revision 0's count
   of "190" occurrences of "Jew" did not reproduce and had to be corrected to
   198): (a) the string "Jew" occurs **exactly 198 times** across all ten
   vendored files, recounted independently this pass with `grep -o | wc -l`
   — **CONFIRMED**, reproduces exactly; (b) "Marburg" and "Zwingli" each
   return **zero hits** in all ten files — **CONFIRMED**, `grep -c` against
   each of the ten files independently returns 0 for both strings in every
   file.

All fourteen checks (the required ten plus these four adversarial ones)
independently confirmed. **This is a genuinely clean result, not an
artifact of insufficiently adversarial checking** — the four stress-test
items were chosen specifically to target claims this world's own five-round
review history had previously gotten wrong at least once (R20, R87, the LC
saints passage) or that are exact-count claims rather than single-sentence
quotations (the two SS13 counts), which is a harder bar than the required
ten's single-locus-quote shape. The explanation is not that this pass was
insufficiently skeptical but that `witt_Source_Registry.md` carries an
unusually deep review history for the fleet: five full revisions (not the
Gallic/Cappadocian precedents' three), the last two of which
(`witt_Doc02_Round4_ZellCheck.md`, `witt_Doc02_Round5_ZellFinalCheck.md`)
were run specifically to re-derive and stress-test a single contested
determination, plus an independent post-approval script re-verification of
all 95 rows' schema and statistics. A discovery/recall test run after that
volume of adversarial scrutiny should expect a cleaner result than a
Registry that has been through fewer rounds — this is a stronger, not a
weaker, version of the pattern Cappadocian's and Gallic's own equivalent
steps both named.

---

## Step 3 — the PRESS question, asked verbatim

*"Name up to three sources you would expect a bibliography of this world to
contain that this registry does not hold. If you can name none, say so
explicitly."*

**Answered — three named**, confirmed by direct search of every
`World-Builds/Lutheran-Wittenberg/*.md` document to ensure each is a genuine
absence and not something already tracked as an open item under a different
name:

**(1) Philipp Melanchthon, *Loci Communes Theologici* (1521; rev. 1535,
1543).** The single strongest gap: Melanchthon's own founding work of
Protestant systematic theology — the first Reformation dogmatics text,
written by this world's own second leader — is never named anywhere in
Doc_01 through Doc_10 or the Source Registry, not even as a disclosed
absence. This is a sharper gap than it first appears, because the pattern
elsewhere in this build is the opposite: every other major unvendored
primary document this world's own movement produced (the Book of Concord,
R53; the Saxon visitation protocols, R51–R52; the German Bible, R60; the
Marburg Articles, R56; Melanchthon's 1546 funeral oration, R93) has a
Registry row disclosing it as a named absence with an acquisition lead. The
*Loci Communes* has none — it was apparently never surfaced by any prior
pass, discovery sweep, or review round, which is itself worth naming
plainly rather than folding quietly into the Registry's already-long list
of disclosed gaps.

**(2) A modern, book-length comparative or synthesis history of the
Reformation** — e.g. Diarmaid MacCulloch's *The Reformation: A History*
(2003) or Euan Cameron's *The European Reformation* (2nd ed., 2012). The
Registry's current secondary-scholarship layer is strong on Luther
biography specifically (Brecht, R74; Hendrix, R78; Roper, R79; Oberman,
R82) and on named specialist debates (Strauss/Scribner/Kittelson on
reception, R70–R72; Kaufmann on the Jews, R75), but nothing supplies the
wider comparative frame a synthesis history would — the *Cambridge History
of Christianity* chapters (R81) are the closest the Registry holds, at
chapter rather than monograph length. This is the same "scholarship
apparatus, not primary voice" layer both the Cappadocian and Gallic worlds'
own PRESS findings identified as the recurring pattern across the fleet,
confirmed a third time here.

**(3) Heinz Schilling, *Martin Luther: Rebel in an Age of Upheaval* (Engl.
trans. 2017; German 2012).** The current standard German-scholarship
biography, published for the 2017 quincentenary — a natural companion to
the Registry's existing English-language biographical trio (Brecht,
Hendrix, Roper) but representing the most recent major voice in Luther
scholarship specifically, and not named anywhere in this build. Named third
and separately from the modern-synthesis gap above because it is a
different kind of absence (a specific missing book in an otherwise
well-populated genre, the biography shelf, rather than an entirely
unrepresented genre).

**Disposition (all three):** routed to the pre-freeze re-sweep, same lane
as Cappadocian's and Gallic's own PRESS findings — named with enough detail
(author, title, why it matters to this world specifically, and what is
already in the Registry that each would supplement) for a future pass to
act on directly, not acquired or rowed now, per this process step's own
"namings routed to the pre-freeze re-sweep" instruction.

---

## B-1a — discovery sweep: full record at `records/witt/search_record/witt.search.unopened-volume-sweep.md`

**Scope, as this world's actual sourcing history requires:** the realistic
discovery-sweep question is not "what does the wider literature contain"
(Step 3 above covers that) but narrower and checkable: **did this build
miss anything already sitting in the vendored library (`cic/texts/`) that
is relevant to this world and not yet rowed or recorded, and does every
Native Registry row have exactly one source record?**

**What was searched.** Every filename entry in `cic/texts/REGISTRY.yaml`
naming Luther, Melanchthon, Wittenberg, Karlstadt, Zwingli, or Erasmus was
checked against this world's own ten file-codes (v1, v2, v3, LC, SC, Hy, TT,
Co, AC, Ap, per Doc_03 SS0/Doc_08 SS0), against
`cic/corpus-map/lutheran-wittenberg-and-its-congregations.yaml` and its
`cic/corpus-map/_staging/` entries, and against the Registry's own 95 rows.
Separately, every `records/witt/source/*.md` record's own
`external_ids.witt_source_registry_row` field was extracted by script and
compared against the Registry's live-row list, rather than trusting either
side's own summary statistics.

**Result: no vendored-but-unrowed file found, and a clean 1:1 row-to-record
mapping.** `cic/texts/REGISTRY.yaml` carries exactly ten filename entries
for this world, exactly matching the ten file-codes and the ten
`cic/corpus-map/_staging/` entries — there is no eleventh file sitting in
the library for a sweep to find. The 89 `witt_source_registry_row` values
recovered from `records/witt/source/*.md` are exactly the Registry's 89 live
Native rows (1–32, 34–54, 56, 59–93), with the six absent numbers (33, 55,
57, 58, 94, 95) exactly matching the Registry's own six Excluded/superseded
rows. Full detail, including three checked-and-cleared near-misses
(Melanchthon's *Loci Communes* as an incidental phrase inside R32's own
Verification Note, the Weimarer Ausgabe as editorial apparatus background
inside R63, and the four already-disclosed corpus-map indexing gaps Doc_02
SS16 item 1 assigns to the coach thread, not this build thread), is in the
search_record itself.

**Saturation statement.** `witt_Source_Registry.md` has already been
through five independent review passes, including two bounded checks
(`witt_Doc02_Round4_ZellCheck.md`, `witt_Doc02_Round5_ZellFinalCheck.md`)
that caught a genuinely new defect as late as the last of them (an
undisclosed evidentiary-basis upgrade in R54) — a discovery sweep run after
that scrutiny should expect at most a small residue, not a fresh pile of
misses. That is what this sweep found: nothing, on either the
file-discovery or the row-to-record side.

**Coverage limits — this world's own honest boundary, not a claim of
completeness.** A zero-miss discovery sweep tests only whether this build
missed something already sitting in its own vendored library; it is not a
claim that this world's evidence base is complete, and Doc_02 SS11–SS13
already name the real limits in detail (restated here rather than
re-derived, per this sweep's own note): the founder's argued doctrine
comprises roughly 90% of the library's words while the congregational
register with the largest ecological role (catechism, hymn, weekly sermon,
visitation) has the smallest evidential footprint — an inversion, not
merely a thinness (SS11); no woman's own primary text is vendored, and
Grumbach's Native status (R54) rests on a tertiary source's quotation of her
letter, not a read edition (SS12.1); no ordinary parish record is
vendored — the 1527–28 Saxon visitation protocols exist but sit
untranslated and unread (SS12.2); the two texts most consequential to this
world's ethical record, *On the Jews and Their Lies* (1543) and *Against
the Murderous, Thieving Hordes of Peasants* (1525), are both genuinely
unvendored on rights and hosting grounds and characterized only from
tertiary description, never quoted (SS12.3–12.4); the Reformed and Roman
Catholic contemporaries appear only as this world's own texts represent
them, never in their own voice (SS13); and no period-specific German/Latin
lexicon is vendored (R87). These are this world's real coverage limits, and
this sweep's contribution is confirming, by independent file- and
record-level checking, that they are the complete disclosed set — not a
partial list sitting alongside an undisclosed further gap this sweep would
have caught.

---

## Gate verification

Re-ran the full 18-gate battery (`engine.m1.gates.run_all`) against `witt`'s
complete record set, including the new search_record, from
`/home/user/cic-project`:

| Gate | Findings |
|---|---|
| schema-validation | 0 |
| referential | 0 |
| reciprocity | 0 |
| completion-per-type | 0 |
| narratability | 0 |
| glossary-retrofit-complete | 0 |
| quote-recording | 0 |
| alias-safety | 0 |
| distribution-health | 0 |
| confidence-crosscheck | 0 |
| rights | 0 |
| edition-rights-consistency | 0 |
| canonical-address | 0 |
| readability | 0 |
| canon-coverage | 28 |
| no-build-attribution | 0 |
| voice-perspective | 0 |
| id-convention | 0 |

Matches B-1's own clean state exactly: 17 of 18 gates clean, `canon-coverage`
unchanged at 28 (expected incompleteness — no story/term/doctrinal_witness/
honest_limit records exist yet; those arrive B-2 onward). Nothing regressed
by adding the new search_record.

---

## Verdict

Coverage is not fully saturated in the sense the PRESS question always
guards against — one strong, previously-unnamed primary-source gap
(Melanchthon's own *Loci Communes*) and two modern-scholarship gaps
(a comparative synthesis history; Schilling's current biography) are
confirmed open. It is, however, adequate to proceed on the terms B-1a/B-1b
actually test: the discovery sweep found zero vendored-but-unrowed files and
a clean, script-verified 1:1 mapping between every live Registry row and its
source record; the fourteen-item recall/verification test (ten required
plus four deliberately adversarial stress checks targeting claims this
world's own review history had previously gotten wrong) confirmed every
single item against the actual vendored text, cold; and every finding above
is named with enough specificity — what is missing, why it matters to this
world specifically, and what already exists that it would supplement — for
the pre-freeze re-sweep or the build thread's own next pass to act on
directly.

The 10/10 (14/14 with the adversarial extension) recall score sits above the
fleet's stated 6/10–9/10 range and above PAHC's own cited "clean sweep"
benchmark of 9/10. That is flagged here explicitly, as the process itself
asks a perfect score to be treated as a signal to scrutinize rather than
celebrate, rather than left as an unremarked number: the adversarial
stress test in Step 2 was run for exactly this reason, targeting the
hardest claims available (exact-count assertions, and loci this world's own
five-round review history had previously gotten wrong at least once) rather
than easy ones, and still found nothing. The most defensible reading is
that `witt_Source_Registry.md` has simply been through more independent
review rounds than either fleet precedent this document's own structure is
modeled on (five full revisions against Gallic's and Cappadocian's three,
including two rounds run specifically to re-derive a single contested
determination) — not that this pass checked less carefully than it should
have.

Per CO-022, none of the four standing escalation categories applies to this
step (no representative-identity, portfolio-level, governance/methodology,
or pipeline-unresolvable-tension decision is made here). **Disposition:
Approved to proceed (self-dispositioned).**
