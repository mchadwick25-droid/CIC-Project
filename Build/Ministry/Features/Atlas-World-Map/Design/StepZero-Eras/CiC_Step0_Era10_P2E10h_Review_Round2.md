# Era 10, P2-E10h: adversarial review, Round 2

Reviewer: independent Opus 5.5 review · 2026-11-09 · Round 2 (targeted recheck: only what changed, against the Round 1 findings)

**Object.** `Build/Ministry/Features/Atlas-World-Map/Design/StepZero-Eras/CiC_Step0_Era10_P2E10h_Proposed.json` (revised), on branch `claude/era10-p2e10h` at d9b373401, against `cic-website/data/world-census.json` (release 24, 307 movements). The reviser's response and new trace are under "Revision after Review Round 1" in `CiC_Step0_Era10_P2E10h_Trace.md`. Pre-revision copy: `scratchpad/e10h-merged/proposal.pre-rev1.json`.

**Method.**
- Structural diff of the revised proposal against the pre-rev1 copy (`e10h-rev2/jdiff.py`, output `e10h-rev2/diff.txt`).
- Applied the revised proposal with my own Round 1 applier (`e10h-rev2/myapply.py`). Every old string matched once. `node tools/validate-census.mjs applied.json --atlas cft-website/index.html`: 322 movements, 578 edges, 10 eras, **0 errors, 2 warnings** (the same two era 1 shortName warnings).
- Sentence length (`e10h-rev2/len.py`): every sentence in the 15 new rows and in every edit string, and every sentence of an edited field that differs from release 24.
- Re-verified by web only what the fixes newly rest on: the Holy See Press Office biography of Cardinal Todea, the 1965 Joint Declaration (vatican.va), and *Christianity Today*, "What's Behind the Idea of a Missionary Moratorium?" (November 1974). Mahieu 2004 was re-read from the MPI PDF downloaded in Round 1 (`e10h-rev1/dl/mpi.pdf`).
- Tested every fix below by applying it (`e10h-rev2/fixes.py` → `proposal.r2fixed.json`): old strings match once, 0 validator errors, no prose sentence past 25 words.
- No repo file was edited. No metered model call was made.

---

## Round 1 substantial findings: status

**S-1 (IX.44, Titicaca).** Fixed as given. "The church's own internal arguments" removes the dangling "Its", and "on the altiplano" restores Teel's scope. One new defect comes from my own Round 1 text, not the reviser's: that sentence now runs 27 words, and its "that same public record" now points back across four sentences about the altiplano. See M2-1.

**S-2 (IX.24, Lausanne).** Fixed. Re-read *CT* November 1974: "the idea of a broad moratorium appeared to be rejected by most leaders from the Third World and from the Western nations", and the Covenant quoted as "A reduction of foreign missionaries and money in an evangelized country may sometimes be necessary", continuing to the national church's growth in self-reliance. The note on edit 15 matches. One loosening in my own Round 1 text: "help a national church grow" drops "in self-reliance", and "grow" alone reads as growth in numbers. See M2-2.

**S-3 (IX.73, the Todea date).** Fixed in all five places.
- Holy See Press Office biography, re-read: "On 14 March 1990 was promoted to the Metropolitan See of Făgăraş and Alba Iulia." Confirmed. The biography does not name the pope, but in March 1990 the pope was John Paul II, and the church was then a metropolitan church whose head the pope named. "John Paul II named" is supported.
- Some Romanian sources give 12 March 1990 for the same act (search results; not opened). The Holy See's own record is the right source for the Holy See's act. No change needed.
- Mahieu 2004, re-read: "On December 1, 1948, Decree no. 358 … disbanded the Greek Catholic Church and handed over its properties to the Romanian state", and "abrogated Decree 358/1948 by Decree-Law no. 9 on December 31, 1989". It also reproduces Decree-Law 126 of April 1990. Confirmed. The new source entries are correct.
- The reviser's splits of my statusDescription and sourcing sentences (each over 25 words) are right.
- One new point: Mahieu, now cited, also says "legally, the Orthodox Church did not receive the Greek Catholic properties", and that "the majority of the properties were used by the Orthodox Church". The rows still say the church buildings passed "to the Orthodox church". This is true in practice, and Mahieu herself speaks of "the goods taken by the Romanian Orthodox Church", so it is not substantial. It should still match the source now cited. See M2-3.

**S-4 (IX.72, 1054).** Fixed. Re-read the Declaration: ¶2 "the sentence of excommunication leveled against the Patriarch Michael Cerularius and two other persons by the legate of the Roman See under the leadership of Cardinal Humbertus", and "a similar sentence pronounced by the patriarch and the Synod of Constantinople"; ¶3 "against the persons concerned and not the Churches"; ¶4 "remove both from memory and from the midst of the Church the sentences of excommunication". The new `why` and `longDescription` match the text. The teaser and voice are ruled under "Departures" below.

