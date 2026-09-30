Simulated review — informational only, not an Article 31 substitute.

# Doc_04 Candidate 5: targeted recheck of the six-test verdicts against the corrected premises (lpc)

- **Reviewer model:** claude-opus-5-5
- **Drafter model:** claude-sonnet-5-5
- **Reviewer agent:** independent-review subagent, fresh context, medium effort (wrote none of the text under review)
- **Drafter agent:** lpc build thread, change-order worker (commit d3bec0e96; trailer reads "Claude Sonnet 5.5"; Doc_04 itself was first drafted on Fable)
- **Round:** 1 (a targeted recheck of change order d3bec0e96 only; not a revision round and not a re-review of Doc_04)
- **Truncation check, method 1:** structural count. Doc_04 has all nine `## ` headings (§1 to §8 and Disposition) in order, all eight `### Candidate` headings, and exactly 48 six-test bullets (8 candidates × 6 tests); it ends on a complete sentence and a newline. The G5 record opens with `---`, has exactly two `---` front-matter fences, every YAML field through `classification: supporting`, and a closing body paragraph that ends on a complete sentence.
- **Truncation check, method 2:** byte and hash comparison against the committed blobs at HEAD d114068df. `wc -c` equals `git cat-file -s` (Doc_04 76,616 bytes; G5 record 7,225 bytes), and `git hash-object` equals `git rev-parse HEAD:<path>` for both (Doc_04 6fd146e8…, which is the post-image blob of d3bec0e96; record 91974832…). Neither file has uncommitted changes.
- **Date:** 2026-09-30
- **Documents:** `Build/worlds/lpc/Doc_04_Gravity_Discovery.md`; `records/lpc/gravity/lpc.gravity.conciliar-authority-theory.md`; downstream citations in Doc_05, Doc_07, Doc_08, `lpc_World_Profile.md`, `lpc_Gapped_Formation_Precedent.md`
- **Severity vocabulary:** P0 blocks, P1 must be fixed but is not disqualifying, P2 polish.

## Scope and yardstick

The question is only whether each verdict still follows from the corrected premises. The yardstick is CF V7.4 Part III's own test wording (document.xml paragraphs 289–306): Repetition, "Does it recur across evidence streams?"; Dependency, "Do other dimensions depend upon it?"; Formation, "Does it shape participants?"; Explanatory, "Does it help explain multiple aspects of the ecology?"; Persistence, "Does it remain visible across regions, communities, and evidence streams?"; Supporting, "organize significant portions of the ecology … pass multiple gravity tests but may not demonstrate the same breadth of dependency or persistence."

G5's classification (Supporting, on the project lead's ruling) is not in question and is not reopened here. `lpc_Gapped_Formation_Precedent.md` §4b was read. Nothing below is a new reading of the test language aimed at a cleaner pass. Every point comes from premises the change order itself put into Doc_04.

## Corrected premises, verified at source by structural marker

