# C10 coverage map: money, the poor, work

Read-only pass, 26 October 2026; nothing in the repo was edited. Every claim was checked against `records/<code>/` front matter and `cic/texts/`; file paths, line numbers and verification results are in `search/C10/C10-coverage.json`.

## The sub-questions

The 22 C10 questions group into seven (ids as fixed in `07-subquestions.yaml`):

| id | sub-question | canon / question ids |
|---|---|---|
| S1 | Was wealth a sin; the rich young man, the camel, prosperity teaching | C10-01 (F5-T), 07, 10, 18, 19 |
| S2 | Giving: tithe, alms, alms and forgiveness | C10-02 (F4-T), 16 |
| S3 | Sharing in common as in Acts | C10-12 |
| S4 | Care for the poor, widows, orphans, the sick, non-Christians | C10-06, 15, 22 |
| S5 | Usury and lending | C10-08 |
| S6 | Who paid for churches and bishops; accounts, corruption, paying to belong | C10-09, 14, 17, 20, 21 |
| S7 | Work and class: barred jobs, who the members were, who paid for the way of life | C10-03 (F5-I), 04, 05, 11, 13 |

**Canon demonstrations: zero.** No world has a demonstration for money and poverty (F5-T, canon f5-t-02), tithe (F4-T, f4-t-02) or work (F5-I, f5-i-07). The only demonstrations in these cells answer other questions: F4-T "born again" in don and hal; F5-I women's own words in alx, gallic, hal, witt and "ordinary day" in ijc. What stands in for them are tagged witnesses, limits and quotes (e.g. cappadocian, don, lpc, pahc, witt each have an F5-T witness).

## Layer table

R = RENDERED (a record speaks to it), R* = honest_limit or guard only, L = LOADED (vendored and mapped, read in context, no record), I = IDENTIFIED, O = OTHER, "-" = nothing. IDENTIFIED and OTHER are listed in the JSON per cell, not as table codes.

| world | S1 | S2 | S3 | S4 | S5 | S6 | S7 |
|---|---|---|---|---|---|---|---|
| alx | R | R* | L | R | L | L | L |
| cappadocian | R | R | R | R | R | R | R |
| desert | R | R* | R | R* | L | R* | R |
| don | R* | R* | L | R* | L | R | R* |
| gallic | R | L | R | R | L | R* | R |
| hal | R | R | L | R | L | R | R* |
| ijc | R* | R | L | R | L | R | R* |
| lpc | R | R | L | R | L | L | L |
| pahc | R | L | R | R | L | L | R* |
| rzg | R* | L | L | L | L | L | R* |
| syr | R | L | L | R | L | R | R* |
| witt | R* | R* | L | R | L | L | R |

Totals over 84 cells: R 35, R* 18, L 31, nothing 0. Usury (S5) has records in one world of twelve. `lpc` cells rest on draft records.

Verification: 27 quote records are cited as RENDERED; all 27 MATCH their vendored file. Six needed a manual look after the tool reported a mismatch, and all six were scan noise, not wording changes: a stray OCR glyph (Basil, Longer Rules XXXVII), a footnote mark and "Tor" for "For" (Basil VII), line breaks (Salvian IV.6, lines 5063-5066), a section number and "1" for "I" (Ammianus XXVII.3.14, line 23191), letters-only matches (Salvian Trier, hyphens and notes), and a page marker (Pachomius tablet, not cited).

## World by world

**Cappadocians (cappadocian).** The only world with records in every cell, and the one with the biggest unused asset. `cappadocian.dw.wealth-answerable-to-the-poor` (F5-T), the barns story and `term.pleonexia` say the famine homilies are "unverified" and "unacquired", so no quote record exists. But `npnf208_basil-letters-select-works.xml` carries English extracts: Homily on Psalm 14 against usury (5069-5284, "the borrower bends to necessity and is beaten"), Homily VI on Luke 12 ("Do not wait for a famine before thou openest thy barns", 6272) and Homily VIII on the famine (6926). Must add: quote records from those lines for S1, S4, S5, with the Prolegomena translator named. Nazianzen's Oration 14 and Nyssa's De pauperibus amandis are registered, unvendored (IDENTIFIED).

