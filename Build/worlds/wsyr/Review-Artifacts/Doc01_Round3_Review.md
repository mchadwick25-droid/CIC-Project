# Adversarial Review, Round 3: wsyr library stage (Step 0, Doc_01, Doc_02), targeted recheck against the Round 2 fixes (commit 6a822f4c); cap reached, escalated

**Verdict: SUBSTANTIAL REVISION REQUIRED.**

The Round 2 fix corrected the original misattribution (crediting the
translator's own excursus to John of Ephesus) but overcorrected: several
passages now state John of Ephesus is *not* a source for the Tritheist
controversy at all, which is also false. Checked directly against
`cic/texts/john-of-ephesus_ecclesiastical-history-part3_paynesmith1860.txt`:
the translator's excursus runs c. lines 4471-4575 (the Ascunages creed, the
Condobaudite background, and the reported four-day disputation all sit
inside it — a translator's footnote around lines 4714-4726 even flags that
Bar-Hebraeus "substitutes the name of John of Asia for Stephan" in one
detail, casting further doubt on any claim that John himself took part).
But John's own narrative resumes at line 4580 (Conon's arrest) and covers
the Tritheite controversy at real length afterward — c. 300 lines,
including John of Ephesus himself refusing the Tritheites' bribes and
calling them heretics (~4625-4640), a debate ordered before the patriarch
and synod (~4700), John naming John Philoponus by name as the one who
"first led them into error" (~4777-4790), and the resulting Cononite/
Athanasian split (~4808-4880). The corpus-map staging file
(`cic/corpus-map/_staging/john-of-ephesus_ecclesiastical-history-part3_
paynesmith1860.yaml`) and Doc_02 §2's own verification-loci bullet already
state this correctly (excursus vs. John's own narrative, split at line
~4579). Five other passages do not:

- Doc_02 lines 25-27 ("is not John's own reporting")
- Doc_02 lines 158-160 ("**Not** the source for the Tritheist/Trinitarian
  controversy in Book I")
- Doc_02 lines 238-240 (the faction "known to this build via... translator's
  excursus, not John of Ephesus's own reporting" — false for Philoponus,
  whom John names himself)
- Doc_01 §6 (this build's "own knowledge of it comes from the... excursus...
  not from John of Ephesus's own contemporary narrative" — misleading; John's
  own narrative runs on for c. 300 lines)
- Open_Gaps item 5 ("the Book I controversy material... is the translator's
  excursus... corrected throughout" — too broad)

All other Round 2 findings (Trinitarian-not-Christological framing, the
Step 0 "formulaic" claim/A3 consistency, the Sergius of Tella date, the
Jacobite self-designation overreach, the 586-616 schism/Heraclius gap) are
confirmed FIXED, independently re-verified against the primary sources.
Mechanical checks all pass (`engine.m1.cross_world` exit 0,
`corpus_map_merge.py --check` exit 0, `texts_registry.py` only the two
pre-existing, unrelated fixture-synthetic problems).

**This is the third round of substantial revision. Per `cic-build-cycle`'s
own cap, this document set now stops and escalates as an unresolved
tension rather than attempting a fourth round.** The remaining fix itself
is narrow and precisely specified (reword the five passages above so they
match what the staging file and Doc_02 §2 already correctly state: the
Ascunages creed / Condobaudite background / four-day disputation are the
translator's own excursus via Bar-Hebraeus; the Tritheite schism narrative
from line 4580 onward, including John's own participation and his naming
of Philoponus, is John of Ephesus's own reporting) — but per this
project's own review-cycle discipline, applying it is not this build
thread's call to make unilaterally at this point. See
`Open_Gaps_Tracking.md`'s own final entry and this world's handoff report
to the project lead.

## Disposition

Disposition: Approved to proceed. Recorded by the Library thread after the project lead's directed Round 4 correction, as stated in the status line of Step 0, Doc_01 and Doc_02. The Round 4 check has no review file of its own; it is recorded in `Open_Gaps_Tracking.md` item 18.