| Premise | Where verified | Result |
|---|---|---|
| Clergy and people present at the 256 council | ANF05 (row 4), `<div>` preface after the editor's note, file line 56854: "together with the presbyters and deacons, and a considerable part of the congregation who were also present". Latin, row 261 file, `div n="pr"` line 107–108: "praesentibus etiam plebis maxima / parte" (line-broken, so a one-line search misses it). The formula follows at line 140: "neque enim quisquam nostrum episcopum se episcoporum constituit". | Holds |
| Cyprian restates free judgment in Epistles LIV, LXXI, LXXV | ANF05 `div3 n="LIV"` (to Cornelius): each pastor rules his own portion of the flock "having to give account of his doing to the Lord"; the case is heard where the crime was committed. `n="LXXI"` (to Stephen): "each prelate has in the administration of the Church the exercise of his will free". `n="LXXV"` (to Magnus), §17: "prescribing to no one, so as to prevent any prelate from determining what he thinks right". | Holds |
| Firmilian contests Stephen | ANF05 `div3 n="LXXIV"`, §17: Stephen "so boasts of the place of his episcopate, and contends that he holds the succession from Peter"; later, "he is really the schismatic". The same letter reports Eastern councils at Iconium (§7, §19). | Holds. It is a second voice on the Cyprian pole, and Iconium is a third region. |
| Augustine appeals to plenary Councils in Letters XLIII and LIV | npnf101 `div3 n="XLIII"`: "there still remained a plenary Council of the universal Church". `n="LIV"` (to Januarius): observances held "either by the apostles themselves, or by plenary Councils, whose authority in the Church is most useful", e.g. the annual feasts of the Passion, Resurrection, Ascension and Pentecost. | Holds. LIV applies the theory to the church's shared calendar. |
| *Psalmus contra partem Donati* written for the common people and putting the judging question to them | Row 214 file, Petschenig's praefatio (line ~239): "ut Donatistarum causa ad notitiam etiam indoctorum hominum atque infimi uulgi perueniret". The Psalm, from line 1296: "non iudices consederunt, non sacerdotes de more, / quo solent in magnis causis congregati iudicare"; "proferantur … gesta, quae in concilio solent esse"; "iudices transmarinos petiit". | Holds |
| *En. in Ps.* 36, sermo 2, on who judges a bishop | Migne PL 36–37 file, `SERMO II` at line 27088. Around line 27918 it runs the Caecilian/Primian/Maximian judgments together: "Valeat et in te, quod MaximianLlse * judi-" (OCR as printed), "episcopi illum damnaverunt". | Holds |
| "bishop of bishops" in the sermons only of Christ | `augustine_sermones-guelferbytani-lat_morin1917.txt` line 9557: "Dominus et episcopus episcoporum"; the index at line 14856 reads "episcopus episcoporum, Christus 32". | Holds |
| G7: Cyprian states the theme | `cyprian_ad-donatum…` line 256: "Dei est, inquam, Dei omne, quod possumus". `cyprian_testimoniorum…` line 3300: "IIII. In nullo gloriandum, quando nostrum nihil sit." | Holds. **Also found:** Augustine cites *Ad Quirinum* III.4 against the Pelagians at least five times in row 23 itself (npnf105 lines 18089, 20912, 20975, 22251, 22373). Line 18089 says Pelagius "wishes himself to appear as his imitator". |

## Verdict tables

**(a)** still follows · **(b)** follows, but the wording overstates or understates · **(c)** no longer follows

### Candidate 5

