# Source Readiness Dossier — The Methodist Revival

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is.

**Atlas ID:** VII.5
**Corpus-map slug:** `the-methodist-revival`
**Time window:** 1738–1815
**Region(s):** Britain, then America
**Dossier author / date:** this world's own build thread (`meth`). No separate source-research thread ran ahead of this world's Step 0 and Doc_02 work, so the dossier is written from the research that work performed, not as a prior input to it. It reflects one build thread's single pass, for this world only.
**Corpus-map / `cic/texts/` state:** the world has 12 works assigned across 7 vendored files (see the table below). No Methodist or Wesley bucket or vendored file existed before this world's build.

## 1. Already assigned

12 works, across 7 vendored files, assigned to `cic/corpus-map/the-methodist-revival.yaml`:

| work | author | role | confidence | source file |
|---|---|---|---|---|
| The Journal of the Rev. John Wesley, A.M. (Curnock ed.), Vol. I — the Aldersgate account | wesley-john | tradition | assigned | `wesley-j_journal-v1_curnock1909.txt` |
| The Journal of the Rev. John Wesley, A.M. (Curnock ed.), Vol. I — Curnock's own Editorial Introduction | curnock-nehemiah | context | assigned | `wesley-j_journal-v1_curnock1909.txt` |
| Sermons on Several Occasions, Vol. I — Sermon I, "Salvation by Faith" | wesley-john | tradition | assigned | `wesley-j_sermons-v1_1771.txt` |
| Sermons on Several Occasions, Vol. I — Sermon II, "The Almost Christian" | wesley-john | tradition | assigned | `wesley-j_sermons-v1_1771.txt` |
| Sermons on Several Occasions, Vol. I — Sermon III, "Awake, Thou That Sleepest" | wesley-charles | tradition | assigned | `wesley-j_sermons-v1_1771.txt` |
| Sermons on Several Occasions, Vol. I — Sermons IV–XVI | wesley-john | tradition | provisional | `wesley-j_sermons-v1_1771.txt` |
| Minutes of Several Conversations (the Large Minutes) — Sections I–II | wesleyan-conference | tradition | assigned | `wesley-j_large-minutes_1850.txt` |
| A Collection of Hymns for the Use of the People Called Methodists (1780) — Preface | wesley-john | tradition | assigned | `wesley-c_hymns-methodists_1780.txt` |
| A Collection of Hymns for the Use of the People Called Methodists (1780) — the hymns themselves | wesley-charles | tradition | provisional | `wesley-c_hymns-methodists_1780.txt` |
| The Journal of the Rev. Francis Asbury, Vol. I (1771–1786) | asbury-francis | tradition | provisional | `asbury_journal-v1_1821.txt` |
| The Journal of the Rev. Francis Asbury, Vol. II (1786–1800) | asbury-francis | tradition | provisional | `asbury_journal-v2_1821.txt` |
| The Journal of the Rev. Francis Asbury, Vol. III (1800–1815) | asbury-francis | tradition | provisional | `asbury_journal-v3_1821.txt` |

Full per-row loci, quotability notes, and OCR caveats: `Build/worlds/meth/Source_Registry.md`.

## 2. Cross-link opportunities

**None found.** The corpus-map's assignments for every already-vendored Reformed/Calvinist and Moravian-adjacent file were checked, given this world's doctrinal echo with the Reformed tradition (Doc_01 §4) and its Moravian formative relationship (Doc_01 §7). Nothing in `cic/texts/` is assigned any Moravian-tradition role (no `the-moravian-church-at-herrnhut` bucket exists, §5 below), and the Reformed Cities' vendored corpus (Calvin, Zwingli, Bullinger) is doctrinally adjacent but not the same tradition or figures. No source usable in both worlds' registries was identified. **No corpus-map pair entry is recorded:** ruling on a fleet-level pair is outside this build thread's authority. The Moravian relationship is stated in prose (Doc_01 §7, `Open_Gaps_Tracking.md` item 2) and is not represented as a corpus-map pair.

