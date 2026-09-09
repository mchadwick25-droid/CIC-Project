# Post-Admission Source Finding — Philostorgius and the *Opus Imperfectum in Matthaeum*

**Status:** DRAFT — awaiting independent adversarial review. Not disposed. Nothing in this document is a decision.
**World:** Imperial and Juridical Christianity (`ijc`)
**Date:** 2026-09-09
**Scope:** Two candidate source acquisitions put to this world by an external read-only discovery pass, tested against this world's own already-cleared record. One question only: do either of them change what `Doc_04_Gravity_Discovery.md` currently classifies as central, in particular Candidate 3 (Orthodoxy-Enforcement Through Imperial Power) and its disclosed Confidence/Gravity Cross-Check divergence?
**Answer, stated up front:** **No.** Neither is structural for Doc_04. Finding #1 is real material that belongs to a different world and does not close the gap it was proposed to close. Finding #2 is a real historical work whose only English translation is in copyright, which places it in exactly the same referenced-only posture this world already assigned to Auxentius. **Doc_04 is not revised by this finding, and no record was added to `records/ijc/`.** Two items are flagged for the project lead in §5.

---

## 0. A stale premise corrected first, because everything else was framed on it

This finding was commissioned on the understanding that this world's build has "phase 1 complete and merged" with "the M3 live admission step blocked awaiting a go-ahead," and with an instruction not to advance that gate. **That premise is stale. The gate is already through and this world is live.**

Verified directly on `main` at `f07eb91`:

- `records/worlds.yaml`, `ijc` entry: `state: admitted`, pinned at `packages/ijc/2026-09-04T18-49-02Z` with a `manifest_hash`.
- `records/WORLDS_REGISTRY_LOG.md` §"Fleet-wide facts": all six original worlds including `ijc` were **admitted 2026-08-28**, Mark in session ("yes i admit all six worlds"), certified by that day's fleet-parity battery (28/28 sealed probes), report at `engine/m3/reports/live-admission-report-fleet-parity-2026-08-28.json`.
- Same section: `render.yaml` has carried `CIC_ENFORCE_ADMISSION: "1"` since Mark's 2026-08-28 flip. Doors are open, fleet-wide.

The text the stale premise almost certainly rests on is `world-build-docs/ijc/BUILD-LOG.md` §Header, which still reads "**Compile (6), admission (7), open (8): intentionally NOT started**." That was true when written (2026-08-22) and was overtaken six days later. The BUILD-LOG is stale in a second, smaller way as well: §1 records "154 records in `records/ijc/`," while the tree now holds 182 files. Both are flagged in §5 as documentation drift, not as defects in the world's content.

**Consequence for how this finding should be read.** The instruction "do not approve the M3 gate on the strength of this finding" cannot be complied with as written, because there is no pending gate to approve or withhold. The underlying concern does not disappear, though — it inverts and sharpens. If either finding *were* structural, participants would already be receiving an incomplete account, and the remedy would be a records change plus recompile and repin on a live world rather than a gate held open. That is precisely why §4 states the compile/CI constraint explicitly rather than adding records on this thread's own judgment. As it happens, neither finding is structural, so nothing about the live world needs to change on this account.

---

## 1. What Doc_02 actually names as thin — checked, not accepted secondhand

The discovery pass characterized this world's `Doc_02_Source_Ecology.md` as naming **"no Homoian self-testimony beyond one untranslated fragment."** Read directly, the document says something adjacent but meaningfully different, and the difference matters for testing both findings.

Doc_02 §7 says (verbatim):

> The one substantial piece of near-primary Homoian *self*-testimony available to this world's own Registry is not itself Nicene-transmitted: Auxentius of Durostorum's letter concerning Ulfila survives embedded within the *Dissertatio Maximini contra Ambrosium* …

Two corrections to the secondhand framing:

