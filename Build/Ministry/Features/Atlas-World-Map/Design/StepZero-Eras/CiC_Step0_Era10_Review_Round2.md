# A1.E10 Review Round 2 — adversarial review of `CiC_Step0_Era10_V1_0.md` (post-Round-1 revision + the IX.50 fold-in)

Reviewer: adversarial review agent · 2026-08-14 · Method: independent
recomputation against the primary files, never against the document's own
assertions. Re-read in full: the era doc (1437 lines), Round 1's review, the
survey (`…Survey_Research_E.md`, §3g read verbatim against every restatement),
both sources files (211 items re-counted key-by-key in node/python), the 18
candidate drafts (every field of IX.46 and IX.50 read whole; all 18 re-validated
against the live census), the Living-Era Protocol Addendum V1.0 (R1–R10, its
own R10 charge re-executed on the fold-in material), the Frozen
`CiC_Step0_Era9_V1_0.md` (c2 numbering convention, §4 queue, VIII.28–VIII.32
rows), `validate-census.mjs` (read + run), and `world-census.json` (32 era-10
rows dumped and read; IX.15/IX.24/IX.26 read field-by-field). Git history read
to separate what Round 1 fixed from what the fold-in moved.

Round 1's fifteen substantive findings were checked at their deciding sites,
not taken on the document's word. **Thirteen landed clean** (itemised at the
end). **Two landed only in the era doc's prose and left the identical defect
alive in the candidate draft that would actually enter the census** — those are
S1 and S2 below and they are the most serious findings in this round, because
the era doc now *says* they are fixed.

## VERDICT: GATE-ELIGIBLE AFTER FIXES (REVISE) — 9 substantial (S1–S9), 9 minor (M1–M9), 3 cosmetic (C1–C3)

Nothing here breaks the era's architecture and nothing requires new research
except one optional branch (noted at S1). But two findings would freeze a
manufactured citation and a false census claim into participant-facing census
copy (S1, S2); one states a falsehood about a grounding file in the very block
Mark reads to know what has been corrected (S3); one materially misdescribes
the run's sourcing landscape (S4); three sit on the newest and least-reviewed
material — IX.50's load-bearing Section A and B2 findings (S5, S6, S7); one
leaves the census's last frozen count contestable (S9); and one restates a
verified-anchor tally that disagrees with its own arithmetic by eleven (S8).

**On the fold-in's central question — has IX.50 drifted into pre-adoption, or
into a strawman?** Neither, and this is the fold-in's real achievement: the
pre-adoption hunt came up **empty** (clean check 14) and the strawman hunt came
up **empty** (clean check 15). The defects in the IX.50 material are
evidentiary and citational, not dispositional.

---

## Substantial findings

### S1. Round 1's S3 (the manufactured WCC Basis) was struck from the era doc's prose and left standing in the IX.46 draft — the file that actually enters the census
**Location:** `CiC_Step0_Era10_Candidate_Entries_E.json` **line 405** (IX.46
`floorNote`); era doc §1 item 17 (lines 396–404) and §2 (line 746).
**Ground truth:** the IX.46 draft floorNote reads, verbatim and today:
`"No question — a council of churches, not a confession-bearing body: its own
Basis (the 1948/1961 trinitarian Basis statement [S]) is cited as the
institution's dated text, with member confessions assessed only ever per body"`.
Round 1's S3 fix was "either strike the Basis clause **or** add the Basis to
the sources base as a named [S] item first." Neither happened in the draft. I
re-greped all four research inputs: the string "Basis" appears in **no** sources
file and **no** JSON except this floorNote (the only other hit is the survey
§3g quoting this same floorNote back at itself, line 146).
**Why it is worse than Round 1's version:** the era doc now asserts the fix is
done — §1 item 17: "struck here as a manufactured citation rather than
repeated"; §2 line 746: "the same floorNote's Basis citation is struck as
ungrounded at §1 and is not resurrected here." IX.46's lead lean is **adopt as
drafted** (§1 item 17; Q3). A yes at Q3 writes the manufactured citation into a
participant-facing census floorNote, with the era record stating it was struck.
Round 1 caught the fabrication in prose; the gate would freeze it in data.
**Fix (executable from file):** delete the Basis clause from JSON line 405 so
the floorNote reads "No question — a council of churches, not a
confession-bearing body: member confessions assessed only ever per body"; and
change §2 line 746's parenthetical from "is struck as ungrounded at §1" to
"was struck from the draft floorNote at Round 2." *The alternative branch
Round 1 offered (add the Basis to the sources base first) would require new
research and should not be taken at this gate.*

