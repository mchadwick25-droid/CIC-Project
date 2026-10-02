# Step 0 Movement-Scope Confirmations, Apologist Pair — Round 7 Independent Adversarial Review (targeted recheck)

**Reviewed documents (second 2026-09-29 pass, answering Round 6):**
- `Build/worlds/grkap/Step0_Movement_Scope_Confirmation.md` (Atlas I.35) and `Build/worlds/_cross-world/dossiers/greek-apologists-second-century_Source_Readiness_Dossier.md`, as of commit `244a31cc`.
- `Build/worlds/latap/Step0_Movement_Scope_Confirmation.md` (Atlas I.43, absorbing I.17) and `Build/worlds/_cross-world/dossiers/latin-apologists_Source_Readiness_Dossier.md`, as of commit `9381a2f5`.
- The Library decision log entry "2026-09-29 — Correction: the Syriac Tatian record's clause is about the Encratite charge, not Justin's death" (`Build/worlds/_cross-world/LIBRARY-DECISION-LOG.md`, commit `9452a7d7`).

**Prior round:** `Step0_Round6_Review.md` (R36–R55). Both documents were then SUBSTANTIAL REVISION REQUIRED.

**Reviewer:** independent isolated agent. No part in drafting, revising, or in Rounds 1–6.

**Scope.** Targeted recheck at lower effort, per CLAUDE.md: (1) each Round 6 finding against the revised text, re-derived from the sources and not from the documents' own response notes; (2) the diff `d6c3be46..HEAD` for anything new; (3) the corrected Syriac reading against `records/syr/` (read-only); (4) consistency; (5) escalations; (6) invented detail or generic phrasing in the changed passages. Settled Round 1–6 ground is not reopened.

**Output location.** This file only, in `grkap/Review-Artifacts/`. Round 6 was also committed as an identical copy in `latap/Review-Artifacts/` (checked with `cmp`), and latap §6 cites it there. If latap's next revision cites Round 7 by the same relative path, the copy needs to be made by the thread that owns that folder. This review does not make it.

Marking per Constitution Article 31: Simulated review — informational only, not an Article 31 substitute.

---

## Verdicts

- **I.35 (Second-Century Greek Apologists): NO SUBSTANTIAL REVISION REQUIRED.** All nine Round 6 findings are fixed (R36 fixed in substance, with a leftover in §6; see R56). One new LOW finding. Nothing new is wrong, unsupported or misleading.
- **I.43 (Latin Apologists): NO SUBSTANTIAL REVISION REQUIRED.** All eleven Round 6 findings are fixed. I reproduced the word counts to the word by the method the document now writes out. One new LOW finding, in the dossier only.

Neither Tier moves. The two LOW findings are one-line corrections and do not need another review round. Whoever makes the edit can check those lines directly.

---

## Part A — New or remaining findings

### R56. [LOW] grkap §6 still counts §4 item 8 as an open obligation. This is what is left of R36.

**Where.** grkap §6, Status paragraph (line 231): "§4 items 3, 4 and 8 carry disclosure and drafting obligations". Closing paragraph (line 247): "The remaining pre-Doc_01 obligations are in §4 items 3, 4 and 8". Also the change list (line 242): "item 8 is new (shelf items for the Library thread)".

**Evidence.** §4 item 8 now reads "Shelf notes corrected in the corpus map" and records all four corrections as done. The corpus map confirms them (Part D). The document's own Round 6 response (line 245) says item 8 records the corrections "with no item left open". The grkap dossier says the same: "None is open." Three sentences in §6 still describe item 8 as open work for a later thread.

**Fix.** Lines 231 and 247: "§4 items 3 and 4". Line 242: "item 8 is new (the shelf notes the Library thread corrected)".

### R57. [LOW] The latap dossier labels the *Appendix* of poems "his largest work". The label is new in this revision and it is wrong.

**Where.** `latin-apologists_Source_Readiness_Dossier.md`, §1 table, the row "Appendix of poems ascribed to Tertullian …": "32,001 words (his largest work)". The label was added in `9381a2f5`. The previous row read "31,817 words" with no label.

