# Story Tellings Review — Round 3

**Scope:** targeted check of the Opus re-rendered speech in all 11 tellings, and of the record-defect fixes Mark ordered on 14 October.
**Reviewer:** independent Agent invocation, model opus, with no part in the drafting, re-rendering or fixes.
**Outcome:** NOT CLEAR on one blocking finding (B1, the public page still told of a visit); spans and defect fixes otherwise clear. Last review file allowed; B1 closed under Mark's ruling with a mechanical check (Open_Gaps_Tracking.md, the story-tellings entry of 2026-10-14).

---

## Desert story tellings and record defects: review round 3 (targeted, last allowed)

Scope: uncommitted `git diff -- records/` on branch world/desert-story-tellings.
Reviewer: independent, read-only. No model or paid calls.

## Overall verdict: NOT CLEAR (one BLOCKING finding, a one-sentence fix)

Part 1 (renderings) is clear: every quoted span in all 11 tellings matches the
vendored source within the rendering bar. Part 2 is clear on every ordered defect
except one. The Sarah record now carries a sentence that is false: it says the
participant-facing page matches it, but the page still narrates the visit and
challenge that this round removed.

Checks run:
- `regate desert --base origin/main`: PASS. The only note is the existing
  desert.voice.craft FRE 53.7, not a regression.
- `records desert`: PASS.
- `grade_text` on every telling: FRE 71.7 to 91.5. kellia-day has no `telling` field.

## Part 1: quoted spans in the 11 tellings

| Story | Span (telling) | Source words (file:line) | Verdict |
|---|---|---|---|
| angel-hands-the-tablet | "In the name of the holy Trinity. The ordinance which the angel of the Lord commanded to Abba Pachomius." | identical (pachomius_rules-ethiopic_schodde1885.txt:168). Kept verbatim on purpose as the named first line. | PASS |
| angel-hands-the-tablet | "These prayers are few." | "Few are these prayers." (:176) | PASS |
| antony-call | "If you want to be perfect, go and sell what you have and give to the poor. Then come and follow me, and you will have treasure in heaven." | "If thou wouldest be perfect, go and sell that thou hast and give to the poor; and come follow Me and thou shalt have treasure in heaven." (npnf204:~31251-31253) | PASS |
| antony-call | "Do not be anxious about tomorrow." | "be not anxious for the morrow" (npnf204:~31264-31265) | PASS |
| antony-secret-burial | "Bury my body and hide it underground yourselves," / "Keep my words, so that no one may know the place but you alone." | "Bury my body, therefore, and hide it underground yourselves, and let my words be observed by you that no one may know the place ... but you alone." (npnf204:33510-33519) | PASS ("therefore" is a connective, carried by the narration) |
| antony-tomb-combat | "If you had any power, one of you would be enough. But the Lord has made you weak, so you try to frighten me with numbers." | "If there had been any power in you, it would have sufficed had one of you come, but since the Lord hath made you weak, you attempt to terrify me by numbers: and a proof of your weakness is that you take the shapes of brute beasts." (npnf204:31500-31503) | PASS. MINOR M1: the source sentence goes on past the colon. |
| antony-tomb-combat | "Where were you? Why did you not appear at the start, to end my pain?" | "Where wert thou? Why didst thou not appear at the beginning to make my pains to cease?" (npnf204:31514-31516) | PASS |
| antony-tomb-combat | "Antony, I was here, but I waited to see your fight. You have endured and have not given way. So I will always help you, and I will make your name known everywhere." | "Antony, I was here, but I waited to see thy fight; wherefore since thou hast endured, and hast not been worsted, I will ever be a succour to thee, and will make thy name known everywhere." (npnf204:31516-31520) | PASS ("given way" for "worsted" is acceptable) |
| antony-withdrawal | (no quoted spans) | n/a | n/a |
| arsenius-flee | "Lord, show me how to live." | "O Lord, direct me how to live" (anan-isho_paradise-v2-sayings_budge1907.txt:54) | PASS |
| arsenius-flee | "Arsenius, flee from men, and you will live." | "Arsenius, flee from men, and thou shalt live." (:54) | PASS |
| arsenius-flee | "Arsenius, flee, keep silence, and live a life of silent contemplation. These are the root causes that keep a person from sinning." | "Arsenius, flee, keep silence, and lead a life of silent contemplation, for these are the fundamental causes which prevent a man from committing sin." (:56) | PASS |
| moses-leaking-jug | "Come. All the people are waiting for you." | "Come, for all the people are expecting thee" (:1160) | PASS |
| moses-leaking-jug | "What does this mean, father?" | "What meaneth this, O father?" (:1160) | PASS |
| moses-leaking-jug | "This sand is my sins, running down behind me, and I cannot see them. And today I myself have come to judge faults that are not mine." | "[The sands are] my sins which are running down behind me and I cannot see them, and I, even I, have come this day to judge shortcomings which are not mine." (:1160) | PASS |
| sarah-answer | "It is I who am a man, and you who are women." | "It is I who am a man, and ye who are women." (:2438) | PASS |
| sarapion-anthropomorphite | "Let us make man in our image and likeness." | "Let us make man after our image and likeness." (npnf211:36029-36030) | PASS |
| sarapion-anthropomorphite | "Alas, how wretched I am! They have taken my God away from me. Now I have no one to hold on to, and I do not know whom to worship or speak to." | "Alas! wretched man that I am! they have taken away my God from me, and I have now none to lay hold of; and whom to worship and address I know not." (npnf211:36051-36054) | PASS |
| virgin-who-hid-athanasius | "I have gained two things," / "my own life and hers." | "And I have gained two things, my own life and hers;" (palladius_paradise-v1-syriac_budge1907.txt:1119) | PASS |
| pachomius-founding | (no quoted spans) | n/a | n/a |
| kellia-day | (no telling field) | n/a | n/a |

