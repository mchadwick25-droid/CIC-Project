# CO-LPC-2 Claim Corrections: Targeted Recheck, Round 2

**World:** `lpc`
**Scope:** The fixes for the 7 P1 and 10 P2 findings of `CO-LPC-2_Claim_Corrections_Recheck.md`, and only those. That covers the women's-voice wording, the new Registry licences (rows 14, 269, 270, 280, 302), the rewritten `lpc.gravity.sacramental-ordination-validity` description, the realigned generator scripts, and the 6 new UNVERIFIED Claims Register rows.
**Authority:** System Hub Decision Log, "Cap ruling: lpc CO-LPC-2, a second recheck after its seven P1 findings" (2026-10-24). This file is the one review that ruling covers.
**Reviewer model:** Opus 5.5 (`claude-opus-5-5`) for the whole run. No fallback to another model occurred.
**Date:** 2026-10-24
**Inputs:** the uncommitted `git diff` across 31 files; the round-1 findings; the cited `cic/texts/` lines, each read directly.

**Gates run:** `python -m engine.m10.cli regate lpc` gives PASS: 10 new or edited fields, no regression. `python -m engine.m10.cli claims lpc` gives PASS: 98 derived, 98 registered, 6 UNVERIFIED. `tools/check_live_commentary.py --surface records` reports no `lpc` hit.

Severity: **P0/P1 block**. P2 does not block.

---

## 1. The seven round-1 P1s

### P1-1. f9dafd30: the one-locus claim at four more sites

Fixed at all four sites: Doc_04 line 111 ("Not thin the way Candidate 5 is — argued at length in two independent bishops' own extended treatments"), World Profile line 126, Phase 2 line 64 and Phase 1 line 96 ("each theory in one bishop's own voice"). The sweep for "one locus", "one attested locus", "at one locus" and "confined to one" across `Build/worlds/lpc/` and `records/lpc/` finds no leftover. The one hit is Registry row 1, which uses "this one locus" about a numbering error and is unrelated. The Gapped Formation Precedent keeps the claim as received and is logged at OG-62. True at source: Epp. LXXI, LXXII and LXXV (ANF05 lines 38405, 39018, 40604) each state the freedom of each bishop's judgment. **Closed.**

### P1-2. a187ea83: the rite-wording construction note (Doc_05 line 165)

Doc_05 line 165 now carries the reviewer's text word for word. I checked each item at source:
- the signing and salt: *Confessions* I.11, `npnf101` lines 4429–4431, "signed with the sign of the cross, and was seasoned with His salt";
- the creed handed over and given back: `lpcctx001` lines 34 and 44;
- the interrogation: ANF05 line 38062;
- the renunciation: `npnf108` line 17698;
- the anointing and laying on of hands: `lpcctx003` lines 27–29 and 39;
- *On Baptism* V.20.28 (`npnf104` line 13058), "when he is baptized, he is questioned about the Church".

The note no longer denies what the chunks verify, and it drops the false "each attested in its own phase only". A sweep for "gestures", "fixed spoken exchanges" and "in its own phase only" finds no other site. **Closed.**

### P1-3. 77d40657: grace, "no Cyprian-phase evidence", at nine sites

All nine sites are fixed with the proposed text, or with a close variant of the same claim:
- Doc_04 lines 131, 132 and 169;
- Doc_05 line 209;
- lpclex007 line 63;
- `lpc.term.grace` `senses.evidential`;
- World Profile line 140;
- Phase 2 line 58;
- Phase 3 line 55.

Doc_04 line 135 also drops "not a gap in the search". The sweep finds none of these phrases left: "Pelagian-anthropology-equivalent", "no Cyprian-phase evidence", "not a gap in the search", "anywhere in Cyprian's corpus". One phrase in `wb_lpc_s25.py` line 855 reads "no Cyprian-phase evidence of it organizing formation is identified". It is the already-corrected grace-gravity divergence note, and it is true. The *Testimonies* III.4 quotation ("That we must boast in nothing, since nothing is our own", ANF05 line 53424) is word for word. **Closed.**

