# Targeted Recheck, Round 2 — obel (The Old Believers)
## Step 0, Doc_01, Doc_02 / Source Registry

**Reviewer:** independent review thread, did not draft or revise the material
under review, and did not write the Round 1 review.
**Date:** 2026-09-25
**Branch reviewed:** `worktree-agent-add54097ad81169da` at `6d06fbb`
**Scope:** targeted recheck against the 29 numbered findings of
`obel_Step0_Doc01_Doc02_Review_Round1.md` (read in full, including its §8
Addendum of 2026-09-25) and against the diff that answered them — per
`CLAUDE.md`'s review-cost discipline ("From round 2 onward, do a targeted
recheck (only what changed, against prior findings) instead of a full
re-review from scratch") and the `cic-build-cycle` skill's matching rule.

**Documents rechecked:**
- `worlds/obel/Step0_Movement_Scope_Confirmation.md`
- `worlds/obel/Doc_01_World_Identification_Boundaries_Orientation.md`
- `worlds/obel/Doc_02_Source_Ecology.md`
- `worlds/obel/obel_Source_Registry.md`

**Also opened and checked directly, because findings name them:** both
vendored source files; `worlds/obel/Open_Gaps_Tracking.md`;
`records/worlds/obel.yaml`; `cic/texts/INTAKE.md`; `cic/texts/REGISTRY.yaml`;
`cic/corpus-map/the-old-believers.yaml` and both corpus-map staging files;
`cic/corpus-map/fixture-synthetic.yaml`;
`worlds/_cross-world/dossiers/the-old-believers_Source_Readiness_Dossier.md`;
`cic-website/data/world-census.json`; `engine/m1/cross_world.py`;
`engine/m9/holdings.py`; `Ministry/Features/Atlas-World-Map/Decision-Log.md`;
`reference/L3B-World-Build-Methodology/Source_Registry_Template.md`;
`reference/method/CiC_Record_Native_World_Build_Process_V1.5.md`; and
`reference/method/` as a directory listing.

I re-derived every quotation and every page locus myself, from the vendored
files, before looking at what the documents claim. I did not treat a finding
number cited in a fix as evidence that the fix is right.

---

# 1. Overall verdict

## **Substantial revision still required — but narrowly, and on document hygiene and process, not on substance.**

This is a different kind of verdict from Round 1's, and the difference should
not be blurred. **All six of Round 1's blocking findings are closed** —
Finding 1 (the floor claim the source refutes), Finding 2 (the fabricated
INTAKE.md ruling), Finding 3, Finding 20 (V1.8 as unreadable governing
authority), Finding 21 and Finding 22. Of the 29 findings, **25 are closed, 3
are partially closed, and 1 is not closed.** Every substantive historical
claim I rechecked is now accurate, every quotation's wording is exact, and —
this is the largest single improvement — **every page locus is now correct**,
against a pagination convention I established independently before reading
what the documents assert.

Several of the fixes are better than the findings that prompted them. The
Finding 1 rewrite does not merely soften the floor claim; it quotes the p. 34
passage at both places the claim is made, restates the floor at the precision
the source supports, corrects `records/worlds/obel.yaml`'s `doorway_description`
to match, and correctly refuses to touch the census. The Finding 4 fix reaches
the right answer on all three points the Round 1 addendum laid out, and I
confirmed its load-bearing negative claim directly: "Theodoret" occurs exactly
once in the whole English file, so the original draft's premise of a
separately-named Theodoret was indeed wrong. The Finding 14 fix turns a
"we don't know" into a real, citable edition finding, and both halves of it
survive independent checking. The Finding 24 fix is the model of what the
build-cycle skill's "never dismissed without re-verification" rule asks for:
the unverifiable dismissal is gone and the finding is left open rather than
re-dismissed on a different authority.

What still blocks is a narrower set, and it is almost entirely one thing plus
its neighbours:

1. **Finding 29 (process narration in canonical files) is not closed, and on
   the Source Registry the revision made it worse.** The three narrative
   documents are much cleaner — the §16 self-assessment advocacy, the
   "Corrected, self-review:" blocks and the "an earlier draft said X"
   sentences are gone from body text and now live in the document logs and
   `Open_Gaps_Tracking.md`, which is exactly right. But the Registry now
   carries "corrected Round 2, Finding N — an earlier draft of this row…"
   narration in its header, its status line, eight of nine rows and its
   footer, plus a paragraph arguing its own case to a reviewer. Finding 29
   named the Registry explicitly. This is the same direction the Round 1
   addendum already recorded once for the self-review pass, and it is a
   live/canonical surface.
2. **`Open_Gaps_Tracking.md` entry 10's original text was rewritten, not
   appended to** — and the replacement text states that the original was
   "left in place per the append-only rule rather than rewritten," which the
   diff shows is not what happened. Four other entries were corrected
   correctly, by appending. This one was not.
3. **Doc_01 §13 points the reader at "this world's final handoff report,"
   which does not exist anywhere in the tree.** That is a new instance of the
   precise failure mode Findings 21 and 22 were about.
4. **Step 0 §5 and Doc_02 §16 name escalation categories that apply to this
   package and then announce that the thread will self-dispose to "Approved to
   proceed" anyway.** The skill's gate reads the other way.

Below those sit two small numeric/scope imprecisions the fixes introduced
(§3, N2 and N4), one undisclosed transcription convention that Round 1 already
flagged as cosmetic and that has since become load-bearing (N1), and one item
the brief asked me to confirm that I cannot confirm: **`python -m engine.m9.cli
holdings obel` does not run in this checkout at all** (§5(g)).

None of the remaining items changes a historical claim, a confidence rating, a
sourcing conclusion or a scope boundary in a way a reader would be misled by.
But `CLAUDE.md` treats process narration in a live/canonical file as
corruption to remove, and breaking the append-only rule while stating that it
was honoured is not a hygiene matter either. So: substantial, narrow, and
fixable in one pass.

**Note on the round count.** This is round 2 of at most three. The
`cic-build-cycle` skill: "Three rounds of substantial revision on the same
document without it clearing review is itself an unresolved tension the
pipeline can't close on its own… Never start a fourth round." The remaining
work is small and well-specified enough that a third round should clear it; if
it does not, the skill's escalation applies rather than a fourth attempt.

**This file is not a ruling.** Per the build-cycle skill, no document may be
dispositioned on the strength of its reviewer's own reading, and the three
governance/portfolio escalations these documents name are still open with
Mark.

---

