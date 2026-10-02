Simulated review — informational only, not an Article 31 substitute.

Reviewer model: claude-opus-5-5
Drafter model: claude-fable-5-1
Reviewer agent: Doc_10 round 2 recheck, fresh context, medium effort, targeted; read the round-1 review, OG-66, OG-67 and the current files, nothing of the revising session
Drafter agent: the Doc_10 round-1 revision session (Fable, working alone), commit 7c37e12f9, recorded in `Open_Gaps_Tracking.md` OG-66 and OG-67
Round: 2 of 3 for Doc_10 (`roundcount lpc 10 --check-new` passed before this file was written; 1 earlier review file on record)
Truncation check, method 1: heading count and closing line. `grep -cE '^### N[0-9]+ '` on this file returns 5 new-finding headings, and `tail -n 1` returns "End of review.", both run after the last edit.
Truncation check, method 2: set comparison in Python. The ids in the summary table (26: S1–S9, O1–O12, N1–N5) equal, as a set, the ids of the prior-finding verdict table (21) together with the `###` new-finding sections (5). The reviewed files were checked the same two ways: each file's byte count on disk equals `git cat-file -s HEAD:<path>` (Doc_10 77,596; Permanent Prompt 22,272; demonstrations 4,517, 4,110, 4,967 and 4,557; voice record 7,106; world_core 31,443), and each ends on a complete sentence. The compiled prompt (the package pinned at the time (its compiled prompt), 85,033 bytes, not tracked by git) ends on the last sentence of the road-back demonstration, and the four demonstration exchanges and the `living_traditions` and voice-record texts in the package equal the record files.

# Round-2 recheck of Doc_10, Representative Construction Notes: Datus (`lpc`)

**Scope.** Only what changed since round 1, against `Review-Artifacts/Doc10_Round1_Review.md`: Doc_10; the Permanent Prompt file; the four demonstrations; `lpc.craft.datus-voice`; `world_core.living_traditions`; the compiled prompt of the pinned package (`records/worlds/lpc.yaml`: the package pinned at the time). N1 was found while verifying the S2/O11 sentences of the compel demonstration at source, and is raised because it is a factual error in a deployed exemplar, not a stylistic preference.

## Verdict

**Not approved to proceed this round.** Every round-1 finding is resolved: S1–S8 as proposed, S9 by the project lead's ruling, and all twelve optional findings. Every changed factual statement holds at source. But one new substantial finding stands (N1): the compel demonstration and the Prompt date the petition council to 401, and two of this world's own vendored Native sources date it to June 404. The fix is one word in each place, plus a source locus. N2 is a mechanical citation fix. N3–N5 are optional. Round 3, the last under the cap, should be a targeted recheck of N1 and N2 only.

## Gates run directly

| Check | Result |
|---|---|
| `roundcount lpc 10 --check-new` | PASS (1 review file on record before this one) |
| `prereview lpc --doc 10` | PASS on all five checks (m2 build 22 gates, 0 failing; bar screen 13 voice-diet fields, 0 over FK 10; cross-world 0 new; holdings). The run rewrote `build/lpc_Prereview_Doc10.txt` |
| `records lpc` | PASS |
| `regate lpc` | PASS. 274 public fields, 191 new or edited; 150 below FK 8, reported and not failed |
| `gaps lpc` | PASS |
| `claims lpc` | PASS. 113 derived, 113 registered; the one UNVERIFIED row is `dbfc0882` (Doc_04), not a Doc_10 claim |
| `deployed lpc` | PASS at pin 2026-10-01T14-54-23Z; `living_traditions` verbatim in the prompt |
| Readability, demonstrations (engine `fk.py`) | Representative turns FK 3.6–6.0, FRE 72.5–94.1; average sentence 10.3–14.8 words. Participant turns of 12 words or more clear FRE 60. `living_traditions` FK 7.7, FRE 69.6 |
| Voice gates | `gate_readability`, `gate_voice_perspective`, `gate_quote_verbatim` and the rest of the 22 m2 gates: 0 failing (via prereview) |
| Six-word overlap between any two demonstrations | None |

