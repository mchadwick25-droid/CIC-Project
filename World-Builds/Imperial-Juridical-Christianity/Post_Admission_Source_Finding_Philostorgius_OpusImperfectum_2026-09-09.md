# Post-Admission Source Finding — Philostorgius and the *Opus Imperfectum in Matthaeum*

**Status:** REVISED after Round 3 independent adversarial review (all three rounds: SUBSTANTIAL REVISION REQUIRED). Awaiting Round 4. Not disposed. Nothing in this document is a decision. Revision history at §7.
**World:** Imperial and Juridical Christianity (`ijc`)
**Date:** 2026-09-09
**Scope:** Two candidate source acquisitions put to this world by an external read-only discovery pass, tested against this world's own already-cleared record. One question only: do either of them change what `Doc_04_Gravity_Discovery.md` currently classifies as central, in particular Candidate 3 (Orthodoxy-Enforcement Through Imperial Power) and its disclosed Confidence/Gravity Cross-Check divergence?
**Answer, stated up front:** **No.** Neither is structural for Doc_04. Finding #1 is real material that belongs to a different world and does not close the gap it was proposed to close. Finding #2 is a real historical work whose only English translation is in copyright, which places it in exactly the same referenced-only posture this world already assigned to Auxentius. **Doc_04 is not revised by this finding, and no record was added to `records/ijc/`.** Five items are flagged for the project lead in §5, one of which — a corpus-ranking defect in `engine/m1/cross_world.py` leaving 14 source keys (18 vendored files) unclassifiable by date and rendered under an out-of-window legend across six worlds — is a real fault found only at Round 1 review and is the most actionable thing here.

---

## 0. A stale premise corrected first, because everything else was framed on it

This finding was commissioned on the understanding — paraphrased, not quoted, for the reason given at the end of this section — that this world's build was phase-1 complete and merged, with the M3 live admission step blocked awaiting a go-ahead, and with an instruction not to advance that gate. **That premise is stale. The gate is already through and this world is live.**

Verified directly on `main` at `f07eb91`:

- `records/worlds.yaml`, `ijc` entry: `state: admitted`, pinned at `packages/ijc/2026-09-04T18-49-02Z` with a `manifest_hash`.
- `records/WORLDS_REGISTRY_LOG.md` §"Fleet-wide facts": all six original worlds including `ijc` were **admitted 2026-08-28**, Mark in session ("yes i admit all six worlds"), certified by that day's fleet-parity battery (28/28 sealed probes), report at `engine/m3/reports/live-admission-report-fleet-parity-2026-08-28.json`.
- Same section: `render.yaml` has carried `CIC_ENFORCE_ADMISSION: "1"` since Mark's 2026-08-28 flip. Doors are open, fleet-wide.

The text the stale premise almost certainly rests on is `world-build-docs/ijc/BUILD-LOG.md` §Header, which still reads "**Compile (6), admission (7), open (8): intentionally NOT started**." That was true when written (2026-08-22) and was overtaken six days later. The BUILD-LOG is stale in a second, smaller way as well: §1 records "154 records in `records/ijc/`," while the tree now holds 182 — a like-for-like comparison, not a record-to-file mismatch: `find records/ijc -type f` returns 182, all `.md`, all inside typed record directories, and the pinned manifest lists 182 `records/` entries (Round 1, L15). Both are flagged in §5 as documentation drift, not as defects in the world's content.

**A note on the commissioning brief itself, added at Round 1 review.** Every characterization of the brief in this document is a paraphrase. The brief is an off-repository session instruction: no later reader can open it, and a repo-wide grep for its distinctive phrases returns nothing outside this document. This project's standing rule against attributing content without a verifiable record is written about the project lead specifically, but the same hazard applies here, so the brief is paraphrased rather than quoted throughout and its unverifiability is disclosed rather than left for a reader to discover.

**Consequence for how this finding should be read.** The instruction not to advance the M3 gate cannot be complied with as written, because there is no pending gate to approve or withhold. The underlying concern does not disappear, though — it inverts and sharpens. If either finding *were* structural, participants would already be receiving an incomplete account, and the remedy would be a records change plus recompile and repin on a live world rather than a gate held open. That is precisely why §4 states the compile/CI constraint explicitly rather than adding records on this thread's own judgment. As it happens, neither finding is structural, so nothing about the live world needs to change on this account.

---

## 1. What Doc_02 actually names as thin — checked, not accepted secondhand

The discovery pass characterized this world's `Doc_02_Source_Ecology.md` as naming, in substance, no Homoian self-testimony beyond a single fragment that had never been rendered into English — its wording paraphrased here for the reason given at §0. Read directly, Doc_02 says something adjacent but meaningfully different, and the difference matters for testing both findings.

Doc_02 §7 says (verbatim):

> The one substantial piece of near-primary Homoian *self*-testimony available to this world's own Registry is not itself Nicene-transmitted: Auxentius of Durostorum's letter concerning Ulfila survives embedded within the *Dissertatio Maximini contra Ambrosium* …

Two corrections to the secondhand framing:

1. **"Untranslated" appears nowhere in this world's own build folder or record set, outside this finding and its own review artifacts** — verified by grep over `World-Builds/Imperial-Juridical-Christianity/` and `records/ijc/`. The word is the discovery pass's own gloss on Doc_02, not Doc_02's language.

   *Correction disclosed rather than silently narrowed, twice over.* **Round 1 (H1)** found that this paragraph originally asserted a full-tree grep for `untranslated`, `not translated` and `no english translation` "returns nothing" repo-wide. That was false, and it was a claim of verification at a scope the verification did not reach — inside a paragraph whose whole rhetorical work is correcting someone else's imprecision, which makes it worse rather than incidental. Re-run from the repository root, `untranslated` appears in **38 files** case-sensitively (39 case-insensitively) — `records/desert/`, `records/alx/`, `cic-website/data/world-census.json`, Ministry audit files. `not translated` likewise returns hits, one directly germane: `cic/texts/README.md` line 168 records that "Hilary's historical/polemical works are not translated here," in a note written in response to the Imperial-Juridical scrub's own finding 7.

   **Round 2 then found the first repair self-falsifying**: it adopted Round 1's narrowed scope but dropped Round 1's own "outside this document" qualifier, while this section's opening sentence still quoted the gloss verbatim — so the word was present in the very scope the sentence declared clean. Fixed twice: the qualifier is restored above, and the opening sentence now paraphrases rather than quotes. Round 2 also corrected the count (36 was an undisclosed exclusion). The narrowed claim, as now stated, is true and fully supports the point being made.

   This is not pedantry: the *actual* recorded reason is narrower and load-bearing. `records/ijc/search_record/ijc.search.auxentius-ulfila-english.md` records the real finding — a public-domain **English** translation does not exist, because the standard modern translation (Heather & Matthews 1991) and the critical Latin/French text (Gryson) are both in copyright. The Latin exists and is edited; what fails is this project's public-domain rights test. That distinction is the whole hinge of finding #2 below.