| Test | Current text (Doc_04) | Corrected premise | Grade | Honest verdict / minimal true wording | Moves classification? |
|---|---|---|---|---|---|
| Repetition | l.90: "Passes narrowly and locally. … Each theory therefore recurs in more than one text of its own author, and each still comes from one bishop's own voice." | The theory recurs across four Registry rows (1, 4, 11, 13), in three genres (conciliar acta, letters, treatise), in both phases. Firmilian (row 1) is a second voice on the Cyprian pole. | **(c)** | "Locally" rested on the withdrawn single-locus premise. "Each still comes from one bishop's own voice" is contradicted by Doc_04's own l.92 and l.94, which name Firmilian. On the Framework's test ("across evidence streams"), and on Doc_04's own scale (C6 "passes strongly" on rows 1, 4 and 13), the honest verdict is **Passes**. It could carry an Author Gravity qualifier: "each pole is voiced chiefly by its own bishop; Firmilian (Epistle LXXIV) also contests Stephen". | No. Supporting still fits, and Primary stays barred by Formation and Dependency. It is still a verdict change, which is outside a wording-only change order. **Project lead to decide.** |
| Dependency | l.91: "Passes narrowly. … No candidate below depends on this axis resolving one way or the other." | The change order did not touch this test's premises. | **(a)** | Stands. | No |
| Formation | l.92: "Does not clearly pass. Awareness of the question is attested. … What this document does not find is evidence that … were formed by this specific theoretical question as a teaching." | Awareness is attested (256 plebs; the Psalmus). No source shows formation. | **(a)** | Follows. P2 below notes that the Framework's "participants" also covers bishops, and the 256 procedure shows the formula governing 87 bishops' sententiae. "Does not clearly pass" allows for that. | No |
| Explanatory | l.93: "Passes narrowly. Explains the specific shape of the Cyprian/Stephen rebaptism dispute and of Augustine's own extended argument against Cyprian's ruling, but does not explain multiple, independent aspects of the wider ecology the way Candidates 1–3 and 6 do." | Letter LIV uses plenary-council authority to explain why the church's universal observances bind. Letter XLIII uses it to frame the Caecilian case. | **(b)** | "Passes narrowly" can stand. The clause "does not explain multiple, independent aspects" is now contradicted. Minimal true wording: "Passes narrowly. Explains the shape of the Cyprian/Stephen dispute and Augustine's argument against Cyprian's ruling. In Augustine's letters it also explains how the Caecilian case was framed (Letter XLIII) and why universal observances bind (Letter LIV). It does not explain the ecology's pastoral and sacramental core the way Candidates 1–3 and 6 do." | No |
| Persistence | l.94: "Does not pass at the world level, on a disclosed search bound rather than an unqualified absence. … This document has found no evidence that it was operative in ordinary congregational formation." | Visible in both phases; in three regions (Africa, Rome, Cappadocia/Iconium); across four rows; before clergy and people at Carthage in 256. | **(c)** as written | The only remaining ground, "operative in ordinary congregational formation", is the Formation test's criterion, not Persistence's. C6 passes Persistence on the same two-phase shape (l.115). Two honest options: **(i)** "Passes narrowly: visible in both phases, three regions and four evidence streams; among communities, chiefly in episcopal councils and correspondence, with congregations present only at the 256 council"; or **(ii)** keep "does not pass", but ground it on the Framework's "communities" limb, stated as such. Reviewer's recommendation: (i). It matches C6, and the premises force it; it is not a reading of the test language chosen to pass more cleanly. | No: under (i) or (ii), Supporting holds and Primary stays barred. Under (i), though, Supporting is reached on six-test evidence, which bears on l.101 ("Alone among the eight candidates, this line does not record this document's own verdict") and on §7 item 8. **Project lead to decide.** |
| Overall reading | l.99: "This candidate's six-test profile is narrow: narrow passes on Repetition, …; Persistence does not pass at world level." §4 l.159 and §5 l.186 restate it. The classification line is l.101. | As above | **(b)** | The lines follow §3 faithfully, so they inherit §3's Repetition and Persistence defects. "Whether the candidate 'organize[s] significant portions of the ecology' is neither established nor refuted" still follows. The classification line (Supporting, on the ruling) is untouched. These lines should be re-derived from whatever the lead decides on Repetition and Persistence. | No |

### Candidate 7, Persistence

| Current text | Corrected premise | Grade | Minimal true wording | Moves classification? |
|---|---|---|---|---|
| l.132: "Fails to pass at the world level (Cyprian states the theme, at *Ad Donatum* 4 … and in the chapter list of *Ad Quirinum* III.4 … but no Cyprian-phase controversy or body of work is built on it) but passes strongly *within* Augustine's own phase". §5 l.169: "Candidate 7 fails Persistence at world level *because it is confined to one phase* — Cyprian states the theme but …" | The theme is visible in Cyprian's phase. Augustine carries it across the gap himself, citing *Ad Quirinum* III.4 in row 23. | **(b)** | The verdict follows only if Persistence is read as persistence *as an organizing force*. Doc_04 reads it that way elsewhere (C2, C8), so say so. l.132: "Does not pass at world level as an organizing force: Cyprian states the theme (…), and Augustine cites him for it against the Pelagians, but no Cyprian-phase controversy or body of work is built on it; passes strongly within Augustine's phase." l.169: replace "because it is confined to one phase" with "because it organizes only one phase". §4 l.160: "Augustine-phase-bound as an organizing gravity". The World Profile (G7 entry) and the grace record (l.63–66) already use this wording, so Doc_04 now lags its own derivatives. | No. Supporting holds, on Dependency and Explanatory. |

### Candidate 6, Repetition

| Current text | Corrected premise | Grade | Minimal true wording | Moves classification? |
|---|---|---|---|---|
| l.111: "Passes strongly. Recurs in … (Row 1), … (Row 4), and *On Baptism* in full (Row 13 …). Argued across two bishops' own extended treatments, decades apart." | The contrast with C5 is gone. The 256 council records 87 bishops' judgments, and Firmilian also argues the point. | **(b)** | "Passes strongly" follows. "Decades apart" understates Doc_04's own "over a century", and "two bishops" understates. Minimal wording: "Argued at length by both anchor bishops, over a century apart, and in Cyprian's phase by the 87 bishops of the 256 council." | No |

