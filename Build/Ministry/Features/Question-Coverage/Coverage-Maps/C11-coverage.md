# C11 coverage map: Jews, pagans, Muslims, other religions

Read-only pass, 26 October 2026; nothing in the repo was edited. Claims were checked against `records/<code>/` front matter and `cic/texts/`; files, lines and verification results are in `search/C11/C11-coverage.json`. Tool runs: `S1-jews.json` to `S8-rivals.json` (re-run, all clean).

## The sub-questions

Ids follow `repo/07-subquestions.yaml`.

| id | sub-question | question ids |
|---|---|---|
| S1 | Jews: what was said, blame, harm, practices kept, Jewish Christians, "to my face" | C11-05, 06, 11, 12, 16 |
| S2 | Pagans and their gods; eating and festivals; Rome | C11-08, 14, 20 |
| S3 | Greek philosophy; pagan authors quoted | C11-13, 21 |
| S4 | Muslims (worlds after 632 only) | C11-07, 17 |
| S5 | Can a good pagan be saved; one way; all worship | C11-01, 09, 23, R-26 |
| S6 | Would you have converted me; is trying wrong | C11-10, R-38 |
| S7 | Rivals: gnostics, Manichees, Marcion | C11-19 |
| S8 | Respect; India; atheists; the spiritual-but-not-religious; rabbis and Josephus; the outsider's view | C11-02, 03, 15, 18, 22, R-37 |

## Layer table

R = RENDERED, R* = a record exists but answers only part, or only as an honest_limit or guard, L = LOADED (vendored, mapped, read in context, no record), I = IDENTIFIED, "-" = nothing, out = out of window.

| world | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 |
|---|---|---|---|---|---|---|---|---|
| alx | R* | R* | R | out | R | R | R | R* |
| cappadocian | R* | R | R | out | - | R* | R | R* |
| desert | - | R* | R | out | R | R* | R | R* |
| don | L | R* | R* | out | R* | R* | R | R* |
| gallic | L | R | R* | out | L | R | R | R* |
| hal | R* | R* | R | out | R | R* | R | R* |
| ijc | R* | R | L | out | R* | R | R | R* |
| lpc | L | R* | L | out | L | R | R | R* |
| pahc | R* | R | R | out | R | R | R | R |
| rzg | L | L | L | L | R* | R* | R | L |
| syr | R | R* | R | out | R | R | R | R* |
| witt | R* | R* | R* | R* | R | R* | R | R* |

Windows (`records/worlds/<code>.yaml`): ten worlds end by 451; only rzg (1519-1650) and witt (1517-1580) fall after 632. Worlds without records (aec, hus, jes, meth, obel, rcg, wsyr) are in the JSON only.

Canon cells, recounted from demonstration front matter. F6-T has 7 demonstrations: 2 for f6-t-01 (alx, hal), 5 for the divorce variant f6-t-03 (alx, hal, desert, pahc, syr), none for f6-t-02 ("too narrow", C11-01). cappadocian, don, gallic, ijc, lpc, rzg and witt have none. F3-P has 3, all f3-p-02 (don, gallic, lpc draft); none for f3-p-03 (the temples and the old gods).

Verification: 30 quote records cited as RENDERED were re-searched in their vendored files; 27 match exactly, 3 after spacing only (Aphrahat Dem. XXI, Sozomen, Jerome Ep. 108). None differs in wording.

## World by world

