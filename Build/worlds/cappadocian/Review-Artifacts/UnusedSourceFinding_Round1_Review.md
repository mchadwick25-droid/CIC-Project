# Unused-Source Finding — Round 1 Independent Adversarial Review

**Document under review:** `Build/worlds/cappadocian/cappadocian_Unused_Source_Verification_2026-09-09.md`, together with the whole change set it dispositions (7 modified files, 2 new records).
**Reviewer stance:** Independent adversarial. Did not author the document or any part of the change set; no stake in its passing.
**Review date:** 2026-09-09.
**Branch reviewed:** `claude/cappadocian-unused-source-finding` (default branch `main`).
**Methodology consulted:** `cic-build-cycle` SKILL.md (four escalation categories; cross-document fact consistency; scope of a build thread's write access); `cic-gravity-index` SKILL.md (its "What an independent review of gravity-discovery work must check" list — note that this skill file is **truncated mid-sentence at line 49** in this environment, so the checklist may be incomplete); `Build/reference/L3B-World-Build-Methodology/Source_Registry_Template.md`; `CAPPADOCIAN_BUILD_LEDGER.md` §§45–49; `cic/corpus-map/README.md`.

---

## VERDICT: **SUBSTANTIAL REVISION REQUIRED**

Twelve substantial findings. The document's headline judgment — that the Amphilochius availability claim was false and needed correcting — is **correct, and I independently confirmed it against the file**. Three of its four other dispositions are also broadly right, and its restraint on Doc_04 reaches a defensible conclusion. But the correction that this document exists to make repeats, inside itself, the exact defect class it was written to condemn: **its central quantitative claim about the Amphilochius extract ("roughly 240 words in Amphilochius' own voice") was taken from the corpus-map row's own `locus` string, not measured from the file.** The true figure is 129 words in the extract's body, of which 39 are the NPNF editor's bracketed summary — about 90 words of Amphilochius. That claim now stands in four places.

Alongside it: the new row 117 is graded **A** in direct contradiction of the Source Registry's own written A–B rule; the new source record is `verified-direct` against this world's own established mapping rule and the ledger §47 precedent that corrected exactly this move; §5's assertion that `staleness-check` "passes for all eight registry entries" is **false as delivered** (I re-ran it: `pass: false`, cappadocian stale) and contradicts the document's own §6.1; the Registry's new log entry cites `CAPPADOCIAN_BUILD_LEDGER.md` **§50**, which does not exist and was never written; the twice-stated exculpation "three review rounds ... could not have" caught the Amphilochius error is **demonstrably untrue** — the Registry's own rows 60 and 78 already point into the very volume the extract sits in; and the cross-document sweep the build-cycle skill requires was not run, leaving at least six live occurrences of the corrected claims uncorrected across Doc_01 §4a, Doc_02 §2, Doc_02 §1.4, the Forces Document, the Integrated Ecology Analysis, and the G1 manifest.

None of this touches the honesty of the document's intent, which is high. It touches its execution, which does not meet the standard the document itself sets in its opening paragraph.

---

## PART ONE — WHAT I INDEPENDENTLY VERIFIED, AND HOW

Everything below was checked against the actual file, command output, or branch, not against the document's description of it.

**The Amphilochius extract.** Opened `cic/texts/npnf214_seven-ecumenical-councils.xml` and read `div2` id `xvii.xxiii` in full (lines 44075–44103), plus its endnote 603 and the sibling Gregory-Theologus section `xvii.xxii` for contrast. Counted words programmatically, with and without the bracketed stretches. Read `cic/corpus-map/cappadocian-nicene-pastoral-monastic-tradition.yaml` lines 6–15 for the row and its date.

**The Macrina quote.** Opened `cic/texts/npnf208_basil-letters-select-works.xml`. Word-for-word compared the record's `text` against lines 37060–37065 (`ix.ccv-p26`). Located the letter's prefatory note (endnote 2734, at lines 36847–36858) and read the "passages in brackets are Newman's version" statement in situ. Traced the bracket boundaries by reading lines 37050–37070 continuously. Confirmed element ids `ix.ccv`, `ix.ccxi`, `ix.ccxxiv` against their printed headings. Read Letter CCX (`ix.ccxi`) in full for Gregory-Thaumaturgus content, and the prolegomena citation at line 952 with its endnote.

**CTh 16.1.3.** `git ls-tree -r --name-only origin/main -- cic/texts/` — the three named files are absent (71 files, none of them). `git fetch --depth 1 origin donatism-lpc-integration`; `git ls-tree -r --name-only FETCH_HEAD -- cic/texts/` — all three present. Extracted both Latin witnesses and diffed the document's quoted clause word-by-word against the Latin Library text (65 words each way). Read Mommsen–Meyer at the rubric `XVI, 1, 3 (381 Iul. 30)` including its apparatus. Read Boyd at the footnote and checked its page position against the surviving running heads.

**Compile and gates.** Ran `python -m engine.m2.cli build cappadocian` (package `2026-09-09T01-33-13Z`), read `validation/gates-report.json` in full, ran `determinism-check` and `staleness-check`, and ran `pytest engine/m1/tests engine/m2/tests`. Read `engine/m1/gates.py::gate_voice_perspective` and `_PERSPECTIVE_FIELDS` to establish whether the failing gate is per-record. Read `engine/m2/tests/test_restore.py` to test the clone-artifact explanation against the test's own assertions. Read the package `manifest.json` and `compiled/coverage.json`.

**Corpus map.** Read `cic/corpus-map/README.md`, the two `_staging` files at the specific rows named, and grepped the generated bucket file for the two works.

**Cross-document sweep.** Grepped `Build/worlds/cappadocian/`, `records/cappadocian/`, and the seven `cappadocian*ctx*/lex*/story*` deployment chunks for every form of the three corrected claims.

**One environment note for the record, disclosed rather than smoothed over.** During this review the working tree was committed as `88f9dd4` by a process other than me (the message is the build thread's own), and the two package directories the change set had produced (`2026-09-09T01-19-58Z`, `...T01-25-33Z`) disappeared from `packages/cappadocian/` between my first `git status` and my second command. I could not therefore inspect the build thread's own baseline package. I compensated by establishing the pre-existing gate failure analytically (see CLEARED item 12) rather than by rebuild, since two attempts to construct a clean baseline tree (`git checkout <sha> -- records/cappadocian`, `git worktree add`) were both refused by this environment's permission layer. `git diff f07eb91 88f9dd4` is byte-identical to the change set I reviewed, so no content was lost.

---

## PART TWO — FINDINGS

### 1. [SUBSTANTIAL] The "roughly 240 words" figure is wrong by ~2.7x, and was taken from the corpus map rather than measured from the file — the same defect class this document exists to correct.

**Location:** verification document line 79; `records/cappadocian/source/cappadocian.source.amphilochius-iambics-to-seleucus.md` line 47; `cappadocian_Source_Registry.md` row 117 (line 217, "Roughly 240 words"); `cappadocian_Doc_02_Source_Ecology.md` §1.6 (line 51, "roughly 240 words at div2 17.23"); `records/cappadocian/figure/cappadocian.figure.amphilochius.md` line 14 ("roughly 240-word extract").

**What I measured.** The extract's body is the single paragraph `xvii.xxiii-p4`. Stripped of markup it is **129 words**. Of those, **39** are the NPNF editor's own bracketed summary in the third person ("[Then follows a list of the proto-canonical books of the Old Testament, Esther alone being omitted. All the deutero-canonical books are omitted. He then continues]" — 25 words; "[Then follow all the books of the New Testament except the Revelation. He continues,]" — 14 words). **Amphilochius' own rendered voice is about 90 words.**

**Where 240 came from.** `cic/corpus-map/cappadocian-nicene-pastoral-monastic-tradition.yaml` line 9 reads `locus: div2 17.23 (~242 words)`. My own count of the *entire* `div2` element — heading, the "VIII." numeral, endnote 603, the body, and the editor's separate closing "Note." paragraph about there being four or five different canons — is **243 words**. The corpus map counted the whole element; the verification pass reproduced that number and attached it to the phrase "in Amphilochius' own voice."

**Why this is substantial.** Row 117's Verification Note says the extract's "heading, locus ... and wording [were] all checked against the file itself rather than against any prior document's description of it." The word count was not. This is precisely the failure the document's own §0 says a verification pass must not commit ("a verification pass that only confirms what it was handed has not verified anything"), and it is now propagated into two cleared world-build documents, the Registry, and two compiled records.

**Recommended fix.** Replace "roughly 240 words" everywhere with the measured figure and the honest split — e.g. "129 words as printed, of which 39 are the editor's bracketed summary; about 90 words of Amphilochius' own rendered voice." State in row 117's note that the corpus map's `~242 words` counts the whole `div2` including apparatus.

---

### 2. [SUBSTANTIAL] The extract is described as containing an enumeration of the biblical books and as "verse." It contains neither.

**Location:** source record line 47–52; Doc_02 §1.6 line 51; figure record body ("a verse list of which books of Scripture may be trusted").

**What the file actually holds.** The book-lists are exactly the material the editor removed. What stands in their place is his bracketed statement *that* a list follows in the original. No Old Testament book is named. No New Testament book is named. The record's "WHAT IT IS" paragraph — "an enumeration of the Old Testament proto-canonical books with Esther omitted ... the New Testament books with the Revelation similarly held back" — describes the *original poem*, not the held text, and reads as a description of what a builder could quote.

Nor is it verse. Endnote 603 reads: *"I have substituted my own Epitome, in the room of Johnson's, translating the original as it is found in Beveridge's Synodicon, Tom. II., p. 179."* Compare the immediately preceding section (`xvii.xxii`, Gregory Theologus), where the same editor writes: *"Not being satisfied with Johnson, I have supplied a translation from Beveridge."* The editor draws the distinction himself: for Gregory he supplies a **translation**; for Amphilochius he supplies **his own epitome**. What is vendored is an editorial prose abridgement, not the Iambics. Doc_02 §1.6's "one genuine extract of his own verse is vendored and readable" is therefore not accurate, and neither is the figure record's "a verse list."

**Recommended fix.** Say what is held: an editorial prose epitome of roughly 90 rendered words of Amphilochius, with the book-lists replaced by summary. Drop "verse" and "enumeration" from every description of the held text; if the original's verse character is worth stating, state it as a fact about the poem, explicitly distinguished from what this build holds.

---

### 3. [SUBSTANTIAL] Row 117's Confidence A violates the Source Registry's own written A–B rule, and is inconsistent with the same pass's treatment of rows 11, 66 and 69.

**Location:** `cappadocian_Source_Registry.md` row 117 (line 217); the rule it breaks is at line 14 of the same file.

**The rule, quoted from the document being amended:** *"Citation Reliability A is reserved for sources this build session itself directly verified — the files Mark supplied 2026-08-30/31 (nine Registry rows' worth: rows 18, 21, 22, 33, 48, 57, 63, 71, 72)... **Sources vendored in earlier sessions for other worlds (the NPNF/ANF volumes, present in `cic/texts/` since 2026-08-15) are real and usable but were not re-verified by this session — they are rated B, not A, on that basis alone**, regardless of how solid their content actually is."*

Row 117 is inside `npnf214_seven-ecumenical-councils.xml`, one of exactly those pre-vendored NPNF volumes — the new source record's own `rights_status` says so ("present in the shared library since 2026-08-15"). Row 117 justifies its A as "per this Registry's own rule (a source this session itself directly verified in the file)," which quotes the first clause of the rule and drops the second, which is the operative one.

**The internal inconsistency clinches it.** The Registry's own new log entry (line 239) says the same pass "also verified rows 11, 66, 69, and 79 directly against their own files; all four held." All four remain at **B**. The same evidentiary act therefore yields B for four rows and A for one, in one pass, with no disclosure. Note also the Registry's own claim at line 14 that "The independent review checked every Confidence-A row against this rule directly and found no violations" — that is no longer true of this Registry.

**Recommended fix.** Regrade row 117 to **B**, and record why in the note. If the build genuinely believes the rule should now key off *when a verification happened* rather than *which vendoring batch a file came from*, that is a change to the Registry's own governing rule and belongs in escalation category 3 (governance/methodology), not in a row's confidence cell.

---

### 4. [SUBSTANTIAL] `verification_state: verified-direct` on the Amphilochius extract contradicts this world's own established mapping rule and the ledger §47 precedent that corrected exactly this move.

**Location:** `cappadocian.source.amphilochius-iambics-to-seleucus.md` line 11.

**The precedent, from `CAPPADOCIAN_BUILD_LEDGER.md` §47:** a cold review found `cappadocian.quote.basil-against-delaying-baptism`'s `verified-direct` "overselling this record's own actual provenance — the quoted sentences survive only as the NPNF editor's own selected citation embedded in the Prolegomena's scholarly survey, not as the homily's own complete, independently-checkable text." It was corrected to `verified-via-authority`, "matching this world's own established mapping rule (**direct primary-text access earns verified-direct; content resting on a citing authority's own selection earns verified-via-authority**)."

The Amphilochius case is the same shape and, if anything, further from direct: the Greek Iambics are not vendored anywhere; what is held is not even the editor's *selection* from a complete text but his own declared **Epitome** — an abridgement he made, with two stretches replaced by summary in his own third-person voice. The build thread read the vendored NPNF file directly, which is true and worth saying; but under this world's own rule, reading the vendored file directly was already ruled insufficient when the content is the citing editor's own production.

The record's `divergence_note` states the epitome limit honestly and well. That is the right content in the wrong field: the limit belongs in the `verification_state` too, exactly as §47 ruled.

**Recommended fix.** `verified-via-authority`, with the divergence note left as it stands and a sentence added naming the §47 precedent. Note that this compounds Finding 3: a record at `verified-via-authority` cannot easily support a Registry row at A.

---

### 5. [SUBSTANTIAL] "Three review rounds ... could not have" caught the Amphilochius error is false. The contradicting evidence sat inside a volume the Registry itself already cites twice.

**Location:** verification document line 83 ("They could not have. The contradicting evidence was in neither the Registry nor Doc_02; it was in a shared corpus-map file that neither document cross-checks"); repeated in the Registry's new log entry, line 239 ("did not catch this one, and could not have").

**What I found.** `cappadocian_Source_Registry.md` **row 60** (Gangra canons) and **row 78** (Constantinople 381 and its creed) both locate their sources "within `cic/texts/npnf214_seven-ecumenical-councils.xml`." The 2026-08-31 sweep record (`cappadocian.search.unopened-volume-sweep`) names the same volume explicitly in its own result note: *"the conciliar volume npnf214 (rows 60, 78)."* The extract is in that volume, four `div2` sections after the Basil canonical letters to Amphilochius (`xvii.xi`ff.), in a run that also contains "From an Epistle of the Same to the Blessed Amphilochius" (`xvii.xiv`) and "From Chapter XVII. of the Book St. Basil Wrote to Blessed Amphilochius on the Holy Ghost" (`xvii.xix`). A single `grep -n Amphilochius` on a file the Registry already cites returns the heading.

The corpus map was not the only route, and it was not the shortest one. This matters because the exculpation drives the document's own stated lesson (§3: "a process gap between two layers, not a research failure inside one"), its §6 item 4 ("nothing currently cross-checks this world's own availability claims against the shared corpus map"), and the standing check it recommends. The actual lesson is narrower and harder: an availability claim on a row (65) was never checked against a volume already sitting in the same Registry two rows-groups away. A corpus-map cross-check would be useful; it is not what was missing here.

**Recommended fix.** Withdraw "could not have" in both places. State what I found: the extract was reachable from the Registry's own rows 60/78 by opening a vendored file the Registry already cites. Rewrite the standing-check recommendation accordingly — the check that would have caught this is "every row asserting a source's *absence* gets a direct search of the vendored volumes this Registry already names," which is cheaper and more general than a corpus-map join.

---

### 6. [SUBSTANTIAL] §5's claim that `staleness-check` "passes for all eight registry entries" is false as delivered, and contradicts the document's own §6.1.

**Location:** verification document line 121.

**What I ran, on the delivered state:**

```
$ python -m engine.m2.cli staleness-check
{ "pass": false, "worlds": { ... "cappadocian": { "stale": true, "diff": [
    "compiled/coverage.json", "compiled/prompt.txt", "compiled/quotes.json",
    "compiled/repository.json", "manifest.json",
    "records/doctrinal_witness/cappadocian.dw.how-it-reached-us.md",
    "records/figure/cappadocian.figure.amphilochius.md",
    "records/quote/cappadocian.quote.macrina-the-elder-taught-me.md",
    "records/source/cappadocian.source.amphilochius-iambics-to-seleucus.md",
    "records/source/cappadocian.source.amphilochius-of-iconium-own-works.md",
    "records/source/cappadocian.source.basil-macrina-the-elder-letters.md",
    "records/source/cappadocian.source.imperial-communion-law-of-381.md" ] } ... } }
```

Every other world is clean; cappadocian is stale on exactly the seven records this change set touched, against the pin `packages/cappadocian/2026-09-04T16-41-51Z` in `records/worlds.yaml` line 203.

This is not a surprise — it is the necessary consequence of §6.1, which correctly says "the current pin ... does **not** contain them." The two statements cannot both be true. §5 presents its contents as measured state ("The pre-existing failure is stated as pre-existing because it was measured that way"), so a reader is entitled to read the staleness line as measured on the delivered state, and it was not.

**Recommended fix.** State it correctly and make it useful: "`staleness-check` now reports `pass: false` with cappadocian stale on the seven touched records — the expected and intended consequence of §6.1's deferred re-pin, and the mechanical signal that the re-pin is owed." Left as written, the document's own §5 conceals the one measurement that proves §6.1's point.

---

### 7. [SUBSTANTIAL] The Registry's new log entry cites `CAPPADOCIAN_BUILD_LEDGER.md` §50. It does not exist, and no ledger entry was written.

**Location:** `cappadocian_Source_Registry.md` line 239, "(see `CAPPADOCIAN_BUILD_LEDGER.md` §50)".

The ledger's section headings run 1 through **49** (`## 49. card_name CONFIRMED ... (2026-09-02)`, line 789 — the last heading in the file). The ledger is not in the change set at all. So the Registry now points a reader at a section that has never been written, and the verification document's §5 promise about the `voice-perspective` false positive — "It is named for the ledger instead" — is unfulfilled: it is named in this document, and nowhere in the ledger.

This is a live-document cross-reference error of exactly the class the Registry's third and fourth review rounds were built to eliminate ("every 'row N' and 'rows N–M' cross-reference in the document was checked by directly reading the target row's own content"), reintroduced by the same document.

**Recommended fix.** Either write ledger §50 (which the build-cycle skill's Disposition section requires anyway: "Log it: document name, review outcome, how many revision rounds it took, where each review artifact file lives, and which disposition it received"), or drop the forward reference until it exists. Writing it is the better option, since §5's `voice-perspective` hand-off and §6's four open items currently have no home outside this one document.

---

### 8. [SUBSTANTIAL] The cross-document consistency sweep the build-cycle skill requires was not run. At least six live occurrences of the corrected claims are untouched, and one of them now contradicts a record this pass edited.

The skill's rule: *"When two documents in the same world's build state the same specific claim ... drawn from the same underlying source material, check that they actually match, or that any difference is deliberate and disclosed."* Its Naming and term propagation rule: *"check every file it appears in ... before treating the change as complete."*

**a. The four-versus-eleven correction was applied to one field and not to the rest.** Inside the very record it edited, `cappadocian.source.imperial-communion-law-of-381.md` line 28 still reads `work: The imperial communion law of 381 ..., naming Helladius, Otreius, Gregory of Nyssa, and Amphilochius` while its new `divergence_note` (line 12) opens "The law names eleven bishops, not four." One record, two answers.

**b. `cappadocian_Source_Registry.md` row 79** (line 145) still carries the four-name framing in its Licensed-For cell and still says "the Mommsen–Meyer Latin text is public domain but not acquired into `cic/texts/` this session" with `named-not-rechecked` implied throughout — while the Registry's own new log entry two hundred lines below says row 79 was "verified ... directly against [its] own file" and "upgraded to verified-direct" in its record. Row 79 itself was not edited.

**c. `cappadocian_Doc_01_World_Identification.md` §4a, line 96:** *"The 381 communion law naming this world's own bishops (Helladius of Caesarea, Gregory of Nyssa, and Amphilochius of Iconium) as **the empire's own standard** is the clearest documentary marker of this shift."* Three names, and the unqualified "the empire's own standard" — which is the exact construction §1.2 of the verification document calls an overstatement in the discovery pass's framing. §1.2 praises Doc_02 §2's "among" and does not look at Doc_01 §4a, which it names two sentences earlier as one of the places the law is already carried.

**d. `cappadocian_Doc_02_Source_Ecology.md` §2, line 57**, the sentence the document endorses, continues past the part it quotes: *"Amphilochius' inclusion is the strongest support for this document's own conclusion that **'the world's own men made the empire's standard'**."* The careful "among" and the strong claim are in one sentence; the review read the first half.

**e. `cappadocian_Integrated_Ecology_Analysis.md` line 139:** *"the 381 communion law (CTh 16.1.3) **makes this world's own bishops the empire's legal touchstone**."* Unqualified, in a live cleared document, and now in direct tension with the source record's new instruction that the claim "should be cited as the bounded version."

**f. `cappadocian_Forces_Document.md` line 114** names three bishops ("Helladius of Caesarea, Gregory of Nyssa, Otreius of Melitene") and omits Amphilochius — a different three-name set from Doc_01 §4a's, which omits Otreius. Doc_02 §2 names four. No document names eleven.

**g. `cappadocian_Doc_02_Source_Ecology.md` line 37** tells the reader to "see §2 for the law's own **full citation and bishop list**." §2 gives four names and no citation of the Latin. That pointer was wrong before this pass and is still wrong after it, in the one pass that finally had the full list in hand.

**h. `cappadocian_G1_Scope_and_Source_Acquisition_Manifest.md` line 92** still lists "Amphilochius of Iconium's genuine works" among the honest gaps with no acquisition, alongside Epiphanius' *Panarion*. This is the same manifest whose "Honest gaps" line 85 the Registry's own fifth-pass log entry treats as the authority that should have caught rows 16 and 20. It was not checked here.

**i. Registry row 11 (line 50) and Doc_02 §1.4 (line 42)** both cite "Epp. 204 and 223"; the edited source record now cites 204, 223 **and 210**. §4 of the verification document discloses the difference in its own prose — good — but neither of the two documents that state the claim was updated or annotated, so the disclosure lives only in a document a reader of the Registry will not necessarily open.

**Recommended fix.** Run the sweep. At minimum: fix (a) and (b) — a record contradicting itself and a Registry row contradicting its own log are not deferrable; and decide explicitly whether (c)–(f) are corrections this build thread makes or an escalation, saying which.

---

### 9. [SUBSTANTIAL] The Doc_04 argument answers only the elevation question. Open Item 1 asks the opposite one, and the same evidence pushes that way.

**Location:** verification document §1.3, lines 38–47.

The argument's structure is: (i) the Primary/Supporting question turns on the Formation score alone; (ii) CTh 16.1.3 is "recognition and property," not formation; (iii) therefore no change; plus (iv) "corroborating evidence cannot raise a score that is already at maximum."

**Premise (i) I checked and it holds.** Doc_04 §3.2's candidate-8 bullet and §4's index row both name the Formation moderation as the sole reason the Supporting alternative is flagged. Fair.

**Point (iv) is a non-sequitur for the question actually open.** Doc_04 §9 Open Item 1 asks whether Gravity 3 should be **Supporting** — a downgrade. "Corroborating evidence cannot raise a score already at maximum" answers an upgrade question nobody asked. The document never turns the argument around and asks whether the new reading strengthens the downgrade case. It should have, because it does: the argument at (ii) is itself a downgrade argument. If the gravity's culminating documentary act is an instrument of recognition and property that touches no formation practice, that is evidence the gravity organizes the world's *situation* rather than its *formation* — which is the substance of the Supporting case. The document converts this into "the law strengthens the annotation" (line 44). The annotation sits inside Primary; the same fact sits equally comfortably inside Supporting. Asserting the first without disposing of the second is the gap.

**Premise (ii) is too clean, and the document's own strongest line hides the middle term.** "A law that changes who holds the basilica does not change whether the plateau farmer's becoming ran through the imperial contest." But Doc_04 §3.1's Formation moderation rests on a specific list of instruments: "household teaching, **baptism**, psalmody, **festival**, brotherhood and alms." Two of those six happen in the buildings the law reassigns, administered by the clergy whose communion the law makes the test. A law that hands every church in the eastern dioceses to bishops of a named communion changes *who baptizes* and *who preaches at the panegyris*. Whether that is "conditioning" or "constituting" is exactly the argument at issue — and it is not made. The word "property" does the work that an argument should.

**The `cic-gravity-index` checklist item that was not run.** That skill requires, of any review of gravity work, that "the Confidence/Gravity Cross-Check [was] applied to every Primary classification specifically." Gravity 3's Cross-Check (§3.2) rated its evidence "Documented" under Doc_04 §9 Open Item 9's blanket caveat that "nothing in this build has been verified against editions or external scholarship." This pass has, for the first time, verified one of that gravity's instruments against two editions. That moves the evidential-confidence side of the Cross-Check axis. The document does not mention the Cross-Check at all — not even to say "no change." Given that this pass also does not update Open Item 9, Doc_04 now carries a systemic caveat that is no longer wholly true and a Cross-Check that was not revisited when its input changed.

**Recommended fix.** Add the downgrade analysis explicitly and reach a stated conclusion on it. Engage the baptism/festival objection rather than routing around it. Either re-run the Cross-Check for Gravity 3 and record "no change, and here is why," or say plainly that it was not re-run and why that is acceptable. If the honest answer is that the law makes the Supporting case marginally stronger without being decisive, say so — that is a finding, and Open Item 1 stays open either way.

---

### 10. [SUBSTANTIAL] The Open Item 2 contribution does not do the work it is credited with, and points the other way.

**Location:** verification document line 47; carried into `cappadocian.source.imperial-communion-law-of-381.md` body, closing paragraph.

Doc_04 §9 Open Item 2 states the exposure precisely: *"much of what is here called 'the world's' is documented only in the circle's record. Bears most heavily on Gravities 6 and 8."* That is a **representativeness** problem: does the circle's record stand for the world beyond the circle?

An imperial list naming four circle members as the communion test is external evidence that **the circle was prominent**. Nobody has ever doubted that. It says nothing about the plateau beyond them — and if anything it *sharpens* the exposure, because a circle written into the empire's own communion test is exactly the kind of unusually well-placed group whose surviving record is least likely to be representative. The document half-concedes this ("the law attests the circle's *standing*, not the world's formation ecology beyond the circle") and then keeps the credit anyway, calling it "a real, if small, external datum against a risk that has had almost none."

It is not a datum against that risk. It is a datum about a fact the risk presupposes. And the record now carries the claim in compiled content: "which bears on Doc_04's standing Open Item 2 (the circle-versus-world exposure)."

**Recommended fix.** Either drop the Open Item 2 attribution from the record and the document, or restate it accurately: external, non-circle confirmation of the circle's public standing — which is worth having on the record, is *not* progress against the circle-versus-world exposure, and arguably tightens it. Note also that Open Item 2 names Gravities 6 and 8 as where the exposure bites; the law bears on neither.

---

### 11. [SUBSTANTIAL] The C-E fit argument is contradicted by the next clause of the same sentence — a clause the record itself quotes when marking the bracket boundary.

**Location:** `cappadocian.quote.macrina-the-elder-taught-me.md`, body, "WHY C-E" paragraph (line 87ff.); `cappadocian.dw.how-it-reached-us.md` `positions`.

The C-E witness's `positions` field — which **is** compiled into the voice; I confirmed it in `compiled/repository.json` — includes: *"what reached us was an already-completed deposit — scripture, creed, and baptismal formula — **not a personally gathered testimony**."*

The quote's `text` stops at "upon the doctrines of piety." The source sentence does not. It continues, in the same bracketed Newman stretch: *"And when I gained the capacity of thought, my reason being matured by full age, **I travelled over much sea and land, and whomsoever I found walking in the rule of godliness delivered, those I set down as fathers**, and made them my soul's guides in my journey to God."*

That is personally gathered testimony, stated in the first person, in the same breath as the sentence being used to close the cell. And the record's own verification note quotes the clause — it uses "those I set down as fathers" to mark where the Newman bracket closes. So the drafting read it and did not notice that it cuts against the cell's second position.

The fit argument as written ("that specifies the cell rather than contradicting it") is defensible for the `text` field's own claim, and the "not from an eyewitness" qualifier in the dw's `text` genuinely absorbs the Thaumaturgus chain. It is not defensible for the `positions` line, which is unqualified and which the voice will speak. A participant asking C-E's own retrieve_when question ("how the faith actually reached the people of this world, in concrete terms") can now be handed both.

**Recommended fix.** Not necessarily to remove the quote from C-E — the pairing is genuinely illuminating. But the tension must be named where it is load-bearing: either extend the quote's `text` to include the travelling clause and let the cell carry both halves honestly, or add the tension to the dw's `tensions` field, or qualify the `positions` line. Silently truncating a quote one clause before it complicates the cell it is placed in is the move this project's discipline exists to prevent.

---

### 12. [SUBSTANTIAL] The scope-discipline argument at §2 misreads the skill it cites, and is applied inconsistently with what this same pass actually did.

**Location:** verification document lines 65–66.

**a. The skill's scope rule is about a named class of governance files, not "anything outside my folder."** `cic-build-cycle` SKILL.md: *"Editing authority over **non-world-build files — the Construction Framework, the Representative Construction Framework, the Build Protocol, the Change Orders Register, and the L3B/L4 templates** — belongs to a coach thread, not a build thread. A build thread's write access is scoped to its own world's build folder."* The second sentence is a gloss on the enumerated first. `cic/corpus-map/_staging/` is not on that list and is not that kind of file.

**b. The pass applied the rule selectively.** This change set edits five files under `records/cappadocian/` and creates two more. `records/` is also outside `Build/worlds/cappadocian/`. If the sentence means what §2 says it means, the quote record and the source-record edits were equally out of scope. They were not treated that way, and rightly — but then the rule cannot bear the weight §2 puts on it for the corpus map.

**c. Escalation category 2 does not fit the Thaumaturgus edit by its own definition.** The category is *"Portfolio-level or cross-world strategic decisions — anything decided **for a reason external to this specific world's own ecology**."* The document's own rationale for the Thaumaturgus edit is Doc_02 §1.6 and Doc_01 §4 — this world's own ecology, explicitly. "Touches a shared file" and "decided for a reason external to this world's ecology" are different tests, and §2 substitutes the first for the second.

The Firmilian escalation is a different matter and I would sustain it: splitting a work out of a letters-corpus row against that file's own stated granularity rule is a precedent call, and the `npnf214` split's own note ("Split 2026-08-26 on Mark's ruling") is a real precedent for taking it up. That half is right.

**Recommended fix.** Either make the Thaumaturgus edit (with the correction in Finding 13 applied), or decline it on a ground that survives reading — e.g. "the `_staging` files are owned by the assignment thread by convention and I am not that thread," which is a coordination argument, not a scope-of-authority one, and should be labelled as such.

---

### 13. [SUBSTANTIAL] The Thaumaturgus edit as specified is not correct as written: it would give the Cappadocian assignment `assigned` confidence, against the two sibling rows' deliberate `provisional`.

**Location:** verification document line 69 (the specified edit); `cic/corpus-map/_staging/anf06_gregory-thaumaturgus-...yaml` lines 32–92.

The `Canonical Epistle` row (line 80) carries `confidence: assigned`. A row has one `confidence` value for all its `atlas_ids`. Adding `cappadocian-nicene-pastoral-monastic-tradition` to that row therefore lands the Cappadocian assignment at `assigned`.

Both sibling Thaumaturgus rows that carry the Cappadocian id are at `confidence: provisional`, and both say why in their own notes: *"provisional because he predates the entry's 360-380s range by a century"* (The Oration and Panegyric, line 51); *"No census entry for 3rd-c. Pontus itself"* (A Declaration of Faith, line 66). That reason applies with identical force to the Canonical Epistle. The file's own header notes say the same thing at volume level: *"3rd-c. Pontus (Gregory Thaumaturgus): no census entry; the Cappadocian entry (c. 360-380s) venerates him as its forerunner and is used as the shelf."*

The file also shows the mechanism for this case: "The Oration and Panegyric Addressed to Origen" appears as **two rows**, one per atlas entry, precisely so the two assignments can carry different confidences. So the doc's claim that the one-line addition is "consistent with the two sibling Thaumaturgus rows" is not right — those rows use a different shape, for a reason that applies here.

Two smaller points in the same passage: the "non-exclusive by default" rule the document attributes to "the file's own stated" rule is stated in `cic/corpus-map/README.md`, not in the `_staging` file; and "The Epistles of Cyprian" is not one row assigned to three entries but **two** rows (`[latin-pastoral-congregational-christianity, novatianism]` role `tradition`; `[donatism]` role `antecedent`).

**Recommended fix.** Specify the edit as a **second row** for the Canonical Epistle: `atlas_ids: [cappadocian-nicene-pastoral-monastic-tradition]`, `role: tradition`, `confidence: provisional`, with the century-gap reason carried in the note — matching its two siblings exactly. As specified, the edit is not "trivial to apply."

---

### 14. [SUBSTANTIAL — narrow] Epistle 210 is mischaracterized. It does carry the transmission of Thaumaturgus' teaching; what it does not carry is Macrina as the link.

**Location:** verification document §4; `cappadocian.source.basil-macrina-the-elder-letters.md`, "A THIRD PASSAGE THIS ROW DID NOT NAME."

The record says Ep. 210 "establishes the upbringing but not the transmission of Thaumaturgus' teaching, which is the part that makes this datum load-bearing." I read Letter CCX (`ix.ccxi`) in full. Its §3 is *about* that transmission and is one of the sharpest statements of it in the corpus: *"There is going on among you a movement ruinous to the faith ... disloyal too to **the tradition of Gregory the truly great**, and of his successors up to the blessed Musonius, whose teaching is still ringing in your ears"* (endnote 2772: "i.e. Gregory Thaumaturgus"), followed by a long discussion of Gregory's ἔκθεσις τῆς πίστεως with a cross-reference to Ep. 204 itself.

So Ep. 210 is a *stronger* third witness than the record allows, on a different axis: it independently establishes the Neocaesarean Thaumaturgan transmission chain that Ep. 204 routes through Macrina. What it lacks is Macrina in the chain. As written, the record understates a source it has just read, which is an unusual direction for an error but still an inaccurate characterization of a witness.

**Recommended fix.** One clause: "it establishes the upbringing, and independently the Thaumaturgan tradition at Neocaesarea (§3), but not the two joined — Macrina is not named as the link there, which is the part that makes this datum load-bearing."

---

### 15. [COSMETIC] The prolegomena cites three letters, not two.

The volume's biographical prolegomena (line 952, endnote 21) reads *"Epp. cciv., ccx., ccxxiii."* — 204, 210 **and** 223. The verification document (§4) and the record both say it "cites Epp. 204 and 210 together." Harmless to the argument, but it is a claim about what a file says, in a document staking its authority on that.

---

### 16. [COSMETIC] The quoted Latin block matches neither named witness exactly, and the document does not say it is normalized.

My word-by-word diff against the Latin Library text: 65 words each way, identical except that the document prints `episc.` where the Latin Library prints `episcopo`, four times. Against Mommsen–Meyer, the document resolves `episc(opi)` → `episcopi` for Nectarius and `Marcianop(olitano)` → `Marcianopolitano`, while keeping the abbreviations elsewhere. It is a lightly normalized composite presented under the sentence "Both carry an identical clause and an identical bishop list." **The substance is exactly right** — I confirmed the clause and all eleven names in both witnesses, and in Boyd — but a document about verbatim discipline should say which text it is transcribing and that it has normalized abbreviations.

---

### 17. [COSMETIC] The two Latin witnesses are presented as independent confirmation without disclosing what their own vendoring notes say about them.

`codex-theodosianus_latinlibrary.txt`'s own header states: *"wording in this file should be treated as Confidence C pending independent line-level comparison against the Mommsen/Meyer edition; **do not rely on this file alone for a claim that turns on a constitution's exact wording**"* — and that The Latin Library "does not identify which critical edition its transcription follows." The Mommsen–Meyer file is OCR of markedly poor quality in this passage (`D£ FIDE CATHOLICA`, `sanctom`, `&cientes`, `conunemoratio`, `pxae-cepti`, `hkragi.(xae)`, and an apparatus reading `macbario` that is plainly `machario`). Neither is disclosed. The conclusion survives — the two agree on every substantive word, and Boyd's independent English note lists the same eleven — but "two independent public-domain witnesses" oversells what was actually consulted, and a later editor should know that the apparatus in particular is not reliably legible.

---

### 18. [COSMETIC] Structural and counting slips.

- §2 line 59: Gregory Thaumaturgus' *Canonical Epistle* is a **div3** (`iii.iii.iii`); "Acknowledged Writings" is the **div2** (`iii.iii`) containing it. The document says the Epistle is "under `div3` 'Acknowledged Writings'."
- §2 line 71: "re-run `python cic/engine/corpus_map.py` (or the merge script)". The generated bucket's own header names `cic/engine/corpus_map_merge.py` as the generator; `corpus_map.py` is the stats printer per the README. The parenthetical hedges it, but the primary instruction names the wrong script.
- §3 line 81: "the **sixth** instance ... the Registry's own living-document log records five before it (the Eupsychius homily; rows 16 and 20; and others)." Reading the log, I count three prior findings covering four rows: the Eupsychius fabrication (round 2); row 82's `In XL Martyres`/npnf205 error (fourth pass); rows 16 and 20 (fifth pass). "Five before it" is not supported by the log the sentence cites, and "and others" is carrying the difference. Either name them or drop the ordinal.
- The record's rendering of the printed heading as *"Letter CCIV. Placed in 375. To the Neocaesareans."* fuses the heading (`Letter CCIV.`), an endnote (`Placed in 375.`) and the italic subtitle. Conventional, but stated as "the letter's printed heading reads."
- `modern_rendering` adds two small glosses not in the text: "who came from **your own city**" (the text has "who came from you") and "she shaped and formed me **with them**" (the text attaches the forming to "the doctrines of piety," not explicitly to Gregory's words). Both are defensible readings; the spoken form is what a participant hears, so they are worth a deliberate decision rather than an unnoticed drift.
- The packages built during this pass are stamped `records_commit: f07eb919...` — a commit that does not contain the records they were built from (the compiler takes `_git_head()`). This is engine behaviour, not the build thread's doing, but it means §5's determinism and gate evidence is not reproducible from the stamp on the package. Worth one line in the ledger entry Finding 7 asks for.

---

## PART THREE — CHECKED AND CLEARED

Stated explicitly so the record shows what was examined and held.

1. **The Amphilochius locus.** `From the Iambics of St. Amphilochius the Bishop to Seleucus, on the Same Subject` is genuinely a `div2` with `id="xvii.xxiii"` at line 44075, between `xvii.xxii` (Gregory Theologus) and `xvii.xxiv` (Timothy of Alexandria). "div2 17.23 / element id `xvii.xxiii`" is correct.
2. **The corpus-map row and its date.** Present at lines 6–15 of `cappadocian-nicene-pastoral-monastic-tradition.yaml`, `locus: div2 17.23`, with the note "Split 2026-08-26 on Mark's ruling." The 2026-08-26 date and the five-day-precedence point are correct.
3. **The "epitome" characterization.** Endnote 603 does say what the document says it says. Naming it as the editor's own epitome, and locating it in Beveridge's *Synodicon* II.179, is accurate — see Finding 2 only for the further point that the epitome character is stronger than "two stretches replaced."
4. **The Macrina quote is verbatim.** Character-for-character against `ix.ccv-p26`, lines 37060–37065, allowing only the dropped section number "6." and the stated double-space normalization. Nothing added, dropped, or reordered within the quoted span.
5. **The element ids and the off-by-one.** `ix.ccv` for printed Letter CCIV, `ix.ccxxiv` for CCXXIII, `ix.ccxi` for CCX — all confirmed against their printed headings. The off-by-one is real and correctly described.
6. **The line numbers.** 37060–37065 is exactly the quoted span.
7. **The Newman claim, which is the best single piece of work in this change set.** The prefatory note (endnote 2734) does state "The passages in brackets are Newman's version," and the bracket does open before "If there be anything you do not understand" (line 37055) and close after "those I set down as fathers,]" (line 37067), with the quoted sentences wholly inside it. I checked both boundaries myself. This is a genuine find that a later editor would have needed and would not have gone looking for.
8. **Epistle 223.** "the teaching about God which I had received as a boy from my blessed mother and my grandmother Macrina, I have ever held with increased conviction" is verbatim at line 39213. "Shorter corroborating form" is fair.
9. **The CTh branch claim, in both directions.** The three files are absent from `cic/texts/` on `origin/main` and present on `donatism-lpc-integration`. Row 79's original statement about non-acquisition is therefore still accurate as written, as the document says.
10. **The Latin substance, the eleven names, the addressee, and the western-bishop point.** All confirmed independently in the Latin Library text, Mommsen–Meyer, and Boyd (p. 46 n. 1, whose page position I verified against the surviving running heads at lines 6374/6464). Boyd's note independently says "It is notable that there is no mention of any western bishops." The count of eleven and of four circle members is right.
11. **`verified-direct` on the law record.** Defensible. The build thread read the primary Latin directly in two editions; the Registry's own rule keys verification to whether a check happened, and the record keeps acquisition and verification carefully apart in `rights_status`, warning explicitly that no default-branch builder can reopen it. I would not sustain an objection here — but note the asymmetry with Finding 4, where a looser standard was applied to a text that is an editor's abridgement.
12. **The `voice-perspective` failure is genuinely pre-existing, and I established it without a rebuild.** `gate_voice_perspective` in `engine/m1/gates.py` iterates `for rid, rec in records.items()` and emits findings strictly per record; nothing about it aggregates across records. `cappadocian.dw.reading-scripture` is not in the change set (`git show --stat 88f9dd4` lists ten files; it is not among them), and its `text` is unchanged. A per-record gate firing on an untouched record cannot have been caused by this change set. My own compile reproduces it: 18 gates, 17 pass, the same single finding on the same string. Leaving it unfixed is legitimate and the reasoning given is right; note only that Finding 7 makes the "named for the ledger instead" disposal presently empty.
13. **`test_restore.py` — the clone-artifact explanation holds, though I could not reproduce the failure.** I got **34 passed, 0 failed**. Reading the test source confirms the explanation exactly: `test_a_checkout_with_only_manifests_can_rebuild_the_pinned_package` asserts `removed > 0` after stripping the `fix` package to `manifest.json`, which fails on a fresh shallow clone where only `manifest.json` is tracked. It is also self-healing: the *second* test in the same file calls `restore_package("fix")` at its end, so any prior run of the suite materializes the files and the first test passes thereafter. The document's characterization is correct and its non-reproducibility now is expected.
14. **Determinism and coverage.** `determinism-check`: `{"pass": true, "differing_paths": []}`. `coverage_summary`: 26 substantive / 2 honest-limit / 0 empty, matching the claim exactly. The quote floor moved 19 → 20 as expected.
15. **The reciprocity link is correct in both directions.** `associated-with` on the quote targeting `cappadocian.dw.how-it-reached-us`, and on the dw targeting the quote. The `reciprocity` gate passes. `associated-with` is its own inverse in `engine/m1/schemas.py`. `speaker_or_author: cappadocian.figure.basil` follows this world's dominant convention (16 of 20 quote records).
16. **The two records already reasoning from Macrina the Elder.** `cappadocian.gravity.household-lineage` (lines 19, 84) and `cappadocian.force.gentry-household` (lines 17, 34) do both carry the grandmother's Thaumaturgan teaching. The document's correction of the discovery pass on this point is right, and its narrower restatement ("no *quote* carried it") is exactly right.
17. **The no-figure-record decision for Macrina the Elder.** `cappadocian.figure.macrina` line 47 does state on the record that Macrina the Elder has no figure record "since no Doc_09 story entry narrates her." Leaving that standing is correct and well argued.
18. **C-E was genuinely left open on fit grounds.** Ledger §47 says so in terms: "`cappadocian.dw.not-later-formulas` (F1-T) and `cappadocian.dw.how-it-reached-us` (C-E) were set aside on redundancy/fit grounds rather than forced." The document's account of the cell's history is accurate — see Finding 11 only for the fit argument itself.
19. **`formation_confidence: Inferential-Thin` was rightly left unchanged on the figure record.** Ninety words of epitomized canon-list does not make Amphilochius Documented. This restraint is correct and I would have objected to any other choice.
20. **The claim that the law is not unused material.** Confirmed at Doc_01 §4a (line 96), Doc_02 §2 (line 57), §7 (line 112) and §9 (line 126) — I checked the section boundaries, so the "§2/§7/§9" citation is right — Registry rows 79 and 80, and Doc_04 §3.3's first and eighth entries, both of which do read the Theodosian settlement as the force that ends the world by fulfilling its central fight. Accurate.
21. **The six-test scores cited for candidate 8.** Doc_04 §3.1's matrix row reads strong / strong / **moderate** / strong / strong / strong. "Repetition, Dependency, Explanatory and Persistence are all already strong" is correct.
22. **Firmilian and the Canonical Epistle are where the document says, and neither is in the bucket file.** Firmilian at `div3 iv.iv.lxxiv`, `shorttitle="Epistle LXXIV"`, title exactly as quoted. Canonical Epistle at `div3 iii.iii.iii` (see Finding 18 for the div-level slip). `grep` of `cappadocian-nicene-pastoral-monastic-tradition.yaml` returns neither. The `npnf214` "Split 2026-08-26 on Mark's ruling" precedent is real.
23. **The corpus-map lever argument.** `cic/corpus-map/README.md` says exactly what the document quotes: "this sits outside `records/` entirely ... touched by nothing in the compile path. Changing anything here moves no package hash and no world's content." The point that a corpus-map row is a bibliographic assignment rather than voice content is correct and worth having made.
24. **The spend-authorization convention.** Ledger §45 and §47 both close with the recompile/re-pin and live M3 admission requiring "Mark's own per-run spend authorization." §6.1 applies it correctly.
25. **No deployment-chunk occurrences.** I grepped all seven `cappadocianctx*/lex*/story*` chunks for the three corrected claims. `ctx002` mentions the 381 settlement but not the law or its bishop list; `story001` names Amphilochius as the correspondent who asked for *On the Holy Spirit*, which the correction does not touch. No chunk edit was owed, and the document is right not to have made one — though it does not say it checked.
26. **The Registry's status framing.** "Not Frozen, and not proposed for Frozen ... The project lead has not seen it" is correct discipline and correctly stated, and the contingency on this review is properly worded.

---

## PART FOUR — ON THE DISPOSITION

§7's "Approved to proceed" is conditioned on this review not calling for substantial revision. It does, so the disposition does not attach and the question of whether the escalation analysis was right is not yet live. Two observations for when it is.

**The escalation reasoning is not wrong so much as under-shown.** §7 tests exactly one candidate against category 4 (the Doc_04 question) and asserts the other three categories in a single clause each. The Amphilochius correction deserves the same explicit test: it changes a sourcing conclusion in a document already at "Approved to proceed." My own reading is that it does **not** trip category 4 — category 4 is about *unresolved* tensions, and this one resolves — but the document should show that work rather than assume it, given that the same paragraph shows it for the case that was easier.

**One thing that is claimed as done and is not.** Beyond Finding 7's missing ledger §50: §5 says the `voice-perspective` false positive "is named for the ledger instead." It is named here and nowhere else. And §6's four deferred items — the re-pin, the two corpus-map edits, the gate false positive, the process gap — have no durable home outside this single document, which is not itself Frozen and is not in the ledger's index. If this document is the only record of four open items, that is a fragile place to leave them.

**What I would not change.** The decision not to revise Doc_04; the decision not to create a figure record for Macrina the Elder; the decision not to quietly fix an unrelated record to clean up a gate report; the decision to escalate the Firmilian split rather than make it; and the decision to name the prior false claim rather than silently rewrite it. All five are right, and the last is the discipline the project says it wants.

---

## CLOSING VERDICT

**Substantial revision is called for.** Findings 1, 3, 4, 6, 7 and 8 are corrections of fact or of the change set's own internal consistency and should be made before this is dispositioned; Findings 5, 9, 10, 11, 12 and 13 require the document to redo or withdraw an argument. Findings 2 and 14 are characterization fixes of a few clauses each. The cosmetic findings can be applied directly.

The pattern worth naming, since this document names patterns: every one of the six most serious findings above is a claim the document asserted about a file, a rule, or a command's output without running the check. The word count came from the corpus map. The Confidence-A justification quoted half of the rule it cites. The `verified-direct` grade skipped the precedent in this world's own ledger. The staleness line was not re-run. The ledger §50 pointer was written before the section. And "three review rounds could not have caught it" was asserted without opening the Registry's own rows 60 and 78. This is the same defect class the document was written to close, committed by the document that closes it — which is not an indictment of the work so much as a demonstration that the discipline has to be applied to the correction as rigorously as to the thing corrected. The underlying research is sound, the honesty is real, and the corrections it identified were genuinely needed. It is the verification of the verification that did not happen.
