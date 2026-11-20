# desert-monasticism: Review Round 1

Scores from `python -m engine.m1.profile_readability` on the `<key>.txt` files (grade, then reading ease, names out). No piece fails a hard limit.

| Piece | Verdict | Grade | Ease | Findings |
|---|---|---|---|---|
| story | REVISE | 8.4 | 68.8 | PRE-EXISTING: martyrdom-succession inference told as settled; MINOR: Scetis/Scete |
| legacy | REVISE | 7.2 | 72.4 | BLOCKING: "technique" and "systematized" lost; MINOR: "the desert monks had" widens the eight-kind scheme |
| docstory-desert.story.angel-hands-the-tablet | PASS | 6.3 | 82.8 | none |
| docstory-desert.story.antony-call | PASS | 7.8 | 77.6 | MINOR: a 36-word sentence made by a join |
| docstory-desert.story.antony-secret-burial | PASS | 6.5 | 83.6 | none |
| docstory-desert.story.antony-tomb-combat | PASS | 5.3 | 83.1 | none |
| docstory-desert.story.antony-withdrawal | PASS | 6.7 | 80.6 | none |
| docstory-desert.story.arsenius-flee | PASS | 3.3 | 93.1 | none; listener read: not flat, not a children's book |
| docstory-desert.story.moses-leaking-jug | PASS | 3.4 | 93.6 | none; listener read: not flat, not a children's book |
| docstory-desert.story.pachomius-founding | PASS | 8.4 | 75.2 | none |
| docstory-desert.story.sarah-answer | PASS | 6.5 | 75.7 | none |
| docstory-desert.story.sarapion-anthropomorphite | PASS | 6.5 | 81.3 | none |

With the proposed wording applied, legacy scores grade 7.8, ease 67.6, and story scores grade 8.5, ease 68.4.

## Quotes

Every quoted span is identical between original and rewrite (checked mechanically and by reading).

| Piece | Span | Record | Source file and line |
|---|---|---|---|
| arsenius-flee | "Lord, show me how to live." | none | `cic/texts/anan-isho_paradise-v2-sayings_budge1907.txt` 54 |
| arsenius-flee | "Arsenius, flee from men, and you will live." | none | same file, 54 |
| arsenius-flee | "Arsenius, flee. Keep silence. ..." | desert.quote.arsenius-flee-tace-quiesce | same file, 56 |
| moses-leaking-jug | "Come. All the people are waiting for you." | none | same file, 1160 |
| moses-leaking-jug | "What does this mean, father?" | none | same file, 1160 |
| moses-leaking-jug | "my sins, running down behind me. I cannot see them." | desert.quote.moses-sins-run-out | same file, 1160 |
| sarah-answer | "It is I who am a man, and you who are women." | desert.quote.sarah-man-among-you | same file, 2438 |
| angel-hands-the-tablet | "In the name of the holy Trinity. ..." | desert.quote.pachomian-rule-opening-superscription | `cic/texts/pachomius_rules-ethiopic_schodde1885.txt` 168 |
| angel-hands-the-tablet | "These prayers are few." | desert.quote.rule-for-the-weak | same file, 176 |
| antony-call | "If you want to be perfect, ..." | none | `cic/texts/npnf204_athanasius-select-works-letters.xml` 31244-31246 |
| antony-call | "Do not be anxious about tomorrow." | none | same file, 31264-31265 |
| antony-tomb-combat | "If you had any real power, ..." | desert.quote.antony-not-worsted | same file, 31499-31505 |
| antony-tomb-combat | "Where were you? ..." | none | same file, 31515-31517 |
| antony-tomb-combat | "Antony, I was here, ..." | none | same file, 31517-31519 |
| antony-secret-burial | "Bury my body and hide it underground yourselves," | none | same file, 33512 |
| antony-secret-burial | "Keep my words, so that no one may know the place but you alone." | none | same file, 33512-33513 (text continues after the endnote) |
| sarapion-anthropomorphite | "Let us make man after our image and likeness" | none | `cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml` 36030 |
| sarapion-anthropomorphite | "Alas! I am a wretched man! ..." | desert.quote.they-have-taken-away-my-god | same file, 36051-36054 |

No BLOCKING-QUOTE.

## Patterns

- The rewrites are light, as Mark's depth ruling asks: the voice changed ("Our sayings", "Athanasius tells us", "this world's own" are gone) and short sentences were joined. No first person, "this world" or build vocabulary remains outside quotes.
- The two low scores (arsenius-flee 3.3, moses-leaking-jug 3.4) come from the sayings' own short quoted clauses, which cannot change. The narrator's lines around them are adult. Lengthening them would pad pieces the record keeps thin.
- The one blocking fault came from the sentence-splitting fix in legacy: splitting is safe, but two qualifiers fell out in the rewording. A split that also rewords needs a word-level check against the original.
- Place spellings vary across pieces: Tabennesi (story), Tabennesis (angel-hands-the-tablet), Tabennisi (pachomius-founding); Scetis and Scete. Each follows its own original and source. Only the Scetis/Scete split inside story can confuse a listener; the rest is for `tools/check_tree_overlap.py` and the census to settle.