**Desert (desert).** Strong on renunciation (Antony's call, Melania, Ladder; four quotes verified) and on work: `gravity.manual-labor` and `term.cheironaxia` are tagged F5-T and F5-I. One real defect: `desert.limit.tithe` (Documented) says no source names a tithe, but its check covered only the Vita and Palladius. Cassian, Conference XXI (`npnf211` 44550-44680), mapped to this world, discusses tithes and first-fruits and says renouncers go beyond them. Narrow the limit or add the passage. Unrendered: Palladius ch. XXXII (`palladius_lausiac-history_clarke1918.txt` 405) lists the Panopolis trades: 15 tailors, 7 smiths, 4 carpenters, 15 fullers.

**Donatists (don).** `don.dw.silver-and-the-goods-of-the-poor` (F5-T) is the most documentary money story in the fleet: Lucilla's 400 pieces and the 320 inquiry. It refuses any claim on Donatist teaching, and the F4-T witness retrieves on "tithed" then bars an answer, so S1 and S2 are guards. Optatus III.4 (`optatus_against-the-donatists.txt` 2002) on Axido and Fasir wiping out debts is hostile, loaded and unused.

**Gallic monastics (gallic).** Strong on renunciation and the poor: Martin's cloak, Cassian's guest as Christ, Salvian's "rich murdering the poor" (all verified), and Martin's discharge as the one barred-job story. Nothing on tithes (Conference XXI is loaded), usury (Cyprian, De lapsis on bishops "multiplying usuries", `anf05` 43784) or who paid for bishops.

**Jerome's circle (hal).** Good: Paula's divestment is correctly a contested_claim; "we did not tithe" (`hal.dw.practices`, F4-T); Fabiola and Portus quotes verified; patronage records. Thin on ordinary members: the "educated rich" charge (C10-05) is answered only by implication.

**Imperial-juridical (ijc).** Leo's collections without a fixed tenth (`ijc.dw.collections-discipline`) is a clean S2 answer. `ijc.limit.marriage-money` (F5-T) admits money is seen "from above". Leo's Letter on usury (`npnf212` 1549) and Ambrose on ransoming captives are loaded, unquoted.

**Latin pastoral (lpc, building).** `lpc.witness.almsgiving-quenches-sin` (F5-T, draft) covers S1 and S2 well, and the ransom story covers S4. The loaded library is richest here and unrendered: Cyprian on usury, stipends and Acts 4; Augustine on tithes, the common life, and actors and trades (City of God). All draft.

**Post-apostolic house church (pahc).** `witness.marriage-and-wealth` (F5-T, Hermas's elm and vine) and Lucian's widows, orphans and common property (both quotes verified). Unrendered and loaded: Tertullian, De idololatria on barred trades (`anf03_tertullian.xml` 4968-6200; schoolmasters 5484, military service 6145) and Polycarp 10, "alms delivers from death" (`anf01` 3512).

**Zurich and Geneva (rzg).** `rzg.limit.no-teaching-on-wealth-or-marriage` (F5-T) is true of the records but not of the library: Calvin's Institutes (vol. 3, 2436, deacons and the poor) and Zwingli on tithes, usury and Anabaptist community of goods (Selected Works 5519; Latin Works vol. 3 5478) are vendored. The 1541 Ordinances are registered, unvendored.

**Syriac (syr).** Best ground for accounts and trust: the rich "trusted no one to handle the giving honestly", Ephrem appoints himself hospitaller (three quotes verified). Aphrahat, Dem. VII (hallock 44) on alms is unrendered. Alms and usury hits in `npnf213` and `npnf208` are Gregory the Great and Basil, not Syriac.

**Wittenberg (witt).** Poor-man warning from the Large Catechism (F5-T, verified) and calling and office terms (every trade has its own office). Tithe is a guard. Loaded and unrendered: Apology on "community of property" (7025), Luther on usury (`luther_works-v1` 6560).

**Alexandria (alx).** Clement's possessions quote (F5-T, F4-T, verified) and plague nursing. Everything else is loaded only; work and class have no evidence beyond Origen's four obols a day (`npnf201` 32818).

## Other sources (outside the repo; from working knowledge, not fetched)

Nyssa, De pauperibus amandis and Nazianzen, Or. 14 (Greek, PG 46 and 35; the English is in copyright); Basil's two homilies in Greek (PG 29, 31); Salvian, Ad ecclesiam (CSEL 8, 1883); Aphrahat, Dem. XIV and XX (Parisot, Patrologia Syriaca I, 1894-1907); Zwingli on divine and human righteousness (Zwingli Werke 2, 1908) and Calvin's Ordonnances (Opera Calvini 10/1); Luther's usury sermons and Common Chest ordinance (WA, German; the 1931 Holman English enters the US public domain on 1 January 2027); Ambrose, De Nabuthae (PL 14). Editions and licences are in the JSON `other` block.

## Not checked

- `canon/sealed_probes/` was not read.
- The first agent's S1 to S5 JSON files were missing; those runs were redone.
- The tool scans whole mapped files, so LOADED hits can belong to another author in a shared volume (Gregory the Great in npnf213, Cyril in npnf207, Basil in npnf208 for syr); flagged where seen, not every line was traced.
- Non-English vendored texts were counted, not read. The Sayings (Budge vol. 2) and Apostolic Constitutions were not mined for S4 and S7. Zwingli and Calvin tithe hits were not traced to editor or author.
- Which `lpc` draft records reach the compiled package was not checked. Readability of spoken fields was not graded.
