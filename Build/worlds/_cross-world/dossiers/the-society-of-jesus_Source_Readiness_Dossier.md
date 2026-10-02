# Source Readiness Dossier — The Society of Jesus

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is.

**Atlas ID:** VI.11
**Corpus-map slug:** `the-society-of-jesus`
**Time window:** 1540–1650
**Region(s):** Rome, then worldwide
**Dossier author:** source-research thread
**Corpus-map / `cic/texts/` state:** read from `cic/corpus-map/the-society-of-jesus.yaml`.

## 1. Already assigned

Nineteen works are vendored and assigned to `cic/corpus-map/the-society-of-jesus.yaml`.

| work | author | role | confidence | source file |
|---|---|---|---|---|
| The Spiritual Exercises of St. Ignatius (Mullan, 1914) | ignatius-loyola | tradition | assigned | `ignatius-loyola_spiritual-exercises_mullan1914.txt` |
| The Autobiography of St. Ignatius (O'Conor, 1900) | ignatius-loyola | tradition | assigned | `ignatius-loyola_autobiography_oconor1900.txt` |
| Letters and Instructions of St. Ignatius Loyola, Vol. I, 1524–1547 (O'Leary/Goodier, 1914) | ignatius-loyola | tradition | assigned | `ignatius-loyola_letters-instructions-v1_oleary-goodier1914.txt` |
| Monumenta Ignatiana: Epistolae et Instructiones, Tomus I (Latin, 1903) | ignatius-loyola | tradition | assigned | `ignatius-loyola_epistolae-et-instructiones-v22-lat_1903.txt` |
| The Life and Letters of St. Francis Xavier, Vol. I (Coleridge, 1872) | francis-xavier | tradition | assigned | `francis-xavier_life-and-letters-v1_coleridge1872.txt` |
| The Life and Letters of St. Francis Xavier, Vol. II (Coleridge, 1872) | francis-xavier | tradition | assigned | `francis-xavier_life-and-letters-v2_coleridge1872.txt` |
| Memoriale Beati Petri Fabri (Latin, 1873) | faber | tradition | assigned | `faber_memoriale-lat_1873.txt` |
| The Life of the Blessed Peter Favre (Boero, tr. Coleridge, 1873) | boero | context | provisional | `boero_life-of-peter-faber_coleridge1873.txt` |
| Constitutiones Societatis Iesu, cum earum Declarationibus (Latin, 1606) | society-of-jesus | tradition | assigned | `jesuit-constitutions_constitutiones-societatis-iesu-lat_1606.txt` |
| Nadal, Adnotationes et Meditationes in Evangelia (Latin, 1595) | nadal | tradition | assigned | `nadal_adnotationes-et-meditationes-in-evangelia-lat_1595.txt` |
| Nadal, Epistolae, Tomus I, 1546–1562 (Latin, 1898) | nadal | tradition | assigned | `nadal_epistolae-v1-lat_1898.txt` |
| Nadal, Scholia in Constitutiones (Latin, 1883) | nadal | tradition | assigned | `nadal_scholia-in-constitutiones-lat_1883.txt` |
| Lainez, Epistolae et Acta, Tomus I, 1536–1556 (Latin, 1912) | lainez | tradition | assigned | `lainez_epistolae-et-acta-v1-lat_1912.txt` |
| Salmeron, Epistolae, Tomus Primus, 1536–1565 (Latin, 1906) | salmeron | tradition | assigned | `salmeron_epistolae-v2-lat_1906.txt` |
| Salmeron, Epistolae, Tomus Secundus, 1565–1585 (Latin, 1907) | salmeron | tradition | assigned | `salmeron_epistolae-v3-lat_1906.txt` |
| Polanco, Chronicon, Tomus V, the year 1555 (Latin, 1897) | polanco | context | assigned | `polanco_chronicon-v1-lat_1894.txt` |
| Ribadeneira, Vita Ignatii Loiolae (Latin, 1572; OCR-flagged) | ribadeneira | context | assigned | `ribadeneira_vita-ignatii-loiolae-lat_1572.txt` |
| A Summe of Christian Doctrine (Canisius, English, 1622) | canisius | tradition | assigned | `canisius_summe-of-christian-doctrine_anon1622.txt` |
| The Canons and Decrees of the Council of Trent (Waterworth, 1848) | council-of-trent | context | assigned | `council-of-trent_canons-and-decrees_waterworth1848.txt` |

The Latin originals are primary evidence for the movement, since scan quality decides quotability, not language (`cic/texts/INTAKE.md` §2). Their scans carry occasional letter-level misreads, so wording is verified against the page image before it is quoted. Nadal's *Adnotationes* and the Constitutions have no public-domain English translation. The Ribadeneira scan is flagged for OCR quality.

Institutional voice is dense to 1556 (Lainez Tomus I, Polanco Tomus V, Nadal), runs to 1562 through Nadal's letters, and after that rests on Salmeron's letters alone, to 1585. Nothing vendored gives the voice of Lainez, Borgia or Mercurian as General. Ignatius's own vendored letters end in 1547.

## 2. Cross-link opportunities

The Trent Canons and Decrees are vendored and double-placed to the sibling `the-tridentine-church` candidate (VI.22), consistent with §5.

## 3. Verified acquisition leads

| title | author | translator/ed. | year | url | rights basis | verified by |
|---|---|---|---|---|---|---|
| Spiritual Exercises | Ignatius of Loyola | Elder Mullan, S.J. ("translated from the autograph") | 1914 | archive.org `spiritualexercis00ignauoft` | pd-us-by-date | direct fetch, `NOT_IN_COPYRIGHT` confirmed |
| Autobiography of St. Ignatius (dictated to Luis Gonçalves da Câmara, 1553–55) | Ignatius of Loyola | ed. J.F.X. O'Conor, S.J. | 1900 | https://www.gutenberg.org/files/24534/24534-h/24534-h.htm | pd-us-by-date | direct fetch, explicit PD ebook |
| Letters and Instructions of St. Ignatius Loyola, Vol. 1 (1524–1547) | Ignatius of Loyola | tr. D.F. O'Leary, ed. A. Goodier | 1914 | archive.org `LettersAndInstructionsOfStIgnatiusV1` | pd-us-by-date | direct fetch, Public Domain Mark confirmed. A selection (24 letters), not the full ~7,000-letter corpus; a further volume of the series, beyond 1547, is not vendored (§4). |
| Council of Trent, Canons and Decrees | (conciliar) | James Waterworth | preface 1848, this printing c. 1888 | archive.org `thecanonsanddecr00unknuoft` | pd-us-by-date | direct fetch, `NOT_IN_COPYRIGHT` confirmed. Directly relevant: the doctrinal anchor the Jesuits implemented. |
| Life and Letters of St. Francis Xavier, Vol. I | Francis Xavier | Henry James Coleridge | 1872 | archive.org `LifeLettersOfStFrancisXavierV1` | pd-us-by-date | direct fetch, Public Domain Mark confirmed. Vol. I covers Xavier's birth in 1506, his university years, India and the Fishery Coast, Malacca and the Moluccas 1541–48, and the Xavier–Ignatius correspondence. Vol. 2 (later Japan and China years, Xavier's death 1552) is vendored (§1). |

**Scale.** Nineteen works are vendored (§1): the English translations and biographies above, plus Latin critical editions of the first generation's own letters and acts. Word counts are not extracted here.

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Jesuit Constitutions, **English** translation | The order's own governing document | The only English translation is George Ganss, S.J. (1970/1996, Institute of Jesuit Sources), in copyright and lending-only on archive.org (`constitutionsof00jesu`). The Latin text of 1606 is vendored (§1). |
| Nadal, *Annotations and Meditations on the Gospels*, **English** translation | A major first-generation Jesuit theological voice | The only English translation is Frederick Homann, S.J. (Saint Joseph's University Press, 2003), in copyright and print-disabled on archive.org. Nadal's Latin *Adnotationes* is vendored (§1). |
| Peter Faber's *Memoriale*, English translation | His own spiritual diary | No standalone public-domain English translation found. Faber's Latin *Memoriale* (1873) and Boero's biography are vendored (§1). |
| Peter Canisius, primary source | A major first-generation Jesuit | A 1622 English translation of his own *Summe of Christian Doctrine* is public domain and vendored (§1). |
| Diego Lainez, primary source in English | A major early Jesuit figure | No English translation of his own writing exists. His Latin *Epistolae et Acta*, Tomus I, 1536–1556, is vendored (§1). It ends before his generalate (1558–65), and no later volume is vendored. |
| Borgia and Mercurian (Generals 1565–80, 1573–80), own writings | Institutional voice after 1562 | No file is vendored; the corpus-map holds none. Open. |
| *Jesuit Relations* and other missionary correspondence after Xavier | Global and missionary voice after 1552 | No file is vendored. Open; Doc_02 must state the gap. |
| Letters of Ignatius beyond 1547, in English | Ignatius's later letters | A second volume of the O'Leary/Goodier series was searched for and not found. Only the Latin Tomus I (§1) is vendored. |

## 5. Open cross-world questions

**Against sibling Era VII candidate The Tridentine Church (VI.22), researched separately this same pass:** real but not disqualifying source overlap. Both candidates would likely cite the Waterworth Trent Canons/Decrees, but with different evidentiary weight — native/foundational for the Tridentine Church (the body that convened and enacted them), implementing/corroborating here (the Jesuits as one of Trent's most vigorous executors). The Jesuits' own gravity-bearing spine (Ignatius's Exercises, Constitutions, Autobiography) belongs wholly to this world and touches nothing in the Tridentine Church's own material. Same shared-text pattern already precedented in the existing corpus (PAHC/Latin-Apologists' Tertullian case) — flag for whichever Doc_02 runs first to settle who claims "native" register on the shared Trent text.

## 6. Step 0 scope notes (for whoever drafts Doc_01)

**Doctrinal floor clears.** Ignatius and the first-generation Jesuits are Nicene and Chalcedonian. Trent's own canons reaffirm the Nicene Creed and Chalcedonian Christology, and Ignatius's Exercises and Autobiography contain no Trinitarian or Christological deviation.

**The Chinese and Malabar Rites controversy is inside the window.** Ricci's method in China (from the 1580s), de Nobili's Madurai accommodation (from 1606), Gregory XV's 1623 ruling on Malabar practices, the Jiading conference (1627–28) and Propaganda Fide's 1645 decree all fall between 1540 and 1650. Its later condemnations come after 1650. Doc_01 treats it as a scope boundary, per Step 0 §4 item 4.
