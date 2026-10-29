Simulated review — informational only, not an Article 31 substitute.

Reviewer model: claude-opus-5-5
Drafter model: Sonnet 5.5
Reviewer agent: a39d62e79285ad3b3
Drafter agent: not recorded in the build state (`build/aec_Build_State.yaml` names the drafter model only)
Round: 4
Truncation check, method 1: full read of `Doc_01_World_Identification_Boundaries_Orientation.md` (118 lines, matching `wc -l`; all eight `## ` sections present, §1 to §8, ending in the §8 Disposition)
Truncation check, method 2: byte and tail check: `wc -c` gives 31,767 bytes; `tail -c` shows the file ending on the §8 line "Held pending the project lead's confirmation of the World #8 boundary question, matching Step 0's status."; sha256 `cdd02a94…137314` at `origin/main` `5136d7f58`

# Review of Doc_01 — World Identification, Boundaries, and Orientation (`aec`): cap-ruling targeted recheck

**Authority.** Mark ruled on 2026-10-29 that Step 0, Doc_01 and Doc_02 had each used the three-round cap without clearing, and ordered one more targeted Opus review of Doc_01 and Doc_02. This review is that one. **Under that ruling it does not count toward the three-round cap.** If it does not clear, the result goes back to Mark with the open findings. No further rounds run on the build thread's own initiative.

**Gate note.** The `roundcount` gate excuses a review file only when a System Hub Decision Log entry headed "Cap ruling" names it. No such entry for `aec` exists in `Build/Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md` at `origin/main` `5136d7f58`. Until one names this file, the gate will count it.

**Scope and method.** This is a targeted recheck, not a fresh full review. It takes each Doc_01 finding left open by Round 3 (`Doc01_Round3_Review.md`), checks it against the current text, and then checks what changed after Round 3. Every quotation, and every claim about what a vendored file holds, was re-read in `cic/texts/` directly, with XML tags stripped and endnotes set aside. No drafter claim of "verified" was relied on. Counts were re-run independently. I did not edit the document.

---

## Round 3 findings: status

| Round 3 finding | Status | Evidence |
|---|---|---|
| H1. The Theodoret strand question was closed in §4 but still deferred to Doc_04 in §4's "Governing consequence", §7 items 2 and 6, and §5 Cell 3B | **Closed** | All four places now say the strand and inclusion question is closed by §4. Only the narrower *Ecclesiastical History* gravity question and the edge-of-window fit stay open for Doc_04. |
| H2. The "one consistent criterion" rested on a false premise that all of Theodoret's Letters are 440s material | **Closed in substance**; one example is wrong (new finding N2) | §4 now splits the Letters by subject. The 430–431 run is real: `npnf203` `iv.x.cli` (Letter CL to John of Antioch, dated February 431 in the note), `iv.x.clxiii` (to Andreas, from Ephesus, July–August 431), `iv.x.clxiv` (the Commissioners, September 431), `iv.x.clxvii` (the Commissioners' petition from Chalcedon). |
| M1. "A jurisdictional and personal dispute, not a doctrinal one" was unsourced and wrong against Socrates II.44 | **Closed** | §5 now quotes Socrates exactly: "because Meletius had been ordained by the Arians, and his adherents had been baptized by them" (`npnf202` `ii.v.xliv-p3`, verbatim). The quotation just before it in the same paragraph has a separate problem (new finding N1). |
| M2. "The third city… by standard reckoning" left unqualified | **Closed** | §2 now reads "ranked third behind Rome and Alexandria on an older reckoning", with Constantinople's overtaking marked Widely Accepted. |
| M3. The fellow-students sentence cited the NPNF endnote (`ii.ix.iv-p6`), not Socrates' text (`ii.ix.iv-p2`) | **Closed** | §2 cites `ii.ix.iv-p2`. The words "entered upon the ascetic life, under the guidance of Diodorus" are in Socrates' body text there, verbatim. |
| L1(a). Diodore stated as Chrysostom's teacher as settled fact | **Closed** | §2, §5 and §6 all hold the link at Widely Accepted and not re-verified for Chrysostom by name. |
| L1(b). §6's "consensus… taken for granted" against §5's Anomoean correction | **Closed** | §6 now narrows the inheritance to the *homoousion* question and points to §5 for the live Anomoean phase. |
| L1(c). The Counter-statements' edge-case status credited to "subject-matter grounds too" | **Closed** | §4 now says both pass the subject test and that the edge case comes from the condemnation and the composition date. |
| L1(d). The Template's Boundary Check quote joined two sentences with an ellipsis and altered the wording | **Closed** | §4 now quotes the two passages separately. Both match `Source_Registry_Template.md` line 50 verbatim. |
| Narration clean-up (required before any disposition) | **Closed** | No correction narration remains in the body. `tools/check_live_commentary.py --surface worlds` flags only protected status, date and route-cue lines. |

