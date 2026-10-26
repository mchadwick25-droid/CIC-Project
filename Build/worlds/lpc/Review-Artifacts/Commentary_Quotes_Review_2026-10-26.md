# lpc commentary-by-passage batch (15 quotes): independent review

- Branch: `claude/lpc-next-session-2026-10-26`. The batch was uncommitted when the review began and was committed during it as `900435e2` ("lpc: commentary-by-passage batch, 15 quote records"). The review covers that commit, diffed against `7a87165a`.
- Scope: the 15 new records under `records/lpc/quote/`, their gravity edges (`wb_lpc_s25.py`, mirrored into six gravity records), canon cells (`wb_lpc_s2y_canon_cells.py`) and use notes (`wb_lpc_s2u_use_notes.py`).
- Reviewer model: Opus 5.5 (`claude-opus-5-5`).
- No repo file was modified other than this one. No command that calls a model was run.

## Gates and mechanical checks

- `python -m engine.m10.cli records lpc`: **PASS**.
- `python -m engine.m10.cli regate lpc`: **PASS** against the default base, which is now HEAD, so 0 files changed. Against `--base 7a87165a`: **PASS**. 21 record files changed, 309 fields checked, 15 new or edited, and 15 edited fields below FK 8 are reported but not failed. Every other note is a base failure that this batch did not change.
- **Verbatim, two independent methods.** Method A: Python takes the `text` field from the YAML, strips `<note>` blocks and tags, and folds whitespace. It then searches the stated NPNF line range and the whole file for the text as a substring. Method B: `sed -n a,bp` on the range, then `tr` to fold newlines, then `sed` to strip notes and tags, then `grep -cF -f` to search for the text. **All 15 match exactly once at the stated lines** under both methods. For every multi-line range, Method A also checked the range with its first line dropped and with its last line dropped. Neither shortened range holds the passage, so no range is wider than it needs to be. The notes inside ranges, at lines 1668, 1671, 3291, 3294, 9116, 14471 and 26756/26759/26762, are stripped, and each record says so.
- **Latin ranges.** I read every range in the OCR files. Each one starts on the line that holds the first Latin word and ends on the line that holds the last. Ps 136: 126347 *Qualem* to 126369 *Christus*, with the footnote block at 126357-126366 inside the range, as the record says. Ps 50: 43058 *Quisquis* to 43065 *intercludatur*. Ps 21: 12992 *Deus* to 13000 *meorum*. Ps 132: 123237 *Omnes* to 123247 *non soli audierunt*. Tr. 25: 20107 *Respondit* to 20111 *manducasti*. Tr. 123: 46148 *Sit* to 46154 *charitate*. Hom. 7: 50812 *Puerum* to 50829 *existere*. Tr. 6: 7937 *Quid* to 7945 *baptizat*. Tr. 46: 29570 *Jam* to 29578 *timor est*. Tr. 80: 37171 *Quare* to 37176 *visibile verbum*. Tr. 33: 23617 *Haec* to 23626 *in terra*. Hom. 3: 48396 *Ex nobis* to 48407 *grana non erant*.
- **The Latin claims hold.** *sanctitas Baptismi* (7941) and *proprietatem* (7939). *mango* (50813). *fiunt ad disciplinam dictante charitate* (50822-50823). *Dilige, et quod vis fac* (50824). *Sit amoris officium* (46148). *in Deum* (123244). *misera et misericordia* and *trabali telo* (23621-23623). *cibum* (20109). *Ut quid paras dentes et ventrem* (20110). *Benedictionem, Eucharistiam* (48402). *Fuga animi, timor est* and *tacet, non corripit* (29573, 29577). *Detrahe verbum, et quid est aqua nisi aqua* (37174). *agere poenitentiam* and *intercludi* (43058, 43064). *Vetus enim homo confixus cruci loquitur* (12997). *Nascentes malae cupiditates* (OCR *malx rapiditates*), *offocentur* and *elidantur* (126348-126350). The Ps 21 variants note at PL line 1156 reads *Hebr. verba rugitus mei*, as claimed. The editor's note at NPNF 14471 is quoted correctly.
- **Context claims that hold.** Sermon on the Mount II §28 on debts (2325-2330). The closing sentence of §29 on revenge (2334). §§59-61 (2860-2889). §58's opening on the right cheek and on Paul (1639-1655). Book I chapter 20 on correction out of love (1714, 1728). Tr. 25: "distinguished from works", then faith declared a work, then "Nor did He say, This is your work" (4497-4503). Tr. 80: "not because it is uttered, but because it is believed" (10115). Tr. 123: "Lovest thou me? Feed my sheep" just after the passage (13433). Hom. 3 §5: the threshing-floor sentence just after the passage, and the Donatists named in §7 (14511). Tr. 33 §5: before the passage, and §6 after it. Ps 22 §1 says "sustaining also the person of the old man" (3284). Ps 133 §2 names the Jews just before the passage (26738-26746). The ellipsis before the Ps 137 passage is at 27121. The Coxe note on the Ps 51 passage is at 9116.
- **Readability of `use_note.means`** (`engine.m1.gates.grade_text`): all 15 are one sentence of 25 words or fewer, with FK ≤ 10 and FRE ≥ 60. The highest FK is 9.995 (office of love) and the lowest FRE is 64.7 (other cheek; Peter may baptize). The old-man sentence is FK 6.9, below the grade-8 floor, which the Hub treats as reported, not failed.
- **`retrieve_when` Bible references.** All are correct in English numbering: Ps 137:9, Ps 133:1, Ps 22:1, Ps 51; Matt 5:39, 6:12, 7:1; John 1:33, 6:29, 8:1-11, 10:11-13, 15:3, 21:15-17; 1 John 2:19. The Vulgate number is given in each locus. See L-3 for 1 John 4.
- **Relations.** Each quote carries one `associated-with` edge, and the gravity record carries the inverse edge in every case. Every `prefer_instead` target exists.
- **No invented dates, places or occasions.** Every record carries the generic years 391-430. None gives a date or an occasion. The Ps 22 guard correctly keeps out the Coxe note at 3275 ("read on the anniversary of our Lord's passion").