1. **"Untranslated" appears nowhere in this repository.** A full-tree grep for `untranslated`, `not translated`, and `no english translation` returns nothing. The word is the discovery pass's own gloss. This is not pedantry: the *actual* recorded reason is narrower and load-bearing. `records/ijc/search_record/ijc.search.auxentius-ulfila-english.md` records the real finding — a public-domain **English** translation does not exist, because the standard modern translation (Heather & Matthews 1991) and the critical Latin/French text (Gryson) are both in copyright. The Latin exists and is edited; what fails is this project's public-domain rights test. That distinction is the whole hinge of finding #2 below.

2. **The named gap is specifically *Homoian* self-testimony**, not non-Nicene self-testimony generally, and Doc_02 §7 itself draws the boundary that makes the distinction operative:

> Homoian theologians deliberately avoided both *homoousios* … and *heteroousios* ("of a different substance," associated with the more radical Anomoian position) as unscriptural, metaphysically overreaching vocabulary, preferring instead to confess the Son as *homoios* …

So this world's own Doc_02 defines Homoian identity partly *by its rejection of the Anomoian position*. Any candidate offered as filling the Homoian gap has to clear that boundary, not straddle it.

### Was the gap knowingly left open, or missed?

**Knowingly left open, and disclosed at three separate layers.** This is not a case of a build discovering its own blind spot after the fact:

- **Search layer.** `ijc.search.auxentius-ulfila-english.md` records the query, `result: not_found`, the editions checked, and an explicit CONSEQUENCE clause: the source is registered as referenced-only "licensing no quotation — and the world's Homoian-recentering obligation is discharged through the formulae Hilary quotes (`ijc.source.hilary-de-synodis`), the historians' reports, and honest confidence-flagging, never through invented Homoian voice."
- **Source layer.** `records/ijc/source/ijc.source.auxentius-letter-ulfila.md` carries `rights_status: "referenced-only; no vendorable public-domain English edition (fails closed for quotation)"` and a body paragraph explaining why the record exists despite licensing nothing quotable.
- **Participant layer.** The `thinness_statement` in `records/worlds.yaml` — text a participant sees at the doorway — reads: "…thinner on ordinary believers' daily lives, women's own words, **and the defeated Homoian side's own voice**."

The gap is disclosed to the participant, in plain words, at the door. That is the discipline working, not failing.

---

## 2. Finding #1 — Philostorgius's *Ecclesiastical History*

### 2.1 The material, verified

- **Vendored file (exact name confirmed):** `cic/texts/philostorgius_ecclesiastical-history_walford1855.txt` — 1,007 lines. Walford's 1855 English translation of Photius's Epitome, all twelve books, plus translator's Biographical Notice, Pearse's 2002 note quoting Quasten, and 241 footnotes. Public domain (Pearse/Tertullian Project), supplied by Mark 2026-08-31.
- **Current assignment:** `cic/corpus-map/_staging/philostorgius_ecclesiastical-history_walford1855.yaml`, merged into `cic/corpus-map/anomoean-eunomian-christianity.yaml` (`role: tradition`) and `cic/corpus-map/cappadocian-nicene-pastoral-monastic-tradition.yaml` (`role: context`). **No `imperial-juridical-christianity` row.** Confirmed by grep across the merged maps.
- **Drawn into a world's records:** yes, but not this one — `records/cappadocian/source/cappadocian.source.photius-epitome-philostorgius.md`. Grep of `records/ijc/` for `philostorg|eunomi|anomoean` returns **zero hits**. So the discovery pass's core factual observation — never considered for this world — **is correct.**

### 2.2 Does it close the named gap? No, and the repository has already ruled on why

The caveat the discovery pass flagged is not a technicality. Tested three ways, it holds:

**(a) This world's own Doc_02 already excludes the conflation.** Per §1 above, Doc_02 §7 defines Homoian theology partly by its deliberate rejection of the Anomoian *heteroousios*. Philostorgius was a follower and admirer of Eunomius — the file's own Quasten note calls the work "a late apology for the extreme Arianism of Eunomius." He is on the far side of the boundary Doc_02 itself draws.

