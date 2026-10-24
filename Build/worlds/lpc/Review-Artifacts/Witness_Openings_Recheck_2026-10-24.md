# Witness Openings Recheck — lpc doctrinal_witness rewrites (round 2)

- **Date:** 2026-10-24
- **Reviewer:** independent adversarial reviewer, running as Claude Opus 5.5 (`claude-opus-5-5`)
- **Round:** 2, targeted recheck. Only what changed since round 1 was checked, against the round-1 findings in `Witness_Openings_Review_2026-10-24.md` (8 P1, 21 P2).
- **Scope:** the uncommitted fields in `records/lpc/doctrinal_witness/` (`git diff`). No repo file was modified except this one.
- **Stated deviations from the round-1 proposed texts:** tradition-tested `text` (P1 sentence split; three readability trims) and apostolic-succession `positions[0]` (the clause "each with the man who filled it "to-day."" kept).

## Method

1. **Quotations.** Every double-quoted string in every changed field (text and positions) was searched for in the cited `cic/texts/` files, with tags stripped, quote marks and whitespace normalised, and case and trailing punctuation ignored. **All quoted strings match verbatim.** No quotation was lost or altered by the P2 fixes.
2. **Loci.** I re-read the loci behind each P1 field: Letter LIII §2 (npnf101 lines 29696–29712), Answer to Petilian II.51 (npnf104 line 16912), Cyprian Ep. 73 §9 (anf05 line 39328), On Baptism V.23 (npnf104 lines 13135–13141), City of God XI.7 (npnf102 line 20406), and Reply to Faustus XXII.73–76.
3. **Readability.** Per-field scores from `engine.m1.fk`. Every changed field is at FK ≤ 8.9 and FRE ≥ 60.2.
4. **Gates.** `python -m engine.m10.cli regate lpc`: **PASS** (162 fields checked, 22 new or edited, no regression; 16 edited fields below FK 8, reported, not failed). `python -m engine.m10.cli records lpc`: **PASS**.

## Check 1 — the eight P1s

| Record / field | Round-1 P1 | Now | Fixed? | Claim vs. locus |
|---|---|---|---|---|
| apostolic-succession `text` | "Linus, the successor named by Peter himself" (invented) | "He reached Linus, Peter's own successor -- "In this order of succession no Donatist bishop is found."" | Yes | Matches Letter LIII §2, "The successor of Peter was Linus". The invented detail is gone. `positions[0]` does not carry it either. |
| blamed `text` | Meta-opener "We can tell you one real charge…" | "One charge our neighbours made comes down to us, because Cyprian wrote a whole reply to it." | Yes | Same claim as before. No widening. |
| days-before-the-sun `positions[0]` | Meta-opener | "Augustine took up how to read the days of Genesis directly, in City of God." | Yes | Same claim. |
| days-before-the-sun `text` | Meta-opener | Same new opener | Yes | Same claim. |
| heard-for-salvation `text` | Meta-opener "We have something real to give you…" | "Augustine taught directly on prayer that goes unanswered, from the apostle Paul's own words." | Yes | Same claim (Homily VI §6). |
| scripture-above-councils `text` | Hedge moved onto "above our bishops" | "Scripture stood above our bishops' own writings, but it was not our only authority." | Yes | Now states On Baptism II.3.4 without qualification, and puts the limit on "only authority", where the record's note puts it. Not narrowed or widened. See P2 below on the closing sentence. |
| tradition-tested `text` | Spoken garden-path "They are not rebaptizing, …" | "One practice is baptizing infants. The other is refusing to baptize again a person already baptized among heretics." | Yes | Neither practice is put in the collective "we" voice, so Cyprian's Africa is not misdescribed. Matches On Baptism II.7.12 and IV.24.32. |
| violence `text` | "A modern reader may miss why we found this untroubling" | "A modern reader may miss something here. Our bishop did not answer this way because he thought little of it." | Yes | The collective "we found this untroubling" is gone. The new sentence denies a dismissive motive in one named author. That is consistent with the record's own "much disturbed" and with its `tensions` field ("not an absence of moral seriousness"). It adds no positive claim the source must carry. See P2 below on the signpost sentence. |

**All 8 P1s are fixed. No fix adds, widens or narrows a claim against its cited locus.**

## Check 2 — the stated deviations

