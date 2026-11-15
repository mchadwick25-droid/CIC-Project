# Library search log: era 8 (1650-1815), batch 1, the global files, 2026-11-15

The search record for the first era 8 batch: Africa, Egypt, Ethiopia, the Syriac churches, Latin America and Asia.
The wants are in `ERA8_WANTS_MASTER.md` beside this file (groups 2, 3, 4, 5 and part of 6). The searches were run by
the first era 8 session and are summarized in `Handover.md`; this session fetched every candidate again by its
archive.org identifier, read each imprint, had the contents mapped, and vendored 32 files. The vendored files,
their state and their shelves are in `Build/Ministry/Features/Source-Library/CFT-Wants.md` (the "Era 8, batch 1"
section).

## Rights rule used

A printed imprint of 1930 or earlier, read on the title page in the OCR or on the scan's page image; a reprint
counts by its own date; no NC or ND licence, no permission notice, no access-restricted item. Nothing was taken
under the rule for American books of 1931-1963.

Three coordinator calls of 15 November under Mark's ruling of that day on title pages that print no year
("Copyright notice yes, preface with a check": a copyright notice dated 1930 or earlier counts; a dated preface
counts when the library catalog's date agrees). The coordinator's call, which Mark may overrule, is that a printed
licence or approbation leaf is the same kind of evidence as a dated preface.

1. **Rhodes, Cathechismus (Rome, Propaganda press): taken.** The title page prints no year. The licence of
   Goswinus Nickel on the next leaf is dated "Romae 8. Iulij 1651" (page image, leaf n6), and the archive.org
   record's date is 1651. The header's rights line records the date and the leaf.
2. **Weld Blundell, The Royal Chronicle of Abyssinia (royalchronicleof00welduoft): not taken.** The scan has the
   half-title (leaf n4) and the publisher's leaf with "All rights reserved" (n5), then the Ge'ez text. No dated
   title page, preface or copyright notice is in the OCR (no "1922" anywhere; the only 192x date is a footnote's
   "Oct. 1921"), and the colophon gives no year.
3. **Merolla, A Voyage to Congo, in English (voyagetocongosev00mero): not taken.** A part of Churchill's
   Collection with no imprint of its own; the scan does not hold the volume's title page. The Italian original
   (1692) and the English of Pinkerton XVI are held already.

## Hosts

| host | state from this sandbox | used |
|---|---|---|
| archive.org (metadata, djvu.txt, page images) | reachable | all 32 files |
| gallica, HathiTrust, books.google downloads, MDZ, documentacatholicaomnia | blocked or broken, by the earlier logs | not tried |
| dbnl.org | reachable, by the earlier logs | not needed: Valentijn's third deel came from archive.org on the first try |

No host was newly refused by the network proxy.

## How each file was checked

Forty scans were fetched. Each download's byte count was compared with the size archive.org lists for the
djvu.txt, and all forty were equal. The Library thread read the title-page lines of each. Where the OCR did not
give the year cleanly, it read the page image: Vansleb's Histoire (leaf n4) and Nouvelle relation (n6); Rhodes's
Tunchinensis historiae (n4) and Cathechismus (n4, n6); the Historia cultus Sinensium (n6); Bruce, vol. 2 (n12);
Guidi's Versio (n8) and Textus (n6); Gobat (n9); Baldaeus in English (n12 engraved, n14 letterpress); Barros
(n2); Pallu (n2); Valentijn, deel 3 (n4). Five mappers (Sonnet, read-only) then mapped the contents of the files
to be taken: divisions by their heading lines, editorial matter, the wanted passages, mixed voices, OCR quality
and the end of each book. The Library thread spot-checked the wanted passages in ten files and corrected one
range (Maigrot's Mandate ends at host line 15921, where his signature stands; the longer range first reported
ran on into a later piece).

Three host dates differ from the title pages: Guidi's Versio is 1912 (host 1910); Valentijn's third deel is 1726
(host 1724); al-Jabarti's tome V is 1890 (host 1888). The headers give the title-page year.

## What was taken, by want

**Kongo and West Africa.** Proyart's Histoire de Loango (1776) in French; the English is held in Pinkerton XVI.
Pascoe's Two Hundred Years of the S.P.G., vol. 1 (1901), for Thomas Thompson and Philip Quaque; the first bound
volume stops inside the chapters on India, and the second volume (twohundredyearso02pasc, Asia onward) was
fetched, checked and not taken. McCarter's Dutch Reformed Church in South Africa (1869).

**Egypt.** Vansleb's Histoire de l'Église d'Alexandrie (1677), his Nouvelle relation (1677) and its English, The
Present State of Egypt (1678). Butcher, vol. 2 (1897). Al-Jabarti's chronicle, tome V of the Cairo French
translation (1890), which holds the obituary of Ibrahim al-Jawhari under the year 1209.

**Ethiopia.** Bruce's Travels, vols 2 and 3 (1790). Gobat's Journal in the London first edition (1834), which
the census names; the New York edition of 1850 (journalthreeyea01bairgoog) was fetched and not taken, as a later
edition of the same book. Guidi's Annales regum Iyasu II et Iyo'as: the translation (1912), which is in French,
and the Ge'ez text (1910).

**The Syriac Orthodox.** Parry's Six Months in a Syrian Monastery (1895). The scan opens with Columbia's
microfilm target, which carries the library's standard statement on photocopying under US copyright law; it is
not a statement about this book, and the title page reads 1895.

**Latin America.** Vieira's Maria Rosa Mystica, parts 1 (1686) and 2 (1688); Barros's Vida (1746); Vieira's
Cartas, tomos 1 and 2 (1735); Antonil (1711); the Code noir in Prault's collection of 1767, which prints the
Edict of March 1685 and the Louisiana edict of March 1724. The Code noir of 1743 (codenoirourecuei00fran) was
fetched and not taken: a second collection of the same acts.

**Asia.** Launay's Histoire générale, tomes 1 and 2 (1894), to 1836; tome 3 (cihm_54002, from 1836) was fetched
and left for era 9. Pallu's Relation abrégée (1682). Rhodes's Divers voyages (the 1682 printing), his
Tunchinensis historiae (1652) and his Cathechismus (1651). The Historia cultus Sinensium (Cologne, 1700), which
prints Maigrot's Mandate in Latin; its Continuatio (bub_gb_rG8lStorjTwC, 1700) was fetched and not taken. The
Sketch of the Catholic Church in Ceylon (1848). Baldaeus in Dutch (1672) and in English (Churchill, 1703).
Valentijn's third deel (1726), which holds the church affairs of Amboina; the second deel
(oudennieuwoostin02vale, 1724) was fetched and not taken, since the first session did not find the church book in
it.

## Not found, from the first session's searches (not searched again)

The relations of Bernardo da Gallo and Lorenzo da Lucca (no print by 1930); Zucchelli's Italian; Capitein;
Thompson's own account (an image-only scan); Ntsikana's hymn in a print by 1930; the acts of the Synod of Mount
Lebanon of 1736 (Collectio Lacensis, vol. 2, is not on archive.org); Charon's tome I (never
printed); Hernández y Dávalos and Morelos; Úrsula de Jesús in a print by 1930; Launay's Lettres de Mgr Pallu and
Documents historiques; the Monita in an early print; Rego's Life of Joseph Vaz and any English Life printed by
1930; Huang Bolu; André Ly's Journal; the Sichuan synod of 1803; Urakawa; Tenchi hajimari no koto; the
Varthamanappusthakam; Ittoop; E. M. Philip (1908). The queries are in the first
session's reports, which did not survive it; the list above is from `Handover.md`.

## Held for Mark

- Ximénez, Historia de la provincia de San Vicente de Chiapa y Guatemala, vols 1 (1929) and 2, the Biblioteca
  Goathemala uploads: licence CC BY-NC-ND 3.0. Vol. 3, with Cancuc, is dated 1931.
- Rhodes's catechism in a modern Vietnamese upload (phep-giang-tam-ngay): CC BY-NC-ND 4.0.

## Left for a later batch

Vieira's Sermões (early volumes located by the first session: sermoensdopanton01viei 1683, 07viei 1689, 00viei
1699): none chosen. Dobrizhoffer in Latin and English, the Muratori files and the other Catholic Europe candidates
of `Handover.md` go with batch 2. Pascoe vol. 2 and Launay tome 3 are located for era 9.