## 3. Verified acquisition leads

Not yet vendored. Full detail and per-item rationale: `Build/worlds/meth/Source_Acquisition_Manifest.md` (items G1–G10). This table restates only the leads that carry a specific, checkable URL.

| title | author | translator | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| The Journal of the Rev. John Wesley, A.M. (Curnock ed.), Vols. II–VIII | John Wesley | ed. Nehemiah Curnock | [1909?]–1916 | `archive.org/details/a613690402wesluoft` (Vol. II; III, IV, VIII independently confirmed under the sequential identifier `a613690401wesluoft`–`a613690408wesluoft`) | pd-us-by-date | Direct archive.org metadata check (title, publisher, date and rights all match the already-vendored Vol. I), meth build thread |
| Journal of the Rev. Francis Asbury (1852, Lane & Scott ed.) | Francis Asbury | — | 1852 | `archive.org/details/journalofrevfran03asbu` | pd-us-by-date | Found via search, host page not re-fetched; **not used**. The 1821 first edition (already vendored) is the earlier, more directly authorial printing |

**Not yet reduced to a specific verified URL:** George Whitefield's own Journals/Sermons (Manifest G5); the annual Conference Minutes distinct from the Large Minutes (G3); the remaining 28 Standard Sermons (G2 — Vol. I holds 16, not 12, so 44 − 16 = 28 remain); Mary Bosanquet Fletcher's 1771 letter, Hester Ann Rogers's *Account*, the *Arminian Magazine*'s lay narratives, the Wesley–Crosby correspondence (G6–G9, all Article 20 cases not yet searched for); the Twenty-Four Articles of Religion (G10); class/band/circuit records (G4, likely a research-library, not public-domain-text-search, acquisition channel).

**A live cross-world allocation question, not an acquisition item, that bears on how G5 is eventually used.** Doc_01 §9 escalates to the project lead the question of how George Whitefield's post-1741 institutional legacy should be allocated across this world's census entry and its neighbours (VII.6, VII.10). Any future use of a Whitefield primary text (once acquired) should be read against whichever option the project lead selects.

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Wesley's Large Minutes, final 1789 edition | The historically definitive form of the text, issued in Wesley's own lifetime | Not located; the 1850 reprint of an 1797 printing was vendored instead and is explicitly disclosed as a different, later printing (`cic/texts/REGISTRY.yaml`, `wesley-j_large-minutes_1850.txt`) — not closed as unusable, but the 1789 edition itself remains an open, not-yet-found lead and is not folded into the 1850 reprint's claim |
| "Journal of the Rev. Francis Asbury," archive.org identifier `journalofrevfran00asbu` | Initially reported by a search-summary as Volume I | The file's own title page reads "VOL. II", so the identifier is Volume II, which is vendored as `asbury_journal-v2_1821.txt` (`cic/texts/REGISTRY.yaml`) |

## 5. Open cross-world questions

- **The Moravian Church at Herrnhut (`the-moravian-church-at-herrnhut`, Atlas VII.4).** This world's own doorway event (Aldersgate, 24 May 1738) took place at a Moravian-influenced society; Wesley's own first Moravian contact was actually two years earlier still (his 1735–36 voyage to Georgia, per Doc_01 §7); the relationship broke in 1740 over "stillness" doctrine. VII.4 is a separate, "Pre-Survey Candidate" census entry with **no corpus-map bucket and no vendored texts of its own**. Named here, not decided: a future Moravian-world build thread (or the project lead) should determine how that world's own Doc_01 characterizes its relationship to this one, rather than this world's own build thread deciding it unilaterally in either document. Full detail: `Build/worlds/meth/Doc_01_World_Identification_Boundaries_Orientation.md` §7 and `Build/worlds/meth/Open_Gaps_Tracking.md` item 2.