# 2. Finding-by-finding recheck (Round 1 Findings 1–29)

Verdicts are against the location each finding names. "Re-verified" means I
checked it myself against the primary file or the cited repository file, not
against the fix's own account of itself.

| # | Round 1 finding (short) | Verdict | Reason |
|---|---|---|---|
| 1 | Floor claim contradicted at p. 34 (**blocking**) | **CLOSED** | Step 0 §2, Doc_01 §9 and `records/worlds/obel.yaml`'s `doorway_description` all restated at the precision the source supports; p. 34 quoted at both places; registered as a `contested_claim` candidate (Doc_01 §10, Open_Gaps 11); census correctly *not* edited and escalated as portfolio-level. I re-verified the p. 34 passage, its locus, and the Russian counterpart (see §4). |
| 2 | Fabricated INTAKE.md "2026-09-25 ruling" (**blocking**) | **CLOSED** | `grep -n "2026-09-25" cic/texts/INTAKE.md` → no matches, confirmed myself. The citation is gone as an assertion from all six locations; the real 2026-09-02 rule is now quoted accurately in each. See §5(f). |
| 3 | Doc_01 §4 used the Russian as free-standing evidence (**blocking**) | **CLOSED** | §4 rebuilt around the edition-comparison finding; the Russian is used only to identify what the English omits, with the second-witness rule stated inline; Registry R2's licence for that claim is explicitly **withdrawn**, not reworded. |
| 4 | Invented "Bishop of Cyrus" emendation | **CLOSED** | Conjecture deleted. "Cyrene" now correctly the faithful reading of *киринейскаго*; "Heart" correctly identified as OCR for *Блаженнаго*; Theodore/Theodoret divergence tagged [Contested]; *Slovo Feodoritovo* crux registered as a `contested_claim` candidate. I confirmed the fix's load-bearing negative: "Theodoret" occurs **once** in the English file (line 4847), so no separate Theodoret exists for the phrase to duplicate. |
| 5 | Silent "Meletina" → "Meletius" | **CLOSED** (was already closed at the addendum) | Doc_01 §1 prints "Meletina of Antioch" exactly as the file does; I string-matched the whole authority list against the source and it is exact. Residual nicety, not a finding: the edition's own "Melety" variant (line 4854) is still unrecorded. |
| 6 | p. 120 vs pp. 120–121; Doc_01/Doc_02 disagreed | **CLOSED** | I re-derived the pagination convention from scratch (marker at the **foot**, next page's running head immediately after; proved at the 120/121 and 121/122 breaks). Doc_01 §1 → p. 121 ✓; Doc_01 §9 → pp. 120–121 with the split stated ✓; Step 0 §2 → pp. 120–121 ✓; Doc_02 §1.1 → pp. 120–121 ✓; Registry R1 → pp. 120–121 ✓. All five now agree and all five are right. |
| 7 | Dedication is p. 33, not p. 32; stated method off by one | **PARTIALLY CLOSED** | Documents fixed and re-verified: the dedication and its footnote both sit between the 32 and 33 markers → p. 33, and Doc_02 §1.1 now has both there. The stated method is corrected to "the **next** page's own running head." **But `Open_Gaps_Tracking.md` entry 5 still cites "(p. 32)" with no appended correction**, while four other entries did get one. |
| 8 | Closing passage locus wrong on both counts | **CLOSED** | Re-verified: the passage falls after the printed "155" and after a fresh running head → **p. 156**, and 155 is not the last page. Doc_02 §1.1 now says p. 156 with the reasoning; "155pp." → "at least 156pp." in Doc_02 §0, the corpus-map `locus`, and the Dossier §1. |
| 9 | False claim that no Orthodox-lane world is built | **CLOSED** | I confirmed `cappadocian-nicene-pastoral-monastic-tradition` is `lane: "3 Greek East & Orthodoxy"`, `status: "Built & Live"`. Doc_01 §5, §8, Doc_02 §8 and the Registry footer all name it and redo the comparandum assessment by the right method. Minor residual at §3 N5. |
| 10 | Doc_01 §8 self-contradiction ("built or candidate") | **CLOSED** | §8 now separates built from candidate correctly and names the three `russian-church-*` entries as Pre-Survey Candidates. Residual imprecision at §3 N4. |
| 11 | Pomorian Answers misattributed to Semyon Denisov | **CLOSED** | Corrected to Andrei Denisov (1664–1730) with Trifon Petrov and Semyon Denisov as participants, and propagated to all four places the finding named: Registry R7, Doc_01 §1 and §2.3, Doc_02 §2, Dossier §4, plus an appended correction at Open_Gaps entry 4. |
| 12 | A–E tiers misapplied in five of nine rows; R2 over-claimed | **CLOSED** | Checked each row against the template's own table (lines 42–46): R5 → C ✓, R6/R7/R8/R9 → B ✓, R2 → B ✓, R3/R4 C re-confirmed ✓, R1 A ✓. All nine now match the printed definitions. Two notes: R2's Confidence cell still carries prose around the letter (Round 1 cosmetic 9), now as revision narration — see Finding 29; and the **template itself** is internally inconsistent about what B means (see §3 N9) — pre-existing, in `reference/`, not this world's. |
| 13 | Undisclosed bracketed editorial glosses in the Russian file | **PARTIALLY CLOSED** | The hazard is now disclosed, well and in the right places: Doc_02 §7, Registry R2, Doc_01 §4 and §11, Open_Gaps 15, the corpus-map bucket, the staging file and `REGISTRY.yaml`, each with the "strip before quoting" instruction. **But the count is wrong** — "roughly ninety" is a byte-vs-character artifact of Round 1's own `grep`, and the real figure is 116. See §3 N2. |
| 14 | §4 left settled question open on a false premise | **PARTIALLY CLOSED** | Doc_01 §4 is now a genuine, correct edition finding, and I verified both halves independently: the two openings are positionally aligned (same Epiphanius attribution, same "Amen", identical following Trinity paragraph), and no equivalent of the plain-speech apologia exists anywhere in the English file. **But Open_Gaps entry 5 still carries the superseded "does not know whether the English translators abridged, relocated, or otherwise handled this passage differently" with no appended correction.** |
| 15 | Overstated provenance; undisclosed edition substitution | **CLOSED** | Doc_02 §7 now distinguishes a traceable *printing* from a traceable *text*, names Brostrom (1979) and Gluck & Brostrom (2021) as the census's own editions and discloses the public-domain substitution and its cost, and names redaction identity as an unresolved gap (also Open_Gaps 13). |
| 16 | Edition's own Chronological Table carries 1681 | **CLOSED** | Re-verified in the file (line 1197: "1681, April. Avvakum and his friends executed."). Disclosed at Doc_02 §1.1 and Open_Gaps 14 as an apparatus error; Doc_01 keeps the correct 1682. |
| 17 | Two witnesses contradict on the opening's authorship | **CLOSED** | Both readings re-verified exactly — the English footnote at p. 33 and the Russian "писано моею рукою грешною". Disclosed at Doc_02 §1.1, carried into §6's thin-evidence map as a Contested row, and into §7 and Open_Gaps 13, without preferring either witness. Minor: "attached to the opening dedication" is an inference (the OCR carries no footnote marker) stated as fact — reasonable, and I would not revise for it. |
| 18 | Step 0 §1 misread the "12 drafts" list | **CLOSED** | Re-verified: the log says "12 drafts (VII.18–VII.29)", which excludes VII.7, and the 2026-08-02 entry's "NOT written: VI.24→VII.4, VI.23→VII.7 (era 8's)" confirms VII.7 pre-existed as a banked receiver. Step 0 §1 and Doc_01 §1 now state exactly that, and no longer claim this world was drafted at the Era 8 gate. |
| 19 | "A1.E8 (1650–1815)" misattributed | **CLOSED** (was already closed at the addendum) | Re-verified myself: the string is at line 3990, inside the "Next:" line closing the **2026-08-02** Era 7 Frozen entry (heading at line 3958), not in either 2026-08-03 Era 8 heading. Both documents now attribute it there, and both render the en dash. |
| 20 | Three canonical documents governed by a spec not in the tree (**blocking**) | **CLOSED** on the documents; escalation open | Re-confirmed V1.8 is absent (`reference/method/` holds V1.5, no V1.8) and V1.5 is present. Every governing citation is re-grounded on V1.5; the surviving V1.8 mentions are the open-item disclosure (Doc_01 §10), the escalation statements, and the document logs — none of them load-bearing. Two observations at §3 N6 and §6. |
| 21 | Step 0 dispositioned on a nonexistent review file (**blocking**) | **CLOSED** | The disposition is withdrawn and the pointer now names the combined Round 1 file, which exists. The sequencing irregularity the addendum noted cannot be undone; it is disclosed in the logs and is materially mitigated by all three documents now being reviewed as one package. **A new instance of the same failure mode appears elsewhere — see §3 N3.** |
| 22 | Open_Gaps entry 8 pointed at review files that do not exist (**blocking**) | **CLOSED** | Correction appended to entry 8 (append-only, correctly); the single combined review artifact exists and is named. The tool-surface discrepancy is left open and disclosed rather than resolved, which is the right call. |
| 23 | "Documented" resting on the census | **CLOSED** | §2.1 (1666–1667 council) and §3 (geographic core) are re-tagged **Widely Accepted**; §2.3's Solovetsky basis is restated as what was actually done. I checked all three surviving [Documented] tags in Doc_01 — three fingers (§1), Meletios/"Meletina" (§1), Siberia/Dauria (§3) — and each rests on direct verification against a vendored file. The Meletios upgrade follows the Round 1 addendum's own recommendation. |
| 24 | §5 dismissed a tooling finding on a docstring that says otherwise | **CLOSED** | Re-verified: `engine/m1/cross_world.py`'s docstring (lines 1–34) says nothing about COVERAGE; the inline comments near lines 218–250 do record "asserted for correction… they RANK rather than exclude," twice, dated 2026-09-09. Doc_02 §5 now states that accurately and **leaves the finding open** instead of re-dismissing it. Arithmetic re-verified independently (§5(g)). |
| 25 | Partial delivery against V1.8 §2; unauditable | **CLOSED** | Every row Round 1's table marked wrong or incomplete is fixed: loci (Findings 6/7/8), cross-world overlaps (9), edition and original-language notes (13/15/16/17), holdings disposition (24). The auditability problem is resolved the right way — by ceasing to cite an unreadable spec, not by arguing compliance with it. See §6 for one consequence worth naming. |
| 26 | Framing instruction attributed to "the task" | **CLOSED** | No occurrence of "the task's own instruction", "as instructed" or any equivalent survives in any of the four documents. |
| 27 | Dossier attributed a finding to `CLAUDE.md` that is not in it | **CLOSED** | The Dossier header now states the correction plainly: the finding stands, the citation was wrong and is removed. |
| 28 | Census prose attributed to Avvakum's translators | **CLOSED** | Doc_01 §4 now attributes "the plain, angry, comic Russian of speech rather than of books" to the census's own characterization (`documentedStories[0]`) and tags it **Widely Accepted** as a project-internal characterization. |
| 29 | Process narration in all three documents and the Registry | **NOT CLOSED** | Substantially improved in Step 0, Doc_01 and Doc_02 — but four instances Finding 29 named by name survive there, and on the **Registry**, which Finding 29 also named, the revision added a great deal more than it removed. Detail immediately below. |