## Findings

**P0-1. Doc_04 §5, l.173: the reopening-trigger finding rests on a premise the change order made false.** The text reads: "This document surfaces no such evidence: it re-weighs Doc_01 §4's two quotations — the 256 preface and *On Baptism*'s 'authority of plenary Councils' — and adds nothing to them." After d3bec0e96, §3 C5 adds Epistles LIV, LXXI and LXXV, Firmilian's LXXIV, Letters XLIII and LIV, the 256 attendance clause, the *Psalmus* and *En. in Ps.* 36. Doc_01 mentions none of them on this axis (Doc_01 l.152 names Firmilian only as a correspondent). Doc_01 §8 item 10 (l.180) reopens the strand-singular finding if Doc_04 "surfaces evidence this document has not weighed". On its literal terms, that condition now reads as met. Wording cannot fix this, because the conclusion ("trigger is not met") depends on the false sentence. **This is for the project lead** (Article 21 / governance). The reviewer's reading, offered without deciding it: the new evidence shows bishops of one communion disagreeing inside communion, which is G3's own shape. It does not show two formation communities, so a reopening would likely reaffirm strand-singular status. Whether to reopen and reaffirm, or to record why the trigger's condition is not engaged, is the lead's call.

**P1-1. Doc_04 l.90, Repetition: "narrowly and locally" no longer follows (c).** Project-lead decision (verdict change), as tabled above.

**P1-2. Doc_04 l.94, Persistence: the stated ground is the Formation criterion (c).** Project-lead decision between options (i) and (ii), as tabled above. Classification is not moved either way.

**P1-3. Doc_04 l.93, Explanatory: "does not explain multiple, independent aspects" is contradicted by Letter LIV (b).** Minimal wording tabled above.

**P1-4. "One bishop's own voice" is contradicted by Doc_04's own l.92 and l.94 (Firmilian).** It appears at Doc_04 l.14 ("Candidate 5, whose two poles are each drawn from one bishop's own voice"), l.86 (Author Gravity flag), l.90, and the G5 record l.62 ("Each theory comes from one bishop's own voice"). True wording: "each pole is voiced chiefly by its own bishop; in Cyprian's phase Firmilian (Epistle LXXIV) also contests Stephen."

**P1-5. G7: Doc_04 l.132, l.169 and l.160 overstate phase-confinement (b).** Wording tabled above. §5 l.169 is internally inconsistent as it stands: "confined to one phase — Cyprian states the theme".

**P1-6. G5 record l.69: "It explains nothing else in the wider world."** This is stronger than Doc_04 itself, and Letter LIV contradicts it. It should follow whatever Doc_04 l.93 becomes.

**P1-7. Doc_07 l.202 restates the withdrawn "only between two bishops" premise.** The text says G5 is "two men … answering a question neither posed to the other, whose disagreement becomes consequential only because a third party cited the first against the second." In Cyprian's phase the question was already consequential, argued among Cyprian, Stephen and Firmilian and before the 256 assembly. True wording: "…whose two formulas meet only because a third party cited the first against the second; in Cyprian's own time the question was already contested among several bishops."

**P1-8. `lpc_Gapped_Formation_Precedent.md` l.33 restates the false premise:** "Candidate 5 (conciliar authority) structurally needed the gap bridged. One attested locus in each phase, a century apart." This document was received from the project lead, and its ruling adopts §3, not §4. Its §4 narrative now misdescribes C5, because C5 is attested independently on both sides and needs no bridge. **Flag for the project lead; not a build-thread edit.**

**P2-1. Doc_04 l.111 (C6 Repetition):** "decades apart" and "two bishops", as tabled above.

**P2-2. Doc_07 l.234:** the *Gesta* is "the most obvious place in this corpus where inter-episcopal authority structure would be visible among clergy other than the two anchor figures". Rows 1 and 4 already show it among other bishops (Stephen, Firmilian, the 87). Suggested wording: "…the most obvious place in this corpus for its visibility in Augustine's phase beyond Augustine himself."

