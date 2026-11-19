# R5 cap check: strings changed by c9fd357d (Mark's cap ruling, "List the lines, one last check", 2026-11-14)

## Scope

Only the strings changed by commit c9fd357d:

1. `Who-Profiles/era3/batch6/records.json`, `babai-the-great`: the Braun parenthesis in the Life of George claim.
2. Same entry, `absent_details` "A Syriac or English text of his own books".
3. Same file, `ruricius-of-limoges`: the OCR flag list in the Bruns quotation (Agde 506 claim).
4. `Who-Profiles/era3/batch5/records.json`, `henana-of-adiabene`, `absent_details` "A second witness to Babai's doctrinal charges".
5. `Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md`, entry 251: the Braun clause in "Not held", the Chabot clause in "Correction to batch 5", and "era 2 person entries" in "List lines".

No other string was reviewed. No other file in this audit folder was read before this verdict.

## Method

- `git show c9fd357d` to fix the changed strings.
- Braun (`persian-martyr-acts_ausgewahlte-akten-persischer-martyrer-bkv22-deu_braun1915.txt`): read the Life of George from its heading (l.852-860) and its text (l.12419) to its last line ("Amen. Amen.", l.15452) and its last footnote (l.15455). Listed every footnote in that span by marker (`x)`, `J)`, `*)`, `1)`-`9)`, `:)`) and searched OCR-tolerantly for `übergeh`, `ubergeh`, `übergang`, `gebe ich`, `Es folgt`, `folgen`, `setzt sich`, `kürz`/`kurz`, `weggelass`, `ausgelass`, `Lücke`, `inhalt`, `zusammen`. Sorted each hit into Braun's own editorial notes and Babai's text.
- Chabot (`synodicon-orientale_..._chabot1902.txt`): read l.42060-42120, 42225-42275 and 42485-42505.
- Bruns (`bruns_canones-apostolorum-et-conciliorum-pars-altera-lat_1839.txt`): read l.10494-10503.
- `cic-website/data/world-census.json`: walked every string for "Gennadius", and checked the era and kind of each movement that names him.
- `git diff origin/main -- .../era3/batch5/`; parsed both records files with `json.load`; counted words per sentence with parenthetical citations stripped.

### Braun's own notes in the Life of George

| Line | Note (OCR as printed) | Kind |
|---|---|---|
| 12442-12443 | "Von der sehr langen Einteilung [Einleitung] gebe ich nur die wichtigsten Gedanken." | shortens the introduction |
| 13161-13162 | "Das folgende, sachlich belanglose Enkomion auf die Heilige übergehe ich." | left out |
| 13270 | "Eine hier folgende Betrachtung habe ich übergangen." | left out |
| 13319-13322 | "Ein langes Enlromion [Enkomion] ... übergehe ich." | left out |
| 13362-13363 | "Es folgt zunächst im Anschluß an 1 Kor. 7, 29-81 [31] eine Betrachtung über die Schlechtigkeit der Zeit." | summed up |
| 13806-13807 | "Die folgenden, sachlich inhaltslosen Ausführungen übergehe ich." | left out |
| 14944-14947 | "Das Gebet setzt sich noch lange fort in einem Dank für die Berufung zum Christentum ..., zum Mönchtum und Martyrium." | summed up |
| 14995-14996 | "Es folgen zunächst drei längere Gebete, um Standhaftigkeit, für die Kirche und sein Kloster, für die Häretiker." | summed up |

Excluded, correctly: l.14728, "Es folgt im Text eine Lücke" (a gap in the Syriac, not Braun's cut); l.14397-14399 (says the Symbolum is in the Synodikon; the omission there is Babai's own narrative, not Braun's); "dürfen wir nicht übergehen" at l.15169 and l.15293-15294 (Babai's text). No other note in the span shortens, passes over or sums up.

## String 1: batch 6 Babai claim, Braun parenthesis: PASS

"Braun shortens the introduction and leaves out or sums up several passages, braun1915 l.12442-12443, 13161-13162, 13270, 13319-13322, 13362-13363, 13806-13807, 14944-14947, 14995-14996"

- Each of the eight ranges is one of Braun's own notes, and each shortens, passes over or sums up (table).
- None is missing. The Lücke note at l.14728 is rightly left out.
- "several" is fair: seven passages besides the introduction, four left out and three summed up.
- Nothing in the parenthesis goes beyond the notes.

## String 2: batch 6 absent_details "A Syriac or English text of his own books": PASS on substance, MINOR on prose

- Braun line list: as String 1. PASS.
- "three passages in Chabot's French (chabot1902 l.42080-42252, two on Henana's doctrines; l.42257-42498)": Chabot says "Le récit renferme, au sujet de ces doctrines, deux passages" (l.42092-42093). The first runs l.42094-42107 ("Édit., p. 476-477"), the second l.42108-42252 ("Édit., pages 495-505"). The third, on the bishops calling George to court, runs l.42257-42498 ("Edit. pages [5]05-521"). Three passages, two on the doctrines. PASS.
- Prose: see MINOR 1.