**(b) The project has already made this exact ruling, on record, in the corpus map.** `cic/corpus-map/anomoean-eunomian-christianity.yaml` carries a note stating plainly: *"The Anomoeans/Eunomians are not strictly Homoians."* That entry exists **because** of this distinction — it was added to the census on 2026-08-26, and the note explains why: "canon 1 [of Constantinople 381] names Eunomians and Arians as separate parties." Treating Philostorgius as Homoian self-testimony would reverse a governance ruling this project has already made deliberately.

**(c) Most decisive — the text itself will not support the role.** Reading the actual vendored file rather than reasoning from the label, Philostorgius is not merely *distinct* from the Homoians; he is **hostile to them**, and the imperial coercion he complains of is coercion *by* the Homoian establishment against his own party:

- Book IV.12: at Constantinople in 360, Constantius orders the Western bishops' letter — "That the Son is like to the Father according to the Scriptures," the Homoian formula — subscribed by all present, and "by the artifice of this same Acacius … both all the bishops who were present, and also those who hitherto had professed to believe the Persons to be unlike in substance, added their subscriptions." Philostorgius is describing his own side being made to sign the Homoian creed under imperial pressure.
- Acacius of Caesarea, the Homoian architect, is his villain — "who always had one thing hidden in his bosom and another ready upon his tongue." Photius's own *Bibliotheca* cod. 40 notice, reproduced in the vendored file, independently confirms this: Philostorgius "severely attacks Acacius … for his extreme severity and invincible craftiness."
- Book V.1: Aetius is deposed and banished with his own former partisans subscribing, "some casting entirely away the opinion which they had previously embraced; others, again, playing the part of mere time-servers, and reverencing the will of the emperor as paramount to the truth."

**Verdict on the substitution: it fails, and would be worse than the gap.** Filing Philostorgius as this world's Homoian voice would install, as the defeated Homoians' self-account, a text written by a member of the party the Homoians themselves deposed and coerced — misrepresenting both sides at once. The honest description is a *third* losing position, not the one Doc_02 names.

### 2.3 Does it bear on Doc_04 Candidate 3 anyway? Genuinely — but supplementally, not structurally

This is the question that actually decides the commission, and Philostorgius does better here than in §2.2. Book V.1's "reverencing the will of the emperor as paramount to the truth" is a losing-side verdict on precisely the mechanism Doc_04 Candidate 3 is named for, and IV.10–12 narrates Rimini, Seleucia and Constantinople 360 as imperially-convened, imperially-steered events from outside the Nicene tradition entirely. That is real, apt material.

It is nonetheless not structural, for reasons internal to Doc_04's own text:

- **No test result moves.** Candidate 3 already passes all six (Repetition, Dependency, Formation, Explanatory, Persistence, Interaction). Philostorgius corroborates Repetition, Explanatory and Persistence — including, usefully, the content-reversal that Persistence turns on — but corroboration of a passing test is not reclassification.
- **The Cross-Check divergence is not touched.** Doc_04 states the divergence with precision: the mechanism is Documented, while "the specific *content* of Homoian theology itself … rests more heavily on Hanson's modern reconstruction … than on directly-surviving Homoian self-testimony (Confidence C, Registry row 23)." Philostorgius supplies **narrative**, not Homoian **theological content**. The divergence is about the latter. It would stand, unchanged and correctly flagged, with Philostorgius in the record.
- **Cross-strand status is unaffected.** Candidate 3 is confirmed cross-strand to Strands A and B only. Philostorgius bears on neither strand boundary; nothing in Article 21 terms changes.
- **No other candidate is implicated.** Candidates 1, 2, 4, 5, 6 rest on Roman primacy documents, the alliance's institutional forms, Ambrose's Strand C confrontations, Christological precision, and the sacramental/positional tension. Philostorgius touches none of their evidentiary bases.