### S2. Round 1's S2 (the one-sided IX.24 counter-pole) was fixed in the era doc and left standing in the IX.46 draft — and the doc's new wording misdescribes where it lives
**Location:** `CiC_Step0_Era10_Candidate_Entries_E.json` **line 406** (IX.46
`relationsSummary`); era doc §1 item 17 (lines 391–395).
**Ground truth:** the draft relationsSummary still reads
`"…counter-pole relation to IX.24 (Lausanne 1974 as the evangelical alternative
— both rows say so)…"`. Round 1's S2 fix said in terms: "and correct the IX.46
draft's relationsSummary at the same time." It was not corrected. I re-read
IX.24's census row in full: teaser, `why`, `floorNote` ("No question"),
`statusDescription` and `relationsSummary` ("The 1974 Congress …;
network-not-denomination shape; a Noll turning point previously missing")
contain no mention of the WCC, the ecumenical movement, or any counter-pole.
**The new era-doc text compounds it:** §1 item 17 now says the mutual claim was
"the mutual claim **earlier drafts of this doc** asserted" — locating the defect
in superseded revisions of the era doc, when it is live in the candidate JSON
this minute. A reader of the era doc would conclude the file is clean.
**Fix:** in JSON line 406 replace "— both rows say so" with "— proposed here;
IX.24's row gains the line only at adoption"; and in §1 item 17 replace "not
the mutual claim earlier drafts of this doc asserted" with "the draft's own
'both rows say so' corrected at Round 2 — the claim was never true of IX.24's
row."

### S3. Header correction (ii) now states a falsehood about the drafts file — the note it describes was rewritten two commits ago
**Location:** era doc lines 70–76.
**Doc:** "the candidate living flags are **17 true / 1 false (IX.34)** across
the eighteen drafts, not the drafts-file note's '15 true' — **and that note is
now stale twice over: written when there were seventeen drafts, it still reads
'17 drafts… 15 true' after IX.50's addition; the note was not retroactively
rewritten (the same convention slip (v) names)**…"
**Ground truth:** `CiC_Step0_Era10_Candidate_Entries_E.json`'s `note` field
today reads "**18 drafts**, drafted under the Living-Era Protocol Addendum
V1.0 … Living flags set per draft on the merits (the E9 R1-S6 practice):
**17 true**; IX.34 false…". It was rewritten in commit `cb387d5` ("reconcile
candidate-JSON note (17->18 drafts, 15->17 living) + fix receiver-draft
miscount in era doc") — the same commit that edited this era doc and left this
sentence untouched. Both halves of the doc's claim are false: the note does not
read "17 drafts… 15 true", and it *was* retroactively rewritten.
**Secondary problem inside the same sentence:** it invokes the standing
convention that research files are not retroactively edited to explain the
staleness — but the drafts file was edited, so either the convention does not
cover the drafts file (and the appeal is wrong) or the edit broke it. The gate
should not be asked to freeze either reading by accident.
**Fix:** rewrite (ii) to: "the candidate living flags are 17 true / 1 false
(IX.34) across the eighteen drafts — recomputed here from the JSON's own
fields; the drafts-file note (originally '17 drafts… 15 true') was reconciled
to '18 drafts… 17 true' after IX.50's addition, so the two now agree. The
drafts file is a drafting artifact, not a banked research file, and is
reconciled rather than left stale — unlike the research files named at (v)."

### S4. §4's IX.50 uniqueness claim is false: SIX drafts have neither a row-keyed nor an extra-topic base, not one
**Location:** era doc §4, lines 1030–1039 ("**IX.50 is the ONE draft of the
eighteen with neither a row-keyed base nor an extra-topic base of its own**").
**Ground truth (recomputed from `CiC_Step0_Era10_Sources_E.json` key-by-key):**
the 32 row keys are *exactly* the 32 era-10 census ids (IX.1–IX.32; no
candidate has a row key, by construction), and the 11 `extra--` keys map as:
X.1→IX.33/34/35 (6 items), X.2→IX.37 (3), X.3→IX.38 (3), X.4→IX.41/IX.42 (4),
X.5→IX.39 (4), X.6→IX.40 (3), X.7→IX.10 existing row (3), X.9→IX.36 (6),
X.10→MacArthur, no row (3), X.11→IX.48/IX.31 (5), X.12→IX.49 (4). Sum 44 ✓.
**Drafts with no base of any kind: IX.43, IX.44, IX.45, IX.46, IX.47 and
IX.50 — six.** Corroborating check: "World Council of Churches" / "Amsterdam
1948" appear **zero** times in `CiC_Step0_Era10_Sources_Research_E.md`, and the
file's own header (line 3) enumerates the extra topics it staged — the
completeness-find candidates are not among them.
**Why it matters:** the sentence is the doc's own honesty disclosure about
sourcing debt, and it makes IX.50 look uniquely unbased while five drafts
carrying **lead lean: adopt** — including IX.43 (a Tier-1 signal and a Frozen
VIII.1 write), IX.46 and IX.47 (both Frozen writes) — are in exactly the same
position. Two of them (IX.43, IX.47) are also on the all-[S] list at §3 B1, so
the run's weakest-sourced rows are precisely the ones this sentence exempts by
implication.
**Related, same fix:** §3 B1's "The THINNEST bases among the eighteen … IX.49
… and IX.38" no longer squares with §4 — IX.49 and IX.38 have staged bases (4
and 3 items); IX.50 and the five completeness drafts have none.
**Fix:** replace the §4 sentence with: "**SIX of the eighteen drafts have
neither a row-keyed base nor an extra-topic base of their own — IX.43, IX.44,
IX.45, IX.46, IX.47 and IX.50** — the five completeness/receiver finds because
the independent sources run staged only the E9-banked topics and Mark's
mid-run additions, and IX.50 because that run predates it entirely. All six
carry inline anchors only and all six enter the §4 queue owing a first
independent sourcing pass, not a deepening; IX.50 is distinguished only in
that its inline set is single-run *verified* rather than largely [S]." And in
§3 B1, scope the thinnest-bases sentence to "among the drafts with a staged
base."

### S5. IX.50's Section A finding — the fold-in's load-bearing judgment — rests entirely on [S] anchors, and nothing in the doc or the draft says so
**Location:** era doc §2, lines 712–752; draft `floorNote`, JSON line 521.
**Ground truth (§3g read against §3g's own marks):** the Section A finding
("no independent confession to test — coalition logic") stands on exactly three
evidentiary legs, and **all three are [S] in the survey's own text and in its
own [S] ledger**: (a) the founders'-circle composition — "three Catholics
(Weyrich, Viguerie, Dolan), a Jew (Phillips), and two fundamentalist Baptists
(Falwell, Billings) **[S — the founders'-circle composition]**"; (b) the
Falwell "coalition of moralists" quotation **[S]**; (c) Whitehead & Perry's
independence-of-scores finding **[S]**. The survey's own tally lists all three
among §3g's six [S] items. Meanwhile **none of the fifteen verified anchors
bears on Section A at all** — they are founding dates, media launch dates, book
imprints and death dates.
**Why it matters:** the era doc introduces this evidence as "the current's own
dated, own-voice founding record, not an opponent's characterization" and calls
the finding "the row's own hardest fact… carried in its copy, not softened."
Under R1 an A3/floor finding cites a **dated own-voice statement**, and where
the determination is unclear the finding is **recorded open with the gap named**
— the discipline this same document applies, correctly and at length, to PAW
and ALJC at §2 and Q5. The strongest single argument for Q12's branch (ii) is
therefore never put to Mark: the finding that makes the row unusual is the part
of the file with the weakest verification.
**Fix (executable from file):** add one sentence to §2's IX.50 paragraph — "All
three legs of this finding (the founders'-circle composition, the Falwell
quotation, and the independence-of-scores result) are **[S]** this session;
none of IX.50's fifteen verified anchors bears on Section A, so the finding is
recorded as a **provisional** Section A reading pending verification, the same
posture Q5 takes on ALJC" — and mark the three legs [S] in the draft floorNote,
with "recorded provisionally pending verification" added to its closing clause.
Then say so in Q12's lean, one clause.

### S6. Manufactured quotation in IX.50's draft floorNote: "a cultural framework… distinct from personal religiosity" appears in no research file
**Location:** `CiC_Step0_Era10_Candidate_Entries_E.json` **line 521** (IX.50
`floorNote`): "…its own most careful recent scholarly self-definition
(Whitehead & Perry, 2020) names it **'a cultural framework... distinct from
personal religiosity,'** not a doctrinal claim."
**Ground truth:** the string "distinct from personal religiosity" occurs
**nowhere** in any of the four research inputs (greped). What §3g actually
carries is two separate things: a quoted definition — "a cultural framework…
that idealizes and advocates a fusion of Christianity with American civic life"
— and a *separate*, [S]-flagged empirical finding, that Christian-nationalism
scores and personal-religiosity scores move independently. The draft splices
the two across an ellipsis and presents the result inside quotation marks as
Whitehead & Perry's definition. It is not a quotation of anything, and the [S]
mark is dropped in the splice.
This is the same defect class as Round 1's S3 (composition supplying a fact the
research never carried), one field further downstream, and it sits in the
floorNote that Q12 branch (i) would freeze.
**Note:** the era doc's own §2 prose handles this correctly — it quotes the real
definition and carries the independence finding separately and [S]-marked. The
defect is in the draft only, which is exactly why it survived the fold-in's
self-check.
**Fix:** rewrite the floorNote clause to "…names it 'a cultural framework… that
idealizes and advocates a fusion of Christianity with American civic life'
[S], with their own survey data showing Christian-nationalism and
personal-religiosity scores moving independently [S] — a sociological
description, not a doctrinal claim."

### S7. The B2 finding's calibration is anchored to a comparison that does not exist: IX.49's "hard case, argued in the draft" is an R7 finding, not a B2 assessment
**Location:** era doc §3 B2, lines 934–937 ("**Finding: thin but not empty —
B2 clears at the same Tier-3 strength as IX.49's 'hard case, argued in the
draft,' not at Tier-1 strength**"); restated at Q12 line 1362.
**Ground truth:** the quoted phrase is IX.49's **recency-marker** finding. Era
doc §1 item 6: "R7: the institutional wing passes, the digital wing does not —
**the marker's hard case, argued in the draft**." Survey §3f says the same and
runs **no Section B at all** on IX.49 — §3f is a shape-fork analysis. IX.49 is
mentioned in the era doc's B1 (thinnest base), B3 (vs IX.13) and B5 (instrument
gap) but **nowhere in B2**. So there is no IX.49 B2 assessment, at Tier-3
strength or any other, anywhere in the corpus to calibrate against.
**Why it matters:** this is the single load-bearing judgment of the whole
fold-in — Q12 turns on whether B2 is "thin but not empty" or disqualifying, and
the doc offers exactly one calibration anchor for "thin but not empty." A gate
reading it believes a comparable B2 case was assessed and cleared at Tier 3.
None was. The finding may still be right; it is simply uncalibrated, and the
doc should say so rather than borrow authority from a finding about a different
criterion.
**Fix:** replace with "**Finding: thin but not empty — B2 clears at Tier-3
strength, not Tier-1. There is no prior B2 case at this strength to calibrate
against (IX.49's 'hard case, argued in the draft' is its R7 marker finding, a
different criterion, and no B2 assessment of IX.49 exists on file), so the
finding is offered on its own reasoning: one dominant lens, with a real but
narrow origin-narrative/boundary-structure/formation-logic residue past bare
politics.**" Mirror the correction at Q12.

### S8. The verified-anchor tally the doc restates twice disagrees with its own enumeration by eleven
**Location:** era doc line 40 ("the survey run's verification tally **68 → 83
verified**") and line 55 ("83 anchors verified in-session… the survey's own
tally as reconciled"); source: survey line 212.
**Ground truth (arithmetic re-run):** the survey states "anchors **verified this
session via WebSearch: 83** (counted: the register/Oneness set 6; INC/Way/UC/
LLDM set 8; Davidian/Waco set 4; Rātana set 3; fundamentalism set 9; Social
Gospel set 4; mainline set 6; Georgia set 3; Malankara set 4; SDA set 3; AIC
set 7; ecumenical set 4; YRR/Mars Hill set 7; charismatic set 4; reconstruction
set 3; Girgis/Pyongyang/TJC/HKBP set 4; misc. 1 [within the AIC set]; §3g
Christian Right set 15)". The enumerated sets sum to **94** (95 if the misc
item is counted separately rather than as stated, "within the AIC set"). The
pre-fold-in version had the identical structure: headline **68**, enumeration
**79/80**. The reconciliation preserved the discrepancy exactly (+15 to both),
so it is inherited, not introduced by the fold-in.
**Second, smaller instance in the same ledger:** §3g's own 15-item enumeration
(restated verbatim in the era doc's B1, lines 858–862) omits "**Christian
Coalition founded 1989 by Pat Robertson**", which §3g's own convention
("Documented anchors, verified this session unless marked") makes verified and
which is bolded as such. So even the +15 is at least one short.
**Unverifiable-this-session, stated as such:** I cannot determine which figure
is correct without a full anchor-by-anchor recount of the survey's bolded
claims, which is on-file work but beyond this review's scope. What is verified
is that the two numbers in one sentence disagree, and that the era doc restates
the headline as established fact in the same block where it corrects five other
research-file slips on the record.
**Fix:** add a sixth not-inherited slip to the header's (i)–(v) list: "(vi) the
survey's verified-anchor headline (83) does not match the sum of its own
enumerated sets (94); the discrepancy predates §3g (68 vs 79/80) and is carried
here as a disclosed open ledger question rather than restated as settled — no
proposal in this document rests on the figure, and §3g's own set is at least
one short (Christian Coalition 1989 is verified by §3g's convention and absent
from its enumeration)." Then scope lines 40 and 55 to "the survey's stated
tally (disclosed as unreconciled at (vi))".

### S9. Round 1's S7 fix numbered IX.16 and excluded IX.17 by rule, but left IX.15 — an argued c2 disposition on a living row — unnumbered and unexplained, while numbering IX.26 whose census c2 is equally null
**Location:** era doc §2 lines 660–710; Q6 lines 1238–1241.
**Ground truth (census read):** `c2` values on the era-10 roster are
IX.4/IX.5/IX.7/IX.14 = `"question"`; IX.16/IX.17 = `"record"`; **IX.15 = null**;
**IX.26 = null**; all others null. The doc numbers six live applications —
IX.4 tenth, IX.5 eleventh, IX.7 twelfth, IX.14 thirteenth, **IX.26 fourteenth**,
IX.16 fifteenth — then excludes IX.17 with an explicit stated rule ("a closed,
dead movement's own historical texts… not a live test") and disposes of IX.15
with no rule at all: "**IX.15's deliberate c2:null** (argued above) completes
the register arithmetic."
**Why that is not sound:** IX.15 is living:true, and §2 runs a full c2 argument
on it ("no single founder — McAlister/Ewart/Cook/Haywood, multiple bodies from
the start, all outgrown; the disposition runs on A1 grounds alone"). Under the
Frozen E9 convention the doc invokes, numbering "counts cleared runs" and
includes runs that stayed open (E9 numbered VIII.18 seventh with its office-run
question open — E9 §2 line 358, header line 17). IX.26, whose c2 is null for the
same reason IX.15's is, *is* numbered. So the document numbers one argued
null-c2 living row and silently declines the other, at the one gate with no
successor gate to repair the count.
**Fix (one line, either direction):** either number IX.15 sixteenth (Q6 becomes
"tenth through sixteenth") with its clear-by-inapplicability stated as the
finding; **or** state the exclusion rule explicitly, e.g. "rows whose c2
disposition is that the criterion does not apply — no person-ground to test —
are recorded as register machinery and not numbered among live applications;
IX.15 and IX.26 are both such rows, and IX.26 is numbered only because its
office-question is a live test of the VIII.18 law." The second is the harder
one to write honestly, which is itself a reason to prefer the first.

---

## Minor findings

**M1.** *Q8's two 'formed' edges still cannot be written.* The validator
enforces `CONFIDENCE ∈ {Documented, Widely Accepted, Contested}` on **every**
edge (`validate-census.mjs`, edges block). Q8's lead lean says "adopt all
three, with IX.33↔IX.35 graded Documented and **the two VIII.3 'formed' edges'
grade left to Mark's call**" — so "apply recommendations" writes two edges the
validator rejects. Round 1's N1 asked for three stated grades; the revision
substituted an honest gap-naming, which is better than a guess but still not
executable. Fix from grounding on file: propose **Documented** for both, on the
basis the doc already relies on elsewhere — Frozen VIII.3's own `dateRationale`
names the verified 1906 census listing that records the separation of the two
wings — with the note dated per R3(iv); keep "Mark may re-grade" as the
fallback rather than as the lean.

**M2.** *Wrong cross-reference at §3 B1, line 906.* "Divine Principle's
English-translation year… — corrected in **§1 item 4** above." §1 item 4 is
IX.36 (New Calvinism); the Divine Principle divergence is carried in §2's IX.16
bullet (lines 530–535). Fix: "corrected in §2's IX.16 per-body bullet above."
(All six other "§1 item N" references check out — see clean check 16.)

**M3.** *IX.50's draft `relationsSummary` is a review memo in a
participant-facing field.* It runs **1,956 characters** — 3.2× the longest
`relationsSummary` anywhere in the 257-row census (605) and 2.4× the longest of
the other seventeen drafts (IX.35, 806) — and it is the only field in the whole
drafts file carrying criteria machinery into census prose: "B2 ecology honestly
thin", "Tier-3 B2 strength, not Tier-1", "this row's B1 strength", "the IX.32…
carrier-device parallel, argued not asserted". No other draft's
`relationsSummary` mentions B1–B5 or a tier. Fix: move the B1/B2/tier
reasoning to the `why` field (where method language is conventional across the
file) and cut the relationsSummary to the dated carrier line plus the
differentiation, keeping the B2-thinness disclosure in one plain
participant-facing clause — which is what Q12 branch (i) actually promises
("B2's thinness written into the row's OWN participant-facing copy").

**M4.** *The IX.50→IX.24 disclosure line rides in every branch but its words
exist nowhere.* Q12 states the line "is a copy line on IX.24's EXISTING era-10
record: era-10-internal, written at this Freeze", and that the relations lines
"ride REGARDLESS of the row's fate" — so both branches write copy onto a census
row, and no draft of that copy exists in the era doc, the survey, or the JSON.
Contrast Q10, which drafts the IX.20 replacement text verbatim. Note also the
asymmetry: Q12 spells out what the IX.33 line becomes on branch (ii) ("a named
disclosure inside IX.33's copy") and says nothing about what the IX.24 line
becomes. Fix: draft the IX.24 clause in Q12 (one sentence, e.g. "the American
Christian Right's political mobilisation (1979– ) draws heavily on this
movement's American wing, while this row's own record stays
global-congress-shaped — disclosure, not identity"), and state its branch-(ii)
form.

**M5.** *R9 is mis-cited, twice, for the Fox News scope limit.* §1 item 7:
"R9 also binds: Fox News's current programming is outside this survey's scope";
Q12 line 1397: "R9 keeps Fox News's current programming out of scope entirely."
R9 is **published-sources-only / no outreach** ("the run performs no outreach…
A question only the body itself could answer is recorded as open, not asked").
Nothing about Fox News's current programming requires outreach — it is
published. The rules that actually govern are R3 (present-state claims take
CD/CR, never the classical ladder) and R4 (present-tense humility). The doc
uses R9 correctly elsewhere (ZCC, ALJC), so this is a citation slip on the
newest material. Fix: cite "R3/R4" in both places.

**M6.** *The structural headline's receiver arithmetic doesn't match its own
premise.* §1 lines 108–113: "the E9 gate seated the big-church receivers to
1906 (**VIII.28–VIII.31**) and era 10 orphans them again — answered here by five
receiver-class drafts (IX.43, IX.46, IX.47, and the two IX.37/IX.38 banked
segments)". Census read: the five drafts receive VIII.1, VIII.25, VIII.26,
VIII.27 and VIII.29 — **only IX.47 receives a VIII.28–31 row**. VIII.28
(Orthodoxy after 1821), VIII.30 (Victorian Church of England) and VIII.31
(Russian Synodal Century) stay unreceived at the census's last era gate, with
no continuesAs and no draft. The count "five" is right; the claim that it
answers the VIII.28–31 orphaning is not. Fix: "…answered only in part — IX.47
receives VIII.29, and VIII.28, VIII.30 and VIII.31 remain unreceived at the
last gate (the strongest argument for the named-not-drafted 20th-century
Anglicanism and post-Soviet Orthodox flags); the run's other four
receiver-class drafts answer VIII.1, VIII.25, VIII.26 and VIII.27 instead."

**M7.** *The row's own start anchor carries an undisclosed within-file
divergence.* The doc consistently treats Moral Majority's 6 Jun 1979 founding
as **[S]** (§1 item 7, §3 B1(b), §5, and the draft's own fields) — the
conservative reading, and the right one. But §3g **bolds** "6 June 1979" under
a preamble reading "verified this session unless marked", with its [S] bracket
scoped explicitly to "the exact founder list beyond Falwell", while §3g's own
[S] ledger lists "Moral Majority's exact founding date/founder list". The
survey is internally divided about the row's start anchor and the doc's
four-case divergence-disclosure paragraph (§3 B1) does not include it. Fix: add
it as a fifth case in that paragraph, one clause, noting the doc takes the
conservative reading.

**M8.** *The c2 numbering violates its own stated ordering rule.* §2 line 661:
"[numbering proposed per the E9 cleared-runs-count convention, **document
order**…]". In §2's own document order IX.16 (line 515) precedes IX.26 (line
567), but IX.26 is numbered fourteenth and IX.16 fifteenth — an artifact of
Round 1's S7 fix appending IX.16 to the end of the c2 list. Fix: swap the
ordinals (IX.16 fourteenth, IX.26 fifteenth) or scope the rule to "the order of
this list."

**M9.** *B3 overstates IX.24's global framing against the doc's own Q10 item.*
§3 B3 lines 960–964: IX.24's "own census record is framed globally
**throughout** (region 'Global'; …; network-not-denomination)". IX.24's
`regions[]` array reads `["North America","North Europe"]` — the mismatch this
same document proposes to fix at Q10. "Throughout" is false as written and, more
usefully, the contrast is *stronger* once Q10's fix lands. Fix: "framed globally
in its region field, teaser and relations line (its `regions[]` array is the
coding mismatch Q10 fixes)".

## Cosmetic

- **C1.** Header line 59 says the 211 items span "the 32 rows and **twelve**
  extra topics"; §4 line 1018 says "32 worlds + **11** extra-topic keys". Both
  are defensible (twelve topics staged, X.8 discharged with zero items) but they
  are never reconciled in the same place. One clause at line 59: "eleven
  extra-topic keys across twelve staged topics (X.8 discharged at IX.19)".
- **C2.** "§2c" (line 251) and "§2c/§3e" (lines 737, 1371) are **survey**
  sections; this document has no §2c and no §3e, so the references read as
  phantom era-doc subsections. Fix: "survey §3e" (the reconstruction mandate;
  survey §2c is R7/IX.31, and is the wrong pointer for the reconstruction
  disposition at line 251).
- **C3.** §3 B1 characterises the Mars Hill 1996 case as "a mark error, the
  wrong direction" in this document only. It is in fact a genuine cross-run
  divergence of the same shape as the T4G case, in the opposite direction: the
  survey holds "Mars Hill Church (Seattle, 1996 [S])" while the sources run
  verified it (X.9, "all verified this session"). One clause restores the
  symmetry.

---

## Clean checks defended (independently recomputed — do not "fix" these)

1. **Thirteen of Round 1's fifteen substantive findings landed clean at their
   deciding sites.** S1: the all-[S] roster is exactly right — I recomputed
   "verified"-marked anchors across all eighteen drafts' fields and got zero for
   **IX.38, IX.41, IX.42, IX.43, IX.47** and non-zero for all others, with
   IX.41's inherited-from-VIII.3 credit correctly stated. S4: pre-1906 starts
   among era-10 rows recomputed = IX.2 (1904), IX.4 (1900), IX.20 (1900),
   IX.29 (1875) — **four**, with IX.4's both-branch crossing correctly argued.
   S5: the landing split is right (below). S6: verified against the survey —
   PAW's only staged item is an undated "current Minute Book / statement of
   faith [S]" and ALJC has only "(1952 merger [S])"; the revision names both
   gaps without overcorrecting into a claim that no PAW material exists (the
   sources base's Haywood/PAW *records* are correctly not counted as a current
   statement). S8: Q7's ratify-or-correct now carries a three-sentence merits
   argument in §5 with a stated lean and the Optina cross-reference. N1 (see
   M1), N2 (IX.20 now explicitly BANKED, not written), N3 (the Harrist/Aladura
   counter-note claim is now the honest negative — confirmed: no counter-note
   for either family exists in any research file), N4 (the R6 sentence is
   scoped to existing rows' date strings, with IX.34's legal window named),
   N5 (three divergence cases added), N6 (scale claims), N7 (flag 12), C1–C3
   all applied. **The two that did not land are S1 and S2 above.**
2. **Census untouched and legal.** `validate-census.mjs` on the live file:
   257 movements, 21 edges, 10 eras, **0 errors, 0 warnings**. Last commit
   touching `world-census.json` predates this branch's era-10 work entirely.
   Working tree clean before this review's own commit.
3. **All eighteen drafts re-validated against the 257-row census with IX.50
   included:** zero `id` collisions, zero `atlasId` collisions, every
   `shortName` ≤ 20 chars (IX.50 = "Christian Right", 15), every `start ≤ end`,
   every `era` = 10, every draft's **key set identical** to the others (IX.50
   included — no schema drift), and every `lane` string already present in the
   census. The doc's §1 claim to this effect is true as stated.
4. **The 211-item landing arithmetic is exactly as §4 and Q11 now state it:**
   32 row keys (= precisely the 32 era-10 census ids) carrying **167** items,
   11 `extra--` keys carrying **44**, total **211**; X.10's MacArthur base is
   **3** items as claimed; X.8 carries zero by design. Round 1's S5 fix is
   sound and consistently phrased in both places.
5. **Every dated anchor the era doc restates from §3g traces to §3g verbatim**
   — I checked all eleven claim clusters: the 21 Aug 1980 Dallas briefing and
   the full Reagan quotation word-for-word; the platform roster (Falwell,
   Robertson, Robison; Criswell presiding); Moral Majority 6 Jun 1979 and its
   1989 dissolution with Falwell's own framing; Christian Coalition 1989 /
   Robertson / Reed as founding executive director; FFC 14 May 2009; Limbaugh
   1 Aug 1988 (ABC Radio, 56 stations); Fox News 7 Oct 1996; the six-item
   naming wave with correct publishers and years (Oxford UP 2020, Liveright
   2020, Bloomsbury 2020, Princeton UP 2019, Routledge 2020, BJC/FFRF 9 Feb
   2022); the three death dates. **The manufactured-fact hunt on §1 item 7's
   anchor list came up empty** — the one manufactured item in the fold-in is in
   the draft floorNote (S6), not in the era doc's prose.
6. **B1(a)'s single-run disclosure is TRUE and is the fold-in's best piece of
   self-criticism:** "Moral Majority", "Falwell", "Limbaugh" and "Christian
   nationalis*" occur **zero** times in `CiC_Step0_Era10_Sources_Research_E.md`
   and zero times in `CiC_Step0_Era10_Sources_E.json`. IX.50 genuinely has no
   cross-run corroboration and the doc says so unprompted.
7. **The B5 scale sweep is complete.** I re-swept all eighteen drafts for
   present-state scale language: the only unclassed claims are IX.37's "among
   the largest Lutheran bodies on earth" and IX.38's "Mizoram and Nagaland
   among the most Christian regions on earth [S]" — the two the doc names —
   plus IX.50's region/scale material. IX.44's "~22 million" is already
   correctly classed ("[S — the church's own count; CR until an independent
   counter is named]"). No missed CD/CR case; "three" is right.
8. **The eleven-row living/end mismatch sweep is complete and correctly
   classified against the census.** Era-10 rows with a non-boundary end:
   IX.1 (1920), IX.2 (1910), IX.3 (1970), IX.8 (1990), IX.9 (1970), IX.12
   (1991), IX.15 (1993), IX.21 (1989), IX.22 (1991), IX.28 (2015) — plus
   IX.17's living:false/2026 inverse = eleven; IX.6 (1945) correctly excluded
   as dead. 3(a) + 6(b) + 2(c) = 11 ✓, and the set matches the addendum §1's
   own "IX.15, IX.17, IX.28 at minimum + the eight enumerated" exactly.
9. **Every other count recomputed and correct:** tiers 7+18+2+5 = 32 with all
   32 ids present once; 257+17 = 274 and 257+18 = 275; the §4 queue
   5+11+10+9+12+24+**18** across seven eras correctly extends Frozen E9's
   six-era "5+11+10+9+12+24" (read in E9 §4); E9's c2 numbering (VIII.10 sixth,
   VIII.18 seventh, VIII.8 eighth, VIII.23 ninth) confirmed in the Frozen text,
   so tenth-next is right; the candidate-side straddle count "two of eighteen"
   is right (IX.34's 1886, IX.35's 1900; IX.50's 1979 nowhere near 1906); the
   +15/+6 §3g deltas match the survey's own reconciled figures (the separate
   question of whether *those* figures are internally consistent is S8).
10. **Frozen-write legality unchanged and IX.50 adds nothing to it.** The
    fold-in proposes no `continuesAs`, no edge, and touches no Frozen row in
    any branch — verified against Q7's list and Q8's 21→24 count, both of which
    are correctly stated as unmoved. IX.24 **is** an era-10 row (census `era:
    10`), so Q12's classification of the IX.50→IX.24 disclosure as
    era-10-internal rather than a Frozen-record write is **correct**. The
    misclassified-write hunt on the new material is empty.
11. **R10 self-hunt re-run on the fold-in material.** *Classical grades on
    present-state claims:* the word "Documented" now appears three times — twice
    as the IX.33↔IX.35 edge grade on the **dated rupture texts** (legal, and
    exactly R3(iv)'s named case) and once as §3g's inherited heading phrase
    "Documented anchors" over dated past events (legal per R3(i)). No
    present-state claim carries a classical grade anywhere. *Verdicts on
    people:* Falwell Sr., Robertson and Limbaugh are carried on dated death
    dates and organizational record only; Reed is named only through dated
    organizational acts; the Driscoll rule is applied identically, as claimed.
    *Obituaries:* IX.50 is `living: true` with end 2026; Moral Majority's 1989
    dissolution is a dated organizational fact, not a movement end. *Interior
    windows:* none proposed for IX.50; R6 holds. *Safety clause:* the fold-in
    touches neither IX.5 nor IX.31 and identifies no non-public person or
    community.
12. **The Section A finding's *reasoning* is faithfully carried from §3g** —
    both the against-independent-standing case and the "Section A may be the
    wrong test" counter-case are reproduced without softening, additions or
    drift, including the survey's own admission that the carrier-device reading
    would move the whole test to Section B. The defect is the [S] status of its
    evidence (S5), not the argument.
13. **The B2 argument is likewise faithful to §3g on both sides** — the
    one-lens critique, the origin/memory narrative, the boundary structures and
    Du Mez's formation-logic thesis all appear as §3g states them, and the doc
    adds a genuinely useful separation §3g lacked ("uniqueness establishes that
    nothing else covers this shape; it does not establish that the shape is a
    formation world"). The defect is the false comparator (S7), not the
    reasoning.
14. **The pre-adoption drift hunt came up EMPTY.** Every figure that would move
    on IX.50's adoption is stated conditionally: Q3 splits 274/275 and
    explicitly refuses to fold IX.50 into its lean; the tier tally says it is
    "unmoved by IX.50"; the straddle count "stays two of eighteen, recounted
    rather than assumed"; §4's queue names IX.50's zero-base condition rather
    than smoothing it; the forward-flags block carries the branch-(ii)
    contingency; and Q10 deliberately keeps the IX.50→IX.24 line out of the
    prose-sweep question "so that a yes to the prose sweep cannot implicitly
    rule on IX.50." Mark's "let the step 0 process define everything" is
    honoured structurally, not just rhetorically.
15. **The strawman hunt also came up EMPTY.** Branch (ii) is given §3g's own
    "the more conservative reading" language, an explicit statement that it
    "costs nothing sourcing-wise", the reconstruction analogy *and* a stated
    account of where that analogy breaks down in branch (ii)'s disfavour, plus
    "a defensible weighing, not an error" and "the gate should feel free to take
    it without argument." Q12 states B2's thinness before B4's strength and says
    why. This is a gate question a reasonable Mark can decline on the record.
16. **Renumbering damage is limited to one reference.** §1's items run 1–18
    sequentially with no gaps or duplicates. All seven "§1 item N" cross-
    references resolve correctly except line 906 (M2): item 4 = IX.36 (cited
    correctly at lines 899 and 1213), item 7 = IX.50 (lines 232, 1333), item 8
    = IX.37 (line 1003), item 9 = IX.38 (line 1001).
17. **The fold-in's two self-flagged items are real and correctly flagged** —
    the sources base predating IX.50 (§4) and the [S] start anchor (§5). Both
    are honest and both are on file. They are not the ones that needed catching:
    S4, S5, S6 and S7 are all in material the fold-in reported as settled.
18. **Q1's addendum fold is still faithful** — six sub-questions, same grouping,
    leans unchanged (freeze + adopt ×5) against the addendum's own §5; the
    addendum's header's "two review rounds, all findings applied" is accurate.
    The addendum's own R1 composite/culture/label rosters match the doc's use of
    them (the doc's addition of IX.26 to the composite list is argued on the
    row's own unnamed "& Pacific Adjustment Movements" tail, not attributed to
    the addendum).
19. **Gate decidability elsewhere is intact.** Q1–Q7 and Q9–Q12 each carry a
    stated lean that resolves to one application, Q12 included (branch (i), with
    the weakest lean in the document, argued on the merits). The only
    lean-execution gap is M1's two ungraded edges inside Q8.

— End of Round 2. Nine substantial findings; two of them (S1, S2) are Round 1
fixes that landed in prose but not in the data, and those two are the ones that
would put manufactured and false content into the census if the gate says yes.
All fixes are executable from grounding already on file; only S1's *alternative*
branch (staging the WCC Basis in a sources base) would need new research, and
that branch should not be taken at this gate. REVISE, then the package is
gate-ready.
