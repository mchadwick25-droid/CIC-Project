# R3 recheck, part C: era 3 batch 6

Scope: `constantius-of-lyon`, `faustus-of-riez`, `gennadius-of-marseilles` and `ruricius-of-limoges`, with their briefs, cards, audio scripts and `records.json` entries in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch6/`; the clauses of Open-Gaps 251 and the batch README on these ids. Round 3 of 3, a targeted recheck.

## Method

I am a fresh Opus reviewer. I did not draft, review or fix these files in rounds 1 or 2. I read `CLAUDE.md` in full, part C of `R2_recheck.md` and `R2_changes.md`, and the brief for this round. I read every change since R2 began as a word diff from `1304da0b` ("R2 recheck, parts B and C") to HEAD (`c7b84b31`). The four `records.json` entries were diffed one by one by script. The diff holds the R2 fixes, the lead's removal of empty `"date": null` keys, and the American-spelling pass. For every R2 finding, and for every changed string, I opened the cited lines in the vendored file myself and asked who speaks there: the ancient writer, an editor, a note or an apparatus. I read the Open-Gaps and README clauses against the cards, the records, `cic-website/data/world-census.json` and `cic/corpus-map/`. I edited no profile file, and made no git write, model, web or paid call. Line numbers point to files under `cic/texts/` unless another path is given.

Mechanical checks, all four:
- Each audio script equals its brief once `[calmly] ` and `[warmly] ` are removed (checked by script). Each has one of each tag, and no tag appears in a brief.
- All four cards and `records.json` parse.
- `tools/check_spelling.py` on the four briefs, four cards and `records.json`: 0 British spellings. The spelling changes are all in our own prose or in modern renderings: "labor" (Faustus brief, inside Opus's modern rendering, so American spelling is right), "favored" (Faustus card and records paraphrase), "harbor" (Ruricius brief), "catalog" (Gennadius card and records paraphrase). No verbatim quotation from an edition was respelled.
- The removed `"date": null` keys leave every entry with title, author, language and file. No other field moved.

| Profile | Words | Est. @162 | FK | Flesch | Cap |
|---|---|---|---|---|---|
| Constantius of Lyon (recorder) | 323 | 2:00 | 8.0 | 66.1 | within 325 |
| Faustus of Riez | 324 | 2:00 | 8.1 | 63.1 | within 325 |
| Gennadius of Marseilles (recorder) | 325 | 2:00 | 8.2 | 64.0 | 325, at the cap |
| Ruricius of Limoges | 324 | 2:00 | 7.3 | 66.8 | within 325 |

## 1. R2 findings

| Finding | Status | Evidence |
|---|---|---|
| R2-C-M1 (Constantius card `uncertain` 6) | RESOLVED | The item now reads "…he reverses this, and holds that the writer of that Life… drew on Gregory." and "Levison also says the text in common use was a much-interpolated second Life, and Duru's edition reprints that second Life." Levison: "Vita altera admodum interpolata" (levison1920 l.659-661); "Textum vulgatum interpolationibus refertum esse" (l.703); "Vitae Germani secundae (§ 18 — 37, AA. SS. Iulii VII, 206 — 210; Duru l. l I, 57— 66)" (l.599); Duru "editionem Boschianam iteravit" (l.1619-1621). The colon-reveal is gone and no sentence runs past 25 words. Records side 2 carries the Duru clause with l.599, 1620-1621. |
| R2-C-M2 (Constantius records, citation lines) | RESOLVED | Krusch's note 2, "Hoc caput Gregorius fere ad verbum cum Vita S. Germani Autisiod. a Constantio composita convenit; lib. I, c. 7, Duru" stands at arndt-krusch1885 l.44307-44310 (OCR "llnc capnt Grcgnrins"). "lam jiuUus dubito" is at l.66258, and the page head "ADDENDA ET EMENDANDA. 883" at l.66231. |
| R2-C-M3 (PL 48: a dissertation, not a note) | PARTLY | The card `uncertain` 2, the records claim and its witness, and the first mention in `absent_details` now say "dissertation". Heading confirmed: "APPENDIX SECUNDA … DISSERTATIONES SEPTEM" (pl48 l.18388-18399). The same `absent_details` note still closes "Rees and the PL 48 note call him priest" (R3-C-M1). |
| R2-C-M4 (Constantius sources) | RESOLVED | Both entries are in `sources.about` and both files exist. The PL 48 entry has no `date` key, under the lead's ruling. Rees's words "the life of Saint Germanus, written by Constantius, a priest of Lyons" (rees 1853 l.17717-17718) stand in his note to the Life of Cadoc, so "notes" in the title is right. |
| R2-C-M5 (Ruricius brief: "he held nothing against him") | RESOLVED | Brief l.1: "Yet Caesarius held nothing against him." Engelbrecht l.24713-24716, "nihil pietati vestrae vel potuimus vel debuimus inputare". The audio script matches. |
| R2-C-M6 (Ruricius records: era 644) | PARTLY | The era figure is now explained, and the card no longer says the acts give 506. But the new parenthesis says "Bruns gives the variants 643 and 543" and cites l.13760 as a print of the Agde heading. Line 13760 is in Bruns's apparatus to the Council of Vaison II, not Agde (R3-C-B1). The card's new sentence also runs 34 words (R3-C-M2). |
| R2-C-M7 (review history inside records claims) | RESOLVED | All six parentheses and asides are gone. A search of the four entries for "R1", "R2", "brief now", "first search", "review" and "coordinator" finds nothing. The epilogue claim keeps "the brief gives this in Opus's modern English", as the finding allowed. |

R1 C-M7 (logging the truncated Levison file) is now Open-Gaps 251's Library clause; see section 3.

## 2. The "in 506" question

**The question.** In R2 the era printed with the Agde acts, 644, gives AD 606. So the records retagged 506 as Engelbrecht's reckoning, and the card dropped "whose acts date it to 506". The Ruricius brief still says "in 506" with no source named. Is that fine?

**Judgment: it is fine as told. No change to the brief.** The year is not one editor's guess. Three held witnesses give 506, and none of the held sources gives a different year:

- **Bruns's own dating apparatus.** Bruns heads the council "CONCILIUM AGATHENSE" with no year (l.10481). His note 3 gives the codices' datings (l.10498-10501): "Conc. Agath. viginti quinque episcoporum habitum era 644 [643 JE.], Anno vicesimo secundo Alarici regis sub die tertio Idus Septembris … Messala v. c. consule habet Corbej., Jes. A, B, Reg. B; in aliis deest nota consularis" (OCR "tertiq", "Septenibris", "CQnsvlm"). "JE." is one of his Spanish codex sigla (compare "JE. BR. E. 3. T. 1. 2.", l.882). So the era and its variant come from the Spanish codices, and the consul from the Corbie, Jesuit and Reg. B copies. Bruns's own year is in his table of contents: "LXXI(XLVII) Can. Conc. Agathensis . . a.506 145" (l.22833), and again in his index, "…gattieiise «. 506 n. 145" (l.22953, OCR).
- **Engelbrecht:** "anno enim 506 (sub d. III Idus Septembris Messala u. c. consule…)" (engelbrecht1891 l.2933-2934).
- **The unsigned PL 67 prolegomenon**, already among the Ruricius card's sources: "Anno 506 Caesarius ad concilium convocavit episcopos" and "sub die III idus Septembres, Messala V. C. consule, id est anno Christi 506, Alarici Gothorum in Gallia regis 22" (pl67 l.96489-96496; OCR "Ciesarius", "Chiisti", "Alariei").

The consul Messala fixes the year. The era figure is a scribal fault in the Spanish copies, not a rival dating. A brief may give an agreed year as a plain date, as other briefs in this series do. The card's "which August Engelbrecht reckons as 506" names one witness of three. That is true and not misleading, so I raise no finding on it. The records retag to Dominant Modern Reconstruction is cautious but defensible. A change of tag now would be churn, so I do not ask for one. The records should name all three witnesses, though, and they should drop the wrong "543" (R3-C-B1).

## 3. New findings

One blocking point in the records and one in Open-Gaps 251; three minor, and one note that is not a finding. None touches a brief, an audio script or a card fact.

**R3-C-B1 BLOCKING (Ruricius records, claim "Agde 506": a variant cited from the wrong council's apparatus).**
Evidence: the R2 parenthesis reads "Bruns gives the variants 643 and 543", and the witness cites "bruns … l.10498-10500, 13760". Line 13760 is not a second print of the Agde heading. It is note 1 to "CONCILIUM VASENSE SECUNDUM" (heading l.13728, running head "CONCILIUM VASENSE II." at l.13711), on the canon "Ut presbyteri per parochias juniores lectores domi nutriant" (l.13739): "decem et septem episcoporum add. solus Reg. F; viginti quinque episcoporum habitum era 644. [543. JE.] Codd. Hisp." That is Bruns's apparatus to Vaison II (529). For Agde, Bruns gives only 644 and "[643 JE.]" (l.10499). R2's own evidence for this finding called l.13760 "Bruns's second print of the heading". This is the slip, and the change copied it forward. A checker who follows the citation lands on another council. The brief and card do not depend on it.
Fix, in the claim, replace the parenthesis "(the era figure as printed, 644, gives 606, not 506, and Bruns gives the variants 643 and 543; the year rests on the twenty-second year of Alaric and the consul Messala, which Engelbrecht reckons as 506, l.2933-2934)" with:
"(the era figure of the Spanish codices, 644, gives 606, not 506, and Bruns's codex JE. reads 643; the year rests on the twenty-second year of Alaric and the consul Messala, which Engelbrecht reckons as 506, l.2933-2934, as do Bruns's own table, 'Can. Conc. Agathensis . . a.506', and the PL 67 prolegomenon, 'Messala V. C. consule, id est anno Christi 506' (OCR 'Chiisti'))".
Witness, replace with: "Bruns, Canones II (bruns_canones-apostolorum-et-conciliorum-pars-altera-lat_1839 l.10498-10501; table of contents l.22833); Engelbrecht (faustus-riez engelbrecht1891 l.2933-2942); prolegomenon, PL 67 (facundus-ferrandus-caesarius-dionysius-pl67-lat_migne1865 l.96489-96496)". Keep the tag as it is.

**R3-C-B2 BLOCKING (Open-Gaps 251, "List lines": a false absence for Constantius of Lyon).**
Evidence: "Constantius of Lyon, Severinus of Noricum and Ruricius of Limoges are named nowhere in the census." The census names Constantius of Lyon in two person entries. In Germanus of Auxerre (`movements[463]`, id `germanus-of-auxerre`), the long description has "Now, Constantius of Lyon writes, Germanus…". The card has "Constantius of Lyon wrote his Life, by Levison's date about 480 or a little after" (`legacy.remembered` 1), "Bede took the British chapters of Constantius of Lyon's Life…" (`legacy.traces` 1) and "Most of his story comes from Constantius of Lyon's Life…" (`uncertain` 0). It also lists him as the author of a source. In Hilary of Arles (`movements[464]`), `legacy.remembered` 0 reads "Constantius of Lyon, in his Life of Germanus of Auxerre, calls him…". He has no people row and no voice. A search of the census for Ruricius and for Severinus finds nothing, so those two halves stand. The map Who build slice is told to place him as if he were new to the census, when two entries already cite him.
Fix: "Constantius of Lyon has no people row, but the Germanus of Auxerre entry and the Hilary of Arles card name him as the writer of the Life of Germanus. Severinus of Noricum and Ruricius of Limoges are named nowhere in the census."

**R3-C-M1 MINOR (Constantius records, `absent_details` "His family, birth, death, orders"; R2-C-M3 left half-done).**
Evidence: the note now says "Marius Mercator PL 48, an unsigned dissertation calling him 'Constantius presbyter'", but closes "Rees and the PL 48 note call him priest, Isidore bishop."
Fix: "Rees and the PL 48 dissertation call him priest, Isidore bishop."

**R3-C-M2 MINOR (Ruricius card `uncertain` 2; the new sentence runs 34 words, with a loose "which").**
Evidence: "Its acts date the council to the twenty-second year of King Alaric, with the consul Messala in some copies, which August Engelbrecht reckons as 506; the Spanish era printed with them, 644, does not fit that year." "Which" can attach to "some copies" as easily as to the date, and the semicolon joins two thoughts (`Who_Profile_Pattern.md` item 4; CLAUDE.md, nothing past about 25 words). The facts are right: Bruns has the consul only in "Corbej., Jes. A, B, Reg. B; in aliis deest nota consularis" (l.10500-10501).
Fix: "Its acts date the council to the twenty-second year of King Alaric, and some copies add the consul Messala. August Engelbrecht reckons this as 506. The Spanish era printed with the acts, 644, does not fit that year." The rest of the item is unchanged.

**R3-C-M3 MINOR (Open-Gaps 251, "List lines" on Faustus: an unchecked "only", and a census error it should log).**
Evidence: "Faustus of Riez is named only in the text of the Gallic monastic entry". He is also named in the note on the link `gallic-monastic-ascetic-christianity--merovingian-gallic-christianity` (`edges[26]`): "Gennadius tells of Faustus, the first abbot of Lérins, who became bishop of Riez." That note misreads Richardson's English. Richardson has "Faustus, first abbot of the monastery at Lerins, and then made bishop of Riez" (npnf203 l.43682-43686), meaning first abbot and then bishop, and his own note reads "Abbot of Lerins 433–4". Engelbrecht's index has "Honoratus primus abbas Lirinensis" (engelbrecht1891 l.28706), and the census's own Gallic monastic entry says Honoratus founded the house.
Fix, in "List lines": "Faustus of Riez is named in the text of the Gallic monastic entry ("Faustus, later became bishop of Riez") and in the note on the link from it to Merovingian Gallic Christianity; the Faustus people row is Faustus of Milevis." In "Census text", add: "The note on the link from Gallic Monastic-Ascetic to Merovingian Gallic Christianity calls Faustus "the first abbot of Lérins". It reads Richardson's "first abbot of the monastery at Lerins, and then made bishop" (npnf203 l.43684-43685) as an order of abbots. Honoratus was the first abbot ("Honoratus primus abbas Lirinensis", Engelbrecht's index, engelbrecht1891 l.28706), as the Gallic monastic entry itself says. Owner: the coordinator, for the census text."

**Note, not a finding (Bruns on the Alaric year).** I record one point so a later reader does not re-raise it. Bruns's note may mean that the Alaric year, like the era, stands only in the Spanish heading ("cum in nonn. Codd. Hisp.", OCR "noni."). The OCR does not settle this, and the PL 67 prolegomenon gives Labbe's title with both the consul and "Alarici … regis 22". The card's "Its acts date the council to the twenty-second year of King Alaric" is therefore supported as worded.

## 4. Open-Gaps 251 and the README

Clauses on part C ids, each checked against the files:

- **List lines.** Faustus: see R3-C-M3. The Faustus people row is Faustus of Milevis (`movements[10]`, Manichaeism) ✓. Gennadius: no people row or voice, and he is named only in text ✓. Constantius: false absence (R3-C-B2). Ruricius: named nowhere ✓.
- **Card tradition.** Constantius's card reads "British and Welsh Christianity". The Germanus of Auxerre entry is `toldWithin: british-welsh-christianity` ✓. Constantius is called "a man of Lyon" ✓ (card `place`, "Lyon, in Gaul"). Ruricius's corpus-map row `faustus-riez_de-gratia-and-collected-works_engelbrecht1891--ruricius-limoges-letters` has `confidence: needs-ruling`, and its note says "Which Gaul entry holds him is a needs-ruling" (`cic/corpus-map/merovingian-gallic-christianity.yaml` l.67-74) ✓. His card reads "Merovingian Gallic Christianity" ✓.
- **Library (the truncated Levison file): correct.** I checked the truncation two independent ways.
  - Bytes: `od -c` on the last 300 bytes ends "E t   i d e o   i n   s c r i b e n d o   s u c c i n c t u m ^ \n". The file has 4580 lines, and l.4580 is the last.
  - Structure: the page head "… AUCTORE CONSTANTIO. 283" is at l.4571, and the epilogue starts at l.4574 and breaks off mid-sentence. The only "Explicit" in the body after the header is a variant reading in the p.282 apparatus, "Explicit vita sancti Germani episcopi A 6" (l.4550). No EXPLICIT line and no p.283 apparatus follow.
  - The header promises the text "through 'EXPLICIT VITA SANCTI GERMANI EPISCOPI' (p. 283)", pp. 225-283, from archive.org `passionesvitaequesanctorum5` (header l.3, 7, 9) ✓.
  - "No profile claim rests on the missing text" ✓. The epilogue claim cites l.4574-4579, which is held, and the brief's rendering covers only "Deum testor … tacuisse" (l.4577-4579).
- **Not held.** The Library has no Sidonius file; the only Sidonius hits are in other works. His letters to Constantius and Ruricius come through Levison and Engelbrecht ✓. No English of Faustus, Ruricius or Constantius is held; Levison's header says no public-domain English exists ✓. Gennadius's works against the heresies and his letter to Gelasius are named as not held, consistent with the card.
- **Scan corrections.**
  - Faustus "c.405/410-c.490/495" is the header (engelbrecht1891 l.2). Engelbrecht: "Faustum non multo ante annum 410 natum esse statuam" (l.163); "Quo anno mortuus sit Faustus, prorsus incertum est" (l.365) ✓.
  - Gennadius "died 496": Richardson's note "Died 496." (npnf203 l.43968) and Jackson ✓. "Richardson thinks a later hand added it": "This compels the rejection of the paragraph on Gennadius himself as by a later hand" (l.38478-38479) ✓.
  - Constantius "fl. c.480" is Levison's date ✓.
  - Ruricius "c.440 to c.507" is the header (engelbrecht1891 l.2) ✓, and 485 is Engelbrecht's reckoning ✓.
  - "The Ruricius who signs councils in 535 and 541 is his grandson, by Leo's index to Fortunatus" ✓. Leo has "Ruricii episcopi Lemovicini. Eorum epitaphium IV, 5. [Ad alterum c. a. 507 mortuum … alter nepos illius interfuit concilio Arverno I. a. 535, Aurelianensi IV. a. 541, V. a. 549 per Bantaredum archidiaconum subscripsit]" (leo-krusch1881 l.53125-53130; OCR "Huricii", "51)7", ",541"). The card's `uncertain` 5 says the same and adds 549 through the archdeacon.
  - Faustus's "the semi-Pelagian reply" told as fact, against Engelbrecht ✓ (card `uncertain` 1; engelbrecht1891 l.652-670 per records). Constantius's "only near-contemporary Life" as an unchecked "only" is a description of the scan and is fair.
  - Caesarius is not named in the scan-corrections clause, so there is nothing to check there.
- **README.** Line 5 names Constantius, Severinus, Faustus and Gennadius as the first era 3 WHO rows of the supplement scan "by best held date", then Ruricius in Benjamin's place. That order matches the dates the cards give: c.480, about 482, c.490/495, 496, then c.507. The supplement scan rows (Who_Scan_Supplement.md l.136, 147, and the follow-up pass at l.38 for Ruricius) agree ✓. Line 7 makes Constantius and Gennadius recorders at standard length, and Faustus and Ruricius standard ✓. "None is a live person entry" holds for all four.

## 5. Verdicts

- **Constantius of Lyon: CLEAR.** One minor records wording (R3-C-M1). The Open-Gaps false absence (R3-C-B2) is in the tracking entry, not the profile.
- **Faustus of Riez: CLEAR.** The census point (R3-C-M3) belongs to Open-Gaps, not the profile.
- **Gennadius of Marseilles: CLEAR.**
- **Ruricius of Limoges: NOT CLEAR on one records point (R3-C-B1).** The brief, audio script and card are sound, and "in 506" stands. The records claim cites a Vaison II apparatus line as an Agde variant. The fix is a one-clause, ready-to-apply replacement. Since this is round 3, it goes to the cap ruling as a records-only correction. R3-C-M2 is a card sentence split with no change of fact.

Open-Gaps 251 needs R3-C-B2 and R3-C-M3 applied before it is committed as final.