**Verdict: supplemental. Doc_04 is not revised.**

### 2.4 The one genuine residue — a corpus-map question, not a Doc_04 question

There is a real, modest observation left over, and it deserves surfacing rather than burying: **by this repository's own established precedent, Philostorgius has a defensible claim to a `role: context` row for `imperial-juridical-christianity`.** The precedent is exact. Athanasius's *Historia Arianorum* carries this note in `cic/corpus-map/homoian-arian-christianity.yaml`:

> Assigned three ways — the author's entry; the homoian entry it describes from outside; and **ijc, because its central question ('what has the emperor to do with the church?') is the ijc world's own problem stated by its sharpest opponent.**

Philostorgius states that same question from a *third* position — neither Nicene nor Homoian — and, unlike Athanasius, from outside the tradition that won. Under the corpus map's own four-way role definition that is `context`, never `tradition`, for this world.

This thread is not making that assignment. Three reasons, all disclosed rather than assumed: (i) it is a cross-world corpus-map decision, and the `cic-build-cycle` skill scopes a build thread's write access to its own world's build folder; (ii) the staging file's header states plainly that the merged maps are generated and that the staging file is the editable artifact, so the change would touch shared generation inputs; (iii) it would only matter downstream if a record were added, and §4 explains why no record was added. **Flagged for the project lead at §5, item 2.**

---

## 3. Finding #2 — the *Opus Imperfectum in Matthaeum*

Put to this thread explicitly as a hypothesis to check, not a holding. Checked. **The attribution substantially holds; the acquisition fails.**

### 3.1 Attribution — holds, with two real caveats that must not be smoothed over

Modern scholarship does judge this a genuinely Arian Latin work transmitted under a false Chrysostom attribution, the misattribution first refuted by Erasmus in 1530. It is a substantial commentary (PG 56:611–946), not a scrap. So far the discovery pass's background knowledge is confirmed against external sources.

Two caveats materially affect its usefulness here:

- **The date is genuinely disputed, and one side of the dispute puts it outside this world's window.** Joop van Banning, senior editor of the in-progress Brepols/CCSL edition, argues for the second or third quarter of the fifth century; Dekkers argued for the mid-sixth. This world's window closes at **451**. On van Banning's dating it is plausibly inside; on Dekkers's it is a century outside. This is unsettled scholarship, and this document does not resolve it.
- **Authorship is unidentified, with competing candidates.** Proposed: an Arian priest in Constantinople named Timothy; Maximinus, the Arian bishop who accompanied the Goths; and Anianus of Celeda — the last judged "attractive" but "problematic" by Cooper. The Maximinus candidacy is a striking connection, since the *Dissertatio Maximini contra Ambrosium* is the very text preserving the Auxentius fragment Doc_02 §7 rests on. It is also only a candidacy, and this document treats it as one.

Its Christology is generally characterized as *mildly* Arian, which further weakens any claim that it would supply the sharply-defined Homoian theological content Doc_04's Cross-Check divergence is about.

### 3.2 Acquisition — fails, on this project's own rights test

- **Latin:** public domain. PG 56:611–946; *Patrologia Graeca* vol. 56 is available on the Internet Archive.
- **English:** the first and only complete English translation is **Kellerman / Oden, *Incomplete Commentary on Matthew (Opus imperfectum)*, InterVarsity Press, Ancient Christian Texts, 2010, 2 vols. — in copyright.**

This is the identical posture already recorded for Auxentius: an edited text exists, the rights test fails on the English translation. Under this world's own established discipline (the CONSEQUENCE clause of `ijc.search.auxentius-ulfila-english.md`), that means referenced-only at most, licensing no quotation.