### P1-4. 48fee228: no Registry licence for *Answer to Petilian* §§202–205

The licence is fixed at all four sites:
- **Row 14** now licenses "those two loci only". Its Verification cell adds "Book II, chapter 93 (sections 202–205) directly verified ... lines 17610–17726".
- **Row 280** now says "two loci" three times.
- **Row 302** says "one of the two loci", and it is accurate that only §118 was compared with the Latin.
- **Doc_02 line 29** names both claims.

I checked each quotation in `npnf104`:
- "has never found anything save envy" is at line 17610 (§202);
- "certainly no foe to the name of Christian, but rather rendered glorious by it" is at §205 (lines 17719–17727);
- chapter 93 opens at line 17608, and §206 starts at line 17728.

The range 17610–17726 holds §§202–205. The quotations are word for word. The generated source record (`wb_lpc_s21.py`) carries the same two-locus divergence note. **Closed.** One P2 follows below (N4).

### P1-5. 31abcdcc (a): "twice" at World Profile lines 428 and 652

Both lines are fixed with the proposed text, and so is Phase 2 line 33 ("attested more than once"). A sweep for "attested twice" finds no leftover. The remaining hits for "twice" in the world are about G6, the font question answered twice, which is a different and true claim. **Closed.**

### P1-6. 31abcdcc (b): "the only one that engages Cyprian's conciliar acts"

The phrase now reads "the only one in which this world itself reads and answers" at all five sites:
- Doc_08 lines 191 and 302;
- Force Index line 91;
- World Profile line 366;
- the 2B-4 force record ("Cyprian's council acts").

No copy of "that engages" or "takes up Cyprian's council" is left. **Closed.**

### P1-7. 94dc0428: the women's-voice wording

See §2. **Closed.**

---

## 2. Women's voice

**Sites checked:** `records/lpc/honest_limit/lpc.limit.womens-own-voice.md` (`statement`, `why_sources_cannot_answer`, body); Doc_09 §7 item 4 (line 125); World Profile lines 620 and 622; Registry rows 269 and 270.

**At source.**

*Passio Montani et Lucii* 8. In Knopf-Krueger it runs from line 5771 to line 5785. In Gebhardt it runs from line 7655 to line 7690. The two printings agree:
- "sorori nostrae Quartillosiae hic nobiscum positae ... cuius mulieris et maritus et filius ante triduum passi erant": she is held with the martyrs, and her husband and son suffered three days before;
- "quae in hunc modum quod uidit exposuit. Vidi, inquit, filium meum, qui passus est, uenisse huc ad carcerem": she tells the vision herself, in the first person.

The quotation "Vidi, inquit, filium meum" is word for word in both files. Gebhardt's OCR prints "?Vidi". Each paraphrase is faithful:
- "held in prison with the martyrs";
- "three days after her husband and son had been put to death";
- "her son, who had suffered, coming to the prison".

Is she unique? I searched the three Cyprianic acts for other women's speech. Marianus's mother rejoices without speaking (Knopf line 5598). Flavianus's mother speaks only inside his own vision (line 6162). Quartillosia is the one woman who narrates. Neither text claims she is the only one, but the reading holds.

**Monica.** The *Confessions* (Registry row 9, Native) set down Monica's direct speech:
- "Son, for myself, I have no longer any pleasure in aught" (IX.10.26, `npnf101` line 14147);
- "Here ... shall you bury" and "Lay this body" (IX.11.27, lines 14185–14192).

That is the same kind of evidence as Quartillosia's: a woman's words set down by a man, not a text she wrote. The new wording survives it:
- The record's spoken `statement` says "Now and then a woman's spoken words reach us, set down by men."
- The record's `why_sources_cannot_answer` gives Quartillosia as an example ("such as"), not as the only case.
- Doc_09 and the World Profile say "One martyr text reports", with no "only".
- World Profile line 620's "not one of them speaks in her own words" covers the named list, which leaves Monica out on the ground Doc_02 §6 gives at line 110.

