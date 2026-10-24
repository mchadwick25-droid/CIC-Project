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

## 2026-10-24 — Borromeo's pastoral voice is co-owned by Borromean Milan and the Tridentine Church

**Ruling, Mark's answer** to three options put to him in the session: (1) co-owned,
(2) Borromean Milan (VI.12) owns it, (3) the Tridentine Church (VI.22) owns it.
He answered "1". The Library recommended option 1.

**Basis.** The Tatian ruling of 2026-09-29 holds that a voice shaping several
worlds of one era is shared and "doesn't have to be just one". That entry limited
itself to Tatian and figures of his shape. This entry is the separate ruling for
Borromeo.

**Changes.** The Tridentine Registry licenses the five Italian Borromeo files
(rows 29 to 33) for the pastoral voice. The Tridentine Doc_02 moves from Cleared
review to Approved to proceed. Borromean Milan keeps the same files as its own,
so nothing changes in that world's placements. The corpus map still shows the five
files as `context` for the Tridentine Church; the request to change them to
`tradition` is Tridentine Open_Gaps OG-23.

**What this does not rule.** It does not rule on the Lives of Borromeo, the Acta,
or any other figure.

## 2026-10-23 — Era III library pass: scope, corrections, and placements left to Mark

**Scope.** The Era III session (branch `library/era-iii-2026-10`) took the
sixteen census worlds of 451-622 that had no Doc_02: Cyrilline Egypt, the
Church of the East under Persia, Armenia after Avarayr, Judean-desert and
Gaza monasticism, early Benedictine Italy, Merovingian Gaul, Irish
monasticism, Aksum, Georgia, Nubia, the Gothic/Vandal/Lombard Homoian
register entry, the Justinianic imperial church, Caucasian Albania, Latin
Africa, Visigothic Iberia, and Britain and Wales. Each has a Source
Readiness Dossier in `dossiers/`, with a build or atlas-only recommendation
in its §6. The recommendations are Mark's to decide; none blocks library
work. Roughly ninety public-domain texts were vendored (plus two renames),
with cross-link rows added to about thirty existing staging files.

**Correction of record: two files vendored 2026-09-25 did not hold what
their names and headers said.** `dorotheus-gaza_doctrinae-instructiones-
grc-lat_migne-pg88.txt` is Patrologia Graeca 87 part 3 (Moschus's Pratum
Spirituale, Sophronius, the end of Procopius of Gaza, Alexander Monachus);
its own running heads show it, and "Dorotheus" occurs seventeen times in
passing. `cyril-scythopolis_vita-sabae-euthymii-grc-lat_cotelier1681.txt`
is Cotelier's *tomus II*, which carries the Vita Euthymii but no Vita Sabae.
Each was renamed to say what it is (`john-moschus_pratum-spirituale-
sophronius-opera-grc-lat_migne-pg87-3.txt` and `cyril-scythopolis_vita-
euthymii-cotelier-monumenta-v2-grc-lat_1681.txt`), with header, registry
note, seed row and staging rows corrected and bodies unchanged. The real PG
88 (Dorotheus, the Barsanuphius and John answers, Climacus, Agathias) is
vendored as its own file. The Vita Sabae stays an open lead: Cotelier's
*tomus III* (archive.org `bub_gb_PLhdE15tQTAC`) exists but its OCR reads the
text as Cyrillic. The original "vita-sabae" and "doctrinae-diversae, whole
file" rows are withdrawn, not edited. This is the "undo and redo" case the
repository's rules ask for, not a patch on the old rows.

**Reader-ready facts.** The design document the brief cites
(`Build/Ministry/Features/Source-Library/Design.md`) is not in the
repository. The session followed the 2026-10-16 Era VII entry above: the
section labelling, credit line and republishing scope go in each registry
note as a `READER:` trailer, with no new schema field. Every file vendored
here is whole-text republishable (public domain by date). Where an edition
has no public-domain English the dossier's §3 records the gap, and nothing
generated was added to the library.

