## Council profiles, era 7 batch 2, round 3: Part D (Colloquy of Poissy 1561)

**Council.** `colloquy-of-poissy-1561`
**Files rechecked.** `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era7/colloquy-of-poissy-1561.brief.txt`, `audio/colloquy-of-poissy-1561.audio.txt`, `colloquy-of-poissy-1561.entry.json`, `records.json` key `colloquy-of-poissy-1561` (113 claims, 12 contested claims, 7 absent details; equal to `working/records_colloquy-of-poissy-1561.json`, checked by script), and the README "Colloquy of Poissy (about 2:30)" line. Scope: `git diff 7ad6d2a2 HEAD` for this council only, against `R2_recheck.md` Part D and `R2_changes.md` Part D.
**Brief.** 400 words by `wc -w` (2:30 at 160 wpm). `grade_text`: FK 7.50, Flesch 65.65. Longest sentence 25 words ("In January 1562 a royal edict ...", unchanged). No sentence over 25 words.
**Audio.** Equals the brief with `[calmly] ` at the start and `[warmly] ` before the last paragraph, and no other tag (checked by stripping the two tags and diffing: identical).
**Reviewer.** Fresh Opus, full effort. Read and grep only; no repo file edited; no model, network or paid calls. Scratch copies at `/tmp/claude-0/-home-user-CIC-Project/af34472b-cc0a-504c-a9aa-6aa7f1f6ba1a/scratchpad/poissy_r3/`.

Abbreviations as in rounds 1 and 2 (HE1, AYM, LAI6, LAI8, PAL1, SARPI, WAT).

## Verdict: REVISE (1 blocking, 0 substantial, 0 minor)

Round 2 fixed Sarpi's label. He is now "the Venetian friar Paolo Sarpi, hostile to the papal court", which matches the batch. But the fix kept the frame "The Catholic side speaks through Jesuits ... So do two historians of Trent". That frame now says outright that a witness hostile to the papal court speaks for the Catholic side. At Poissy that side was the prelates and the pope's legate. Sarpi's own Poissy chapter does not speak for them (D3-B1). The fix is word-neutral and keeps the brief at 400 words.

The "two meetings" change holds, in both the brief and the entry. Every other round 2 fix is closed and right, and every changed quote is verbatim.

## Round 2 findings