No sentence is falsified. A P2 below (N6) suggests naming her.

**Is the limit still honest?** Yes. The claim is now about authorship: "No text a woman wrote herself survives". That is true:
- The corpus map and the Registry's Native rows hold no work by a woman.
- Perpetua's own narrative is out of boundary (rows 204 and 282).
- The Paulinus and Therasia letters are in Paulinus's first person.

The limit is not erased. It still says what the record lacks, a body of women's writing, in both phases. It is not overstated. It names Quartillosia's voice, and the record's `statement` also admits other reported words ("now and then"). "Almost always in someone else's words" is the right hedge. Doc_09 adds that "no story here is built from it", which is true and keeps the story inventory consistent with its heading.

**Voice.** The `statement` stays in the world's own first-person plural ("our own record", "reach us", "from us"). It does not hedge in academic phrasing. It names no build process. Nothing in it reads as generated. Line 622 of the World Profile ("We can tell you what happened ... That is one voice, set down by men") is in the same voice.

**Readability**, scored with the engine's own grader (`engine.m1.gates.grade_text`):

| Field | FK | FRE | Result |
|---|---|---|---|
| `statement` (spoken) | 8.9 | 68.7 | Passes |
| World Profile line 622 ("How the Representative handles it") | 8.5 | 72.9 | Passes |
| Doc_09 line 125 | 9.6 | 61.3 | Passes |
| `why_sources_cannot_answer` | 11.4 | 51.6 | Not a compiled field (`engine/m1/gates.py` comment at line 774), so the bar does not apply |
| World Profile line 620 (Ecological basis, builder-facing) | 11.0 | 55.3 | Most of the score comes from the unchanged opening sentence |

No finding blocks. Five P2s follow.

- **P2 (N1). Two spoken sentences run past about 25 words.** CLAUDE.md asks for nothing past about 25 words. The FK/FRE gate passes.
  - Sentence 1 (31 words). Current: "No text a woman wrote herself survives from us, in our early years or our later ones, and that is not because one half of our record is thinner than the other." Proposed: "No text a woman wrote herself survives from us, in our early years or our later ones. That is not because one half of our record is thinner than the other."
  - Sentence 2 (35 words). Current: "Quartillosia was held in prison with the martyrs, three days after her husband and son had been put to death, and she told what she saw: her son, who had suffered, coming to the prison." Proposed: "Quartillosia was held in prison with the martyrs. Her husband and son had been put to death three days before. She told what she saw: her son, who had suffered, coming to the prison."
  - The same change goes in `wb_lpc_s28.py` `build_limit_womens_own_voice`.
- **P2 (N2). The record's `sources` list does not carry the text its `statement` now names.** `sources` still lists only the Cyprian Epistles and the Augustine correspondence. No `lpc.source` record exists for Registry rows 269 and 270. The claim can still be traced through `why_sources_cannot_answer`, which gives the file, the lines and the Registry rows, and `statement` is the only field the compiler reads (`engine/m2/builders.py` line 94). So this does not block. Proposed: add a source record for the *Passio* of Montanus and Lucius (row 269) and list it here, or log the gap in `Open_Gaps_Tracking.md`.
- **P2 (N3). The line ranges are a little short.** Chapter 8 runs to line 5785 in Knopf, not 5783. In Gebhardt it runs from line 7655 to line 7690, not 7654–7677. The quoted words and every paraphrased detail fall inside the cited ranges. Proposed: "lines 5771–5785" at the record, Doc_09, the World Profile, Registry row 269 and `wb_lpc_s28.py`; "lines 7655–7690" at rows 269 and 270. Row 269 also licenses wording "once a passage is checked against the printed page". The check was made against the two editions' text layers. Proposed: say so in the Verification cell ("checked against the text layers of both printings; the page scans were not viewed").
- **P2 (N5). `wb_lpc_s28.py` module docstring, lines 88–99.** It still cites "Doc_09 §5 item 4", quotes "none is audible", and ends "A woman's own first-person narration is attested in neither." That statement is false against Quartillosia. It is not emitted into any record. But `Build/worlds/` is a canonical surface, so it should go. Proposed: replace the last sentence with "No text a woman wrote herself survives in either phase; one woman's first-person account of a vision is reported in the *Passio* of Montanus and Lucius 8", and change "§5" to "§7".
- **P2 (N6, optional). Name Monica beside Quartillosia.** Proposed: in `why_sources_cannot_answer`, after "such as Quartillosia's account ... ", add "and Monica's words in the *Confessions* IX.10–11, which Doc_02 §6 sets aside as pre-clerical formation narrative". Then a builder who meets her will not read the record as having missed her.