The narrative words around each changed span still read correctly. That covers the
narrator lead-ins ("cried out with deep groans:", "he said:", "he said." before
"Keep my words") and the narration "Antony asked". No sentence in a changed span
runs past 25 words.

## Part 2: ordered record defects

| Defect | Verdict | Notes |
|---|---|---|
| Moses: stale "no vendored edition" note now cites Budge (divergence_note, locus, body) | PASS | sec. 542 at line 1160 is correct. Budge restarts its numbering, so the line pin is needed and is given. Hedges and Widely Accepted / Inferential-Thin kept. MINOR M2 (wording). |
| Moses modern_contrast: jug becomes basket of sand | PASS | Matches :1160. |
| Sarah: stale note now cites Budge | PASS | sec. 525 at line 2438 is correct. |
| Sarah: absent_detail, modern_contrast, body, retrieve_when, tellable_as and use_note.means drop visit and challenge, and say "a man ... women" | PASS on absent_detail, retrieve_when, tellable_as, use_note.means and divergence_note. **BLOCKING B1** in the body. **MINOR M3** in modern_contrast. | Spoken fields: tellable_as and means match Budge and are too short to be graded. |
| Arsenius: stale note now cites Budge; body no longer calls the voice God's | PASS | Book the First, Ch. I, secs 1-2 at lines 54 and 56 are correct. No remaining "God's voice" anywhere in the record. |
| antony-withdrawal: absent_detail, loci and not_for | PASS | SS13: "those of his acquaintances who came ... spend days and nights outside". SS49: "beset by many ... not suffered to withdraw ... fearing ... puffed up" (npnf204:31567, 32431-32435). SS8 and SS11 give only dispositions ("tightening his hold upon himself", "still more eagerly bent on the service of God"), not reasons for the move, so "a reason only for the last move" holds. |
| antony-tomb-combat: locus narrowed to SS8-10 | PASS | Body updated to match. No remaining fort or crowd reference. |
| antony-secret-burial: divergence_note, narrative_tier_justification, modern_contrast | PASS, with MINOR M4 and M5 | SS91-92 (npnf204:33508-33549) check out. Antony orders one sheepskin and the garment to "Athanasius the bishop". The Vita gives no source for the death. SS92 has "no one knows to this day ... save those two only" and the recipients guarding the items "as a precious treasure". Antony's own words give the house-custom as his reason ("to avoid this I entered into the mountain"). |
| kellia-day locus | PASS | sec. 527 at :2442 and sec. 637 at :2810 say what the locus says. The admission that neither attests constancy is accurate. See MINOR M6, which lies outside the ordered scope. |
| kellia-excavations divergence_note | PASS | It adds a limit, not a claim. Documented and verified-via-authority are kept. |

