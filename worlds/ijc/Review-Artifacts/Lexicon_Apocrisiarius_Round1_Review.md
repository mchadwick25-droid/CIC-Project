# Apocrisiarius Lexicon Entry (`ijclex013`) + Index Amendment — Round 1 Independent Adversarial Review

**Reviewed:** `Lexicon-Chunks/ijclex013_apocrisiarius.md` (new, DRAFT) and `Lexicon_Deployment_Index.md` (amended 2026-09-10 for the thirteenth entry), as one output set. Commit `0ddcf0d9`.
**Reviewer:** independent isolated agent (Opus), no drafting or prior review involvement on this entry; instructed to verify the load-bearing attestation claim from the vendored corpus directly rather than accept the chunk's own account of it
**Date:** 2026-09-10
**Overall verdict: SUBSTANTIAL REVISION REQUIRED**

Marking per Constitution Article 31: Simulated review — informational only, not an Article 31 substitute.

---

## Independent verification performed (from primary data, not trusted from the documents)

**Corpus attestation sweep.** `grep -ric "apocrisiar"` across all 98 files in `cic/texts/`: four files, 25 total occurrences — `npnf212` (16), `gregory-great_epistolae-selectae_turchi1907` (5), `npnf213` (3), `npnf214` (1). Zero occurrences anywhere else. Also checked, and not in the chunk: `apokris` (zero), the Greek stem `ποκρισ` in any accentuation (zero occurrences corpus-wide — the vendored corpus contains no Greek instance of ἀποκρισιάριος, and no instance of the underlying noun ἀπόκρισις either), and `responsal*` (32 occurrences: `npnf212` 12, `npnf213` 7, `gregory-great` 15 — every one at or after `npnf212` line 22818, i.e. all inside the Gregory division).

**`npnf212` division boundaries, read directly.** `<div1>` structure: `id="ii"` "The Letters and Sermons of Leo the Great" spans lines 311–22082; `id="iii"` "The Book of Pastoral Rule, and Selected Epistles, of Gregory the Great" begins at line 22083. Exactly one of the 16 occurrences (line 817) falls inside the Leo division; the remaining fifteen fall inside the Gregory division.

**The Leo-era occurrence, read in place.** Line 817 sits inside `<div2 title="Introduction.">` → `<div3 type="Section" title="Life." n="I">` (opened at lines 386/388), in a paragraph beginning "To return to Leo, we have letters from Marcian, Anatolius, and Julian…" and carrying an editorial endnote citing "Gore's Life, pp. 113 and 114." Text: *"…eagerly seizing at pretexts of complaint against him, and appointing Julian his `apocrisiarius` or resident representative and correspondent."* This is Feltoe's own nineteenth-century prefatory Life, not Leo's text. **The chunk's central claim on this point is correct**, and the phrase it quotes is verbatim accurate.

**`npnf214`, read in place.** Its single occurrence (line 1888) is in Percival's own introductory essay on the origin of the Canon Law, describing John of Antioch surnamed Scholasticus, "representative or apocrisiarius of the Church of Antioch at Constantinople," patriarch 564–578. Modern editorial apparatus, mid-sixth-century subject. Correct as the chunk states.

**`npnf213` / `gregory-great_epistolae-selectae`, read in place.** All occurrences are Gregory-era: endnote glosses identifying Anatolius (npnf213 line 1293) and, in `npnf212`'s Gregory division, Sabinianus (line 23387, and line 46374 "the deacon Sabinianus, Gregory's apocrisiarius") and Gregory himself (line 22818, c. 578–585); Turchi 1907's Latin prolegomena and index. Correct as the chunk states.

**The in-window function, verified independently.** Julian of Cos is amply attested inside Leo's own letters (57 hits on "Julian" inside the Leo division; four letters titled "To Julian, Bishop of Cos" at lines 6089, 6170, 6928, 8318, plus "To Bishop Julian" at 8135). The Chalcedon legates' Canon 28 objection is carried in `npnf214` at "Extracts from the Acts. Session XVI." (line 22571): Paschasinus, holding the place of Rome, says "…it is said that certain decrees were made, which we esteem to have been done contrary to the canons… We request that your magnificence order these things to be read." **The chunk's function-without-the-name claim is well founded.**

