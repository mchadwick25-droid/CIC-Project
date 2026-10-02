# Source Readiness Dossier — The Hussite and Bohemian Brethren Movement

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and
why it exists.

**Atlas ID:** V.6
**Corpus-map slug:** `the-hussite-and-bohemian-brethren-movement`
**Time window:** c. 1402–1517 (the census entry reads 1415–1517; see §6)
**Region(s):** Bohemia (with Moravia for the Unity of the Brethren)
**Dossier author:** source-research thread
**Corpus-map / `cic/texts/` state:** read from `cic/corpus-map/the-hussite-and-bohemian-brethren-movement.yaml`.

## 1. Already assigned

Twenty-three files are vendored and assigned to
`cic/corpus-map/the-hussite-and-bohemian-brethren-movement.yaml`, in 24
assignments: the Brown *Fasciculus* file carries two, one for the volume
(context) and one for the Brethren's Latin Confession inside it
(tradition). Eleven assignments are in `tradition` role (Hus's own
voice, Chelčický, the Brethren's Confession, and Březová) and thirteen in
`context` role. Fifteen are `assigned`; nine are `provisional`.

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| The Letters of John Hus (Workman & Pope, 1904) | hus | tradition | assigned | ~673K chars | `hus_letters_workman-pope1904.txt` |
| De Ecclesia. The Church (Schaff, 1915) | hus | tradition | assigned | ~736K chars | `hus_de-ecclesia-the-church_schaff1915.txt` |
| *M. Jana Husi Korespondence a dokumenty* (Novotný, 1920; Latin and Czech) | hus | tradition | assigned | ~1.48M chars | `hus_korespondence-a-dokumenty-lat-ces_novotny1920.txt` |
| *Sebrané spisy české*, vol. 1: Creed, Ten Commandments, Lord's Prayer, tract on simony (Erben, 1865; Czech) | hus | tradition | assigned | ~1.24M chars | `hus_sebrane-spisy-ceske-v01-ces_erben1865.txt` |
| *Sebrané spisy české*, vol. 2: the Czech *Postilla* (Erben, 1866; Czech) | hus | tradition | assigned | ~1.15M chars | `hus_sebrane-spisy-ceske-v02-ces_erben1866.txt` |
| *Sebrané spisy české*, vol. 3: *Dcerka*, *Zrcadlo*, *Výklad písničky Šalomúnovy* (Erben, 1868; Czech) | hus | tradition | assigned | ~818K chars | `hus_sebrane-spisy-ceske-v03-ces_erben1868.txt` |
| *Tractatus responsivus* (Thomson, 1927; Latin with English introduction) | hus | tradition | provisional | ~492K chars | `hus_tractatus-responsivus-lat-eng_thomson1927.txt` |
| *Documenta Mag. Joannis Hus*: letters, the *Relatio* of Petr of Mladoňovice, documents of 1403–1418 (Palacký, 1869; Latin and Czech) | palacky | tradition | assigned | ~1.82M chars | `palacky_documenta-mag-joannis-hus-lat-ces_1869.txt` |
| *Síť víry* (Chelčický, the Net of Faith; Smetánka, 1912, from the 1521 printing; Czech) | chelcicky | tradition | assigned | ~1.00M chars | `chelcicky_sit-viry-ces_smetanka1912.txt` |
| *Historia Hussitica* (Lawrence of Březová, ed. Goll, 1893; with Pulkava, the University chronicle and Bartošek; Latin and Czech) | laurentius-de-brezova | tradition | provisional | ~3.28M chars | `laurentius-de-brezova_historia-hussitica-lat-ces_goll1893.txt` |
| The Brethren's Latin Confession to King Vladislav (in Brown's *Fasciculus*, 1690) | unity-of-the-brethren | tradition | provisional | part of ~3.07M chars | `gratius_fasciculus-rerum-expetendarum-v1-lat_brown1690.txt` |
| *Fasciculus rerum expetendarum et fugiendarum*, vol. I (Brown, 1690), the whole volume | gratius | context | provisional | ~3.07M chars | `gratius_fasciculus-rerum-expetendarum-v1-lat_brown1690.txt` |
| *Urkundliche Beiträge zur Geschichte des Hussitenkrieges*, Band I: 1419–1428 (Palacký, 1873; Latin, Czech and German) | palacky | context | provisional | ~1.53M chars | `palacky_urkundliche-beitraege-hussitenkrieg-v1-deu-lat_1873.txt` |
| *Urkundliche Beiträge zur Geschichte des Hussitenkrieges*, Band II: 1429–1436 (Palacký, 1873; Latin, Czech and German) | palacky | context | provisional | ~1.22M chars | `palacky_urkundliche-beitraege-hussitenkrieg-v2-deu-lat_1873.txt` |
| *Historia Bohemica* (Piccolomini, 1592 Latin printing) | piccolomini | context | assigned | ~385K chars | `piccolomini_historia-bohemica-lat_1592.txt` |
| *Historia Bohemica* (Piccolomini, Cologne, 1524 printing) | piccolomini | context | provisional | ~289K chars | `piccolomini_historia-bohemica-lat_1524.txt` |
| Church Constitution of the Bohemian and Moravian Brethren (*Ratio Disciplinae*, 1632/33; ed. Seifferth, 1866) | unity-of-the-brethren | context | assigned | ~343K chars | `unity-of-the-brethren_church-constitution_seifferth1866.txt` |
| *Historia Fratrum Bohemorum* (Comenius; Buddeus's preface; Halle, 1702; Latin) | comenius | context | provisional | ~719K chars | `comenius_historia-fratrum-bohemorum-lat_1702.txt` |
| The Life & Times of Master John Hus (Lützow, 1909) | lutzow | context | assigned | ~1.03M chars | `lutzow_life-and-times-of-hus_1909.txt` |
| The Hussite Wars (Lützow, 1914) | lutzow | context | assigned | ~990K chars | `lutzow_hussite-wars_1914.txt` |
| Bohemia: An Historical Sketch (Lützow, 1920) | lutzow | context | assigned | ~1.04M chars | `lutzow_bohemia-historical-sketch_1920.txt` |
| The Life and Times of John Huss, Vol. II (Gillett, 1871) | gillett | context | assigned | ~1.47M chars | `gillett_life-and-times-of-huss-v2_1871.txt` |
| The Acts and Monuments of John Foxe, Vol. III (Cattley/Townsend, 1837), the Hus section | foxe | context | assigned | file lines 30742–46807 of ~3.99M chars | `foxe_acts-and-monuments-v3_cattley-townsend1837.txt` |
| The Bloody Theater, or Martyrs' Mirror (Van Braght, 1660; Sohm, 1886), the Hus and Taborite sections | van-braght | context | provisional | file lines 47370–47660 of ~6.60M chars | `van-braght_martyrs-mirror_sohm1886.txt` |

**Voices.** Hus speaks for himself in English (the *Letters*, *De
Ecclesia*), in Latin and Czech (Novotný, Palacký), and in Czech pastoral
works (Erben vols. 1–3). The *Tractatus responsivus* is Hus's only on the
editor's argument: Thomson states that no manuscript names Hus, so it is
quoted only as "the tract attributed to Hus by Thomson". Chelčický is
vendored in the Czech he wrote. The Utraquist chronicler Březová is the
main source for Tábor and the Adamites and is hostile to Tábor, so the
Taborite strand is seen through him and not in its own voice. Palacký's
*Urkundliche Beiträge* prints the wars' own documents from many hands
(Hussite, Taborite, Catholic and royal); the documents are not one voice,
and the German summaries are the editor's.

**Unity of the Brethren.** No Unity text from inside the window
(1457–1517) is vendored except the Latin Confession to King Vladislav,
printed in Brown's 1690 *Fasciculus*, and two short quotations from the
Brethren's 1508 letters to Dr. Augustine in Seifferth's Introduction. The
*Ratio Disciplinae* is a 1632/33 text and falls outside the window.
Comenius's *Historia* is the Unity's later account of itself, written by
its last bishop and printed in 1702. It gives the Unity's picture of its
origins at second hand and is not its voice of the years to 1517.

**Scan quality.** Witness grade follows the corpus-map notes.

- Piccolomini is a contemporary hostile source. The 1592 scan carries
  systematic long-s errors and interleaved marginal notes (see Doc_02).
  The 1524 printing has no interleaved marginal notes and keeps the long
  s as ſ, but misreads many letters (word-form coverage against a clean
  Latin vocabulary 0.60, about the same as the 1592 printing). It does
  not by itself supply a clean witness.
- Březová's Latin is legible but carries frequent letter-level misreads
  and the editors' numbered manuscript variants interleaved with the
  text. The volume's title page reads 1893; the archive record dates it
  1873.
- Brown's 1690 *Fasciculus* reads the long s as f, confuses italic and
  roman, and carries stray glyphs. The Confession is readable in
  outline; the volume does not settle whether it is the 1504 or the 1508
  text.
- Comenius's 1702 print reads the long s as f throughout, with many
  word-level misreads (word-form coverage 0.42).
- Palacký's *Documenta* reads well in Latin (coverage 0.80), but the
  Czech letters keep his 1869 orthography and the OCR drops or misplaces
  some diacritics. The *Urkundliche Beiträge* reads legibly in Latin and
  German (coverage 0.54, lowered by the German and Czech).
- Novotný's footnote marks and superscript digits are scattered through
  the lines. Erben's 1865–68 orthography is the old one, and the OCR
  misreads some letters of the marginal scripture citations.
  Chelčický's woodcut pages read as noise. The *Tractatus responsivus*
  Latin is clean (coverage 0.83); its front matter reads as noise.

Every Latin or Czech wording is checked against the page image before it
is quoted (`cic/texts/INTAKE.md` §2).

## 2. Cross-link opportunities

- **Lollardy (V.5).** The link is direct textual borrowing, not a
  contested influence line. Schaff's translator introduction to the
  vendored *De Ecclesia* says Hus took whole paragraphs from Wyclif.
  Wyclif's own *Tractatus de Ecclesia* (`wyclif_de-ecclesia-lat_loserth1886.txt`)
  is vendored under Lollardy, and Loserth's introduction to it discusses
  Hus's use of Wyclif. Thomson's introduction to the vendored *Tractatus
  responsivus* also treats Hus's borrowing from Wyclif. Foxe's *Acts and
  Monuments*, Vol. III (`foxe_acts-and-monuments-v3_cattley-townsend1837.txt`)
  is assigned to both Lollardy and this world: each world reads a
  different part of it. Its Hus section carries the Constance
  proceedings, the petitions of the Bohemian nobles and the university,
  and a papal inquisitor's testimonial to Hus.
- **Lutheran Wittenberg (VI.1).** Luther's vendored works name the
  Bohemians and Hus directly (for example, the 1520 *Address to the
  Christian Nobility* in `luther_works-v2-selected_jacobs-spaeth1916.txt`).
  These are later (post-1517) witnesses to the tradition. Luther's hymn
  *Jesus Christus unser Heiland* is printed as "Improved" from a
  Communion Hymn of John Huss; the stanzas are Luther's revision and are
  not given to Hus.
- **The Anabaptist Movements (VI.3).** Van Braght's *Martyrs' Mirror*
  (`van-braght_martyrs-mirror_sohm1886.txt`) is assigned to both worlds.
  Its Hus and Taborite sections are a 1660 Anabaptist reading of the
  Hussites, at three removes from any Taborite text, and it prints what
  it calls a Taborite confession of 1431 whose own source is not
  vendored. It is a witness to how a later movement read them, not
  Hussite voice.
- **The Society of Jesus (VI.11).** The Jesuit works that name Hus or the
  Hussites (Polanco, Lainez, Canisius) fall after the window.

## 3. Verified acquisition leads

Every vendored work below was checked against the Internet Archive item
and the header of its vendored file. All are public domain by the
project's date rule (published 1930 or earlier).

| title | author / editor | year | archive.org item | rights basis | verified by |
|---|---|---|---|---|---|
| The Letters of John Hus | Jan Hus, trans. Herbert B. Workman & R. Martin Pope | 1904 | `lettersofjohnhus00husjuoft` | pd-us-by-date, `NOT_IN_COPYRIGHT` confirmed | direct fetch; metadata and body text both checked |
| De Ecclesia. The Church | Jan Hus, trans. David S. Schaff | 1915 | `deecclesiachurc00hussgoog` | pd-us-by-date, `NOT_IN_COPYRIGHT` confirmed | direct fetch; metadata and body text checked |
| *M. Jana Husi Korespondence a dokumenty* | Jan Hus, ed. Václav Novotný | 1920 | `mjanahusikorespo00husjuoft` | pd-us-by-date; `NOT_IN_COPYRIGHT` on the item as supporting evidence | direct fetch of the full-text file; file header |
| *Sebrané spisy české*, vols. 1–3 | Jan Hus, ed. Karel Jaromír Erben | 1865, 1866, 1868 | `sebranespisyesk01husjuoft`, `sebranespisyesk02husjuoft`, `sebranespisyesk03husjuoft` | pd-us-by-date; `NOT_IN_COPYRIGHT` on each item as supporting evidence | direct fetch of each full-text file; file headers |
| *Documenta Mag. Joannis Hus* | ed. František Palacký | 1869 | `documentamagjoa00palagoog` | pd-us-by-date; `NOT_IN_COPYRIGHT` on the item as supporting evidence | direct fetch of the full-text file; file header |
| *Mag. Johannis Hus Tractatus responsivus* | ed. S. Harrison Thomson (Princeton) | 1927 | `magjohannishustr00husj` | pd-us-by-date (a US publication of 1927, inside the 1930 rule); the item carries no rights field | direct fetch of the full-text file; title page |
| *Síť víry* | Petr Chelčický, ed. Emil Smetánka | 1912 | `stvry00chel` | pd-us-by-date; the item carries no rights field | direct fetch of the full-text file; title page |
| *Historia Hussitica*, in *Fontes rerum Bohemicarum* V | Lawrence of Březová, ed. Jaroslav Goll | 1893 | `fontesrerumbohe00goog` | pd-us-by-date; `NOT_IN_COPYRIGHT` on the item as supporting evidence | direct fetch of the full-text file; title page (the archive record's own date is wrong for this volume) |
| *Urkundliche Beiträge zur Geschichte des Hussitenkrieges*, Bände I–II | ed. František Palacký | 1873 | `urkundlichebeitr01pala`, `urkundlichebeitr02pala` | pd-us-by-date; the items carry no rights field | direct fetch of the full-text files; title pages |
| *Fasciculus rerum expetendarum et fugiendarum*, vol. I | Ortwin Gratius (1535); ed. Edward Brown | 1690 | `bub_gb_Z7e69raCdb8C` | pd-us-by-date; the item carries no rights field | direct fetch of the full-text file; title page |
| *Historia Bohemica* (Cologne printing) | Aeneas Silvius Piccolomini | 1524 | `bim_early-english-books-1641-1700_aeneas-silvius-sene_1524` | pd-us-by-date (colophon); the item carries no rights field | direct fetch of the full-text file; colophon |
| *Historia Bohemica* (1592 printing) | Aeneas Sylvius Piccolomini | 1592 | `bub_gb_9KLM6ygwsQQC` | pd-us-by-date; access-restricted-item: None | direct fetch of the full-text file; item metadata |
| Church Constitution of the Bohemian and Moravian Brethren | ed. B. Seifferth | 1866 | `bub_gb_p-4QAAAAIAAJ` | pd-us-by-date; access-restricted-item: None | direct fetch of the full-text file; item metadata |
| *Historia Fratrum Bohemorum* | Jan Amos Comenius; preface by Johann Franz Buddeus | 1702 | `bub_gb_WoZLAAAAcAAJ` (a second scan of the same printing is `bub_gb_dmdTAAAAcAAJ`; the vendored file is the fuller) | pd-us-by-date; the item carries no rights field | direct fetch of the full-text file; title page |
| The Life & Times of Master John Hus; The Hussite Wars; Bohemia: An Historical Sketch | Count Francis Lützow | 1909; 1914; 1920 | `lifetimesofhus00ltuoft`; `hussitewars00lt`; `bohemiahistorica1920lt` | pd-us-by-date; `NOT_IN_COPYRIGHT` on the first, access-restricted-item: None on the others | direct fetch of each full-text file; item metadata |
| The Life and Times of John Huss, Vol. II | Ezra Hall Gillett | 1871 | `lifetimesofjohnh02gill` | pd-us-by-date, `NOT_IN_COPYRIGHT` confirmed | direct fetch; item metadata |
| The Acts and Monuments of John Foxe, Vol. III | John Foxe, eds. Cattley and Townsend | 1837–41 | `actsmonumentsofj03foxe` | pd-us-by-date, `NOT_IN_COPYRIGHT` confirmed | direct fetch; item metadata |
| The Bloody Theater, or Martyrs' Mirror | Thieleman J. van Braght, trans. Joseph F. Sohm | 1886 | `MartyrsMirror` | pd-us-by-date; the item carries no rights field | direct fetch of the full-text file; the stated publication date |

**Open leads.** None of these is vendored and none is verified to exist
as a public-domain scan. Each has a row in `Build/worlds/hus/Source_Registry.md`
unless noted.

| title | author | year | url | rights basis | status |
|---|---|---|---|---|---|
| *Historia et Monumenta Joannis Hus et Hieronymi Pragensis* (Frankfurt, 1715, a reprint of the edition of 1558), the Latin base text of Schaff's translation of *De Ecclesia* | Jan Hus | 1558; 1715 | not located | not checked; dated before 1930, so it may be public domain by date | The reachable hosts were searched and it was not found. Schaff compared it paragraph by paragraph with his English and names no critical edition. Only Schaff's English is on the shelf. |
| Unity of the Brethren primary material from inside the window: Gregory the Patriarch's letters, the 1504 Confession to King Vladislav, the 1508 letters to Dr. Augustine, discipline ordinances, and the 1501 hymnbook | the Unity of the Brethren | 1457–1517 | not located | not checked | The hymnbook of 1501 (or 1505) and Gregory the Patriarch's letters were not found. The Confession and the Brethren's *Excusatio* against two letters of Dr. Augustine are in Brown's 1690 volume as a second witness; the letters to Augustine as separate documents were not found. A clean witness of the Confession is the 1535 Cologne printing on the Internet Archive (`dlibra.kul.pl.P.XVI.804`), which is not vendored. |
| *Acta Unitatis Fratrum*, vol. 1 (the Brethren's own records of 1457–1467) | the Unity of the Brethren | 1457–1467 | not located | not checked | Not vendored. It is the census's source for the lot at Lhotka. |
| Jaroslav Goll, *Quellen und Untersuchungen zur Geschichte der Böhmischen Brüder* (1878–82) | Jaroslav Goll | 1878–82 | on the Internet Archive; the text file returned HTTP 500 | public domain by date, as far as the builder knows; the Library must verify | Blocked. The item is queued. |
| The Four Articles of Prague, Hussite and Taborite manifestos and chronicle excerpts, in T. Fudge, *The Crusade against Heretics in Bohemia, 1418–1437* (Ashgate, 2002) | Hussite and Taborite writers | 1418–1437 | not located | Fudge's book is in copyright; a clean edition would be an original text | The Latin of the Four Articles is on the shelf in two places (the papal legate's reply in Palacký, vol. 1, and Březová's copy) and the two differ in order. Still wanted: the Articles as the Praguers issued them, and the Taborite articles in their own voice. The *Archiv český*, which Palacký cites for them, was not found on the Internet Archive. |
| A clean witness of Piccolomini's *Historia Bohemica* | Aeneas Silvius Piccolomini | 1524; 1592; 1699 | not located | public domain by date | Neither vendored printing is clean. A 1699 Helmstedt printing is queued as no cleaner. No Registry row of its own; the two vendored printings are at rows 11 and 72. |
| Camerarius, *Historica narratio* | Camerarius | after the window | not located | not checked | Named in the Seifferth Introduction as a later Unity history. Not found. No Registry row. |
| Lasitius on the Brethren's discipline | Lasitius | after the window | not located | not checked | Named in the Seifferth Introduction as a later Unity history. Not found. No Registry row. |
| Flajšhans's later edition of Hus's works (1904 on) | Jan Hus, ed. Václav Flajšhans | 1904 on | not located | not checked | Queued. No Registry row for the later edition; row 47 is his 1905 *Super IV. Sententiarum*. |
| Hus, *De sanguine Christi sub specie vini a laicis sumendo* | Jan Hus | not stated | not located | not checked | Named in Novotný's note to letter no. 141 as "Op I 42–44" in the printed *Opera*. Not on the shelf. No Registry row. |

**Scale (rough):** about 35.3 million characters in 23 files. Two of
them are whole volumes assigned only for their Hus sections (Foxe and
Van Braght, about 10.6 million characters together); the other 21 files
hold about 24.8 million. In tradition-role terms Hus writes in three
languages and three genres (letters, a systematic treatise, Czech
pastoral works), and Chelčický adds a second Czech voice.

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| *The Appeale of John Hus from the General Council's Excommunication* (London, 1662) | A short 17th-century English printing of a Hus text, archive.org `bim_early-english-books-1641-1700_the-appeale-of-_hus-jan_1662`, `NOT_IN_COPYRIGHT` | The OCR is unusable throughout. Not vendored. The vendored *Letters* already carry Hus's appeal language ("I have appealed to Christ"). A re-OCR or transcription of the existing scan could reopen it. |
| Hus's Latin *De Ecclesia* | The original of the treatise that led to his condemnation | Only Schaff's 1915 English is vendored, and the Latin edition Schaff hoped for did not exist in 1915. Not found on the reachable hosts; an open lead (§3). |
| Hus's Czech works and the Latin and Czech originals of the *Letters* | Hus writes in Czech and Latin, and the English *Letters* reach neither original | Vendored: Erben vols. 1–3, Novotný and Palacký (§1). Each wording is checked against the page image before quotation. |
| Palacký's *Documenta* with the Latin *Relatio* | The earliest account of the Constance trial, in the original language | Vendored (§1). In the *Relatio*, Hus's third clause reads *Qui natus es ex Maria virgine* ("born"); Workman's English gives "conceived". No voice gives "conceived" as Hus's last words. |
| Chelčický's *Síť víry* | The Unity's main lay-pacifist thinker | Vendored in Czech (§1). |
| The Taborite strand in its own voice | The stricter, more radical branch of the movement | No Taborite text in its own voice is vendored. The Taborite twelve articles and the priests' articles are in Březová as a hostile chronicler copied them, and Palacký's *Urkundliche Beiträge* gives only German summaries of the Taborite documents. Van Braght's "Taborite confession of 1431" has no vendored source. Open (§3, Four Articles). |
| Unity of the Brethren primary material (a confession, a catechism, or the 1501 hymnbook) | The stricter branch the census names | The Latin Confession is vendored as a second witness inside Brown's 1690 volume. The Brethren's *Excusatio*, their reply to two letters of Dr. Augustine, is in the same volume. The two short 1508 quotations in Seifferth's Introduction are fragments at two removes. The hymnbook, Gregory the Patriarch's letters and the *Acta* are not found. The earlier Cologne printing of 1535 (`dlibra.kul.pl.P.XVI.804`) is not vendored. Open, and not assumed absent. |
| A cleaner *Historia Bohemica* | Piccolomini is the main contemporary hostile source | A second printing (Cologne, 1524) is vendored and is no cleaner; a 1699 Helmstedt printing is queued as no cleaner. Whether the pair meets the Library's rule for a clean witness is the Library's ruling. |
| Later Unity histories: Comenius, Camerarius, Lasitius | The Unity's later account of the window at first hand | Comenius (1702) is vendored as a second witness. Camerarius and Lasitius were not found. |
| A separate edition of the Four Articles or the Taborite articles | The movement's own programme in its original documents | No separate edition found. The Praguers' Articles are quoted in Latin in the legate's reply and in Březová. |

## 5. Open cross-world questions

**Vs. Lollardy (V.5).** The census's Lollardy entry names a "contested
influence line to the English Reformation." That line does not run to
Hussitism. The Hussite link to Wyclif is direct textual borrowing (§2),
established by Schaff's introduction to the vendored *De Ecclesia*. The
two movements diverged sharply in outcome: Lollardy stayed underground,
while Hussitism won legal recognition in 1436. They are correctly two
separate candidates. A whole-of-tradition scholarly debate also exists
over how much Hus owed to Wyclif and how much to earlier Bohemian
reformers (Lützow's 1909 biography stresses the Bohemian forerunners).
Doc_01 for either world should carry both.

**Foxe and Van Braght, one text in two worlds.** Each is assigned to
this world and to another. A placement of one text in two worlds records
that each world reads a different part of it: here, the Hus and Taborite
sections only.

**Census hymnbook wording.** The claim that the Unity printed "what is
often called the first hymnbook in a European vernacular" by 1501
appears in the census entry's `why` and `longDescription` fields. It does
not appear in `relationsSummary`.

## 6. Step 0 scope notes

**Doctrinal floor:** the Step 0 check (`Build/worlds/hus/Step0_Movement_Scope_Confirmation.md`)
found no creedal question in Hus's own voice. Doc_01 extends that check
across all five commitments of Article 4 and across the movement's other strands.

**Scale honestly stated:** Hus is now rich in tradition voices across
three languages and several genres. The movement's institutional and
legal story (the 1436 Compactata) is covered by context-role secondary
works and by Palacký's documents. The Taborite strand has no voice of
its own, and the Unity's in-window voice rests on one second-witness
Latin print and two short quotations.

**Census record to update:** the V.6 entry's `dates` field reads
"1415-1517"; the window is c. 1402–1517 (the entry's own
`statusDescription` already says the Prague formation runs 1402–14).
The corpus-map notes for the *Letters* ("his career at the university")
and several others need a hygiene pass in `cic/corpus-map/_staging/`.