## Records

### A1 `lpc.quote.all-sins-against-us-are-to-be-forgiven` (De serm. Dom. II §29)

The quote is verbatim, the range is tight, the cell F2-I fits, and the safety guard is present and adequate.

- **A1-1 (P2).** The rendering drops "by our Father". In the text, our Father is the one who forgives ("forgiven by our Father which we commit against Him"). In the rendering, "our sins against our Father forgiven", he becomes only the one sinned against. Proposed final sentence: `So we must admit that every sin committed against us is to be forgiven, if we want our Father to forgive the sins we commit against Him.`
- **A1-2 (P2).** The first guard says §28 "argues that 'debts' in the petition means sins". §28 says the petition covers "all ways in which any one sins against us, and by consequence in reference to money also" (2329-2330). The second guard supports its point with the sentence on revenge, which does not speak of correction. Proposed guards 1-2: `The passage does not speak of money debts; section 28, outside it, says 'debts' in the petition covers every way anyone sins against us, a withheld money debt included.` and `It does not say that forgiving means the offender goes uncorrected; section 28, just before it, allows a creditor to press gently for what is owed so as to bring the debtor to what is right.` In the lens note, replace `'Debts' in the petition, which section 28 explains, means sins.` with `Section 28, just before, explains that 'debts' means every sin done against us.`

### A2 `lpc.quote.believe-and-thou-hast-eaten-already` (Tr. in Jo. 25 §12)

The quote is verbatim, the range is right, and the rendering carries every clause. The *cibus* claim and the three guards hold. The gravity (grace-and-human-incapacity, through "the work of God") is fairly hedged in the body. No findings.

### A3 `lpc.quote.dash-the-little-ones-against-the-rock` (En. in Ps. 136 §21 PL / §12 NPNF)

The quote is verbatim, and the range and page-break note are right. "Cravings" for 'lusts' is a sound choice: *cupiditas* is desire, and modern 'lusts' would narrow it to sex. "Old, deep-rooted" carries 'inveterate' (*vetere*).

**Safety.** No guard is needed. The passage turns the verse away from violence against anyone and toward a person's own new-born desires. A frightened reader of the verse (canon F2-P-02) is served by the lens note. Present distress stays with the Facilitator's per-turn check, as for every record. No findings.

### A4 `lpc.quote.david-himself-hath-been-sent-to-thee` (En. in Ps. 50 §5)

The quote is verbatim, the range is right, and the rendering holds. "Set right" renders *correctum*, and "kept out" renders *intercludi*.