**Index arithmetic, recomputed from the thirteen chunk files' own front-matter, not read off the index.** Tier counts 5/5/3 ✔. AS 7 ✔, SC 6 ✔, DR 7 ✔, TC 11 ✔, RT 13 ✔, PV 6 ✔, CT 4 ✔. Every tag cell in the new master-table row matches the chunk. Related-Terms cell matches the chunk exactly. Reciprocity: transcribed all thirteen Related-Terms fields and summed out-degrees — the original twelve sum to exactly **42 directed edges / 21 reciprocal pairs, every edge reciprocal, zero gaps** (independently confirming the pre-amendment claim the amendment deleted); `apocrisiarius` adds 4 out-edges and 0 in-edges, and **none of `communio`, `primatus`, `Tomus`, `concilium` lists it back** — §5's one-directional claim is accurate. `git show --stat 0ddcf0d9` confirms only two files changed; none of the twelve original chunks was touched, and no original master-table row was altered.

---

## Findings

### 1. [HIGH] The entry's stated justification rests on a premise a later, recorded project-lead ruling already superseded — and the chunk never checks it.

The chunk's Attestation Note justifies its Template departure "because this term is participant-facing and its evidentiary basis is thinner than any other entry"; its Retrieve-When is "participant asks what this Representative's own title means"; the index amendment note and Open_Gaps item 15 both frame the work as preventing an unglossed label reaching the UI.

Checked against the canonical registry. `records/worlds.yaml` line 165: `representative: {name: Marius, role_label: "Deacon of the Letters"}`. `Ministry/Technology/CiC_FrontEnd_Decision_Log.md` (2026-08-28, "Mark's identity ruling applied: the registry wins") records: *"three titles corrected to registry values (Household Leader, Abba (Elder), Deacon of the Letters — the last superseding Mark's 2026-07-22 'Apocrisiarius —' long form by this ruling)."* Every participant-facing surface I could find now carries "Deacon of the Letters" and not "Apocrisiarius": `cic-website/data/world-census.json` (`"representativeTitle": "Deacon of the Letters"`), `packages/ijc/*/compiled/frame.json`, `records/WORLDS_REGISTRY_LOG.md`'s own header line. The only surviving "Apocrisiarius" strings outside build documents are an XML source comment inside three copies of the world icon SVG and the internal `records/ijc/voice_craft/ijc.voice.craft.md`.

So the word does **not** currently reach the UI as an unglossed label. Item 15's premise is stale by roughly two weeks at the time of drafting, and the ruling that made it stale is on the verifiable record. This does not make the entry worthless — "apocrisiarius" remains a plausible runtime term, and the chunk correctly lists "Deacon of the Letters" among its Aliases so it retrieves on the actual title — but it does invalidate the specific ground the chunk gives for departing from the Template, and it means the entry is closing a gap that was already closed by other means. `cic-build-cycle`'s Review requirement ("internal consistency with decisions already made earlier in this world's build") and its Naming-and-term-propagation section both required this check before drafting.

### 2. [HIGH] The entry contradicts Open_Gaps item 15's own factual characterization of the term, and does not name the contradiction.

Item 15 (line 107) states: *"'Apocrisiarius' is a genuine, well-attested period term (a deacon-legate carrying correspondence and petitions between sees — Gregory the Great's own pre-papal office in Constantinople is the best-known instance)."* The chunk's finding is that the word is unattested in this world's window and that the Gregory instance is a century and a half outside it. Both cannot stand as written.