**S-5 (El Shaddai).** Fixed, first option. Edit 52 carries no founder and no date. IX.66 has no El Shaddai source entry and no Velarde voice; I checked that neither "1984" nor "Velarde" appears in the applied IX.66. The gap is logged in `notes.asia.notDrafted` and `notes.rev1.wants`, so it does not go quiet.

## Round 1 minor findings: status

- **M-2.** Done for the four quoted sentences, and for the IX.62 teaser. My check finds two more sentences this slice rewrites past 25 words, in IX.11 (see M2-4). Source `work` strings over 25 words (IX.15, IX.46) are citations, not prose, and are exempt.
- **M-3.** Done ("Latin Am. Catholic").
- **M-4.** Done ("Most belonged").
- **M-5.** Done in IX.69 to IX.72. In IX.73 the kept "It had been legal again since 1989." now opens the legacy with a past perfect that has no reference time, and it repeats the longDescription. That was my wording. See M2-3.
- **M-6.** Done.
- **M-7.** Done.
- **M-8.** Done in sourcing, the source, the voice and `why`.
- **M-9.** Done: the narrow claim, Longman 2009 in IX.59 and edit 1, and "Saint Peter's" throughout. No "St Peter's" remains.
- **M-10.** IX.8 done, as given. IX.21: see S2-1.
- **M-11.** Not done, and the reviser's reason holds: the validator ties each country to the place label. It stays a coordinator call.
- **M-12.** Done: the Korean lines are in `notes.asia.notDrafted`, Zink is "secondary", and the C7 table is superseded in the repo trace's revision section.
- **M-13.** Left as drafted, with the want logged. Acceptable; it was optional.
- **M-15.** Done. IX.63 is FRE 48.8 and FK 8.87, with no fact changed. I checked the reworded sentences against the pre-rev1 text: no fact is added or lost.

## Departures and open points: ruled

- **IX.73 drops "published the next day".** Accepted. No opened item carries 2 December 1948, and Mahieu gives only 1 December. The text keeps what is verified.
- **IX.72 teaser and Paul VI voice still say "ended" and "lifted".** Consistent with S-4 in substance. Neither says the churches cut each other off, and "lifting of the excommunications" is the common phrase. Two small problems remain, so this is minor, not substantial. The row now uses two verbs for one act, against the Declaration's own "remove from memory". And the teaser gives the act to the Patriarchate alone, although it was a joint act with Rome. See M2-5.
- **IX.21's order after M-10.** Not acceptable as it stands. See S2-1.

## Diff against the pre-rev1 copy

Every content change in the diff is one listed in the reviser's response: S-1 to S-5, M-2 to M-10, M-12 and M-15, plus the new `notes.rev1` block and the two `notDrafted` lines. Nothing else changed. The one other difference is format only: the repo copy drops the `slice` key ("afla", "asia", "east") from every register edit. The applier ignores that key, and the merged scratch copy still has it.

---

## SUBSTANTIAL findings

**S2-1. IX.21: after the M-10 move, "What followed was forty-three years" reads as the Czechoslovak church's story.**
- *Location:* registerEdits[43], IX.21 `longDescription`.
- *Evidence:* the applied text reads: "…none took part. In communist Czechoslovakia the Greek Catholic Church was liquidated between 1948 and 1950. A 'sobor' met at Prešov on 28 April 1950, in an operation called 'Action P'. What followed was forty-three years as the largest banned church in the world…". The nearest subject of "What followed" is now the Prešov sobor. Forty-three years (1946 to 1989) is the Ukrainian count, and it is wrong for the Czechoslovak church. My M-10 fix created this. The reviser saw it and flagged it.
- *Fix:* registerEdits[43]:
  - `old` = "none took part. What followed was forty-three years as the largest banned church in the world: priests ordained in secret, liturgies in apartments and forests, bishops in the Gulag." (It matches release 24 once.)
  - `new` = "none took part. In communist Czechoslovakia the Greek Catholic Church was liquidated between 1948 and 1950. A 'sobor' met at Prešov on 28 April 1950, in an operation called 'Action P'. For forty-three years the Ukrainian church was the largest banned church in the world. It had priests ordained in secret, liturgies in apartments and forests, and bishops in the Gulag."
  - This also brings the old 26-word sentence under 25. It adds no fact.

---

## MINOR findings