**Rights calls made.** (1) Migne's Patrologia volumes carry a placeholder
host date of 1800; the title leaf was read where it states a year (PL 42,
67, 80, 83, 88, 96) and otherwise the registry note records that the
series was printed 1844-1878. (2) Works published outside the US between
1923 and 1928 (Gasquet 1925, Taylor's Samson 1925, Moberg 1924, Budge's
Ethiopian Synaxarium 1928) are taken as public domain under the rolling
95-year rule, and each header says so. (3) Gutenberg's J. A. Giles
Nennius gives no print year; the translator died in 1884. (4) Items that
need a renewal check (Scott's Civil Law 1932, Loeb Buildings 1940,
McNeill and Gamer 1938, Garvin 1946, Zimmerman 1959) were not vendored.

**Duplicates avoided.** Other threads vendored, while this session ran,
Raabe's Peter the Iberian, PO 8, Nau's Dioscorus, the Synodicon Orientale
in French and German, Budge's Ethiopian Synaxarium vols. I-II and the PO
16 Synaxarium. This session removed its own two duplicate vendorings
(Raabe and PO 8) and skipped the rest. One overlap remains by design:
`ethiopian-synaxarium_book-of-saints-ethiopian-church-v2-v4-microform_
budge1928.txt` repeats volume II, because it carries volumes III-IV, which
the other file does not.

**Placements left to Mark (`needs-ruling` or flagged `provisional`).**
Gregory's Dialogues II as tradition for the Benedictine entry as well as
the Gregorian one; Peter the Iberian across Georgia, Judean-desert
monasticism and the West Syriac entry; the duplicate Egyptian ids
(`cyrilline-miaphysite-egyptian-tradition` and this entry); the 410, 420
and 424 Persian synods; Maximus the Confessor and the African councils of
646 between Latin Africa and the Heraclian entry; Sophronius; the Akathist
(date Contested); the Ge'ez Pachomian rules; the Nubian royal letters;
Ruricius of Limoges; Toledo III shared by Iberia and the Homoian entry;
and whether the Homoian register entry is a continuation of, a duplicate
of, or separate from the era-2 Homoian bucket.

**Hygiene defects found in other threads' files and not touched.** The
Dalton Gregory of Tours file's header and bucket locus say Books VI-X but it
holds all ten books. PL 39 is vendored twice (Caesarius and Augustine
copies). `capitulatio-de-partibus-saxoniae_pertz1881.txt` is the whole MGH
Capitularia regum Francorum I, with a preface dated 1883. Two John of
Ephesus OCR pairs and two Audollent files and two Chronica minora I scans
are duplicates. The PO 17, 18 and 19 files bind other works (Basset's
Coptic Synaxarium, Grebaut, an Armenian Synaxarion, Marr's Georgian
Synaxarion) that STRUCTURE.md does not list as their own volumes.

**Leads recorded for a later pass.** The Vita Sabae needs fresh OCR of
Cotelier's tomus III; Evagrius in Greek (Bidez and Parmentier) returned
HTTP 500 and should be retried; Romanos on el.wikisource was rate-limited;
Reeves's 1857 Latin Adamnan returned HTTP 500; Babai's Liber de unione
(Latin volume) and Chabot's 1896 "L'ecole de Nisibe" were not located.

**A fault in this session's own tooling, repaired.** The helper that wrote
registry, seed and staging text wrapped lines at hyphens, which broke world
slugs across lines (`chalcedonian-` then `monasticism`) and, once folded,
produced "chalcedonian- monasticism". The damage was found in review and
repaired in only the regions this session added; the repair is in the same
commit as the dossiers.

---

## 2026-10-23 — Era VII rulings after the two library passes (Mark, six decisions)

Mark took the six decisions the Era VII dossiers had left to him, one at a
time, after PR 1071 merged. Each was put as options with a recommendation;
each answer is recorded here in its own words.

1. **Portfolio.** All 20 build-recommended worlds go into Steps 0 to 2, one
   at a time: the Anabaptists and the Tridentine Church first (they need only
   Doc_02), then the other 18 ranked by the dossiers' sourcing, the clean
   English own-voice worlds first.
