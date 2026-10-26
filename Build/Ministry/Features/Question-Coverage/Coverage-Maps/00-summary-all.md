# Coverage maps: all sixteen clusters

> **Corrections after the independent Opus review of 2026-10-26** (`../Review/opus-work-review.md`). Of 38 claims checked, 26 held, 7 held in part, 5 failed; all 6 quotes re-verified matched. Read this block before using any number or row below.
> - **Withdrawn or corrected:** npnf203 53776 is Origen's letter quoted by Jerome, not a hal quote (hal worklist row withdrawn); Ep. 77.3 does not call Fabiola's husband violent; the "two cookie paragraphs" privacy item is withdrawn (feature flag); the Didascalia and Erasmus acquisition scores ignore window and place and are not reliable.
> - **"Contradicted" limits:** `desert.limit.tithe` and `desert.limit.f2-scripture-detail` hold. The rzg limit needs only its `why_sources_cannot_answer` line fixed; the syr marriage limit needs only its "not a description of Christian practice" clause narrowed; whether the Formula of Concord (1577) speaks in `witt.term.free-will`'s 1520-45 voice is a world decision, not drift. Read "contradicted" in the sections below as "narrow".
> - **"Loaded" is not all own-voice.** The search tool ignores the corpus-map role and scans whole shared volumes, so the loaded-only totals (and the 299 and 371 cells) include opponent and outside voices and other authors in shared volumes. Re-run with role, window and author filters (`engine.m9.cli holdings`/`shelf`) before sizing any build.
> - **Held for Mark:** the 69 Facilitator-adjacent worklist rows wait for a ruling under Facilitator Governance V3.6; the Chrysostom mapping is held for re-decision; the Doc_02 sub-question duty in the first Library prompt was a method change and is struck.
> - **lpc:** it has 360 records, all draft with no `use_note`, and no `packages/` folder, so none reaches a participant.


Read-only pass, 26 October 2026, over the twelve worlds with records (alx, cappadocian, desert, don, gallic, hal, ijc, lpc, pahc, rzg, syr, witt). Sixteen coverage reports, C1 to C16, were put together. Each judged what a world can say to a cluster of visitor questions. Mark's layers are used throughout: RENDERED (a record speaks to it, so the voice can reach it), LOADED (the answering text is vendored and mapped to the world, but no record carries it), IDENTIFIED (named in the world's source registry, not vendored), NOTHING. Quote records cited as rendered were re-verified word for word against their vendored file in every report. Nothing in the repo was changed. No model was called and no network was used.

C17 (challenging the system) was not mapped. Its 16 questions are listed in the repository file in the scratchpad: 3 exist as sealed-probe items, 13 are predicted, and 5 are flagged for the Facilitator (C17-04, 05, 06, 13, 16). C17-05 and C17-06 ask the same thing as the C16 Part B questions below.

The two worklists that go with this summary are `worklists/acquire.yaml` (165 acquisition rows, 233 world-by-sub-question cells unlocked) and `worklists/records-by-world.yaml` (742 rows, 69 Facilitator-adjacent). The 4-cluster versions are kept as `*-4cluster.*`.

## The picture in numbers

Cells judged: 1,392 world-by-sub-question cells in fifteen reports, plus 240 wordings in C15. The table is taken from each report's own layer table. How the report codes were mapped:

- **Rendered, answers**: R, and the R-grades in C1 (h, m, l), C4 (R-q, R-w), C7 (R with F, P or T depth), C14 (R with h, m, l).
- **Rendered, as a limit or partial**: R*. In C1 this is R(hon), in C4 R-l, in C7 R*-T, in C14 R*. R* is not always an honest_limit. In C2 and C5 to C13 it also covers a record that answers only one facet, or only a guard or not_for. In C9 it also covers draft-only cells (all 330 lpc records are draft).
- **Loaded only**: L, L-, L-T.
- **Identified only**: I. One cell in the whole fleet.
- **Nothing**: "-", "N", and C4's dash. Two cases are mapped here by me: C16's layer O ("governed by instruction or product fact, no record") counts as nothing, and C15's LIMIT-ONLY counts as nothing (the report says nothing is never used there, because a limit can always be written).
- **C11** marks 10 cells "out" (Muslims, for the ten worlds that end by 451). They are shown in their own column and are not in the other five.
- **C15** uses NEAREST-RENDERED, NEAREST-LOADED and LIMIT-ONLY, counted over 240 wordings, not 96 cells. NEAREST-RENDERED (a record with nearest material and a guard that names the modern frame) goes in the limit column. NEAREST-LOADED goes in loaded. No C15 question can be answered, so the first column is 0. On the 96-cell best-layer view the counts are 38 nearest-rendered, 35 nearest-loaded and 23 limit-only (from the C15 JSON).
- **C16** Part A uses its layer table: R 64, R* 21, O 11. The report's own sentence says "73 of 96 cells are rendered outright". The table gives 64. The table is used here. Part B is about the Facilitator and has no cells.