The chunk is, on my own verification, right and item 15 is wrong. But `cic-build-cycle`'s Cross-document fact consistency section names this exact failure mode as one of two real defects in this project's history: *"World #7's Doc_02 and Doc_03 independently asserted contradictory claims about the same vocabulary term (one treating it as attested, the other excluding it as unattested) without either document cross-checking the other."* This is a verbatim recurrence, on a vocabulary term, in a build whose Doc_06 disposition already logs a repeated self-verification defect as "a caution for Doc_07 onward." The chunk had to name the contradiction and say which claim now governs. It does not mention item 15's characterization at all, and item 15 itself was not amended — `git show --stat` confirms `Open_Gaps_Tracking.md` was not touched, so it still reads "Not yet done" and still asserts "well-attested period term."

### 3. [HIGH] The Tier 3 assignment is nowhere reasoned, and the index now points a reader to a section that does not contain the reasoning.

Doc_06 §2 is titled "Final Tier Classification — **reasoned, not restated**" and assigns every one of the twelve tiers against Doc_04's own gravity classifications. Neither the chunk nor the index gives any tier reasoning for the thirteenth. The index's §2 closing sentence — unchanged by the amendment — still reads: *"Reasoning for this distribution against Doc_03's own ten-of-twelve provisional Tier 1 flagging is recorded in full in `Doc_06_Full_Lexicon_Development.md` §2 — not repeated here."* That sentence was true of a twelve-row distribution. It is now attached to a thirteen-row distribution whose thirteenth row Doc_06 §2 does not mention. I confirmed by direct grep that "apocrisiar" appears **zero** times in Doc_01, Doc_02, Doc_03, Doc_05, Doc_06, Doc_07, `Source_Registry.md`, `ijc_World_Capsule_Core.md`, and `ijc_Representative_Permanent_Prompt_Marius.txt`.

**On the substance, Tier 3 is right and I would keep it** — but for a reason the entry does not state. Doc_06 §2's discriminating test is *organizing weight against Doc_04's classifications*, not recurrence: Tier 2 in this build is reserved for terms tied to a Supporting-classification gravity (`homoousios`/Candidate 5, `concilium`, `haeresis`, `Tomus`, `Nea Rhōmē`). `apocrisiarius` has no Doc_04 gravity link at all; it is at most an instrument of `communio` and `primatus`. Certainty of arising at runtime cannot argue for Tier 2, because all thirteen terms carry RT — that tag, not the tier, is where runtime likelihood is recorded. So the answer to "should this be Tier 2 given it is the Representative's title and certain to arise?" is no. The defect is the missing argument, not the value.

### 4. [MEDIUM] The bolded caution inside World Meaning is a builder speaking through the mask, not an in-voice caution.

`cic-lexicon-index` requires World Meaning to read from inside the world's own ecology with no analytical-distance markers. None of the Template's literally-listed markers survives ("scholars believe," "this reflects," "we can see," "evidence suggests," "the sources indicate," "historically," "reconstruction") — I checked each. But the chunk introduces a different one of the same species, and arguably worse:

> **Said plainly, because a participant meeting this title deserves it:** this word is not in our own mouths. It belongs to the century after this one.

"a participant" names the runtime apparatus from inside the world's first person — no fifth-century deacon has participants. And "It belongs to the century after this one" is knowledge from outside the world's own horizon asserted in the world's own voice: a speaker inside 451 cannot know what the next century will call this. The same break appears in the Quick Meaning ("It is the name a later age gave the work").

Compare `ijclex009_tomus.md`, which the review prompt rightly points at as the house model: *"**This entry is our own only example of this genre in the record we can point to** — we do not have a second Tome, from us or from another see, to show this is a repeated form rather than one document doing double duty…"* That is bolded, evidentiary, and stays inside what a person in-world could actually say — "the record we can point to," "we do not have." It carries a real limitation without stepping outside the horizon. The apocrisiarius caution can be rewritten to the same standard (e.g. naming that the men doing this work are known by their errands and their sees rather than by any settled name) without losing anything the participant needs.

Doc_06 Round 1 finding 9 already noted that Tier 3 World Meaning sections "lean analytical," tolerated under the brevity allowance. This one goes past leaning.

