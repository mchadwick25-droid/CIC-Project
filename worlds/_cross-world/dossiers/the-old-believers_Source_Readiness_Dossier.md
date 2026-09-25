# Source Readiness Dossier — The Old Believers

See `worlds/_cross-world/SOURCE-READINESS.md` for what this is and why it
exists.

**Atlas ID:** VII.7
**Corpus-map slug:** the-old-believers (census id; matches
`cic-website/data/world-census.json`'s own `id` field)
**Time window:** 1666-1815
**Region(s):** Russian north, Siberia (North Europe, per the census's own
`regions`)
**Dossier author / date:** Claude, obel library-stage source-research pass,
2026-09-25
**Corpus-map / `cic/texts/` state as of:** 2026-09-25, this same pass (no
prior Old Believer/Avvakum material existed in either before this pass —
independently re-checked, per `CLAUDE.md`'s "Scaling the build" section,
which already recorded that finding as of the same date)

## 1. Already assigned

Before this pass, nothing. This pass adds:

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| The Life of the Archpriest Avvakum by Himself | avvakum | tradition | assigned | whole work, 155pp. | `avvakum_life-of-archpriest-avvakum_harrison-mirrlees1924.txt` |
| Zhitie protopopa Avvakuma, im samim napisannoe (original-language text) | avvakum | tradition | assigned | whole work | `avvakum_zhitie-protopopa-avvakuma-orv_wikisource-transcription-nd.txt` |

## 2. Cross-link opportunities

None found. This is this project's first Slavic/Russian-Orthodox-schism
world; nothing already vendored for any other world (all Greek East texts
vendored so far are patristic-era, 3rd-8th c.) plausibly names Avvakum, the
1666-67 Moscow council, the Solovetsky siege, or the Vyg community. Checked
by title/author scan of `cic/corpus-map/WORKS.yaml` and `AUTHOR-IDS.yaml`
for "Avvakum", "Nikon", "Solovetsky/Solovki", "Old Believer", "raskol" —
no hits.

## 3. Verified acquisition leads

| title | author | translator | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| The Life of the Archpriest Avvakum by Himself | Avvakum Petrov | Jane Harrison & Hope Mirrlees, preface D. S. Mirsky | 1924 | archive.org/details/bwb_C0-ARS-081 | PD by date (1924 publication, >95 years); `access-restricted-item` absent from this identifier's own metadata (confirmed distinct from two OTHER archive.org identifiers for later reprints of the same translation, both `access-restricted-item: true`) | Direct archive.org Metadata API fetch + direct unauthenticated `_djvu.txt` download, HTTP 200, 2026-09-25 |
| Zhitie protopopa Avvakuma, im samim napisannoe (Old East Slavic/early Russian original) | Avvakum Petrov | n/a (original language) | composed c. 1673; this transcription undated | ru.wikisource.org (page cites az.lib.ru as its own source) | Underlying 17th-c. composition is PD by any measure; page's own `ЛИЦЕНЗИЯ = PD-old` infobox field | Direct MediaWiki `action=raw` fetch, HTTP 200, 2026-09-25. NOT independently verified hop-by-hop against a specific dated critical edition — az.lib.ru itself unreachable this pass (network egress allowlist). See Open_Gaps_Tracking.md. |

**Not yet closed, not yet vendored (found but not downloaded this
pass):** the extended (*prostrannaya*) redaction of *Povest' o boyaryne
Morozovoy* (Tale of Boyarynya Morozova) — a real file was located at
`upload.wikimedia.org/wikipedia/commons/c/c4/Повесть_о_боярыне_Морозовой_
(пространная_редакция).pdf`, but the download itself returned HTTP 429
(Wikimedia rate-limiting) this pass, not a rights or existence problem.
A live lead for the next pass, not listed in §4 below since it was not
actually run down to a closed answer — see `Open_Gaps_Tracking.md` /
Doc_02 §10 (Missing Voices) for the same finding.

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| archive.org `lifeofarchpriest0000avva` (Archon Books, 1963) | Same translated text, different scan | `access-restricted-item: true` (confirmed via metadata API and a direct 401 on file fetch) — controlled digital lending, not freely downloadable. Superseded by `bwb_C0-ARS-081` (the actual 1924 first edition, unrestricted) — use that identifier instead. |
| archive.org `bwb_KR-696-874` (Hogarth Press, 1963 reprint) | Same translated text, different scan | Same finding: `access-restricted-item: true`, HTTP 401 on direct file fetch. Closed for the same reason. |
| HathiTrust `mdp.39015014696838` (full view, per catalog record) | Catalog record shows this as the 1924 London Hogarth Press edition, "Full view" | Not independently confirmed downloadable this pass — `babel.hathitrust.org` returned a Cloudflare bot-challenge page (HTTP 403) to both WebFetch and a direct `curl`, in this sandbox. Not needed once `bwb_C0-ARS-081` cleared instead; leaving this open as a second front-matter cross-check if ever wanted (title page details already independently confirmed from the vendored file's own OCR, so this is not blocking). |
| `az.lib.ru` (Maksim Moshkov's library) direct access | Named as the Wikisource transcription's own cited source; would let the transcription chain be checked one hop closer to a critical edition | Host not in this session's network egress allowlist (HTTP 403, "Host not in allowlist"). Could not be checked this pass. |
| `krotov.info` (Повесть о боярыне Морозовой transcription) | A full transcription of the Tale of Boyarynya Morozova, a named figure in this world's own census entry | Host not in this session's network egress allowlist (HTTP 403, "Host not in allowlist"). Could not be checked this pass. |
| Evfrosin, *Otrazitel'noe pisanie o novoizobretennom puti samoubiistvennykh smertei* (1691) | Named in the census as a genuine internal Old Believer dissent against self-immolation — would be valuable own-voice-against-the-practice material | Only scholarly discussion of the work (pravenc.ru, sedmitza.ru, a 2020s academic article by N. S. Demkova) surfaced this pass, no accessible full-text transcription of the work itself. Not closed as "doesn't exist" — closed as "not found this pass"; a genuine acquisition lead for a future pass, not yet verified. |
| Поморские ответы (Pomorian Answers, 1723, Semyon Denisov et al.) | Named in the census as a foundational bespopovtsy document | The `ru.wikisource.org` page for this title exists but is a stub (manuscript-listing metadata only, no license field, no transcribed answer text) — not a usable source. `rusneb.ru` (Russian National Electronic Library) hosts scanned editions but as image/catalog pages, not confirmed-downloadable plain text, and `rusneb.ru` was not tested against the network allowlist this pass. Real acquisition lead for a future pass. |
| Solovetsky petitions (1667, esp. the Fifth Petition) | Named in the census as the monastery's own founding statement of the case | Only secondary discussion and one manuscript-image archive (British Library Endangered Archives Programme, EAP1017-1-9) surfaced — no clean transcription found this pass. Real acquisition lead for a future pass. |

## 5. Open cross-world questions

- None specific to another sibling world's own territory. This is a
  self-contained Russian Orthodox schism with no plausible overlap (yet
  found) with any other built or candidate world in this fleet's own
  corpus. If a later Greek-East or Balkan Orthodox world's own research
  turns up Nikon-era Greek-authority material (the Greek patriarchs whose
  approval Nikon cited), that would be the first genuine cross-link — flag
  it back here if found.
