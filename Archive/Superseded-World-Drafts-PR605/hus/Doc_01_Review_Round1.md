# Doc_01 Review — Round 1
## The Hussite and Bohemian Brethren Movement — World Identification, Boundaries, and Orientation

**Document reviewed:** `Doc_01_World_Identification_Boundaries_Orientation.md` (DRAFT)
**Checked against:** `Step0_Movement_Scope_Confirmation.md` (Revision 3, Approved to proceed), `Step0_Review_Round3.md`, `worlds/_cross-world/dossiers/the-hussite-and-bohemian-brethren-movement_Source_Readiness_Dossier.md`, `cic-website/data/world-census.json` (entries V.6, V.11, VI.24), `reference/L4-Templates/[world-code]_Forces_Document.md` (Layer definitions), and the vendored files in `cic/texts/`: `hus_letters_workman-pope1904.txt`, `hus_de-ecclesia-the-church_schaff1915.txt`, `lutzow_bohemia-historical-sketch_1920.txt`, `gillett_life-and-times-of-huss-v2_1871.txt`, `lutzow_hussite-wars_1914.txt`.
**Review type:** Independent adversarial review, Round 1, full review.
**Date:** 2026-09-25.

---

## Verdict

**NOT CLEARED — revise and return for a Round 2 targeted recheck.**

The window is stated correctly and consistently as c. 1402–1517 throughout. The Lollardy relationship is engaged honestly. The dossier's staleness is flagged, not silently resolved. The Unity-of-the-Brethren strand is argued from simultaneity, not sequence.

Five substantial findings still block clearance. Two are factual errors: the direction of the Wyche letter is reversed, and the Compactata are called "papal-recognized." One misreads the census's own status for Taborite Radicalism, and the whole §4.2 scoping rationale rests on that misreading. One puts a construction decision into a Layer-1 forces cell. One overstates a hedged secondary source in the Strand B evidence. Seven minor findings follow.

---

## Findings by severity

### Substantial (blocking)

**S1. §4.2 misreads the census status of Taborite Radicalism (V.11). The scoping rationale rests on that misreading.**
§4.2 says the census has "already registered it as a separate, independently-built world (its own Atlas ID, its own window, its own dedicated primary-source track)." §7 item 8 repeats that it is "census-registered as its own world." §9 item 4 says it has a "separate, already-registered world-build track."

The census says the opposite. `world-census.json`, entry `taborite-radicalism`:
- `"status": "Within Another World (A5)"`
- `"statusWord": "Named within another tradition's story"`
- `"statusDescription": "Not counted as a candidate tradition of its own — its story is told plainly inside another tradition's, rather than standing alone."`
- `"relationsSummary": "The radical wing of the Hussite movement."`

Its `sources` list is a reference list attached to a census row. It is not a build track, and nothing records V.11 as built or scheduled to be built. The census's own A5 classification points toward Taborite material being told *inside* another world. The most natural candidate is this one: V.6's own `longDescription` narrates the Žižka and Prokop armies, and V.11's `legacy` field ties Tabor's end directly to Chelčický and the Unity's pacifism.

The decision to flag the question for Mark rather than settle it is correct, and should stay. But the flag has to describe the options accurately. As written, the default ("external comparative context") is presented as census-backed when the census cuts the other way. Double-claiming, the reason given against treating Tabor as an internal strand, does not arise for an A5 entry.

*Required:* Correct the description of V.11 in §4.2, §7 item 8 and §9 item 4. Restate the question for Mark with accurate options. For example: (a) Taborite radicalism is an internal strand of V.6, consistent with its A5 status; (b) V.11 is promoted to a candidate world of its own, which would be a census reclassification; (c) something else. Either do not state a working default, or state one that does not rest on a claim of separate registration. This finding changes a scope rationale, so it is substantial.

**S2. §1 reverses the direction of the Wyche letter.**
§1 says: "Hus's letter to the English Wycliffite Richard Wyche was read aloud in the Bethlehem Chapel." The source says the reverse. It was *Wyche's* letter to Hus that Hus read in the Bethlehem.
- Contents entry for Letter VI (line 389): "Hus's delight with Wyche's letter; He read it in the Bethlehem."
- Hus's reply, lines 2659 and 2688–2698: "On the receipt of Wyche's letter, Hus replied as follows … our dear brother Richard, partner of Master John Wyclif in the toils of the gospel, hath written you a letter of so much cheer … Christ's faithful ones were fired with such ardour by the letter that they begged me to translate it into our mother tongue."