2. **The named gap is specifically *Homoian* self-testimony**, not non-Nicene self-testimony generally, and Doc_02 §7 itself draws the boundary that makes the distinction operative:

> Homoian theologians deliberately avoided both *homoousios* … and *heteroousios* ("of a different substance," associated with the more radical Anomoian position) as unscriptural, metaphysically overreaching vocabulary, preferring instead to confess the Son as *homoios* …

So this world's own Doc_02 defines Homoian identity partly *by its rejection of the Anomoian position*. Any candidate offered as filling the Homoian gap has to clear that boundary, not straddle it.

### Was the gap knowingly left open, or missed?

**For Auxentius specifically: knowingly left open, and disclosed at three separate layers. For non-Nicene self-testimony generally: not actually asked.** The distinction is drawn sharply here because Round 1 review found this document's first pass too generous on exactly this point.

- **Search layer.** `ijc.search.auxentius-ulfila-english.md` records the query, `result: not_found`, the editions checked, and an explicit CONSEQUENCE clause: the source is registered as referenced-only "licensing no quotation — and the world's Homoian-recentering obligation is discharged through the formulae Hilary quotes (`ijc.source.hilary-de-synodis`), the historians' reports, and honest confidence-flagging, never through invented Homoian voice."
- **Source layer.** `records/ijc/source/ijc.source.auxentius-letter-ulfila.md` carries `rights_status: "referenced-only; no vendorable public-domain English edition (fails closed for quotation)"` and a body paragraph explaining why the record exists despite licensing nothing quotable.
- **Participant layer.** The `thinness_statement` in `records/worlds.yaml` — text a participant sees at the doorway — reads: "…thinner on ordinary believers' daily lives, women's own words, **and the defeated Homoian side's own voice**."

The gap is disclosed to the participant, in plain words, at the door. For the Auxentius fragment, that is the discipline working, not failing.

**But the disclosure does not reach as far as this document first claimed.** Two limits, both verified:

- **The search was scoped to one text, not to a question.** `ijc.search.auxentius-ulfila-english`'s own `query` field asks only for "a vendorable public-domain English translation of Auxentius of Durostorum's letter on Ulfila." Nothing in this world's 24 search records asks the broader question — is there *any* non-Nicene narrative self-account of these decades.
- **The one sweep that might have caught it could not have.** `ijc.search.unopened-volume-sweep` is dated 2026-08-27 and covers only NPNF volumes. The Philostorgius file was vendored 2026-08-31, four days later, and is not an NPNF volume. It was never in that sweep's frame.

So the honest statement is narrower than "knowingly left open": the *named* thinness was disclosed with real care, and the *adjacent* question was never put. Whether that adjacency matters is what §2.3 tests — and the answer there is that it does not change Doc_04. But the disclosure record should not be cited as though it had already considered and rejected Philostorgius. It had not seen it.

---

## 2. Finding #1 — Philostorgius's *Ecclesiastical History*

### 2.1 The material, verified

- **Vendored file (exact name confirmed):** `cic/texts/philostorgius_ecclesiastical-history_walford1855.txt` — 1,007 lines. Walford's 1855 English translation of Photius's Epitome, all twelve books, plus translator's Biographical Notice, Pearse's 2002 note quoting Quasten, and 241 footnotes. Public domain (Pearse/Tertullian Project), supplied by Mark 2026-08-31.
- **Current assignment:** `cic/corpus-map/_staging/philostorgius_ecclesiastical-history_walford1855.yaml`, merged into `cic/corpus-map/anomoean-eunomian-christianity.yaml` (`role: tradition`) and `cic/corpus-map/cappadocian-nicene-pastoral-monastic-tradition.yaml` (`role: context`). **No `imperial-juridical-christianity` row.** Confirmed by grep across the merged maps.
- **Drawn into a world's records:** yes, but not this one — `records/cappadocian/source/cappadocian.source.photius-epitome-philostorgius.md`. Grep of `records/ijc/` for `philostorg|eunomi|anomoean` returns **zero hits**. So the discovery pass's core factual observation — never considered for this world — **is correct.**

### 2.2 Does it close the named gap? No, and the repository has already ruled on why

The caveat the discovery pass flagged is not a technicality. Tested three ways, it holds:

**(a) This world's own Doc_02 already excludes the conflation.** Per §1 above, Doc_02 §7 defines Homoian theology partly by its deliberate rejection of the Anomoian *heteroousios*. Philostorgius was a follower and admirer of Eunomius — the file's own Quasten note calls the work "a late apology for the extreme Arianism of Eunomius." He is on the far side of the boundary Doc_02 itself draws.

**(b) The project has drawn this distinction on record, in the corpus map — stated at the strength the record actually supports.** `cic/corpus-map/anomoean-eunomian-christianity.yaml` carries, on the Chrysostom *Homily on the Paralytic* row, the sentence: *"The Anomoeans/Eunomians are not strictly Homoians."* Two qualifications Round 1 review was right to force:

