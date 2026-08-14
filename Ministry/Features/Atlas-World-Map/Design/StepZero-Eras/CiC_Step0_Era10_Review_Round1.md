# A1.E10 Review Round 1 — adversarial review of `CiC_Step0_Era10_V1_0.md` + drafts

Reviewer: adversarial review agent · 2026-08-14 · Method: independent recomputation
against `world-census.json` (257 movements, 21 edges — validator re-run 0/0),
`CiC_Step0_Era10_Survey_Research_E.md`, `CiC_Step0_Era10_Sources_Research_E.md`
+ both JSONs (17 drafts; 211 source items re-counted in node), the Frozen
`CiC_Step0_Era9_V1_0.md` (GATE OUTCOME header, §2 runs, §5 register-cap ruling,
§6 writes, forward flags), the Living-Era Protocol Addendum V1.0 (R1–R10; its
own R10 charge executed against this document's text), the Criteria Relook,
`validate-census.mjs` (read, and run), and the HANDOFF discipline block. Every
count re-run; every quoted census and Frozen-record claim read in the file;
every candidate JSON field greped. Object commit `6a58e5d` adds only the era
doc; the census is untouched since the E9 Freeze.

## VERDICT: GATE-ELIGIBLE AFTER FIXES (REVISE) — 8 substantial (S1–S8), 7 minor (N1–N7), 3 cosmetic

None of the eight breaks the era's architecture, and the highest-value hunt
classes came up empty (no validator-illegal write anywhere in Q7 — every
proposed continuesAs is era-gap 0/1 with no successor-starts-early warning; no
classical grade on any present-state claim — zero hits for the ladder
vocabulary in the whole document; no undated-people verdict; no speculative
end). But three of the eight would freeze false statements of record (S1, S2,
S4), one manufactures a fact the research never carried (S3), one would
mis-execute the Freeze's largest mechanical write (S5), and one leaves the last
gate's one Frozen-adjacent ratification item undecidable (S8). All are fixable
from grounding already on file. The clean-checks list at the end states what
was verified sound so the revision does not touch what isn't broken.

---

## Substantial findings

### S1. §3 B1's all-[S] disclosure is false: FIVE drafts carry zero verified-this-session anchors, not none
**Doc (§3 B1):** "All-[S]-anchored candidates (zero verified anchors this
session), said plainly: NONE — every draft carries at least one verified
anchor; the THINNEST bases are IX.49 … and IX.38 …"
**Ground truth (JSON greped, survey tally recomputed):** the survey's own
verification ledger has no Stone-Campbell, no Black-Church, and no
Catholic-segment verified set, and the candidate file confirms it: **IX.38,
IX.41, IX.42, IX.43, and IX.47** contain not one "verified" anchor in any
field — every anchor is [S] (IX.43's §1 item 13 list is itself all-[S] in the
doc's own text: Great Migration [S], COGIC 1907 [S], 1915 split [S], SCLC 1957
[S], Cone 1969–70 [S]; IX.47's base is Lamentabili/Pascendi/oath/DAS/nouvelle
théologie [all S]). IX.41's start anchor (the 1906 census listing) IS verified
— but at the **E9 session**, inside Frozen VIII.3's dateRationale, not "this
session," and the doc's own sentence excludes inherited verification by its
wording. This is the E9-R1-S3 defect exactly (the incomplete all-[S] roster),
on the disclosure Mark uses to judge sourcing weakness before adopting 17 rows.
**Fix:** name the five (IX.38, IX.41, IX.42, IX.43, IX.47) as
zero-verified-this-session; credit IX.41's Frozen-inherited 1906 anchor as
inherited, explicitly; keep the thinnest-bases framing (IX.49/IX.38) — it is
true and useful — under the corrected roster.