- **A4-1 (P1).** The record presents a contested reading as settled. *agere poenitentiam* is, in Augustine, the ordinary phrase for undergoing the Church's penance as well as for repenting, and the passage does not say which is meant. The divergence note reports Coxe's bracketed note as if it settled the question ("the earlier translation 'do penance' misled and was corrected"). Coxe's note calls 'do penance' "feeble" and "unjust to the author's entire system of thought", which is a 19th-century editor's judgment. The lens note then defines *poenitentia* one way only ("the turning back of a sinner to God"). With the gravity set to penitential-discipline, this tells the voice to deny a rite reading that the Latin allows. Proposed divergence_note: `The text field is the NPNF English as printed. Its 'exercise penitence' renders agere poenitentiam, which in Augustine can mean to repent or to undergo the Church's penance; the passage does not say which. An editor's bracketed note at line 9116, outside the text field, calls the earlier 'do penance' 'feeble'; that is the editor's judgment, not the author's.` Proposed last sentence of the lens note: `'Penitence' renders the Latin poenitentia, repentance; the passage does not say whether the Church's formal penance is meant.` Mark the formation_confidence on the meaning of the phrase as Contested in the body, or point to a `contested_claim` if one exists.

### A5 `lpc.quote.judge-not-nor-despair-of-a-return` (De serm. Dom. II §61)

The quote is verbatim, the range is tight, the rendering holds, and the §59-61 guards are accurate.

- **A5-1 (P1, safety).** "Nor let us so reprove ... as that we should despair of a return to a right state of mind" can be turned on someone who is being harmed now: keep hoping he will change, and do not judge him. That is the same risk the forgiveness and other-cheek records guard against, and this record has no guard. Proposed added guard: `The passage must not be used to tell anyone to keep hoping for, or to stay near, a person who is harming them now; a participant who describes present harm is the Facilitator's to answer, not the voice's.` Add `not_for`: `"a reason to stay near someone who is causing harm now"`.
- **A5-2 (P2).** Cell F6-I ("anything about your own community that troubled you / never settled / hardest true thing") does not fit a reading of Matt 7:1. Proposed: `F2-I`, as for the other Matthew commentary quote, A1.

### A6 `lpc.quote.let-it-be-the-office-of-love-to-feed-the-flock` (Tr. in Jo. 123 §5)

The quote is verbatim, and the range is right. *officium* is rightly "duty" and *indicium* rightly "mark". The rendering's five sentences carry every clause. The cell (F3-I) and gravity (pastoral-office) fit. No findings.

### A7 `lpc.quote.love-and-do-what-thou-wilt` (In ep. Jo. 7 §8)

The quote is verbatim, and the range is right. "Slave-dealer" is the plain sense of *mango*, and the divergence note gives the fawning-to-take sense. "To train and correct" for *ad disciplinam* is inside the word's range. "Love" for both *charitas* and *dilectio* is flagged in the divergence note.

**Safety.** The father-beating guard is adequate as a claim guard. See L-2 for the `not_for` list.

