# Library eras 4-5: round 2 recheck (2026-11-15)

A fresh Opus reviewer, read and grep only, checked the eleven round 1 findings against the corrected files. The
text below is the reviewer's own, as returned.

I checked all 11 findings by reading and grepping only, with no edits. All are fixed in the file headers. Three small leftovers remain, and none is blocking.

1 (blocking): fixed. The editor's note at file lines 46937-46941 reads "der Bericht ist in dieser Form nur hier erhalten … Über die Synode vgl. sonst noch Nicetas »Vita sive certamen sancti Ignatii«". The new header, both shelf notes and the REGISTRY and README CONTENTS text say the same: "survives in this form only here" plus Nicetas's Life of Ignatius. "Abridged" and "only surviving record" are gone from the header (0 hits), the shelf notes and CONTENTS. "The Latin abridgment of the council of 861" is left only in the WANT clause: REGISTRY.yaml:23844, README.md:2447 and CFT-Wants.md:384. It is labelled as Open-Gaps 266's own wording ("WANT: … not held"), and CONTENTS just before it corrects it, so I find it acceptable rather than misleading.
2: fixed. Creator line says the translation is joint. The opening note is placed at about OCR line 17923, Dümmler's introduction at about 18062, and the manuscript list (Vladislav 1469/1479) in the opening note. The shelf title and note say "the editors' Latin".
3: fixed. Header, registry and the cistercian and staging shelf notes say "as Powicke prints it, ending where Walter announces four stories".
4: fixed. Depositions to about 37500, appendices to about 38400 (registry line 23984, README line 2350).
5: fixed. General index from about 62692 (header, registry line 23936, README line 3565).
6: fixed. "Charlemagne's ecclesiastical capitularies, with their index of titles" in the header, registry line 23856 and README line 3103.
7: fixed in the header (Publisher line, "read on the page image, leaf n8").
8: fixed. OCR line 37 (file line 49) shows "1905."; OCR line 63 (file line 75) shows "1906.". The header gives both.
9: fixed. Shelf locus is about OCR lines 95370-98310 (cistercian-monasticism.yaml line 82).
10: fixed. "dbnl's text ends at page 301 … whether the printed volume runs past page 301 was not checked" in the header, registry line 23992 and README line 2720.
11: fixed. File line 92 (OCR line 80) reads "1g03".

Leftovers (minor):
- The registry row for Mansi XII still says "facsimile reprint of the Florence 1766 printing" without the page-image note. It is not false, but it lacks the caveat.
- The Deusdedit shelf row id still contains "…the-acts-of-constantinople-861-abridged-in-deusdedit-s…", in byzantine-imperial-church-macedonian.yaml line 15 and _staging/deusdedit_*.yaml line 3. It is an identifier only, but the reviewed wording survives there.
- The registry rows for Mansi XII, Mansi XXIV and Levison don't carry the Publisher or date-line detail, so there is no stale copy of the old claims there either.

README.md has no stale copies of the old claims (no "about 66", "81005" or Powicke "in full").

BLOCKING POINTS REMAINING: none

## After the recheck

No blocking point remains. The Mansi XII registry and queue titles keep "Florence 1766"; the header says where that
was read. The Deusdedit shelf row keeps its row id, which is assigned once and never changed; the row's title and
note carry the corrected words.
