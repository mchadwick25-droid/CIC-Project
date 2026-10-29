Simulated review — informational only, not an Article 31 substitute.

Reviewer model: claude-opus-5-5
Drafter model: Sonnet 5.5
Reviewer agent: second cap-ruling reviewer (fresh Opus 5.5 subagent, session_01JMNsSDRcCWuRTZfKoJ41wk)
Drafter agent: aec cap-ruling fix-pass thread (PR #1292, merged at `aa6adda5`)
Round: 5
Truncation check, method 1: full structural read of `Doc_01_World_Identification_Boundaries_Orientation.md` (124 lines by `wc -l`; all eight `## ` sections present, §1 to §8, counted by `grep -c '^## '`; the file ends on the §8 line "Held pending the project lead's confirmation of the World #8 boundary question, matching Step 0's status.")
Truncation check, method 2: byte comparison: the working file's 38,601 bytes (`wc -c`) equal its blob size on `origin/main` at `c358f051b` (`git ls-tree -l`), and `tail -c` shows the closing line complete; sha256 `30ac3f23…9c296c`

# Review of Doc_01 — World Identification, Boundaries, and Orientation (`aec`): second cap-ruling targeted recheck

**Authority.** Mark ruled on 2026-10-29 that Doc_01 and Doc_02 get a second extra targeted Opus review after the narrow fixes of PR #1292. The System Hub Decision Log entry "2026-10-29 - Cap ruling: aec Doc_01 and Doc_02, second extra review (project lead)" names this file. **Under that ruling this review does not count toward the three-round cap.** If it does not clear, the specific open findings go back to Mark. No further round runs on the build thread's own initiative.

**Gate note.** `python -m engine.m10.cli roundcount aec 1` still counts this file (4 files against a cap of 3). The gate reads only bare file names in backticks (`_LOGGED_FILE` in `engine/m10/rounds.py` excludes any name containing "/"), and the Cap ruling entry names this file by its full path. The ruling itself is clear. Matching the entry to the gate is for the project lead or the thread that owns the Decision Log, not for this review.

**Scope and method.** A targeted recheck. Each finding of `Doc01_CapRuling_Review.md` (N1 to N5) is checked against the current text. Every claim, figure, quotation and locus that PR #1292 changed or added is checked again against the vendored files in `cic/texts/` and against the corpus map, with XML tags stripped and endnotes set aside where a body text is quoted. No drafter claim of "verified" was relied on. I did not edit the document.

---

## Prior findings: status

| Prior finding | Status | Evidence |
|---|---|---|
| N1. §5: the Socrates II.44 quotation joined across a sentence boundary and cited for agreement after 381 | **Closed** | §5 now quotes two whole sentences of `npnf202` `ii.v.xliv-p3`, verbatim: "those who originally embraced the homoousian opinion would not communicate with them, because Meletius had been ordained by the Arians, and his adherents had been baptized by them. Thus was the Antiochian church divided, even in regard to those whose views on matters of faith exactly corresponded". The claim is now limited to Meletius's first episcopate, about 360 to 361, which is what the chapter narrates (election at Antioch, exile under Constantius, Euzoïus installed). The post-381 settlement is stated separately and tagged Widely Accepted. |
| N2. §4: `iv.x.cl` called "independently verified present" | **Closed** | §4 now says `iv.x.cl` appears "by its title alone, with an editor's note on its authorship". Verified: the division holds only the line "CXLIX is 'Copy of the Letter written by John, Bishop of Antioch, to Nestorius.'", one sentence, and a note quoting Venables and Tillemont on its attribution to Theodoret. The working example is `iv.x.cli`. Each of the five letters now named (`iv.x.cli`, `iv.x.clxiii`, `iv.x.clxiv`, `iv.x.clxvii`, `iv.x.clxxiii`) opens with printed text in the file. The editor's dates hold: `cli` "may be dated in February 431"; `clxiii` "towards the end of July or in the beginning of August 431"; `clxiv` "may be dated in Sept. 431"; `clxvii` is headed "addressed from Chalcedon". The date given for `clxxiii` is a new problem (R2-N1). |
| N3. §4: canon XIII "by name" against "not named" | **Closed** | §4 now says canon XIII "condemns by description, not by title". The quotation of `npnf214` `xii.vii-p36` is verbatim: "the impious writings of Theodoret, directed against the true faith and against the first holy Synod of Ephesus and against St. Cyril and his XII. Anathemas, and [defends] that which he has written in defence of the impious Theodore and Nestorius". The disclosure now reaches `iv.x.clxiii` and `iv.x.clxxiii`, and both quotations are verbatim: "Such is the mockery of a synod held by Egyptians, by Palestinians, by men from the Pontic and Asian dioceses, and by the West in their company" and "to what has been done unjustly and illegally against your holiness, not even if one were to cut off both my hands would I ever assent". The other letters carry the disclosure until a reading settles them. |
| N4. §4 and §6: the boundary finding did not reach the Antiochene-party `tradition` rows | **Closed as to coverage**; two new problems in the added text (R2-N1, R2-N2) | §4 now weighs each of the five rows: the *Bazaar* with Nau's translation, Loofs's *Nestoriana* split by item, the *Conciliabulum Ephesinum* and the *Synodicon*. §6 points to §4. The corpus-map rows are left to the Library thread. |
| N5. §1: exact word counts no longer reproduced | **Closed** | Re-run on `npnf109` to `npnf114` at `origin/main`: `LC_ALL=POSIX wc -w` 3,332,586; `LC_ALL=C.UTF-8 wc -w` 3,351,124; a Python 3 whitespace split after replacing each tag with a space 3,032,271. All three match §1, which now dates them (October 2026) and states their scope (markup and apparatus included). |

## Verified at source this round (holds)

- §4, the *Bazaar*: the corpus-map note and the file header both say "written in exile in the 440s". The Driver and Hodgson introduction, reporting Bethune-Baker, says "The book must have been written by Nestorius in the year 451 or 452", from the death of Theodosius II in 450 and the flight of Dioscorus (file lines 314 to 317). Nau says "terminé en 451" (file lines 857 to 858). The Contested tag is right. The header names Ephesus II (449) and Leo's Tome as part of the subject.
- §4, *Nestoriana*: the Driver and Hodgson table (compiled from Kidd, file lines 799 to 800) lists "November Nestorius Ad Caelestinum III" (line 813) and "Dec. 13 & 14 Nestorius preaches two sermons (xiii and xiv) and sends them to Cyril with counter anathematisms" (lines 825 to 827). The *Tragoedia* and *Theopaschites* passage is verbatim at Bazaar file lines 2297 to 2299: "as a defence against those who blamed him for having wanted a council to be held". The Loofs contents list names "Aus der ep. II ad praesidem. Thebaidis" (line 474), "Aus der Tragoedia" (489) and "Aus dem Theopaschites" (490).
- §4, the *Conciliabulum*: "THE Council of Ephesus met in June, A.D. 431" (Bazaar file line 264). Mansi file header names the acts at index 325 and heading 46711, as the corpus map does. Canon XIII's closing clause, "all those who have written contrary to the true faith or against St. Cyril and his XII. Chapters", is verbatim at `xii.vii-p36`. The Inferential-Thin tag on whether it reaches the acts is apt.
- §4, the *Synodicon*: the Baluze preface (Mansi file lines 73052 to 73056, OCR spelling normalized here) opens "Certum est opus esse hominis post Justinianum scribentis, defensoris praeterea trium capitulorum", and a later sentence calls the compiler "Nestorii sectatorumque ejus adversarium". The document's paraphrase holds.
- §4, canon XI: "Arius, Eunomius, Macedonius, Apollinaris, Nestorius, Eutyches and Origen, as well as their impious writings" is verbatim in `npnf214`. The paragraph locus is off by one (R2-N3).
- §1 and §6: no new claim. `tools/check_live_commentary.py --surface worlds` flags only protected status, date and route-cue lines in this file.

---

## New findings

### R2-N1. Blocking (substantial). §4: Letter `iv.x.clxxiii` is misdated into the "430–431" run, and the same letter gets two Boundary Statuses.

**Location.** §4, the Letters paragraph: "a run of letters directly from the Nestorian controversy of 430–431 (… his letter to Nestorius, `iv.x.clxxiii`; …)". §4, second bullet, which holds this run as a live edge case. §4, the *Synodicon* bullet, which finds the *Synodicon*'s letters of 431 to 435 "out of the window by subject and date". §7 items 2 and 6 carry the same split.

**Evidence.**
- The letter's own text (`npnf203` `iv.x.clxxiii`) cannot come before Ephesus. Theodoret refuses to assent "to what has been done unjustly and illegally against your holiness", which is Nestorius's deposition of 431. He also writes "Let no one therefore persuade your holiness that I have accepted the Egyptian writings as orthodox, with my eyes shut, because I covet any see", and says he has found them "free from all heretical taint".
- The NPNF note gives the letter's first Latin witness as "Synod c. 120. Mens. v. 898". That is the *Synodicon* in Mansi tom. 5. The same letter is in the vendored Mansi file at lines 88748 to 88766 (columns 899 to 900; OCR spelling normalized in both quotations here): "His autem quae contra tuam injuste & inique facta sunt sanctitatem, nec si ambas manus meas quilibet abscindat, patior assentire".
- The Mansi editor's note on it (file lines 88713 to 88724) says: "In Concilio vero quinto adnotatum est eam esse scriptam post unitatem factam inter orientales & Cyrillum". It also gives Mercator's title, "directa Nestorio jam in exilio". So the letter was written after the union of 433, to Nestorius already in exile. That is Documented in the vendored apparatus. The NPNF note's own phrase, "not long after the receipt by Theodoret of the Chapters of Cyril", gives no year and cannot mean 430, given the letter's content.

**What is wrong.**
- The letter is not 430–431 material. It belongs to the 431–435 aftermath, the same span the *Synodicon* covers.
- One letter now has two statuses: a live edge case in the Theodoret run (§4; Registry row 11a) and, as part of the *Synodicon*, "out of the window by subject and date" (§4; Registry row 23).
- The test is applied unevenly to the Ephesus aftermath. §4 holds Theodoret's letters of July to September 431 (`clxiii`, `clxiv`, `clxvii`) and the *Conciliabulum* acts of 431 as live edge cases, because their subject, Ephesus, sits one year past the window. Yet it excludes the *Synodicon*'s letters of 431 to 435, whose subject is the same events and whose dates overlap. §4 says the test is subject matter, applied "consistently". As written, the outcome depends on which vendored volume prints a letter.

**Why it matters.** This is a scope-boundary decision, not a style point. The condemned-content disclosure travels either way, but the Boundary Status of the same text cannot be both edge case and excluded.

**Required.** Correct the date and status of `iv.x.clxxiii`, citing the Mansi note. State how the subject test treats the Antiochene party's letters after Ephesus, from 431 to 435, and apply it the same way to the `npnf203` letters and to the *Synodicon*'s letters. If the compiler's later, hostile frame is the reason for excluding the *Synodicon*, say that it excludes the frame, and give the letters it gathers the status their subject and date earn. This review's predecessor (`Doc01_CapRuling_Review.md`, N3) also described `iv.x.clxxiii` as part of the 430–431 run. That description was wrong, and this finding corrects it.

### R2-N2. Blocking (source attribution). §4, *Nestoriana* bullet: the witness for the letters to the governor of the Thebaid is Evagrius, not "a Syriac account".

**Location.** §4, *Nestoriana* bullet: "the letters to the governor of the Thebaid, which a Syriac account quoted in Nau's introduction cites for the penalties that befell him (Nau file lines 940-943)".

**Evidence.** In `nestorius_livre-d-heraclide-de-damas-fra_nau1910.txt`, Nau introduces the passage at lines 892 to 900. He says that "l'historien Évagrius a vu le texte grec des deux derniers ouvrages de Nestorius", and then: "Nous résumons tout ce chapitre d'Evagrius". The passage at lines 902 to 943 is that summary of Evagrius. Lines 941 to 943 read: "Quant aux peines qui lui sont arrivées … on les apprend par d'autres lettres qu'il a écrites au gouverneur de la Thébaïde". Nau's footnote 2 (line 960) confirms it: "Evagrius cite la lettre par laquelle Nestorius apprend au gouverneur…". The "légende syriaque" is a separate footnote (line 945).

**Why it matters.** The dating conclusion holds: the letters come from the Egyptian exile, after Ephesus. But the document names the wrong source for a claim. Evagrius is a Greek church historian of the later sixth century, hostile to Nestorius. That is a different witness, with different weight, from a Syriac account. Under CLAUDE.md's source-fidelity rule, a wrong statement of what a source is, or what it says, is not cosmetic. The same attribution sits in Registry row 25a.

**Required.** Attribute the passage to Evagrius, as Nau summarizes him, and keep the line loci.

### R2-N3. Non-blocking (locus). §4: canon XI is cited to its heading paragraph.

`npnf214` `xii.vii-p26` (file line 23852) holds only the heading "XI." The canon's text, with the quoted words, is `xii.vii-p27` (line 23853). Canon XIII is correctly cited to its text paragraph, `xii.vii-p36`. Correct the locus here and in Registry row 24.

### R2-N4. Non-blocking (overstatement). §4: "never by title".

§4 says canons XI to XIII "condemn writings by naming or describing their author, never by title". Canon XII (`xii.vii-p34`) names a work: "this same Theodore in his Commentary on the Acts of the Apostles compares Christ to Plato, Manichæus, Epicurus and Marcion". The point that matters, that canon XIII names no work of Theodoret's, still holds. Narrow the sentence to what each canon does.

### R2-N5. Non-blocking (alignment with the Contested tag). §4: "Written after the window, by about twenty years."

"About twenty years" takes the 451 or 452 date. On the "440s" statement, which the same bullet reports, the gap is ten to nineteen years. State the gap as a range, or tie it to the date it assumes. The same phrase is in Registry row 24.

---

## Verdict

**Doc_01: did not clear. Not Approved to proceed.**

All five prior findings are closed. N4 is closed as to coverage, but the text added to close it carries two new blocking findings: R2-N1 and R2-N2. R2-N3 to R2-N5 are non-blocking and can be applied directly without a further review. Under Mark's ruling of 2026-10-29, this review does not count toward the cap, and no further round runs on the build thread's own initiative. The open findings go back to Mark.

Open blocking findings for Mark, exactly:

1. **R2-N1.** §4 places Theodoret's letter to Nestorius (`npnf203` `iv.x.clxxiii`) in a "430–431" run and holds it as a live edge case. The letter refers to Nestorius's deposition and to Theodoret's acceptance of "the Egyptian writings". The vendored Mansi file prints it in the *Synodicon* (lines 88748 to 88766), with a note that it was written after the union of 433 to Nestorius in exile (lines 88713 to 88724). §4 excludes the *Synodicon*'s letters of 431 to 435, but holds Theodoret's letters of 431 and the *Conciliabulum* of 431 as edge cases. So the same letter has two statuses, and same-subject letters are treated differently according to the volume that prints them.
2. **R2-N2.** §4 credits "a Syriac account quoted in Nau's introduction" with citing Nestorius's letters to the governor of the Thebaid. Nau's text there is his summary of Evagrius (Nau file lines 892 to 943; footnote 2 at line 960).

Non-blocking items to apply directly: R2-N3 (canon XI locus `xii.vii-p27`), R2-N4 (canon XII names Theodore's *Commentary on Acts*), R2-N5 (state the *Bazaar* gap as a range).