**tradition-tested `text`.**

- *Split sentence.* Faithful. It has the same two practices and the same wording, now in two sentences.
- *"one test … truly came from".* Faithful. "Single" was redundant, and "came from" and "goes back to" carry the same claim.
- *"about 150 years later".* **Acceptable.** Cyprian's letter to Pompeius (Ep. 73) dates to c. 256, and he died in 258. Augustine wrote *On Baptism, against the Donatists* c. 400–401. That gap is about 142–145 years. "About 150 years" is a fair round figure. It matches "a century and a half", which the world already uses in apostolic-succession, scripture-above-councils and communion-over-separation. "Nearly 150 years" would be a little more exact. It is not a finding.
- *". He uses this same second test."* Faithful. Its present tense matches the "does trace" just before it. On Baptism V.23 (lines 13135–13141) supports "fairly held to have been enjoined by the apostles, which yet are not mentioned in their writings".
- Scores: FK 7.9, FRE 60.6. Longest sentence: 21 words.

**apostolic-succession `positions[0]`: ", each with the man who filled it "to-day.""**

- Faithful. Petilian II.51 reads "the Roman Church, in which Peter sat, and which Anastasius fills to-day; or the chair of the Church of Jerusalem, in which James once sat, and in which John sits today". The quoted "to-day" appears verbatim in the locus. Applying it to both chairs matches the source's sense.
- Scores: FK 8.5, FRE 60.8.

## Check 3 — did the P2 fixes introduce problems?

All 21 P2 fixes were applied as proposed. Quotations are intact and attributions are kept. Specifically, days-before-the-sun now reads "We cannot understand how it was, he wrote, and yet we must believe it.", which restores the attribution. Two of the round-1 proposed texts themselves introduced small defects. Two older defects that this round left in unchanged fields are flagged for the owner.

| Record / field | Problem | Sev | Proposed text |
|---|---|---|---|
| apostolic-succession `text` | "Each still filled, "to-day," by a living bishop." is a sentence fragment with no main verb. This came from round 1's own instruction to keep the clause "as its own sentence". | P2 | "Each was still filled "to-day" by a living bishop." |
| baptism `positions[0]` | "names two of our practices as coming from the apostles, by name" says "name" twice. This came from round 1's own proposed text. | P2 | "Augustine traces two of our practices to the apostles by name, not only from a general belief." |
| scripture-above-councils `text` | The new opener says flatly that scripture "was not our only authority". The older closing sentence, "We do not claim scripture was our only authority in every sense.", now repeats it and hedges it again. "In every sense" implies that in some sense it was the only authority. | P2 | Delete "We do not claim scripture was our only authority in every sense." Keep "Our bishops and councils held real authority of their own, over real disputes among us." |
| violence `text` | "A modern reader may miss something here." is a signposting sentence with no content of its own, a mild assistant-voice cadence. This came from round 1's own proposed text. | P2 | Delete it. The next sentence, "Our bishop did not answer this way because he thought little of it.", stands alone. |
| almsgiving `positions[0]` | Unchanged field. It still opens "We had rich members.", the wording round 1 flagged in `text`. The two fields are now inconsistent. | P2 (flag only) | "Some among us were rich." |
| heard-for-salvation `positions[0]` | Unchanged field. "Augustine taught this directly" has no antecedent for "this", because the opener it once followed is gone. | P2 (flag only) | "Augustine taught directly on prayer that goes unanswered, from the apostle Paul's own words." |

I found no new AI tells beyond the violence signpost, and no lost attributions or altered quotations. Sentence-length outliers in the per-field scan were checked by hand. They are artefacts of a quotation ending in `."`, not real run-ons.

## Check 4 — gates

- `python -m engine.m10.cli regate lpc`: **PASS**
- `python -m engine.m10.cli records lpc`: **PASS** (state `building`)

## Counts

- Records rechecked: 14. P1 fields rechecked: 8, all fixed. P2 fixes rechecked: 21, all applied. Quoted strings: all verbatim.
- **P0: 0**
- **P1: 0**
- **P2: 6** (4 new from round-1 proposed texts; 2 flag-only in unchanged fields)
- Round count on this review series: 2 of 3. None of the P2s is a substantial finding, so they do not justify another revision round. They can be applied as mechanical edits without a round 3.

VERDICT: Approved to proceed
