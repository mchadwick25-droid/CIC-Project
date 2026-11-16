# Round 1 changes, era 8 batch 2 (2026-11-16)

Every finding of `R1_review.md` was accepted. Each was corrected in `mkspec2.py`, and the 37 files, their
registry entries, seed rows and shelf rows were removed and vendored again from the corrected spec. Nothing was
patched in place.

| finding | what changed |
|---|---|
| F1 Campbell | The year is 1908, read on the page image (leaf n3, the leaf after the title page; the title page, n2, prints no year). File renamed `..._1908.txt`; header, rights line, registry, seed and shelf row follow. The publisher line now says which leaf prints what. |
| F2 Todd and Bray | The direction is reversed: Todd says the Biographia Britannica article copies this Life. |
| F3 Gibbons | The dedication is signed Hoxton-Square, 11 April 1780 (host lines 131-134); the preface is unsigned. Header and date source corrected. |
| F4 Dutton | The list of tracts is I-XXI in Part III, continued as XXII-XXXIII in the Appendix; "26" is gone. |
| F5 Gleaner vol. III | Play ranges corrected: Virtue Triumphant at about 643-4809, The Traveller Returned at 6157-8771. |
| F6 Gleaner vol. III | Date sources give only what the volume prints (No. LXXXVII written December 1796; title page February 1798). |
| F7 McGready | The narrative carries the heading the volume prints, with the contents' wording beside it. |
| F8 Vieira | "printed in his lifetime" removed from all three notes. |
| F9 Dutton | Junk lines given as 86-112. |
| F10 Dutton | The letter's date is 1750, with her tract list's number XIV cited for an earlier printing of unknown year. |
| F11 Orton | 1766 removed; the date is the preface's, 1765. |
| F12 Love | "about twelve printed lines". |
| F13 Cooley | Chapters VIII (5326) and IX (5664) added. |
| F14 Cooley | The sermon was delivered in June 1805 (host lines 4109-4110); its preface is dated 30 December 1805 (4129). The reviewer's line numbers were a few lines off and were read again. |
| F15, F16 Gleaner | Vols. I-II: "Essays and a serial story"; the judgment on her faith removed; the Margaretta numbers completed. |
| F17 Soli | Date start 1758. |
| F18 Muratori | "the second part came out in 1747" removed. |
| F19 Relation | The separate "to the reader" removed; the preface runs 419 to about 830. |
| F20 Marsollier | The privilege is of 21 July 1758. |
| F21 Launay | The author line is credited to the title page. |
| F22 Continuatio | The second Vindiciae was offered on the ides (13) of November 1699. |
| F23 Quesnel | The note speaks of the Réflexions as a whole and says what was not checked. |
| F24 notes | Shelf and ruling reasons removed from five notes; they stand in the Decision-Log entry and Open-Gaps 298. Parry's note now gives the 1892 visit and the society named in the prefatory note, and drops the Sayfo clause. |
| F25 slugs | Russell's essay has the slug `russell-david`. The Davies memoir row is split into three rows under `gibbons-thomas`, `finley-samuel` and `bostwick-david`, each with an `authors_ruled` entry. |

After the change the spec's line-anchor checks pass, the map check is valid, and the registry checks pass.