The broader point, a real personal channel between Hus and the Wycliffites, still stands. It is in fact stronger than §1 says: the congregation asked for the English Wycliffite's letter to be put into Czech.

*Required:* Rewrite the sentence. For example: "Wyche's letter to Hus was read aloud in the Bethlehem Chapel, and the congregation asked for it to be translated into Czech. Hus's reply (Letter VI, September 1410) records this." This is a factual correction, so it is substantial.

**S3. §1 calls the Compactata "a papal-recognized legal settlement."**
The Compactata were negotiated with the Council of Basel and confirmed by Sigismund at Iglau. The vendored Gillett, Vol. II, line 21825: "These articles — soon confirmed by the Emperor Sigismund at Iglau, and afterward known as the Compactata of Iglau." The census `longDescription` calls them "the Compacts of Basel." Gillett at line 22171, one of the very lines Doc_01 cites, says that holding by the Compactata "came far short of the standard of papal orthodoxy," and goes on to Pius II's hostility.

The papacy never ratified the Compactata. Pius II's 1462 repudiation is standard history, though the lines checked here do not state it directly. "Papal-recognized" is therefore wrong. The same idea leaks into §5, "winning legal recognition from that same order," which is defensible only if "order" means the Council.

*Required:* Replace with "a legal settlement negotiated with the Council of Basel (1436)," or similar. Check §5's phrasing for the same slip. This changes a claim's substance, so it is substantial.

**S4. §5 Cell 3B is not a Layer-1 historical event. It is a construction scoping decision.**
The sketch is labelled "Layer 1 only — Historical Event." The Forces template defines Layer 1 as "what actually happened, as sources allow." Cell 3B reads: "The window's own 1517 close, chosen to keep the Unity of the Brethren's later generational voice … with the separate `czech-churches-last-century` entry." That is the project's own boundary choice, not an internal ending or transforming force in the world's history.

Every other cell stays on the historical-event layer. Cell 1B and Cell 2B are held on the Layer-1 side by their documentary framing, even though Cell 1B, "Hus's own ecclesiological conviction," sits near Layer 2. Cell 3B is the one category error, and it matters because the sketch "governs Step 2's source-ecology scope."

*Required:* Fill Cell 3B with a real internal ending or transforming event from inside the window, or mark it "not identified at Step 1 — for Doc_08." One candidate, from the vendored Lützow at p. 184: the Unity's late-15th-century split into the "Great" and "Small" parties, in which the Great party "reconciled itself with the world." Keep the boundary rationale in §2, where it already sits. This changes a forces claim, so it is substantial.

**S5. §4.1 overstates Lützow on Chelčický, and leaves out Lützow's evidence that Strand B changed inside the window.**
Two problems.

1. **Overstatement.** §4.1 says Lützow "records Chelčický's own explicit doctrinal distance from both the Taborites and (on the Eucharist specifically) from Hus, considering Wyclif rather than Hus his own teacher on that point." Lützow is hedged and narrower. The text at lines ~10035–10043 reads: "His views with regard to the Sacrament of the Altar … were opposed to those of the Taborites, *with whom he sympathized on some points*. … He *seems to have considered* that the English divine, rather than Hus, was his own teacher." Lützow records no explicit doctrinal distance from Hus on the Eucharist. He records a hedged inference about whom Chelčický counted as his teacher.

2. **Omission.** Lützow (p. 184, lines ~10110–10125) records that "about the end of the fifteenth century" the Unity split. The "Small" party held to Chelčický's non-resistance and "soon became extinct." The "Great" party "reconciled itself with the world, and by partly abandoning its earliest principles secured the future existence of the 'Unity.'" This falls inside the 1457–1517 window. §4.1 describes Strand B's ground as "deliberate, principled pacifism and a stricter separatist discipline" with no qualification. That is only true of the Unity's first decades on this source.

