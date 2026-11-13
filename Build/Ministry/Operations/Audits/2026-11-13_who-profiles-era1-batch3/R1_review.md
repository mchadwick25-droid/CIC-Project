# R1 review: four Who profiles, era 1 batch 3 (Church Family Tree)

Reviewer: independent, first sight of these drafts. Bar: `Who_Profile_Pattern.md` review checklist 1 to 14, the outside-witness and common-name sections, Mark's converged card order; `CLAUDE.md` "Trust and source fidelity" and "Accessible and rigorous"; and the batch 1 and batch 2 R1 findings (same folder, 2026-11-12), so the same bar is applied and their failure modes are checked. I did not edit the drafts. I made no paid or model-API calls of any kind; readability and quote search were run with local scripts only.

Profiles: `peter-of-alexandria` (MAJOR), `anatolius-of-alexandria-and-laodicea`, `polycrates-of-ephesus`, `pliny-the-younger` (outside witness). Per the README, Mark confirmed the major marks on 2026-11-13: Peter is major; the other three are not. Pliny is a Who as an outside witness (Mark, 2026-11-12, Open-Gaps 233).

Method. Every quotation in the briefs and cards was searched in the vendored file with whitespace-tolerant matching (`wsf.py`, loose mode on OCR files), judged against the rendered text (tags/notes removed, OCR line-breaks and curly apostrophes ignored), and read in context with translator and editor notes nearby. Every factual sentence in each brief was checked against the passage it rests on. I grepped the whole of `cic/texts/` before passing any "only" / "alone" / single-witness line, and before passing each contested point I located both named sides. Readability came from `engine.m1.gates.grade_text`, run locally. Length assumes 162 words a minute. Line numbers point to the vendored files under `cic/texts/`.

## Applies to all four

