# Library decision log — rulings that govern the corpus, not one world

Hand-written, append-only, no-rewrite-history — the same discipline
`cic/texts/REGISTRY.yaml`'s own header already states for itself. An entry
records what was ruled, when, why, and what it changed; it is never edited
to match a later ruling. A later ruling gets its own entry and says plainly
what it supersedes.

This is where a rule's *reasoning* lives. The rule itself, stated plainly
with no history in the document, lives in the file it governs (here,
`cic/texts/INTAKE.md`) — the same split this project already draws between
`Ministry/`'s decision logs and the canonical documents they explain.

---

## 2026-09-30 — Step 0-2 process and gate fixes, 2026-09-30

**Instruction.** The project lead ordered: "also apply fixes to the step 0 - 2
build process so we have what we need for future builds." The jes and hus
builds exposed the gaps.

**Gate (engine/m10, tools).** The quote store joins line-end `¬` hyphenation in
the Institutum scans before matching. The project-document pool includes plain
text of the `.docx` files under `Build/reference` (the Constitution and the
Framework), so Article 4 and Framework quotations count as project-document
quotations. A review file may carry a `Cycle reset` header field; the
three-round cap counts from the latest file that carries it (the 2026-09-29
ruling), and every file stays on record. `check_live_commentary.py` treats ISO
dates in table rows of `*Source_Registry*.md` files as schema data.

**Process and templates.** Process V2.0 Section 4 gains the Library-stage
rules and completion checklist (registry entry timing, review-file naming and
filing, quotations, dossier, Registry row rules, Doc_02 checks, manifest,
shared working tree) and Section 12 records the change order. The handoff
items 1 and 12, the review-file header template and the Launch Prompt V2.0
follow.

---

## 2026-09-30 — Foxe vol. III and Van Braght placed to the Hussite world

**Ruling.** The project lead approved the two cross-world placements the hus build requested (Open_Gaps E1, E2) and said the Library should make placements of this kind itself, escalating to him only for a significant problem. Foxe's *Acts and Monuments* vol. III (Hus section, file lines 30742–46807) is placed to `the-hussite-and-bohemian-brethren-movement` as `role: context`, alongside its Lollardy placement. Van Braght's *Martyrs' Mirror* (Hus and Taborite sections, lines 47370–47660) is placed there as `role: context`, `confidence: provisional`, alongside its Anabaptist placement. The hus Registry gains rows for them in the hus thread's next revision; Doc_02 relies on neither yet.

---

## 2026-09-30 — lpc row 229 stays unsplit; the lpc build continues

**Ruling.** The project lead ruled that row 229 (33 Native sermons plus 9
unassessed tractatus, Morin) stays as one row, and that the lpc build
continues. This supersedes the part of the 2026-09-29 entry that listed
row 229 among the rows to split by status; rows 231 and 232 stay split
(rows 245–248). The Round 33 recheck's fixes are in place and the file
passes `reviewfile`.

---

## 2026-09-29 — lpc Registry rulings: row letters, no split letters, Petschenig placements

**Rulings.** The project lead chose, from options with recommendations, in
one session, on the questions the Library put to him after the lpc readiness
sweep. He chose "Raise to A" for row 44; "Raise to B" for row 33; "No split;
narrow the rows" for rows 11 and 14; "Seven authentic works, in lpc and
Donatism" for the eight further Petschenig works; "Re-letter to B; rule
unchanged" for rows 227, 228 and 230; "Split into one row per status" for
rows 231, 232 and 229; and "Accept all four" for the remaining letters
(Petschenig rows at A, TEI and scan rows at B, scholarship rows at C, row 225
at B). He also ruled "retire the CSEL 58 file per the Johnson precedent".

