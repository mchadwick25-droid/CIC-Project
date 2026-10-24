# Source Readiness Dossier — Shakers

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and why it
exists.

**Atlas ID:** VII.12
**Corpus-map slug:** `shakers`
**Time window:** 1774-1815
**Region(s):** England, then America; census `regions`: North Europe
**Dossier author / date:** Claude, Library thread, Era VIII source-research pass, 2026-10-23
**Corpus-map / `cic/texts/` state as of:** branch `library/era-viii-2026-10`, this pass.

## 1. Already assigned

13 works across 12 vendored files in `cic/corpus-map/shakers.yaml`.

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| An Account of the People called Shakers (1812) | brown-thomas | context | assigned | whole work | `brown-thomas_account-of-the-people-called-shakers_1812.txt` |
| The Manifesto (1818) | dunlavy | tradition | assigned | whole work | `dunlavy_manifesto-declaration-of-the-doctrines-and-practice-of-the-church-of-christ_1818.txt` |
| A Brief Statement of the Sufferings of Mary Dyer (1818) | dyer-mary | context | assigned | whole work | `dyer-mary_brief-statement-of-the-sufferings-of-mary-dyer_1818.txt` |
| Shakers: Compendium (1859) | evans-frederick | transmission | assigned | whole work | `evans-frederick_shakers-compendium-of-the-origin-history-principles-rules_1859.txt` |
| The Shakers' Covenant (1873) | grosvenor | tradition | provisional | the Covenant or Constitution | `grosvenor_shakers-covenant-with-a-brief-outline-of-shaker-history_1873.txt` |
| The Shakers' Covenant (1873) -- Grosvenor's introduction and outline of Shaker history | grosvenor | transmission | assigned | the Introduction and the outline of Shaker history | `grosvenor_shakers-covenant-with-a-brief-outline-of-shaker-history_1873.txt` |
| The Kentucky Revival (1808) | mcnemar | tradition | assigned | the account of the entrance and progress of Shakerism | `mcnemar_kentucky-revival-with-the-entrance-of-shakerism_1808.txt` |
| A Declaration of the Society of People (commonly called Shakers) (1815) | shakers | tradition | assigned | whole work | `shakers_declaration-reasons-for-refusing-to-aid-the-cause-of-war_1815.txt` |
| A Summary View of the Millennial Church (1823) | shakers | tradition | assigned | whole work | `shakers_summary-view-of-the-millennial-church_green-wells1823.txt` |
| Millennial Praises (1813) | shakers | tradition | assigned | the Preface and the four parts of hymns | `shakers_millennial-praises-gospel-hymns_1813.txt` |
| Testimonies of the Life, Character, Revelations and Doctrines of Mother Ann Lee (second edition, 1888) | shakers | tradition | assigned | whole work | `shakers_testimonies-of-mother-ann-lee-and-the-elders_bishop-wells1888.txt` |
| Shakerism Detected (1810) | smith-james | context | assigned | whole work | `smith-james_shakerism-detected_1810.txt` |
| The Testimony of Christ's Second Appearing (second edition, 1810) | youngs-benjamin-seth | tradition | assigned | whole work; the Advertisement and Preface name the Ministry as publisher | `youngs-benjamin-seth_testimony-of-christs-second-appearing_1810.txt` |

## 2. Cross-link opportunities