- **Audio = brief.** Each audio script is byte-identical to its brief once `[calmly]` and `[warmly]` are removed (confirmed by `diff`). Each opens with `[calmly]`; each carries exactly one `[warmly]`, sitting immediately before the closing sentence. No tags appear in any brief or card. Item 13 passes everywhere.
- **Readability.** `grade_text` passes for all four (FK at most 10, Flesch at least 60). Peter sits closest to the floor (Flesch 60.2), as batch 1's Eusebius did.
- **Card order.** All four cards are in Mark's converged order (name, otherNames, [label], knownFor, dates, place, tradition, role, briefLength, keyWorks, legacy, uncertain, sources). `keyWorks` is three for Peter and fewer for the rest (never over three). No card has a "links on the map" field; a missing field is left absent. Each card's `uncertain` opens with the brief's own caveat, as the pattern asks.
- **Outside witness.** Only Pliny carries `label` "Outside witness" and `tradition` "Outside the church"; his `legacy` has no "traces" part, which is right for a reporter. The other three carry no label and keep their tradition. As in batch 1 (Josephus M8) and batch 2, the JSON places `label` after `otherNames` rather than literally "beside the role"; this is rendering-dependent and reported, not blocking (Pliny M1).
- **Length.** Peter 405 words / 2:30, exactly at the major cap (2:30, about 405). Anatolius 325 / 2:00, Polycrates 320 / 1:59, Pliny 310 / 1:55, all within the non-major 2:00. `briefLength` on every card matches its brief.
- **List lines (item 14).** The drafts carry no list lines; these belong to the map Who build, as in batch 1 and 2, and were not verified on the site here. Every subject passes the Who test (Peter, Anatolius and Polycrates each have a body of work and a following; Pliny is a governor reporting officially, not a polemicist, and is labelled an outside witness per Mark's ruling).

| Profile | Words (wc / regex) | Est. length @162 | FK | Flesch |
|---|---|---|---|---|
| Peter of Alexandria (MAJOR) | 405 / 405 | 2:30 | 8.2 | 60.2 |
| Anatolius of Alexandria and Laodicea | 325 / 325 | 2:00 | 7.7 | 64.1 |
| Polycrates of Ephesus | 320 / 321 | 1:59 | 7.7 | 63.9 |
| Pliny the Younger (outside witness) | 310 / 310 | 1:55 | 8.0 | 61.6 |

---

## 1. Peter of Alexandria (MAJOR)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS |
| 2 | Quotes verbatim | PASS |
| 3 | No invention (esp. no invented family) | PASS |
| 4 | Reading aids | PASS, with a minor dispute opener (M1) and one borderline-long sentence (M3) |
| 5 | No role for a witness | PASS (McGiffert, Hartranft, Robertson, Coxe, Maffei all named) |
| 6 | Partisan witness named and marked | PASS ("Athanasius ... was an enemy of the Meletians") |
| 7 | Contested shown both sides, not settled | PASS (the schism origin) |
| 8 | Common names placed | PASS |
| 9 | One term | PASS |
| 10 | Story, scene, in-place disputes, length | PASS (major, 2:30) |
| 11 | grade_text | PASS |
| 12 | Card order and caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | List line; Who test | PASS (Who; list line not checked here) |

**Quotes** (all exact against the rendered text)
- "in parishes having no manner of connection with thee" — exact (anf06 l.16724, four bishops' letter).
- "the honour of our great bishop and father, Peter" — exact once the two embedded editor notes are removed; the main text reads "...our great bishop and father, Peter," (anf06 l.16750).
- "hold no communion with him, until I meet him in company with some wise and discreet men" — exact (Peter's letter, anf06 l.27802).
- "a divine example of a bishop" — exact (Eusebius HE VII.32, npnf201 l.47994).
- "for no cause and quite unexpectedly" — exact (same line, npnf201 l.47994, HE IX.6).
- "the fourth passover of the persecution" — exact (Canon I, anf06 l.26607).
- "for the safety of their life" — exact (Canon XIII, anf06 l.27537).
- "and among the rest of offering sacrifice to idols" — exact (Athanasius, Apol. c. Arian. 59, npnf204 l.24779).
- "need not be taken very seriously" — exact (Bell 1924 l.3155; Bell applies it to the sacrifice charge, as the brief does).
- "spurious and historically quite worthless" — exact (McGiffert's note on The Genuine Acts, npnf201 l.43252).
- "a nominal dignity" — exact (Socrates's text of the Nicene synodal letter, npnf202 l.3211).
- "from the times of the blessed Peter, Bishop and Martyr" — exact (Athanasius, npnf204 l.22464).
- Card "one of the most excellent teachers of the religion of Christ" — exact (npnf201 l.44801). "the day in which the memory of the martyr and bishop Peter was celebrated" — exact (Socrates I.15, npnf202 l.4008). Dupin's "more judicious or more equitable" — exact (Coxe quoting Dupin, anf06 l.28223). Robertson's "deserve little credit" — exact (npnf204 l.1684, of the Arius tales).

**Narrative checks**
- The opening prison scene matches both the anonymous account appended to the four bishops' letter and Bell. "An old account kept with the letter says Meletius never answered" = "After receiving and perusing this epistle, he neither wrote any reply nor repaired to them in the prison" (anf06 l.16830 region, headed "The Conclusion of the Epistle of the Bishops"). "When the four had died as martyrs, he went to Alexandria" = "when all these bishops and presbyters and deacons had suffered martyrdom in the prison at Alexandria, he at once entered Alexandria." "Meletius set aside the priests Peter had left to visit the needy, and named men of his own" = Peter's presbyters, "to whom the blessed Peter had given power to act as parish-visitors," whom Meletius "suspended ... and by his own authority ordained two persons in their place."
- **"Peter was in hiding" is sourced**, not transferred from the account's "presbyters, then in hiding." Bell 1924 (l.3206): "he went down to Alexandria, where, finding that Peter was in hiding, he proceeded to excommunicate various priests and visitors." The brief's whole sequence follows Bell's reconstruction.
- **The schism origin is given both sides and left open.** Athanasius (council deposed Meletius for crimes including sacrifice to idols), marked partisan, against Epiphanius (both jailed together, split over the lapsed, Peter for mercy). Bell undercuts Athanasius's sacrifice charge; Hefele undercuts Epiphanius. **Hefele's point is in the Library**: HE v1 l.22250–22256, "S. Epiphanius was mistaken on the principal points ... the original documents prove that, at the time of the commencement of the schism, neither Peter nor Meletius was in prison." The records.json `contested_claim` renders both sides accurately.
- **Family not invented.** Absent from the brief; the card and records.json carry the honest limit ("No early source gives his birth, family or schooling. Later Coptic and Ethiopic lives give a family, and do not agree with each other").
- **The Passion is marked late and doubtful** in both brief and card, with McGiffert's "spurious and historically quite worthless."
- **The Arius claim is card-only, attributed and hedged** (Sozomen; Hartranft "no one else links Arius with the Meletians early"; Robertson "deserve little credit").
- Card spot-checks verified: Maffei first edited the Latin (anf06 l.16704, l.25804); "McGiffert counts fourteen canons" (npnf201 l.43238 "Fourteen Canons,") and "the Ante-Nicene Fathers prints fifteen" (anf06 prints Canon XV, l.27694); Balsamon and Zonaras commentaries (anf06 l.1991, l.9713). The card line "most of the prisoners took Meletius's side" rests on Epiphanius, Panarion 68 (vendored only in Greek/Latin, Oehler); it is consistent with the known Epiphanian account and was not re-verified against the Greek — a verification limit, not a finding.

**Findings**
- **M1 MINOR.** "The quarrel with Meletius is told two ways." is a dispute-announcing paragraph opener (the batch 1 Ignatius M5 / batch 2 pattern), and the card's `uncertain` opens the same way ("How the split with Meletius began is told two ways"). It is milder than the batch 1 examples — a genuine topic sentence that then delivers both sides in place — so this is borderline, but flagged for consistency.
- **M2 MINOR.** records.json tags "Peter ordained Arius a deacon and later cast him out" **Inferential-Thin**. This is Sozomen's direct report (one witness), doubted by Hartranft and Robertson — thin, but a report, not an inference. The same tag choice was raised as minor across batch 1 and 2. Contested, or Documented with a one-witness note, fits the vocabulary better.
- **M3 MINOR (borderline).** One narrator sentence runs 26 words ("In the ninth year of the persecution, Eusebius says, Peter was seized 'for no cause and quite unexpectedly' and beheaded, many bishops of Egypt with him"), but about 20 of those are the narrator's once the embedded quote is set aside. Within "about 25"; noted only.

No blocking findings.

---

## 2. Anatolius of Alexandria and Laodicea (not major)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS, with one long narrator sentence (M1) |
| 5 | No role for a witness | PASS (McGiffert, Richardson, Salmond, Ideler, Zahn named) |
| 6 | Partisan witness | n/a. No hostile witness is used |
| 7 | Contested shown both sides, not settled | PASS (the Latin Paschal Canon; the siege date on the card) |
| 8 | Common names placed | PASS, with a two-Eusebius clarity point (M2) |
| 9 | One term | PASS |
| 10 | Story, scene, length | PASS (2:00) |
| 11 | grade_text | PASS |
| 12 | Card order and caveat | PASS |
| 13 | Audio tags | PASS |
| 14 | List line; Who test | PASS (Who; list line not checked here) |

**Quotes** (all exact against the rendered text)
- "secretly clothed in women's garments" — exact (Eusebius HE VII.32, npnf201 l.42757; source has a curly apostrophe).
- "stood first among the ablest men of our time" — exact (npnf201 l.42687).
- "Anatolius did not write very many works" — exact (npnf201 l.42769).
- "so far as we know" — exact (McGiffert's note, npnf201 l.40909 / l.42791, that Anatolius was the first Christian to use the nineteen-year cycle for Easter).
- Colman's "a holy man, and much commended in church history" — exact (Bede, HE III.25, Giles l.8117).
- Wilfrid's "a most holy, learned, and commendable man" — exact (Bede, Giles l.8135); Wilfrid's "since you do not observe his decrees" supports the brief's "But Colman's side ... did not keep his cycle."
- Card: Jerome's "a man of wonderful learning" — exact (Lives 73, npnf203 l.40934); "They say" for the siege — exact (npnf201 l.42718).

**Checks**
- **Namesake trap avoided.** Neither the brief nor the card mentions Anatolius, patriarch of Constantinople (451); no conflation. Display name and `otherNames` ("of Alexandria", "of Laodicea") keep the two early sees distinct.
- **Disputed dates not told as settled.** The brief gives no siege or Laodicea date. The card's `uncertain` carries the siege date (McGiffert: the revolt of Aemilian, 260; "Valesius and others ... a later siege under Claudius" is exact at npnf201 l.42712), the Latin Paschal Canon dispute (McGiffert/Zahn for an early translation of a genuine work; Ideler for a seventh-century work), and the birth/death limit (Richardson's and Salmond's estimates, each marked conjectural and source-less; Eusebius places the death before the persecution). records.json matches.
- **Whitby used correctly.** Both Colman (citing him in favour) and Wilfrid (conceding his holiness but denying the Ionans kept his cycle) name Anatolius, as Bede has it.
- Card `uncertain` "Jerome has grammar in place of physics" is accurate (Jerome lists grammar; Eusebius lists physics). The Aristotelian-school report and McGiffert's note that Eusebius gives Anatolius no church office in Alexandria are both borne out by HE VII.32 and its note.

**Findings**
- **M1 MINOR.** One narrator sentence runs 29 words: "His friend Eusebius, a deacon, was in the part of the city that sided with Rome, and he won the Roman commander's promise to spare anyone who came over." Past "about 25"; the batch 1/2 reviews flagged 26–31-word narrator sentences as minor.
- **M2 MINOR.** The siege story holds two men named Eusebius — "Eusebius of Caesarea" the narrator and Anatolius's "friend Eusebius, a deacon." The brief distinguishes them (place vs. role), and the collision is in the source, so this is a clarity note, not a common-name failure; a listener could momentarily conflate them.

No blocking findings.

---

## 3. Polycrates of Ephesus (not major)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS, with one long narrator sentence (M1) |
| 5 | No role for a witness | PASS (McGiffert, Valesius, Lightfoot named) |
| 6 | Partisan witness | n/a |
| 7 | Contested shown both sides, not settled | PASS (Victor's excommunication; Philip apostle vs. evangelist) |
| 8 | Common names placed | PASS |
| 9 | One term | PASS |
| 10 | Story, scene, length | PASS (1:59) |
| 11 | grade_text | PASS |
| 12 | Card order and caveat | PASS |
| 13 | Audio tags | PASS |
| 14 | List line; Who test | PASS (Who; list line not checked here) |

**Quotes** (all exact against the rendered text)
- "We observe the exact day ... neither adding, nor taking away" — exact (Polycrates' letter, Eusebius HE V.24, npnf201 l.31324–31325; the brief's comma at the split stands for the source's semicolon, no words changed). Also in anf08 l.72579–72582.
- "great lights" — exact (npnf201 l.31325).
- Philip "one of the twelve apostles" — exact (HE III.31, npnf201 l.19095).
- John "who reclined upon the bosom of the Lord" — exact (npnf201 l.19153); card "wore the sacerdotal plate" — exact (l.19154).
- "All these observed the fourteenth day of the passover according to the Gospel" — exact (HE V.24, npnf201 l.31364).
- "For seven of my relatives were bishops; and I am the eighth" — exact (npnf201 l.31386).
- "lived sixty-five years in the Lord" — exact (npnf201 l.31397).
- "not affrighted by terrifying words" — exact (npnf201 l.31399).
- "wholly excommunicate" — exact (McGiffert on Victor, npnf201 l.31419).
- "just how and when we do not know" — exact (McGiffert, npnf201 l.31185).
- Jerome's "to show through a small example the genius and authority of the man" — exact (Lives 45, npnf203 l.40413).
- Card: "the leading opponent of Bishop Victor of Rome" — exact (npnf201 l.31097); "The only writing of Polycrates of which we know" (brief: "the only writing of Polycrates known") — exact (l.31104); "no particular authority for that year" (the 198 synod date) — exact (l.31242).

**Checks**
- **Victor's excommunication given both sides, not settled.** Brief: Eusebius says Victor "declared the brethren there 'wholly excommunicate'"; Hefele, following Valesius, reads it a threat only; McGiffert holds it was carried out, as Socrates of Constantinople says; Irenaeus urged restraint. Both named sides present; records.json matches. (McGiffert's judgment that the measure took effect, and Socrates's direct statement, are both in the Library; Hefele–Valesius "threat only" is the counter.)
- **Philip apostle vs. evangelist attributed, not flat.** "McGiffert thinks Polycrates confused the apostle Philip with Philip the evangelist of the book of Acts" — the confusion is McGiffert's note at HE III.31 (l.19095 region). The card adds Lightfoot's defence of Polycrates. Both sides named.
- **Death honest limit kept.** "McGiffert says the year of his death is not known" (brief); card and records.json add that the accession year is also unknown and that the only dated figures (anf08 "about 200"; the editor's "130–196") are unsourced and disagree. No held source gives his end, and none is asserted.

**Findings**
- **M1 MINOR.** One narrator sentence runs 27 words: "The churches of Asia ended their fast on the fourteenth day of the moon, the day of the Jewish Passover, whatever day of the week it fell." Past "about 25."

No blocking findings.

---

## 4. Pliny the Younger (outside witness, not major)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | No role for a witness | PASS (McGiffert, Rolfe named) |
| 6 | Partisan witness | n/a. Tertullian is placed as a defender of the Christians |
| 7 | Contested shown both sides | PASS (the governorship date: McGiffert vs. Harnack, on the card) |
| 8 | Common names placed | PASS (Pliny the Younger / the Elder distinguished; Trajan, Tertullian of Carthage, McGiffert, Rolfe) |
| 9 | One term | PASS |
| 10 | Story, scene, length; reporter, no "fought-for" beat | PASS (1:55; he reports only) |
| 11 | grade_text | PASS |
| 12 | Card order and caveat | PASS |
| 13 | Audio tags | PASS |
| 14 | Outside witness is an objective reporter, not a polemicist | PASS (per Mark's 2026-11-12 ruling) |

**Quotes** (all exact against the rendered text; Pliny and Trajan both from McGiffert's note to HE III.33)
- "pertinacious and inflexible obstinacy ought to be punished" — exact (npnf201 l.19475).
- "one even twenty years before" — exact (npnf201 l.19490).
- "on a fixed day before daylight" — exact (npnf201 l.19493).
- "sing responsively a song unto Christ as God" — exact (npnf201 l.19494).
- "who were called deaconesses" — exact (npnf201 l.19504; source "two female slaves who were called deaconesses (ministræ)").
- "nothing except a superstition depraved and immoderate" — exact (npnf201 l.19506).
- Trajan's "are not to be searched for; if they are accused and convicted, they are to be punished" — exact (npnf201 l.19526).
- "offered incense and wine to the emperor's image" — supported (npnf201 l.19483, "offering incense and wine to thine image"; l.19490, "adored thine image ... and cursed Christ").
- Tertullian's "It forbids them to be sought after as innocent ... and it commands them to be punished as guilty" — exact (Apology 2, anf03 l.1585).
- Eusebius's "was to a certain degree checked" — exact (HE III.33, npnf201 l.19544).
- McGiffert's "a man of great literary attainments and an intimate friend of the Emperor Trajan" — exact (npnf201 l.19453); "nephew of Pliny the Elder" borne out by the same note ("to distinguish him from his uncle, Plinius Secundus the elder").
- Card: Eusebius's "one of the most noted of governors" — exact (npnf201 l.19448); Harnack's "about 111 to 113" — supported ("ep. 96 c. ann. 111/13", Harnack, Mission, l.8820). The Rolfe line (Suetonius's life known largely from Pliny's letters; Pliny got him a military post) rests on Rolfe's Suetonius introduction, already used in batch 2.

**Checks**
- **Outside-witness form kept.** The brief reports what Pliny did and what the Christians told him; there is no "what he fought for" beat and no editorializing on his motives. Passages are quoted or tightly paraphrased from the vendored text.
- **Doubts named with their owners.** Card `uncertain`: Pliny writes as the official who held the trials, and what he reports of the worship came from apostates (his own statement); the Library holds no edition of Pliny, only McGiffert's note, and Tertullian/Eusebius give only a short summary without the deaconesses or torture; McGiffert dates the governorship 110 or 111, Harnack dates the letter about 111–113.
- **No unsupported birth/death/Tacitus.** The brief asserts no birth or death year and never names Tacitus. records.json and the card carry the honest limit: "No held primary source gives the years of his birth or death ... No held source attests his friendship with Tacitus." Confirmed: the Library holds no Pliny edition. records.json tags Pliny's and Trajan's direct reports **Documented**, not Inferential-Thin — the batch 1/2 tagging fault does not recur here.

**Findings**
- **M1 MINOR (report-only).** The card's `label` "Outside witness" is placed after `otherNames`, above `knownFor`, rather than literally "beside the role" as the pattern's outside-witness section asks. Identical to batch 1 Josephus M8 and batch 2; it depends on how the page renders the field, so it is reported, not changed here.
- Note (not a finding): Pliny is a Roman governor, not a historian, so the outside-witness label is a judgment call; it stands on Mark's 2026-11-12 ruling (Open-Gaps 233), and he reports rather than fights the church, so the Who test passes as ruled.

No blocking findings.

---

## Summary

| Profile | Blocking | Minor |
|---|---|---|
| Peter of Alexandria (MAJOR) | 0 | 3 |
| Anatolius of Alexandria and Laodicea | 0 | 2 |
| Polycrates of Ephesus | 0 | 1 |
| Pliny the Younger (outside witness) | 0 | 1 |
| **Total** | **0** | **7** |

No blocking findings in this batch.

This batch reads as markedly cleaner than batch 1 and batch 2, and the recurring batch-1/2 failure modes were checked hard and were **not** found:
- **Dispute outcomes.** Every contested point (Peter's schism origin, Polycrates' Victor-excommunication and Philip, Anatolius' Latin Canon and siege date) is given both sides with witnesses named and is left open; none is told to its end on the wrong side, and none drops the verdict of the profile's own named witness. Hefele's "neither man in prison / Epiphanius mistaken on the principal points" is genuine and in the Library (HE v1 l.22250–22256), not a stand-in.
- **Roles for witnesses.** None found; McGiffert, Hartranft, Robertson, Coxe, Maffei, Richardson, Salmond, Rolfe are all named.
- **"Only" / single-witness lines.** All grepped against the whole Library; each is attributed to its scholar (McGiffert on Polycrates' one surviving letter; the Pliny-edition absence) and holds.
- **records.json tags.** The one carry-over is Peter's Sozomen-on-Arius line tagged Inferential-Thin (M2); Pliny's and Trajan's direct reports are correctly Documented.
- **Dispute-announcing openers.** One mild instance (Peter M1).
- No dropped quote words, no "not X but Y" / colon-reveal / rhetorical build-up in any narrator prose, no unearned superlatives, no invented family or anecdote, no contested birth or date told as settled. Three narrator sentences run 27–29 words (Peter M3 borderline, Anatolius M1, Polycrates M1).