### S2. False census-content claim: "counter-pole relation to IX.24 (both rows say so)" — IX.24's row says no such thing
**Doc (§1 item 16, IX.46):** "counter-pole relation to IX.24 (both rows say
so)."
**Ground truth (census IX.24 read in full):** IX.24's teaser, why,
floorNote ("No question"), statusDescription, and relationsSummary ("The 1974
Congress …; network-not-denomination shape; a Noll turning point previously
missing") contain **no mention of the WCC, the ecumenical movement, or any
counter-pole**. Only the IX.46 *draft* says so; the survey's G4 proposed the
relation without the both-rows claim ("Lausanne's 1974 counter-pole (relation
to IX.24)"). The doc inherited the draft's embellishment and asserts census
content that does not exist — directly against its own header claim that
"every claim below about a row was read against the row."
**Fix:** "counter-pole relation to IX.24 proposed (the IX.46 draft says so;
IX.24's row gains the line at adoption)" — and correct the IX.46 draft's
relationsSummary at the same time.

### S3. Manufactured fact: the WCC "1948/1961 trinitarian Basis" appears in no research input
**Doc (§1 item 16, IX.46):** "A council of churches, not a confession-bearing
body — its 1948/1961 trinitarian Basis [S] cited as the institution's dated
text, member confessions only ever per body."
**Ground truth (all four research inputs greped):** neither research file nor
either JSON anywhere mentions the WCC Basis, 1948 or 1961 — the only "basis"
in the corpus is the UMJC's doctrinal basis (IX.13). The sources base stages
the IMC/Amsterdam/New Delhi event cluster and the Lausanne covenant series;
the survey's G4 likewise. The era doc has supplied, from nowhere, the dated
own-voice text on which IX.46's A3 posture runs — the manufactured-fact class
(composition adds structure and leans, never facts; E8-S12's ungrounded-hinge
shape). The claim is historically real, which is exactly why it must enter
through a research base, flagged, not through composition.
**Fix:** either strike the Basis clause (the council-of-churches point stands
on the member-confessions-per-body rule alone) or add the Basis to the sources
base as a named [S] item first and cite it from there.

### S4. Straddle-sweep start-side recount fails: FOUR existing rows start pre-1906, not three — IX.4's recorded 1900 is missed
**Doc (§5 straddle sweep):** "Start side — pre-1906 starts among existing
rows: THREE (IX.2's 1904 …; IX.20's 1900 …; IX.29's 1875 …); candidate-side:
TWO drafted … plus ONE conditional (IX.4 under fork (i))."
**Ground truth (recomputed over all 32 era-10 rows):** starts strictly before
1906 are IX.2 (1904), **IX.4 (1900, "1900s–present")**, IX.20 (1900), IX.29
(1875) — four. The doc's own §5 table states IX.4's Current as "'1900s–present'
/ 1900" three rows up, then the sweep drops it from the existing-rows count
and misfiles it as a *conditional* crossing that exists only "under fork (i)."
The fork (1880s vs keep-1900) changes the crossing's depth, not its existence:
IX.4 crosses 1906 on EITHER branch. This is the E8-S1 asserted-not-computed
sweep defect, in the paragraph headlined "arithmetic, from the survey,
corrected against the census."
**Fix:** recount to four with IX.4 in the existing-rows list (both-branch
crossing noted); the conditional slot then describes only the 1880s deepening.

### S5. §4↔Q11: "the 211-item sources[] landing on this era's 32 rows" cannot execute — only 167 items are row-keyed
**Doc (§4):** "The 211-item base … lands as sources[] on this era's 32
existing entries at the Freeze, per the standing pattern." **(Q11):** "Confirm
the 211-item sources[] landing on this era's 32 rows at the Freeze …"
**Ground truth (JSON recomputed):** 211 = **167 items keyed to the 32 census
ids + 44 items keyed to the 11 `extra--` topic keys** (X.1–X.12, X.8 zero by
design) — the doc's own §4 parenthetical says so ("167 row items + 44 extra
items") and then both landing statements say 211 anyway. The 44 cannot land on
the 32 rows: they belong to the cluster candidates (X.1→IX.33–35), the banked
segments (X.2/X.3), other drafts (X.4/X.5/X.6/X.9/X.12), a world with **no row
at all even on full adoption** (X.10 MacArthur), and pathway material split
across rows (X.11) — and §4's own next sentence routes candidate bases to the
follow-up queue, not to sources[]. The Frozen E9 pattern being invoked ("the
149-item sources[] landed") was all-row-items; the transfer is wrong, and a
literal "yes" to Q11 either mis-lands 44 items or leaves the executor
inventing the split.
**Fix:** both sentences become "the 167 row items land on the 32 rows; the 44
extra-topic items ride their candidates (inline anchors now, full bases via
the §4 queue), with X.10's base banked to the MacArthur forward flag" — one
clause, stated in §4 and Q11 identically.

### S6. The IX.15 disposition overclaims its own textual base: "each with its current statement identified" is untrue for PAW and ALJC
**Doc (§2):** "Named bodies, each with its current statement identified:
UPCI (… verified as the annually-dated own-voice statement this disposition
needs …); PAW (the oldest body, Oneness from 1916 [S], historically
interracial …); ALJC (1952 merger [S]) …" **(Q5):** "per-body at
own-confession strength on the named bodies' dated texts."
**Ground truth:** the doc names **no PAW text at all** (the survey stages
"current Minute Book / statement of faith [S]" — undated; the sources base's
IX.15 items carry UPCI, the 1913–16 origin layer, and Haywood/PAW *records*,
no dated current statement) and **no ALJC text exists in any input** — the
survey gives ALJC only "(1952 merger [S])." So Q5 proposes a per-body
disposition "on the named bodies' dated texts" when dated texts are staged for
one body of the named five (UPCI, by Manual year — whose own [S]-wording debt
the doc discloses honestly). Under the addendum this is R1/R4 territory (a
per-body A3 finding cites a dated own-voice statement; where unclear, the
finding is recorded open), and it is the E8-S5 shape: the era's ONE
record-mandated disposition proposed on a citation base narrower than its
description claims. Mark would freeze believing five bodies' statements are
staged; two are not.
**Fix:** per-body honesty in §2 and Q5 — UPCI as staged; PAW: name the Minute
Book/statement [S, year unpinned — the citation owed before the finding
lands]; ALJC: no current statement staged, the sub-finding recorded open with
the gap named (the R9 pattern the doc already uses for ZCC).

### S7. c2 numbering scope: the IX.16 per-body run (and IX.17's record staging) sit outside "tenth through fourteenth," unnumbered and unexplained
**Doc (§2/Q6):** "the criterion's TENTH through FOURTEENTH live applications
[numbering proposed per the E9 cleared-runs-count convention …]" — numbering
IX.4, IX.5, IX.7, IX.14, IX.26; then "IX.15's deliberate c2:null … and IX.16's
per-body 'record' findings (both limbs stated per body …) complete the
register arithmetic."
**Ground truth:** the Frozen E9 convention counts every application performed
at a gate, light clears included ("VIII.10 sixth, VIII.18 seventh, VIII.8
eighth, VIII.23 ninth, per the program's cleared-runs-count numbering" — so
tenth is correctly next). But this gate also *performs and records* c2
analysis on IX.16 — four bodies, both limbs argued per body, findings routed
to Mark via Q5 — which is one entry-level application by the doc's own
per-body counting rule, and stages IX.17's c2-"record" evidence besides. The
doc explicitly de-counts the VIII.10 completion ("not a new run — its numbered
case exists") but says nothing about IX.16/IX.17, leaving the Frozen count
contestable — the E9-R1-S5 defect recurring at the census's LAST gate, where
no later era can repair the count.
**Fix:** either number IX.16 (and IX.17 if its staging is held to be a run) in
document order, or state the exclusion convention in one line (e.g. "rows
whose c2 value predates any gate and is not changed here are analyzed as
register machinery, not counted as runs") — said on purpose, so the frozen
count is closed either way.

### S8. Q7's VIII.11→IX.22 "ratify or correct" carries no lean and no merits argument — undecidable under the discipline block
**Doc (Q7):** "the VIII.11→IX.22 continuesAs FOUND IN THE FILE but unlisted
in the Frozen E9 record's writes — ratify or correct (the VIII.13→IX.10
ratification pattern; the sweep found no other unrecorded writes)."
**Ground truth:** the find itself is verified TRUE (the write is in the file;
the Frozen E9 Q6 lists VIII.13→IX.10 + the twelve era-8 writes + VIII.49→IX.20
and nothing else; the full continuesAs sweep into era 10 = exactly four
writes). But "ratify or correct" is a genuine either/or, and the doc argues
neither side and states no lean — while its own Q10 carries the directly
relevant evidence (the sources register's Optina-genealogy nuance: IX.9's
line says "the Optina tradition scattered by revolution," i.e. the file
carries TWO different claims about where Optina's lane goes) without ever
connecting the two items. HANDOFF discipline: "items with no stated lean stay
open; gate packages state leans so 'apply recommendations' works as a ruling"
— on a "yes to all," this Frozen-adjacent item alone stays unresolved, at the
one gate with no successor gate to catch it. (Citing "the VIII.13→IX.10
ratification pattern" gestures at ratify but is not a stated lean.)
**Fix:** argue it in §2 or §5 in three sentences (identity case: New Martyrs
as the lane's next episode, VIII.11 end 1906 → IX.22 start 1917, the write is
validator-legal; counter-case: the Optina thread's Paris-School half), state a
lean, and cross-reference the Q10 Optina-nuance line.

---

## Minor findings

**N1.** Q8's three proposed edges carry no confidence grade anywhere in the
doc, and the validator requires one per edge (`CONFIDENCE` set enforced). The
survey staged the IX.33↔IX.35 grade ("Documented on its dated texts, per
R3(iv)"); the two VIII.3 'formed' edges have no grade in any input. State the
three proposed grades in Q8 so "adopt all three" is executable.

**N2.** Q10 bundles the IX.20 stale-line replacement into a question whose
Freeze "applies words," while the item itself says "Frozen-adjacent, Mark's,
whenever the row is next opened." Say which it is: does a yes to Q10 write
IX.20's line now, or bank the drafted text? (The E9 flag's language supports
either; the ambiguity supports neither.)

**N3.** §2/Q6(a): "Harrist/Aladura … likely-clear on the community limb [lead
lean], counter-notes named" — no counter-notes for these two families exist in
the doc or either research file (contrast IX.5's CRI note, which is real).
Name one (e.g. the transmission-tier constraint on Harris's unwritten
teaching) or drop the clause — a two-word assertion of analysis that isn't
there (E8-S9's small sibling).

**N4.** §5: "No interior gravity window is proposed anywhere in this run — R6
held" — the IX.34 draft's relationsSummary carries "gravity window 1907–1918
(Christianity and the Social Crisis to Rauschenbusch's death, verified)." The
window is R6-LEGAL (both anchors verified this session), so the discipline
held; the blanket sentence is still false as written. Scope it ("no interior
window on any existing row's date string") or name IX.34's window as the
verified-anchor exception.

**N5.** The verification-divergence disclosure rule is applied to three cases
(Georgia 1990, Girgis 1918, Malankara "across the two research runs") and
skipped for three of the same shape: T4G first conference 2006
(survey-verified, sources-[S] "not confirmed this session"); Mars Hill 1996
(doc says "[S-start]" though sources X.9 verified it — wrong direction,
harmless, still a mark error); Divine Principle ET year (survey 1996 vs
sources 1973, doc silently picks 1996 [S]). One disclosure sentence covers all
three.

**N6.** Present-state scale claims ride participant-facing draft fields with
no CD/CR class: IX.38's "Mizoram and Nagaland among the most Christian regions
on earth [S]" (restated in §1 item 8) and IX.37's "among the largest Lutheran
bodies on earth." The doc's own B5/CD-CR register is the instrument — class
them (census-data claims are CD-eligible with the counter named) or recast as
dated fact.

**N7.** E9 forward flag 12 (Syriac resumption at IX.19) is dispositioned only
implicitly: the header claims all twelve dispositioned, and Q10 carries the
Assyrian-wing scope note, but the flag's actual disposition
("confirmed standing — the row is the resumption exactly as ruled," survey) is
nowhere stated, and the survey's "no action beyond the era doc carrying the
E9 named-gap disclosure forward" is not performed. One line in §1's
declined/routed list closes it.

## Cosmetic

- **C1.** The sources research header says "233-movement census"; the census
  was 257 at run time (the survey confirms 257). The banked file stays as-is
  per convention, but the doc's header corrections list (i)–(iv) should carry
  this as a fifth noted-not-inherited slip, one clause.
- **C2.** §1 item 1: "annual 1876–1897" drops the survey's "1875/1876–1897"
  variant on the Niagara conferences' first year.
- **C3.** §2 IX.15: "descends from the same 1914 Mexican Apostolic milieu"
  drops the survey's [S] on the 1914 milieu date.

---

## Clean checks defended (all independently recomputed — do not "fix" these)

1. **All four header corrections verified TRUE**: era-10 living is 30 of 32
   (only IX.6, IX.17 false — the survey's "29" was its own arithmetic slip);
   candidate living flags are 16 true / 1 false (IX.34) against the JSON note's
   "15 true"; Frozen VIII.32 ends **1906** in the census (the survey's "ends
   1915 — seamless" was wrong; the doc's nine-year-seam correction and the Q7
   no-write disposition are exactly right); the TGC 2004/2005/2007 resolution
   matches the sources register item 8 verbatim.
2. **Every proposed census write is validator-legal** (rule read in
   `validate-census.mjs`: era gap 0 or 1, successor-start warning): VIII.26→
   IX.37 (1861→1906, seamless), VIII.27→IX.38, VIII.1→IX.43, VIII.25→IX.46
   (1920→1921), IX.9→IX.48 (same-era, 1970 handoff), the VIII.29 re-point both
   legs (VIII.29→IX.47 at 1906; IX.47→IX.23 seamless at 1962), VIII.11→IX.22
   (1821→1917). No adjacency violation, no start inversion, anywhere — the
   E6-class illegal-write hunt is EMPTY. Validator on the untouched census:
   257 movements, 21 edges, 0 errors, 0 warnings.
3. **The unrecorded-write find is real and complete**: the full continuesAs
   sweep into era 10 yields exactly VIII.11→IX.22, VIII.13→IX.10, VIII.29→
   IX.23, VIII.49→IX.20; the Frozen E9 Q6 lists the last three and not the
   first; "the sweep found no other unrecorded writes" is TRUE (S8 concerns
   the missing lean, not the find).
4. **Counts**: 17 drafts (JSON count, no id/atlasId collisions against the
   257, all shortNames ≤20, start≤end, era:10 throughout, lane encodings
   match census precedent — "2 Caucasus" = IX.27's string; the "1<->6 bridge
   …/1.5" already exists in the census); 257→274; 21→24 edges with the three
   proposals; tier arithmetic 7+18+2+5=32 with all 32 ids present exactly
   once; the mismatch sweep's 3(a)/6(b)/2(c)=11 is complete against the census
   (every living era-10 row with a non-boundary end is in it; no twelfth case
   exists; IX.17 is the one living:false/2026 inverse); prose sweep 13 hits =
   3 strong + 10 mild, 19 clean, matching the survey table; 211 = 167 row +
   44 extra items recomputed from the JSON (32 row keys + 11 extra keys, X.8
   zero by design — S5 is about the landing sentence, not these numbers);
   Q4's NINE rationale writes = 3(a)+6(b); the draft-base queue
   5+11+10+9+12+24+17 across seven eras extends the Frozen E9 §4 statement
   correctly, era-4 eight-draft question restated.
5. **Frozen-record citation fidelity — the misattributed-Frozen hunt is
   empty**: IX.15's floorNote "formal disposition to this era's Step 0" is
   verbatim and unique (greped across all 32 floorNotes — the era's ONE
   record-mandate claim is true); "stays on the register until era 10
   completes the case" is verbatim Frozen E9 Q5(a); the register-cap
   convention quote matches E9 §5 word-for-word; the VIII.18 office-run law
   ("single irreplaceable locus") matches E9's text; the cleared-runs-count
   convention and sixth–ninth are E9's own, so tenth-next is correct; VIII.3's
   dateRationale genuinely names the verified 1906 census listing (the "rare
   seam" claim is real); VIII.1's relations line genuinely names "the
   civil-rights church"; IX.20's "ended at 1500" stale line is really there;
   IX.29's row really names VIII.23 as parent; IX.24's regions array really
   reads North America/North Europe against a Global teaser; VIII.28–31 all
   end 1906; the census carries exactly ONE existing "in tension with" edge
   (so "second" is right) and the Augustine→Geneva shorthand is grounded (the
   I.8 edge's note is explicitly Augustine→Calvin); VIII.20 is still the only
   Outside-A4 row; the Timor revival is genuinely staged in Frozen VIII.26's
   own sources[] with the window flag; the E9 fork's "era-10 segments at the
   E10 gate" terms are as quoted. All twelve E9 forward flags located and
   dispositioned (flag 12 implicitly — N7).
6. **The Q1 addendum fold is faithful**: six sub-questions, same grouping
   (frame / R1–R2 / R3 / R4–R6 / R7 / R8–R10), leans unchanged
   (freeze/adopt×5), nothing added, nothing dropped; the addendum's header
   confirms two review rounds applied, as the era doc states.
7. **R10 self-hunt on the era doc's own text**: zero classical-ladder
   vocabulary anywhere in the document (greped); no present-tense verdict
   phrased against people found (the hard cases — Driscoll/Mars Hill, LLDM
   2022, L'Arche, Hanegraaff — are all dated-public-record phrasings with the
   R4 posture stated); every end is R5-classed with IX.28's judgment-end said
   as a judgment; no obituary for a living movement; the safety clause holds
   in the doc's own copy (no non-public person or community identified; IX.17
   remnant language held to existence-only). The only R6-adjacent blemish is
   N4's sentence scope, not a violation.
8. **Gate-decidability elsewhere**: Q1–Q6 and Q8–Q11 each resolve to one
   unambiguous application under their stated leans (Q3's three-part bundle
   carries separate leans for the 17, the two structural questions, and the
   MacArthur menu; Q4's every item has a lean; Q9's menu has a marked LEAD
   LEAN). The exceptions are exactly S8 (Q7's ratify-or-correct), N1 (edge
   grades), and N2 (IX.20 timing).
9. **Register/A3 machinery**: beyondFloor arithmetic (IX.15/16/17 true,
   IX.26 false question-framed) matches the census; the c2 carrier set
   (IX.4/5/7/14 "question", IX.16/17 "record") matches; the composite/culture
   /label row lists match the addendum's own R1 lists; IX.18's label-row
   discipline is held throughout (no entry-level finding appears anywhere in
   the doc); the Kimbanguist 2005→2008→2021 arc, the FFOZ 2009 shift, the
   Lausanne three-confession ladder, and the Waco/Rātana/INC verified sets all
   match the research verbatim.

— End of Round 1. Eight substantial findings; none census-touching until the
gate; every fix executable from the grounding already on file — no
re-research needed. REVISE before the package goes to Mark; Round 2 on the
revision.
