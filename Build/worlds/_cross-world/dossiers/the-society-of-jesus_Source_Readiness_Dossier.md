# Source Readiness Dossier — The Society of Jesus

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is.

**Atlas ID:** VI.11
**Corpus-map slug:** `the-society-of-jesus`
**Time window:** 1540–1650
**Region(s):** Rome, then worldwide
**Dossier author / date:** source-research thread, 2026-09-15; updated 2026-09-24
**Corpus-map / `cic/texts/` state as of:** 2026-09-24 — the four §3 leads
below, Xavier Vol. 2, and three new finds from a deeper
pass (Canisius, the Jesuit Constitutions' Latin original,
Nadal's own Latin original) have all been vendored, headered, registered,
and assigned. See §1 below for current state.

## 1. Already assigned

**No longer a cold start.** Ten works vendored and
assigned to `cic/corpus-map/the-society-of-jesus.yaml`:

| work | author | role | confidence | source file |
|---|---|---|---|---|
| The Spiritual Exercises of St. Ignatius | ignatius-loyola | tradition | assigned | `ignatius-loyola_spiritual-exercises_mullan1914.txt` |
| The Autobiography of St. Ignatius | ignatius-loyola | tradition | assigned | `ignatius-loyola_autobiography_oconor1900.txt` |
| Letters and Instructions of St. Ignatius Loyola, Vol. I | ignatius-loyola | tradition | assigned | `ignatius-loyola_letters-instructions-v1_oleary-goodier1914.txt` |
| The Canons and Decrees of the Council of Trent | council-of-trent | context | provisional | `council-of-trent_canons-and-decrees_waterworth1848.txt` |
| The Life and Letters of St. Francis Xavier, Vol. I | francis-xavier | tradition | assigned | `francis-xavier_life-and-letters-v1_coleridge1872.txt` |
| The Life and Letters of St. Francis Xavier, Vol. II | francis-xavier | tradition | assigned | `francis-xavier_life-and-letters-v2_coleridge1872.txt` |
| A Summe of Christian Doctrine (Canisius) | canisius | tradition | assigned | `canisius_summe-of-christian-doctrine_anon1622.txt` |
| The Life of the Blessed Peter Favre (Faber) | boero | context | provisional | `boero_life-of-peter-faber_coleridge1873.txt` |
| Constitutiones Societatis Iesu, cum earum Declarationibus | society-of-jesus | tradition | assigned | `jesuit-constitutions_constitutiones-societatis-iesu-lat_1606.txt` |
| Adnotationes et Meditationes in Evangelia (Nadal) | nadal | tradition | assigned | `nadal_adnotationes-et-meditationes-in-evangelia-lat_1595.txt` |

Two are Latin originals and PRIMARY content, not second witnesses — the
Constitutions (the Society's own governing document, closing what §4
originally flagged as "a real gap for a movement whose governing document
is this central") and Nadal's own Adnotationes — since no PD English
translation of either exists (checked directly, not assumed; see §4's
updated entries). Canisius is a genuine first find: no prior pass had
checked for any Canisius material at all.

## 2. Cross-link opportunities

Resolved — see §1: the Trent Canons/Decrees are vendored
and double-placed to the sibling `the-tridentine-church` candidate (VI.22),
consistent with §5's own reasoning below.

## 3. Verified acquisition leads

| title | author | translator/ed. | year | url | rights basis | verified by |
|---|---|---|---|---|---|---|
| Spiritual Exercises | Ignatius of Loyola | Elder Mullan, S.J. ("translated from the autograph") | 1914 | archive.org `spiritualexercis00ignauoft` | pd-us-by-date | direct fetch, 2026-09-15, `NOT_IN_COPYRIGHT` confirmed |
| Autobiography of St. Ignatius (dictated to Luis Gonçalves da Câmara, 1553–55) | Ignatius of Loyola | ed. J.F.X. O'Conor, S.J. | 1900 | https://www.gutenberg.org/files/24534/24534-h/24534-h.htm | pd-us-by-date | direct fetch, 2026-09-15, explicit PD ebook |
| Letters and Instructions of St. Ignatius Loyola, Vol. 1 (1524–1547) | Ignatius of Loyola | tr. D.F. O'Leary, ed. A. Goodier | 1914 | archive.org `LettersAndInstructionsOfStIgnatiusV1` | pd-us-by-date | direct fetch, 2026-09-15, Public Domain Mark confirmed. A selection (24 letters), not the full ~7,000-letter corpus; a Vol. 2/later-years volume may exist, not yet checked. |
| Council of Trent, Canons and Decrees | (conciliar) | James Waterworth | preface 1848, this printing c. 1888 | archive.org `thecanonsanddecr00unknuoft` | pd-us-by-date | direct fetch, 2026-09-15, `NOT_IN_COPYRIGHT` confirmed. Directly relevant: the doctrinal anchor the Jesuits implemented. |
| Life and Letters of St. Francis Xavier, Vol. 1 (1506, university years, India/Fishery Coast, Malacca/Moluccas 1541–48, extensive Xavier–Ignatius correspondence) | Francis Xavier | Henry James Coleridge | 1872 | archive.org `LifeLettersOfStFrancisXavierV1` | pd-us-by-date | direct fetch, 2026-09-15, Public Domain Mark confirmed. A companion Vol. 2 (later Japan/China years, Xavier's death 1552) likely exists under the same series — not yet checked. |

**Scale estimate:** Strong for a first pass — Mullan's Exercises (~150pp), O'Conor's Autobiography (~90pp), O'Leary/Goodier Letters Vol. 1 (24 letters), Waterworth's Trent (620pp), Coleridge's Xavier Vol. 1 (462pp, Vol. 2 likely available). Combined total plausibly in the hundreds of thousands of words once Vol. 2s are added — comparable in order of magnitude to existing built worlds' corpora, though not yet word-extracted since nothing is vendored.

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Jesuit Constitutions, **English** translation | The order's own governing document — should be central | Only English translation found is George Ganss, S.J. (1970/1996, Institute of Jesuit Sources) — archive.org `constitutionsof00jesu` is access-restricted, in-copyright, lending only. No PD English translation found. **Superseded, not simply closed** — checked for the Latin original 2026-09-24 and found multiple PD 16th-19th-c. editions; the 1606 Rome printing is now vendored as PRIMARY content for this world (§1). |
| Jerónimo Nadal, *Annotations and Meditations on the Gospels*, **English** translation | A major first-generation Jesuit theological voice | Only English translation is Frederick Homann, S.J. (Saint Joseph's Univ. Press, 2003) — print-disabled/restricted on archive.org. In copyright. **Superseded, not simply closed** — checked for the Latin original 2026-09-24 and found a PD 1595 edition, now vendored as PRIMARY content for this world (§1). |
| Peter Faber's *Memoriale* (full translation) | His own spiritual diary | No standalone PD English translation found. **Partially resolved 2026-09-24**: Giuseppe Boero's 19th-c. biography *The Life of Blessed Peter Favre* (archive.org `lifeofpeterfavre00boeruoft`) confirmed `NOT_IN_COPYRIGHT` and vendored (§1, role `context`) — but it remains a biography quoting the Memoriale, not a full translation of it; how much of the diary's own words it actually reproduces verbatim is still unchecked and flagged for a future pass before any passage is cited as Faber's own words. |
| Peter Canisius, any primary source | A major first-generation Jesuit (catechisms widely translated) — not previously checked at all | Checked 2026-09-24 and **found, not closed**: a 1622 English translation of his own *Summe of Christian Doctrine*, unambiguously PD (Early English Books, 1475-1640), now vendored (§1). Listed here to record that the search happened, not because it failed. |
| Diego Laynez (2nd Superior General), any primary source | A major early Jesuit figure | Checked 2026-09-24: no English translation of anything in his own hand exists; only a 19th-c. Spanish-language secondary biography (Rivadeneira, 1868) was found. Genuinely closed. |
| Xavier Vol. II, Letters Vol. II+ | Named as "likely exists, not yet checked" in the original 2026-09-15 pass | Checked 2026-09-24: Xavier Vol. II confirmed and vendored (§1, Public Domain Mark). A second volume of the O'Leary/Goodier Letters series (beyond 1524-1547) was searched for and not conclusively found — one low-confidence, unverifiable archive.org item surfaced but was not pursued further. |

## 5. Open cross-world questions

**Against sibling Era VII candidate The Tridentine Church (VI.22), researched separately this same pass:** real but not disqualifying source overlap. Both candidates would likely cite the Waterworth Trent Canons/Decrees, but with different evidentiary weight — native/foundational for the Tridentine Church (the body that convened and enacted them), implementing/corroborating here (the Jesuits as one of Trent's most vigorous executors). The Jesuits' own gravity-bearing spine (Ignatius's Exercises, Constitutions, Autobiography) belongs wholly to this world and touches nothing in the Tridentine Church's own material. Same shared-text pattern already precedented in the existing corpus (PAHC/Latin-Apologists' Tertullian case) — flag for whichever Doc_02 runs first to settle who claims "native" register on the shared Trent text.

## 6. Step 0 scope notes (for whoever drafts Doc_01/the Step 0 confirmation)

**Doctrinal floor clears without question.** Ignatius and the first-generation Jesuits are uncontroversially Nicene/Chalcedonian — Trent's own canons (confirmed PD-sourced above) explicitly reaffirm the Nicene Creed and Chalcedonian Christology as the Catholic position, and Ignatius's own Exercises and Autobiography contain no Trinitarian or Christological deviation. No internal complication comparable to Minucius Felix's silence or Lactantius' pneumatology was found.

**One scope note, correctly out-of-window, not a live complication:** the Chinese/Malabar Rites controversies intensify mid-to-late 17th c. and are formally condemned 1704/1742/1774 — well past this world's own 1650 close, and first-generation figures (Ignatius d. 1556, Xavier d. 1552, Nadal d. 1580) predate the dispute entirely. Note as correctly excluded rather than silently omitted, the same disclosure discipline this project applies elsewhere.