### 5. [MEDIUM] The Quick Meaning is three sentences where the Template specifies one, and this departure is not disclosed.

Template, Quick Meaning: "[ONE SENTENCE — the runtime-facing summary of this term. Usable as a popup definition…]". All twelve existing chunks comply — `Tomus`, `basilica`, `martyrium` each have exactly one. The new chunk has three, two of them meta-commentary on the term's own attestation. The chunk's Final Assembly Instruction discloses only the Attestation Note as a departure; this second departure goes unmentioned, which matters because the Final Assembly Instruction is the place a reviewer is entitled to find every departure listed.

### 6. [MEDIUM] The Attestation Note should have been Reported-Experience Status — the Template already provides a section for exactly this, and this build's own review history has already required its use in this circumstance.

Template: *"Reported-Experience Status — {Include only where applicable — where this term's World Meaning is historically uncertain but formationally central. Omit if not applicable.}"* That is a precise description of this entry: a title whose application to this window is unattested, carried because it is formationally central to the Representative. Final Assembly Instruction step 5 requires the verbatim marker where it applies.

This is not a theoretical alternative. `Doc06_Round1_Review.md` finding 5 was "[LOW-MEDIUM] Reported-Experience Status marker absent from `homoios` and `Imperator` chunks despite both containing historically-uncertain-but-formationally-central content matching the marker's own scope. **FIXED** — added to both." I read both sections: each opens with the verbatim marker and then gives a short, specific note on why the status applies. The apocrisiarius chunk's Attestation Note is doing that job under a new name, and its Final Assembly Instruction never mentions the existing section, so a reader cannot tell whether it was considered and rejected or simply missed.

I do not think the content should be cut — it is the most valuable thing in the entry. But inventing a section when the Template supplies one is a departure that needed to be argued against the actual alternative, and was not.

### 7. [MEDIUM] Build-apparatus identifiers appear inside a runtime-retrievable chunk, in a register no other chunk uses.

The Attestation Note carries `npnf212`, `npnf213`, `npnf214`, `gregory-great_epistolae-selectae`, `ijc.source.leo-letters`, `ijc.figure.leo`, `ijc.dw.received-not-seen`. No other chunk in this lexicon does this: `Tomus`'s Key Sources reads "Leo I's Tome to Flavian (Epistula 28), and its reception (and, regarding Canon 28 specifically, non-reception) at Chalcedon" — human-readable, no filenames, no record IDs. The Template's Final Assembly Instruction requires that no builder notes remain; vendored-corpus filenames and internal record IDs are builder notes by any reasonable reading. This content belongs in the index, in Doc_06's open items, or in a build note — not in a file whose stated purpose is runtime retrieval to a participant.

### 8. [MEDIUM] The bolded attestation claim is stated at a wider scope than the check performed supports.

The chunk asserts, in bold: **"The word is not attested in this world's own in-window sources."** What was actually checked — and what I re-checked — is the vendored corpus. Two limits on that:

- The corpus contains essentially no continuous Greek. `npnf214` carries 857 `lang="EL"` spans and `npnf212` carries 93, but these are scattered quotations embedded in English translations; there is no Greek text of the councils. The corpus-wide absence of ἀποκρισιάριος is therefore very weak evidence about the Greek record, and the office's own name is Greek.
- `npnf214` presents Chalcedon as "Extracts from the Acts" (that heading appears 44 times across the volume's councils), not the complete Acts. The in-window conciliar record is present in excerpt only.

The absence is real as far as the corpus goes, and it agrees with the mainstream dating the chunk implies. But this build has a documented history — logged in Doc_06's own Round 2 disposition — of confidence claims about its own completeness being wrong twice in the same section. The defensible sentence is "not attested anywhere in this build's vendored corpus, which for this window carries the councils in English excerpt and almost no continuous Greek"; the sentence written claims the source ecology, not the corpus. Given this is the single load-bearing claim of the entry, it should be scoped to what was checked.

### 9. [MEDIUM] The Quick Meaning imports the later institution's role-rank while flagging only the later word — and the in-window exemplar the chunk itself offers does not fit it.

The Quick Meaning defines the term as "**A deacon** kept at another see." The chunk's own attested in-window exemplars are not deacons: Julian of Cos was a **bishop** (Leo's letters to him are titled "To Julian, Bishop of Cos" — `npnf212` lines 6089, 6170, 6928, 8318), and the Chalcedon legates who made the recorded objection were Paschasinus, bishop of Lilybaeum, and Lucentius, bishop (`npnf214` lines 19159–19239, 20021).

