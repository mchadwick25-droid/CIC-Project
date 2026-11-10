# Handover — Library thread for the Church Family Tree, batch 6

Written 2026-11-10 at the end of batch 5. Batch 6 starts in a fresh session after the weekly reset.

## The charter and the coordinator

Mark's charter (2026-11-10): "launch a library thread that is patterned after previous threads with
full research, organization and render abilities to find the sources you need, public domain in any
language we can find it." The coordinator is session `session_01JMNsSDbFsmawtDvuAiukNQ`; report to it
with `send_message` after each batch. Read CLAUDE.md first, all of it.

## Where things stand

| batch | PR | what it did |
|---|---|---|
| 1 | #1577 | the later-worlds people gate; Library defects in Open-Gaps 165 and 152 |
| 2 | #1579 | 22 files for the eras 8-9 holds; Mark's Bell and Pedalion rulings |
| 3 | #1581 | 20 files for the earliest named gaps of Open-Gaps 158; AP10 |
| 4 | #1584 | 27 files for the religious orders and the Maronites |
| 5 | this PR | ME-21 (Rabinowitz, from `_intake/`); 12 files for six early modern mission and Eastern gaps; held texts shelved on the new eras 8-9 entries; the batch 4 Duwayhi correction |

- **The record:** `CFT-Wants.md`, one section per batch.
- **The decisions:** `Decision-Log.md` in this folder.
- **Open-Gaps entries:** 170-172, 193 and 194 in `Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md`.
- **The page for Mark:** https://claude.ai/artifact/RTJ2uXC4rjqKEguvt4UiDP. Its source is not in the repo.
  Read it with the Artifact tool's `read` action, then republish to the same `url`.

## How a batch runs

`HANDOVER-batch4.md` holds the full procedure (steps 1-10). Batches 4 and 5 added these points:

- **The holdings check must grep by title words and spelling variants**, as well as filenames.
  Batch 4 missed a held al-Duwayhi because it grepped "douaih" and "maron", not "duwayhi" or
  "maruniyya". Grep `cic/texts/REGISTRY.yaml` for title words, then check the archive id.
- **The shelf rule.**
  - A text goes on its own tradition's entry when one covers its date of writing.
  - If not, it goes on the church-wide entry of that date, where one exists. For the Latin church
    these are the Gregorian, Avignon to Lateran V, Tridentine, ancien regime and long nineteenth
    century entries.
  - Otherwise it is vendored with no shelf.
  - A book written after an entry's window but about it goes on as `context`.
  - Use `needs-ruling` where the fit is the tree's question, for example Ukrainian Orthodoxy on the
    Russian church's entry.
- **Check main's census first.** Data releases add entries mid-batch: release 33 added about
  26. Merge main in before the PR, and move rows onto any new entry that fits better.
- **PDF intake from `_intake/`:**
  - read the Google id from the PDF's own links (`pdfinfo -url`);
  - extract with `pdftotext -layout`;
  - check the page breaks against `pdfinfo` pages, and read the end;
  - clear the files from `_intake/`.
- **Headers.** The header is nine lines, then a blank line, a row of 70 underscores and a blank line,
  so the offset is "add 12". Never write a name, date or place the title page or host does not give.
  Batch 5 caught two of these before writing: a first name for Pastor Faltin, and a printing date of
  1904 that the volume's own notes contradict.

## Batch 6: Europe, 1650-1815 and after — searched, not yet vendored

Two Sonnet searchers ran in batch 5's session. Their scratch folders do not survive the container, so
everything needed to re-fetch is here. The searchers report every byte count as matching. None of it is
verified yet: re-read each host record and title page yourself before vendoring. "Rights none" means
the record has no rights field, so the imprint date is the basis.

Entries that exist (check main again first):
- `hungarian-and-transylvanian-protestantism-1650-1815`;
- `catholic-church-ancien-regime` (1650-1815) and `catholic-church-long-nineteenth-century` (1815-1906);
- `the-haugean-awakening` (1796-1842) and `laestadianism-and-the-nordic-revivals` (1844-1906).

None exists after 1650 for the Waldensians, Schwenkfelders, Remonstrants or Church of Scotland, none
after 1785 for the Hutterites, none after 1787 for the French Reformed, none after 1786 for the
Delaware Swedes, and none for the Nordic state churches after 1650.