**M2-1. IX.44: a 27-word sentence, and "that same public record" now points too far back.**
- *Fix:* put the Titicaca sentences after the existing last sentence, and leave that sentence as it stood. registerEdits[55]:
  - `old` = "rather than hidden in it." (It matches once.)
  - `new` = "rather than hidden in it. In 1911 Ferdinand and Ana Stahl joined Manuel Camacho at Utawilaya, in Platería district, Puno province, on the Peruvian side of Lake Titicaca. Camacho, an Indigenous visionary, was one of the first Adventist converts on the altiplano. He had opened a free school in his home about 1902. The Stahls lived in an adobe building that served as a school on weekdays and a place of worship on Sabbaths."
- With that, "Its own internal arguments" again follows the sentence about the church's own record, which it was written to follow. The S-1 pronoun problem cannot recur. The sentence is the census's own (26 words) and this slice no longer touches it.

**M2-2. IX.24: keep the Covenant's "in self-reliance".**
- *Fix:* in registerEdits[14] `new`, "might sometimes help a national church grow." → "might sometimes help a national church grow in self-reliance."

**M2-3. IX.73: say what Mahieu says about the buildings, and drop the orphaned legacy sentence.**
- `why`: "Its property passed to the state, and its churches to the Orthodox church." → "Its property passed to the state, and most of its churches came into Orthodox use."
- `longDescription`: "Its property passed to the state, and its church buildings to the Orthodox church." → "Its property passed to the state, and most of its church buildings came into Orthodox use."
- `relationsSummary`: "which received this church's buildings" → "which took over most of this church's buildings".
- `legacy`: delete "It had been legal again since 1989. " (the fact stays in `why` and `longDescription`).

**M2-4. IX.11: two sentences this slice rewrites run 37 and 42 words.** Both were long in release 24. This slice edits both (edits 49 and 51), so they should come under 25 now. The teaser also carries map commentary ("rather than described from outside"), which M-14 asks the PR to clear.
- registerEdits[49]: `old` = the whole release 24 teaser, "Brazil, Nigeria, Ghana, Korea and the Philippines, 1950s to 2010 — Pentecostalism's growing edge, descended from Azusa Street and Africa's independent churches alike, its argument over the prosperity gospel carried on the record in the movement's own published critiques rather than described from outside."; `new` = "Brazil, Nigeria, Ghana and Korea, 1910 to 2010 — Pentecostalism's growing edge, descended from Azusa Street and from Africa's independent churches. Its argument over the prosperity gospel is on the record in its own published critiques."
- registerEdits[51]: `old` = "The Assembleias de Deus in Brazil date from 1911; the Redeemed Christian Church of God was founded in Nigeria in 1952; Yoido Full Gospel Church in Seoul from 1958; the Igreja Universal in Brazil from 1977; El Shaddai in the Philippines from 1984." (It matches once.); `new` = "The Assembleias de Deus in Brazil date from 1911. The Redeemed Christian Church of God was founded in Nigeria in 1952. Yoido Full Gospel Church in Seoul dates from 1958, and the Igreja Universal in Brazil from 1977."
- No fact is added or lost.

**M2-5. IX.72: one verb for the act of 1965, and Rome named in the teaser.**
- `teaser` = "Greece and Istanbul, 1906 to 2010 — the Church of Greece and its Zoe brotherhood, and the Ecumenical Patriarchate. With Rome, it removed the excommunications of 1054 from memory in 1965."
- `voices[1]` = "Paul VI — the pope who, with Athenagoras, removed the excommunications of 1054 from memory"

**M2-6. IX.8 (optional): "again" and "both meetings" have no antecedent inside `relationsSummary`.** Medellín is named only in the longDescription. That was my wording.
- registerEdits[17] `new` = "continued inside Latin American church life. The bishops' meetings at Medellín in 1968 and Puebla in 1979 are told in the entry on Latin American Catholicism, the parent of this one."

All six fixes together were applied and tested (`e10h-rev2/proposal.r2fixed.json`): every old string matched once; validator 322 movements, 578 edges, 0 errors, 2 warnings (the same two); no prose sentence in a new row, edit string or rewritten field passes 25 words.

---

## Verdict

**Not approved to proceed.** S-1 to S-5 are fixed, and what the fixes newly rest on checks out: the Todea biography (14 March 1990), Mahieu 2004, the Joint Declaration's wording and the *CT* sentences. The diff is clean, and the minors are carried out. One substantial finding remains, and the revision created it: S2-1. IX.21's forty-three years now attach to the Czechoslovak church. It comes from my own Round 1 M-10 fix, and the reviser flagged it.

The fix is exact text, needs no research, and is tested. Round 3 should check S2-1 and whichever of M2-1 to M2-6 are taken up, and nothing more. This is Round 2 of the three-round cap. If S2-1 is applied as given, nothing I have seen would hold up approval in Round 3.