The "deacon" element traces to the sixth-century Roman practice, and the corpus says so in as many words at `npnf212` line 22826, in the same editorial Life the chunk correctly identifies as retrospective: *"The office of apocrisiarius was usually filled by a deacon."* The chunk sets out to flag one anachronism (the word) and silently carries a second (the rank) into its single most participant-facing sentence, then offers a bishop as the in-window warrant for it without noting the mismatch.

I recognise that "deacon" is not freely revisable here — `ijc_Representative_Permanent_Prompt_Marius.txt` line 1 establishes Marius as "a deacon, entrusted with carrying letters and hearing petitions between the great sees," and that is settled identity. The entry is not obliged to change it. It is obliged to disclose that the rank, like the word, belongs to the later shape of the office, and that its own in-window example held a different one.

### 10. [MEDIUM] Author-Gravity-Risk cell is index-only, is not derivable from the chunk, and repurposes the column's defined meaning — and it contradicts the adjacent cell in its own row.

`cic-lexicon-index` defines this column as "yes/no, **pulled from whether the Key Sources note flags single-source dominance**." The chunk is Tier 3 and correctly has no Key Sources section, so there is nothing to pull from; the chunk never uses the phrase "Author Gravity" anywhere. The index nonetheless asserts "**Yes, in the strongest form** — no in-window source at all," converting "one source dominates" into "no source exists." Those are different findings and the column cannot carry both. Both other Tier 3 rows say "No."

Within the same row, the Source Registry Cross-Reference cell says "**None**" while the Author-Gravity cell names "Rows 12–13." Those cross-references are also imprecise: Row 12 is Leo's *Tome to Flavian*, which has nothing to do with legates, and the row that actually carries the legates' recorded objection — Row 11, "Acts and Canons of the Council of Chalcedon (451), esp. Canon 28," which is where I verified the Session XVI protest — is not cited. `Doc06_Round1_Review.md` finding 8 caught this same class of defect ("Index Source-Registry cross-references imprecise") and it was fixed then.

### 11. [MEDIUM] The amendment deleted a true, independently verified, checkable claim and replaced it with a citation to a past review.

Pre-amendment §5 read: *"The total across all twelve chunks' current Related-Terms fields is **42 directed edges (21 reciprocal pairs)** — every one confirmed to have a matching reverse edge by explicit enumeration of all twelve lists."* I recomputed this from the chunk files and it is exactly right: out-degrees 7+5+2+6+2+4+4+3+4+2+2+1 = 42, all 21 pairs reciprocal, zero gaps. `Doc06_Round3_Review.md` independently recomputed the same figure.

The amendment replaced that with "verified by direct enumeration at Doc_06 Round 3 and unchanged since." "Unchanged since" is true (git confirms it). But a first-hand, reproducible number has been downgraded to a historical citation, and the new totals the amendment creates — 46 directed edges, 21 reciprocal pairs plus 4 one-directional — are stated nowhere. This is a regression in exactly the section Doc_06's own disposition singles out: *"this document's own confidence claims about its own completeness have now been wrong twice in the same section, which is itself logged as a caution."* Section 5 is the last place in this index where a verified count should have been dropped. Nothing false was introduced; something true and checkable was removed.

