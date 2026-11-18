# R4 cap check: Babai the Great, Ruricius of Limoges, Open-Gaps 251 (Mark's cap ruling, 2026-11-14)

## Scope

One targeted check, ordered in Mark's cap ruling ("One targeted check", 2026-11-14), of these strings only:

1. Babai the Great and Braun's German Life of George (`cic/texts/persian-martyr-acts_ausgewahlte-akten-persischer-martyrer-bkv22-deu_braun1915.txt`):
   - a. `era3/batch6/records.json`, `babai-the-great`, the claim opening "Babai's Life of George, in Braun's German", its parenthesis and line numbers.
   - b. Same entry, `absent_details` "A Syriac or English text of his own books".
   - c. `era3/batch5/records.json`, `henana-of-adiabene`, `absent_details` "A second witness to Babai's doctrinal charges" (all of it), and the batch 5 diff against `origin/main`.
   - d. `Open-Gaps.md` entry 251: the Babai clause in "Not held" and the "Correction to batch 5" clause.
   - e. `era3/batch6/babai-the-great.card.json`, `keyWorks[1].about`, the two Braun sentences.
2. `records.json`, `ruricius-of-limoges`, the Agde (506) claim (`claims[2]`): the parenthesis on the era figure and the dating, and its witness.
3. Open-Gaps 251, "List lines", every sentence, against `cic-website/data/world-census.json`.

Nothing else was reviewed. No other file in this audit folder was read before this verdict.

## Method

- **Braun.** The Life of George runs from l.12419 (title) to l.15453 ("Amen. Amen."). The Namenverzeichnis starts at l.15459. I pulled every footnote in that span (82 blocks, each starting with a marker of the form `1)`, `*)`, `x)`, `J)`, `:)` and so on) and read each one. I also grepped the span, allowing for the scan's double spaces and OCR, for `übergeh`, `übergang`, `gebe ich`, `es folg(t|en)`, `setzt sich`, `Lücke`, `kürz`, `weggel`, `ausgel`, `habe ich`, `nur die`, `im Text`, `hier folg` and `fort in`. For each note I checked the anchor point in the text.
- **Other sources.** I read the cited lines in Labourt (l.15740-15870), Chabot (l.42070-42500), Hoffmann 1880 (l.5590-5614), Bruns (l.10470-10501, 22825-22840), Engelbrecht (l.2920-2948) and PL 67 (l.96475-96500).
- **Census.** I walked every string field of `world-census.json` (movements, including `kind: person` and council entries, edges, retiredLinks and retiredMovements). I used name variants: Columb, Moschus/Moschos/Pratum, Biclar/Biclarum/John of Gerona, Bab[aä]i/Babaï/Babhai/Babaeus, Isidor, Faust, Gennad, Constantius/Constance/Life of Germanus/Vita Germani, Severin/Noric/Eugippius, Ruric/Rurik/Limog. I listed every `people[]` name and every movement id.
- I compared quotations with the cited lines character by character. The scan's double spaces were read as single spaces.
- `git diff origin/main -- .../era3/batch5/` shows one file and one line changed.

### Braun's own notes on what he leaves out (whole Life)