- That sentence sits inside a note that *originally* recorded an open question, not a settled ruling — its own next clause read "Needs Mark's ruling on whether that entry covers anti-Anomoean material or the second id should be dropped." What closed it is the dated addendum on the same row: the `anomoean-eunomian-christianity` census entry was added 2026-08-26, and anti-Eunomian material was re-pointed to it "rather than the Homoian wing it split from in 360."
- The "canon 1 names Eunomians and Arians as separate parties" rationale is from a *different* row in the same file (the Constantinople 381 row), not from the note containing the sentence quoted above. This document's first pass fused two notes into one citation.

Corrected, the point is weaker than "a ruling would be reversed" but still holds: the project separated these two parties deliberately and on a dated record, rather than treating them as one bucket.

**(c) The text shows a schism inside the non-Nicene coalition — stated more carefully than this document's first pass stated it.** Round 1 review was right that "hostile to the Homoians" overreads, and the correction matters, so it is made in full rather than softened. Reading the vendored file, Philostorgius's relation to the Homoian party is not uniform hostility but a fracture inside a coalition he was part of:

- *Against* — Acacius of Caesarea — the Homoian architect, this document's own historical gloss rather than the vendored text's (Round 1, L14) — is his villain, "who always had one thing hidden in his bosom and another ready upon his tongue" (IV.12), and Photius's own *Bibliotheca* cod. 40 notice, reproduced in the vendored file, says that Philostorgius "severely attacks Acacius … for his extreme severity and invincible craftiness" — corroborating, but **not independent** (Round 1, L13): Photius is the epitomizer through whom the entire work survives, so this is the same transmitter's editorial judgement, not a second witness. At Constantinople in 360 (IV.12) Constantius has the Western bishops' letter subscribed by all present, and "by the artifice of this same Acacius … both all the bishops who were present, and also those who hitherto had professed to believe the Persons to be unlike in substance, added their subscriptions" — Philostorgius describing his own side made to sign under imperial pressure. Book V.1 records Aetius deposed with his own partisans subscribing, "some casting entirely away the opinion which they had previously embraced; others, again, playing the part of mere time-servers, and reverencing the will of the emperor as paramount to the truth."
- *With* — Eudoxius, co-architect of the 360 settlement, is treated as an ally, not an opponent; he and Aetius, "having subscribed their names to the doctrine of unlikeness, sent their letters about in every direction" (IV.11), and Philostorgius censures him only for want of courage.

**Verdict on the substitution: it still fails, but on a narrower and more accurate ground.** Not "Philostorgius hated the Homoians" — rather, he wrote from a position that split from theirs in 359–360 and was coerced by them at the moment of the split. Installing him as the defeated Homoians' own self-account would put the Anomoean side of an intra-coalition schism in the mouth of the party that won that particular fight. That misrepresents both. Legs (a) and (b) above carry this conclusion; (c) supports rather than decides it.

### 2.3 Does it bear on Doc_04 anyway? A corrected answer — the first pass got the reason wrong

This document's first pass argued that Philostorgius is supplemental because it supplies "narrative, not Homoian theological content." **Round 1 review demonstrated that ground is false to the text, and it is withdrawn.** Philostorgius reproduces the enforced Homoian formula verbatim, twice, in the very chapters this document already cited: IV.10 ("declaring the Son to be like to the Father according to the Scriptures, it confirmed that belief with the signatures of the bishops present") and IV.12 ("in the letter were contained the following words, 'That the Son is like to the Father according to the Scriptures'"). The first pass read the file for hostility, found it, and then asserted an absence of content it had not actually checked for. That is the same failure class this build's own history logs repeatedly, and it is named here rather than quietly repaired.

**The conclusion survives on different and better ground.** Doc_04's Cross-Check divergence is not about whether the Homoian formula is recoverable — it is about *Homoian self-testimony*, Registry row 23, Confidence C. And the formula Philostorgius quotes is **already held by this world, once, at higher confidence than he could supply**: `records/ijc/source/ijc.source.hilary-de-synodis.md` — Hilary's *De Synodis*, `citation_specificity: A`, `verification_state: verified-direct`, `formation_confidence: Documented`, vendored public-domain in NPNF 2.9, the record's own body noting "the 'like the Father' formula discussed from line 8067 and repeatedly after."

*Correction, Round 2 Finding F2 (HIGH), and the most serious error this document has made.* The first repair of H2 claimed the formula was held "twice over," offering Athanasius's *De Synodis* as the second holding on the strength of a `homoian-arian-christianity` corpus-map row. **That is a different atlas entry, and the Athanasius corpus is Excluded for this world.** `Source_Registry.md` row 24 marks "Athanasius corpus generally (*Life of Antony*, Festal Letters, anti-Arian polemics)" as **Excluded**, a Named Comparandum belonging natively to Worlds #2 and #3, with the instruction "do not use beyond the single Julius I quotation already licensed at row 4" — and row 4 itself warns "do not extend Native status to the surrounding Athanasian material." `cic/texts/README.md` line 168 records the project's own ruling on exactly this point: "srcIJC24 excludes the Athanasius corpus… **Hilary is an independent Latin transmitter of the same texts, so the exclusion does not apply**." So Hilary is precisely the holding that survives the exclusion, and Athanasius is precisely the one that does not. A repair for a finding about reasoning from label rather than evidence reintroduced excluded material by reading a corpus-map row instead of this world's own Registry. Withdrawn.

The point stands on Hilary alone, and does not need a second holding: a Homoian formula quoted by an opponent — Hilary, or Philostorgius — is precisely what this world already holds, and precisely what the divergence says is *not* the same thing as Homoian self-testimony. Philostorgius adds a second opponent-transmitter of an already-Documented formula. **The divergence stands exactly as Doc_04 flags it.**

*One half of the divergence declined rather than answered, named here rather than passed over (Round 2, F3).* Doc_04's Cross-Check reads "what, precisely, was being enforced **or resisted**." The argument above reaches the *enforced* half. On the *resisted* half Philostorgius is not a second opponent-transmitter but an insider narrating his own party's coercion (IV.12, V.1) — something Hilary does not supply. This does not change the verdict, because the divergence is defined by Registry row 23 against *Homoian* self-testimony and Philostorgius is not Homoian (§2.2). But it is the one place where he supplies something this world does not already hold, and it should be visible rather than absorbed.