**Claims register.** No Doc_10 claim id changed in this revision. The S5 sentence derives no claim, and stale row `e7517592` is removed, as OG-67 records. The Doc_10-derived ids still registered are `016b10a0` (VERIFIED), `a609c538` and `f2a0dc4c` (JUDGEMENT), as round 1 set them. The voice-record silence claim is `7480efe2`; the world_core claims are `0981e69a`, `dc7b8b34`, `cf7ee278` and `47bbbca6`. The removed compel sentence ("Cyprian never asked the state for anything") was never derived. No register row was edited by this review.

## Changed statements re-verified at source

| Statement | Vendored location | Result |
|---|---|---|
| Returning schismatics not baptized again; returning clergy not ordained again; a practice already in force (S1) | NPNF104 `div4 id="v.iv.iii.i"` (l. 10809), On Baptism I.1.2, l. 10826–10842 | holds |
| Council decision, envoys, a law already published with fine and exile; "medicinal inconvenience ... cannot be softened by words"; "left our deputation nothing to do" (S3, O11) | NPNF104 `div3 id="v.vi.ix"`, Letter 185 §§25–26, l. 19620–19640 | holds. The year 401 is the editor's footnote there, not Augustine's text (see N1) |
| "originally my opinion was, that no one should be coerced"; "fear of the imperial edicts"; "would scarcely be believed"; others "mentioned to me by name" (O11) | NPNF101 Letter XCIII §17, l. 38240–38262 | holds; "would hardly believe" is faithful |
| Harnack: 259, "die herrschende Ansicht"; Koch: end of the third century at the earliest, "den Augen- und Ohrenzeugen spielt"; "on either date ... does not fill the silence" (S4) | Doc_02 §7, l. 120 | holds; Prompt l. 21, Doc_10 §3 and §8 Scholarly item 2 carry it as Contested |
| "Both anchor voices are bishops; ... attested only through episcopal mediation" (S5) | Doc_01 §8 item 3, l. 173 | holds. Doc_02 §6 (l. 107) also names Pontius and Epistles XX–XXI (see N3) |
| Epistle X: "Such a one with his friends"; "twenty or thirty or more"; "designate by name ... whom you yourselves see" | ANF05 `div3 id="iv.iv.x"` (l. 29836), l. 29936–29950 | holds |
| "present themselves at the threshold of the church" (O4, as the reviser corrected it) | ANF05 `div3 id="iv.iv.xxx"` (l. 31564, "The Roman Clergy to Cyprian"), l. 31759–31760 | holds. The reviser was right: Epistle XXX, not Cyprian's own words; the locus says so |
| Novatian's party made Maximus "their false bishop in that place" (O4) | ANF05 `div3 id="iv.iv.liv"` (l. 34434, Epistle LIV to Cornelius), l. 34776–34780; "excommunicated by them here", l. 34770 | holds; "here" is Carthage, so "in Carthage itself" stands |
| *Datus* as an African cognomen (O12) | Gsell, index from l. 110230 (Aemilius, Calpurnius, Lolius Datus and others; 13 hits) | holds |
| *Datus* as Baronius's variant for *Dantus* (O12) | `monumenta-vetera-donatistarum-303-340_migne-pl8.txt` l. 2506, 2622 ("Dantus. Bar. Datus.") | holds |

## The self-naming line (S9 ruling)

The single sanctioned world line is "I am a representative of the ordinary churches of Latin Africa." It stands in the voice record's self-reference note (l. 44), in Prompt l. 17 (once in a turn, only when asked what the voice is), in Doc_10 §8 Calibration item 1, and in the compiled prompt (l. 45). The compiled prompt's fleet rule (l. 13) prints the fleet form with the display name. The syr package does the same (l. 13 and l. 42), so this is fleet practice, not a second form.

No "flock kept ... keeps its own" line remains in the voice record, the Prompt, the demonstrations or the compiled prompt. Doc_10 keeps it once, by design, in §3 "What Was Excluded and Why" (l. 209), as the record of what was excluded. §8 item 1 also names the removed tail in parentheses. Neither is a sanctioned line.