## Verified at source this round (holds)

- §2, Socrates VI.3 (`npnf202` `ii.ix.iv-p2`): "John was a native of Antioch in Syria-Cœle, son of Secundus and Anthusa, and scion of a noble family in that country. He studied rhetoric under Libanius the sophist, and philosophy under Andragathius the philosopher." Verbatim.
- §2, the Socrates account of Chrysostom's career, same paragraph: made reader, then deacon by Meletius; on Meletius's death he "separated himself from the Meletians, without entering into communion with Paulinus, and spent three whole years in retirement"; ordained presbyter "by Evagrius the successor of Paulinus". Matches the document's summary.
- §2, the alternative account (`npnf109` `iii.vi-p2`): "ordained deacon by Meletius in 380 or 381, and a few years afterwards presbyter by Flavian (386)". Verbatim.
- §2, Ammianus Book XXII (`ammianus-marcellinus_roman-history_yonge1862.txt`): the order to shut "the chief church of Antioch" is at lines 16184–16188; the *Misopogon* at lines 16236–16237.
- §4, the Boundary Check quotations: verbatim, `Source_Registry_Template.md` line 50.
- §5, the homily "Concerning the Equality of the Divine Father and the Son" (`npnf109` div1 `xii`), with the editor's note tying it to the Anomoean homilies. It supports the claim as worded.
- §1 and §6, the `lpc` contrast: the current `Build/worlds/lpc/Doc_04_Gravity_Discovery.md` still classifies Candidates 1, 2, 3 and 6 Primary and Candidate 4 (Preaching and Catechesis) Supporting.
- §6, the Mingana 1932 rights note: a 1932 publication enters the US public domain on 1 January 2028. Correct.

---

## New findings

### N1. Blocking (substantial). §5: a Socrates quotation is joined across two sentences and cited for a period it does not describe.

**Location.** §5, "What larger world was it embedded in", first sentence: "…the settled post-381 Nicene-Constantinopolitan consensus among the Antiochene church's own rival Meletian and Paulinian factions alike, in the narrow sense that both claimants' own confessed faith exactly corresponded by the time of that consensus (Socrates, `…:ii.v.xliv`: "those who originally embraced the *homoousian* opinion... views on matters of faith exactly corresponded")."

**Evidence.** `npnf202` `ii.v.xliv-p3` reads: "nevertheless, those who originally embraced the homoousian opinion would not communicate with them, because Meletius had been ordained by the Arians, and his adherents had been baptized by them. Thus was the Antiochian church divided, even in regard to those whose views on matters of faith exactly corresponded."

**What is wrong.**
- The ellipsis runs across a sentence boundary. It joins the subject of one sentence to the predicate of the next, which is the pattern Round 3 L1(d) already found in this document.
- The passage describes Meletius's installation and exile under Constantius, about 361. It says nothing about the period after 381, and it comes before Paulinus was consecrated (362, per §2 of the same document). So it cannot show that "both claimants'" faith corresponded "by the time of that consensus".