**P2-3. G5 record l.96–97:** "The 411 Gesta … remain unread and have not reopened the question. It remains open." Doc_04 §7 item 6 closes it "as a persistence question" and says it is "no longer carried as an open question about Candidate 5's persistence". The record should say the question is closed, as Doc_04 does.

**P2-4. G5 record l.117 (body after front matter):** "Re-derived from the approved Doc_04 §3 … See this script's own docstring, 'G5'S OWN JUDGMENT CALL,' …" This is process narration in a canonical `records/` file (CLAUDE.md, "Keep the live/canonical surfaces clean"). Doc-hygiene on another thread's content, so flagged, not touched.

**P2-5. Formation (a), scope note.** CF V7.4 asks whether a gravity shapes "participants". Doc_04 l.92 narrows this to ordinary believers, catechumens and most clergy. The 256 procedure (each bishop giving his own sententia under the formula) shows the formula shaping bishops' practice. "Does not clearly pass" allows for this, so no change is needed, but the scope could be stated.

**P2-6. Doc_04 l.131 (G7 Explanatory):** "no Pelagian-anthropology-equivalent material is identified anywhere in Cyprian's own corpus" is true only in the sense of no rival anthropology. Now that l.132 says Cyprian states the theme, it can read as a contradiction. Suggested: "no controversy equivalent to the Pelagian one is identified in Cyprian's corpus".

## Downstream sweep (sentences citing G5 verdicts)

- **Doc_05** l.175, l.257, l.303, l.317: already corrected to "awareness attested, formation not shown". No old premise restated. l.175 cites Doc_04 as finding "no evidence in Doc_02", a phrase Doc_04 l.92 no longer uses. That is harmless.
- **Doc_07** l.88, l.94, l.186: consistent. **l.202: P1-7. l.234: P2-2.**
- **Doc_08** l.79, l.135, l.330: consistent (l.330 already carries the corrected 1B-1 wording). l.344 carries "thin across the span" from Doc_04 §5. It is consistent now, but follows any Persistence decision.
- **World Profile** l.122 ("Persistence fails at world level") and l.126 carry Doc_04 faithfully and follow any decision. l.128 and l.242: consistent. The G7 entry is already correct.
- **G5 record:** P1-4, P1-6, P2-3, P2-4. The rest of the body matches Doc_04 as it now reads.

## G5 record confidence (Inferential-Thin) against Doc_04 §4

Consistent. Doc_04 §4 (l.159) records a divergence: "both formulas' existence Documented; organizing breadth not comparably supported, flagged not upgraded". It assigns no five-level tier to organizing breadth, so the record's choice of Inferential-Thin for that claim does not contradict it. Under CF V7.4 ¶309, a thin evidential tier on a Supporting gravity raises no Primary bar. The record's divergence_note (l.15–23) cites "six-test profile being narrow throughout and Persistence failing at world level". That is accurate to Doc_04 as written, but it must follow any change the lead makes under P1-1 or P1-2. Even under option (i), the claim that the axis *organizes* stays inferential (Formation does not clearly pass), so the tier itself would not need to move.

## For the project lead

1. **P0-1:** Doc_01 §8 item 10's reopening condition now reads as met on its own terms. Decide whether to reopen and reaffirm strand-singular status, or to record why the new evidence does not engage the trigger. Doc_04 l.173 cannot stand as written either way.
2. **P1-1 and P1-2:** decide whether to authorize verdict-level corrections beyond the wording-only change order: Repetition to "Passes", and Persistence to option (i) or (ii). **No answer here moves G5's classification.** If (i) is chosen, decide also whether Doc_04 then records Supporting as its own six-test verdict (l.101, §7 item 8), given precedent §4b.
3. **P1-8:** the precedent document's §4 restates the false single-locus premise.

## Bottom line

Of the eight verdict texts rechecked, two still follow (G5 Dependency, G5 Formation; G5's classification line itself is untouched). Four follow but misstate (G5 Explanatory, the G5 overall-profile lines, G7 Persistence, C6 Repetition). Two no longer follow (G5 Repetition, G5 Persistence). No classification moves. The change order is **not clean as "no verdict changed"**. Doc_04 §5 l.173 is a P0 because it now contradicts §3 on the point that decides Doc_01's reopening trigger.