Outside the prompt: `lpc_Voice_Configuration_Datus.md` l. 10 now carries the ruled line (commit `6ea583fe2`). `lpc_World_Capsule_Core.md` l. 3 still carries the old tail: "the flock kept by a named man who is answerable for it, and the flock that keeps its own." It is not compiled, so it is not a Doc_10 defect, but its owner should bring it to the ruling (N5).

## Verdicts on the round-1 findings

| id | verdict | evidence in the current files |
|---|---|---|
| S1 | resolved | Font turn 1: "By his years we no longer baptized such people again." Turn 2: "Augustine's answer was our practice." No causal step from his books |
| S2 | resolved | Compel turn 1: "In Cyprian's years the emperors were the ones persecuting us." The Scope note grounds it in `lpc.force.decian-persecution-libelli-system` |
| S3 | resolved | Turn 2 closes on "He called the laws a kind of medicine for hearts that words could not soften." Doc_10 §2 (b) is true as written |
| S4 | resolved | Prompt l. 21 as proposed, with the following sentence deleted. Doc_10 §3 (l. 201) and §8 Scholarly item 2 carry the Contested date |
| S5 | resolved (see N3) | Doc_10 §1 l. 39 carries the proposed wording |
| S6 | resolved | `living_traditions` (world_core l. 364–370), compiled l. 179, Prompt l. 67 and Doc_10 §10 carry the same text. It is in-voice ("ours", "we"). The divergences stay Facilitator-carried (Doc_10 §6). It passes no judgement on any present-day church: "none from ours alone" is a historical statement, and "Those churches have their own voice" defers to them. The 33-word sentence is logged for M2 (N4) |
| S7 | resolved | Doc_10 §8 Calibration item 8 and OG-66 carry the *Dativus* conflict for the project lead |
| S8 | resolved | §4 (l. 241) cites Build Process V2.0's Result-label check. §7 carries no pass/fail verbs on simulated results ("passed", "failed" and "scored" do not occur) |
| S9 | resolved by the project lead's ruling | See above |
| O1 | resolved | §8 item 4 gives the right reason (template text, not spoken; 5d protects the museum-guide paragraphs) |
| O2 | resolved | §2 l. 178: clears FRE 72–94, below the FK 8 floor at FK 3.6–6.0, which matches this review's measurement |
| O3 | resolved | "In time he gave in his name"; the Scope note says the turn names no season |
| O4 | resolved, with the reviser's correction accepted | `sources[]` names Epistle XXX (the Roman clergy) and Epistle LIV |
| O5 | resolved | §8 item 2 |
| O6 | resolved | Thinness row "Daily and household life" (l. 64) |
| O7 | resolved | §2 l. 168 names the shared wording with the Prompt file |
| O8 | resolved | Font turn 1 closes "Which of the two answers would you argue for?" §2 says each first turn hands the question back |
| O9 | resolved | Prompt l. 19: "What is not yours is anything after 430." |
| O10 | resolved | Both meta-phrases are gone. The compiled prompt's only "in order." is in an unrelated witness record (l. 305) |
| O11 | resolved | "came back without it"; "you would hardly believe it had once shared it" |
| O12 | resolved | Doc_10 §1 and OG-66 carry the recheck; verified above |

**Craft/Focus bar, all four demonstrations after the edits.** (a) holds: the C-P second turn answers the personal press in its first sentence, with no composite-voice framing. (b) holds: the second turns close on, in turn, the "kind of medicine" paraphrase of Letter 185 §26, the change of practice and Cyprian's words kept, the *Confessions* I.1 rendering, and the De Lapsis paraphrase. No turn closes on meta-commentary. (c) holds: no six-word run repeats across demonstrations. (d) holds: the compel hedge keeps the contested record's own two alternatives. (e) holds: the garden, the 256 council, Epistle X and Letter XCIII's towns are told as scenes.

## Summary of findings