**On the substance of §5's one-directional finding: it is accurate, and the decision to flag rather than repair unilaterally is right.** I confirmed all four named chunks and none lists `apocrisiarius` back. Of the two closures offered, closure 1 is the better one — the skill's own instruction is that relationships "should generally" be reciprocal — but editing four disposed chunks is properly a decision for whoever disposes of this entry, and declining to make it here is correct.

### 12. [MEDIUM] `ijc.dw.received-not-seen` is cited for content it does not contain.

The Attestation Note cites three records for "Rome's legates at Chalcedon in 451, whose recorded objection to Canon 28 is carried in this world's own registry (`ijc.source.leo-letters`, `ijc.figure.leo`, `ijc.dw.received-not-seen`)." I read all three.

`ijc.source.leo-letters` supports it (its work field names "the rejection of Chalcedon's Canon 28 (452)"; its notes name "Leo's legates' objection" directly). `ijc.figure.leo` supports it (line 23: "Canon XXVIII (his legates' objection)"). `ijc.dw.received-not-seen` does **not**: it is about received witness and chain of custody, and its only legate content is Paschasinus reciting the rule of faith at Session IV — a different session, a different act, nothing about Canon 28. A reader auditing the citation will not find the claim there.

### 13. [MEDIUM] The amended document now carries three mutually inconsistent status signals.

Line 3 (unchanged): "**Status:** Cleared review (Round 3, CLEARED) — Approved to proceed…". Line 5 (new): "…the entry and this index's amendments are DRAFT and carry no disposition…". The Disposition section (unchanged): "Pending independent adversarial review, run and disposed of together with `Doc_06`…". A reader or a downstream check reading the top-line Status of this file gets "Approved to proceed" for a document that now contains undisposed content. `cic-build-cycle`'s "A status line inside the document is not evidence of anything on its own" cuts both ways — the top-line status here now actively misdescribes the file. The amendment note is honest; the header it sits under was not brought into line with it.

### 14. [MEDIUM] The new master-table row drops an alias the chunk carries — and it is the load-bearing one.

Chunk Aliases (five): "apocrisiary, responsalis, Deacon of the Letters, resident representative, **legate (in the correspondence-carrying sense only)**". Index cell (four): the last is dropped.

This is the exact defect `Doc06_Round3_Review.md` found and fixed at Round 3 ("Master table's primatus row omitted 'apostolic primacy' from its own chunk's Aliases field. **FIXED.**"), so it is not an accepted house shorthand — it was ruled a defect once already. It matters more here than it did there: "legate" is the word the chunk's own Distortion Risk identifies as what the in-window record actually shows ("what the record shows is legates and letter-carriers"), so dropping it removes the one alias that connects the index row to the attested in-window vocabulary.

*Noted as pre-existing, not introduced by this amendment:* several original rows still truncate their chunks' Aliases (`presbeia` drops "New Rome's rank"; `homoios`, `communio`, `Imperator`, `homoousios`, `concilium`, `Tomus`, `Nea Rhōmē`, `basilica`, `martyrium` all drop one or more). Round 3 fixed only `primatus`. Worth a separate sweep, but it is not this entry's defect and does not bear on this verdict.

### 15. [MEDIUM] The index's RT rationale is now false as applied to the thirteenth term.

§3: "**RT (Likely Runtime Term):** all thirteen — every term was generated specifically because it is expected to arise in encounter (**Doc_03's own candidate-generation method**)." `apocrisiarius` was not generated by Doc_03's method; it appears nowhere in Doc_03 (verified: zero occurrences). The count "all thirteen" is correct — every chunk does carry RT — but the reason given was true of twelve terms and is now attached to thirteen. A one-clause carve-out fixes it.

### 16. [LOW] The §3 TC bullet is garbled by an incomplete edit, damaging the record of a deliberate departure.