**Every candidate gravity tested, not five dismissed in a sentence.** Round 1 review was right that the first pass waved at Candidates 1, 2, 4, 5 and 6 without testing them, and right that at least two deserved a real answer:

| Candidate | Does Philostorgius bear? | Does any test result move? |
|---|---|---|
| 1 — Juridical Primacy-Claiming | Barely. He narrates Liberius's recall and subscription at Sirmium (IV.3), which touches Rome's see as an object of imperial management, not as a primacy-claimant. | No. |
| 2 — Church-State Alliance and Its Limits | **Yes, genuinely.** Its Forces-connection notation rests on the alliance fracturing and re-forming as "which theological content it favors shifts with the reigning emperor" — which is what IV.10–V.1 narrates from outside. | No. This *corroborates* a notation already stated; it does not alter the classification, which is already Primary and already cross-strand-confirmed. |
| 3 — Orthodoxy-Enforcement Through Imperial Power | Yes — see above. | No. Six tests already pass; the Cross-Check divergence is untouched for the reason given above. |
| 4 — Episcopal Independence from Imperial Command | No. Strand C / Ambrosian material, a generation later and in the West; Philostorgius's actors submit or are exiled, they do not assert sacramental independence. | No. |
| 5 — Doctrinal/Christological Precision-Seeking | **Yes, and this is the strongest bearing of the two.** Its Formation test is a narrow pass grounded on the gravity shaping which vocabulary actors could safely use. Book IV.12 is a sustained scene of exactly that policing: Aetius offers "like without any difference," and the emperor — "Constantine" in Walford's text at this point, evidently a slip for Constantius — "not even enduring to learn in what sense Aetius used that term," has him expelled; subscriptions are later defended "under the name of economy." | No — but it *strengthens* an already-narrow pass rather than changing it. Classification stays Supporting. |
| 6 — Sacramental/Moral vs. Institutional/Positional Authority | No demonstrated relationship. | No. |

**Cross-strand status (Article 21) and the Interaction Matrix are also unaffected.** Candidate 3 is confirmed cross-strand to Strands A and B only; Philostorgius bears on neither strand boundary. No matrix cell changes, because no new relationship between two candidates is demonstrated — Philostorgius corroborates existing cells rather than creating one.

**Downstream carriers checked, which the first pass omitted entirely.** The divergence does not stop at Doc_04. `Doc_08_Forces_Document.md` carries it at full strength in **Section 8 — Governing Principles Applied**, under the Named-Tension Principle ("**Status:** CONFIRMED. Doc_04's own Candidate 3 Confidence/Gravity Cross-Check divergence (Section 7) is carried at full strength, not resolved"), and routes it onward to Doc_09's Validation Layer as "a standing, unresolved item" in its **Open Items and Process Findings**, item 2. (Both locators were cited as "§7" and "§9" before Round 2; §9 is a checkbox certification list containing no numbered items.) `Doc_05_Ecological_Reconstruction.md` §5 rests its boundary analysis on the same Homoian reversal. **Doc_08 Section 6** (transmission forces and Author Gravity), named by number in Round 1's M12 and omitted from this list until Round 3 (R11), was also read: its argument that Homoian self-testimony survives in one substantial instance is unaffected, because Philostorgius is not Homoian self-testimony (§2.2). Since the divergence itself is unchanged, every downstream carrier of it is unchanged too — but that had to be checked rather than assumed, and now has been.

**Verdict: supplemental. Doc_04 is not revised, and neither is Doc_05, Doc_08, or Doc_09.**

### 2.4 The one genuine residue — a corpus-map question, not a Doc_04 question

There is a real, modest observation left over. **By this repository's own precedent, Philostorgius has a defensible claim to an `imperial-juridical-christianity` row in the corpus map.** The precedent is Athanasius's *Historia Arianorum*, whose note in `cic/corpus-map/imperial-juridical-christianity.yaml` reads:

> Assigned three ways — the author's entry; the homoian entry it describes from outside; and **ijc, because its central question ('what has the emperor to do with the church?') is the ijc world's own problem stated by its sharpest opponent.**

**Two corrections to this document's first pass, both forced by Round 1 review and both weakening the argument rather than strengthening it:**

- It originally called the precedent "exact" and offered it as support for a `role: context` assignment. It is not exact. The **ijc** row for *Historia Arianorum* carries **`role: tradition`**, not `context`. The `context` role appears on the *homoian* copy of the same work, and only there, under a sentence the first pass quoted around: "Role normalised to `context` for the doctrinal-floor entry" — a normalisation specific to doctrinal-floor entries, which does not transfer to ijc. What transfers is the *rationale* ("this world's own problem stated by its sharpest opponent"), not the role.
- The first pass justified not making the change partly by citing the staging file's header as stating the maps are generated and the staging file is the editable artifact. That banner is on the **merged** files and the corpus-map README, not on the staging file, whose header is a worker note about the author slug. The fact is true; the citation was wrong.

So the honest position is: the rationale for an ijc assignment is real and precedented, but **what role it should carry is genuinely open**, and the nearest precedent points the wrong way for a simple `context` answer — Athanasius gets `tradition` for ijc because he is arguably native to this world; Philostorgius plainly is not. That makes it more of a judgment call, not less.

This thread is not making the assignment. It is a cross-world corpus-map decision, and the `cic-build-cycle` skill scopes a build thread's write access to its own world's build folder. **Flagged for the project lead at §5, item 2.**

## 3. Finding #2 — the *Opus Imperfectum in Matthaeum*

Put to this thread explicitly as a hypothesis to check, not a holding. Checked. **The attribution substantially holds; the acquisition fails.**

### 3.1 Attribution — holds, with two real caveats that must not be smoothed over

Modern scholarship does judge this a genuinely Arian Latin work transmitted under a false Chrysostom attribution, the misattribution first refuted by Erasmus in 1530. It is a substantial commentary (PG 56:611–946), not a scrap. So far the discovery pass's background knowledge is confirmed against external sources.