| id | severity | where | subject |
|---|---|---|---|
| S1 | resolved | font | causal step removed |
| S2 | resolved | compel | absence claim replaced |
| S3 | resolved | compel; Doc_10 §2 | meta closing deleted |
| S4 | resolved | Prompt l. 21; Doc_10 §3, §8 | Pontius's date held Contested |
| S5 | resolved | Doc_10 §1 | overstatement replaced |
| S6 | resolved | `living_traditions` | overclaim and judgement gone |
| S7 | resolved | Doc_10 §8; OG-66 | *Dativus* conflict carried |
| S8 | resolved | Doc_10 §4, §7 | result-label language |
| S9 | resolved by ruling | voice record; Prompt; compiled prompt | one world self-naming line |
| O1 | resolved | Doc_10 §8 item 4 | template "this world" reason |
| O2 | resolved | Doc_10 §2, §7 | FK band wording |
| O3 | resolved | one-of-us | "In time" |
| O4 | resolved | road-back `sources[]` | loci added, Epistle XXX corrected |
| O5 | resolved | Doc_10 §8 item 2 | "about 130" |
| O6 | resolved | Doc_10 §1A | household row |
| O7 | resolved | Doc_10 §2 | grep-clean qualifier |
| O8 | resolved | font; Doc_10 §2 | first-turn close |
| O9 | resolved | Prompt l. 19 | after 430 |
| O10 | resolved | compel; font | meta-phrases |
| O11 | resolved | compel | two sharpenings |
| O12 | resolved | Doc_10 §1; OG-66 | name recheck |
| N1 | new, substantial | compel turn 1; Prompt l. 23 | the petition council dated 401; the world's own sources date it June 404 |
| N2 | new, mechanical | Doc_10 l. 152, l. 446 | cites a package pin that no longer exists |
| N3 | new, optional | Doc_10 §1 l. 39 | "heard only through them" is broader than Doc_02 §6 |
| N4 | new, optional | `living_traditions` sentence 2 | 33 words, over the break rule (already logged for M2) |
| N5 | new, optional (owner's file) | `lpc_World_Capsule_Core.md` l. 3 | old "flock kept" tail remains |

## New findings

### N1 Compel demonstration and Prompt l. 23: the petition council is dated 401; this world's own sources date it June 404

Compel turn 1: "Then, in 401, our bishops in council agreed to petition the emperors for one narrow thing." Prompt l. 23: "Then our bishops in council, in 401, agreed to ask the emperors for one narrow measure." The demonstration is compiled into the deployed prompt as an exemplar.

The year comes from the NPNF editor's footnote to Letter 185 §25 (NPNF104 l. 19631: "That of Carthage, held June 26 ... 401"). Augustine's text gives no year, and Doc_02 §7 (l. 17) already says so. Two vendored Native sources in this world's Registry date the council that sent the narrow petition:

- The Code of Canons of the African Church, the note before Canon XCIII (NPNF214 `id="xv.iv.iv.xciii-p6"`, l. 35826–35831; Registry row 26): "The most glorious emperor Honorius Augustus, being consul for the sixth time, on the Calends of July, at Carthage ... In this council Theasius and Euodius received a legation against the Donatists." Honorius's sixth consulship is 404. The commonitorium that follows (Canon XCIII, l. 35851 ff.) asks for Theodosius's law of "ten pounds of gold". That is the narrow measure Letter 185 §25 describes. The same text stands in the Latin (Bruns, row 202, l. 12659–12663: "Honorio augusto sextum consule").
- Hefele–Leclercq (row 247, l. 4882–4884): "Au mois de juin de l'année 404, le IX^e concile de Carthage ... députa aux empereurs ... deux évêques, Théase et Evode." At l. 4911–4915 it adds that Honorius's edict, with fines and exile, came before the envoys reached him, and that the severe laws followed in February 405. This matches Letter 185 §26's "a law had already been published".

The 401 council did deal with the Donatists, but it was conciliatory. The petition that the 405 law overtook was the council of 404. The voice states as fact a date its own sources contradict. That is a factual error in a Doc_10 deliverable, so it is substantial. It is not blocking.

**Exact wording, Doc_10's own surfaces.**
- Compel turn 1: replace "Then, in 401, our bishops in council agreed" with "Then, in 404, our bishops in council agreed".
- Compel `sources[]`: add `source_id: lpc.source.code-of-canons-of-the-african-church-419`, locus "the note before Canon XCIII and Canon XCIII (vendored NPNF214, div xv.iv.iv.xciii–xciv, lines 35826-35831 and 35851 onward), the legation of Theasius and Evodius in Honorius's sixth consulship (404) and its commonitorium on Theodosius's ten-pound fine", license `public-domain`.
- Compel Scope note: replace "a decision of the council of 401 to petition the emperors" with "a decision of the council of June 404 to petition the emperors (dated by the Code of Canons of the African Church, the note before Canon XCIII; Letter 185 gives no year)".
- Prompt l. 23: replace "in 401," with "in 404,".
- Then rebuild and repin.

**Outside Doc_10, for the record owners, in the same change.** The same 401 stands in the compiled `world_core` caution 5 (world_core l. 304: "Between them falls the council of 401 that Letter 185, section 25, records"; should read "the council of 404 whose petition Letter 185, section 25, describes"). It also stands in `lpc.source.augustine-correction-of-the-donatists` (l. 18), `lpc.source.augustine-letter-93-to-vincentius` (l. 42) and Doc_02 §7 (l. 17, l. 124). Doc_02 is approved, so correcting it is a change order. If only the demonstration changes, the compiled prompt will contradict itself (404 in the exemplar, 401 in caution 5). The correction belongs in `Open_Gaps_Tracking.md` as one entry. If the record owners cannot move in the same pass, the interim Doc_10 wording drops the year and gives no date ("Then our bishops in council agreed ..."; Prompt "Then our bishops in council agreed ..."). Do not write 404 in the voice beside 401 in the world core.

### N2 Doc_10 cites a package pin that no longer exists

Doc_10 l. 152 and l. 446 quote and name the package pinned at the time (its compiled prompt). Commit `2562d68f0` repinned the package to `2026-10-01T14-54-23Z` and removed the old directory. It did not update Doc_10. The quoted texts (the source-anchor paragraph and `living_traditions`) are verbatim in the new pin's prompt (checked in Python), so only the path is wrong. **Fix:** replace both path strings with the package pinned at the time (its compiled prompt). If N1 causes another repin, use that pin instead. This is a mechanical citation fix and needs no review of its own.

### N3 Doc_10 §1: "the ordinary believer is heard only through them"

This was round 1's proposed wording, and the revision applied it exactly. It cites Doc_02 §6. But Doc_02 §6 says that "two lay believers' own letters survive in their own words" (Epistles XX and XXI), and that the skew "is narrower than a blanket negative would suggest". The sentence reaches no participant and derives no claim, so this is optional. **Wording:** "both anchor voices are bishops, and the ordinary believer is heard almost only through them; Doc_02 §6 names the narrow exceptions (Doc_01 §8 item 3; Doc_02 §6)."

### N4 `living_traditions`, second sentence: 33 words

The sentence is "They carried forward, in different measures, how we thought of a bishop's care for his own people, our examined road back for the fallen, and our argument over what a sacrament truly needs." It runs past the roughly 25-word limit. OG-67 has already logged it for the project lead at M2. **A split, if he wants one:** "They carried forward, in different measures, how we thought of a bishop's care for his own people. They carried our examined road back for the fallen, and our argument over what a sacrament truly needs." Apply the same text to world_core, Prompt l. 67 and Doc_10 §10, then repin.

### N5 `lpc_World_Capsule_Core.md` l. 3 keeps the old tail

The line "the flock kept by a named man who is answerable for it, and the flock that keeps its own" stands in that file. It is not compiled and not part of Doc_10. OG-67 already flags it for its owner, and this review confirms it is still there. The Voice Configuration's line has been brought to the ruling.

## Round record

This is round 2 of 3 for Doc_10. Round 2 checked only what changed, against the round-1 file. All 21 round-1 findings are resolved. One new substantial finding (N1) and one mechanical finding (N2) remain. Round 3 is the last round under the cap. It should be a targeted recheck of N1 and N2 only. If N1 cannot clear in round 3, the cap rule applies and the document goes to the project lead. The verdict is not "no substantial finding". Doc_10 is not approved to proceed on this round.

End of review.