## String 3: Ruricius, Bruns OCR flags: PASS

l.10498: "Conc. Agath, viginti quinque"; l.10500: "tertiq Idus Septenibris"; "Messala v. c. CQnsvlm". All four flagged readings stand on the cited lines. Observation, not a finding: the claim renders "CQnsvlm" as "consule"; the OCR could also stand for "consulem". The flag now tells the reader the quotation is normalized, which is enough.

## String 4: batch 5 Henana absent_details "A second witness to Babai's doctrinal charges": PASS on substance, MINOR on prose

- Braun line list: as String 1. "but keeps the charges (... l.13355-13400)": l.13355-13368 opens the charge passage on Hannänä ("Dieser lehrt das Fatum"). PASS.
- "the two passages on Henana's doctrines that Chabot gives in French (synodicon-orientale chabot1902 l.42080-42252)": matches Chabot l.42092-42252. PASS.
- `git diff origin/main` on batch 5 shows one changed line, this note. Both records files parse.
- Prose: see MINOR 1.

## String 5: Open-Gaps 251

- "Not held", Braun clause: same wording and line list as String 1. PASS.
- "Correction to batch 5", "three French passages Chabot gives (two of them on Henana's doctrines) and in Braun's abridged German": matches Chabot and Braun. "abridged" is fair. PASS on substance; prose, see MINOR 1.
- "List lines", "era 2 person entries cite him as the writer of the Lives of Illustrious Men": in the census, thirteen era 2 person entries name Gennadius (Gregory of Nazianzus, Pachomius, Rufinus, Evagrius, Cassian, Sulpicius Severus, Tyconius, Theodoret, Pelagius, Honoratus of Arles, Hilary of Arles, Marius Mercator, Prosper). Twelve list "Lives of Illustrious Men" (or "On Illustrious Men ... Gennadius's continuation") with Gennadius as author in their sources. No era 1 entry names Gennadius. Dropping "era 1" was right. PASS.

## Findings

**MINOR 1: three changed sentences run well past about 25 words, and one reads ambiguously.** These are evidence records and a tracking file, not participant-facing text, but the brief holds our own prose to the 25-word line. Word counts exclude parenthetical citations.

- Batch 6 note, "The Life of George is held in Oskar Braun's German ..., which shortens ... several passages ..., in Georg Hoffmann's German extracts ... and as three passages in Chabot's French ...": 37 words. The relative clause also lets "several passages, in Georg Hoffmann's German extracts" read as if Braun's passages sit in Hoffmann. Fix: "The Life of George is held in three forms. Oskar Braun's German (persian-martyr-acts bkv22 braun1915 l.12419 ff.) shortens the introduction and leaves out or sums up several passages (l.12442-12443, 13161-13162, 13270, 13319-13322, 13362-13363, 13806-13807, 14944-14947, 14995-14996). Georg Hoffmann gives German extracts (persian-martyr-acts hoffmann1880 l.5596-5612). Chabot gives three passages in French, two of them on Henana's doctrines (chabot1902 l.42080-42252; the third, l.42257-42498)."
- Batch 5 note, "Both held texts that state the charges are Babai's own: his De Unione, ... and his Life of George of Izla, ...": about 80 words. Fix: "None held. Both held texts that state the charges are Babai's own. The first is his De Unione, held in part as J. Labourt quotes and reports it in French from an unpublished copy Chabot made available to him (labourt1904 l.15764-15866; on Henana and the resurrection body, l.15816-15820). The second is his Life of George of Izla. Oskar Braun's German shortens the introduction and leaves out or sums up several passages, but keeps the charges (persian-martyr-acts bkv22 braun1915 l.12419 ff.; Braun's notes at [same eight ranges]; the charges at l.13355-13400). It is also held in Georg Hoffmann's German extracts (persian-martyr-acts hoffmann1880 l.5596-5612) and in the two passages on Henana's doctrines that Chabot gives in French (synodicon-orientale chabot1902 l.42080-42252). Babai's Evagrius commentary ..." (rest unchanged).
- Open-Gaps 251, "Correction to batch 5", "It is held in part, ..., and his Life of George of Izla is held in three French passages ...": about 40 words. Fix: "It is held in part, as Labourt quotes it in French (labourt1904 l.15764-15866). His Life of George of Izla is held in Braun's abridged German and in three French passages Chabot gives, two of them on Henana's doctrines."

The "Not held" bullet is one long semicolon list. Its form predates c9fd357d and is not counted here.

No BLOCKING finding. Every changed string states what its source lines hold. No line is miscited, no Braun note is missing, and none is overstated.

## Verdict

NOT CLEAR, on MINOR 1 only (sentence length and one ambiguous clause). No blocking point remains. All five strings pass on accuracy against the vendored files. If the three sentence fixes are applied, nothing in this scope stands open.