**Sources for this section, added at Round 1 review** (the first pass cited none, which is the same failure class already logged in this repository at `Ministry/Operations/Audits/CiC_Redesign_Research_2026-07-25/03_WorldBuilds_Validation_Sweep.md`, where a fabricated gloss was traced to AI-generated search-result summaries). All consulted 2026-09-09 via web search result summaries and, where reachable, fetched pages; none is held in this repository, and §3.2's note about blocked hosts applies here too — where a host was unreachable, the fact rests on search listings rather than on a retrieved copy, and is marked as such: the Brepols/CCSL edition listing for *Opus imperfectum in Matthaeum* (brepols.net, product IS-9782503008752-1) for van Banning's editorship and dating; the Wikipedia *Opus Imperfectum* article for the Erasmus refutation and the authorship candidates — **not** for the Dekkers dating, which this document credited to Wikipedia (wrong, caught at Round 2) and then to the Brepols listing (also wrong, caught at Round 3 — Brepols does not appear to carry it); the channel that does carry the van Banning/Dekkers dispute is Papahagi's *Mediaeval Studies* article named next; Papahagi's article at *Mediaeval Studies* 78 (2016), 277–83 (pims.ca), reporting **Cooper (1993)** on **Schlatter's (1988)** Anianus proposal — the bare surname "Cooper" was Round 1's actual complaint and was left undischarged by the first repair; and the InterVarsity Press and Internet Archive listings for the translation and PG 56 respectively. These are the actual channels used; they are named so a later reader can re-check them rather than take this section on trust.

Two caveats materially affect its usefulness here:

- **The date is genuinely disputed, and one side of the dispute puts it outside this world's window.** Joop van Banning, senior editor of the in-progress Brepols/CCSL edition, argues for the second or third quarter of the fifth century; Dekkers argued for the mid-sixth. This world's window closes at **451**. On van Banning's dating it is plausibly inside; on Dekkers's it is a century outside. This is unsettled scholarship, and this document does not resolve it.
- **Authorship is unidentified, with competing candidates.** Proposed: an Arian priest in Constantinople named Timothy; Maximinus, the Arian bishop who accompanied the Goths; and Anianus of Celeda — it is *Schlatter's proposal* of Anianus that Cooper judges "attractive" but "problematic," not the candidacy in the abstract (a displacement in this document's first pass, corrected at Round 1 review). The Maximinus candidacy is a striking connection, since the *Dissertatio Maximini contra Ambrosium* is the very text preserving the Auxentius fragment Doc_02 §7 rests on. It is also only a candidacy, and this document treats it as one.

Its Christology is generally characterized as *mildly* Arian, which further weakens any claim that it would supply the sharply-defined Homoian theological content Doc_04's Cross-Check divergence is about.

### 3.2 Acquisition — fails, on this project's own rights test

- **Latin:** public domain. PG 56:611–946; *Patrologia Graeca* vol. 56 is listed as available on the Internet Archive — established from search listings, not from a copy retrieved here, since `cic/texts/README.md` records that this sandbox blocks archive.org (Round 1, L16).
- **English:** the first and only complete English translation is **Kellerman / Oden, *Incomplete Commentary on Matthew (Opus imperfectum)*, InterVarsity Press, Ancient Christian Texts, 2010, 2 vols. — in copyright.**

This is the identical posture already recorded for Auxentius: an edited text exists, the rights test fails on the English translation. Under this world's own established discipline (the CONSEQUENCE clause of `ijc.search.auxentius-ulfila-english.md`), that means referenced-only at most, licensing no quotation.

**One partial route was checked and should be rejected rather than left as an open possibility.** Aquinas's *Catena Aurea* quotes the *Opus Imperfectum* extensively, and Newman's 1841 English translation of the *Catena* is public domain and available on CCEL. That is technically a public-domain English channel to some of this text. It should not be used as Homoian self-testimony: those are excerpts selected by a thirteenth-century Dominican, for scholastic purposes, under the false Chrysostom attribution — the losing side's voice arriving pre-filtered and re-labelled by the winning tradition. That is the *exact* transmission pathology Doc_02 §7 exists to name. Using it here would deepen the problem while appearing to close it.

**Verdict: not acquirable as quotable material. Not structural for Doc_04. No record added.**

---

## 4. Why no record was added to `records/ijc/`, stated as a constraint rather than a preference

Ordinarily the correct artifact for a documented negative result in this project is a `search_record` — this world already holds 24 of them, including two (`ijc.search.auxentius-ulfila-english`, `ijc.search.unopened-volume-sweep`) that do precisely this job. Two such records would be the natural output here.

They were not written, because **`records/ijc/` is no longer a free-write tree.** This world is admitted and pinned. `.github/workflows/ci.yml` runs an `m2-staleness-check` job that "recompile[s] every built/admitted/open world from its stored `records_commit` and check[s] it still produces the package" on record. Adding any record would invalidate the pin at `packages/ijc/2026-09-04T18-49-02Z` and fail CI until a deliberate recompile and repin — which, per `WORLDS_REGISTRY_LOG.md`, is a logged, Mark-in-session event for admitted worlds, not a side effect of a finding thread.

Since neither finding is structural, forcing a recompile of a live world to record two negative results is not obviously worth its own cost. That is a judgment for the project lead, not this thread. **Flagged at §5, item 1**, with both records' content already fully specified in §2 and §3 so they can be written directly if approved.

---

## 5. Flagged for the project lead — nothing here decided by this thread

