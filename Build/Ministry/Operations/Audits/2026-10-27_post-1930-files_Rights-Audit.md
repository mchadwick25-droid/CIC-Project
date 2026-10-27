# Rights audit: the vendored files published after 1930

Dated 2026-10-27. Asked by Mark after the question of replacing CCEL and other intermediary hosts. Scope: the eight vendored files whose names carry a year of 1931 or later, which cannot rest on the project's 95-year date rule. A four-file extension covers files whose headers show a later reprint. Method: read each file's own rights header, check the host's own statement where the host was reachable, and run the renewal search that the Knappen file's header describes (the 1960 to 1962 renewal catalogues as transcribed by Project Gutenberg, ebooks 11821 to 11826) plus the 1974 to 1976 catalogues (ebooks 11849 to 11854) for the 1947 file. This is the project's reading, not legal advice.

## Result

| File | Verdict | Basis that holds |
|---|---|---|
| `knappen_two-elizabethan-puritan-diaries_1933.txt` | Cleared | 1933 US publication not renewed; host states "Public domain according to HathiTrust rights database" |
| `luther_small-catechism_smith1994.txt` | Cleared | Translator's release printed in the file itself |
| `hetum_history-of-the-tartars-flower-of-histories-of-the-east_bedrosian2004.txt` | Cleared | Translator's declaration in the file; the translator uploaded it himself |
| `doctrina-christiana_manila-1593-tgl-spa_wolf1947.txt` | Cleared | 1593 original public domain; no renewal found for the 1947 facsimile essay; Library of Congress and Gutenberg statements |
| `all-saints-bristol_pre-reformation-records-part1_burgess1995.txt` (also parts 2 and 3) | Cleared with conditions | CC BY-SA 4.0 set on each archive.org item by the Bristol Record Society |
| `aphrahat_demonstrations-2-7_hallock1932.txt` | Probably public domain; recorded basis is weak | No renewal found; the recorded basis is only a transcriber's declaration |

## Findings by file

**Knappen 1933.** The header's claim holds. The renewal search over the 1960 to 1962 catalogues finds no entry for Knappen, "Elizabethan Puritan", or the American Society of Church History. The archive.org item's rights field reads "Copyright review: Public domain according to HathiTrust rights database". Two independent bases. No action.

**Luther, Small Catechism (Smith).** The header rests the status on Project Gutenberg's hosting, and says the translation is modern and not public domain by date. The stronger basis is in the file itself, at the end of the text: "It has been placed in the public domain by him [the translator]. You may freely distribute, copy or print this text." Gutenberg's ebook 1670 page also reads "Public domain in the USA". The release is Robert E. Smith's, for Project Wittenberg, covering his 1994 translation as revised in 2002 and 2004. Verdict: cleared. Suggested fix: cite the in-file release in the header, since the current wording leans on Gutenberg's label.

**Het'um, History of the Tartars (Bedrosian).** The translator's declaration is in the file ("This translation is in the public domain. It may be copied and distributed freely."), and the archive.org item was uploaded by the translator's own account. The preface says passages from Burger's 1988 edition of Pynson's c. 1520 English appear in square brackets; the preface describes them as translations of alternate words, which would make them the translator's own work. That wording was not checked against Burger. Verdict: cleared. Residual risk: low.

**Doctrina Christiana (1947 facsimile, Wolf's essay).** The 1593 work is public domain by date. A facsimile adds no copyright. The open part is Edwin Wolf 2nd's 1947 introductory essay, which would have needed renewal in 1975. The renewal catalogues for 1974 to 1976 were searched for Wolf, Edwin; Doctrina Christiana; Tagalog; and Philippines. No entry for this work turned up. The header's note says the renewal check could not be run in that session; this search supplies it. The header also cites the Library of Congress record statement and Project Gutenberg's declaration. Verdict: cleared. Suggested fix: add the renewal search to the header.

**All Saints', Bristol, parts 1 to 3 (Burgess).** The archive.org items `bristol-record-society-46`, `-53` and `-56` all carry `licenseurl` CC BY-SA 4.0, uploaded by the Society's account with the note "A Bristol Record Society volume, uploaded by the General Editor". Each volume prints "© Clive Burgess". Conditions:
- CC BY-SA allows commercial use, so the organization's for-profit form is not a bar.
- Attribution is required, and share-alike applies to any redistribution of the text or an adaptation of it.
- Open point: the printed notice names the editor as the copyright holder and the host record shows the Society as the one licensing. The Society's own licence statement could not be read: the University of Bristol pages for the Society returned 403 and 404 to the sandbox. Whether the Society holds the editor's licence is unconfirmed.

**Aphrahat, Demonstrations VII and II (Hallock, 1932).** The header says the file rests on Roger Pearse's 2006 declaration that material on his page is public domain, and notes that the 1932 translation does not clear the date rule. Pearse transcribed the text and did not own Hallock's translation, so his declaration is a weak basis. A better basis exists but is not recorded: the 1960 to 1962 renewal catalogues, which cover books, pamphlets, serials and contributions to periodicals, contain no entry for "Oriental Research", "Aphra", "Persian Sage", "Nashotah", or Frank H. Hallock (the only Hallocks listed are other people). A work first published in 1932 and not renewed passed into the public domain. This is a negative result in a transcribed catalogue, so name variants and transcription errors could hide an entry. Verdict: probably public domain. Suggested fix: record the non-renewal basis in the header and the registry entry, and have a person confirm in the Stanford renewal database, which the sandbox could not read (it answers automated requests with a JavaScript challenge, and the audit did not work around it).

## Extension: four reprint-dated files

Checked and clear, no action: `cyprian_opera-omnia-critical_hartel-csel3-pars1-2.txt` (1868 and 1871), `wyclif_de-civili-dominio-liber-primus-lat_poole1885.txt` (1885), `taeuferakten-wuerttemberg_quellen-geschichte-wiedertaeufer-1-deu_bossert1930.txt` (1930, which the rolling rule has covered since 1 January 2026), `eunomius_first-apology_whiston1711.txt` (Whiston's 1711 translation as Pearse re-edited it for the web in 2002; the translation is public domain, Pearse's edits are not claimed).

A first pass over all headers for a publication date of 1931 or later was too loose: most hits were fetch dates. The filename years and the four extensions above are the real set. A file whose header shows a pre-1931 date but whose edition was printed later would not be caught by either method.

## Open items

1. Hallock: add the non-renewal basis to the header; one person to confirm in the Stanford renewal database.
2. Bristol: confirm the Society's licence authority; record the attribution string and the share-alike condition in the registry entries.
3. Smith and Wolf: header wording fixes described above.
4. None of these changes has been made to the files. Header edits to vendored files are Mark's call.