## Finding 29 in detail — what moved and what did not

**Genuinely fixed, and worth saying so.** Doc_02 §16's "Self-assessment
against the task's own bar" — the paragraph of advocacy addressed to a
reviewer, which Round 1 called the clearest case — is gone. So are Doc_02
§3's "**Corrected, self-review:**" block, Doc_02's cosmetic-classification log
entry, Doc_01 §2.2's "This document does not re-litigate that portfolio-level
decision (outside this thread's authority…)", §2.3's "named here so it is not
lost", §8's "This document names no false proximate neighbor rather than
manufacture a comparison", and every "Finding N" / "an earlier draft said X"
reference in all three documents' body text. That history now sits in each
document's own Document Log and in `Open_Gaps_Tracking.md` entry 16, which is
where `CLAUDE.md` puts it. The honest-limit statements — "not yet verified
against a primary source", "Contested", "nothing vendored" — are correctly
kept as content. The line Round 1 asked for was drawn, and mostly drawn well.

**Still present in the three narrative documents**, each named explicitly by
Finding 29:

- **Doc_02 §16, "Escalation check"** — a whole body section of build-process
  bookkeeping. Finding 29: "belongs in the Decision Log."
- **Step 0 §5's disposition-and-escalation reasoning** — rewritten, not
  relocated. Finding 29 named this same section.
- **Doc_02 §15, "Open items from this revision"** — a section whose only
  content is a pointer, framed as revision bookkeeping.
- **Step 0 §1's** "(a portfolio-level matter, outside this thread's
  authority)" — the same sentence-shape Finding 29 quoted from Doc_01 §2.2 and
  which was removed there.