| Line(s) | Note (OCR as printed) | Kind |
|---|---|---|
| 12442-12443 | "Von der sehr langen Einteilung [=Einleitung] gebe ich nur die wichtigsten Gedanken." | introduction shortened |
| 13161-13162 | "Das folgende, sachlich belanglose Enkomion auf die Heilige übergehe ich." | passed over |
| 13270 | "Eine hier folgende Betrachtung habe ich übergangen." | passed over |
| 13319-13322 | "Ein langes Enlromion [=Enkomion], worin die Beiden mit den die Bundeslade ... ziehenden Kühen ... und mit dem seinen Sohn opfernden Abraham verglichen werden, übergehe ich." | passed over |
| 13806-13807 | "Die folgenden, sachlich inhaltslosen Ausführungen übergehe ich." | passed over |
| 13362-13363 | "Es folgt zunächst im Anschluß an 1 Kor. 7, 29 — 81 [=31] eine Betrachtung über die Schlechtigkeit der Zeit." (anchor: "was der selige Paulus voraussagte1)", l.13349, then §30 begins) | given only as a note |
| 14944-14947 | "Das Gebet setzt sich, noch lange fort in einem Dank für die Berufung zum Christentum. — ... — , zum Mönchtum und Martyrium." (anchor l.14926) | given only as a note |
| **14995-14996** | **"Es folgen zunächst drei längere Gebete, um Standhaftigkeit, für die Kirche und sein Kloster, für die Häretiker."** (anchor: "erbarme Dich meiner1)", end of §65, l.14963-14964; §66 follows with "Nachdem er ... vollendet") | **given only as a note** |
| 14728 | "Es folgt im Text eine Lücke." | a gap in the Syriac Braun reports, not an omission of his own |

Count: one shortened introduction, four passages passed over, and **three** passages given only as notes. Two of the passed-over passages are called of no substance ("sachlich belanglos", l.13161; "sachlich inhaltslos", l.13806). No other footnote in the span reports an omission. The in-text phrases "nicht übergehen" (l.15169, 15293-15294) are Babai's own words.

## 1a. Records claim "Babai's Life of George, in Braun's German": FAIL (BLOCKING 1)

- The parenthesis reads: "the introduction shortened, four passages passed over and two given only as a note". "Two" is wrong. Braun gives three passages only as notes: l.13362-13363, 14944-14947 and **14995-14996**. The cited lines leave out l.14995-14996.
- The other parts hold. The introduction note is at l.12442-12443, and the four passed-over passages are at l.13161-13162, 13270, 13319-13322 and 13806-13807.
- The quotations are verbatim:
  - l.12424-12425: "verfaßt vom heiligen Rabban Mär / Bäbai, dem Abte auf dem Berge Izalä1)". The footnote mark is dropped.
  - l.12435-12440: "Vor ungefähr dreiund- / dreißig Jahren schrieb ich ... Später schrieb ich die Geschichte seines Nach- / folgers Dädischö' aus Bet Däräje". The quote's "..." stands for the omitted words. The footnote mark after "Kaschkar" is dropped.
  - l.13395-13396: "Er leugnet die Auferstehung der Leiber und (lehrt), daß / es eine Erlösung nur für die Seelen gebe".
  - The heading: "f 14. Jan. 615" (l.852) and "608 — 628" (l.858).

## 1b. Absent detail "A Syriac or English text of his own books": FAIL (BLOCKING 1, MINOR 1, MINOR 2)

- **BLOCKING 1.** The note says Braun "gives a reflection on the times and the rest of George's prayer only as notes (l.13362-13363, 14944-14947)". It leaves out the third such note, the three longer prayers at l.14995-14996.
- **MINOR 1.** The note says the Life is held "as two passages in Chabot's French (chabot1902 l.42080-42240)". Chabot translates three passages of the Life:
  - (i) l.42094-42107, "(Édit., p. 476-477.)";
  - (ii) l.42109-42252, "(Édit., pages 495-505.)";
  - (iii) "Le récit poursuit en ces termes", l.42257-42498, "(Edit. pages [5]05-521.)".
  
  Only the first two are about Henana's doctrines (l.42092-42093: "deux passages" on "ces doctrines"). The cited range also stops before the end of passage (ii), which ends at l.42252.
- **MINOR 2.** A comma is missing after "(l.12442-12443)".
- The other parts hold:
  - The four passed-over passages are described correctly ("two encomia, a reflection and one passage he calls empty of content").
  - Labourt l.15845-16120 holds his quotations of the De Unione.
  - Hoffmann l.5596-5612 holds his extract.

## 1c. Henana absent detail "A second witness to Babai's doctrinal charges": FAIL (BLOCKING 1, MINOR 1); diff PASS

