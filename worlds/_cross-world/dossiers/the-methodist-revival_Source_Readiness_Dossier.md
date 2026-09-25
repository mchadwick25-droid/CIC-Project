# Source Readiness Dossier — The Methodist Revival

See `worlds/_cross-world/SOURCE-READINESS.md` for what this is.

**Atlas ID:** VII.5
**Corpus-map slug:** `the-methodist-revival`
**Time window:** 1738–1815
**Region(s):** Britain, then America
**Dossier author / date:** this world's own build thread (`meth`), 2026-09-25. **Disclosed plainly rather than smoothed over:** no dossier existed for this world before this date — no separate source-research thread ran ahead of this build's own Step 0/Doc_02 pass, so this dossier is written *retroactively*, from the same research that pass already performed, rather than being the prior input that pass would ordinarily have worked from. A future world sharing this era/region should not assume this reflects a proactive sweep predating its own Doc_02 stage the way, for example, `worlds/rzg/`'s or `worlds/witt/`'s own dossiers do — it reflects one build thread's own single pass, done under time pressure, for its own world only.
**Corpus-map / `cic/texts/` state as of:** 2026-09-25 — a cold start before this pass (confirmed via `corpus_map.py --coverage`, no methodist/Wesley bucket or vendored file existed as of the morning of 2026-09-25); this pass assigned 11 works across 7 vendored files.

## 1. Already assigned

11 works, across 7 vendored files, assigned to `cic/corpus-map/the-methodist-revival.yaml`:

| work | author | role | confidence | source file |
|---|---|---|---|---|
| The Journal of the Rev. John Wesley, A.M. (Curnock ed.), Vol. I — the Aldersgate account | wesley-john | tradition | assigned | `wesley-j_journal-v1_curnock1909.txt` |
| The Journal of the Rev. John Wesley, A.M. (Curnock ed.), Vol. I — Curnock's own Editorial Introduction | wesley-john | context | assigned | `wesley-j_journal-v1_curnock1909.txt` |
| Sermons on Several Occasions, Vol. I — Sermon I, "Salvation by Faith" | wesley-john | tradition | assigned | `wesley-j_sermons-v1_1771.txt` |
| Sermons on Several Occasions, Vol. I — Sermon II, "The Almost Christian" | wesley-john | tradition | assigned | `wesley-j_sermons-v1_1771.txt` |
| Sermons on Several Occasions, Vol. I — Sermons III–XII and following | wesley-john | tradition | provisional | `wesley-j_sermons-v1_1771.txt` |
| Minutes of Several Conversations (the Large Minutes) — Sections I–II | wesley-john | tradition | assigned | `wesley-j_large-minutes_1850.txt` |
| A Collection of Hymns for the Use of the People Called Methodists (1780) — Preface | wesley-john | tradition | assigned | `wesley-c_hymns-methodists_1780.txt` |
| A Collection of Hymns for the Use of the People Called Methodists (1780) — the hymns themselves | wesley-charles | tradition | provisional | `wesley-c_hymns-methodists_1780.txt` |
| The Journal of the Rev. Francis Asbury, Vol. I (1771–1786) | asbury-francis | tradition | provisional | `asbury_journal-v1_1821.txt` |
| The Journal of the Rev. Francis Asbury, Vol. II (1786–1800) | asbury-francis | tradition | provisional | `asbury_journal-v2_1821.txt` |
| The Journal of the Rev. Francis Asbury, Vol. III (1800–1815) | asbury-francis | tradition | provisional | `asbury_journal-v3_1821.txt` |

Full per-row loci, quotability notes, and OCR caveats: `worlds/meth/Source_Registry.md`.

## 2. Cross-link opportunities

**None found this pass.** Checked `corpus_map.py --coverage` and skimmed the corpus-map's own assignments for every already-vendored Reformed/Calvinist and Moravian-adjacent file (given this world's own doctrinal echo with the Reformed tradition, Doc_01 §4, and its real Moravian formative relationship, Doc_01 §7): nothing in `cic/texts/` as of this pass is assigned any Moravian-tradition role at all (no `the-moravian-church-at-herrnhut` bucket exists — §5 below), and the Reformed Cities' own vendored corpus (Calvin, Zwingli, Bullinger) is doctrinally adjacent but not the same tradition or figures, so no genuine cross-link candidate — a source actually usable in both worlds' own registries — was identified. This section stays empty honestly rather than forcing a weak link.