| ID | Status | Evidence |
|---|---|---|
| D2-S1 | PARTLY CLOSED; see D3-B1 | The label is closed. Brief p.2: "the Jesuit Sforza Pallavicino and the Venetian friar Paolo Sarpi, hostile to the papal court." It matches Regensburg and Trent ("The Venetian friar Paolo Sarpi was hostile to the papal court"). The appositive sits right after Sarpi's name, so it attaches to him alone. New `claims[112]` holds "hostile": SARPI l.8828-8830, "the See of Rome ... exorbitant power, mounted from ſmall beginnings by divers degrees unto an unlimited exceſs, it hath ſo eſtabliſhed and confirmed the fame". That is Sarpi's own opening judgment, and the claim renders it faithfully. Not closed: the side. "So do" still puts him in "the Catholic side speaks through". The finding's own heading was "a side that is not quite his". |
| D2-M1 | CLOSED | Entry `calledBy`: "Her two meetings 'à deux divers jours' fit the sessions Polanco dates to 24 and 26 September." (17 words). The quote is verbatim: AYM l.25545-25546, "de deux Communications qu'ils a voient faites à deux divers jours". "Her" is fair, because the letter says she thought it good that the prelates meet the ministers (l.25539-25543), and `calledBy` is about who called them. "Fit" keeps the identification as the profile's own. The dates check out. Polanco's letter of 27 September gives "El miércoles passado" (LAI6 l.3606-3607; the editors' note 4 reads "Id est 24 Septembris 1561", l.3634), and "El viernes siguiente, que fué ayer 26 de Setiembre" (l.3653). Records `claims[67]` agrees. |
| D2-M2 | CLOSED | `claims[81]` witness is now "l.9099-9102; for "canonists", l.7353-7358, 9761-9762, 10501-10502". The corrected range is right. l.9761 ends "the" and l.9762 begins ")nists, Boncompagno, Fachenetti, Paleotto, Lancellotto". l.7353-7358 gives Simonetta "his intimate acquaintance with canon law", with the four assistants. l.10501-10502 gives "Castagna ... one of the most able canonists of his day". The entry is unchanged. |
| D2-M3 | CLOSED | Entry `traditions` (the-society-of-jesus): "It came in as a college, not a new order, on condition it take another name." Source: LAI8 l.39603-39605, "par forme de collége et non de religión nouuellement institutée, á la charge qu'ilz seroient tenuz prandre aultre tiltre que de société de Jésus ou de Jésuites". The condition is now told as a condition. |
| D2-M4 | CLOSED | All four cuts are in place: "refectory", "directed it", "to give the ministers a safe-conduct and a hearing" and "spoke to the queen". The rendering in P3 is faithful to HE1 l.25997-25998, "auroient faufconduict pour l'y trouver, & y eftre ouis". "The History says" still sits on the aim in the next sentence. No witness tag was orphaned. "Italian" stays in the entry's `record`. |
| P7 observation | CLOSED | Brief p.7: "Catherine wrote that two meetings bred disputes upon disputes, far more than union." Source: AYM l.25545-25548, "de deux Communications ... Confufion de Difputes fur Difputes nourries de Diffencions & Difcordes beaucoup plus que d'Union". This is now limited to the two meetings, which come before the five-and-five in her letter ("je m'advifé de faire effiier fi par cinq ou fix", l.25550-25551). The sentence is faithful and adds nothing. It agrees with `calledBy` and with `outcome`. |

## New findings

### Blocking

**D3-B1. Blocking (a witness given a side that is not his, in the brief; from the D2-S1 fix).** Brief p.2: `The Catholic side speaks through Jesuits who came with the pope's legate. So do two historians of Trent, the Jesuit Sforza Pallavicino and the Venetian friar Paolo Sarpi, hostile to the papal court.`
- "So do" makes both historians voices of "the Catholic side". In this brief that side is the prelates who stood with the pope's legate against the Reformed, the counterpart of "It tells the Reformed side". The new appositive now tells the listener that the same man was hostile to that side's head. As written, the sentence puts an anti-curial writer in the papal party's mouth. Pallavicino's whole book was written to refute him as "un'istoria falsa" (PAL1 l.1).
- Sarpi's own Poissy chapter does not carry the prelates' case. He gives the Chancellor urging the bishops "not to be averſe from the Proteſtants, who were their Brethren" (SARPI l.42805). He has Tournon rise "full of -difdain" (l.42840). On the one point the brief takes from him, he says Beza spoke "with ſuch heat, that bogeve [OCR for "it gave"] ill fatisfaction to thoſe'of his vwis [own] party ; ſothat he was command.ed to conclude" (l.42836-42838). That detail runs against the History, but Sarpi gives it as Beza's own party's displeasure, not as a Catholic charge.
- He is a Catholic witness, and his side is "Catholic but hostile to the papal court" (entry `record`, D-S5). The pattern asks that a partisan witness carry his own side (Pattern C1; review_brief_r1 Severity: "a claim given to the wrong witness ... or anything else wrong or misleading in the brief"). The README's new reason, "each Catholic witness with his own side", promises the same thing. In batch 1, the blocking point after round 3 was a round 2 fix that overstated its witness. This fix is the same kind.
- Fix, brief p.2 (replace these two sentences; they are 12 + 21 = 33 words now, and become 18 + 15 = 33): `The Catholic side speaks through Jesuits: those with the pope's legate, and Sforza Pallavicino, a historian of Trent. Another historian of Trent, the Venetian friar Paolo Sarpi, was hostile to the papal court.`
  - The second sentence matches the batch label word for word ("The Venetian friar Paolo Sarpi was hostile to the papal court"). "Another" claims no count of Trent's historians.
  - Pallavicino keeps "Jesuit" through the colon. "Those with the pope's legate" are the same Jesuits as before.
  - Apply the same change to `audio/colloquy-of-poissy-1561.audio.txt` (regenerate with `mkaudio.py`).
  - No entry or records change is needed. `record` already places both men, and `claims[110]` and `[112]` hold Sarpi's order and stance.
  - The README line stays true and needs no change.
- Checked on a scratch copy: 400 words (2:30), FK 7.58, Flesch 65.01, longest sentence 25 words (unchanged). The new sentences are 18 and 15 words.

### Substantial

None.

### Minor

None.

## Verified

- Every changed brief string, read against its source in context: p.1 "refectory" (HE1 l.27648); p.2 "directed it" (Reuss's view unchanged); p.2 the Sarpi sentence (see D3-B1); p.3 safe-conduct (HE1 l.25997-25999); p.5 Laínez on 26 September (LAI6 l.3653); p.7 "two meetings" (AYM l.25545-25548).
- Changed or added quotes, verbatim: "à deux divers jours" (AYM l.25546); "exorbitant power" (SARPI l.8829, in `claims[112]`); "canonists" (WAT l.10502). The French in D2-M3 is unchanged and matches LAI8 l.39603-39605.
- Translations and renderings: `claims[112]`, "the council confirmed the 'exorbitant power' of the See of Rome", is faithful to SARPI l.8826-8830. In that passage Rome feared the council as a means to moderate its power, and the council "eſtabliſhed and confirmed the fame". `claims[67]` adds nothing to the letter: the identification is marked as fitting Polanco's dates.
- Records: the working file equals `records.json`. `claims[112]` was appended, so no index moved. The shared fields (`claim`, `witness`, `witness_kind`, `formation_confidence`) are present.
- Entry sentence lengths in the changed strings: `calledBy`'s new sentence is 17 words; the Jesuit note's new sentence is 15. None is over 25.
- Audio equals the brief apart from the two tags.
- README line: "so its standing must be placed, and each Catholic witness with his own side". It is true of the brief once D3-B1 is applied. The time "about 2:30" is true at 400 words.

## Searches run

No new absence is asserted in the changed text. Reads and greps for the points above:
- SARPI l.42760-42900 (the whole first-session passage); `grep -n` for "Brethren, repe|fatisfaction to thoſe|full of -difdain|ed to conclude" (hits l.42805, 42837, 42838, 42840); l.8818-8838.
- AYM l.25530-25560 (the body of Catherine's letter).
- LAI6 l.3595-3656 (Polanco's postscript, the editors' notes on the days); `grep -n -i "miércoles|viernes"`.
- LAI8 l.39598-39606.
- WAT l.7352-7359, 9097-9103, 9759-9763, 10500-10503.
- PAL1 l.1 (title).
- The era 7 briefs: `grep -o` for Sarpi sentences and `grep -n` for "speaks through|Catholic side" (label and framing comparison).

## Counts

Round 2 findings: 5 (D2-S1, D2-M1 to D2-M4), plus the P7 observation. 4 are closed (D2-M1 to D2-M4), and the observation is closed. 1 is partly closed (D2-S1): the label is fixed, the side is not, and this carries into D3-B1.
New: Blocking 1 (D3-B1). Substantial 0. Minor 0.
Brief: 400 words (2:30) now; 400 words (2:30) with D3-B1, FK 7.58, Flesch 65.01, longest sentence 25 words.