## Findings

**B1 (BLOCKING): sarah-answer body, final sentence.** The sentence reads "The participant-facing page
(cic-website/traditions/desert-monasticism.html) matches this record." It is now false. Line 277 of that
page still reads: "When a group of elder monks visited to test her standing as a woman, she told them
plainly that she was the man among them, and they were the women." That is the visit and challenge Mark
ordered out, and it is participant-facing. The record's claim also hides that from any later check.

The fix in records: delete the sentence. Do not replace it with a mismatch note, because a mismatch note in a canonical record
would be process commentary. Log the page gap in desert's Open_Gaps_Tracking.md. Fix the page itself
under the website's own change. Suggested replacement for its line 277 text: "Sarah was one of a small
number of women remembered by name in this world's own teaching tradition. She used to say to her
brothers that she was a man, and they were women." The sentence "Six of her sayings survive" can stay.
The vendored Budge names Mother Sarah at six places: lines 604, 620, 926, 1210, 1524 and 2438.

**M1 (MINOR): antony-tomb-combat telling.** The taunt stops at the colon, so the source's last clause is
dropped: "and a proof of your weakness is that you take the shapes of brute beasts". Under the
every-clause bar, consider adding it after "...frighten me with numbers.": "And taking the shapes of
beasts proves how weak you are."

**M2 (MINOR): moses divergence_note.** "so the check is verbatim for Budge only" could read as a claim
that the record quotes Budge word for word. The telling is a rendering. Replace it with "so the check
holds for Budge's wording only".

**M3 (MINOR): sarah modern_contrast.** "Sarah's own answer works by claiming..." still implies she was
responding to something. Replace "Sarah's own answer" with "Sarah's own saying".

**M4 (MINOR): antony-secret-burial narrative_tier_justification.** This field is new in this diff. It says
Athanasius "attended him for a long time". The vendored edition's own note (npnf204:~31200-31206) says the
reading is uncertain. Some manuscripts read "was able to learn from him who was his attendant". Replace
it with "...that he saw Antony many times and, in the reading this edition prints (some manuscripts
differ), attended him for a long time."

**M5 (MINOR): antony-secret-burial divergence_note.** "the Vita itself already states no one but the two
attendants ever knew the site" overstates SS92, which says "no one knows to this day". Replace "ever
knew the site" with "knew the site when it was written". The clause "- matching
desert.story.antony-call's own basis ..." now sits after the SS92 sentence and reads as if it qualifies
SS92. Move it to follow "composed within a few years of Antony's death".

**M6 (MINOR, out of scope, pre-existing): kellia-day `text`.** The locus is now honest, and it shows that "the
Psalms were recited constantly, or nearly so" has no specific passage behind it. The record's own
narrative_tier_justification says an element like that is removed, not kept with a caveat. Register this
in Open_Gaps_Tracking.md, or bring the text into line with secs 527 and 637. Suggested text: "the
Psalms were sung in the cell at set hours of the night, alongside manual work".

**Observed outside scope (not findings against this diff; for Open_Gaps):**
- desert.quote.sarah-man-among-you still has `retrieve_when: "participant asks whether a woman was ever
  tested or challenged, and how she answered"`. That is the same challenge residue.
- The same quote record gives its locus as line 2429. The saying is at line 2438.
- moses-leaking-jug `use_note.means` says "the elders released the brother". Budge has only "they", so
  "those gathered" would match the source.