| gap | candidates (archive.org id, date, djvu bytes, rights) | voice | notes |
|---|---|---|---|
| Transylvanian Unitarians after 1650 | `kereszteny-magveto_1861_1` (Keresztény Magvető 1861, 497,212, none); `unitriusegyhzit00unkngoog` (church marriage law, 1889, 104,363, NOT_IN_COPYRIGHT); `jegyzoknyv0000magy` (Főtanács minutes, 1912, 1,990,366, none) | insider | The Magvető (Kolozsvár, from 1861) runs to the 1930s; pick volumes. Shelf: the 1650-1815 entry only for texts written then; later ones have none yet. Ferencz (1875, 1907) is held. |
| Hutterites after 1785 | `diehuttererste00wolk` (Wolkan, Die Hutterer, 1918, 429,990, none; Fraktur OCR garbled) | outsider | No insider print before 1931 found. Horsch's The Hutterian Brethren is dated 1931, which is too late. |
| Waldensians after 1655 | `histoiredelaglor00arna` (Arnaud, Glorieuse rentrée, Pignerol 1880, 496,996, none, clean); `israelofalpscom01must` (Muston, Israel of the Alps, 1866, 1,637,373, none); `gloriousrecover00arnagoog` (Arnaud in English, 1827, 448,026, NOT_IN_COPYRIGHT) | insider (Arnaud led the 1689 Return) | Muston's French original (1851) is also on archive.org. |
| Schwenkfelders after 1650 | `genealogicalreco00krie` (Genealogical Record, 1879, 568,890, none); `schwenkfelderhym00seip` (Seipt, Schwenkfelder Hymnology, 1909, 231,198, NOT_IN_COPYRIGHT); `lehre-und-ordnungs-regeln` (Schultz, written 1838, 6,747) | insider | `lehre-und-ordnungs-regeln` carries a CC BY-NC-ND licence on its record. Check it before use, and don't take it if the licence covers the text. The 1762 hymnal itself was not found. Kriebel (1904) is held. |
| Remonstrants after 1650 | `compleatsystemor01limb` (Limborch, Compleat System, 1702, 1,292,990, NOT_IN_COPYRIGHT; title page lost to stamps); `deremonstrantsc00rogggoog` (Tideman, De Remonstrantsche Broederschap, 1905, 1,041,721, NOT_IN_COPYRIGHT); `deremonstranteng0000unse` (gedenkboek, 1919, 378,065, none) | insider | Limborch's Latin Theologia Christiana (1730, `theologiachristi0000limb`, 5 MB) also exists. |
| Nordic state churches after 1650 | `svenskakyrkansh00corngoog` (Bishop Cornelius, Svenska kyrkans historia, 1886, 1,680,088, NOT_IN_COPYRIGHT); `dendanskekirkesh02helw` (Helweg, Den Danske Kirkes Historie II, title page 1855, 1,362,485, none) and vol. I `dendanskekirkesh01helw` (1,163,497) | insider-leaning (Helweg's office unchecked) | Not found: the 1686 Church Law, Pontoppidan's Sandhed, Kingo, Brorson. The Vidalin scan is undated and garbled. |
| Church of Scotland after 1650 | `ActsOfTheGeneralAssemblyOfTheChur` (Acts of the General Assembly 1638-1842, preface dated May 1843, 4,875,360, none; the record has no date or real creator); `historyofsufferi03wodr` (Wodrow III, 1829, 2,946,642, NOT_IN_COPYRIGHT, clean); `memoirsoflifetim00bostrich` (Thomas Boston's Memoirs, 1899, 1,681,214, NOT_IN_COPYRIGHT) | insider | The Acts item is a user upload whose record has no rights or date. Read its title page and imprint carefully. |
| English and Welsh Catholics after 1650 | `doddschurchhist04dodduoft` (Dodd-Tierney IV, 1,672,486, NOT_IN_COPYRIGHT; record date "1839-1943", so confirm the volume's own year) and V `doddchurchhist05dodduoft` (1,727,574); `endofreligiousco02milniala` (Milner, End of Religious Controversy, 1818, 368,630, NOT_IN_COPYRIGHT) | insider | Shelf: the ancien-regime entry for texts written 1650-1815, the long-nineteenth-century entry after. Kirk's Biographies was not found. |
| French Reformed after 1787 | `histoiredusynode0001bers` (Bersier, Histoire du synode général 1872, t. I, 807,899, none); `duprotestantism00prgoog` (Samuel Vincent, Du protestantisme en France, 1860 ed., 1,284,936, NOT_IN_COPYRIGHT) | insider | The Bulletin of the Société de l'histoire du protestantisme français is on archive.org (`bulletinhistori01fragoog`, 02, 05), not yet opened. |
| Delaware Swedes after 1786 | `annalsofswedes00clay` (Clay, Annals of the Swedes on the Delaware, 1835, 215,181, NOT_IN_COPYRIGHT, clean); `recordsofholytri09holy` (Records of Holy Trinity, Wilmington, 1697-1773, with an abstract to 1810, 1890, 1,452,218, none) | insider (Clay was rector of Gloria Dei) | Check that the Holy Trinity abstract reaches past 1786. |

## What is left after batch 6

1. **Open-Gaps 158:** 49 named gaps remain before batch 6. Batch 6 covers about ten.
   - **Batch 7, after 1815:** English Dissent, the Old Believers, the Brethren, Armenian Catholics and
     the Mekhitarists, the Moravians, New England Congregationalists, Welsh chapels, the Shakers,
     English Unitarians, the New Church, Korean Catholics, the Haitian church, the Inner Mission,
     Malagasy churches, the Melkites after 1911.
   - **Batch 8, after 1906:** the denominations whose window ends in 1906. The public-domain window
     is only 1906-1930.
2. **Open-Gaps 159:** Alexandria, Cyprus, the Polish, Czech-Slovak and Macedonian Orthodox
   churches; the ten Eastern Catholic churches the tree never names.
3. **Open-Gaps 162:** the living marks after 2010. These are mostly web material; ask the
   coordinator whether they are the Library's.
4. **The loci pass:** 707 staging files say "whole".
5. **Still open from earlier batches:**
   - the Hebrew letters of Rabinowitz;
   - a clean al-Duwayhi;
   - a Chinese Catholic's own text (Andreas Ly's Journal, 1906; the 1803 Sichuan synod);
   - a Puthenkoor text of its own;
   - Kongolese texts besides the Paiva Manso letters;
   - the Syriac Orthodox Church 1300-1915 (Wright's catalogue);
   - batch 2's not-found list (AF-8, ME-4, ME-7, RV-9, AP13, the Molokans, Peking after 1808, the
     1860 Concordat).