- Milder: **Doc_02 §0's** "Before this pass, nothing was vendored for it. This
  session vendored two files."

**The Registry is where this went backwards.** `obel_Source_Registry.md` now
carries:

- a header parenthesis: "**corrected, Round 2, cosmetic Finding 3** — an
  earlier draft of this header named a nonexistent
  `obel_Doc_02_Source_Ecology.md`";
- a status line that reports what Round 1 found about this Registry;
- a "Living-document protocol" paragraph that argues, to a reviewer, why
  in-place row correction is permissible under the Template's append-only
  rule;
- "**corrected Round 2, Finding N** — an earlier draft of this row…"
  narration inside eight of nine rows, in the Source, Confidence, Licensed
  For, Verification Note and Added cells;
- a footer parenthesis narrating what an earlier draft of the footer asserted.

`CLAUDE.md` is unambiguous that `worlds/` holds "only what runs the program or
constitutes the finished record — no notes, commentary, change history, review
discussion, or process narration embedded in them," and that finding such
material in a live file is corruption to remove rather than add to. Round 1
found two instances here (the status line and the "Checkpoint confirmed"
footer). There are now roughly a dozen. The *corrections themselves* are
right and should stay; what should move to `Open_Gaps_Tracking.md` and to the
review files is the account of what an earlier draft said and which finding
number prompted the change. A reader of the finished record needs to know that
R7 is Andrei Denisov; they do not need to know that R7 once said Semyon.

The Registry's self-granted exception also deserves naming: the "Living-
document protocol" paragraph reasons its way to permission to edit row text in
place. I think the *conclusion* is defensible — the Template's rule protects
row identity and forbids renumbering and removal, and correcting a factual
misattribution in place while disclosing it is not the same as removing a row.
But a canonical document arguing its own exemption to a Template rule is
exactly the "review discussion, written into the canonical document, about the
canonical document" that Finding 29 was about, and if the exception is real it
belongs in the Template or in a decision log, not in the artifact claiming it.

---

# 3. New issues introduced by the fix

Ranked by severity. Nothing here is a fabricated claim or a misattribution of
the kind Round 1 found; the two substantial items are both process.

### N3 — Doc_01 §13 cites a "final handoff report" that does not exist
**Severity: substantial (process).**
Doc_01 §13's last line: "See this world's final handoff report for the
complete list." `find . -iname "*handoff*"` returns handoff documents for
other workstreams and worlds (`worlds/alx/build/HANDOFF-TO-BUILD-THREAD.md`,
several under `Ministry/`, one under `worlds/lpc/`) and **none for `obel`**.
The line is new in the Round 2 revision commit (`db91d0a`).

This is the same failure mode as Findings 21 and 22, in the same package, one
round later: Round 1 on Finding 22 — "A pointer to evidence that does not
exist is weaker than no pointer, because it reads as verification." The three
escalations are stated in full in Step 0 §5, Doc_01 §13 and Doc_02 §16, so
nothing is actually lost; the pointer adds a nonexistent artifact to a list
that is already complete. **Required:** delete the pointer, or create the
report before citing it.

### N10 — `Open_Gaps_Tracking.md` entry 10's original text was rewritten, and the replacement says it was not
**Severity: substantial.**
The file's own header rule, from `CLAUDE.md`: "Entries are append-only and
numbered; a merged entry's number never changes." Entries 4, 7, 8 and 9 were
corrected correctly — original text untouched, a dated **Correction** block
appended. Entry 10 was not. `git diff db91d0a^ HEAD` shows six lines of the
original entry's own text deleted (the "Meletina is plausibly… / the Heart
Bishop of Cyrene plausibly a corruption of the Bishop of Cyrus… / not flagged
for priority acquisition" reasoning), "p. 120" edited in place to "p. 121,
corrected locus below", and a bracketed placeholder inserted in their place.

The placeholder reads: "[Original entry's own guesses were wrong — see the
2026-09-25 Round 2 correction immediately below, **left in place per the
append-only rule rather than rewritten**.]" The text it describes as left in
place is the text that was deleted. That sentence is not true of the file it
sits in, and it reads as compliance with a rule the same edit broke.

**Required:** restore entry 10's original text verbatim from `0370466` and
leave the Round 2 correction block appended below it, as entries 4, 7, 8 and 9
do. Do not fix this by editing the placeholder's wording.

### N6 — Step 0 §5 and Doc_02 §16 announce self-disposition while naming escalation categories that apply
**Severity: substantial (process). Mark's call, not mine.**
Step 0 §5 names two matters that "meet the governance/methodology escalation
category" and a third that is portfolio-level, says all three "go to Mark
directly," and then closes: "With those two items escalated rather than
resolved here, and once this revision clears independent re-review, this build
thread applies 'Approved to proceed' itself per CO-022's own self-disposition
rule." Doc_02 §16 says the same in substance.

The `cic-build-cycle` skill's gate reads the other way: "Before disposing of
any document, check it against these four categories. **If any apply, stop and
escalate directly to the project lead — do not self-dispose, regardless of how
clean the review came back.**"

There is a real reading on which the escalated items are separable from these
documents' own content — the fabricated citation's *origin*, and *which*
process document governs the build, are questions about the build process
rather than about Step 0's substance, and the V1.8 question has been worked
around by re-grounding on V1.5. I do not think the build thread is being
evasive here. But it is resolving a genuine ambiguity in its own favour, in
advance, in a canonical document, on a package whose Round 1 review found a
fabricated citation inside it. That is the decision the gate exists to take
out of the build thread's hands.

For comparison, the pre-revision version of this section claimed "no
escalation category applies (none appear to at this stage)" — which was simply
wrong. The revision is markedly more honest about *what* applies and less
correct about what follows from it. **Required:** either drop the
self-disposition sentence and let Mark dispose, or put the reading above to
Mark explicitly as the question it is.

### N1 — OCR normalizations inside quotations labelled verbatim, convention still undisclosed
**Severity: minor, rising to substantial for the p. 34 quote.**
Round 1's cosmetic item 1 asked that the documents state their transcription
convention once. They still do not, and one of the affected quotations is now
the single most load-bearing quotation in the package. Normalizing whitespace
and smart quotes, I get:

| Quote | Source prints | Document prints |
|---|---|---|
| Doc_01 §9, p. 34 (introduced as "quoted verbatim") | `than to cut out “ True”, for in that name **zs** contained the essence of God` | `than to cut out "True", for in that name **is** contained the essence of God` |
| Doc_01 §9, the patriarchs | `“Why”, said they,` | `"Why," said they,` |
| Doc_01 §9, Avvakum's reply | `was no sedition. **-Nikon**, the wolf,` | `was no sedition. **Nikon**, the wolf,` |

Every other English quotation I tested matches exactly after whitespace
normalization: the authority list, the dedication, the Epiphanius footnote,
both halves of the Markovna exchange, the closing passage, and the
Chronological Table line. All the **words** are right and all the **loci** are
now right; the issue is solely that three OCR artifacts are silently mended
inside passages presented as verbatim, with no stated convention.

`zs` → `is` is obviously correct, and I would not want it left as `zs`. But
`CLAUDE.md` makes verbatim re-verification the standing rule, and
`cic/texts/REGISTRY.yaml`'s own note on this very file says "any quotation must
still be independently re-verified character-by-character before use." One
sentence in Doc_02 §7 or Registry R1 — this edition's OCR carries stray
hyphens, `zs` for `is`, and British punctuation outside the quotation mark;
quotations here silently repair those and normalize smart quotes — closes it
permanently for every downstream document. **Required:** state the convention
once.

### N2 — "roughly ninety" bracketed glosses undercounts; the real figure is 116
**Severity: minor, but it is in six places.**
Round 1's Finding 13 reported 90 matches from
`grep -o "\[[^]]\{1,60\}\]"`. That number is a measurement artifact: GNU grep
counts the `{1,60}` bound in **bytes**, and Cyrillic is two bytes per
character in UTF-8, so every gloss longer than about 30 characters was missed.
Counting characters in Python:

- `re.findall(r'\[[^\]]{1,60}\]')` → **107**
- `re.findall(r'\[[^\]]*\]')` → **116**, of which 9 exceed 62 characters
- **0** of the 116 lack Cyrillic, so none is a footnote marker or similar —
  all 116 are editorial glosses

"Roughly ninety" is now stated in Doc_01 §4, Doc_01 §11, Doc_02 §7, Registry
R2, Open_Gaps 15, `cic/texts/REGISTRY.yaml` and the corpus-map bucket and
staging file. It undercounts by about a fifth.

I flag this not because the difference matters to the hazard — the instruction
to strip the glosses before quoting is correct and complete either way — but
because of *how* it got there: the figure was carried forward from a finding's
own grep rather than re-derived. That is the specific habit this recheck was
asked to test for. **Required:** state 116 (or "more than a hundred"), in all
seven places.

### N4 — Doc_01 §8's "three entries in the same window and lane" is loose
**Severity: low-to-moderate.**
Doc_01 §8: "the census carries three entries in the same window and lane…
(`russian-church-stoglav-to-nikon`, `russian-church-nikon-to-holy-synod`,
`russian-church-synodal-century`)". Against the census, with this world at
1666–1815:

- `russian-church-nikon-to-holy-synod` — 1652–1815. Genuinely overlapping,
  and the real nearest candidate.
- `russian-church-stoglav-to-nikon` — 1517–1650. **No overlap at all**; it
  ends sixteen years before this world begins.
- `russian-church-synodal-century` — 1815–1906. Touches at the single
  endpoint year.

The lane is right for all three and the substantive conclusion is right. But
"the same window" is an over-broad scope statement of exactly the kind Finding
10 was about, and the follow-on sentence — "This world is the ritual-and-
textual position **those entries'** own anathema was directed against" —
attributes the 1666 anathema to an entry that closes in 1650. **Required:**
name `russian-church-nikon-to-holy-synod` as the overlapping candidate and the
other two as adjacent-but-non-overlapping.

### N5 — `imperial-juridical-christianity` is Built & Live and unnamed in the same-lane check
**Severity: low.**
Doc_01 §5 and Doc_02 §8 both call `cappadocian` "the one other Built & Live
world in this fleet's 'Greek East & Orthodoxy' lane." Strictly true of the
lane string `3 Greek East & Orthodoxy`. But `imperial-juridical-christianity`
(`ijc`, 312–451) is also Built & Live on lane `3<->5 bridge (Greek East /
Latin West)` — half in this lane. Since Finding 9's whole point was that an
absence claim must be reached by enumerating and setting aside rather than by
assertion, the enumeration should say so and set `ijc` aside in the same
breath (which it plainly deserves: fifth-century imperial law is no
comparandum for seventeenth-century Muscovy). The general sweep in Doc_01 §5
— "or with any other built or candidate world in this fleet" — covers it, so
the conclusion is safe.

### N7 — Registry R1's "see R-note below" is a dangling cross-reference
**Severity: low.** The string "R-note" occurs exactly once in the Registry,
in the reference itself. Nothing below it is an R-note.

### N8 — see §5(g): two tooling invocations cited in Doc_02 do not run as printed
Reported under the brief's point (g) rather than repeated here.

### N9 — the Source Registry Template contradicts itself about tier B
**Severity: low. Not this world's defect; for the coach thread.**
`reference/L3B-World-Build-Methodology/Source_Registry_Template.md` line 44
defines **B** as "Specific work/locus named, not independently re-checked this
session." Line 83's parenthetical says the opposite happened: "The prior rule…
assumed the Confidence letter's B still meant 'specific work/locus named';
**after the Round-1 recalibration redefined B to mean recall**, the legacy
letter stopped marking the actual risk boundary."

So the Template's own table and its own process note disagree about what B
means. The Registry's Round 2 tier assignments follow the **printed table**,
which is the right choice for a build thread to make, and Finding 12 is closed
on that basis. But a future world will hit the same contradiction. Editing
`reference/` is a coach thread's authority, not a build thread's — flagged
here for whoever holds it.

---

# 4. Quotation and locus re-verification — what I did, and what I found

**I re-derived the English file's pagination convention before reading any
locus claim.** Page numbers print on their own line at the **foot** of the page
they number, immediately followed by the **next** page's running head. I
proved this at two breaks, independently of Round 1's proof:

```
… only thou standest out in thine obstinacy and      ← last line of p.120
120
THE ARCHPRIEST AVVAKUM                               ← running head of p.121
dost cross thyself with two fingers; it is not seemly.
```
```
… Then in the time of Ivan, the Tsar, there were the ← last lines of p.121
121
THE LIFE OF                                          ← running head of p.122
```