**Evidence.** The same table gives *The Five Books Against Marcion* 187,134 words, also labelled "(his largest work)". Step 0 §3 B1 calls *Against Marcion* "his largest surviving work by a wide margin". The *Appendix* is the sixth-largest item among the 32 by the recount (after *Marcion* 187,134, *Soul* 49,425, *Resurrection* 46,242, *Apology* 38,163 and *Ad Nationes* 34,919). Step 0 and the map also call it pseudonymous verse, so it is not "his" work in the plain sense.

**Fix.** Delete "(his largest work)" from the *Appendix* row.

*Cosmetic, not findings:*
- grkap §2 A2 cites the Syriac paragraph as lines 46–50 in one place (line 42) and 46–52 in two others. The paragraph runs 46–52.
- grkap §4 item 4, Ambrose: the file reads "A memorial[note] a which Ambrose…". The stray "a" is a marker artefact, and dropping it inside the quotation is harmless. It could be shown as "[a]" for strictness.
- The Library log's correction entry quotes the record's heading as "The Encratite charge, handled honestly". The record prints it in capitals. The grkap Step 0 quotes it in capitals, correctly.
- latap dossier §5, "Stale references": the dossier says the census's "opened" wording "appears in six places". Two of the six don't use that word. `longDescription` fixes the order ("Roughly a generation on … Minucius Felix") and the edge reads "opens". Step 0 §4 item 1(a) describes all six accurately. The dossier's list also leaves out the *Against Marcion* "about a hundred and eighty-four thousand words" figure that Step 0 lists. The latap dossier header still gives the corpus-map state as "HEAD `d1140c9f`", which is older than the recount it now reports.
- Zahn 1881 (grkap §2 A2): Round 6 could not find the volume. It is on archive.org as `ForschungenZurGeschichteDesNeutestam1` (Teil I, *Tatian's Diatessaron*). I verified the quotation there (Part E). Citing that id would let the next reader check it without searching.

---

## Part B — Status of R36–R55

| # | Sev. (R6) | Status | Verification (mine, from the sources) |
|---|---|---|---|
| R36 | MOD | **Fixed** (residue R56, LOW) | Parsed `greek-apologists-second-century.yaml`: 39 rows, 17 works, 36 `tradition` / 3 `context` (Ambrose anf08, *Hortatory* anf01, *Hortatory* Otto 1879). Joined all `_staging/*.yaml` rows by title. Four rows name this entry alone: Ambrose `context`, Apollinaris anf08 `tradition`, both *Hortatory* `context` rows. PAHC 16 of 17, Syriac 2 of 17. B1, B3, dossier §1 and the dossier "shelf notes … None is open" all match. The "still `role: tradition`" sentence is gone. §6 leftovers: R56. |
| R37 | MOD | **Fixed** | `NEEDS-RULING.md` line 24 reads exactly "The entry's own record states the objection against it — that apologetic is a genre rather than a community — rather than hiding it." The census I.35 `why`/`sourcing`/`relationsSummary`/`legacy` carry no genre-vs-community objection, so "The census entry no longer carries the objection" is true. "verified verbatim" is gone. |
| R38 | MOD | **Fixed** | See Part C. |
| R39 | LOW | **Fixed** | The ruling paragraph (line 169) now reads "Under that ruling a cross-build flag was added … Whether such a flag may stay is an open decision for Mark (below), and this paragraph does not endorse it", and cites the Hub log 2026-09-26 as the only written record. That matches the log's "Follow-up not ruled". |
| R40 | LOW | **Fixed** | The log now has six 2026-09-29 entries. Four bear on the Apologists: correction, slate, cross-world ownership, Tatian. The other two concern Ottoman Orthodoxy. grkap §6 names exactly those four. The dossier header's "four entries of that date, one of which corrects a sentence of another" is right. |
| R41 | LOW | **Fixed** | Puech, `lesapologistesgr00puec_djvu.txt`: running head "TATIEN l5l" (line 7006), then "les termes dans lesquels il parle de Justin nous inclinent à croire que celui-ci était déjà mort" and "dans les deux ou trois années antérieures" (7019–7028). The citation is p. 151. |
| R42 | LOW | **Fixed** | (a) The gloss has moved outside the quotation marks ("A memorial" (the ANF footnote gives the Greek *hypomnemata*) "which Ambrose…"). It matches `anf08` 69480–69485, including the footnote n. 3496 "The Greek ὑπομνήματα". (b) §6 now paraphrases the old Tatian note without quotation marks. |
| R43 | LOW | **Fixed** | "original founder of the Severians" is gone from §2 A2. §4 item 3 quotes IV.29.6 in full ("their original founder, Tatian, …"), which is verbatim and leaves "their" unresolved. That is correct. |
| R44 | LOW | **Fixed** | grkap dossier §4 Commodian row: "its Latin has since been vendored (`commodian_carmen-apologeticum-lat_dombart1887-csel-tei.txt`), and what is missing is an English translation". |
| R45 | MOD | **Fixed** | I reran the stated method myself (regex, tag replaced by space, whitespace split, stop at the next `<div2 `/`<div1 `/`</div1>`). **Every figure reproduces to the word.** Tertullian's 32 works 731,618 (per-work: *Marcion* 187,134; *Soul* 49,425; *Resurrection* 46,242; *Ad Nationes* 34,919; *Appendix* 32,001; *Praxeas* 31,933; *Apology* 38,163; *Modesty* 26,183; *Hermogenes* 23,066; *Jews* 22,346; *Prescription* 20,936; *Flesh* 20,148; remaining twenty from *Ad Martyras* 2,677 to *On Idolatry* 15,121). *Passion* 7,325. *Octavius* 23,819; *Instructiones* 15,008; Arnobius 140,826; *Divine Institutes* 242,005 (Books I–VII 209,958 + *Epitome* 32,044 + 3-word heading); *Anger* 20,397; *Workmanship* 18,853; fragments 3,932. Original seven 464,840; added 738,943; **combined 1,203,783**. The "earlier figures 15, 15 and 13 words lower" claim checks against `d6c3be46` (241,990 / 20,382 / 18,840). "Against All Heresies" (anf03 v.xi) is correctly not among the 32: it is not on the shelf. "more precise", "confirming" and "a few dozen words" are gone. Header, B1, Tier, dossier table and dossier "What the 1,203,783 figure covers" all agree. |
| R46 | MOD | **Fixed** | (a) §4 item 1 now tags "used Cyprian's writings and read Tertullian and Minucius" `Widely Accepted` (Dombart preface lines 203–212 "Commodianum pedisequi modo institisse certissimum est", 285–286 "Tertullianeae et Minucianae lectionis … uestigia": both read) and "after Cyprian's death" `Contested`, naming Harnack, Monceaux and Aubé against Dombart, Ebert, Teuffel–Schwabe and Bardenhewer. This matches the evidence Round 6 set out. Dombart lines 149–151 "media fere parte tertii post Christum saeculi" and note 11906–11908 "persecutio septima non Gothorum est, sed Decii" re-read. (b) *De mortibus*: `Contested`, with the three dates stated. |
| R47 | MOD | **Fixed** | "Prepared at the project lead's direct request" is gone from both Step 0s and both dossiers (grep for "direct request" finds only the §6 notes recording its removal). See Part F for every remaining attribution. |
| R48 | MOD | **Fixed** | Census re-read: §0 now quotes `NEEDS-RULING.md` line 49 "The least thin of the five" exactly. §1 quotes I.43 `relationsSummary` "the Latin counterpart to the Greek apologists of the second century, a generation later and never as coherent a body" (verbatim) and says the census no longer carries the comparison (true). §2 A5 quotes `legacy` "The Latin vocabulary of Christian argument was made here. Tertullian coined most of the technical words Western Christians still use for the Trinity and the sacraments." (verbatim). |
| R49 | LOW | **Fixed** | "vendored in all six volumes (volumes I and III are cited here)". All six `monceaux_…tome1_1901` to `tome6_1922` files are present. The dossier's new claim, volumes I–III on LPC's map and IV–VI on Donatism's and none on this shelf, checks against the three maps. |
| R50 | LOW | **Fixed** | "eleven author keys across 17 works, in 39 rows". |
| R51 | LOW | **Fixed** | The Fronto mention is tagged `Documented` (Halm TEI 927 "Cirtensis nostri testatur oratio"; 3476–3477 "tuus Fronto": both re-read). The c. 160 limit is `Dominant Modern Reconstruction`, as Round 6 proposed. |
| R52 | LOW | **Fixed** | Wallis has left pole A. The text now reads "sets out both conditionals and adopts neither: about 166, under Marcus Aurelius, if Tertullian borrowed …; the beginning of the third century if Minucius borrowed …". This matches `anf04` 17131–17146 ("probably about the year 166, and Minucius flourished in the reign of Marcus Aurelius"; "the commencement of the third century"). |
| R53 | LOW | **Fixed** | "deinde fecit alterom [sic; the apparatus at line 7423 reads *alterum*], in quo indoles diuinae stirpis non permansit". The TEI has "alterom" at 7395 and the lemma "deinde fecit alterum]" at 7423. Both checked. |
| R54 | LOW | **Fixed** | §4 item 1(a) lists all six, each verbatim against the census: `voices`, `why`, `relationsSummary`, `longDescription`, I.17 `relationsSummary`, and the edge "opens the Latin case" with `confidence: Documented`. It also adds the `sourcing` "just under half a million words" and "about a hundred and eighty-four thousand words" (both verbatim). |
| R55 | LOW | **Fixed** | Now quoted to the semicolon with an ellipsis, and the document notes that the census names only two of its "three". Verbatim against I.43 `sourcing`. |
| (cosmetic) | — | Fixed | "Article 5" now reads "Methodology Section A5" (latap §2 A5). |

---

## Part C — The corrected Syriac reading (scope item 3)

**Records re-read (read-only).** `records/syr/source/syr.source.tatian-address-to-greeks.md` lines 46–52. The paragraph is headed "THE ENCRATITE CHARGE, HANDLED HONESTLY. Eusebius accuses him of it …", and the clause is "written before the events Eusebius describes". The frontmatter has `formation_confidence: Documented` (line 13) and `verification_state: verified-direct`. `records/syr/figure/syr.figure.tatian.md` lines 38–39: "Eusebius IV.29 carries the Encratite heresy charge against him personally". I grepped all of `records/syr/` for Justin, Crescens, IV.16 and martyrdom. Justin appears only as Tatian's teacher (figure line 31, source line 16, the search record lines 24 and 51). "Martyrdom" appears only for Persian martyrs. Nothing refers to Justin's death or to *HE* IV.16.

**What the Step 0s now say.** grkap §2 A2 (line 74), §4 item 2 and item 3, and dossier §5 all say the same four things:
- the clause refers to the Encratite events;
- read that way it is supported as Dominant Modern Reconstruction, not Documented;
- the record says nothing about Justin's death;
- its real defects are the accuser ("Eusebius accuses him", where Irenaeus is earlier) and the `Documented` tag.

That is exactly what the records support. The earlier wording ("ambiguous", "not supported as worded", "over-broad") is gone from both documents. grkap adds one qualification: the `Documented` tag "fits what it says about the text of the *Address*" and is too strong for a relative date. That is fair, because the record's other claims (ch. XLII, the Assyrian origin, verified directly at a line) are textual. It does not overstate the defect.

**The log entry.** The correction entry (log lines 16–38) sits above the slate entry, which the log's newest-first order requires. It says "the entry below", which is right. It supersedes "only that one sentence of the slate entry" and leaves the slate entry's text intact, as append-only requires. It states the same reading as the Step 0s, the same two defects, and that no record is edited. It is consistent with grkap and with the grkap dossier.

**Result.** Consistent and correct. Any change to the Syriac records still belongs to the Syriac world's thread (Part G, item 4).

---

## Part D — The diff: new material (scope item 2) and fresh samples

**grkap (six or more sampled, all verified):**
1. `NEEDS-RULING.md` line 24 quotation: verbatim.
2. Puech p. 151: verified (R41).
3. Harnack 1897 on the *Hortatory Address*, reworded to "2. Jahrh. lieber nicht angehört": verbatim substring of "da sie dem 2. Jahrh. lieber nicht angehört" (`b1geschichtederalt02harn_djvu.txt` 30167–30168, footnote 4). This replaces Round 6's word-order note.
4. Harnack 1897 on Aristo, reworded to "dem J. c. 140 nahe zu bleiben": verbatim at 17285, in the footnote on pp. 268–269 ("bestärkt uns in der Annahme, dass wir dem J. c. 140 nahe zu bleiben haben"). The earlier "der Zeit um 140 nahe zu bleiben" (17212) was also verbatim, so the change is from one real phrase to another.
5. Syriac record paragraph and figure-record "Eusebius IV.29" (lines 38–39): verbatim (Part C).
6. Hub log 2026-09-26 entry, "quotes no words of Mark's": true. It names "Mark's ruling (2026-09-10)" and quotes nothing he said.
7. Zahn 1881, "a Google Books scan, not vendored": the archive.org item `ForschungenZurGeschichteDesNeutestam1` is Teil I. On p. 279 it has "also etwa um 150", the singular-king argument excluding the joint reign ("nur vor dem März 161, noch unter Antoninus Pius"), and on p. 283 "schrieb bald nach seiner Bekehrung die Griechenrede". Everything except "soon after his conversion" falls inside the cited pp. 275–280. That phrase is on p. 283, a page-range slip too small to count as a finding. **Round 6's "not verified" is now verified.**

**latap (six or more sampled, all verified):**
1. `NEEDS-RULING.md` line 49, "The least thin of the five": verbatim.
2. I.43 `relationsSummary` and `legacy` quotations: verbatim.
3. The six census phrases and the edge note: verbatim (R54).
4. Hub log 2026-09-26 entry title and the "records it as a ruling dated 2026-09-10 … quotes no words of whoever ruled" description: accurate.
5. Brandt TEI 7395–7396 and 7423: verified (R53).
6. Dombart preface 149–151, 203–212, 283–286, note 11904–11908: verified (R46).
7. Wallis's two conditionals (`anf04` 17131–17146): verified (R52).
8. New claim: "the Round 1 and Round 3 review artifacts record that wording" (the pre-merger `relationsSummary`). True. The phrase appears in latap Rounds 1, 2, 3 and 5, so the list is incomplete but not wrong.
9. New claim: Monceaux I–III on LPC and IV–VI on Donatism, none on this shelf: true (R49).

**New numbers.** All latap figures reproduce (R45). grkap introduces no new numbers beyond the recounted shelf (R36).

**Changed confidence tags.**
- Commodian "after 258": now `Contested`.
- *De mortibus*: now `Contested`.
- Fronto mention: now `Documented`.
- c. 160: now `Dominant Modern Reconstruction`.

Each change matches the evidence cited and Round 6's re-derivation. No tag was raised.

**Tier reasoning.** Unchanged in both documents. latap's Tier sentence now carries 1,203,783 and 464,840, both reproduced.

---

## Part E — Consistency (scope item 4)

- **grkap Step 0 and dossier.** They agree on 17 works, 39 rows, 36/3 roles, 22 original-language rows (6/16), the corrected shelf notes (dossier: "None is open"), the Syriac reading, the four log entries, the Tatian ruling and the cross-build flags. The only inconsistency left is inside Step 0 §6 (R56).
- **latap Step 0 and dossier.** They agree on every word count (all 40 table rows match my run), 43 works, 96 rows, 42/54, 94/2 roles, 6 provisional works, 42 of 43 with an original-language witness (the *Appendix* has none; the *Carmen* has no English), the dating tags and the census list. The exceptions are R57 and the cosmetic "six places" wording.
- **Between the two Step 0s.** Both treat "direct request" the same way: removed, with the removal recorded in §6. Both cite the Hub log 2026-09-26 as the only record of their earlier ruling. Both quote the slate entry the same way. latap's I.35 bullet (17 works, 39 rows, eleven author keys) matches the grkap shelf.
- **Against the census now.** Every census quotation in either Step 0 was re-checked against `cic-website/data/world-census.json` in this round and is verbatim, including I.25 `floorNote`, I.20 status, IV.13 and V.11 "Within Another World (A5)", and I.17's status and "No community descends from him".

---

## Part F — Attribution to the project lead or Mark (scope item 1)

Every remaining statement in either Step 0, or either dossier, that names Mark or the project lead:

| Where | Statement | Record | Safe? |
|---|---|---|---|
| grkap header, §2, §3 opening; latap §2 A5 (line 63) | "for the project lead's own consideration / use" | None needed. These describe the audience, not an act. | Yes |
| grkap §2 A5 (line 98); latap §4 item 1 | Mark's / the project lead's words "yes, approve the slate and proceed" | LIBRARY-DECISION-LOG, slate entry, verbatim | Yes |
| grkap §3 B3 (line 171); grkap dossier §5 | Mark's words "that shouldnt be something he says …" | Log, cross-world-ownership entry, verbatim with his spelling | Yes |
| grkap §3 B3 (line 175), §4 item 2, §6 (line 231); grkap dossier §5 | Mark's words "if a voice influcences three worlds …"; "Mark's ruling of 2026-09-29" | Log, Tatian entry, verbatim. The reading is labelled the Library's and "stated back to Mark for correction" | Yes |
| grkap §3 B3 (line 169), §4 item 1 (line 202); grkap dossier §5 | cross-build flags "an open decision for Mark" / "flagged to Mark" | Log "Follow-up not ruled" | Yes. These route an open matter to him; they do not attribute a decision. |
| grkap line 169, line 233 | Justin ruling's only record is the Hub log 2026-09-26, "which quotes no words of Mark's" | Hub log, read | Yes |
| latap §2 A5 (line 59) | Tertullian ruling's only record is the same Hub entry, "quotes no words of whoever ruled" | Same | Yes. The document does not name the ruler; the Hub entry does ("Mark's ruling"). |
| latap §4 item 6, §6 (line 223) | "a decision for the project lead" / "Two matters remain the project lead's" | None needed. These route open matters. | Yes |
| latap §6 (line 221), grkap §6 (line 237) | Record the removal of the "direct request" sentence | — | Yes |

Nothing attributes a ruling, request or quotation to Mark or the project lead without a record I could open.

---

## Part G — Escalations (scope item 5)

1. **Cross-build flags already in canonical records** (`pahc.figure.justin.md` lines 44–46; `alx.figure.antony.md`). Mark's decision. The log flags it, and both documents leave it open. **Still needs the project lead.** Unchanged from Round 6.
2. **Justin co-ownership and the Tertullian merger (I.17 → I.43).** Both are cross-world decisions whose only written record is the derivative Hub-log entry, which quotes no words of Mark's. Both documents now say so plainly. **Needs the project lead only for confirmation**, if the Hub entry is not accepted as the record. That Hub entry (append-only, in `Build/Ministry/`) also still carries the superseded figures 464,797 and 1,194,575. That is not a defect of these documents. A later Hub entry could point to the recount (1,203,783).
3. **Tatian as a general rule.** The log's reading ("not a ruling on anything beyond Tatian and figures that share Tatian's shape") is quoted accurately by grkap. It should not be applied to a third figure until Mark confirms the reading. Neither document does so. **No new escalation.**
4. **The Syriac record's two defects** (the accuser; `Documented` on a relative date). These are cross-world and belong to the Syriac thread. The documents and the log now state them correctly and edit nothing. **Flag to the project lead**, as Round 6 did, now with the corrected characterization.
5. **Census wording** (six "opened/opens" phrases, two word figures) and **IJC's Lactantius record** (authorship dispute unstated). Both are correctly routed to the project lead. Nothing is edited.
6. **Review-cycle cap.** Both documents clear at this round. No fourth substantial round arises, and the Round 6 question on how the cap counts a document that took on new material after clearing does not need an answer for these two.
7. **Out of scope, flagged not touched (CLAUDE.md: doc-hygiene on content that isn't this thread's).**
   - The Ambrose row of `cic/corpus-map/greek-apologists-second-century.yaml` (line 16) still carries "Earlier note follows." (Round 6, Part E item 7).
   - `python3 tools/check_live_commentary.py --surface cic-corpus-map` reports 15 hits on `latin-apologists.yaml` (change-history patterns around lines 427–436) and none on the Greek shelf. The flagged lines I read look like witness notes rather than change history, so they may be false positives.

   Both are for the Library thread.

No Representative identity or title decision appears in either document. No governance or methodology change is made. Nothing is treated as settled that needs the project lead beyond items 1, 2 and 4, and those are stated as open.

---

## Part H — Invented detail and register in the changed passages (scope item 6)

- **Invented detail.** None found. Every new or changed quotation I sampled is verbatim at the cited line or page (Part D). Every new number reproduces. The new provenance note on Zahn (a Google Books scan) matches the archive.org item, which is a scan of that kind.
- **Register.** The changed passages are short, declarative and plain: the method paragraph in latap §3 B1, the Commodian sub-claims, grkap §2 A2's "What the Syriac record says". They have no assistant cadence, hedging filler or disclaimer-as-crutch. The UNVERIFIED markers for post-1930 scholarship are honest limits.
- **Step 0's job.** Both documents still do it. Tier reasoning, sourcing, overlap and disclosure obligations are intact, and the Tier changes from Round 6 remain stated rather than silent.

---

## Part I — Verifications performed (reproducible)

- **Corpus maps** (Python `yaml`): `greek-apologists-second-century.yaml`: 39 rows / 17 works; roles 36/3 with the three `context` rows named; confidence rows 32/7. Join over `cic/corpus-map/_staging/*.yaml` by title: 4 rows alone; PAHC 16, Syriac 2. `latin-apologists.yaml`: 96 rows / 43 works; 42 ANF / 54 other; roles 94 `tradition` / 2 `transmission`; authors Tertullian 32, Lactantius 4, Commodian 2, Cyprian 2, Arnobius 1, felix 1, passion_of_perpetua 1; 6 provisional works (no work with mixed confidence); no original-language row for the *Appendix*; no English row for the *Carmen*. Monceaux files: tome1–3 on `latin-pastoral-congregational-christianity.yaml`, tome4–6 on `donatism.yaml`, none on `latin-apologists.yaml`.
- **Word counts:** the script as described in R45, over `anf03`, `anf04` (div2 `iii.ii`–`iii.xi`, `iv.iii`, `v.ii`), `anf06` (`xii.iii`) and `anf07` (`iii.ii`–`iii.vi`; `iii.ii` split at div3 `iii.ii.viii`). All figures in Part B, R45.
- **Census:** `movements` I.35, I.43, I.17, I.25, I.20, IV.13, V.11; `edges` from and to both entries. All quotations in both Step 0s re-checked.
- **Records (read-only):** `records/syr/` as in Part C.
- **Logs:** LIBRARY-DECISION-LOG.md 2026-09-29 entries (headings at lines 16, 42, 77, 102, 132, 179), read in full for the four Apologists entries. `CiC_System_Hub_Decision_Log.md` 2026-09-26 entry (lines 5569–5595). `NEEDS-RULING.md` lines 24 and 49.
- **Vendored texts:** `anf08` 69466–69490; `anf04` 17128–17150; Halm TEI 925–928, 3475–3478; Brandt TEI 7393–7398, 7420–7425, 22700–22707, 35340–35343, 35377–35383; Dombart CSEL 15 145–152, 203–213, 283–287, 11900–11910; `npnf203` 40648–40653; `npnf206` 16714–16717; Robinson 1733–1738, 3354–3365; `anf03` 59447–59462; Monceaux I 5622–5627.
- **Public-domain scholarship (archive.org `_djvu.txt`):** Harnack 1897 `b1geschichtederalt02harn` (17210–17216, 17270–17287, 30165–30172); Puech `lesapologistesgr00puec` (7000–7030); Zahn 1881 `ForschungenZurGeschichteDesNeutestam1` (16640–16662, 16890–16898; page heads 279, 283).
- **Diffs:** `git diff d6c3be46 HEAD` for both Step 0s, both dossiers and the log. `cmp` of the two Round 6 copies.
- **Attribution:** grep of both Step 0s and both dossiers for "Mark", "project lead", "direct request", "ruled/ruling" (Part F).