As it stands: *"…the tag tracks technicality, not tier, and the previous coincidence of the two is not a rule. Open to reviewer challenge, **whose own chunks and this index's own master table both correctly withhold the tag, consistent with their narrower, non-technical function (Doc_06 §2).**"* The bolded clause is a fragment of the pre-amendment sentence whose antecedent ("the two Tier 3 entries") was removed; "whose" now dangles off "reviewer challenge." The count itself is correct (eleven of thirteen; I verified every Tags field).

**Taking up the invitation, since the bullet asks for it:** I would **keep TC**, but re-ground the reason. The Template defines TC as "carries specific theological or philosophical precision," which an administrative-juridical office title does not obviously do — so the index's new principle ("the tag tracks technicality, not tier") is a fresh reading of the tag rather than an application of it. The tag does not need that fresh reading: `concilium` and `Tomus` are institutional and genre terms respectively and both carry TC with Doc_06's endorsement. That house precedent is the sound basis. The rewritten bullet should cite it and drop the "technicality, not tier" formulation, which introduces a new tag principle in passing.

### 17. [LOW] The Attestation Note's audit trail cannot be reproduced from what it says.

It claims "Every occurrence in the vendored corpus was checked directly" and then accounts for `npnf212` with a single bullet about "the one Leo-era occurrence." `npnf212` contains sixteen; the other fifteen are never mentioned. The volume is also labelled "(Leo the Great)" when its own DC.Title is "NPNF-212. Leo the Great, Gregory the Great" and its second division is Gregory's. An auditor greping the file finds 16 hits against a note that describes one, with no stated reason for the gap. The claim is true — I verified it — but the note as written does not let anyone else confirm that without redoing the division-boundary work from scratch.

### 18. [LOW] `responsalis` sits in Aliases without the caveat the Attestation Note gives its headword.

`responsalis` is the Latin counterpart, and unlike `apocrisiarius` it appears in Gregory's *own letter text* rather than only in editorial apparatus (e.g. `npnf212` line 40425, "Prosper your delegate (`responsalis`)"; line 41261, "Sabinianus my `responsalis`"). It is nonetheless just as absent from the window — all 32 corpus occurrences fall at or after `npnf212` line 22818, inside the Gregory division. A reader meeting it in Aliases with no comment could reasonably take it as an in-world synonym. One clause in the Attestation Note fixes this.

---

## What checked out clean

- **The load-bearing attestation claim survives adversarial checking.** I attacked it as instructed and could not break it. The Leo-era `npnf212` occurrence is in the editor's Introduction/Life, exactly as claimed, and the quoted gloss is verbatim. `npnf213`, `npnf214` and Turchi are correctly dated and correctly characterised. No Greek form of the word exists anywhere in the corpus; no `responsalis` occurrence falls in-window. **The chunk neither overstates nor understates the absence within the corpus** — my only reservation is the scope of the sentence (finding 8), not its truth.
- **The function-without-the-name claim is well founded and independently verifiable.** Julian of Cos as Leo's resident man at court, and the legates' on-the-spot Canon 28 objection entered in the acts, both check out in the vendored text. The World Meaning's "they said so on the spot and it was written down that they had" is an accurate rendering of Session XVI.
- **The inverted Distortion Risk argument is genuinely good work** — that this term's risk runs opposite to the rest of the lexicon (a later word overwriting an earlier practice, rather than a modern sense overwriting a world sense) is correct, well-put, and is the strongest thing in the entry.
- **Every tag cell, the Tier cell, and the Related-Terms cell of the new master-table row match the chunk exactly.** Every count in §2 and §3 recomputes correctly at thirteen. The CT check sheet remains accurate ("all other terms | No" correctly covers the new entry), and withholding CT is right: anachronism is not the "live scholarly contest" Article 26 §B and Doc_06 §3 require.
- **§5's one-directional finding is accurate and honestly reported**, and declining to edit four disposed chunks unilaterally is the correct call.
- **The original twelve are untouched and still fully reciprocal.** `git show --stat` confirms two files changed; my from-scratch recount of the twelve reproduces 42 edges / 21 pairs with no gaps. No original row or disposition was silently altered. Apart from finding 13's header ambiguity and findings 3 and 15's now-stale rationales, the amendment broke nothing that was true.
- **No fabricated quotations.** Every quotation I could trace — the NPNF editor's gloss, item 15's quotation of the Permanent Prompt's line 1 — is verbatim accurate.
- **No content is attributed to the project lead without a record.** The 2026-07-22 title choice is on the record at Open_Gaps item 15 and in `records/WORLDS_REGISTRY_LOG.md`. (That it was later superseded is finding 1, not an attribution defect.)
- **No uncredited reuse of another world's material.** §6's Cross-Build Sheet is unchanged and remains accurate; the Gregory-era material is cited only to exclude it.
- **No disposition pre-declared and no self-scoring.** The chunk's Final Assembly Instruction flags its own departure "for review rather than assumed acceptable," and the index amendment note states DRAFT with no disposition. That discipline was kept, and it is why several of the findings above are recoverable rather than fatal.