---

## 3. Registry row 14, plus rows 280 and 302

Covered at P1-4 above. One P2 follows.

- **P2 (N4). Row 14's date cells do not record the new locus.** "Added by / Date" still reads "locus added 2026-09-25". "Last verified" names only chapter 51 (2026-09-25). Proposed: append "; Book II, chapter 93 (sections 202–205) added 2026-10-24" and "; Book II, chapter 93 (sections 202–205): direct verification against the same file / 2026-10-24".

---

## 4. `lpc.gravity.sacramental-ordination-validity` description

I compared it paragraph by paragraph with the earlier text. Every claim survives, in plainer words:
- the question's centrality and the two opposite answers;
- the three loci of recurrence;
- the two independent bishops, decades apart;
- the dependencies on collegial communion and on the confessor tension;
- the practical effects: rebaptism policy, Donatist clergy received in their orders, the Stephen–Cyprian break, the Donatist appeal to Cyprian;
- persistence across the phases;
- the four gravities it reinforces;
- the cited loci (On Baptism I.1.2, the 256 preface, Book III ch. 2);
- the Donatist pressure and the one-way link to penitential discipline.

One change is deliberate. "Unlike conciliar authority, it is not confined to one source" becomes "Unlike conciliar authority, it is not thin". That carries P1-1's correction into this record and agrees with Doc_04 line 111. No new claim is added. FK 7.9, FRE 60.2. The FK score is just under the band floor of 8, which is reported and does not fail. The FRE score only just clears 60. The voice is plain and in register. "A close cousin of it" is informal, but it is clear.

- **P2 (N7).** "all through Augustine's On Baptism, a whole book on the question" could be read as one book. *On Baptism* has seven books. Proposed: "all through Augustine's On Baptism, seven books on the question".

---

## 5. The ten round-1 P2s

All ten are applied:

| Round-1 P2 | Where | Applied |
|---|---|---|
| Possidius line cite | Doc_02 line 59 | "lines 35938 and 36299–36301" |
| Ep. LXXI is synodal | Doc_04 line 90 | "each in his own voice or his council's". Also carried to the conciliar gravity record, "the letter he and his council sent to Stephen", which is true: Ep. LXXI speaks as "we" (ANF05 lines 38395–38405) |
| Faction picture | Doc_07 line 126 | "The faction picture is a real distortion" |
| Lens table | Doc_05 line 69 | "most visibly" |
| Grammar slip | transmission force record | "The concern with grace and human incapacity shapes only the second" |
| `retrieve_when` | constantine witness | "the Constantine sub-question of the four, which our own record answers" |
| Repetition | lpcstory003 line 33 | "he survived the fire, and he had not wanted to" |
| 2A-4 a second strand | Doc_08 line 191 | Reviewer's text, word for word |
| Build narration | 2B-4 force record | "This placement was checked, not simply inherited." deleted |
| Prosper | `lpc.figure.possidius` | "adds that he was still answering Julian, but says nothing of the sickroom". True at `prosper_chronica-minora-1-lat_mommsen1892.txt` lines 54206–54212 |

