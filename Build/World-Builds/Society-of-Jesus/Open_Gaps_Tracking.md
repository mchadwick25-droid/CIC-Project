# Open Gaps — The Society of Jesus

Append-only ledger for this world's build. Entries are numbered and dated; a merged entry's number never changes. Cross-references cite subject and date, not a bare number. The world has no registry code yet, so the folder stays at `Build/World-Builds/Society-of-Jesus/`.

---

## OG-1 — Institutional voice after 1556 is thinner than a first reading of the corpus suggests (2026-09-30)

**Source:** `Step0_Review_Round3.md`, finding S1.
**Status:** Open. Binding on Doc_02.

The vendored volumes cover the order's institutional voice as follows, checked against their own title pages:

| Vendored file | Title page reads | Covers |
|---|---|---|
| `lainez_epistolae-et-acta-v1-lat_1912.txt` | TOMUS PRIMUS 1536-1556 | Ends before Lainez's generalate (1558–65) |
| `polanco_chronicon-v1-lat_1894.txt` | TOMUS QUINTUS (1555); body opens ANNUS 1555 | The single year 1555 |
| `nadal_epistolae-v1-lat_1898.txt` | TOMUS PRIMUS (1546-1562) | Nadal's letters to 1562 |
| `salmeron_epistolae-v2-lat_1906.txt` | TOMUS PRIMUS 1536-1565 | Salmeron's letters to 1565 |
| `salmeron_epistolae-v3-lat_1906.txt` | TOMUS SECUNDUS 1565-1585 | Salmeron's letters to 1585 |

Institutional voice is dense to 1556, partial to 1562, and after that rests on one correspondent (Salmeron) to 1585. Nothing vendored gives the voice of Lainez as General, of Borgia (1565–72), or of Mercurian (1573–80). Doc_02 must not look for Lainez's generalate or Polanco's earlier years in these files. Doc_02 either narrows its institutional claims after 1556 to what is held, or acquires later volumes first.

**Disagreement between review rounds.** Round 2 of the Step 0 review supplied a re-dating of "Lainez (General 1558–65) ... c. 1580" without checking the volumes' title pages. Round 3 found it wrong. The title pages above support Round 3. The Round 2 wording is not carried into any document.

## OG-2 — Vendored file headers contradict the corpus-map on second-witness status (2026-09-30)

**Source:** `Step0_Review_Round3.md`, finding L3 (carried from Round 2, finding m4).
**Status:** Open. Owner: Library thread.

The provenance headers of the files vendored on 2026-09-25 say the text is "a second witness, never primary evidence". That contradicts the corpus-map and `Build/worlds/_cross-world/LIBRARY-DECISION-LOG.md` point 5 for the clean-scan files. Under that ruling only the 1606 Constitutions, Nadal's *Adnotationes* and Ribadeneira's 1572 life are held at second-witness status for scan quality. Files affected among this world's works: `lainez_epistolae-et-acta-v1-lat_1912.txt`, `nadal_epistolae-v1-lat_1898.txt`, `nadal_scholia-in-constitutiones-lat_1883.txt`, `polanco_chronicon-v1-lat_1894.txt`, `salmeron_epistolae-v2-lat_1906.txt`, `salmeron_epistolae-v3-lat_1906.txt`, `ignatius-loyola_epistolae-et-instructiones-v22-lat_1903.txt`. The corpus-map notes are the authority. The headers are to be corrected at source by the Library thread.

The second half of L3, the "Correction (2026-09-25)" narration in the Constitutions and *Adnotationes* corpus-map notes, is no longer present in `cic/corpus-map/`.