---

## Result

**Verdict: SUBSTANTIAL REVISION REQUIRED.**

Three findings are individually substantial under `cic-build-cycle`'s own test (a claim's substance, a sourcing conclusion, or a scope boundary): the entry's stated justification rests on a superseded premise (1); it contradicts the tracking item it closes without saying so (2); and its tier is asserted where the build's own method requires it to be argued, with the index now pointing at a section that does not contain the argument (3). Findings 8, 9, 10 and 12 each touch a sourcing conclusion or participant-facing content.

None of this is a reason to abandon the entry. The core scholarly finding is sound and I could not break it under direct attack; the Distortion Risk section is the best thing in this lexicon on its own terms; and the decision to surface the reciprocity asymmetry rather than paper over it is exactly right. What the entry needs is to be re-grounded on why it exists now that the title question has moved, to argue its tier, to bring its evidentiary note inside the Template's own provision and out of the runtime register, and to scope its central claim to what was actually checked.

**One matter for the project lead rather than for revision (see below), and it does not block a Round 2.**

### Escalation assessment — this reviewer's own view

`cic-build-cycle` reserves "Representative identity, name, or title decisions" and "a finding that cuts against an earlier decision" to the project lead. **My view: escalate, narrowly — not as a proposal to change the title, but because a decision's stated factual basis has been shown to be wrong, and the record still carries the wrong basis.**

A disclosed lexicon gloss is the right response to the *vocabulary* question and is sufficient for it. It is not sufficient for the record. Mark chose "Apocrisiarius — Deacon of the Letters" on 2026-07-22, and Open_Gaps item 15 attaches to that choice the assertion that the word is "a genuine, well-attested period term." This build's own verification now shows that is false for 312–451, and the best-known instance item 15 cites is a century and a half outside the window. That is not a lexicon finding; it is new information about the basis of an identity decision, and it lands squarely in the fourth escalation category.

Two things keep this narrow. First, the practical stakes are low: the 2026-08-28 registry ruling already removed "Apocrisiarius" from every participant-facing surface, so nothing unglossed is reaching anyone. Second, the finding does not argue against the title. A title drawn from the word a later age gave a practice this world genuinely had is a defensible choice — arguably a good one, and the chunk's own honest framing ("we do not use this word of ourselves") is exactly how such a choice should be carried. The escalation is not "reconsider the title."

What should go to Mark is a short, factual note with three items and a question: (a) the word is unattested in this world's window and the build has now verified that directly; (b) item 15's characterization of it as "well-attested" is wrong and item 15 is the record his 2026-07-22 choice hangs on; (c) the 2026-08-28 ruling has already superseded the long form, so the current title is "Deacon of the Letters" alone. The question is whether item 15 should be closed as moot and corrected, or whether he wants the word restored with the gloss now that one exists. He should be the one to answer that, because the answer determines whether this lexicon entry has a participant-facing job at all.

That escalation should be raised alongside the revision, not instead of it — the entry's other defects are ordinary build work and do not need him.