The 140 marker lines run from `2` to `155`; `155` (line 6168) is the last, and
text continues past it under a fresh running head.

**English file** (`avvakum_life-of-archpriest-avvakum_harrison-mirrlees1924.txt`):

| Quotation, as now cited | Cited locus | Locus verdict | Text verdict |
|---|---|---|---|
| Creed-wording passage, "It were better in the Creed…" (Doc_01 §9; Doc_02 §1.1; Registry R1) | p. 34 | **Correct** — between the 33 and 34 markers (lines 1235–1298) | Words exact; one silent OCR repair, `zs` → `is` (N1) |
| Opening dedication, "Avvakum, archpriest, was bidden by the monk Epiphanius…" (Doc_02 §1.1) | p. 33 | **Correct** — between the 32 and 33 markers | **Exact** |
| Footnote, "In the original manuscript this is in the writing of Epiphanius" (Doc_02 §1.1) | p. 33 | **Correct** — same page as the dedication, as it must be | **Exact** |
| Markovna, "How long, archpriest, are these sufferings to last?" / "Markovna! till our death" (Doc_02 §1.1; Registry R1) | p. 80 | **Correct** | **Exact** |
| The patriarchs' question, "Why, said they, art thou stubborn?…" (Doc_01 §9; Step 0 §2) | pp. 120–121, question spanning both | **Correct** — begins line 4807 (p. 120), ends "it is not seemly" on p. 121 | Words exact; British comma moved inside the quote (N1) |
| Avvakum's reply, "By the gift of God among us there is autocracy…" (Doc_01 §9) | p. 121, entirely | **Correct** | Words exact; stray OCR hyphen in `-Nikon` dropped (N1) |
| The authority list, "Meletina of Antioch, Theodoret, the Heart Bishop of Cyrene…" (Doc_01 §1) | p. 121 | **Correct** | **Exact**, including "Meletina" |
| Closing passage, "…When we die, then shall this be read…" (Doc_02 §1.1) | p. 156; p. 155 not the last page | **Correct on both counts** | **Exact** |
| Chronological Table, "1681, April. Avvakum and his friends executed." (Doc_02 §1.1) | the edition's own apparatus | **Correct** — line 1197 | **Exact** |

**Russian file** (`avvakum_zhitie-protopopa-avvakuma-orv_wikisource-transcription-nd.txt`).
Tested by exact substring match in Python, character-for-character, with
occurrence counts — not by eye:

| Quotation | Count | Offset | Verdict |
|---|---|---|---|
| "Лучше бы им в Символе веры не глаголати господа… обоя имена исповедаем" (Doc_01 §9) | 1 | 2175 | **Exact** |
| "не позазрите просторечию нашему… но дел наших хощет." (Doc_01 §4) | 1 | 201 | **Exact** |
| "Мелетия антиохийскаго и Феодора Блаженнаго, епископа киринейскаго, Петра Дамаскина и Максима Грека" (Doc_01 §1) | 1 | 84714 | **Exact** |
| "По благословению отца моего старца Епифания писано моею рукою грешною протопопа Аввакума" (Doc_02 §1.1) | 1 | 46 | **Exact** |
| "духу и от сына исхождение являют" (Doc_01 §9) | 1 | 7660 | **Exact** |
| "Да будет проклят сице поюще" (Doc_01 §9) | 1 | 7193 | **Exact** |

**Substantive claims I checked, not just quoted strings:**

- **The p. 34 passage is about the Creed's eighth article.** Confirmed in
  substance: the Nikonian revision removed *истиннаго* from "и в Духа Святаго,
  Господа истиннаго и животворящаго", the Holy Spirit article. Doc_01 §9's
  and Step 0 §2's characterization is accurate, and the passage is
  unambiguously an argument about the Creed's text and content, not about
  ritual gesture.
- **The filioque tie is real.** At offset 7660 the file reads "по-римски
  святую тройцу в четверицу глаголют, духу и от сына исхождение являют" — the
  Roman manner makes the Trinity a quaternity and derives the Spirit's
  procession from the Son too. Doc_01 §9's claim stands. **One caution:** the
  document renders this as a single quotation, "по римской бляди… духу и от
  сына исхождение являют". Those two fragments are 577 characters apart
  (offsets 7083 and 7660) with an unrelated passage on the third triad and the
  anathema between them, and the second fragment's own context reads
  "по-римски", not "по римской бляди". Both fragments are exact and the claim
  is right; the ellipsis is doing more work than a reader would assume. Worth
  splitting into two quotations with their own introductions.
- **The anathema is on fourfold Alleluia.** Confirmed: "…а не четыржи, по
  римской бляди; мерзко богу четверичное воспевание сицевое… Да будет проклят
  сице поюще."
- **The openings are positionally aligned** (Finding 14). Confirmed: Russian
  paragraph 1 = Epiphanius attribution + plain-speech apologia + the Pauline
  citation + "Аминь."; paragraph 2 = "Всесвятая троице, боже и содетелю всего
  мира! поспеши и направи сердце мое…". English: same Epiphanius attribution +
  "Amen!", then "All Holy Trinity! Do thou, O God the Creator of all the
  world, speed me and direct my heart…". Same passage, with the apologia and
  the Pauline citation dropped from the middle.
- **The apologia is not relocated.** Confirmed:
  `grep -niE "plain speech|common speech|vernacular|philosophic|native tongue|fine words|mother tongue|adorn"`
  over the whole English file returns two hits, neither an equivalent (one in
  Mirsky's preface about liturgical translation, one about a ship "not adorned
  with gold"). Doc_01 §4's finding is sound.
- **"Theodoret" occurs once** in the English file (line 4847), and "Melety"
  once (line 4854). The Finding 4 correction's negative premise holds.

**Summary.** Of the fifteen quotations now carried across the four documents,
**all fifteen are word-accurate and all fifteen loci are correct.** Round 1's
verdict on this package was "true about the words and false about the places."
The places are now right. Three English quotations carry undisclosed silent
OCR repairs (N1); one Russian quotation uses an ellipsis across an unusually
wide gap. Nothing I checked is fabricated, misattributed, or unverifiable.

---

# 5. Explicit confirmations on the brief's points (c), (d), (f), (g)

## (c) `Open_Gaps_Tracking.md` — append-only, no rewrites of prior entries

**Mostly correct; one real violation and two omissions.** I checked this
against `git diff db91d0a^ HEAD -- worlds/obel/Open_Gaps_Tracking.md` rather
than by reading the file alone, because a rewrite is invisible from the file.

**Correct:** entries 4, 7, 8 and 9 each keep their original text untouched and
carry a dated **Correction** block appended below — exactly the discipline the
file's own header states. Entries 11 through 16 are new appends. No entry was
renumbered or removed. The file's header rule is restated accurately.

**Violation:** **entry 10's original text was rewritten** — six lines of its
own reasoning deleted, "p. 120" edited in place, a bracketed placeholder
inserted, and the placeholder asserting that the original was "left in place
per the append-only rule rather than rewritten." Full detail and the remedy at
§3 N10.

**Omissions, both at entry 5:** entry 5 still cites the dedication at "(p. 32)"
(Finding 7 corrected this to p. 33 everywhere else) and still states "This
document does not know whether the English translators abridged, relocated, or
otherwise handled this passage differently" (Finding 14 established that the
evidence settles it, and Doc_01 §4 now says so). Under append-only the
original text should stay — but a **Correction** block should be appended, as
four other entries got. Both findings name entry 5 in their "Where," so both
are recorded above as partially closed.