- **L-1 (P2).** Cell F1-I ("What did you believe about God?") does not fit a precept about the root of deeds. Proposed: `F2-I` (how they read their Scriptures, here 1 John 4).
- **L-2 (P2).** The striking guard does not appear in `use_note.not_for`, which is the short list beside the `means` sentence that names the beating. Proposed added `not_for`: `"a warrant for striking a child or anyone today"`.
- **L-3 (P2).** The first `retrieve_when` reads "participant asks about 1 John 4, 'Love, and do what thou wilt'". That attributes Augustine's sentence to the epistle. Proposed: `participant asks about Augustine's 'Love, and do what thou wilt', from his homily on 1 John 4`.
- **L-4 (P2).** The body sentence "The passage runs longer than most so that the short precept keeps the father and the boy-stealer and the sentences on the root of love." is a note about how the record was built, inside a canonical record. Proposed: delete it.

### A8 `lpc.quote.many-have-learned-to-offer-the-other-cheek` (De serm. Dom. I §58)

The quote is verbatim, and the range and the two inside notes are right. The rendering holds. Cell F2-P fits ("what might a modern reader miss"). The present-harm guard is adequate.

- **C-1 (P1).** The gravity edge to `lpc.gravity.penitential-discipline` ("the reintegration of the failed": taking back those who gave way) is not supported by the passage. Nothing in it concerns a failed member or taking anyone back. The body justifies the edge "in its form of love for the one who does harm", which is not a form that the gravity record names. The edge also ties a non-resistance text to the concern a participant reaches when asking about wrongdoing and return, which is the wrong neighbour for this passage to have. Proposed: move the edge to `lpc.gravity.preaching-and-catechesis`, as the Ps 137 exposition already has it. That means the quote's relation, the `wb_lpc_s25.py` lists and both gravity records. Replace the body's last sentence with `The passage carries the gravity lpc.gravity.preaching-and-catechesis through its teaching on the Lord's precept.` If no gravity fits, escalate the choice rather than keep this edge.
- **C-2 (P2).** Guard 1 and `not_for` 1 put self-defence, lawsuits and correction side by side. They then support only correction ("correction out of love is not forbidden"). That lets the voice imply Augustine allowed self-defence, which the passage does not address and his other writings do not support. Proposed guard: `The passage does not take up self-defence or lawsuits and must not be given as Augustine's ruling on them; later sections, outside it, say correction out of love is not forbidden.` Proposed `not_for`: `"a ruling on self-defence or lawsuits, which the passage does not take up"`.
- **C-3 (P2).** The NPNF prints "hear witness of the evil", a misprint for "bear witness". The rendering silently corrects it, and the note at 1668 gives Augustine's own reading, *Exprobra de malo*. Proposed divergence_note addition: `NPNF's 'hear witness' is a misprint for 'bear witness', which the rendering uses; the note at line 1668 gives Augustine's Latin reading, Exprobra de malo, 'charge me with the evil'.`

### A9 `lpc.quote.peter-may-baptize-but-this-is-he-that-baptizeth` (Tr. in Jo. 6 §7)

The quote is verbatim, and the range is right. "Holiness" for 'virtue' is correct (*sanctitas*). The rendering holds, and the Judas and no-Donatists guards are right.

- **P-1 (P1).** Guard 3 says the passage "does not say the minister's character is of no account" and cites §15, where "holy things can harm a person who receives them badly". §15 (1485-1490) is about the **recipient**, specifically one who holds baptism "apart from the dove". It is not about the minister. Cited this way, it lets the voice say that Augustine thought the minister's character affects the sacrament, which is the opposite of this passage ("be they righteous or unrighteous"). `not_for` 3 points the same wrong way. Proposed guard: `It speaks only of whose baptism it is; it does not say the minister's own sin is of no account to the minister. Section 15, outside it, says baptism held apart from the Church's unity harms the one who receives it; that is about the recipient, not the minister, and must not be cited for the minister.` Proposed `not_for` 3: `"a claim that the minister's own sin is of no account to him, which the passage does not discuss"`.
- **P-2 (P2).** `means` ends "since the power is his alone". 'Power' is the old sense of NPNF's 'virtue', which the record's own divergence note corrects to holiness. Proposed (20 words, FK 9.3, FRE 63.9): `Augustine says Peter may baptize, and Paul, and Judas, but it is Christ who baptizes, and the holiness is his.`

### A10 `lpc.quote.the-flight-of-the-mind-is-fear` (Tr. in Jo. 46 §8)

The quote is verbatim, the range is right, the rendering holds, and the cell and gravity fit.

- **F-1 (P2).** The lens note's "Standing at his post in body is not enough" draws on "Thou stoodest with thy body, thou fleddest in thy spirit", which is outside the passage (7237). The body describes the next sentences as "on Paul's spirit being present in his letters", but they quote Col 2:5, "absent in the flesh, yet ... with you in the spirit", and say nothing of letters. Proposed lens-note sentence: `Saying 'I am here' is not enough: fear is 'the flight of the mind'.` Proposed body clause: `so are the sentences after 'The flight of the mind is fear', which contrast standing in body with fleeing in spirit and quote Colossians 2:5.`

### A11 `lpc.quote.the-old-man-nailed-to-the-cross-speaks` (En. in Ps. 21 I §2)

The quote is verbatim, the range is right, and the PL 36 line-1156 variants claim holds. "Old self" for 'old man' is right: it is the modern rendering of Rom 6:6, which §1 cites, and the lens note glosses it. The rendering holds.