**What each changed.** Row 44 to A on the ground that its narrow Licensed-For
was itself read and verified. Row 33 to B, matching rows 31 and 32. Rows 11
and 14 narrowed with new B rows for the wider claims. Rows 227, 228, 230 to B.
The Petschenig works: Contra litteras Petiliani, Epistula ad catholicos,
Breviculus collationis, Contra partem Donati post gesta, Sermo ad Caesariensis,
Gesta cum Emerito and Contra Gaudentium were added to the `lpc` and
`donatism` shelves as tradition; the Sermo de Rusticiano, which the editor
prints as spurious, stays unassigned. CSEL 58 moved to
`Archive/Retired-Library-Texts/`. Row 229 was not split because it holds one
Native group and unassessed sermons; whether that reading is right is put to him.

**Not changed.** The Registry's Confidence calibration rule text is not
amended; a change to it would be a methodology change that comes from the
Template and applies to every world.

---

## 2026-09-29 — Step 0 of the Greek and Latin Apologists: Approved to proceed

**Disposition, by the Library thread (no escalation category applies).**
Both Step 0 documents are Approved to proceed, for the Step 0 document only.
Approved to proceed unblocks Doc_01 and nothing more. Neither is Frozen, which
only the project lead assigns.

| document | review outcome | substantial revisions after Round 5 | review artifacts | disposition |
|---|---|---|---|---|
| `Build/worlds/grkap/Step0_Movement_Scope_Confirmation.md` (I.35) | Round 5: no substantial revision (earlier text). Round 6: substantial revision required (MODERATE R36-R38, LOW R39-R44). Round 7: no substantial revision required (LOW R56, applied as a wording correction) | 1 | `Build/worlds/grkap/Review-Artifacts/Step0_Round6_Review.md`, `Step0_Round7_Review.md` (identical copies in `latap/Review-Artifacts/`) | Approved to proceed |
| `Build/worlds/latap/Step0_Movement_Scope_Confirmation.md` (I.43) | Round 5: no substantial revision (earlier text). Round 6: substantial revision required (MODERATE R45-R48, LOW R49-R55). Round 7: no substantial revision required (LOW R57, applied to the dossier) | 1 | same files | Approved to proceed |

**Cap count.** Counted from the significant new material, per the ruling
above: the Round 6 fixes were the first substantial revision of each
document; two more would have been allowed.

