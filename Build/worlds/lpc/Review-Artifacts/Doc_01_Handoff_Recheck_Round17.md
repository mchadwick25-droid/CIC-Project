Simulated review — informational only, not an Article 31 substitute.

# Doc_01 recheck: the Phase L1 handoff changes

- **Document:** `Build/worlds/lpc/Doc_01_World_Identification_Boundaries_Orientation.md`, changes read as `git diff 5cc91f71 31fc57ae` (the changes are in `7191a6d5`)
- **Round:** 17
- **Reviewer:** Opus 5.5, for the whole run; no fallback to another model occurred
- **Reviewer model:** claude-opus-5-5
- **Reviewer agent:** independent recheck subagent, fresh context (drafted none of the changes)
- **Drafter:** the `lpc` build thread
- **Drafter model:** claude-opus-5-5
- **Drafter agent:** the `lpc` build thread's Phase L1 handoff pass (drafter model per the commit trailer of `7191a6d5`)
- **Date:** 2026-10-24
- **Scope:** every changed line in Doc_01 (18 lines): the removed quotation marks, the new italics, and the reworded sentence on the sermons preached at Carthage (line 34). Doc_01 is not otherwise re-reviewed.
- **Ordered by:** the project lead's Cap ruling of 2026-10-24 (`Build/Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md`, "Cap ruling: lpc Step 0, Doc_01 and Doc_02, one recheck of the Phase L1 handoff changes", the file's last entry)
- **Truncation check, method 1:** line and byte count with an end-of-file read. 208 lines, 108,912 bytes; ends "open to correction by direct re-examination of the sources."
- **Truncation check, method 2:** hash comparison. `sha256sum` of the working file and of `git show 31fc57ae:<path>` both begin `cb803e042fbd`.
- **Method limits:** no web search and no model call. The diff was split into per-line word changes by script, and each new line was read whole. Sources read: `npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml`, Doc_02 line 19, Step 0 line 87, the Step 0 Conclusion `.docx`, `Archive/Syriac-Build-2026-07/CiC_Coach3_Step0_Critique_2026-07-06.md`, Donatism's Step 0 and its `Step0_Round2_Review.md`, IJC's Step 0, IJC's `Doc_04_Gravity_Discovery.md`, hal Doc_01, and the lpc and ijc corpus maps. Nothing edited except this file.

---

## Line 34: the sermons preached at Carthage

The old text quoted Step 0 §3 B1 as "~97 sermons preached to his own congregations at Hippo and Carthage". The new text reads: "Step 0 §3 B1 counts 97 sermons in the vendored NPNF selection, and their NPNF headings place three of them at Carthage or at the Table of St. Cyprian, as Doc_02 records".

- **Against Step 0:** Step 0 line 87 now reads "97 sermons in the vendored NPNF selection". The new wording matches it.
- **Against Doc_02 line 19 (approved):** Doc_02 says the NPNF headings "place three of them at Carthage or at the Table of St. Cyprian: `npnf106` Sermon XL and ids `vii.lxvi-p4` and `vii.lxxxiii-p4`". The new Doc_01 wording is the same claim.
- **Against the loci:** all three are real headings. Sermon XL is `div2 n="XL"` (file line 15408), titled "...Delivered at Carthage in the Restituta." `vii.lxvi-p4` (line 17969) reads "Delivered at the Table of St. Cyprian, in the presence of Count Boniface." `vii.lxxxiii-p4` (line 19865) reads "Delivered at the Table of the Martyr St. Cyprian, the 9th". The Table of St. Cyprian was at Carthage.
- **Result:** correct. The old wording claimed more than the NPNF headings show. The new wording claims only what they show.

---

## Removed quotation marks and new italics

