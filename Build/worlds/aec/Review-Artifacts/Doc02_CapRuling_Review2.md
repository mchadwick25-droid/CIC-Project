Simulated review — informational only, not an Article 31 substitute.

Reviewer model: claude-opus-5-5
Drafter model: Sonnet 5.5
Reviewer agent: second cap-ruling reviewer (fresh Opus 5.5 subagent, session_01JMNsSDRcCWuRTZfKoJ41wk)
Drafter agent: aec cap-ruling fix-pass thread (PR #1292, merged at `aa6adda5`)
Round: 5
Truncation check, method 1: full structural read of `Doc_02_Source_Ecology.md` (229 lines by `wc -l`; all ten `## ` sections present, §1 to §10, by `grep -c '^## '`; ends on the §10 line "Held pending the project lead's confirmation, matching Step 0's status.") and `Source_Registry.md` (80 lines; 39 table rows by `grep -c -E '^\| [0-9]+[a-z]? \|'`, numbered 1 to 33 with sub-rows 6a, 8a, 11a, 11b, 14a and 25a; the three closing sections present, ending on the Living-document protocol sentence)
Truncation check, method 2: byte comparison: the working files' byte counts by `wc -c` (Doc_02 49,974; Registry 37,814) equal their blob sizes on `origin/main` at `c358f051b` (`git ls-tree -l`), and `tail -c` shows each closing line complete; sha256 `3e0176c1…369313` and `19ee06f8…d625`

# Review of Doc_02 — Source Ecology, with `Source_Registry.md` (`aec`): second cap-ruling targeted recheck

**Authority.** Mark ruled on 2026-10-29 that Doc_01 and Doc_02 get a second extra targeted Opus review after the narrow fixes of PR #1292. The System Hub Decision Log entry "2026-10-29 - Cap ruling: aec Doc_01 and Doc_02, second extra review (project lead)" names this file. **Under that ruling this review does not count toward the three-round cap.** If it does not clear, the specific open findings go back to Mark. No further round runs on the build thread's own initiative. This file covers Doc_02 and its companion `Source_Registry.md`.

**Gate note.** `python -m engine.m10.cli roundcount aec 2` still counts this file (4 files against a cap of 3). The gate reads only bare file names in backticks (`_LOGGED_FILE` in `engine/m10/rounds.py` excludes any name containing "/"), and the Cap ruling entry names this file by its full path. The ruling itself is clear. Matching the entry to the gate is for the project lead or the thread that owns the Decision Log, not for this review.

**Scope and method.** A targeted recheck. Each finding of `Doc02_CapRuling_Review.md` (D1 to D9) is checked against the current text. Every claim, figure, quotation and locus that PR #1292 changed or added is checked again against `cic/texts/`, the corpus map and the holdings tool. Counts are each run by two methods. No drafter claim of "verified" was relied on. I did not edit either document.

---

## Prior findings: status

| Prior finding | Status | Evidence |
|---|---|---|
| D1. The bucket holds 66 rows; the Registry covered 50 | **Closed** | Two methods agree on 66: PyYAML gives `len(works) == 66`, and `grep -c '^- row_id:'` gives 66. Each corpus-map row was mapped by `source_file` and work title to a Registry row. All 66 are covered: `npnf109` 18 rows (rows 2 to 10), `npnf110` to `npnf114` 17 (row 1), `npnf202` 2 (14, 14a), `npnf203` 4 (11, 11a, 11b), `npnf214` 3 (16), `npnf211` 1 (15), `anf07` 1 (12), Ammianus 1 (13), Palladius *Dialogue* 1 (19), Neale 1 (20), *Lausiac History* 1 (21), Mansi 2 (22, 23), Nestorius 3 (24, 25, 25a), PG 47 2 and PG 52 1 (26, 27), Barhebraeus 1 (28), Barhadbeshabba 1 (29), Cyril (Pusey) 2 (30), Marius Mercator 1 (31), Ethiopic Synaxarium 1 (32), Socrates and Sozomen Greek 2 (33). Sum 66. The loci in rows 22 and 26 to 33 match the corpus-map `locus` fields, and the quoted corpus-map notes are verbatim. |
| D2. Stale holdings figures; eleven files undispositioned; Table D 83 not 84 | **Closed** | `python -m engine.m9.cli holdings aec` at `origin/main` reports 1,522 / 2 / 113 / 51 / 1,356, matching §8. A script compared the 113 "in scope, unread" files with §8: 19 are dispositioned in the first table (`npnf111` to `npnf114` counted by their shorthand) and 94 in Table D, with no file missing, no duplicate, and no Table D file outside the 113. Table D has 94 rows by two methods: `grep -c '| Deferred |'` gives 94, and counting lines beginning "| `" inside Table D gives 94. §9 item 6 now says 19 and 94. Tracking entry 17 records the correction of entry 11(d). |
| D3. `iv.x.cl` called verified present | **Closed** | §1 and row 11a now say it is in the volume "by its title alone". Verified, as in `Doc01_CapRuling_Review2.md`. |
| D4. Condemned-content disclosure narrower than canon XIII | **Closed** | Row 11a and §1 now say canon XIII condemns by description and reaches `iv.x.clxiii` and `iv.x.clxxiii`. The canon's wording at `npnf214` `xii.vii-p36` is quoted verbatim. §6 now says "a live edge case under canon XIII's description of condemned writings". |
| D5. Lausiac History line loci at chapter headings | **Closed** | §6 and row 21 now cite lines 549, 427, 477 and 583. `grep -n -F` finds each quoted phrase on exactly those lines: "dispersed all her goods and gave to the poor" and "instructed many women, addressed priests reverently, and honoured bishops" at 549; "embroiled in the disturbance connected with the blessed John" at 427; "the deaconess Sabaniana, aunt of John the bishop of Constantinople" at 477; "to Rome because of the blessed bishop John" at 583. |
| D6. Word counts no longer reproduced | **Closed** | On `npnf110`: `LC_ALL=POSIX wc -w` 534,065; tag-stripped whitespace split 483,878. For the six volumes: 3,332,586 (`POSIX`), 3,351,124 (`C.UTF-8`), 3,032,271 (split). All match §1 and the Registry header, which date them and state their scope. |
| D7. The corpus-map tag revisit promised in §9 but not carried | **Closed** | §9 item 11 and tracking entry 17 now carry it, and extend it to the Antiochene-party `tradition` rows. |
| D8. §2 "out-of-window by date" | **Closed** | §2 now reads "out of the boundary by subject". |
| D9. Registry §9 pointer | **Closed** | The protocol now says "`Doc_02_Source_Ecology.md` §9 item 3 covers them as a group". Rows 2, 4, 13, 14a and 21 are the only A rows, as the protocol says. |

## Verified at source this round (holds)

- §8 first table: the Mansi, Nestorius, PG 47 and 52, Barhebraeus, Barhadbeshabba, Ethiopic Synaxarium, Cyril, Marius Mercator and Greek Socrates and Sozomen files exist in `cic/texts/`, and each points to the Registry row that covers it.
- §1, Antiochene-party paragraph, and §7: the *Bazaar*'s three dating statements are as reported (corpus-map note and file header "the 440s"; Driver and Hodgson lines 314 to 317, 451 or 452; Nau lines 857 to 858, "terminé en 451"). The Contested tag is right.
- Row 24: the edict of August 435 is at Driver and Hodgson file lines 270 to 273: "In August 435 imperial edicts forbade the meetings of Nestorians and decreed heavy penalties against all who should copy, preserve, or read the writings of their master, which were ordered to be burned."
- Row 22: the Council met in June 431 (Driver and Hodgson line 264), and canon XIII's closing clause is verbatim.
- Row 23: the Baluze preface is at Mansi lines 73052 to 73056, as cited.
- Row 13: Book XXII at line 14773; the church closure at 16184 to 16188; the *Misopogon* at 16236 to 16237, inside the cited 16234 to 16238.
- §4 and the acquisition gaps: no vendored file holds the *Adversus Judaeos* homilies. A search of the three vendored Migne Chrysostom volumes (PG 47, PG 50, PG 52) finds only editorial mentions in PG 50 and two garbled OCR occurrences of the word for "Jews" in PG 52, neither a homily heading. No PG 48 file is vendored. The "not vendored" claim stands.
- §6: Eunomius's *First Apology* and Philostorgius are vendored and are on no row of this bucket.
- `tools/check_live_commentary.py --surface worlds` flags only protected status, date and route-cue lines in both files.

---

## New findings

### R2-D1. Blocking (substantial). Registry rows 11a and 23, and Doc_02 §1: one letter has two Boundary Statuses, and the Ephesus-aftermath letters are split by volume, not by subject.

**Location.** Row 11a lists `iv.x.clxxiii` in "the Letters' run of Nestorian-controversy correspondence" and gives the subject as "the Nestorian controversy of 430–431" (Native, live edge case). Row 23 excludes the *Synodicon*'s letters as "of 431 to 435 … and fall wholly after the window" (Excluded, Out-of-Boundary). Doc_02 §1, the Antiochene-party paragraph, applies the same split ("The *Synodicon* … out of the window by subject and date (rows 23 and 25a)").

**Evidence.** As in `Doc01_CapRuling_Review2.md` R2-N1. The letter `iv.x.clxxiii` refers to Nestorius's deposition and to Theodoret's acceptance of "the Egyptian writings". The vendored Mansi file prints it in the *Synodicon* (lines 88748 to 88766, columns 899 to 900, matching the NPNF note "Synod c. 120. Mens. v. 898"). The Mansi note (lines 88713 to 88724) records that it was written after the union of 433, to Nestorius already in exile. So:
- the letter is not 430–431 material;
- it is Native (live edge case) under row 11a and Excluded under row 23;
- Theodoret's letters of July to September 431 (row 11a) and the *Conciliabulum* acts of 431 (row 22) are live edge cases, while the *Synodicon*'s letters of 431 to 435, on the same events, are Excluded. The outcome follows the volume that prints the letter, not its subject.

**Required.** In step with Doc_01: correct row 11a's list and date, and give the *Synodicon*'s letters, as distinct from the compiler's frame, the Boundary Status the subject test gives the same kind of letter in row 11a. Carry the change to Doc_02 §1 and §8 (the `npnf203` and Mansi rows) and to §9 item 11.

### R2-D2. Blocking (source attribution). Registry row 25a: the witness for the letters to the governor of the Thebaid is Evagrius, not "a Syriac account".

**Location.** Row 25a, Verification Note: "A Syriac account quoted in Nau's introduction cites the letters to the governor of the Thebaid for the penalties that befell Nestorius (Nau file lines 940 to 943)".

**Evidence.** As in `Doc01_CapRuling_Review2.md` R2-N2. Nau's lines 902 to 943 are his summary of Evagrius ("Nous résumons tout ce chapitre d'Evagrius", line 899). His footnote 2 (line 960) reads "Evagrius cite la lettre par laquelle Nestorius apprend au gouverneur…". The "légende syriaque" is a separate footnote (line 945). The dating conclusion holds. The named source is wrong.

**Required.** Attribute the passage to Evagrius, as Nau summarizes him, in step with Doc_01.

### R2-D3. Non-blocking (locus). Row 24: canon XI cited to its heading.

Row 24 cites canon XI's wording to `npnf214` `xii.vii-p26`. That paragraph is the heading "XI." The quoted words are in `xii.vii-p27` (file line 23853). Rows 25 and 25a refer back to row 24.

### R2-D4. Non-blocking (stale metadata). Table D's "Assigned elsewhere" column is incomplete for four files.

The column claims to name "the corpus-map buckets that assign each file". Re-derived from every `cic/corpus-map/*.yaml` by `source_file`, 90 of the 94 rows match. Four omit current buckets:
- `chronicle-of-edessa_cowper.txt`: also `the-church-of-the-east-under-persia`;
- `npnf204_athanasius-select-works-letters.xml`: also `aksumite-christianity`;
- `npnf212_leo-great-gregory-great.xml`: also `cyrilline-miaphysite-egyptian-christianity`, `latin-africa-under-byzantium` and `nicene-visigothic-iberia`;
- `npnf213_gregory-great-ephraim-syrus-aphrahat.xml`: also `british-welsh-christianity`, `cyrilline-miaphysite-egyptian-christianity`, `gothic-and-vandal-homoian-christianity`, `insular-irish-monastic-christianity`, `latin-africa-under-byzantium` and `nicene-visigothic-iberia`.

The claim that matters, that none of the 94 is assigned to this world, holds: no Table D file appears on this bucket. Complete the four rows, or date the column.

### R2-D5. Non-blocking (overstatement). Row 26: "the original Greek of works whose English is already covered by rows 5, 6, 6a and 9".

Not all of them are. PG 47's *On compunction* has no English in `npnf109`, which has no division by that title. PG 52's homilies of 399 to 404, including the homily on the exile of Saturninus and Aurelian (file line 3675), have no `npnf109` row: "Saturninus" does not occur in `npnf109`. The corpus-map note says "the English of several is in npnf109". Say "several of whose English".

### R2-D6. Non-blocking (alignment with the Contested tag). Row 24: "composed about twenty years after the window closed".

On the "440s" statement the row itself reports, the gap is ten to nineteen years. State it as a range, in step with Doc_01 R2-N5.

---

## Verdict

**Doc_02 and `Source_Registry.md`: did not clear. Not Approved to proceed.**

All nine prior findings, D1 to D9, are closed. Two new findings are blocking: R2-D1 and R2-D2. Both sit in text added to close the previous round's findings, and both must be fixed in step with Doc_01. R2-D3 to R2-D6 are non-blocking and can be applied directly without a further review. Under Mark's ruling of 2026-10-29, this review does not count toward the cap, and no further round runs on the build thread's own initiative. The open findings go back to Mark.

Open blocking findings for Mark, exactly:

1. **R2-D1.** Registry row 11a holds Theodoret's letter to Nestorius (`npnf203` `iv.x.clxxiii`) as 430–431 material and a live edge case. The vendored Mansi file prints the same letter in the *Synodicon* (lines 88748 to 88766), with a note dating it after the union of 433 (lines 88713 to 88724). Row 23 excludes the *Synodicon*'s letters of 431 to 435, while rows 11a and 22 hold letters and acts of 431 on the same events as edge cases. One letter has two statuses, and same-subject letters are split by the volume that prints them. Doc_02 §1 carries the same split.
2. **R2-D2.** Row 25a credits "a Syriac account quoted in Nau's introduction" with citing Nestorius's letters to the governor of the Thebaid. Nau's text there is his summary of Evagrius (Nau file lines 892 to 943; footnote 2 at line 960).

Non-blocking items to apply directly: R2-D3 (canon XI locus `xii.vii-p27`), R2-D4 (complete Table D's bucket column for four files), R2-D5 (row 26, "several of whose English"), R2-D6 (state the *Bazaar* gap as a range).