The doctrinal agreement after 381 may well be right. But this citation does not support it as worded, and the quotation reads as one sentence the source does not contain.

**Required.** Either cite a source that speaks to the period after 381, or restate the claim as what Socrates says: the parties were divided about 361 although their faith agreed. Quote whole sentences, or mark the break.

### N2. Blocking (substantial). §4: a letter is called "independently verified present" in the vendored file, but only its title is there.

**Location.** §4, the Letters paragraph: "(e.g. John of Antioch's own letter to Nestorius, `iv.x.cl`; … all independently verified present in the vendored file)".

**Evidence.** In `npnf203_theodoret-jerome-gennadius-rufinus.xml`, the `div3` with `id="iv.x.cl"` (lines 36058–36075) holds only the italic line "CXLIX is 'Copy of the Letter written by John, Bishop of Antioch, to Nestorius.'", one sentence saying the letter "has sometimes been supposed to have been really composed by Theodoret", and a note. The letter's text is not printed. The next division, `iv.x.cli`, is Theodoret's own Letter CL to John of Antioch on Cyril's anathemas, dated February 431 in its note.

**Why it matters.** The conclusion, that there is a run of 430–431 Nestorian-controversy letters, still holds. But the document asserts that it verified a specific text in the file, and that text is absent. Under CLAUDE.md's source-fidelity rule, a false claim about what a source contains is not cosmetic. The same claim is repeated in Doc_02 §1 and Source Registry row 11a.

**Required.** Replace the example with `iv.x.cli` (Letter CL, to John of Antioch, February 431), or say that the John-to-Nestorius letter appears only by title.

### N3. Blocking (substantial). §4: Constantinople II canon XIII does not separate the Counter-statements from the anti-Ephesus letters the way the document says.

**Location.** §4, second bullet: "The Counter-statements are confirmed condemned material at the Second Council of Constantinople (553), by name … the Letters' own Nestorian-controversy correspondence is not itself named at that council, but shares its subject and date." The same split drives Source Registry row 11a, whose condemned-content disclosure is limited to the Counter-statements.

**Evidence.** `npnf214` `xii.vii-p36` (Capitula, XIII) names no work by title. It anathematises anyone who defends "the impious writings of Theodoret, directed against the true faith and against the first holy Synod of Ephesus and against St. Cyril and his XII. Anathemas, and [defends] that which he has written in defence of the impious Theodore and Nestorius". The letters this document places in the 430–431 run include Theodoret's letter from Ephesus attacking that synod's proceedings (`iv.x.clxiii`: "Indeed what farce-writer ever performed such a play?") and his letter to Nestorius refusing to assent "to what has been done unjustly and illegally against your holiness" (`iv.x.clxxiii`). Both fall inside the canon's description just as the Counter-statements do.

**Why it matters.** This is a disclosure obligation on condemned material. "By name" against "not named" draws a line the canon does not draw. As written, the condemned-content warning would not travel with letters the canon's own wording covers.

**Required.** State that canon XIII condemns by description, not by title, and that its description reaches Theodoret's writings against Ephesus 431 and in defence of Nestorius as well as those against Cyril's anathemas. Extend the disclosure to the 430–431 letters, or say plainly which of them the description reaches and why. The same wording sits in Step 0 §2 (A1). Step 0 is outside this review, so this is noted, not judged.

### N4. Blocking (substantial). §4 and §6: the boundary finding does not reach Antiochene-party works the world's corpus-map bucket now carries as this world's own `tradition`.

**Location.** §4, which states that whether carried material "is [inside this world's boundary] at all is Doc_01's own job"; and §6, which places the Theodore and Nestorius trajectory "mostly outside this world's own 430 close" and says that continuation is not this document's to reconstruct.