2. **Mission-Born Christianities (VI.13).** Split. The entry stays on the
   census as a label assessed per region (A3); Kongo and Japan get their own
   entries and build later; China and New Spain/Andes get entries that stay
   on the atlas until a public-domain convert text clears. The vendored files
   are re-mapped to the region each serves.
3. **The other open-question worlds.** Ethiopia (VI.25) and Armenia (VI.28)
   build later, with Doc_02 stating the thin inside voice as an absence.
   Schwenckfelders (VI.15) and the Family of Love (VI.16) stay atlas entries
   until Mark rules on their floor questions.
4. **Non-build recommendations accepted.** Anti-Trinitarian Currents (VI.14)
   is atlas only. The Church of the East schism of 1552 (VI.30) is folded
   into V.17 as its closing arc; the census marks it within another world.
5. **Rights.** (a) The 1947 Doctrina Christiana facsimile: the renewal check
   came back clear, so the whole text may be republished (pd-us-no-renewal).
   (b) Bossert 1930: kept as vendored; a facsimile reprint adds no copyright
   to the 1930 text. (c) Anspach's 1858 Heavenly Balm: held as a second
   witness until an 1858 scan is vendored.
6. **Placements.** The seven needs-ruling rows are ruled by one principle: a
   text from before a world's window that the world argued from is
   `antecedent` to it (Tyndale for VI.4, Arminius for VI.26, the Marian
   visitation documents for VI.7); a text from after the window is `context`
   here and `tradition` for the later entry (Baxter's Parts Two and Three for
   English Old Dissent, the 1760 pasyon for the 1650 to 1815 Philippine
   entry); Spottiswood is the Kirk's own voice (`tradition`), with the
   bishops question for Doc_01; Ignatius's Exercises stay `context`,
   provisional, beside Teresa.

**What changed in the files.** The staging rows above carry the ruling in
their notes; the registry entries for the Doctrina facsimile and the Anspach
text carry it as an appended note; the census carries the VI.13 split and the
VI.30 fold; the two dossiers carry a ruling line. The corpus map and the
generated ledgers are regenerated.

---

## 2026-10-23 — Era VII second pass on the unvendored leads

**Instruction.** Mark asked for a second pass on the verified leads the Era VII
dossiers had left unvendored (201 seed-queue rows across the 27 worlds).

**What was done.** Six agents worked the worlds in groups. Each re-verified a
lead on its host before downloading, vendored only what filled a gap the
dossier's section 6 had named, paired an original with its public-domain
English where one existed, and left the rest as leads with the reason. The
dossiers carry a "Second pass, October 2026" line and their sections 1, 3, 4
and 6 are revised in place.

**What changed in the recommendations.** Kyiv-Mohyla (VI.21) moves from
open question to build: Mohyla's own hand and the documentary spine are
now in the corpus. The Remonstrants' condition (one more pass before the
movement's own voice counts as secure) is met. Every other recommendation
stands; the open-question worlds (VI.13, VI.15, VI.16, VI.25, VI.28) are
open for the same reasons as before, with the gaps narrowed and recorded.