| | Cells | Rendered, answers | Rendered, as limit or partial | Loaded only | Identified only | Nothing | Out of window |
|---|---|---|---|---|---|---|---|
| C1 Jesus | 96 | 67 | 13 | 15 | 1 | 0 | |
| C2 God, Trinity, Spirit | 96 | 24 | 44 | 15 | 0 | 13 | |
| C3 Hell, afterlife | 96 | 33 | 11 | 39 | 0 | 13 | |
| C4 Salvation | 96 | 49 | 6 | 34 | 0 | 7 | |
| C5 The Bible | 96 | 31 | 39 | 23 | 0 | 3 | |
| C6 Authority | 96 | 66 | 18 | 12 | 0 | 0 | |
| C7 Worship, baptism, prayer | 96 | 82 | 4 | 10 | 0 | 0 | |
| C8 Women, children, enslaved, marriage, sex | 96 | 41 | 18 | 31 | 0 | 6 | |
| C9 Violence, empire, martyrs | 72 | 34 | 29 | 9 | 0 | 0 | |
| C10 Money, poor, work | 84 | 35 | 18 | 31 | 0 | 0 | |
| C11 Jews, pagans, Muslims | 96 | 36 | 36 | 12 | 0 | 2 | 10 |
| C12 Daily life | 96 | 50 | 33 | 10 | 0 | 3 | |
| C13 Devil, miracles, saints | 84 | 12 | 20 | 50 | 0 | 2 | |
| C14 Suffering, doubt, leaving | 96 | 81 | 6 | 8 | 0 | 1 | |
| C15 Today (240 wordings) | 240 | 0 | 57 | 72 | 0 | 111 | |
| C16 Evidence, "what are you" | 96 | 64 | 21 | 0 | 0 | 11 | |
| C17 System challenges | not mapped | | | | | | |
| **All sixteen** | **1,632** | **705** | **373** | **371** | **1** | **172** | **10** |

On the 1,392 cells of the fifteen cell-based reports (C15 left out): rendered 705 (50.6 percent), limit or partial 316 (22.7 percent), loaded only 299 (21.5 percent), nothing 61 (4.4 percent), identified only 1, out of window 10.

### Quote verification

Every cited quote record was matched against its vendored file. The same quote is cited under several clusters, so the totals are citations, not distinct quotes. The JSON verification blocks hold 340 distinct record ids (C1 and C14 are read from per-cell blocks, C4 from its text output).

| Report | Cited as rendered | Matched | Not clean |
|---|---|---|---|
| C1 | 40 (counted from the JSON; the report gives no number) | 40 | |
| C2 | 51 | 51 | |
| C3 | 25 | 25 | |
| C4 | 30 | 30 | |
| C5 | 32 | 32 | |
| C6 | 68 | 67 | 1 partial: `don.quote.donatus-quid-est-imperatori` |
| C7 | 72 | 72 | |
| C8 | 26 | 26 | |
| C9 | 38 | 38 | |
| C10 | 27 | 27 | |
| C11 | 30 | 30 | |
| C12 | 47 | 47 | |
| C13 | 25 | 25 | |
| C14 | 121 citations of about 70 quotes | 121 | |
| C15 | 34 | 33 | 1 partial: the same Donatus record |
| C16 | 23 | 22 | 1 unresolved: `don.quote.emeritus-magno-argumento` |
| **Total** | **689** | **686** | 3 |

No report found a difference in wording. Every other divergence was an editorial artifact in the vendored file: footnote markers, page breaks, soft hyphens, section numbers, OCR glyphs, spacing. The C1 note of six quotes that failed on the second pass was closed by later reports for five of the six (details in the drift list). Report-level discrepancies: C5 lists 36 ids in its JSON against 32 in its text, C13 lists 26 against 25.

## What the sixteen maps say together