| file | locus | why | suggested role / confidence |
|---|---|---|---|
| asbury_journal-v3_1821.txt | entries on passing Shaker settlements (about lines 7294, 12026, 16729, 20039) and the index line "Remarks on Shakers" | a Methodist bishop's outside view of the Shaker villages in New England and the West, 1790s to 1810s | context / provisional |
| asbury_journal-v2_1821.txt | about line 7838 (Shakers living in celibacy) | as above, earlier | context / provisional |
| wesley-j_journal-v7_curnock1909.txt | about line 24519 (an editor's note on a member who went to America and joined the Shakers) | a passing note only | context / provisional, low value |

## 3. Verified acquisition leads

| title | author | translator | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| Shakerism: Its Meaning and Message | Anna White and Leila S. Taylor | none | 1904 (host 1905) | https://archive.org/details/shakerismitsmea00taylgoog | pd-us-by-date | metadata API, djvu 0.88 MB, OCR 0.85, 23 October 2026 |
| Ann Lee (the founder of the Shakers), a biography, with memoirs | F. W. Evans | none | 1869 | https://archive.org/details/annleethefounder00evanuoft | pd-us-by-date | metadata API, djvu 0.23 MB, 23 October 2026 |
| Reply to the Shakers' statements, called a "Review of the Portraiture of Shakerism" | Mary M. Dyer | none | 1824 | https://archive.org/details/replytoshakersst00dyer | pd-us-by-date | metadata API, djvu 0.25 MB, OCR 0.91, 23 October 2026 |
| Testimony of Christ's Second Appearing (fourth edition) | Benjamin Seth Youngs (attributed) | none | 1856 | https://archive.org/details/testimonyofchris00youn | pd-us-by-date | metadata API, djvu 2.12 MB, 23 October 2026 |
| The Kentucky Revival (Shaker reprint) | Richard McNemar | none | 1846 | https://archive.org/details/kentuckyrevivalo00mcne | pd-us-by-date | metadata API, djvu 0.32 MB, 23 October 2026 |
| The Shaker Collection / Papers of Shakers (manuscript microfilm, 1781 onward) | various | none | 1781-1830s | https://archive.org/details/per_the-shaker-collection_papers-of-shakers_1792_266 | pd-us-by-date | metadata API, djvu 0.00-0.01 MB (images only, no OCR), 23 October 2026 |

The manuscript microfilm series is the village journals and papers the census calls "the lived community record". It would need transcription, not OCR intake, so it is a lead for a later pass only.

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Testimonies 1816 (Hancock first edition) | census source, founding testimony | not found on the Internet Archive (title, creator and subject searches, 23 October 2026) |
| Testimony 1808 (Lebanon, Ohio first edition) | census source | not found; the 1810 second edition is vendored |
| Valentine Rathbun, Account of the Matter, Form, and Manner of a New and Strange Religion (1781) | census source, earliest record | no Internet Archive item found under title, creator or "Nisqueunia/Niskeyuna" searches |
| Amos Taylor, Narrative of the Strange Principles (1782) | census source | no Internet Archive item found |
| Millennial Laws (1821/1845) | census source | no public-domain printing found; the published texts are twentieth-century |
| Mary Dyer, A Portraiture of Shakerism (1822) | hostile ex-member classic | only a 1972 reprint, access-restricted (lending only) |
| testimonychrist00youngoog (1810) | second scan of the 1810 Testimony | duplicate of the vendored edition |
| testimonyofchris01youn (1823, third edition) | the Testimony | later reprint, OCR 0.78; the 1810 is cleaner and earlier |
| testimoniesoflif00bish, preceptsofmother0000unse | 1888 Testimonies | duplicate scans of the vendored edition (the second is a 2026 upload of the same 1888 text) |
| asummaryviewmil00wellgoog, asummaryviewmil02wellgoog | 1823 Summary View | duplicate scans |
| scnesdelaviedeb01murggoog | Dunlavy 1818 under a wrong French host title | duplicate of the vendored Princeton scan, lower OCR (0.84) |
| millenialpraise00tallgoog | Millennial Praises 1813 | duplicate scan |
| accountofpeoplec02browuoft | Brown 1812 | duplicate scan |
| abriefstatement00conggoog | Dyer 1818 | duplicate scan |
| shakerscovenantn00harv | Grosvenor 1873 | duplicate scan of the same copy |
| 2183092R.nlm.nih.gov, A brief exposition of the fanaticism ... of the people called Shakers (1822) | hostile pamphlet | no _djvu.txt (404) |
| Gutenberg #60732, Industries and Inventions of the Shakers / Shaker Music | Shaker subject on Gutenberg | modern booklet, outside the window and not a primary witness; not opened |

## 5. Open cross-world questions

- McNemar's Kentucky Revival carries the Cane Ridge camp meetings and the Springfield Presbytery schism: should its revival half be assigned to `the-second-great-awakening-and-camp-meeting-worl` and `the-stone-campbell-restoration-movement`? Rows are in the spec as provisional context.
- The Shakers grew out of a Quaker-adjacent circle in Manchester ("Shaking Quakers"): is any Quaker cross-link wanted, or is that only a story-level relation?
- No nineteenth-century Shaker world exists in the census. Evans 1859 and Grosvenor 1873 are assigned here as transmission; is that the right home?
- The census dates the world 1774-1815, but the Society's own institutional record (Summary View 1823, Manifesto 1818) mostly falls just after. How far past 1815 should the build lean on them?

## 6. Recommendation (portfolio decision for the project lead; does not block library work)

**Build.** The Society's own voice is deep and in print inside or just past the window: the 1810 Testimony (its confession and the floor-question text), the 1813 hymnal, the 1815 corporate declaration, the testimonies of the founders, and two doctrinal treatises. The hostile record the census names is also here in three different voices (Brown, Dyer, Smith), so the asymmetry the census flags can be shown, not just described. The gaps are real and should be stated plainly in the build: no first editions of the Testimony (1808) or Testimonies (1816), no Rathbun or Taylor, and the village journals exist only as unOCR'd microfilm. All sources are English, and the world is distinct from every sibling in the census: no other world carries a female-Christ confession, celibate communal order and a sung theology of this kind.