| Line | Result | Evidence |
|---|---|---|
| 18 | Meaning kept | "Step 0 §3 B2 calls it plausibly the *richest*..." still names Step 0 as the speaker. |
| 20, 180 | Pointer kept | The Decision Log entry title is now italic, still tied to `lpc_Decision_Log.md`. |
| 104 | Meaning kept | Donatism's Step 0 does say "the Donatists revived Cyprian's own third-century position against Pope Stephen". The rejected framing after it is still marked as "the obvious way to resolve it" and then refuted. |
| 106 | Meaning kept | The Coach3 boundary statement matches the archived file word for word. It is introduced by "states the World #4/#8 boundary as follows", so it is still the Coach3 critique's claim. |
| 114 | Meaning kept | Matches the Conclusion's World #8 entry (docx line 20); introduced by "The Step 0 Conclusion's World #8 entry covers". |
| 116 | Meaning kept | Donatism's Round 2 review reads "In the source it is a parenthesis attached specifically to Cyprian's Decian-persecution material". The paraphrase is faithful. |
| 154 | Meaning kept | Step 0 item 5 and Step 0 §3 B1 are still named. |
| 156 | Meaning kept | The three IJC strand definitions stay attributed to "IJC's own Doc_01 §4 gives". |
| 158 | Meaning kept | IJC's Step 0 item 3 reads "The authority-structure/state-power boundary named in §3 above must be stated explicitly in Doc_01, since World #8 is not yet built and cannot itself hold the line from its side" (`ijc/Step0...:118`). "Set out here in full" is still true of the indirect form. The Conclusion clause matches docx line 20. |
| 160 | Meaning kept | The Conclusion reads "genuine distinctiveness from the other selected worlds (formation-logic, authority structure, relationship to power)". Dropping "from the other selected worlds" does not change the sense. |
| 164 | Attribution blurred | See N11. |
| 165 | Meaning kept | The hal Doc_01 wording ("charismatic-scholarly and voluntary-aristocratic-patronage-based...", "drove him from Rome within months with no institutional recourse") matches hal Doc_01 line 172 and stays attributed to "(hal Doc_01 §8.1)". |
| 167 | Meaning kept, one referent lost | See N12. |
| 169, 196, 204 | Meaning kept | Each matches the Conclusion docx (lines 20 and 67) and stays attributed to it. |

No sentence now presents a ruling, a source's wording or another document's claim as Doc_01's own, except the blur in N11. No pointer is lost. Readability is unchanged.

---

## New findings

### N11 (P2). Line 164 now reads as if the corpus map called Letter 185 "the strongest documented datum"

- **Where:** line 164: "this world's own corpus-map records that Letter 185, carrying Augustine's fullest defense of coercion, is direct evidence for the ijc world's core question, the church's use of imperial law, and is the strongest documented datum on the side this reframing does not favor, restored here rather than left out of an honest report".
- **Evidence:** before, the corpus-map words sat in marks and "the strongest documented datum..." followed as Doc_01's own comment. Now "and is the strongest documented datum" joins the clause governed by "records that". The corpus map says nothing about "this reframing". Also, the note is not in this world's corpus map. It is the ijc map's note (`imperial-juridical-christianity.yaml:192`, also in the shared staging file `_staging/npnf104_augustine-anti-manichaean-anti-donatist.yaml:250`). The lpc map's own note on Letter 185 (`latin-pastoral-congregational-christianity.yaml:1668`) calls it "the classic defense of state correction of schism". The wrong map name predates this change. The new sentence also folds IJC Doc_04's "single most load-bearing explanatory claim" into an appositive; that one is still read as IJC's, which is right (IJC Doc_04 line 44).
- **Why P2:** the facts are true and the sentence still reports, rather than adjudicates. A reader could still credit the corpus map with a judgment that is Doc_01's.
- **Fix:** "the ijc corpus map's note calls Letter 185, carrying Augustine's fullest defense of coercion, direct evidence for the ijc world's core question, the church's use of imperial law. It is the strongest documented datum on the side this reframing does not favor, restored here rather than left out of an honest report."

### N12 (P2). Line 167's "this volume" has no referent

- **Where:** line 167: "(~52,892 words, the largest single thing in this volume after the Confessions)".
- **Evidence:** the corpus-map note's "this volume" means `npnf101`. Without the marks, Doc_01 names no volume. Step 0 line 109 has the same phrase (Step 0 Round 8, N2).
- **Fix:** "the largest single item in the `npnf101` volume after the Confessions, per the corpus map".

---

## Summary

All 18 changed lines were read against their sources. The sermon sentence on line 34 now matches Doc_02's approved wording and Step 0, and its three NPNF loci are real headings that place the sermons at Carthage. The de-quoting keeps every attribution but one: line 164 now lets a judgment of Doc_01's read as the corpus map's, and it names the wrong corpus map (N11, P2). One referent is lost on line 167 (N12, P2).

Counts: 0 P0, 0 P1, 2 new P2 (N11, N12). Round 16's N8 to N10 were outside this recheck and are not rechecked.

VERDICT: Approved to proceed