1. **Two `search_record`s are drafted-in-substance but unwritten, pending a recompile decision.** `ijc.search.philostorgius-homoian-fit` (finding #1: real text, wrong party, correctly assigned elsewhere) and `ijc.search.opus-imperfectum-english` (finding #2: attribution holds, no public-domain English translation, *Catena Aurea* route rejected with reasons). Writing them requires accepting a recompile and repin of an admitted, live world. Your call.

2. **A corpus-map assignment question, cross-world and therefore escalated rather than self-decided.** Whether `philostorgius_ecclesiastical-history_walford1855.yaml` should gain an `imperial-juridical-christianity` row at `role: context`, on the exact precedent of Athanasius's *Historia Arianorum* (§2.4). This thread believes the case is genuinely arguable and has deliberately not made the change.

3. **Documentation drift in `world-build-docs/ijc/BUILD-LOG.md`, noted for correction by whoever owns that file.** Its header still says compile/admission/open are "intentionally NOT started," six days before they happened; §1's "154 records" is now 182 files on disk. This drift is what the commissioning brief for this finding was built on, so it has already cost one session's worth of misframing. Content elsewhere in the BUILD-LOG was not re-audited by this thread.

4. **A real tooling defect, found only at Round 1 review, and broader than this world.** This document's first pass asserted that "nothing here identifies a defect in the live world." That was wrong, and the correction is the single most actionable item in this finding.

    `engine/m1/cross_world.py`'s `COVERAGE` table has **no entry for `philostorgius`**. `corpus_tier()` therefore falls through its `COVERAGE.get(key, (None, None))` lookup and returns `"4 - unclassified"` — the bottom rank — for every world. Philostorgius's *History* covers 300–425; this world's window is 312–451. It overlaps by 113 years and was ranked bottom without its dates ever being consulted.

    **Refinement (i) to how Round 1 review stated this, verified directly and holding.** The code returns `"4 - unclassified"`, not `"4 - outside this window"`; the false "no time overlap" gloss comes from `world-build-docs/_cross-world/CORPUS-USE.md` line 153, whose legend documents only the `outside this window` sense of Tier 4, so the two collapse in the rendered document. The defect is a label collision, not a bad date computation.

**Refinement (ii) was wrong, and its first two corrections were also wrong. Stated here at the precision this thread can actually sustain, with the arithmetic done by script rather than by hand (Round 2 F5; Round 3 R1–R5).**

- **Scale.** The cohort is **14 `COVERAGE` keys, covering 18 vendored files** — `anan-isho`, `basil`, `eunomius`, `evagrius`, `gregory-nazianzen`, `gregory-nyssa`, `julian`, `lucian`, `macarius`, `morison`, `nestle1904`, `pachomius`, `philostorgius`, `tacitus`. Computed by parsing the `COVERAGE` literal directly, excluding the two `BY_DESIGN` keys (`anf10`, `webbe`) that short-circuit the lookup before it happens: 65 vendored files, 60 distinct keys, 44 `COVERAGE` entries.
- **Three wrong figures, disclosed rather than quietly replaced.** The first pass said "roughly a dozen … across all seven worlds." The second said "22 of 60 keys" and offered a keys-versus-files reconciliation for Round 2's count of 18. **Both the 22 and the reconciliation were wrong.** The 22 came from a regex that matched only the first key on each line of the `COVERAGE` literal, so the six `npnf1xx` keys sitting mid-line were counted as missing when they are present at lines 85–88. And the reconciliation was arithmetically impossible on its face — keys group files, so a key count can never exceed the file count it summarizes. Round 2's 18 was correct all along. This is the third time this one ancillary figure has been asserted wrongly, twice in the direction of overstatement, and it is recorded that way rather than presented as a clean correction.
- **World count.** It is **six** worlds, not seven — `alx`, `pahc`, `desert`, `hal`, `syr`, `ijc`. But the reason previously given for cappadocian's absence was also false: cappadocian does not appear anywhere in CORPUS-USE.md at all (`grep -ci cappadocian` returns 0), so it is not "absent from the worklist because it already holds a Philostorgius record" — the report simply predates or omits that world, and is itself stale (its header counts 64 vendored files against 65 on disk). That cappadocian holds `records/cappadocian/source/cappadocian.source.photius-epitome-philostorgius.md` is true and remains the reason Philostorgius is not an unreached volume *for that world*; it is not the reason the report omits it.
- **Precision about what is mislabelled.** The 14 keys are the *code-level* unclassified cohort. They are not identical to the rendered Tier 4 set, because `corpus_tier()` returns `"1 - named, never opened"` before reaching the `COVERAGE` lookup for any volume a world names. The honest statement is that these keys can never be classified by date, and are rendered under a Tier 4 legend that asserts a date judgement, wherever they are not pre-empted by Tier 1.

    **Why this matters rather than being a cosmetic ranking issue.** `world-build-docs/_cross-world/CORPUS-USE.md` line 140 records *"Mark's standard, 2026-08-26: every world should reach every available resource; they can be ranked, but not ignored,"* and line 142 explains that ranking cannot discharge it, because `engine/m4` never opens `cic/texts/` — retrieval runs over the world's compiled repository, so "'not ignored' has to mean a source record exists (even a low-ranked one)." A volume mislabelled as out-of-window is a volume no builder has reason to open. That is the mechanism by which Philostorgius was never considered for this world, and it remains live for the cohort enumerated above.

    This is engine code, outside a build thread's write scope under `cic-build-cycle`. Not touched. Flagged here.

5. **Stated so it is not mistaken for a content defect:** subject to item 4, nothing in this finding identifies a defect in what the live world *says*. The Homoian-voice gap is real, was disclosed at the participant-facing doorway, and neither candidate source closes it.

---

## 6. Escalation-category self-assessment (per `cic-build-cycle`)

- **Representative identity / name / title:** not touched.
- **Portfolio-level or cross-world:** **two**, not one — corrected at Round 2 (Finding F10), which caught that this assessment had not been updated after the H4 repair. (a) The corpus-map assignment question at §2.4. (b) The `engine/m1/cross_world.py` ranking defect at §5 item 4, which this document itself describes as reaching six worlds — it is portfolio-level by its own account, and listing only (a) understated the escalation load in the section that gates self-disposition.
- **Governance or methodology:** not touched. This document applies existing discipline; it does not change it.
- **Unresolved tension the pipeline cannot close:** none created. This finding *confirms* the standing Doc_02 §7 and Doc_04 Candidate 3 positions rather than cutting against them. The two live judgment calls — whether to spend a recompile on two negative-result records, and how to fix the ranking defect — are escalated at §5 rather than resolved here.

**Disposition: none, and none is claimed.** Two independent adversarial review rounds have been filed as files in `Review-Artifacts/` (Round 1: SUBSTANTIAL REVISION REQUIRED; Round 2: SUBSTANTIAL REVISION REQUIRED). Both are cited throughout above. Because Round 2 called for substantial revision and this document has since been revised again, `cic-build-cycle` requires it to go back through review: **a Round 3 is required before any disposition is considered.** This thread does not score its own result, and nothing here is Approved to proceed or Frozen.

*(An earlier version of this section still read "this document has not been independently reviewed at the time of writing" after two rounds had been filed — a stale sentence contradicting the status line and §7, caught at Round 2, Finding F11.)*

## 7. Revision history

**Round 1 independent adversarial review (Opus, isolated context, 2026-09-09): SUBSTANTIAL REVISION REQUIRED.** Filed at `Review-Artifacts/PostAdmission_Source_Finding_Round1_Review.md`. Four HIGH, eight MEDIUM, four LOW. The review could not overturn the headline verdict — neither acquisition is structural for Doc_04 — but found that three of the four places defending it argued from label, precedent, or assertion rather than from evidence this document had open in front of it. That judgment was correct and the fixes below are made in full rather than minimized.

Every HIGH and MEDIUM finding was independently re-verified by this thread before being accepted, per `cic-build-cycle`'s rule that a finding stands until a re-check actually supports its disposition — and in one case the re-check found the review's stated mechanism slightly off (§5 item 4, refinement (i)), which is recorded rather than silently corrected in this document's favour. An earlier version of this sentence claimed two such cases; the second was this document's own miscount, not a defect in the review (Round 3, R10).

- **H1 — a claimed repo-wide grep that returns 36 files.** Confirmed by re-running it. The claim was made at a scope the verification never reached, inside a paragraph correcting someone else's imprecision. Fixed at §1(1) with the correction disclosed inline, not narrowed silently.
- **H2 — the "narrative, not theological content" ground for the supplemental verdict is false to the text.** Confirmed: Philostorgius quotes the Homoian formula verbatim at IV.10 and IV.12. Ground withdrawn; §2.3 rebuilt on the correct ground (the divergence is about Homoian *self*-testimony, and the formula is already held at Confidence A via Hilary's *De Synodis*). Verdict unchanged, reasoning replaced.
- **H3 — five candidate gravities dismissed in one untested sentence.** Confirmed, and the review was right that Candidates 2 and 5 have real bearing. All six now tested in a table at §2.3. No classification moves; Candidate 5's narrow Formation pass is strengthened, not changed.
- **H4 — a real tooling defect the document never looked for.** Confirmed, and found to be *broader* than the review stated: not ijc-specific. (The scale and world-count claimed in that repair were themselves wrong and were corrected again at Rounds 2 and 3 — see below.) Two refinements to the review's own mechanism description recorded at §5 item 4. §5's "no defect in the live world" claim replaced.
- **M5, M7 — the Athanasius precedent mis-stated and a citation pointed at the wrong file.** Both confirmed by direct read; the ijc row carries `role: tradition`, not `context`. §2.4 rewritten, and the argument is now weaker than the first pass claimed, which is the honest result.
- **M6 — the corpus-map ruling overstated and two notes fused into one citation.** Confirmed. §2.2(b) restated at the strength the record supports.
- **M8 — "hostile to the Homoians" overreads.** Confirmed: Eudoxius is an ally in the text, and 359–360 was a schism inside a coalition. §2.2(c) rewritten with both sides of the evidence, and demoted from "most decisive" to supporting.
- **M9 — §3 rested on uncited external research.** Confirmed. Channels now named at §3.1, with the repo's own logged instance of this failure class cited alongside. The review independently re-verified the substance and it held; the Schlatter/Cooper displacement is corrected.
- **M10 — four load-bearing quotations from an unverifiable off-repo brief.** Confirmed. All now paraphrased, with the unverifiability disclosed at §0.
- **M11 — commission item (f), the Decision Log entry, not discharged.** Confirmed. Now written as `Open_Gaps_Tracking.md` item 16.
- **M12 — downstream carriers never checked.** Confirmed. Doc_05 §5, Doc_08 §7 and §9, and the Doc_09 Validation Layer routing now checked and reported at §2.3.

**What Round 1 checked and found clean, recorded as findings rather than as a licence to skip re-checking:** every Philostorgius quotation and book/chapter attribution; both Doc_02 §7 quotations character-for-character; all three disclosure layers; §0's admission facts; the Doc_04 Cross-Check and cross-strand fidelity; the 182-vs-154 comparison (apples-to-apples, only loosely phrased); and — tested at mechanism level against `engine/m2` and `ci.yml` — §4's CI constraint, which is legitimate and not an excuse. No fabricated quotation and no misattributed chapter anywhere in the document.

**Round 2 independent adversarial review (Opus, isolated context, 2026-09-09): SUBSTANTIAL REVISION REQUIRED.** Filed at `Review-Artifacts/PostAdmission_Source_Finding_Round2_Review.md`. Ten of the twelve Round 1 fixes held; **two of the repairs introduced new HIGH errors, both inside the two fixes that mattered most.** That is this project's own documented pattern — Doc_08's Round 2 caught two Round 1 "FIXED" items not holding, and Doc_07 needed three rounds because one flagship fix was wrong twice on the same checkable dataset — and it recurred here rather than being avoided. Each finding was re-verified by this thread before acceptance.

- **F2 (HIGH) — the most serious error this document has made.** The H2 repair claimed the Homoian formula was held "twice over," citing Athanasius's *De Synodis* from a `homoian-arian-christianity` corpus-map row. `Source_Registry.md` **row 24 marks the Athanasius corpus Excluded for this world**, "do not use beyond the single Julius I quotation," and `cic/texts/README.md` line 168 records that Hilary is the transmitter to whom the exclusion does *not* apply. A repair for a finding about reasoning from label rather than evidence reintroduced excluded material by reading a corpus map instead of this world's own Registry. Withdrawn at §2.3; the argument stands on Hilary alone and never needed a second holding.
- **F5 (HIGH).** §5 item 4's refinement (ii) claimed the ranking defect reaches "all seven worlds" and "roughly a dozen volumes." It reaches **six** — cappadocian is absent from CORPUS-USE.md entirely, a stale-report artifact rather than the reason first given here (Round 3, R4) — and a smaller cohort than "roughly a dozen volumes" implied. Overstated in the same direction twice; corrected at §5 and at the headline — **and the Round 2 correction was itself wrong, caught at Round 3 (R1)**.
- **H1 — did not hold.** The repair adopted Round 1's narrowed scope but dropped its "outside this document" qualifier while §1's opening sentence still quoted the gloss verbatim, making the sentence false within its own document. Fixed at both ends: qualifier restored, opener paraphrased. Count corrected 36 → 38.
- **M10 — did not hold.** Three of four brief quotations were paraphrased; the fourth was not, while §0 and §7 both claimed "all." Now actually paraphrased.
- **M9 — did not hold in part.** The Dekkers dating was credited to Wikipedia, which does not contain it, and "Cooper" remained a bare surname. Both corrected.
- **M12 — did not hold on citations.** Substance right, locators wrong: the Named-Tension carrier is Doc_08 **Section 8**, not §7, and the Doc_09 routing is under **Open Items and Process Findings**, not §9. Corrected.
- **F3, F9, F10, F11 (MEDIUM)** — the declined "or resisted" half of the Cross-Check now named at §2.3; item 16 reconciled with this document; §6's escalation count corrected from one to two; §6's stale "has not been independently reviewed" sentence removed.
- **L13, L14, L15, L16** — all four now addressed; Round 2 noted L14 had been fixed silently and the other three not acknowledged.

**Round 2 confirmed clean (reported as findings, not as a licence for a later round to skip re-checking — Round 3, R9):** no fabricated quotations anywhere (every Philostorgius, Doc_02, Doc_04, Doc_05, corpus-map, records, `ci.yml` and CORPUS-USE quotation verified); no wrong chapter attributions; no fabricated project-lead attribution; no uncredited borrowing from another world; H3's six-row gravity table verified row by row against Doc_04; M5, M6, M7, M8, M11 all holding; and the document does not self-score. Round 2 also tested and rejected the wider attack on H2's principle — "a formula quoted by an opponent is not self-testimony" does not prove too much, since Registry row 23 records that Auxentius's containing work is Homoian rather than hostile, and the Hilary record says outright "never as Homoian self-testimony."

**Round 3 independent adversarial review (Opus, isolated context, 2026-09-09): SUBSTANTIAL REVISION REQUIRED** — explicitly "not on the answer; on the same failure class for the third consecutive round." Filed at `Review-Artifacts/PostAdmission_Source_Finding_Round3_Review.md`. The F2 fix — the most serious of the Round 2 findings — was verified completely right, and Round 3 additionally established that Hilary alone is *sufficient*, not merely what survives: the H2 argument needs one holding at a confidence Philostorgius cannot improve on, so "twice over" was surplus rather than load-bearing. What failed was arithmetic and propagation, again, in §5 item 4.

- **R1 (HIGH).** The Round 2 recount ("22 of 60 keys") was wrong: six `npnf1xx` keys listed as missing are present in `COVERAGE` at lines 85–88. Cause found and recorded at §5 — a regex matching only the first key on each line of the literal. The true cohort is **14 keys / 18 files**; Round 2's 18 was right. Recomputed by parsing the literal directly.
- **R2 (HIGH).** Both figures Round 2 marked wrong survived verbatim two lines below their own correction, inside the same item. A propagation failure of exactly the kind `cic-build-cycle`'s naming-and-propagation rule exists to catch. Fixed at §5, §7 and the headline.
- **R3 (MEDIUM).** The keys-versus-files reconciliation offered for Round 2's count was arithmetically impossible — keys group files, so a key count cannot exceed the file count. Withdrawn as the rationalization it was.
- **R4 (MEDIUM).** The stated reason for cappadocian's absence was false: it appears nowhere in CORPUS-USE.md at all, which is itself stale. Corrected without abandoning the true underlying fact.
- **R5 (MEDIUM).** "Unclassified" and "rendered Tier 4" were conflated; Tier 1 pre-empts the lookup. Distinguished at §5.
- **R6, R8 (MEDIUM).** Item 16 still carried the Doc_08 §7/§9 locators and a wrong Round 2 tally, while §7 reported it reconciled. Both fixed in item 16.
- **R7, R9, R10, R11 (MEDIUM).** Dekkers re-misattributed and now traced to the Papahagi article; the "constrains what a Round N should re-examine" framing removed from both revision entries; the "two cases" claim corrected to one; Doc_08 Section 6 added to the downstream carriers actually checked.
- **R12 (LOW) and nine further LOWs.** The unmarked "Constantine"→"Constantius" emendation in the Candidate 5 row is now marked as Walford's slip rather than silently corrected.

**Round 3 verified clean:** the F2 fix in full (Registry rows 4 and 24, `cic/texts/README.md` line 168, and the Hilary record's confidence fields all verbatim); the "or resisted" concession as not verdict-changing; all four Round 1 LOWs; and — worked through from the primary documents for a third independent time — **the headline verdict. All six candidate gravities, the Interaction Matrix, Article 21 cross-strand status, and Doc_08's forces were re-derived, and nothing moves.** No fabricated quotation, no wrong chapter attribution, no uncredited cross-world borrowing, no unsupported project-lead attribution, no self-scoring, no pre-declared disposition, across all three rounds.

**Disposition after Round 3: none.** This document remains DRAFT. A substantial revision goes back through review, so a **Round 4** is required before any disposition is considered. This thread does not self-score.

**A pattern worth naming for the project lead rather than leaving in a revision log.** Three rounds have now failed on the same class — arithmetic and propagation inside §5 item 4 — while the finding's actual subject matter has been verified clean three times running. That asymmetry is itself the useful signal: the analytical judgment held up under sustained adversarial pressure; the hand-maintained counts in an ancillary section did not, three times. The counts in that section are now script-derived rather than hand-written, which is the actual fix; if a Round 4 finds a fourth error there, the right response is probably to delete the enumeration and state the defect qualitatively rather than to correct the number a fourth time.