**One smaller gap:** entry 1 still defers the strand question "(Step 3 onward
**per V1.8**)" with no appended correction, while entries 7 and 9 both got one
for the same V1.8 problem. Finding 20 named entry 1 explicitly.

## (d) Process narration removed from the body text of Step 0, Doc_01, Doc_02

**Substantially yes for the three narrative documents; no for the Registry.**

- **"Round 2," "Finding N," "an earlier draft said X," self-referential
  revision-history commentary: fully gone** from the body text of Step 0,
  Doc_01 and Doc_02. I grepped each document with its Document Log excluded
  and found no surviving instance of any of those four patterns. It now lives
  in the three Document Logs and in `Open_Gaps_Tracking.md` entry 16, which is
  where `CLAUDE.md` puts it. Doc_02 §16's self-assessment section — the worst
  case Round 1 found — is gone entirely.
- **But four instances Finding 29 named by name survive** in those same
  documents: Doc_02 §16 ("Escalation check"), Doc_02 §15 ("Open items from
  this revision"), Step 0 §5's disposition-and-escalation reasoning, and Step 0
  §1's "outside this thread's authority." Doc_02 §0's "Before this pass…
  This session vendored" is a milder fifth.
- **The Registry is not clean and is worse than at Round 1** — roughly a dozen
  instances across its header, status line, protocol paragraph, eight of nine
  rows and its footer. Finding 29's "Where" includes "Registry header and
  footer," and the Registry is one of the four documents under recheck.

Everything remaining is documented at §2 under Finding 29. To be explicit
about the line I am drawing, which is the one Round 1 drew: the honest-limit
statements ("not independently re-checked this session," "not vendored,"
"Contested") are content and must stay, and I am not counting them.

## (f) The fabricated INTAKE.md citation is fully gone from the live surfaces

**Confirmed.** Checked directly rather than taken from the revision's account:

- `grep -n "2026-09-25" cic/texts/INTAKE.md` → **no matches.** There is no such
  ruling in that file, at that date or any date.
- INTAKE.md's real rule, lines 22–27, dated **2026-09-02**: original-language
  texts are sourced "as second witnesses — **never primary evidence for a
  Representative**." Line 163 repeats it: "cross-checking an English rendering,
  not itself citable as a Representative's" evidence. Every document that now
  cites this rule quotes it accurately and dates it correctly.
- A repo-wide grep for `"2026-09-25 ruling"` and `"regardless of language"`
  across `*.md`, `*.yaml`, `*.py` and `*.json`, excluding the Round 1 review
  file, returns **two** hits, and neither is an assertion of the fabricated
  ruling: `cic/texts/REGISTRY.yaml` line 2455 and
  `worlds/obel/Open_Gaps_Tracking.md` line 215 are both explicit retractions
  naming it as fabricated.
- **`cic/texts/REGISTRY.yaml`:** the avvakum-Russian entry's note now cites the
  real 2026-09-02 rule and carries a `CORRECTION` block retracting the
  fabrication. I checked whether such a block is itself out of place on a
  live/canonical surface and concluded it is not: `CORRECTION` notes are an
  established convention in that file, with two precedents (lines 491 and 657)
  predating this pass.
- **`cic/corpus-map/the-old-believers.yaml`:** clean of the fabrication; the
  generated bucket's note cites the 2026-09-02 rule and carries a `CORRECTED`
  line.
- **Corpus-map staging files** (`_staging/avvakum_life-…yaml` and
  `_staging/avvakum_zhitie-…yaml`): clean; the staging note matches the
  generated bucket, so a re-merge will not reintroduce it.
- **The Dossier** (`worlds/_cross-world/dossiers/the-old-believers_Source_
  Readiness_Dossier.md`): clean, and separately corrected for Finding 27 and
  Finding 11.

I also confirmed the fix did not overreach: `cic-website/data/world-census.json`
was **not** modified anywhere in this pass, which is correct — Finding 1 ruled
the census portfolio-level and escalate-don't-edit. The whole pass touches 14
files and none of them is the census.

## (g) Do the two commands still run clean?

**`python cic/engine/corpus_map_merge.py --check` — runs clean. ✅**
Exit 0. "600 distinct work(s) → 877 assignment(s) across 58 Atlas entry(ies)
[check only, nothing written]", no errors, no drift reported. The two obel
staging files merge cleanly into the generated bucket.

**`python -m engine.m9.cli holdings obel` — does NOT run. ❌**
It raises an uncaught exception:

```
FileNotFoundError: [Errno 2] No such file or directory:
  '/home/user/CIC-Project/records/obel'
```

The cause is structural, not a regression from this revision.
`engine/m9/holdings.py::holdings_for` calls
`engine/m1/loader.py::load_world_records`, which iterates `records/<world>/`.
That directory exists for every built world (`alx`, `cappadocian`, `desert`,
`don`, `fix`, `gallic`, `hal`, `ijc`, `pahc`, `rzg`, `syr`, `witt`) and **does
not exist for `obel`**, which has only the world stub `records/worlds/obel.yaml`
— as one would expect of a world at the Doc_01/Doc_02 stage with no record
files written yet. `holdings cappadocian` runs fine, so the tool is healthy;
`obel` simply cannot be its argument yet.

**The numbers Doc_02 §5 reports are nevertheless exactly right.** I reproduced
them by substituting an empty record set for the loader:

- 140 vendored files fleet-wide — confirmed independently: 102 `.txt` + 38
  `.xml` = 140.
- Dispositions: **2 `by design` + 93 `out of window` + 45 `no coverage entry`
  = 140** — reproduced exactly.
- Both avvakum files come back `no coverage entry` — reproduced exactly.

So Doc_02 §5's *result* is sound and its arithmetic is sound. What is not
sound is the claim in its first sentence — "`python -m engine.m9.cli holdings
obel` **was run this session**" — which no reader of this checkout can
reproduce, and which as printed produces a traceback rather than a report.
Round 1's Finding 24 read the module but explicitly did not run it, so this is
newly established here.

**A second, smaller instance of the same thing:** Doc_02's "Built from" block
cites "`python cic/engine/corpus_index.py --entry the-old-believers`
searches". That invocation errors: "a query is required unless using --build
alone". Presumably a query was supplied and dropped from the citation.

**Required:** state in Doc_02 §5 how the holdings figures were actually
obtained — with the command as actually run, or with a plain note that
`holdings obel` cannot run until `records/obel/` exists and how the numbers
were derived instead. Correct the `corpus_index.py` invocation to what was run.
The figures themselves need no change; I have independently confirmed all four
of them.

---

# 6. Two observations that are not findings

**The V1.5 re-grounding is correct but leaves three sections without a stated
requirement.** V1.5's Step 2 row (line 98) asks for the Source Registry
Template from the first row, machine-readable rows, and per-row
confidence/boundary-status/licensed-for/verification-note. Doc_02 delivers far
more than that — quotable-passage loci, own-voice/opponent-voice flags, a
thin-evidence map — because those were V1.8 §2's requirements per the drafting
thread's account, and the V1.8 citations are now gone. Delivering more than
the governing spec requires is not a defect and I am not asking for anything
to be removed. It is worth naming only so that a future reader does not wonder
which document those sections answer to, and so that the V1.8-versus-V1.5
question Mark has to settle is understood to include "V1.5 asks for less than
this world's Doc_02 actually did."

One related tension, noted for completeness: V1.5's same row requires that
"every load-bearing caveat (do-not-cite flags, pending-verification lists)" be
"written as its OWN row field, not prose." The Registry currently carries its
caveats as prose inside the Licensed For and Verification Note cells, and R2's
Confidence cell holds prose around the letter. Fixing Finding 29's Registry
problem and this together would be one edit rather than two.

**The three escalations exist only inside this world's folder.** Step 0 §5,
Doc_01 §13 and Doc_02 §16 each name them — the fabricated citation's origin
and whether the underlying editorial practice should become a real INTAKE.md
rule; whether V1.8 or V1.5 governs and when V1.8 merges; and the census's own
overstated `floorNote`/`statusDescription`. `grep` finds no corresponding
entry anywhere in `Ministry/`. Disposition has not been reached, so the
build-cycle skill's "Log it" step is not yet due, and a build thread has no
reliable channel to Mark of its own. I note it only so the escalations are not
assumed delivered because they are written down. They are written down; that is
not the same thing.

---

# 7. What a third round needs to do

Small, specific, and all of it mechanical except the last:

1. **Strip revision-history narration from `obel_Source_Registry.md`** —
   header, status line, the eight row-level "corrected Round 2, Finding N"
   parentheses, and the footer. Keep every correction; move the account of what
   an earlier draft said to `Open_Gaps_Tracking.md` and this review file. Move
   the "Living-document protocol" argument out of the canonical artifact.
   (Finding 29)
2. **Move the four surviving narration instances out of Step 0 and Doc_02** —
   Doc_02 §16, Doc_02 §15, Step 0 §5's reasoning, Step 0 §1's aside. (Finding 29)
3. **Restore `Open_Gaps_Tracking.md` entry 10's original text verbatim** from
   `0370466`, keeping the Round 2 correction appended below it; delete the
   placeholder sentence that claims the text was left in place. (N10)
4. **Append corrections to Open_Gaps entries 5 and 1** — entry 5 for the p. 33
   locus and the now-settled translation question, entry 1 for the V1.8
   deferral. (Findings 7, 14, 20)
5. **Delete or create the "final handoff report" Doc_01 §13 cites.** (N3)
6. **Correct "roughly ninety" to 116** in all seven locations. (N2)
7. **State the transcription convention once** — Doc_02 §7 or Registry R1 —
   covering the OCR repairs and punctuation normalization. (N1)
8. **Fix Doc_02 §5's and the "Built from" block's tooling claims** to what can
   actually be run; the figures stay. (N8/§5(g))
9. **Narrow Doc_01 §8's "same window"** to the one genuinely overlapping
   candidate, and name `ijc` in the same-lane enumeration. (N4, N5)
10. **Split the "по римской бляди… духу и от сына" ellipsis** into two
    introduced quotations, and delete Registry R1's dangling "see R-note
    below." (§4, N7)
11. **Put N6 to Mark** rather than resolving it: does naming a
    governance/methodology escalation in a document's own Disposition section
    bar that document from self-disposing under CO-022? The build thread has
    answered no, in the document; the skill's text reads yes. That is a
    governance question and therefore not the build thread's to settle.

Items 1–10 are cosmetic-to-mechanical in execution and none of them touches a
substantive claim, so a targeted third round should be short. Item 11 is
Mark's.

---

# 8. Note on this recheck's own standing

This file is the Round 2 recheck artifact for Step 0, Doc_01 and
Doc_02/Registry. It is **not a ruling** and it does not dispose of anything.
Per the `cic-build-cycle` skill, no document may be dispositioned on the
strength of its reviewer's own reading, a build thread never assigns Frozen,
and the three escalations these documents name remain open with Mark.

It is a **targeted recheck**, not a fresh audit: I checked the current state of
the four documents against Round 1's 29 findings at the locations those
findings name, checked the diff for newly introduced errors, and independently
re-verified every quotation and locus now stated. I did not re-audit the
sections Round 1 cleared — Doc_02 §3's corpus-map schema reasoning beyond the
`fixture-synthetic.yaml` header check, §6's thin-evidence calibration, §10's
Missing Voices assessment, §11's asymmetry statement, §12's forces lens, and
Doc_01 §6's strand reasoning — and a reader should treat those as carrying
Round 1's assessment, not a second one. Round 1's own §6 recommended that a
remaining review budget be spent on Doc_02 alone; if a third round clears the
hygiene items above, that recommendation is still the better use of the next
pass than another combined sweep.

Reviewer modified no file other than creating this one.