**Not conditions of the disposition; routed to the project lead** (Round 7,
Escalations): whether the cross-build flags already in
`records/pahc/figure/pahc.figure.justin.md` and
`records/alx/figure/alx.figure.antony.md` reach the voice (the Library found
they do not, from the compiler's code); the census phrases the two documents
list for correction (including that the census says Tertullian's *Apology*
"opens the Latin case", against the approved slate's wording rule); the
Syriac records' two defects ("Eusebius accuses"; a `Documented` tag on an
inferred date); the IJC Lactantius wording.

**Doc_01 obligations carried.** Greek Apologists: §4 items 3 and 4. Latin
Apologists: the wording rules at §4 item 1 (the *Apology* does not "open" the
Latin case; Minucius and Commodian carry Contested dates).

---

## 2026-09-29 — The three-round cap counts from significant new material

**Ruling, Mark's own words**, on how the cic-build-cycle cap of three rounds
of substantial revision applies to a document that cleared review and then
took on new material: "Option 1, count from the new material, significant
new material".

**What this rules.** When a document that has cleared independent review is
later changed by significant new material (new sources, new rulings, a
merged candidate), the count of substantial-revision rounds starts again at
that material. It does not carry forward the rounds that led to the earlier
clearance. Minor edits do not restart the count.

**Applied to.** The Step 0 documents of `greek-apologists-second-century`
and `latin-apologists`: each cleared at Round 5, then took significant new
material (the original-language witnesses, the Tatian ruling, the approved
window slate, and for the Latin Apologists the Tertullian merger). Round 6
is the first review of that material; the Round 6 fixes are the first
substantial revision; Round 7 is the recheck. Two further substantial
revisions would be allowed under this ruling; the build thread stops and
escalates after the third.

**Why it is recorded here.** It is a reading of the cap that the Library
thread had applied before asking. It is a governance clarification and is
Mark's to make; it changes no rule text in the skill.

---

## 2026-09-29 — Correction: the Syriac Tatian record's clause is about the Encratite charge, not Justin's death

**What is corrected.** The entry below (window slate approved) says the
Syriac world's statement that Tatian's *Address* was "written before the
events Eusebius describes" is over-broad because it fails for Justin's
death. That characterization was wrong. Round 6's independent review
(`Build/worlds/grkap/Review-Artifacts/Step0_Round6_Review.md`, R38) checked
the record: in `records/syr/source/syr.source.tatian-address-to-greeks.md`
the clause sits inside the paragraph headed "The Encratite charge, handled
honestly", so "the events Eusebius describes" are the Encratite events of
HE IV.29, and nothing in `records/syr/` speaks of Justin's death. The
evidence supports the clause for that reading: the *Address* precedes
Tatian's break with the Church (Dominant Modern Reconstruction).

**What the Syriac record does get wrong, on the review's reading.** It says
"Eusebius accuses him", where Eusebius reports the charge from Irenaeus
(Adv. haer. I.28.1), the earlier source, and its source record carries
`formation_confidence: Documented` for a dating that is inferred. Neither
record is edited by this entry. The Greek Apologists' Step 0 states these
points without altering the Syriac records.

**Supersedes.** Only that one sentence of the slate entry; the slate itself
is unchanged.

---

## 2026-09-29 — Window slate for the Greek and Latin Apologists approved

**Ruling, Mark's own words**, on the work-by-work slate shown to him: "yes,
approve the slate and proceed".

**Slate approved** (evidence, with citations and confidence tags, is in the
revised Step 0 documents of `greek-apologists-second-century` and
`latin-apologists`; the rule: a work whose plausible date range overlaps its
world's window stays, tagged Contested, with the dispute stated where the
work is used; a work wholly or mostly outside the window that already has a
better home leaves the roster):
- Greek Apologists: stay: Tatian's *Address*, Aristides, Quadratus, Melito,
  Aristo of Pella (in all three entries he already holds), *Diognetus*, the
  pseudo-Justin *Discourse* and *Sole Government*. The pseudo-Justin
  *Hortatory Address* (probably 221-302) is kept as `context`, not the world's
  own voice. The Ambrose *hypomnemata* (3rd century at earliest) leaves the
  roster and stays in Syriac as transmission; its Greek Apologists row is
  `context`, because the corpus map requires a transmitted work's voice to be
  homed somewhere.
- Latin Apologists: stay: Minucius Felix (Contested, 160-192 or 200-250;
  the Roman church entry I.33 makes no claim on him, so nothing moves),
  Commodian (Contested, with the minority 5th-century thesis disclosed),
  Arnobius, Lactantius, Tertullian's Montanist-era works, Perpetua. Doc_01
  must not say Tertullian's 197 *Apology* "opens" the Latin case.

**Changed.** Corpus-map staging in `anf01` (the *Hortatory Address* split
into a pahc row and a Greek Apologists `context` row) and `anf08` (the
Ambrose Greek Apologists row set to `context`). The Syriac world's source
record for Tatian's *Address* is not edited; its statement "written before
the events Eusebius describes" is over-broad (it holds for the break with
the Church, not for Justin's death), and that finding is recorded in the
Greek Apologists' Step 0.

---

## 2026-09-29 — Cross-world ownership is recorded in the references, never in a world's own figure record

**Ruling, Mark's own words**, on the Library's proposal to add a cross-build
flag to `syr.figure.tatian.md`: "that shouldnt be something he says, he
talks from his own world perpsective only, it is noted in the references".

**What this rules.** A world's Representative speaks only from its own
world's perspective. Co-ownership of a voice between worlds is recorded in
the references (this log, the Step 0 documents, the corpus map, the source
readiness dossiers), and no cross-world ownership sentence is added to a
world's figure or source record. The Library proposal to add one to the
Syriac world's Tatian record is withdrawn; that record is unchanged.

**Follow-up not ruled.** `records/pahc/figure/pahc.figure.justin.md` and
`records/alx/figure/alx.figure.antony.md` already carry cross-build flags of
the kind this ruling excludes from new records. Whether they reach what a
Representative says has not been checked, and neither record is edited by
this entry. Both belong to their own worlds' threads and are flagged to Mark
here for a decision.

**Supersedes nothing.** The entry above (Tatian co-owned) stands; this entry
changes only where that ownership is written down.

---

## 2026-09-29 — A voice may belong to several worlds of the same era; Tatian is co-owned

**Ruling, Mark's own words**, on being shown three options for Tatian
(co-owned on the Antony model, a declared outside voice, or excluded):
"if a voice influcences three worlds in the same era that is something
they have in common. it doesn't have to be just one."

**Reading recorded here.** The Library reads this as (1) choosing the
co-ownership option for Tatian in the Greek Apologists' Step 0 (§4 item 2),
on the same footing as the Justin ruling, and (2) a general rule: a voice
that shaped several worlds of one era is a shared feature of those worlds
and is not forced into a single owner. It was stated back to Mark in the
session for correction and is not a ruling on anything beyond Tatian and
figures that share Tatian's shape.

**Context.** Tatian's *Address to the Greeks* is load-bearing in the built
Syriac world (`syr.source.tatian-address-to-greeks`), whose figure record
for him is lighter (`corroborating`, `narratable: false`, "boundary-adjacent
... without adopting him as a founding teacher"). The Greek Apologists'
Step 0 had held the question open, binding on Doc_01.

**Changes.** Step 0 of the Greek Apologists records Tatian as co-owned with
Syriac. No record of the built Syriac world is edited by this entry; the
cross-build flag its figure record would carry is a separate step, and is
put to Mark on its own. What still stands open on Tatian: a cited dating
judgment for the *Address* and the Encratite disclosure, both research and
drafting work for Doc_01 and Doc_02.

---

## 2026-09-29 — Cross-world placements for the Ottoman Orthodoxy sources are made now, by the Library

**Ruling, Mark's own words:** "do the cross-world now, i don't think the
build is a rigorous as you are and they may miss it".

**Context.** The 17 sources vendored for
`orthodoxy-under-the-ottomans-parish-millet-and-n` were first assigned only
to that entry, and the cross-world homes were put to Mark as a question
because cross-world placement is an "Always ask" category. He answered that
the Library should place them itself.

**What was placed** (all rows are in `cic/corpus-map/_staging/`; the reasoning
is in each row's own note):
- `the-kyiv-mohyla-orthodox-revival`: Mogila's Confession, in Overbeck's
  English and in Kimmel's Greek and Latin (tradition, assigned).
- `the-union-of-brest-and-ruthenian-greek-catholic-`: the same two Mogila
  rows (context, provisional; the file text was not checked for its treatment
  of the union).
- `the-reformed-cities-zurich-and-geneva`: Lucaris's Confession in three
  editions (context, provisional; whether Lucaris was a Calvinist is disputed)
  and Aymon's edition of Lucaris's letters (context, assigned: the first letter
  is addressed to the Republic of Geneva and the second to Diodati at Geneva,
  verified against the file's table of contents).
- `lutheran-wittenberg-and-its-congregations`: the 1584 Acta, the Tubingen
  theologians' letters (tradition, provisional, since they are Tubingen and
  not Wittenberg theologians) and the Patriarch's answers (context,
  provisional).
- `orthodoxy-under-the-ottomans-1650-1821`: Dositheus and the 1672 Synod in
  English and Greek, Georgirenes, Rycaut, Smith, and the later Greek books
  (Pedalion, Synaxaristes, Euchologion, Horologion, all provisional).
- `the-kollyvades-and-greek-renewal`: Nikodemos's Pedalion and Synaxaristes
  (tradition, provisional; the placement rests on Nikodemos's historical
  identification as a Kollyvade, not on the files' own text).
- `byzantine-church-palaiologan`: Sphrantzes, Cananus, Anagnostes and Doukas
  (context, provisional).

**Not placed.** `russian-church-stoglav-to-nikon`: Mogila's Confession reached
Moscow only after the window's mid-century, and no file text supports the
fit. It waits for that entry's own build.

**Changed.** Two new corpus-map buckets
(`byzantine-church-palaiologan`, `orthodoxy-under-the-ottomans-1650-1821`)
and added rows in six existing ones. Nothing in any built world's records or
package: the corpus map is outside the compile path.

---

## 2026-09-29 — Non-Western worlds may proceed on an honestly lopsided ecology, Ottoman Orthodoxy first; a protected English translation points to a public-domain original

**Ruling, Mark's own words, two messages in one session.** On the source
search: "remember to look for other language sources that are public
domain, so if there is an english translation version that is protected
that will most certanly come from another language source we can access".
On whether a non-Western candidate may go forward when its public-domain
ecology is strong in some genres and thin in others: "yes, allow it for
Ottoman Orthodoxy first".

**Context.** A four-candidate probe of non-Western entries in eras 6 and 7
(`ethiopian-christianity-gragn-to-fasilides`, the St. Thomas Christians
under Portuguese pressure, `orthodoxy-under-the-ottomans-parish-millet-and-n`,
`hesychasm-and-the-palamite-synthesis`) found none READY. All four were THIN
BUT VIABLE, with strong chronicles and outside witnesses and weak inside
doctrine and prayer. Mark's test for the probe was that the ecology must be
broad enough to build a full world from.

**What this rules.**
- Where an in-copyright English translation exists, the source search looks
  for the public-domain original-language edition behind it (Greek, Latin,
  Ge'ez, Church Slavonic, Malayalam, Portuguese, Italian and the rest), and
  for a clean text of it. A clean original is primary under the 2026-09-25
  ruling below, and the English is rendered from it. A garbled scan stays a
  second witness.
- `orthodoxy-under-the-ottomans-parish-millet-and-n` (VI.17) may proceed
  first, on a lopsided ecology. Each missing genre is recorded as an absence
  in the world's own gap tracking, and a Representative never fills it.

**What this does not rule.** The other three candidates are not approved;
they wait for more acquisition. Two related questions were put to Mark and
are still open: whether a public-domain scholarly translation (Conti Rossini's
French and Latin versions of Ge'ez chronicles) may stand in for a garbled
original or is a cross-check only, and whether the Beta Masaheft
Galawdewos file (CC BY-SA 4.0, based on a 2016 critical edition) may be
vendored. This entry does not answer either.

**Changed.** Nothing in `cic/texts/INTAKE.md`'s rules; its 2026-09-25 text
already covers original-language primary evidence. The Ottoman Orthodoxy
world is a build candidate, subject to its own Step 0 through Doc_02 review.

---

## 2026-09-25 — Non-English originals can be primary evidence; language is not the test

**Ruling, Mark's own words:** "non english sources are treated as primary
sources if they are primary sources to the world. language should not
matter, only the sources credibility and truth."

**Context.** Relayed through a coordinating "managing thread" session as
part of a study into how the library (Steps 0-2) should be set up to best
support a new build process, where the library owns Step 0 through Doc_02
review and a separate build thread starts at Step 3 from the library's own
handoff package. Confirmed directly by Mark in this session before being
acted on — a governance/methodology change of this kind is never executed
on a relayed claim alone, per this project's own standing rule (CLAUDE.md,
"Governance or methodology change" -> "Always ask").

**What it replaces.** `cic/texts/INTAKE.md`'s rule in force from 2026-09-02
(when original-language sourcing began) through today: an original-language
text was a second witness by definition, never primary evidence for a
Representative, because English was named as the project's own evidence
language. That framing predates this ruling and is retired, not merely
revised.

**Reasoning.** The old rule conflated two different questions — is this
text a primary source for the movement it documents, and is it in English —
and let the second answer override the first regardless of the text's own
actual evidentiary standing. A movement's own founding documents, letters,
and institutional records do not stop being primary because they were
never translated, or because the only translation available is itself
in-copyright. What should gate whether a source can be quoted is the two
things that have always mattered for any source in this corpus: whether it
is credible and true to the movement it speaks for, and whether the vendored
text is clean enough to quote from without guessing at what a garbled scan
actually says.

**What changes, concretely:**

1. A clean public-domain original-language text can be primary evidence, on
   the same footing as an English translation would be, when it is primary
   to the world it's assigned to.
2. Quote records hold the original-language text, verified against the
   vendored file - the same verification discipline this project already
   requires for every English quote.
3. The modern English a Representative speaks is an Opus translation of the
   original, independently Opus-checked, and the record states plainly that
   it is rendered from the original rather than drawn from an existing
   English edition.
4. A public-domain English translation, where one exists, becomes a
   cross-check against the Opus rendering - useful corroboration, not a
   precondition for using the original.
5. Scan quality, not language, now decides quotability. A garbled OCR
   scan stays second witness until a clean witness of the same work is
   vendored - this is Mark's OCR ruling "a" (2026-09-25), logged here
   because it's the mechanism that makes point 1 workable rather than a
   license to quote from unreadable text. Systematic, deterministically
   normalizable encoding failures (long ſ, þ, ð) are handled in the quote
   gate itself, not treated as garbling. Per-edition OCR substitution
   patterns (an edition rendering þ as `])`/`]?`, for instance) are
   recorded as `apparatus` mappings in `cic/texts/REGISTRY.yaml`, each one
   verified against page images before it's trusted. No model ever retypes
   a source to work around a bad scan.

**Files flagged, at the time of this ruling, as garbled scans held to
second-witness status under point 5** until a cleaner edition is vendored:
the Ausbund (`ausbund_lancaster1846-deu.txt`), the Hutterite Geschicht-Buch
(`hutterite-brethren_geschichtbuch_wolkan1923-deu.txt`), the 1606 Jesuit
Constitutions (`jesuit-constitutions_constitutiones-societatis-iesu-lat_1606.txt`),
Ribadeneira's 1572 Vita Ignatii Loiolae
(`ribadeneira_vita-ignatii-loiolae-lat_1572.txt`), Nadal's 1595 Adnotationes
(`nadal_adnotationes-et-meditationes-in-evangelia-lat_1595.txt`), and Pole's
1560 Oration (`pole_seditious-oration_wythers1560.txt`). This list is a
snapshot at the ruling's own date, not re-verified on every later read of
this entry - check each file's own current header for its live status.

**What this document does not do.** It does not re-run the primary/second-
witness classification for every already-vendored original-language file in
the corpus - that is a real, separate pass (`cic/corpus-map/`'s own
`_staging/` entries, one file at a time), tracked as follow-up work, not
folded silently into this log entry.

---

## 2026-09-24 — lpc's cross-link into the Petschenig Augustine anti-Donatist edition is a project-lead placement decision, not the dossier's own call

**Ruling.** Four of the six assignments in
`cic/corpus-map/_staging/augustini_scripta-contra-donatistas-pars-i-iii_petschenig1908-1910.yaml`
double-place to `latin-pastoral-congregational-christianity` (lpc) as a
second `tradition` row, alongside their existing `donatism` assignment:
De Baptismo, De Unico Baptismo contra Petilianum, Contra Cresconium, and
Contra Epistulam Parmeniani. Wired in commit `d4512b64` (2026-09-24),
whose own commit message states this cross-link was one the lpc Source
Readiness Dossier flagged and Mark authorized.

**Why this needs its own entry, not just the dossier's.**
`latin-pastoral-congregational-christianity_Source_Readiness_Dossier.md`
§2 identifies the same-work-different-language pairing pattern and the
"not presently reachable from this world's own bucket in any other form"
reasoning for the two English-less works, but the dossier itself states
that whether to actually double-place is "Doc_02's or the project lead's
call, not this dossier's." The double-placement is a cross-world
placement decision - an "Always ask" category - and the record that Mark
was asked and said yes belongs in a decision log, not folded into the
dossier's own reasoning as if the dossier had decided it.

**What this entry does not have.** Mark's authorization is known only
from commit `d4512b64`'s own message ("Mark authorized"); no verbatim
ruling text survives elsewhere. This entry records that the decision was
made and by whom it was made, not a quote that doesn't exist - do not
back-fill one.

**Scope.** Psalmus contra Partem Donati and Contra (Adversus) Fulgentium
Donatistam, from the same source file, are NOT part of this authorization
(not named in the dossier's own §2 reasoning) and stay donatism-only.
