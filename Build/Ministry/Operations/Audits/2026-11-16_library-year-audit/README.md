# The year audit: header years against host dates (Open-Gaps 305, 2026-11-16)

Thread B (Library), session_01JMNsS9WRK3s4XStRhyW6qw. A read-only list of every held file under `cic/texts`
whose header year differs from the host's date for the same item, with the year read on the page image. No
file was changed. The page Mark was sent: https://claude.ai/artifact/SsidCpJNKaA7JXgLS6kkAK.

## Method

1. A script read each file's header (both header layouts) for its year and for the archive.org item it names,
   and fetched each item's own `date` and `year` from the host (`fetch_meta.py`).
2. Where no year in the header matched any year in the host's date, the file was flagged (`flagged_296.json`:
   206 that differ, 82 whose host record gives no date, 8 whose named item the host does not return).
3. For the 206, readers opened the title page, its verso or the imprint on the page image and wrote down
   what it prints (`READ_BRIEF.md`, `leaves.py`, and `crop.py` from
   `../2026-11-16_library-era9-located/tools/`). The twelve with a year of 1925 or later on either side were
   read first. Results: `page_reads_206.json` (209 rows; three files name two host items).

## Counts

2,424 files. 1,996 agree with the host. 206 differ: header right in 189, wrong in 12, not settled by the scan
in 5. Not comparable: 123 name no archive.org item (Project Gutenberg 59, GitHub text collections 18, Roger
Pearse's transcriptions 9, CCEL 7, Wikisource 1, others 29); 82 host records carry no date; 8 name an item the
host does not return; 9 have no year in the header.

## The one that bears on rights

`van-braght_martyrs-mirror_sohm1886.txt` (item `MartyrsMirror`) is marked public domain on 1886. The scan is
a Herald Press printing: the title leaf's verso prints "Second English edition, thirty-third printing, 2012"
and "Copyright © 1938 by Mennonite Publishing House" (the file's lines 119-124). It opens with a publisher's
preface written for the modern printing. Sohm's translation was first published in 1886 at Elkhart, Indiana.
This printing has not been compared with the 1886 one. Mark ruled on 2026-11-16: "Retire it, find the 1886
scan (Recommended)". The 1886 scan is found (`bloodytheatreorm00brag`). Nine live census sources cite the held file, so he
then ruled "Swap now, then retire (Recommended)": Open-Gaps 307, the next session's first job (`Handover.md`). Every record that cites it is in `martyrs_mirror_citations.json`.

## The other eleven wrong years (none changes a rights call; to be corrected under Open-Gaps 308)

| File | Header | Page image |
|---|---|---|
| `groves_memoir-of-anthony-norris-groves_3rd-ed1859.txt` | 1859 | "THIRD EDITION ... 1869." |
| `unity-of-the-brethren_historie-tezkych-protivenstvi-cirkve-ceske-ces_1890.txt` | 1890 | "V Praze ... 1870." |
| `cassiodorus_opera-institutiones-pl70-lat_migne1847.txt` | 1847 in the name, "1866" in the rights basis | 1865 |
| `reitz_historie-der-wiedergebohrnen-t5-deu_1715.txt` | 1715 | "Gedruckt im Jahr Christi 1717" |
| `isidore-seville_sententiae-eccl-officiis-historia-gothorum-pl83-lat_migne1860.txt` | 1860 | imprint 1862 |
| `pseudo-justin_epistle-to-diognetus-grc_lake1917.txt` | 1917, G. P. Putnam's Sons | MCMXIII, Heinemann / Macmillan |
| `subbotin_materialy-dlia-istorii-raskola-v1-dokumenty-rus_1874.txt` | 1874 | cover imprint 1875 |
| `booth-tucker_life-of-catherine-booth-v1_1893.txt` | 1893 | copyright notice "in the year 1892" |
| `mansi_sacrorum-conciliorum-collectio-tomus-26-1344-1409-lat_welter-facsimile1901.txt` | 1901 | facsimile imprint 1903 |
| `new-jerusalem-church_liturgy-with-proud-hymns-and-spiritual-songs_baltimore1793.txt` | 1793 | "Baltimore ... 1792." |
| `augustine_sermones-341-396-et-appendix-lat_migne-pl39.txt` | 1863 | 1865 |

Also, not a year: the header of `evliya-celebi_narrative-of-travels-v1-pt2_hammer1846.txt` says "Part I"; the
title page prints "VOL. I., PART II."

## Not settled by the scan

The Waterworth Trent (undated title page; preface 22 May 1848; a catalogue of 1888 bound in; the header
already says so); Studia Biblica v5 (no printed volume title page in this copy); Subbotin v3 (no printed year
for the volume); Mansi 27 (1903 likely, 1902 not ruled out); Abelard PL 178 (a typewritten replacement title
leaf only).

## Scans printed after 1930 whose headers already say so

Procopius, Wars, vols 4 and 5 (title pages 1962; "First printed 1924 / 1928. Reprinted 1954, 1962"); Wyclif, De
Ecclesia ("First reprinting, 1966", Johnson Reprint). No copyright line on the pages read.

## Limits

The method finds a wrong year only where the host disagrees with the header. The 1,996 that agree were not
read on the page image. Apart from the Martyrs' Mirror page, the reads have had no second reader. Several
headers cite the host text's line for the year where the held file's line is 12 further on (the header's own
length); the years are right.