- **BLOCKING 1.** The note says Braun "passes over four passages and gives two more only as notes", and its list of omission lines leaves out l.14995-14996. The correct figure is three.
- **MINOR 1.** "the two passages Chabot gives in French (... l.42080-42240)". Chabot gives three. Two are on the doctrines, and the second of those ends at l.42252.
- The rest holds:
  - Labourt l.15764-15765: "Grâce à l'obligeance de M. Chabot, nous sommes en mesure d'adjoindre à ces textes un traité inédit de Babaï sur l'Incarnation (De unione)". This supports "an unpublished copy Chabot made available to him".
  - Labourt l.15816-15820 is the De Unione note on Henana and the risen body ("D'après le traité De Unione, Henana admettait que le corps du Christ ressuscité ... (ms., p. 126). Ainsi il n'y avait pas de véritable résurrection des corps").
  - Braun l.13355-13400 holds the charges ("Hannänä / Hdajäbäjä2) spie" to "wie Origenes, der Heide der Heiden, gesagt hat").
  - Braun keeps the charges, and Hoffmann l.5596-5612 has them.
  - The Seert and Evagrius sentences were not in scope beyond the text kept from the old note.
- **Diff: PASS.** `git diff origin/main -- .../era3/batch5/` shows `records.json` only, one line changed: this note. Nothing else in batch 5 changed.

## 1d. Open-Gaps 251, Babai clauses: FAIL (BLOCKING 1, MINOR 1)

- **"Not held" clause, BLOCKING 1.** It says Braun's German "shortens the introduction, leaves out four passages and gives two more only as notes". The correct figure is three more.
- **"Correction to batch 5" clause, MINOR 1.** It says the Life of George is held "in Chabot's two French passages and in Braun's abridged German". Chabot gives three. The Labourt citation (l.15764-15866) holds. "Only that absent_details note was changed" is confirmed by the diff.

## 1e. Card `keyWorks[1].about`, the Braun sentences: PASS

"Oskar Braun translates the Life into German. He shortens its long introduction and leaves out or sums up several passages, two of which he calls of no substance."

- Long introduction shortened: l.12442-12443.
- Passages left out or summed up: four left out and three summed up in notes, so "several" holds.
- Two called of no substance: "sachlich belanglos" (l.13161) and "sachlich inhaltslos" (l.13806).

Observation (outside the strings checked): the next sentence of the same item, "J.-B. Chabot gives two passages in French", has the same undercount as MINOR 1.

## 2. Ruricius of Limoges, Agde 506 (`claims[2]`): FAIL (MINOR 3)

- **Bruns l.10498-10501.** The text, OCR as printed: "3) Conc. Agath, viginti quinque episcoporum / habitum era 644 [643 JE.], Anno vicesimo secundo Alarici regis sub die / tertiq Idus Septenibris cum in noni. Codd. Hisp. --> Messala v. c. CQnsvlm / habet Corbej., Jcs. A, B, Reg. B; in aliis deest nota eonsularis."
  - The note is note 3 on the heading of "CONCILIUM AGATHENSE" (l.10481-10485). Line 10498 opens with the end of note 2, which is also on Agde's canons.
  - Era 644 gives 606, and 643 gives 605. JE. is a Spanish-codex siglum: Bruns uses it beside BR., T. 1. 2. and E. 4, and writes "C. H. praeter JE." at l.10634. So "codex JE." is fair.
  - 'Messala v. c. consule' appears "in other codices" (Corbie, Jesuit A and B, Reg. B). That is correct.
- **Bruns l.22833.** "LXXI(XLVII) Can. Conc. Agathensis . . a.506 145". The quote 'Can. Conc. Agathensis . . a.506' is exact.
- **Engelbrecht l.2933-2934.** "anno enim 506 (suh d. III Idus Septembris Messala u. c. / consule, ...)". This is Engelbrecht's 506, with the day and consul.
  - l.2938-2939: "Kuricius neque uenit neque procuratorem misit, sed litteras / tantum per diaconum Ueri episcopi ') Agathen direxit".
  - The whole range l.2933-2942 is his paragraph on Agde. l.2936-2937 cites an earlier conciliar rule ("pridem iam sanctum erat ... cf. Conc. Gall. coll. I 562") inside that paragraph. The claim does not use it.