**Evidence.** `cic/corpus-map/antiochene-exegetical-christianity-chrysostom-ce.yaml` at `origin/main` `5136d7f58` now carries, among other new rows, these as `role: tradition`, `confidence: provisional`:
- Nestorius, *The Bazaar of Heracleides* (Driver and Hodgson 1925), whose own corpus-map note says it was "written in exile in the 440s";
- Nestorius, *Le livre d'Héraclide de Damas* (Nau 1910);
- Loofs, *Nestoriana* (1905);
- the Acts of the Antiochene counter-council at Ephesus, 431 (Mansi tom. 5);
- the *Synodicon adversus tragoediam Irenaei*, the Antiochene party's letters of 431–435 (Mansi tom. 5).

None of these is weighed by §4's per-work test, which covers only Theodoret's four works. On §4's own subject-and-date reasoning, the *Bazaar* (written in the 440s) stands where the *Eranistes* stands, and the 431–435 Antiochene-party acts and letters stand where the Counter-statements stand.

**Why it matters.** The world's boundary is Doc_01's to set. The bucket now treats as this world's own voice material that Doc_01 either places outside the window or has not considered. This is a scope-boundary conflict between Doc_01 and the corpus-map, not a "could be stronger" note. The shallow checkout cannot date when the rows arrived. Several are tagged "Shared-Events Era 2 batch (Ephesus 431)" in their notes, which suggests they came after the 2026-10-02 filing. Either way, the conflict is open now. The Registry side is Doc_02 finding D1.

**Required.** Extend §4's per-work boundary finding to the Antiochene-party `tradition` rows: Nestorius ×3, the Conciliabulum and the Synodicon. Alternatively, record that the corpus-map placement conflicts with Doc_01 and route it to the Library thread or the project lead. The rows themselves are a corpus-map matter, not this document's to edit.

### N5. Non-blocking (cosmetic). §1: the exact word counts no longer reproduce.

**Location.** §1, Core Identity: "`wc -w` gives 3,339,085 under the `POSIX` locale and 3,357,623 under `C.UTF-8`; a whitespace split in Python 3 with XML tags stripped gives 3,035,294".

**Evidence.** Re-run on the six files `npnf109`–`npnf114` at `origin/main` `5136d7f58`, two ways. `LC_ALL=POSIX wc -w` gives 3,332,586, and `LC_ALL=C.UTF-8 wc -w` gives 3,351,124. A Python 3 whitespace split, after replacing tags with spaces, gives 3,032,271. The files were changed by the CCEL header clean-up (PR #1179, 2026-10-26, with a follow-up on 2026-10-27). "About 3.34 million" is still roughly right at 3.33–3.35 million, so no claim changes. The exact figures need re-running and dating.

---

## Verdict

**Doc_01: did not clear. Not Approved to proceed.**

All ten Round 3 items are closed. Four new findings are blocking (substantial): N1, N2, N3 and N4. One is cosmetic: N5, which can be applied directly without a further review. Under Mark's ruling of 2026-10-29, no further round runs on the build thread's own initiative. The four open findings go back to Mark.

Open findings for Mark, exactly:

1. **N1.** §5: the Socrates II.44 quotation is joined across a sentence boundary and cited for an agreement after 381 among "both claimants". The passage describes about 361, before Paulinus was consecrated.
2. **N2.** §4: "John of Antioch's own letter to Nestorius, `iv.x.cl` … independently verified present". Only the letter's title is in the file. The working example is `iv.x.cli`.
3. **N3.** §4: Constantinople II canon XIII condemns by description, not by name. Its description reaches Theodoret's anti-Ephesus and pro-Nestorius letters as well as the Counter-statements, so the "by name" against "not named" split, and the disclosure limited to the Counter-statements, are wrong.
4. **N4.** §4 and §6: the boundary finding does not cover the Antiochene-party `tradition` rows now on the world's corpus-map bucket: Nestorius's *Bazaar* (written in the 440s), the Nau *Livre d'Héraclide*, Loofs's *Nestoriana*, the Conciliabulum Ephesinum (431) and the Synodicon (431–435).