## 3. Verified acquisition leads

Not yet vendored, each independently confirmed against its actual host — full detail and per-item rationale in `worlds/meth/Source_Acquisition_Manifest.md` (items G1–G10); this table restates only the leads that carry a specific, checkable URL as of this pass.

| title | author | translator | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| The Journal of the Rev. John Wesley, A.M. (Curnock ed.), Vols. II–VIII | John Wesley | ed. Nehemiah Curnock | [1909?]–1916 | `archive.org/details/a613690402wesluoft` (Vol. II; III, IV, VIII independently confirmed under the sequential identifier `a613690401wesluoft`–`a613690408wesluoft`) | pd-us-by-date | Direct archive.org metadata check (title/publisher/date/rights all matching the already-vendored Vol. I), meth build thread, 2026-09-25 |
| Journal of the Rev. Francis Asbury (1852, Lane & Scott ed.) | Francis Asbury | — | 1852 | `archive.org/details/journalofrevfran03asbu` | pd-us-by-date | Found via search, host page not independently re-fetched this pass — **not used**; the 1821 first edition (already vendored) was preferred once located, since it is the earlier, more directly authorial printing |

**Not yet reduced to a specific verified URL, named here for the next pass rather than left only in the Manifest:** George Whitefield's own Journals/Sermons (Manifest G5); the annual Conference Minutes distinct from the Large Minutes (G3); the remaining ~32 Standard Sermons (G2); Mary Bosanquet Fletcher's 1771 letter, Hester Ann Rogers's *Account*, the *Arminian Magazine*'s lay narratives, the Wesley–Crosby correspondence (G6–G9, all real Article 20 cases this pass did not have time to search for); the Twenty-Four Articles of Religion (G10); class/band/circuit records (G4, likely a research-library, not public-domain-text-search, acquisition channel).

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Wesley's Large Minutes, final 1789 edition | The historically definitive form of the text, issued in Wesley's own lifetime | Not located this pass; the 1850 reprint of an 1797 printing was vendored instead and is explicitly disclosed as a different, later printing (`cic/texts/REGISTRY.yaml`, `wesley-j_large-minutes_1850.txt`) — not closed as unusable, but the specific 1789 edition itself remains a genuinely open, not-yet-found lead, not folded silently into the 1850 reprint's own claim |
| "Journal of the Rev. Francis Asbury," archive.org identifier `journalofrevfran00asbu` | Initially reported by a search-summary as Volume I | **Wrong on direct inspection** — the file's own title page reads "VOL. II"; corrected before vendoring (`cic/texts/REGISTRY.yaml`). Logged here as a real, disclosed correction, not merely in the Registry, since it is exactly the kind of "title-matching without host verification" failure this dossier format exists to catch |

## 5. Open cross-world questions

- **The Moravian Church at Herrnhut (`the-moravian-church-at-herrnhut`, Atlas VII.4).** This world's own doorway event (Aldersgate, 24 May 1738) took place at a Moravian-influenced society; Wesley's own first Moravian contact was actually two years earlier still (his 1735–36 voyage to Georgia, per Doc_01 §7); the relationship broke in 1740 over "stillness" doctrine. VII.4 is a separate, "Pre-Survey Candidate" census entry with **no corpus-map bucket and no vendored texts of its own as of 2026-09-25** — confirmed directly this pass, not assumed. Named here, not decided: a future Moravian-world build thread (or the project lead) should determine how that world's own Doc_01 characterizes its relationship to this one, rather than this world's own build thread deciding it unilaterally in either document. Full detail: `worlds/meth/Doc_01_World_Identification_Boundaries_Orientation.md` §7 and `worlds/meth/Open_Gaps_Tracking.md` item 2.