**Hosts.** Google Books could not be used from this environment (API quota
zero, web search rate-limited, text downloads captcha-blocked); HathiTrust's
catalogue answers but its viewer does not. Two new reachable hosts were found
and used: the Biblioteca Nacional Digital of Portugal (Gouvea's Jornada) and
the Hungarian Academy's REAL-EOD repository (the Transylvanian diet records).
The NYPL renewal data is reachable on the `master` branch under
`data/<year>-1.tsv`; the 1947 Doctrina Christiana facsimile shows no renewal
in the 1974 to 1976 files, and whether that lifts its passages-only limit is
Mark's ruling.

**Corpus size.** The second pass added about 90 files. `cic/texts/` is now
well past the 1 GB planning trigger and approaching the 1.5 GB action point in
`PLAN-texts-store-scaling.md`. Nothing was moved; the plan is Mark's to act
on.

---

## 2026-10-23 — Era VII library pass: scope, corpus size, and placements left to Mark

**What was done.** The 27 Era VII census worlds with no Doc_02 now each have a
dossier, vendored texts with staging and registry entries, and a build or
atlas-only recommendation in the dossier's section 6. The three Era VII worlds
with a Doc_02 (VI.1, VI.2, VI.11) were not touched. Every recommendation is for
Mark; none is a decision.

**Corpus size.** `cic/texts/` crossed the 1 GB planning trigger in
`PLAN-texts-store-scaling.md` during this pass (671 MB at the start, about
1.1 GB at the end). The plan says to re-read it at that point and act at
1.5 GB. Nothing was moved or changed here. Mark decides whether to act now.

**Placements left for Mark.** Contested or unread placements were staged as
`needs-ruling` or `provisional`, never as a confident call. The generated
`NEEDS-RULING.md` lists the `needs-ruling` rows. Each dossier's section 5 lists
its other open questions, among them: which world owns Borromeo's voice
(VI.12 or VI.22), whether the Church of the East schism (VI.30) is part of
V.17, whether Mission-Born Christianities (VI.13) should split into its four
regions, and who holds the Westminster Standards (VI.8 or VI.5).

**Rights calls to re-check.** Bossert 1930 (via a 1971 reprint scan with no
host rights statement), the 1947 Doctrina Christiana facsimile (renewal check
not completed), and the Anspach 1858 Heavenly Balm (OCR of a 2024 re-setting).
Each is flagged in its dossier.

**Method note.** The NYPL renewal data files were unreachable for most years;
every 1931 to 1963 candidate was therefore treated as a lead unless a renewal
check was recorded in its dossier.

---

## 2026-10-16 — Reader-ready facts recorded in the registry `notes` trailer, not a new schema field

**Context.** The Source Library design of record (Mark, 2026-10-14,
`Build/Ministry/Features/Source-Library/Design.md`) makes every vendored
text linkable from its atlas world card. The Era VII library session
(branch `library/era-vii-2026-10`) was asked to make each text it vendors
reader-ready: how the edition labels its sections, the credit line, and
whether the rights allow republishing the whole text or only passages.

**Decision (session's own, within the existing schema).** These three
facts go at the end of the file's `REGISTRY.yaml` `notes` as a fixed
trailer: `READER: sections — ...; credit — "..."; republish — ...`.
No new registry field is added. Reasons: `notes` is the schema's own
free-form field for what a file cannot say about itself; a new field is
a schema change for `texts_registry.py` and the generated README, which
is a methodology change for Mark to rule on, not a library session's call;
and a fixed trailer is machine-readable enough for the Stage 1 build to
lift into its per-file index later. For files already registered, the
trailer is appended to the existing note. Appending is within the
registry's append-only rule; nothing already written is changed.

**What this does not decide.** The segmentation index the design places
beside each file, and any `sections` field in the registry, stay for the
Source Library build to propose. If Mark wants the trailer promoted to a
field, the three facts are already separable by their labels.

---

## 2026-10-23 — Era VI library pass: scope, and the one reader-ready convention

**Instruction.** The project lead (2026-10-16): build the library for every
census world that has not started Step 0 to Doc_02, one era per fresh
session, in auto mode inside that scope. This session is Era VI
(1300–1517).

**Scope as applied.** The census lists 23 Era VI worlds. The Hussite and
Bohemian Brethren world has a Doc_02 under `Build/worlds/hus/` and is out of
scope. The other 22 are in scope. Lollardy and the Devotio Moderna have a
Step 0 and a Doc_01 but no Doc_02, and both already have dossiers, which this
pass completes rather than restarts. Taborite Radicalism and the Fraticelli
carry the census status "Within Another World", and the Adamites carry
"Contested - Evidentiary". Each still gets a dossier, and the dossier says
whether its sources support that status. Build-or-atlas recommendations are
the project lead's decision; the dossiers only recommend.

**Reader-ready facts.** This pass follows the convention in the entry
"Reader-ready facts recorded in the registry `notes` trailer, not a new
schema field": a `READER:` trailer at the end of each registry note, no new
field, and nothing added to the vendored file's own header. The Source
Library design document is not at the path the instruction names, so the
trailer is the only reference.

**Nothing generated.** No translation, rendering or paraphrase written by a
model enters the library. Where a non-English text has no public-domain
English translation, the dossier records the gap.

**Roles on reception rows.** Workers staged a later author's reading of an
Era VI text (Wesley on Tauler, Luther on the Theologia deutsch, Hus on
Wyclif, the Synaxaristes on Palamas) as `transmission`. That role is custody,
not reception, and the corpus-map test requires a transmitted work's own
voice to be assigned elsewhere. Those rows are `context`: the view of a
later reader. The two Theologia deutsch rows on the Lutheran world keep
`transmission`, under the same title as the Rhineland tradition rows, since
Luther's printing is why the text survived in print. The four
`tests_corpus_map.py` checks that already fail on `main` (the fixture bucket
name, bucket reproducibility, two unused author rulings, and two orphan
transmissions from earlier passes) are left as found; this pass adds no new
failure. `gen_matrix.py` fails on `main` on a built world's registry
(`role_label`); that is outside the library and is flagged, not fixed.

**Size.** `cic/texts/` stood at about 1.1 GB when this pass restarted, past
the 1 GB planning trigger in `PLAN-texts-store-scaling.md`. This pass vendors
only what a world's own voice or its hostile record needs, and each
pull request states the size it leaves behind.


---

## 2026-09-30 — Two Source Registry rules adopted into the Template

**Ruling.** The project lead adopted both rules proposed in the entry "Step 0-2 process and gate fixes": one Confidence letter per row, with A given only when the Licensed-For content was read and verified at the source by structure marker; and corpus figures counted by two independent methods with the locale stated. His answer to the choice-box question was "Adopt both (Recommended)". Both are now written into `Build/reference/L3B-World-Build-Methodology/Source_Registry_Template.md` (the Confidence field, and a sixth rule). The Template's scale stays A to E; E marks a source later found unreliable. The proposal paragraph in the earlier entry is superseded by this one and is not edited.

---

## 2026-09-30 — Step 0-2 process and gate fixes

**Instruction.** The project lead ordered: "also apply fixes to the step 0 - 2
build process so we have what we need for future builds." The jes and hus
builds exposed the gaps.

**Gate (engine/m10, tools).** The quote store joins line-end `¬` hyphenation in
the Institutum scans (the mark and one line break) before matching, in the
source and in the quotation. The project-document pool includes plain text of
the `.docx` files in `Build/reference/L1-Foundation` and the current Formation
World Construction Framework (highest version number in its name), so Article 4
and Framework quotations count as project-document quotations; superseded,
draft, proposal, safety-test, tracker and register documents are not in the
pool. A review file may carry a `Cycle reset` header field. The three-round cap
counts from the latest file whose field is earned: it cites, by exact title, an
entry of this log (the ruling "The three-round cap counts from significant new
material") or of a Build/Ministry decision log, and the round before it cleared
review. Without an earned field the count starts at round 1, and a reset that is
not honoured routes the cap finding to the project lead with the reason. Every
file stays on record. `check_live_commentary.py` treats an ISO date in a
`Source_Registry.md` or `<code>_Source_Registry.md` table as schema data only
inside a cell whose column header is `Added` or a discovery or date column.

**Process and templates.** Process V2.0 Section 4 gains the Library-stage
rules and completion checklist (registry entry timing, review-file naming and
filing, quotations, dossier, Registry row rules, Doc_02 checks, manifest,
shared working tree) and Section 12 records the change order with its reason
and the worlds it binds. The handoff items 1 and 12, the review-file header
template and its rules file, and the Launch Prompt V2.0 follow.

**Proposed for the Source Registry Template, awaiting the project lead's
decision.** Two rules were drafted into the process document and taken out
again, because each changes the method for every world and comes from the
Template. They are not in force. Exact wording:

- Confidence calibration: "Each row carries one Confidence letter, A to D. A
  is given only when the Licensed-For content was read and verified at the
  source by structure marker."
- Corpus figures: "Corpus figures are counted by two methods, with the locale
  stated (`C.UTF-8` and `POSIX` count differently)."

The Template's own Confidence scale is A to E and defines A as "Verified this
session against an accessible primary source, translation, or authoritative
reference".

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