**One partial route was checked and should be rejected rather than left as an open possibility.** Aquinas's *Catena Aurea* quotes the *Opus Imperfectum* extensively, and Newman's 1841 English translation of the *Catena* is public domain and available on CCEL. That is technically a public-domain English channel to some of this text. It should not be used as Homoian self-testimony: those are excerpts selected by a thirteenth-century Dominican, for scholastic purposes, under the false Chrysostom attribution — the losing side's voice arriving pre-filtered and re-labelled by the winning tradition. That is the *exact* transmission pathology Doc_02 §7 exists to name. Using it here would deepen the problem while appearing to close it.

**Verdict: not acquirable as quotable material. Not structural for Doc_04. No record added.**

---

## 4. Why no record was added to `records/ijc/`, stated as a constraint rather than a preference

Ordinarily the correct artifact for a documented negative result in this project is a `search_record` — this world already holds 24 of them, including two (`ijc.search.auxentius-ulfila-english`, `ijc.search.unopened-volume-sweep`) that do precisely this job. Two such records would be the natural output here.

They were not written, because **`records/ijc/` is no longer a free-write tree.** This world is admitted and pinned. `.github/workflows/ci.yml` runs an `m2-staleness-check` job that "recompile[s] every built/admitted/open world from its stored `records_commit` and check[s] it still produces the package" on record. Adding any record would invalidate the pin at `packages/ijc/2026-09-04T18-49-02Z` and fail CI until a deliberate recompile and repin — which, per `WORLDS_REGISTRY_LOG.md`, is a logged, Mark-in-session event for admitted worlds, not a side effect of a finding thread.

Since neither finding is structural, forcing a recompile of a live world to record two negative results is not obviously worth its own cost. That is a judgment for the project lead, not this thread. **Flagged at §5, item 1**, with both records' content already fully specified in §2 and §3 so they can be written directly if approved.

---

## 5. Flagged for the project lead — nothing here decided by this thread

1. **Two `search_record`s are drafted-in-substance but unwritten, pending a recompile decision.** `ijc.search.philostorgius-homoian-fit` (finding #1: real text, wrong party, correctly assigned elsewhere) and `ijc.search.opus-imperfectum-english` (finding #2: attribution holds, no public-domain English translation, *Catena Aurea* route rejected with reasons). Writing them requires accepting a recompile and repin of an admitted, live world. Your call.

2. **A corpus-map assignment question, cross-world and therefore escalated rather than self-decided.** Whether `philostorgius_ecclesiastical-history_walford1855.yaml` should gain an `imperial-juridical-christianity` row at `role: context`, on the exact precedent of Athanasius's *Historia Arianorum* (§2.4). This thread believes the case is genuinely arguable and has deliberately not made the change.

3. **Documentation drift in `world-build-docs/ijc/BUILD-LOG.md`, noted for correction by whoever owns that file.** Its header still says compile/admission/open are "intentionally NOT started," six days before they happened; §1's "154 records" is now 182 files on disk. This drift is what the commissioning brief for this finding was built on, so it has already cost one session's worth of misframing. Content elsewhere in the BUILD-LOG was not re-audited by this thread.

4. **Not a finding, stated so it is not mistaken for one:** nothing here identifies a defect in the live world. The Homoian-voice gap is real, was known, is disclosed at the participant-facing doorway, and neither candidate source closes it.

---

## 6. Escalation-category self-assessment (per `cic-build-cycle`)

- **Representative identity / name / title:** not touched.
- **Portfolio-level or cross-world:** yes, one — §5 item 2, the corpus-map assignment. Explicitly labelled portfolio-level and escalated, not decided.
- **Governance or methodology:** not touched. This document applies existing discipline; it does not change it.
- **Unresolved tension the pipeline cannot close:** none created. This finding *confirms* the standing Doc_02 §7 and Doc_04 Candidate 3 positions rather than cutting against them. The one live judgment call — whether to spend a recompile on two negative-result records — is escalated at §5 item 1 rather than resolved here.

**Disposition:** none claimed. This document has not been independently reviewed at the time of writing and is not self-scored. It is DRAFT until an independent adversarial review is filed alongside it in `Review-Artifacts/`.