- **O-1 (P2).** The locus and body say "section 3 in the PL text". The OCR prints "3. [vers. 3.]" at 12992, but the next section, at 13002, is also "3.". The first is a misread "2. [vers. 2.]", since Vulgate Ps 21:2 is *Deus, Deus meus, respice*. Proposed: `section 2 (also section 2 in PL 36, where the OCR misprints it as 3)` in both places.
- **O-2 (P2).** `means` says "the old man", which a modern reader hears as an elderly man; the rendering already uses "old self". Proposed (22 words, FK 6.9, FRE 84.5): `Augustine says the old self nailed to the Cross is the one who cries out, not knowing why God has left him.`

### A12 `lpc.quote.the-word-is-added-to-the-element` (Tr. in Jo. 80 §3)

The quote is verbatim, the range is right, and the rendering carries every clause. The "believed, not uttered" guard holds (10115). No findings.

### A13 `lpc.quote.the-wretched-woman-and-mercy` (Tr. in Jo. 33 §5)

The quote is verbatim, the range is right, and the *misericordia* and *telum* claims hold. The guards are right: the passage stops before "Neither do I condemn thee", in §6. The gravity, penitential-discipline, is acceptable: mercy to a sinner at the moment of exposure.

- **W-1 (P2).** "But He did not stoop to watch them fall." In this scene the Lord literally stoops to write (John 8:6, 8), so 'stoop' reads two ways. *nec dignatus est cadentes attendere* is "did not deign to heed their fall". Proposed: `But He did not think their fall worth watching.`

### A14 `lpc.quote.they-first-dwelt-together-in-unity` (En. in Ps. 132 §2)

The quote is verbatim, and the range and the three inside cross-references are right. The 'thence' guard is right, since the Jews are named at 26738-26746. *in Deum* holds.

- **U-1 (P2).** Cell F3-T ("Was your church Catholic? / denominations") does not fit a passage on the first believers' shared goods. The body's "in its congregational form, not in the form of communion between bishops" claims a form that the gravity record (bishops keeping communion despite disagreement) does not have. Proposed cell: `F5-T` ("How did you look at money and poverty"). Proposed body sentence: `The passage is tied to the gravity lpc.gravity.collegial-communion-preserved only loosely: it speaks of the unity of the first believers, not of bishops keeping communion through disagreement.`

### A15 `lpc.quote.they-went-out-from-us-but-were-not-of-us` (In ep. Jo. 3 §5)

The quote is verbatim. The range and the editor's note are right, and "the blessing" for *Benedictionem* is sound. The Donatist and judgment-day guards hold.

- **T-1 (P2).** The same section, outside the passage, says that "they who haply have gone out and return, are not antichrists" and "he that changeth himself for the better, is in the body" (14472-14473). Without that, "they were not grain" reads as a final verdict on anyone who has left. The lens note's "never fully 'of us'" adds 'fully'. The `means` sentence says "those who left", but the passage speaks of many who still receive the sacraments with us. Proposed added guard: `The same section, outside the passage, says that those who went out and return are not antichrists, and that whoever changes for the better is in the body; the passage must not be used as a verdict on anyone who has left.` Proposed lens-note sentence: `He says that many who are not 'of us' share the same baptism and the same altar, and that temptation shows it, as a wind shows what was not grain.` Proposed `means` (22 words, FK 8.5, FRE 73.0): `Augustine says many who share our baptism and altar are not of us, and temptation shows it when they leave like chaff.`

## Penitential-discipline assignments (six)

- David (Ps 51): fits, as the pastoral appeal to the fallen.
- The wretched woman: acceptable.
- Love and do what you will: acceptable through *ad disciplinam*.
- Judge not: acceptable through "a return to a right state of mind".
- Forgive us our debts: acceptable, since forgiveness of the offender is the gravity's core.
- Turn the other cheek: does not fit (C-1).

Moving both Matthew quotes off F3-P was right: neither passage speaks to a church's accountability for real harm.

## Safety summary

The three present-harm guards (A1, A7, A8) are worded correctly. They hand present harm to the Facilitator and do not let the voice handle it. A5 (judge not) needs the same guard (A5-1). A7 needs the guard reflected in `not_for` (L-2). A15 needs its return guard (T-1). A3 (Ps 137) needs none.

## Verdict

**Revise.** 4 P1 (A4-1, A5-1, C-1, P-1) and 16 P2. Every finding has an exact replacement. None needs new source work. After the fixes, a targeted recheck of the changed fields is enough.
