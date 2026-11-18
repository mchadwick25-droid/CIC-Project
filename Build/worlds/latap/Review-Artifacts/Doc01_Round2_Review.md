Simulated review — informational only, not an Article 31 substitute.

# Round 2 review of Doc_01 (latap)

- **Reviewer model:** claude-opus-5-5
- **Drafter model:** Sonnet 5.5
- **Reviewer agent:** independent-review session, fresh context (wrote none of the text under review)
- **Drafter agent:** Sonnet 5.5 library-stage worker
- **Round:** 2
- **Truncation check, method 1:** There are 10 `##` headings, numbered 1 to 10 in order (Formation World Identity through Disposition). The file has 222 lines. It ends on the complete sentence "Draft. It is not approved to proceed, and it is not frozen." followed by a newline.
- **Truncation check, method 2:** The working-tree file is 40,094 bytes. `git hash-object` gives `df1fa38c707170ab65838c05771c4efa06afd623`, which equals `git rev-parse HEAD:Build/worlds/latap/Doc_01_World_Identification_Boundaries_Orientation.md` at HEAD `637c383`.
- **Date:** 2026-10-29
- **Severity vocabulary:** P0 blocks, P1 must be fixed but is not disqualifying, P2 polish.

## Verdict

**Not clear.** P0: 0. P1: 1 (new). P2: 6, of which 2 are partly fixed Round 1 items and 4 are new.

All nine Round 1 P1 findings are fixed. Twelve of the fourteen P2s are fixed and two are partly fixed. The one open P1 is new and appears in the §6 table that was added in this revision: one cell cites Jerome for a claim Jerome does not make.

## Round 1 findings

**P1-1 (cited record files do not exist): Fixed.**
- `Build/worlds/latap/Source_Registry.md` now exists as a draft. Harnack's *Chronologie* II is row 47 and Monceaux I–III are rows 49–51.
- The `build/latap_Build_State.yaml` pointer is gone, and so is "in this pass" (grep finds neither).

**P1-2 (neighbour re-confirmation said to be logged, but logged nowhere): Fixed.** All the cited entries exist and say what the document says:
- `pahc/Open_Gaps_Tracking.md:888`, OG-44.
- `lpc/Open_Gaps_Tracking.md:2394`, OG-114.
- `ijc/Open_Gaps_Tracking.md:431`, entry 48.
- latap OG-10, titled "Neighbour re-confirmation of shared boundaries", which matches the subject cited in §9 item 12.

Each neighbour entry continues its ledger's numbering and states that no record is edited. Each was added in 637c383 as a request, not an edit to the neighbour's content.

**P1-3 (stale LPC distinctness claim): Fixed.** I re-checked each part of the §7 LPC bullet:
- `lpc.source.tertullian-de-pudicitia` carries `register: etic` and `evidentiary_weight: corroborating`.
- It is cited by exactly `lpc.force.decian-persecution-libelli-system` and `lpc.gravity.confessor-authority-vs-episcopal-peace`. The gravity's line 86 reads "Their claim was not new: Tertullian, in On Modesty, already tells of".
- `lpc.force.inherited-latin-theological-vocabulary:31` has "a Latin theological vocabulary that Tertullian is credited with forging".
- `lpc.source.monceaux-histoire-litteraire-tome1` exists.
- The question is carried at §9 item 11 and latap OG-11.

**P1-4 (*De mortibus* named once without the authorship dispute): Fixed.** §7 line 151 and line 160 both name Harnack for and Brandt against. Those are the only places the work is named.

**P1-5 (two different tags on the opening date): Fixed.** Line 31 now gives Dominant Modern Reconstruction, Step 0 §4 item 8's tag, "resting here on Harnack alone". The table row agrees.

**P1-6 (the Cyprian date had no named scholar): Fixed.**
- The row now gives Harnack's "end of 251 or start of 252" and Monceaux's "252 or 253".
- I confirmed Monceaux at `monceaux…tome2_1902.txt:15402–15403`: "écrit en 252 ou 253, pendant la grande peste de Garthage" (the OCR reads "Garthage").
- The row is marked as added from the vendored scholarship, not from Step 0.