Neither problem undoes the strand finding. The simultaneity argument holds, and the split is more evidence of a real, recurring divergence in authority-ground. But the confidence and wording of the Strand B description must match the source.

*Required:* Keep Lützow's "seems to have considered" and "sympathized on some points." Drop "explicit … from Hus." Add the Great/Small split as a documented within-window development of Strand B. This changes a sourcing conclusion and a characterization, so it is substantial.

### Minor (fix in the same revision; none alone would block)

**m1. The Schaff quote in §1 is not verbatim, and one line citation is off.**
§1 renders the quote as "Huss appropriated paragraph after paragraph from his [Wyclif], and transferred them…". The source, lines 1514–1516, reads: "Huss appropriated paragraph after paragraph from his predecessor and transferred them often with little verbal change to his own pages." The bracket *replaces* a word ("predecessor") and a comma has been added. Under this project's verbatim rule, quote the text exactly and gloss outside the quotation marks. For example: "…from his predecessor [Wyclif] and transferred them…".

Separately, "Never did a man owe more…" begins at line 1542 and runs across the page break to line 1552 (pp. xxvi–xxvii). It does not begin at line 1554.

**m2. The census V.6 entry is also stale on the window, and §7 item 6 flags only the dossier.**
The dossier flag is done correctly: flagged, not silently resolved, which satisfies check 7. But `world-census.json` V.6 still reads `"dates": "1415-1517"`, `"start": 1415`, and its teaser says "Bohemia, 1415 to 1517." `Step0_Review_Round3.md` already reported this ("Outside this document"). Doc_01 cites the census repeatedly and should name the census's staleness alongside the dossier's.

**m3. Cell 1A makes an unsourced claim.**
Cell 1A says Wyclif's writings reached Prague "through university and court contacts." Neither Step 0 nor any vendored passage cited in Doc_01 supports this route. Step 0 A5 says only that "the link runs through his texts." Either cite a vendored source or cut the phrase.

**m4. R3-m1 is carried forward only partly.**
§2 correctly says Hus was "appointed … on March 14, 1402." §1's short description still says the movement "began as Jan Hus's Czech-language preaching career at Prague's Bethlehem Chapel (1402)." Workman's footnote gives 1401 as Hus's own first year of preaching. Align §1 with §2 ("appointed preacher at the Bethlehem Chapel in March 1402"). §7 should also list R3-m1 as a carried item.

**m5. `czech-churches-last-century` content is described beyond what the census says.**
§1 and §3 list "the 1632/33 *Ratio Disciplinae*" among that entry's content. The census VI.24 entry does not name the *Ratio*. Its window closes in c. 1627, before 1632/33. The assignment of the *Ratio* away from this world comes from Step 0's ruling and is not reopened here. Describe it as "assigned by the Step 0 ruling to the successor entry," not as part of the census entry's own scope. Add the date mismatch to §7 as an item for Mark.

**m6. A misparse in §5, "What was it responding to."**
"…and, once adopted in 1414, the practice of withholding the communion cup from lay people…" reads as if *withholding* the cup was adopted in 1414. Reword it. For example: "the practice of withholding the cup from lay people, which, once utraquism was adopted in 1414, became…".

**m7. Process narration and phrasing aimed at the reviewer.**
Examples: "per this task's own instruction" (§7 item 6), "this thread" (§4.2), and "for reviewer convenience" (§9 heading). Construction documents move to `worlds/<code>/` once a code is assigned, and that is a canonical surface. Remove these at this revision.

**Gillett note, non-blocking.** Gillett places the Compactata at Iglau, with Sigismund's confirmation there, and does not give a separate "Basel 1436" framing. Doc_01's "1436–37 Council/Diet at Iglau" is acceptable. S3 covers the substantive point.

---

## Confirmed accurate

Each item was re-verified directly against the vendored file or the census JSON.