- **PL 67 l.96489-96496.** "Anno 506 ... Habitum est concilium istud Agattize [=Agathae] (Gallis Agde) ... «sub die m idu: Septembres, Messala V. C. / consule , id est anno Chiisti 506, Alarici Gothorum / in Gallia regis 22". This is Agde. The lines just before (96474-96488) are on Caesarius's ordination and lie outside the cited range.
- **No cited line belongs to another council: confirmed.**
- **MINOR 3 — unflagged OCR emendations.** The claim marks 'tertiq' and 'Septenibris' as OCR but silently emends two more:
  - 'Conc. Agath.' (the scan has "Agath,");
  - 'consule' (the scan has "CQnsvlm").
- Observations, not counted as findings:
  - Engelbrecht's u is printed as v ('venit', 'Veri' for "uenit", "Ueri"). The same entry does this throughout ('vero' for "uero" in claims[3]), so it is a consistent convention.
  - "Engelbrecht cites the same dating" is true of the day and consul. He does not give Alaric's regnal year.

## 3. Open-Gaps 251 "List lines": FAIL (MINOR 4)

| Sentence | Census evidence | Result |
|---|---|---|
| Columbanus, John Moschus, Isidore of Seville have a people row | `insular-irish-monastic-christianity.people[1]` "Columbanus"; `chalcedonian-monasticism-judean-desert-and-gaza.people[4]` "John Moschus"; `nicene-visigothic-iberia.people[2]` "Isidore of Seville" | PASS |
| Babai the Great only as a named voice and in entry text | `the-church-of-the-east-under-persia.voices[3]` "Babai the Great — abbot and theologian ..."; `documentedStories[1].text` "the monastery of Izla under Babai the Great". The other Babai hits (person `simeon-of-beth-arsham`, edge 678) are the catholicos Babai, a different man. No people row. | PASS |
| John of Biclaro only in entry text (Nicene Visigothic Iberia; Nubian Christianity, "John of Biclarum") and the note of edge Nubian to Makurian | Nubian `sources[0].note`, `documentedStories[0].caveat/sources`; Nicene Visigothic Iberia `documentedStories[0].caveat/sources`; edge `nubian-christianity--makurian-nubian-christianity` note (and its sources). Other hits are file names only. | PASS |
| Faustus of Riez in Gallic monastic text ("Faustus, later became bishop of Riez") and the link note to Merovingian; the Faustus row is Faustus of Milevis | `gallic-monastic-ascetic-christianity.longDescription` (quote exact); edge `gallic-monastic-ascetic-christianity--merovingian-gallic-christianity` note "Gennadius tells of Faustus, the first abbot of Lérins, who became bishop of Riez"; `manichaeism.people[2]` "Faustus of Milevis" | PASS |
| Gennadius of Marseilles: no people row; entry text, link notes and **era 1 and 2** person entries cite him as writer of the Lives of Illustrious Men | No people row (the only Gennadius rows are Gennadios Scholarios). Entry text: `aquileian-christianity.legacy`. Link notes: edges 23, 24, 26, 151, 152, with sources "Gennadius, Lives of Illustrious Men, chapter ...". Person entries citing him: Basil, Gregory of Nazianzus, Pachomius, Rufinus, Evagrius, Cassian, Sulpicius Severus, Tyconius, Theodoret, Pelagius, Honoratus, Hilary of Arles, Marius Mercator, Prosper. **All are `era: 2`.** No era 1 person entry names him. | **FAIL (MINOR 4)** |
| Constantius of Lyon: no people row; the Germanus of Auxerre entry and the Hilary of Arles card name him as writer of the Life of Germanus | No people row (the Constantius rows are Constantius II). Person `germanus-of-auxerre`: longDescription "Constantius wrote his Life of Germanus about 480 ..." and `card.legacy.remembered[1]` "Constantius of Lyon wrote his Life". Person `hilary-of-arles`: `card.legacy.remembered[0]` "Constantius of Lyon, in his Life of Germanus of Auxerre, calls him ...". No other hit is this man. | PASS |
| Severinus of Noricum and Ruricius of Limoges named nowhere | "Severin" hits once, in "severing" (edge 53, a Jerome quote). "Noricum" appears only in the Danubian region list, not as him. "Eugippius" has no hits. Ruric/Rurik/Limog/Lemov have no hits. No id matches either name. | PASS |