**P1-7 (Tertullian's work count and share): Fixed.** I recomputed every figure:
- 731,618 − 32,001 = 699,617.
- 699,617 / 1,203,783 = 58.1%.
- 731,618 / 1,203,783 = 60.8%, so "about 61" is right.
- 187,134 / 1,203,783 = 15.5%, so "about 16" is right.
- The "second method 61.0 percent" sentence matches Round 1's own figure, 638,572 / 1,046,740 = 61.0%, and correctly applies to the thirty-two works. See N5 for its sourcing.
- The table now splits the thirty-one works from the *Appendix* ("none; pseudonymous verse").

**P1-8 (heresy treatises called the largest share of the corpus): Fixed.**
- 20,936 + 187,134 + 23,066 + 15,014 + 31,933 = 278,083, and 278,083 / 1,203,783 = 23.1%.
- The text now confines "largest" to within Tertullian's corpus.
- It states Lactantius's 285,187 as the larger shelf-wide block, and it discloses that the count includes the ANF apparatus and was made by one method.

**P1-9 (quotations without a `cic:` locus): Fixed.**
- "a disciple of Arnobius" is in `v.iii.lxxxii`.
- "his pupil Lactantius" is in `npnf206…:v.LXX`. The division id exists and the phrase is inside it.
- "Flourished 196?" is in `v.iii.lx`.

**P2-1 (rule letters mislabelled): Fixed.** Line 48 uses Step 0's (a), (b) and (c), and (c) now says "The NPNF gloss … The bracketed ANF04 note". §9 item 4 cites rule (a).

**P2-2 (wrong section for "best-anchored date"): Fixed.** It now cites §2 A5.

**P2-3 (opening boundary left out earlier works): Fixed.** *Ad Martyras*, *Ad Nationes* and Harnack's note on c. 195–197 are added.

**P2-4 (Carthage locus did not name Carthage): Fixed.** The text now cites Monceaux II line 15403, which names the plague at Carthage.

**P2-5 ("Almighty" attributed to Minucius): Fixed.**
- "the Almighty" is now Commodian's alone.
- Minucius's refusal of "Father" is quoted at `iv.iii.xviii`. The division exists and the sentence is in it.

**P2-6 (wrong chapter for the Spirit and the Virgin): Fixed.** The text now cites ch. XI and ch. XII separately.

**P2-7 (confidence vocabulary misattributed): Fixed.** Line 9 no longer attributes the five levels to Article 17 and spells the token "Inferential-Thin".

**P2-8 (§6 tagged no force): Fixed as to form.** Every cell now carries a tag. Three cell-level defects remain: N1 below, and the Cell 2A and Cell 3B tags in N4.

**P2-9 (*On the Vanity of Idols* called Cyprian's with no dispute): Partly fixed.**
- §4 Finding and the §7 LPC bullet now say "ascribed to Cyprian".
- Three places still say the two works are Cyprian's without qualification: line 89 ("Only two Cyprian treatises stand on this shelf"), line 152 ("the two Cyprian works that both shelves hold") and line 195 ("Cyprian's two works are on the shelf of another world").
- *Fix:* say "the two works ascribed to Cyprian", or "Cyprian's *Address* and the ascribed *On the Vanity of Idols*".

**P2-10 (process narration): Fixed.** `tools/check_live_commentary.py --surface worlds` now reports only PROTECTED lines for this file (4, 199, 210–217) and no REWRITE.

**P2-11 (Lactantius Article 4 result stated too strongly): Partly fixed.** The Book II passage is now disclosed, and the constituted-text reading is separated from the manuscript-only additions. The quotation checks out: ANF07 `iii.ii.ii`, under the heading "Chap. IX.—Of the devil, the world, God…", reads "Then He made another being, in whom the disposition of the divine origin did not remain". This is Brandt's II.8.4, per Step 0 §4 item 5. Two problems remain:
- **The passage is filed under the wrong clause.** Step 0 §2 A2 (line 38) ties it to Jerome's pneumatological charge ("precisely the binitarian-with-a-fallen-second-spirit structure the ancient charge concerns"), which is clause 5. Doc_01 files it under clause 2 only, and the clause 5 entry for Lactantius does not cross-refer to it.
- **The Result overstates.** It says "Lactantius affirms the first four", while clause 2 says whether the passage bears on that commitment "is not settled here". The Result should carry the same qualification.

**P2-12 (uncited census or builder claims): Fixed.**
- "transmitted alongside them on the census's account" is now attributed to the census.
- The acrostic verse is cited to `v.ii`; "acrostic" occurs in that division's opening.
- The Greek-element claim is now Harnack, printed p. 297. That page reads "die karthaginiensische Gemeinde anfangs ein nicht unbedeutendes griechisches Element enthalten hat", which supports it.
- The Lactantius continuation is tagged Inferential-Thin as the builder's reading.

**P2-13 (wrong heading reference for §8): Fixed.** It now cites "Step 0 §2 A2 and §4 item 3".

**P2-14 (speaker unclear): Fixed.** Caecilius makes the charge at ch. IX, and Octavius answers at ch. XXIX (`iv.iii.xxix` exists).

## New findings

### P1

**N1. §6 Cell 1B cites Jerome for Tertullian's rhetorical training, and Jerome does not say it.**
- *Where:* §6 table, Initiating/Internal: "his rhetorical training (…; the training rests on the census and Jerome)".
- *Evidence:* *De viris illustribus* 53 (`npnf203…:v.iii.lv`, notes removed) says Tertullian was from Carthage and "the son of a proconsul or Centurion, a man of keen and vigorous character". It says nothing of rhetorical or legal training.
  - §7 line 146 states the position correctly: "The census says Tertullian was trained as an advocate; Jerome calls Minucius an advocate."
  - Cell 1B turns that into Jerome supporting Tertullian's training. That is a source named for a claim it does not carry.
- *Fix:* rest the training on the census alone, as §7 does, and tag it accordingly, or cite a vendored source that actually says it.

### P2

**N2. The PAHC record set still says the *Apology* "opens" Latin defense. §7 repeats "need no change" without disclosing this.**
- `records/pahc/force/pahc.force.systematic-theological-mode-elsewhere.md:34` reads: "Tertullian wrote his Apology in 197 at Carthage. It opens a body of confident Latin defense."
- Step 0 §4 item 1, rule (a), rejects that framing because on pole A the *Octavius* comes first.
- Doc_01 §7 says "Step 0 found its records need no change". The re-run sweep (latap OG-12) reports only the `lucian-peregrinus` use, and PAHC OG-44 does not mention this record.
- Under CLAUDE.md this is "flag it, don't touch it": name it as a cross-world wording item in §7 or §9, and add it to the PAHC request.

**N3. The Passion's date is attributed to Harnack alone.**
- §2 Historical Pressures says "(Harnack: 7 March 202 or 203)".
- Step 0 §4 item 9 (line 199) says Harnack prefers 203. The "202 or 203" range is Step 0's combined reading of Wallis, Monceaux and Harnack, tagged Widely Accepted.
- *Fix:* cite Step 0 §4 item 9 for the range, or give Harnack's 203.

**N4. Two tagging slips in the §6 table.**
- **Cell 3B tags an absence.** "No internal fracture is attested as closing the world (Inferential-Thin)" puts a confidence level on an absent claim. CLAUDE.md says such an absence is an `absent_detail` or honest limit, not a rating. State it as an absence, consistent with §2's "Doc_08's Ending cell must say so".
- **Cell 2A has an untagged item.** "Persecution in waves" carries no tag of its own. The tags that follow attach to the plague and to the edicts.

**N5. The "61.0 percent" second-method figure has no source in the document.** The sentence is accurate, but the count exists only in `Review-Artifacts/Doc01_Round1_Review.md`. No Step 0 or Registry record holds it, and Step 0 B1 says no second run is claimed. Cite the review artifact as its source, or drop the sentence.

## Verified this round

- `python cic/engine/corpus_map_merge.py --check` exits 0.
- **The records/ search.** I re-ran the case-insensitive search for the eleven terms. It matches files in nine worlds (alx 7, cappadocian 3, desert 3, gallic 3, hal 5, ijc 14, lpc 20, pahc 23, witt 3) plus `records/worlds/`.
  - The matches I read in alx, desert and hal are volume-filename or tertullian.org strings.
  - cappadocian, gallic and witt return no context for the names, which is consistent with "perpetual". The sentence in the document is accurate.
- **PAHC uses of Tertullian.** Every one is of the *Apology* or *Against Marcion*. Apart from the two source records and `lucian-peregrinus`, they are `mutual-aid-prisoner` (Apology 39), `pliny-letters` (Tertullian's summary of the letter, as carried in Eusebius), `systematic-theological-mode-elsewhere`, `contested.rivals-undefeated` and `force.contemporary-rival-movements`. This supports "the same work PAHC already cites", subject to N2.
- **The *Octavius* counts, against the raw XML of `iv.iii`.**
  - The word "Christ" (not "Christian") occurs in the ch. XXXVII heading, once as span text and once in the `title` attribute, and in the Athenagoras footnote ("Legat. pro Christ").
  - "rucifi" occurs in the ch. IX heading (span and `title`) and in the ch. XXIX endnote "[A reverent allusion to the Crucified…]".
  - "Jesus" does not occur.
  - So the document's account is accurate: two and two, all four in apparatus, with both headings repeated in attributes.
- **§8 loci.** `iv.iii.ix`, `iv.iii.xviii`, `iv.iii.xxix`, `v.ii.xliii`, `v.ii.xxxiii`, `npnf206 v.LXX` and `v.LXXXIV` all exist.
- **Step 0 cross-references.** Step 0 dates the *Institutes* 304–311 at item 5. Its §4 item 8 table gives the break as 207/8 against 213, and line 197 tags the two works as pre-break, Widely Accepted among the three authors. Step 0 §4 item 1 gives the *Octavius* poles.
- **Harnack.** Printed p. 297 (Greek element) and the 311 toleration edict (file lines 4535–4548) are as cited.

## Not verified

- I did not confirm that Monceaux III supports "the toleration of 311" (§6 Cell 3A). Its 311 hits that I read concern events at Carthage; I found no passage on the edict of toleration. I did not confirm Monceaux III's treatment of the 303 edicts beyond the Cirta seizures (line 637).
- I did not open the census for "trained as an advocate".
- I did not re-open Harnack for the c. 317 Gaul arithmetic, the *Epitome* after 313, or the c. 190–195 conversion. These rest on Round 1's verification.
- I did not check the `Source_Registry.md` rows beyond their existence; that file is not under review.
- I did not re-check the unchanged quotations Round 1 verified.
- I consulted no post-1930 scholarship.