- **March 14, 1402 appointment.** `hus_letters_workman-pope1904.txt` line 1440: "Two years later (March 14, 1402) he was appointed preacher at the Chapel of the Holy Innocents of Bethlehem." Verbatim.
- **Letters' span from June 1408.** Line 330 "(June 30, 1408)"; line 1381 "(June 30, 1408— September 28, 1411)."
- **Workman p. 177 note.** Lines 8815–8817: "Hitherto, Hus had taken little interest in the matter — in fact, in his De Coena Domini, written at a later date, he still practically concedes the Roman position." Verbatim; the bracketed gloss in §2 is fine.
- **Jakoubek, summer 1414.** Line 8807: "persuaded Jakoubek, in the summer of 1414."
- **"I have appealed to Christ."** Letters, line 11619. *De Ecclesia*'s index also lists "Appeal to Christ, 207, 208" (line 15135). The claim that this is a recurring pattern across both works is supported.
- **Letter VI to Richard Wyche.** Lines 384 and 2467–2853; this is the correct letter number and range. Only the direction in §1 is wrong (S2).
- ***De Ecclesia* Christology.** Line 6000: "confessed Christ to be very God and very man." Line 6285: "heretical, denying Jesus to be very God and very man." Both verbatim. The Trinity and Holy Spirit/Ghost language cited in the floor-check extension is present at multiple points (10 and 35 hits).
- **Wyclif's two sources.** Lines 1545–1546: "The two sources upon which Huss drew were Wyclifs de Ecclesia and his de potestate Papa." This supports Cell 1B.
- **"Never did a man owe more to mortal teacher than Huss did to John Wyclif."** Verbatim, lines 1542 and 1552. Only the line number is off (m1).
- **Lützow on Chelčický.** "The intellectual originator of the 'Unity' of the Bohemian Brethren" and "his belief in the absolute and unconditional sinfulness of bloodshed" are verbatim, pp. 182–183. The Kunwald refuge after Ladislas's death (1457) is at p. 184. "Gregory the Patriarch" is the census's name for him. Lützow calls him "Brother Gregory," so attribute the title to the census.
- **Gillett citations.** Lines 20892 (chapter summary naming the Compactata), 21825 (Compactata of Iglau confirmed by Sigismund) and 22171 (George of Poděbrady "held by the Compactata of Iglau") are all real and on topic.
- **Hus as university rector.** Letters, line 1425.
- **Census quotes.** V.6 `relationsSummary`, "A functioning non-Roman national church a century before Luther," is verbatim. V.11 has dates 1420–1452, and its source note reads "The movement's own bishop defending Taborite doctrine" verbatim. V.6 lane is "Latin West & Catholicism" (Era 6). VI.24 lane is "Protestant & Evangelical" (Era 7), window 1517–c. 1627. Five crusades and Lipany 1434 match the census.
- **Window consistency (check 2): PASS.** The window is c. 1402–1517 in the header, §2, §4.1 and §9. "1415" appears only as the date of Hus's execution and as the stale dossier window being flagged. "1632/33" appears only as the date of the *Ratio*, placed outside the window. No stray boundary anywhere.
- **Strand reasoning mode (check 4): PASS on method.** Strand B is argued from simultaneous coexistence and a distinct authority-ground, not from sequential development. S5 corrects the evidence wording, not the method. The Taborite question is rightly flagged rather than decided, but its framing rests on S1's misreading.
- **Lollardy (check 6): PASS on substance.** Direct textual dependence is stated plainly, and distinctness is rested on outcome and register, not source independence. Fix the S2 and m1 details.
- **Dossier staleness (check 7): PASS.** The dossier's line 8, "Time window: 1415–1517," is flagged in §7 item 6 and not silently resolved. m2 extends the flag to the census.
- **Living Tradition Status** is left PENDING per Article 29 and not self-confirmed. Correct.

---

## Disposition

**Not cleared. Round 2 required.** Five substantial findings (S1–S5) and seven minor findings (m1–m7).

Round 2 should be a targeted recheck of the changed passages against these findings only: §1, §3, §4.1, §4.2, §5 (Cell 1A, Cell 3B, "responding to"), §7 and §9. It should not re-review the whole document.

S1's corrected framing of the Taborite question goes to Mark as a portfolio-level classification question, as the draft already intends. The reviser should not resolve it. This is Round 1 of a maximum of three substantial rounds.

Outside this document, reported but not fixed: the census V.6 `dates`/`start`/`teaser` still read 1415, as Step 0 Round 3 also reported.