**alx.** Strongest on philosophy (Clement's schoolmaster, verified; also his Indian Gymnosophists) and on the one-way question (the f6-t-01 demo). Thin: gods as demons, festivals, idol-meat, the Serapeum (nothing in any record), Muslims out of window. Add: Origen, Against Celsus VII-VIII (anf04), a Jewish-blame contested_claim.

**cappadocian.** Julian's own words (verified) and Basil's Address (vendored, unquoted). Nothing on whether a good pagan is saved, and Open_Gaps line 667 already says so. Add: an honest_limit; Nazianzen and Nyssa as the loaded ground.

**desert.** The model honest limit on outsiders (`desert.limit.outsiders-condemned`). Nothing on Jews or pagans except the heathen-priest sayings, loaded and unrendered.

**don.** Refuses to answer for the one-way question (`don.dw.the-line-we-actually-drew`). Pagans enter only as persecutors the Donatists did not die under. Nothing on Jews.

**gallic.** Fullest pagans cell: temples burned, the devil as Jupiter, church-or-circus. Its `heathen-rustics` not_for forbids judging the burning as intolerance. Nothing on Jews or a good pagan's fate.

**hal.** Ep. 70 on quoting pagan authors (C11-21) is loaded and unrendered. See the Jewish visitor.

**ijc.** Altar of Victory lets Symmachus speak. Callinicum owns the harm. No record on philosophy.

**lpc.** 330 draft records; none on Jews, gods or philosophy. R-38 is the best in the fleet (three-phase compel demo). Loaded: Cyprian Ad Quirinum, City of God.

**pahc.** The only full S8 and the fleet's best S5: Justin's reasonable livers (verified), the "atheist" charge, both answers held with a not_for against the pluralist reading. Dialogue 47 (Jewish Christians "will be saved") is unrendered.

**rzg.** Almost all LOADED. No Muslim record in an Islamic-era world. Zwingli's saved pagans are unvendored (Latin Works vol. 2).

**syr.** Best on Jews and philosophy ("the barbarian philosophy", verified). Out of window for Muslims; the Magi are Zoroastrians. Bardaisan on the Brahmans (anf08, line 7420) is unrendered.

**witt.** The only Muslim material: `witt.term.the-turk`, a prayer and "no other account". Gerlach's Istanbul diary (237 hits) and Luther on the Turks are loaded and unused.

## The Jewish visitor (C11.S1)

Records only; no answer is written. "Guard" is the record's `not_for`.

**alx.** No anti-Jewish polemic record exists. Reachable: `quote.clement-schoolmaster`, `term.christological-reading`, two forces. The guard does not hold against supersession. Bare, the quote says the Law was a custodian for the Hebrews, now done. Hostile text: Origen, Against Celsus (anf04 line 62905, blame on Jewish guilt); Athanasius (npnf204 line 36486).

**cappadocian.** `story.basil-death-funeral`. Guard holds (the encomiast's claim). Bare, Jews mourning would look like proof of good relations. Nyssa and Nazianzen on Jews are unread.

**desert, don, gallic, lpc, rzg.** No record. Hostile text is mapped for four: lpc (Cyprian, Ad Quirinum; Augustine's witness-people), don (Augustine, npnf104 line 5203), rzg (Calvin: "whose blindness is well known"), gallic (npnf211). Desert maps none at work level.

**hal.** `quote.oea-tumult`, `story.oea-gourd`, `quote.no-one-preferred-to-the-seventy`, Hebrew-teacher records. Guard fails on the story: it says the Jewish residents answered "whether from ignorance or spite" (Augustine, Ep. 71.5, line 32546) and its not_for does not stop that. Jerome's own lines (npnf206 line 8405) are unrendered.

**ijc.** `story.callinicum-synagogue`, `demo.hypocrisy`, `limit.earlier-windows`. Guard holds; the Jewish community has "no voice". One blur: the limit says "our own bishop kept unpunished", the story has the Callinicum bishop urging it and Ambrose shielding it. Ambrose's Ep. 40 ("a home of unbelief", line 43280) is unrendered.

**pahc.** `witness.hard-texts` (Marcion; guard holds), `quote.polycrates-to-victor` (Passover date; no Jewish guard). Barnabas and the Dialogue with Trypho are mapped and unrendered.

**syr.** `term.anti-jewish-polemic`, `quote.aphrahat-anti-jewish-frame`, `quote.a-man-called-wise-amongst-the-jews`, `dw.unsettled`, `dw.failures`, `demo.someone-like-me`. Guards hold on every one: no verdict today, no invented Jewish reply, no invented dissent. Bare, Dem. XVII.1 states what Jews did as fact, and Dem. XXI gives the Jewish sage only as Aphrahat retold him. Unrendered: the Addai legend ("destroy those Jews who crucified Him") and Sozomen's "co-operation of the Jews".

**witt.** `dw.what-we-have-never-settled` and `contested.1543-treatise-later-effect` disclose the 1543 treatise at existence only; guard holds. Weak: `term.the-turk` world_word files Jews with the Turk as "one of the devil's instruments", and its not_for covers only the modern-political reading. The 1523 and 1543 texts are unvendored.

## Findings

1. The Library holds no Jewish voice: no Josephus, no rabbinic text, no Philo. Every Jewish voice a world can reach is a Christian's report of one. C11-02 is a Library gap.
2. Three unguarded edges: `hal.story.oea-gourd`, `alx.quote.clement-schoolmaster`, the `witt.term.the-turk` world_word. Five worlds have nothing on Jews while lpc and rzg map hostile text.
3. Ten worlds are out of window for Muslims and none says so. The two in window have a prayer and silence, and both map firsthand Ottoman material (Gerlach, Lucaris) that no record uses.

## Other sources (working knowledge; not fetched)

Whiston's Josephus (1737) for S8; Danby's Mishnah (1933) or Schechter's Talmud extracts for S1; Sale's Koran (1734) for rzg and witt; Aphrahat Dem. XI-XIX in Parisot's Patrologia Syriaca (Syriac and Latin). Editions and licences need the Library thread to confirm. Rows are in the JSON.

## Not checked

- `canon/sealed_probes/` was not read.
- Shared NPNF/ANF volumes yield other authors' hits; hostile-text lists are targeted greps, not read through.
- Readability of spoken fields was not graded; lpc records are drafts and their place in the package was not checked.