## Findings and exact fixes

**BLOCKING 1 — Braun gives three passages only as notes, not two.** The missing note is l.14995-14996, "Es folgen zunächst drei längere Gebete, um Standhaftigkeit, für die Kirche und sein Kloster, für die Häretiker." Fixes:

- 1a (`babai-the-great` claim): replace "four passages passed over and two given only as a note, braun1915 l.12442-12443, 13161-13162, 13270, 13319-13322, 13362-13363, 13806-13807, 14944-14947" with "four passages passed over and three given only as notes, braun1915 l.12442-12443, 13161-13162, 13270, 13319-13322, 13362-13363, 13806-13807, 14944-14947, 14995-14996".
- 1b: replace "(l.12442-12443) passes over" with "(l.12442-12443), passes over". Replace "and gives a reflection on the times and the rest of George's prayer only as notes (l.13362-13363, 14944-14947)" with "and gives a reflection on the times, the rest of George's prayer and three longer prayers before the crucifixion only as notes (l.13362-13363, 14944-14947, 14995-14996)".
- 1c (batch 5 Henana note): replace "gives two more only as notes" with "gives three more only as notes". Replace "13806-13807, 14944-14947;" with "13806-13807, 14944-14947, 14995-14996;".
- 1d (Open-Gaps 251, "Not held"): replace "leaves out four passages and gives two more only as notes" with "leaves out four passages and gives three more only as notes". Per the append-only rule, make this through whatever correction form the tracker allows.

**MINOR 1 — Chabot translates three passages of the Life, not two.** Two are on Henana's doctrines. Fixes:

- 1b: replace "as two passages in Chabot's French (chabot1902 l.42080-42240)" with "as three passages in Chabot's French (chabot1902 l.42080-42252, two on Henana's doctrines; l.42257-42498)".
- 1c: replace "as the two passages Chabot gives in French (synodicon-orientale chabot1902 l.42080-42240)" with "as the two passages on Henana's doctrines that Chabot gives in French (synodicon-orientale chabot1902 l.42080-42252)".
- 1d, "Correction to batch 5": replace "in Chabot's two French passages" with "in three French passages Chabot gives (two of them on Henana's doctrines)".

**MINOR 2 — a missing comma in 1b** after "(l.12442-12443)". The fix is folded into BLOCKING 1 above.

**MINOR 3 — Ruricius `claims[2]`.** Replace "(Bruns's note; OCR 'tertiq', 'Septenibris')" with "(Bruns's note; OCR 'Agath,', 'tertiq', 'Septenibris', 'CQnsvlm')".

**MINOR 4 — Open-Gaps 251, "List lines".** Replace "era 1 and 2 person entries" with "era 2 person entries".

## Verdict

NOT CLEAR. One BLOCKING point remains.

- **BLOCKING 1:** Braun gives three omitted passages only as notes, not two. The fourth note is at l.14995-14996. The wrong count appears in strings 1a, 1b, 1c and 1d.
- **Passes:** 1e (the card) and the batch 5 diff. Only the Henana note changed.
- **MINOR points:** 1 (Chabot gives three passages), 2 (a comma), 3 (two unflagged OCR emendations in the Agde quotation) and 4 ("era 1 and 2" should be "era 2").
- **Substance that holds:** the Agde dating, its witness lines and the council each line belongs to. Every other List-lines sentence checks out against the census.

The blocking fix is mechanical, a figure and one line reference in four places. It needs independent re-confirmation before it is cleared.