1. **The dominant gap is LOADED, not missing.** 299 of the 1,392 cells (21.5 percent) have the answering text vendored and no record to carry it. Only 1 cell is identified-only (C1, witt, S6 his humanity: Luther's 1523 treatise on Jesus born a Jew). Only 61 cells are nothing. In C15, 72 of 240 wordings are nearest-loaded. The worst clusters by share: C13 50 of 84, C3 39 of 96, C4 34 of 96, C8 31 of 96, C10 31 of 84. The records worklist agrees: 343 rows have the text already vendored, 144 depend on an acquisition. Closing the gap costs quote records and renderings, not source research.

2. **The canon does not force demonstrations per world.** Each report counted the demonstrations in its own canon cells.
   - C1: C-I demonstrations in 7 of 12 worlds (none in don, gallic, lpc, rzg, witt), C-T in 3, C-E in 2, C-P in 9.
   - C4: F1-T only in gallic, ijc and witt. F4-T only in don and hal. Eight of twelve worlds have neither.
   - C6: F3-I in 3 worlds (gallic, syr, witt). F1-E and F3-T in none of 12, although 35 and 49 records carry those tags.
   - C7: none for prayer (f4-i-02), the meal (f4-i-03), fasting (f4-i-04) or "what happened when you gathered" (f3-i-02). alx, cappadocian and desert have none in any of the four cells.
   - C8: F5-T none. None for the two tortured enslaved women (f6-e-01), for children (f5-i-04), for the enslaved (f5-i-05) or for marriage (f5-t-01). lpc and rzg have no F6-P demonstration.
   - C9: none for danger (C9-01), catacombs (C9-02) or temples (C9-05). The nine demonstrations in F3-I, F3-E, F3-P and F6-E answer other questions.
   - C10: none for money (f5-t-02), tithe (f4-t-02) or work (f5-i-07).
   - C11: none for "too narrow" (f6-t-02) or temples and the old gods (f3-p-03).
   - C12: 10 of 13 F5 questions have none. cappadocian, desert, don, lpc, rzg and syr have none.
   - C14: none for unanswered prayer (F4-P-03), what to say to one who left (F6-P-04), forgiving the unrepentant (F4-P-02) or failing to hold your own accountable (F3-P-01).
   - C16: F2-E demonstrations in 4 worlds, none for f2-e-04 (suppressed gospels).
   - C2, C5 and C13 have no canon cell. C15 finds F2-T fences in four worlds and F3-T fences in nine, and none for anything else.
   - Three demonstrations are tagged wrongly: `rzg.demo.why-we`, `lpc.demo.compel-three-phase`, and the three rzg demonstrations with empty canon_cells (see the drift list).

3. **Fleet-wide holes, by sub-question.** Counts are worlds out of 12.
   - C1 S5, "did he really exist": rendered in 2, no record retrieves on it. C1 S6, "what did he look like": rendered in 2 (syr and part of pahc), loaded in 9, identified in 1.
   - C2 S1, "is God real": rendered in 0, partial in 6, loaded in 3, nothing in 3. Only cappadocian answers "who made God". C2 S2 (what God is like): rendered in 0. C2 S7 (where evil comes from): rendered directly in 1, syr.
   - C3 S2, "is hell forever": rendered in 1 (witt), partial in 1 (alx), loaded in 10. C3 S4, "were the wicked destroyed": rendered in 0, loaded in 5, nothing in 6. C3 S3, restoration: rendered in 3 (alx, hal, witt), nothing in 6.
   - C4 S6, "those who never heard": rendered in 1 (pahc). C4 S8, the unforgivable sin: rendered in 2, loaded in 10.
   - C5 S8, one verse at a time: rendered in 0. No record answers any of the sampled passages except John 1 (alx) and Genesis 1 (five worlds). The Luke 9:27 gap stands in all twelve. C5 S7, violence in the texts: rendered in 1. C5 S3, reliability: rendered in 2.
   - C6 S6, married clergy and deacons: rendered in 1 (witt).
   - C8 S6, same-sex relations: rendered in 0, loaded in 11. C8 S8, a beaten wife: rendered in 0 (deliberately minimal).
   - C9 S4, soldiers and war: rendered in 1 (gallic), loaded in 7.
   - C10 S5, usury: rendered in 1 (cappadocian).
   - C11 S4, Muslims: 10 worlds are out of window and none says so. C11 S1, Jews: rendered in 1. C11 S8: rendered in 1 (pahc).
   - C12 S2, houses, clothes and speech: rendered in 2. C12 S7, "were you happy": nothing in don, hal and pahc.
   - C13: demons S2 rendered in 2, angels S4 in 1, saints and relics S5 in 2, magic S6 in 0, the dead in dreams S7 in 0 (no record in any world).
   - C16 S7, "you sound too polished": nothing in 11 worlds and a partial in syr.
   - C14 S3, anger at God and lament: rendered in 6 worlds, four of them at low confidence (the C14 table), loaded in 6. Lpc's Enarrationes in Psalmos, the richest lament text in the corpus, has a source record with 0 citing records.

4. **Four worlds carry the worst mismatch between what they will be asked and what they hold.** Share of cells that are loaded-only, identified-only or nothing, over 116 cells per world (C1 to C14 and C16): rzg 55 (47.4 percent), ijc 40 (34.5), lpc 38 (32.8), don 36 (31.0). Lowest: witt 17 (14.7), syr 21 (18.1).
   - **rzg (Zurich and Geneva).** Rendered in only 25 of 116 cells. C1: the weakest world, one witness for S1, no divinity or resurrection record, while Institutes II.16 is vendored. C2: nothing on God, Trinity, Spirit, evil or councils. C4: no record on justification by faith, with Institutes III.11 vendored. C5: nothing on canon, translation or Genesis. C9: Servetus appears in no witness, with Tweedie's book vendored. C13: no record on any question. C14: suffering and lament are loaded only. C16: thin across the row. It also has the largest records worklist, 80 rows.
   - **lpc (Latin pastoral, in build).** All 330 records are draft and have no use_note, so no guards exist (C15). C3: not one record on hell, judgment, purgatory or the dead, with Cyprian's reunion passage, Enchiridion 69 and 110, Monica and City of God I.17 on suicide all loaded. C7: no meal or calendar record. C11: nothing on Jews, gods or philosophy. C13: nothing on any question. Whether any draft reaches a package was not checked.
   - **ijc (Imperial-juridical).** Empty on God, the Spirit and evil (C2), free will and election (C4), philosophy (C11). C3: only the creed and the Altar of Victory story. C13: two adjacent hits. C14: theodicy is loaded only.
   - **don (Donatists).** C14 S8 (despair) is the only NOTHING cell in that cluster. C2: S1, S2, S7, S8 empty. C4: predestination, the unevangelised and indulgences have no record. C13: no record says what happened at the martyrs' graves. The movement's own afterlife and martyr voice (Tilley, Donatist Martyr Stories) is in copyright in English.
   - The Cappadocians are below average on this share (22.4 percent) but have the second-largest worklist (77 rows, 23 awaiting acquisition). C3: no record mentions hell or judgment, with Catechetical Oration 26, Oration 40.23 and On Infants' Early Deaths vendored. C10: the famine homilies are vendored as English extracts and no quote record uses them.

5. **Existing honest_limits and terms that the vendored library overstates or contradicts.** Each is a record to narrow, not a new record.
   - `desert.limit.tithe` says no source names a tithe. Its check covered only the Vita and Palladius. Cassian Conference XXI (npnf211 lines 44550-44680) discusses tithes (C10).
   - `desert.limit.f2-scripture-detail` says no source records a desert voice on Genesis. Cassian Conference X (npnf211 line 35878), which its own Sarapion story uses, is that debate (C5).
   - `rzg.limit.no-teaching-on-wealth-or-marriage` is true of the records and not of the library. Calvin's Institutes (vol. 1 line 25853, vol. 3 lines 2436 and 11100), the Second Helvetic Confession ch. XXIX and Zwingli on tithes, usury and community of goods are vendored (C8, C10, C15).
   - `syr.limit.marriage` and `syr.demo.marriage-ending` say no text speaks to Christian marriage or its ending. The Book of the Laws of Countries (anf08 lines 68966-68985, mapped to syr), Aphrahat Demonstration VI.4-7 and Egeria on Edessa speak to it (C8).
   - `alx.limit.marriage` and the silence on women: Clement Stromateis IV.8 and II.23 are vendored in English (C8).
   - `witt.term.free-will` says the library carries no developed predestination doctrine. Formula of Concord XI is in the vendored Book of Concord at line 25390 (C4).
   - `cappadocian.term.martys-martyrion` has a not_for saying the world "denied" worship of martyrs, with the Basil and Nyssa martyr homilies unvendored (C13).
   - `desert.story.antony-tomb-combat` calls the beast-demons "this world's own chosen register for interior struggle", a modern reading no vendored line settles (C13).
   - Cappadocian source records call the Basil homilies "unverified" and "unacquired" while English extracts sit at npnf208 lines 5069-5284, 6236-6290 and 6926 (C10).
   - `cappadocian.story.slave-market-sermon` rests on Nyssa's Ecclesiastes homily, which is unvendored; the line is a paraphrase (C8). `hal.dw.marriage-ending` is gentler than Jerome's own answer in Ep. 55 (C8).
   - The brief for this pass named a Syriac slavery limit. No report names an overstated one. C8 shows `syr.limit.f5-enslaved` as a guard with no loaded text. The overstated Syriac records are the two marriage records above.

6. **Guards that would fail a visitor.**
   - *The Jewish visitor (C11).* The Library holds no Jewish voice: no Josephus, no rabbinic text, no Philo. The visitor reaches records in seven worlds. Three edges are unguarded: `hal.story.oea-gourd` (the Jewish residents answered "whether from ignorance or spite", Augustine Ep. 71.5, and the not_for does not stop that), `alx.quote.clement-schoolmaster` (no not_for names the supersession reading, and `alx.term.christological-reading` invites "Jews read the same text without Christ"), and `witt.term.the-turk` (its world_word files Jews with the Turk as "one of the devil's instruments", and the not_for covers only the modern-political reading). Smaller edges: `pahc.quote.polycrates-to-victor` has no Jewish guard; `ijc.limit.earlier-windows` blurs "our own bishop kept unpunished" against `ijc.story.callinicum-synagogue`; bare, syr Demonstration XVII.1 states what Jews did as fact. Five worlds have no record (desert, don, gallic, lpc, rzg), and lpc (Cyprian Ad Quirinum, Augustine's witness-people) and rzg (Calvin, "whose blindness is well known") map hostile text. Syr's guards hold on every record. C2 adds that a new rzg quote from Second Helvetic ch. 3 needs a not_for for its line on "the Jews and Mohammedans". C3 asks for a check that the syr anti-Jewish polemic records hold the polemic without a damnation verdict when C3-26 lands on them.
   - *Suicide and self-harm.* The charge that Circumcellions threw themselves over precipices (Augustine, npnf104 line 16889) is vendored and unframed in don (C3, R-20). The same hostile portraits answer C9's martyr-seeking question, and Letter 133 and City of God XIX.6 are mapped and unframed in don and lpc (C9).
   - *Misreadable doctrine.* `gallic.term.predestination` can be read as universalism and its not_for does not guard that (C3). Ephrem's Testament curses (npnf213 lines 11642-11644) would change tone and need a not_for (C3). The Zwingli hit at vol. 3 line 1523 is the editor's paraphrase, not Zwingli (C3).
   - *Violence in the home.* No record names a husband's blows. Basil's hatchet canon, Augustine on Monica's town ("marks of blows") and `hal.quote.she-put-on-sackcloth` (Ep. 77.3) are history, never counsel (C8, C14).
   - *Retrieval traps.* `ijc.quote.jerome-damasus-verses` is retrieved on "tombs of the martyrs" but is about verse-making (C13). `ijc.dw.original-sin-transmitted` is tagged to "did you baptise babies" yet is Leo on inherited sin (C7). `ijc.quote.happy-christian-emperors` is about rulers and must not answer "were you happy" (C12).
   - *Nearest-text decisions.* For gay marriage, AI and abortion the nearest vendored text is condemnatory or penal (Basil Canons II and VII, Salvian on Africa, Rom 1:26-27 as cited by Augustine and Athanasius, idol and oracle polemic). Offered as "nearest" it answers by implication. Whether to name it is Mark's decision (C15).
   - *Citation.* `pahc.quote.two-female-slaves-who-were-called-deaconesses` is verbatim only inside the NPNF editor's endnote and names a Pliny source that is not vendored (C15, C6).

7. **The modern-question gap, and the horizon check (C15).** All 20 C15 questions are never-faced. Over 240 wordings: nearest-rendered 57, nearest-loaded 72, limit-only 111. S3 (AI and talking to a machine) is limit-only in every world. S1 (gay marriage) has no nearest-rendered cell in any world. No record in any world says "we never met that question" for a C15 wording. The fences that exist are by-products: F2-T gives four explicit science non-answers (pahc, syr, witt, alx by a not_for), F3-T gives nine worlds a "not a later denomination" fence. A limit is built in 20 of 96 cells (from the JSON). The engine cannot see these questions: the horizon scan (`engine/m1/horizon.py`) knows 29 events from 303 to 1648, explicit years, centuries after the window and one fleet modern_term (Trinity). Tested clean: evolution, internet, AI, podcast, gay marriage and the bare word "Reformation". A first-ask later_age question goes to the voice with no Facilitator text, so the honest_limit carries the whole answer; the fixed etic text appears only on a second ask. "What do you think about AI?" does not match the system-nature shape either. No modern_term record exists for any C15 term. The report proposes a shape for each sub-question for Mark to react to; none is written. In window terms, 10 of 12 worlds cannot speak to Islam and none says so (C11); only witt and rzg are in window, and both map firsthand Ottoman material (Gerlach, Lucaris) that no record uses.

8. **Most "what are you" questions never reach the Facilitator (C16 Part B).** Of nine questions, one matches a template. "Are you real" and "How were you made" match `_SYSTEM_NATURE_SHAPE` (`engine/m5/routing.py` lines 56-62). These fall through to the Representative: C16-10 ("Were you actually alive ... What are you, exactly?"), C16-11 ("What are you, really?"), C16-13 (who is "we"), C16-16 ("Are you making this up?"), C16-19 ("Are you going to try to convert me?"), C16-20 ("Who wrote your answers?"), C16-26 ("Is my conversation private?") and R-23 ("Should I trust you that much?"). The fleet voice file allows one sentence, "I am a representative of [world]", and forbids explaining what kind of thing is speaking. For C16-20 and C16-26 the voice holds no facts, so its answer will be improvised. The single in-world demonstration, `rzg.demo.why-we`, never says AI. The template today (`engine/m4/facilitator_turns.py` lines 64-76) begins "Yes - we use AI here" and says the voice "isn't a person, it isn't the church". Privacy facts to check any answer against: conversations idle for 90 days are deleted daily and a participant can delete one; the QC store keeps one row per turn under a keyed hash of the session id, clears question and answer text after 90 days, keeps marks, scores, routing and flags indefinitely, and samples whole conversations for an offline audit; backups last 14 days. The privacy page (`cic-website/privacy.html`) says the scrubbed review copy is deleted after 90 days, says "Our project team reviews conversations" and "we never quote from them", names Anthropic's Claude on Amazon's servers, kept out of training, and `about.html` names Faithways Studio, Inc. Two findings after the Opus review: the page does not say the code keeps scores and flags without text (a disclosure gap; its claim that the copy of questions and replies is deleted is true); and nothing inside the conversation app links to or states any of it. The earlier "two back-to-back cookie paragraphs" item is withdrawn: one paragraph is hidden by a feature flag. "Show me the page" is also unmet: the edition is in the payload and `SourceList.tsx` never prints it, the locus is stripped, and the verbatim text is not sent.

9. **Facilitator-adjacent material is uneven by world.** What a Representative can say warmly and truthfully after a redirect, from C14's follow-up section, C3, C8 S8, C12 and C13 S7:

   | World | Holds | Lacks or carries a risk |
   |---|---|---|
   | alx | plague nursing as presence (`alx.story.plague-nursing`) | no grief vocabulary; nothing on the dead baby or suicide; Origen's infant-baptism homilies are Latin and unvendored |
   | cappadocian | tears allowed and despair refused (`term.penthos-paraklesis`); a brother at his sister's deathbed (`story.macrina-deathbed`); Basil's hatchet canon | Oration 40.23 and On Infants' Early Deaths are the Library's best texts on babies who die and are unrendered; no term for purgation |
   | desert | judgment refused (`quote.moses-sins-run-out`); a rule made for the weak | Vita 65-66 on souls rising past the accuser is unquoted; death-wish answers are hedged (`dw.death-wish` is Inferential-Thin) |
   | don | grief kept in the commemorative sermon (`dw.what-belonging-cost`) | nothing on despair; the Circumcellion charge is unframed |
   | gallic | Christ in the beggar (`dw.the-christ-who-bears-the-wounds`); grief aloud at Martin's death | the near-S7 story (Agnes, Thecla and Mary visiting Martin) is unrecorded |
   | hal | grief allowed and consolation given (`dw.suffering`); `quote.she-put-on-sackcloth` (Ep. 77.3 names Fabiola's husband's vices, not violence; corrected after Opus review) | history, never counsel; Letters 39 and 60 (consolations) are unrecorded |
   | ijc | "let the sinner be glad" (`quote.leo-sinner-be-glad`); singing so sorrow would not wear them down | Ambrose on Satyrus and Chrysostom's Letters to Olympias are unrecorded |
   | lpc | the shepherd wounded in the flock; Peter the sick man | nothing on the dead; all draft |
   | pahc | "the multitude of His tender mercies" | Perpetua's vision of her brother Dinocrates, the best dream text in the fleet, is unrecorded |
   | rzg | dread answered by looking to Christ (`demo.predestination-and-dread`) | no grief record |
   | syr | the Physician, the warmest in the fleet (`dw.physician`, `quote.aphrahat-one-innocent`) | Dem. VIII (sleep of the soul) unrendered; Ephrem's curses need a not_for |
   | witt | comfort as rest for an accused conscience (`term.comfort`); death as sweet sleep (`term.death`) | Luther's Fourteen of Consolation is vendored with a source record and 0 citing records |

   No world has a record on a husband's violence. The texts that touch it counsel endurance (Augustine Conf. IX.9, Basil Ep. 188 can. 9, Chrysostom Hom. 20 on Ephesians) and belong, if anywhere, in a Facilitator-governed note. The records worklist flags 69 rows as Facilitator-adjacent, 10 of them for lpc.

10. **What really needs acquiring is small, specific, and often blocked by copyright.** The acquire list has 165 rows unlocking 233 cells. 71 rows are flagged because the English is in copyright or the work is modern scholarship. The top rows by cells unlocked are the Didascalia Apostolorum (11 cells; Gibson 1903 is public domain), the Donatist martyr acts (9; English in copyright, Latin vendored), the Geneva Consistory registers (9; in copyright), Zwingli's Exposition of the Faith (8), the English Theodosian Code (7; in copyright, Latin vendored), Aphrahat's other Demonstrations (6) and the Saxon visitation protocols (5). 43 items the reports listed as "outside the repo" are already vendored. One 4-cluster acquisition (Tyconius, Liber Regularum) is vendored and unread.

## Drift and defects for the owning threads (not touched here)

One list, deduplicated, with the report that found each. Record ids resolve under `records/<code>/<type>/`.

**Registry drift and stale source records**
- `gallic.source.cassian-de-incarnatione` is marked unvendored and on WANTS-REGISTER; the work is in the vendored npnf211 (heading at line 48467) (C1, C2).
- `witt.source.book-of-concord` is marked unvendored while the Jacobs 1911 Book of Concord is vendored and mapped; `witt.term.free-will` is wrong as a result (C4).
- `rzg.source.ecclesiastical-ordinances-1541` is marked unvendored while a 1735 French printing is mapped; confirm it is the 1541 text. The 1576 council revision is also vendored in French (C4, C6, C14).
- `cappadocian.source.liturgy-of-st-basil` is marked unvendored; the Neale volume is mapped (C7).
- `don.source.acta-saturnini-abitinian-martyrs` is marked unvendored; the Latin is in `cic/texts/monumenta-vetera-donatistarum_migne-pl8.txt` (lines 1781, 2974) (C7, C9, C13). `don.source.tilley-donatist-martyr-stories` has the same Latin side vendored; the English is blocked (C3, C14).
- `rzg.source.genevan-psalter` is marked unvendored; `cic/texts/marot-beze_pseaumes-mis-en-rime-francoise-fra_1562.txt` is mapped (C5).
- `witt.source.melanchthon-instructions-for-the-visitors` is cited by C14 and no file of that name exists under `records/witt/source/` (C14).
- `cappadocian.source.pharr-theodosian-code-translation`: Pharr is unvendored and in copyright; the Latin Codex Theodosianus is vendored (C3, C14).
- Source records with 0 citing records: `cappadocian.source.gregory-nyssa-love-of-the-poor-lepers-consolation`, `lpc.source.augustine-expositions-on-the-psalms`, the Beza Job source in rzg, the Luther Fourteen of Consolation source in witt, `syr.source.odes-of-solomon`, the hal Ep. 125 source (C3, C14).
- Corpus-map gaps: `cic/corpus-map/pelagianism.yaml` holds Pelagius's Letter to Demetrias but hal, lpc and gallic are not mapped to it (C4). Chrysostom's Homily 20 on Ephesians (`npnf113`) is mapped to none of the twelve (C8). Chrysostom's verse-by-verse homilies (npnf110, 112, 113, 114) are mapped only to the Antiochene world (C5). Orange 441 canon 26 is mapped only to ijc (C6). Basil Letter 93 is not mapped to desert (C7). Jerome Ep. 146 sits in hal's map, not alx's (C6). The Persian martyr acts and the Anabaptist sources are mapped to other movements (C9). `paulinus-milan_vita-ambrosii_kaniecka1928.txt` reaches ijc only through a source record (C13).

**Mis-tagged or mis-indexed demonstrations and records**
- `rzg.demo.why-we` is tagged `canon_question_id` c-t-03 but its exchange is "what are you" (C1, C16). `rzg.demo.why-we`, `rzg.demo.consensus-contest` and `rzg.demo.predestination-and-dread` all carry empty `canon_cells` (C9, C16).
- `lpc.demo.compel-three-phase` (draft) carries f3-p-02 but its participant line is the hypocrites question (C9).
- `ijc.dw.original-sin-transmitted` is tagged to "did you baptise babies" (C7). `hal.dw.record` carries the "Saints and holy places" tag (C7). `desert.core.desert` is the only source of the fasting tag (C7). The card tags "Hymns and music" and "Feast days" rest on PREDICTED questions, and no Icons or Confession tag exists (C7).
- `pahc.quote.appointed-to-be-read` quotes Athanasius's 367 letter inside a 70-200 world (C1). `pahc.quote.polycrates-to-victor` is filed under F3-I so afterlife retrieval is not guaranteed (C3). `lpc.quote.pardon-through-a-wicked-clergyman` is indexed only for the wicked-minister question (C4).
- Retrieve_when gaps: `hal.dw.authority` retrieves only on "who appointed bishops" (C2). Several alx witnesses have empty retrieve_when (C2). pahc has no record that retrieves on "did he exist" (C1). `ijc.quote.jerome-damasus-verses` retrieves on "tombs of the martyrs" (C13).

**Duplicate records**
- `pahc.quote.justin-reasonable-livers` and `pahc.quote.those-who-lived-reasonably-are-christians` carry the same Justin sentence (C4).
- `gallic.quote.grievous-blasphemy-not-all-men-to-be-saved` and `gallic.quote.without-grievous-blasphemy-all-men-to-be-saved` carry Cassian Conference XIII.7 twice (C4).
- `don.story.macrobius-letter` and `don.story.macrobius-letter-isaac-maximianus` are one story twice (C13).

**Draft status and unpackaged records**
- All 330 lpc records are draft, with no use_note. Which reach the compiled package was not checked (C6, C9, C12, C15).
- `don.limit.bagai-violence-no-account`, `desert.limit.communal-wrong-unrepaired` and `don.quote.donatus-quid-est-imperatori` are draft (C6, C9).

**Unresolved verbatim checks**
- `don.quote.donatus-quid-est-imperatori`: the English matches Vassall-Phillips line 1904; the Latin appears only in the critical edition's index (C6, C9, C15).
- `don.quote.emeritus-magno-argumento`: the Latin is not findable in the OCR-noisy `pl11-zeno-optatus-collatio-carthaginiensis_migne.txt` (C16).
- `pahc.quote.two-female-slaves-who-were-called-deaconesses`: verbatim at npnf201 lines 19502-19506, inside an editor's endnote, with a Pliny source that is not vendored (C15).
- `gallic.quote.salvian-free-men-in-seeming-captivity`: failed the second C1 pass and no later report re-verified it. A grep during this pass found the sentence in `salvian_on-the-government-of-god_sanford1930.txt` at line 6458, split by a line-end hyphen. This is a lead, not a verification. The other five quotes from that C1 note were matched later: `desert.quote.in-real-experience-and-feeling` (C2), `desert.quote.sin-and-grace-in-one-soul` (C4), `gallic.quote.salvian-ever-present-judgment-gallic-provinces` (C2, C3), `gallic.quote.salvian-on-the-unburied-dead` (C12), `gallic.quote.salvian-rich-murdering-the-poor` (C10).

**Overstated or contradicted limits and terms** are listed in finding 5. **Engine, site and product items** are in finding 8 and the `_fleet` section of `worklists/records-by-world.md`.

## What was not done

No record was written or changed, and no file in the repo was edited. No model call, no network. `canon/sealed_probes/` was not opened in any of the sixteen passes. The reports' layer tables were taken as written; I did not rerun any search. Line numbers in the worklists are the reports' own; only the vendored files, records and engine paths were checked to exist (410 record-row paths and 59 registry paths: none missing). A few greps and directory listings of the repo were run while building the worklists and this summary (to find record ids and to locate one Salvian sentence); nothing was read through. Non-English vendored texts were counted, not read. Rights for outside sources come from edition dates and hosts as the reports state them, not page-by-page checks, and "not stated in report" means the report gave none. The seven worlds without records (aec, hus, jes, meth, obel, rcg, wsyr) were mapped only for C3 and appear only as acquisition cells. Readability of spoken fields was not graded. Whether lpc drafts are in a compiled package was not checked. The C16 reader classifier was not run; fall-through is judged from the routing regex. C17 was not mapped. Counts are the reports' own and are not reconciled where they differ (C16: 73 in the prose, 64 in the table; C5: 32 and 36; C13: 25 and 26; C12 gives `On Infants' Early Deaths` at line 443 where the other reports give 32849). The worklists mark rows whose cluster or sub-question the report did not name with "*" or "fleet".