The Possidius figure's new exclusivity claim ("its only witness to the sickroom") is registered as 093c21bd and checked in §7.

---

## 6. Scripts

I reran the pipeline in a scratch copy: `records/lpc` from HEAD plus the working `Build/worlds/lpc`, outside the repo. I ran `wb_lpc_s21`, `s22`, `s24`, `s25`, `s26`, `s27`, `s28` and `s2y_canon_cells`. `s2z_canon_closure` refuses to write, by its own guard. I then compared all 310 output records with the working `records/lpc`, as parsed front matter plus body, with whitespace normalised. **0 content differences** in every record a script writes. The one difference, `lpc.witness.constantine-did-not-corrupt`, is a record no script writes; it is hand-maintained, and the scratch copy kept the HEAD version.

So each script edit emits exactly the corrected record text. No script adds a claim the records do not carry.

A grep of the script files for the old false phrases finds none in an emitted string:
- "Pelagian-anthropology-equivalent";
- "that engages Cyprian";
- "None of them is audible";
- "one attested locus";
- "attested twice";
- "corroborates only";
- "placement was checked".

The only leftover is the s28 docstring (N5). The large s22 and s24 diffs realign the scripts to records already in the repo. Examples are the added relations, `src(17, ...)` and the shortened bodies. They change no record content, as the comparison shows.

---

## 7. Claims Register: the 6 UNVERIFIED rows

Each row was checked at source per `Claims_Register_Template.md`. The completed rows are at `/tmp/claude-0/-home-user-CIC-Project/9b5d8278-a95d-517b-9c50-6f34185a4ec1/scratchpad/claims_D_done.md`. Each has 7 columns, with `id`, `file` and `claim` unchanged, and every cited path exists.

| id | File | Status | Basis |
|---|---|---|---|
| 315f173a | Doc_05 | JUDGEMENT, Widely Accepted | The three context chunks and Doc_02 §5 and §9 items 2 and 9; see P1-2 |
| fd53672d | honest limit, `why_sources_cannot_answer` | JUDGEMENT, Widely Accepted | Corpus map and Native rows: no work by a woman; see §2 |
| 34cb6f76 | Doc_09 | JUDGEMENT, Widely Accepted | Doc_02 §6 line 110 names women; same authorship reading |
| 093c21bd | `lpc.figure.possidius` | JUDGEMENT, Widely Accepted | Prosper lines 54206–54212 read. Possidius, *Vita* 31 (Weiskotten lines 4890, 4916–4928), is the corpus's one deathbed account |
| 34026208 | honest limit, `statement` | JUDGEMENT, Widely Accepted | Same reading, which holds in both phases |
| 56b6171b | World Profile | JUDGEMENT, Widely Accepted | Same reading |

- **Completed: 6 of 6. False: 0.** These are JUDGEMENT rows because "no text a woman wrote" and "only witness" rest on reading the corpus listing, not on a string search.

## No new error

I read every changed sentence in full. No sentence is broken. No new process narration is added, and one piece is removed. Two new exclusivity or absence claims appear: "no text a woman wrote herself" (at four sites) and Possidius's "only witness to the sickroom". Both are registered and true. Every quotation added in a spoken or builder-facing field is word for word: "Vidi, inquit, filium meum", the two Petilian phrases, and *Testimonies* III.4.

---

## Counts

- Round-1 P1s closed: 7 of 7. Round-1 P2s applied: 10 of 10.
- **P0: 0. P1: 0.** P2: 7 (N1–N7; N6 optional).
- Claims Register rows completed: 6 of 6, none false.
- Gates: regate PASS; claims PASS; live-commentary check, no `lpc` hit. Script pipeline: 0 content differences.

VERDICT: Approved to proceed
