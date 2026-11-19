# S1-05 retrieval bench: no-context BM25 on lpc's shelf

Index 82091a7f121b: 116116 passages in 112 files, context column empty. Lens: files on lpc's shelf. Ranking: SQLite FTS5 bm25 over passage text, query terms ORed after dropping English function words. No model call.

Ground truth: each record the coverage maps list for a sub-question (the `records` of the world's cell), and the vendored file and line ranges its `sources` cite (plus, for quote records, the passage holding the quote's first ten words). A case is one query against one such record; it is reached at k when a passage holding the record's cited text is among the top k. Ranks are searched to depth 100. Records with no resolvable citation in the index are left out and listed at the end.

Three queries are scored. `wording` is the visitor's question as written in the repository. `wording+label` adds the sub-question's label (a topic gloss the system holds). `record routing` is the record's own `retrieve_when` text, which is what a routing layer that already knows the record would send; it shows what the index can reach, not what raw visitor words reach.

Cases: 535 wording-by-record cases over 119 sub-question-by-record pairs and 47 records.

## Recall

| Level | Cases (wording) | wording @5 | @10 | @20 | wording+label @10 | @20 | record routing @10 | @20 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Every wording against every cited record | 535 | 1% | 1% | 2% | 2% | 4% | 31% | 39% |
| Best wording per sub-question and record | 119 | 3% | 5% | 8% | 7% | 8% | 31% | 39% |

## By category

| Cluster | Cases (wording) | wording @5 | @10 | @20 | wording+label @10 | @20 | record routing @10 | @20 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| C1 Jesus | 37 | 3% | 3% | 3% | 0% | 0% | 25% | 62% |
| C2 God, the Trinity, the Spirit | 26 | 0% | 0% | 0% | 0% | 0% | 43% | 43% |
| C4 Salvation, grace, works, and 'am I saved' | 45 | 0% | 0% | 0% | 0% | 0% | 33% | 50% |
| C5 The Bible: which books, how to read it, one verse at a time | 58 | 0% | 0% | 0% | 0% | 0% | 64% | 64% |
| C6 Authority: who was in charge, popes, councils, tradition | 94 | 2% | 2% | 2% | 3% | 6% | 35% | 47% |
| C7 Baptism, communion, prayer, worship, confession | 71 | 0% | 1% | 3% | 1% | 1% | 29% | 35% |
| C8 Women, children, the enslaved, marriage, sex | 23 | 0% | 0% | 0% | 9% | 35% | 0% | 0% |
| C9 Violence, empire, persecution, martyrs, power used badly | 24 | 4% | 12% | 12% | 21% | 21% | 0% | 0% |
| C10 Money, the poor, work | 15 | 0% | 0% | 7% | 7% | 13% | 20% | 20% |
| C11 Jews, pagans, Muslims, other religions | 6 | 0% | 0% | 0% | 0% | 0% | 0% | 0% |
| C14 Suffering, doubt, failure, hypocrisy, leaving | 118 | 0% | 0% | 1% | 0% | 0% | 28% | 36% |
| C15 'What would you say about today?' | 18 | 0% | 0% | 0% | 0% | 0% | 43% | 43% |

## By sub-question

| Sub-question | Cases (wording) | wording @5 | @10 | @20 | wording+label @10 | @20 | record routing @10 | @20 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| C1.S1 Who Jesus was to them; the good news; what he taught | 14 | 0% | 0% | 0% | 0% | 0% | 50% | 50% |
| C1.S2 Was he God; prophet, teacher or God as an outsider asks; vir | 5 | 20% | 20% | 20% | 0% | 0% | 0% | 0% |
| C1.S3 His death: why killed, what it did, 'in our place', 'persona | 4 | 0% | 0% | 0% | 0% | 0% | 0% | 100% |
| C1.S4 Resurrection: what happened, how they knew, 'grew in the tel | 3 | 0% | 0% | 0% | 0% | 0% | 0% | 100% |
| C1.S5 Did he exist; eyewitness chain; outside witnesses | 2 | 0% | 0% | 0% | 0% | 0% | 0% | 0% |
| C1.S8 Would Jesus want someone like me; I want to believe | 9 | 0% | 0% | 0% | 0% | 0% | 33% | 67% |
| C2.S2 What God is like: father or judge, angry, the same God as Je | 8 | 0% | 0% | 0% | 0% | 0% | 50% | 50% |
| C2.S3 The Trinity in plain words; the one-and-three objection | 4 | 0% | 0% | 0% | 0% | 0% | 0% | 0% |
| C2.S5 Councils, Arius, homoousios, filioque: 'a council voted Jesu | 8 | 0% | 0% | 0% | 0% | 0% | 50% | 50% |
| C2.S6 Can God be known, felt, experienced; God in nature; God heal | 5 | 0% | 0% | 0% | 0% | 0% | 100% | 100% |
| C2.S7 Where evil comes from; did God create it | 1 | 0% | 0% | 0% | 0% | 0% | 0% | 0% |
| C4.S1 Faith and works, grace, 'what must I do' | 30 | 0% | 0% | 0% | 0% | 0% | 33% | 33% |
| C4.S5 Baptism as new birth, is it needed, once-only repentance | 15 | 0% | 0% | 0% | 0% | 0% | 33% | 67% |
| C5.S1 Which books, the apocrypha, who decided, the Bible as only a | 7 | 0% | 0% | 0% | 0% | 0% | 100% | 100% |
| C5.S2 How they read: literal, more than one meaning, the Old Testa | 24 | 0% | 0% | 0% | 0% | 0% | 33% | 33% |
| C5.S3 Reliability, errors, authorship, 'science disproves it' | 5 | 0% | 0% | 0% | 0% | 0% | 100% | 100% |
| C5.S4 Genesis and creation, the six days | 2 | 0% | 0% | 0% | 0% | 0% | 100% | 100% |
| C5.S6 Who could read or own a Bible; language; translation | 4 | 0% | 0% | 0% | 0% | 0% | 100% | 100% |
| C5.S7 The violence in the texts; the cursing psalms | 2 | 0% | 0% | 0% | 0% | 0% | 0% | 0% |
| C5.S8 One passage at a time (VERSE) | 14 | 0% | 0% | 0% | 0% | 0% | 50% | 50% |
| C6.S1 Who led, how chosen, what the titles meant, bishops or not,  | 40 | 0% | 0% | 0% | 0% | 2% | 0% | 25% |
| C6.S2 The pope and Rome; Peter and 'on this rock' | 3 | 0% | 0% | 0% | 0% | 0% | 100% | 100% |
| C6.S3 Councils and creeds; who decided disputes; did ordinary beli | 4 | 0% | 0% | 0% | 0% | 0% | 100% | 100% |
| C6.S4 Tradition and scripture; apostolic succession; the only true | 20 | 5% | 5% | 5% | 10% | 20% | 50% | 50% |
| C6.S5 Heresy: who decided, what happened to heretics | 1 | 0% | 0% | 0% | 0% | 0% | 0% | 100% |
| C6.S7 The emperor's say in belief | 2 | 0% | 0% | 0% | 0% | 0% | 0% | 0% |
| C6.S8 Leaders who failed, got rich, or abused; distrust of leaders | 24 | 4% | 4% | 4% | 4% | 4% | 50% | 50% |
| C7.S1 Becoming one of them; baptism: infants, dunking or pouring | 6 | 0% | 0% | 0% | 0% | 0% | 0% | 0% |
| C7.S2 The meal: what happened, how often, real presence or symbol, | 14 | 0% | 0% | 7% | 0% | 0% | 0% | 0% |
| C7.S3 Prayer: why and how, set or free, teach me, prayer in anxiet | 20 | 0% | 0% | 0% | 0% | 0% | 50% | 50% |
| C7.S4 Worship in the room: singing and instruments, buildings, ima | 14 | 0% | 0% | 0% | 0% | 0% | 100% | 100% |
| C7.S5 Confession and penance; fasting | 6 | 0% | 0% | 0% | 0% | 0% | 33% | 67% |
| C7.S7 Mary and the saints in prayer; anointing the sick; weddings  | 8 | 0% | 0% | 0% | 0% | 0% | 0% | 0% |
| C7.S8 Did the practices go back to the apostles | 3 | 0% | 33% | 33% | 33% | 33% | 33% | 33% |
| C8.S4 Marriage: age, consent, mixed marriage, widows remarrying, d | 7 | 0% | 0% | 0% | 29% | 71% | 0% | 0% |
| C8.S5 Sex in marriage, virginity ranked above marriage, contracept | 12 | 0% | 0% | 0% | 0% | 25% | 0% | 0% |
| C8.S7 Children: raised, taught, treated | 4 | 0% | 0% | 0% | 0% | 0% | 0% | 0% |
| C9.S1 How dangerous it was; how many died; local or empire-wide; w | 7 | 0% | 0% | 0% | 0% | 0% | 0% | 0% |
| C9.S2 Seeking martyrdom; the lapsed who returned; informers; honou | 10 | 0% | 0% | 0% | 0% | 0% | 0% | 0% |
| C9.S3 Constantine and the empire; instrument or beast; taxes and o | 4 | 25% | 50% | 50% | 100% | 100% | 0% | 0% |
| C9.S4 Soldiers, war, judges, the death penalty, 'render unto Caesa | 3 | 0% | 33% | 33% | 33% | 33% | 0% | 0% |
| C10.S1 Was wealth a sin; the rich young man; the camel; prosperity  | 5 | 0% | 0% | 20% | 0% | 0% | 0% | 0% |
| C10.S2 Giving: tithe, alms, almsgiving and forgiveness | 4 | 0% | 0% | 0% | 25% | 50% | 0% | 0% |
| C10.S4 Care for the poor, widows, orphans, the sick, non-Christians | 6 | 0% | 0% | 0% | 0% | 0% | 50% | 50% |
| C11.S2 Pagans and their gods; eating and festivals with them; getti | 3 | 0% | 0% | 0% | 0% | 0% | 0% | 0% |
| C11.S3 Greek philosophy taken or refused; pagan authors quoted | 2 | 0% | 0% | 0% | 0% | 0% | 0% | 0% |
| C11.S7 Rivals: gnostics, Manichees, Marcion | 1 | 0% | 0% | 0% | 0% | 0% | 0% | 0% |
| C14.S1 Why God allows suffering; a sick child; healing refused; 'do | 18 | 0% | 0% | 0% | 0% | 0% | 33% | 33% |
| C14.S2 Unanswered prayer; God not listening; grief that does not li | 6 | 0% | 0% | 0% | 0% | 0% | 33% | 33% |
| C14.S3 Anger at God; lament out loud | 2 | 0% | 0% | 0% | 0% | 0% | 0% | 0% |
| C14.S4 Doubt and room for it; not believing the church; losing fait | 10 | 0% | 0% | 0% | 0% | 0% | 0% | 0% |
| C14.S5 Hypocrisy and a judgmental community; belonging; forgiving t | 24 | 0% | 0% | 4% | 0% | 0% | 50% | 50% |
| C14.S6 Leaders who did harm, cover-up, bullying bishops, accountabi | 20 | 0% | 0% | 0% | 0% | 0% | 25% | 25% |
| C14.S7 Leaving, drifting, moving away, shunned for questions; what  | 18 | 0% | 0% | 0% | 0% | 0% | 0% | 33% |
| C14.S8 Despair and depression in the world's words; a mind that wil | 20 | 0% | 0% | 0% | 0% | 0% | 25% | 50% |
| C15.S1 Gay marriage | 2 | 0% | 0% | 0% | 0% | 0% | 0% | 0% |
| C15.S2 Evolution, science, climate | 2 | 0% | 0% | 0% | 0% | 0% | 100% | 100% |
| C15.S4 Which church today; the Catholic church now; megachurches; t | 8 | 0% | 0% | 0% | 0% | 0% | 50% | 50% |
| C15.S5 Christians in politics; voting; 'religion causes wars' | 2 | 0% | 0% | 0% | 0% | 0% | 0% | 0% |
| C15.S7 Church life today: ageing churches, burnt-out pastors, the B | 4 | 0% | 0% | 0% | 0% | 0% | 100% | 100% |

## Misses: pairs no visitor wording reaches within 20

110 of 119 pairs. By reason: outranked 77, vocabulary mismatch 33. Best rank over the sub-question's wordings, under each query.

| Sub-question | Record | wording | wording+label | record routing | Reason | Detail |
|---|---|---:|---:|---:|---|---|
| C1.S1 | `lpc.quote.the-creed-first-then-the-prayer` | >100 | >100 | 4 | vocabulary mismatch | at most 1 query terms occur in the gold passages |
| C1.S1 | `lpc.quote.what-is-done-by-you-he-does-in-you` | >100 | >100 | >100 | vocabulary mismatch | at most 1 query terms occur in the gold passages |
| C1.S3 | `lpc.quote.two-hear-one-scorns-one-rises` | >100 | >100 | 17 | vocabulary mismatch | at most 1 query terms occur in the gold passages |
| C1.S4 | `lpc.quote.peter-the-sick-man-and-the-physician` | >100 | >100 | 11 | outranked | 2 query terms occur in the gold passages but other passages score higher |
| C1.S5 | `lpc.limit.no-chain-of-witnesses` | >100 | >100 | >100 | outranked | 2 query terms occur in the gold passages but other passages score higher |
| C1.S8 | `lpc.quote.bind-him-justly` | >100 | >100 | 1 | vocabulary mismatch | at most 1 query terms occur in the gold passages |
| C1.S8 | `lpc.quote.peter-the-sick-man-and-the-physician` | >100 | >100 | 11 | vocabulary mismatch | at most 1 query terms occur in the gold passages |
| C1.S8 | `lpc.witness.grant-me-chastity-but-not-yet` | >100 | >100 | >100 | vocabulary mismatch | at most 1 query terms occur in the gold passages |
| C10.S2 | `lpc.story.hundred-thousand-sesterces` | >100 | >100 | 48 | vocabulary mismatch | at most 1 query terms occur in the gold passages |
| C10.S2 | `lpc.witness.almsgiving-quenches-sin` | >100 | 10 | >100 | outranked | 2 query terms occur in the gold passages but other passages score higher |
| C10.S4 | `lpc.story.hundred-thousand-sesterces` | >100 | >100 | 48 | outranked | 2 query terms occur in the gold passages but other passages score higher |
| C10.S4 | `lpc.story.the-plague-and-the-enemies` | >100 | >100 | 5 | vocabulary mismatch | at most 1 query terms occur in the gold passages |
| C11.S2 | `lpc.story.the-death-of-cyprian` | >100 | >100 | >100 | outranked | 2 query terms occur in the gold passages but other passages score higher |
| C11.S3 | `lpc.force.congregational-acclamation-overriding-preference` | >100 | >100 | >100 | vocabulary mismatch | at most 0 query terms occur in the gold passages |
| C11.S7 | `lpc.witness.violence-commanded-not-cruel` | >100 | 27 | >100 | vocabulary mismatch | at most 1 query terms occur in the gold passages |
| C14.S1 | `lpc.story.the-plague-and-the-enemies` | 70 | >100 | 5 | outranked | 7 query terms occur in the gold passages but other passages score higher |
| C14.S1 | `lpc.witness.blamed-for-the-worlds-troubles` | >100 | >100 | >100 | outranked | 5 query terms occur in the gold passages but other passages score higher |
| C14.S1 | `lpc.witness.heard-for-salvation-not-for-wish` | 45 | 42 | >100 | outranked | 8 query terms occur in the gold passages but other passages score higher |
| C14.S2 | `lpc.quote.shepherd-wounded-in-the-flock` | >100 | >100 | >100 | outranked | 2 query terms occur in the gold passages but other passages score higher |
| C14.S2 | `lpc.witness.heard-for-salvation-not-for-wish` | >100 | >100 | >100 | outranked | 2 query terms occur in the gold passages but other passages score higher |
| C14.S2 | `lpc.witness.restless-heart-and-the-unrepentant-enemy` | >100 | >100 | 2 | outranked | 2 query terms occur in the gold passages but other passages score higher |
| C14.S3 | `lpc.witness.heard-for-salvation-not-for-wish` | >100 | >100 | >100 | outranked | 2 query terms occur in the gold passages but other passages score higher |
| C14.S4 | `lpc.limit.ordinary-interior-life` | >100 | >100 | >100 | outranked | 2 query terms occur in the gold passages but other passages score higher |
| C14.S4 | `lpc.witness.grant-me-chastity-but-not-yet` | >100 | >100 | >100 | outranked | 2 query terms occur in the gold passages but other passages score higher |
| C14.S5 | `lpc.quote.apart-in-heart-united-in-body` | >100 | >100 | 2 | outranked | 2 query terms occur in the gold passages but other passages score higher |
| C14.S5 | `lpc.quote.going-out-without-violating-unity` | >100 | >100 | 61 | vocabulary mismatch | at most 0 query terms occur in the gold passages |
| C14.S5 | `lpc.quote.pardon-through-a-wicked-clergyman` | >100 | 96 | 2 | outranked | 2 query terms occur in the gold passages but other passages score higher |
| C14.S5 | `lpc.quote.reprove-and-forgive-the-surgeons-knife` | 65 | 98 | >100 | outranked | 2 query terms occur in the gold passages but other passages score higher |
| C14.S5 | `lpc.witness.communion-over-separation` | 94 | >100 | >100 | outranked | 4 query terms occur in the gold passages but other passages score higher |
| C14.S6 | `lpc.quote.bind-him-justly` | >100 | >100 | 1 | outranked | 3 query terms occur in the gold passages but other passages score higher |
| C14.S6 | `lpc.quote.ye-belong-to-my-care` | >100 | >100 | >100 | outranked | 2 query terms occur in the gold passages but other passages score higher |
| C14.S6 | `lpc.witness.confessor-claim-vs-regulated-peace` | >100 | >100 | >100 | outranked | 5 query terms occur in the gold passages but other passages score higher |
| C14.S6 | `lpc.witness.violence-commanded-not-cruel` | >100 | >100 | >100 | outranked | 2 query terms occur in the gold passages but other passages score higher |
| C14.S7 | `lpc.quote.going-out-without-violating-unity` | >100 | >100 | 61 | vocabulary mismatch | at most 1 query terms occur in the gold passages |
| C14.S7 | `lpc.quote.peter-the-sick-man-and-the-physician` | >100 | >100 | 11 | outranked | 5 query terms occur in the gold passages but other passages score higher |
| C14.S7 | `lpc.story.celerinus-writes-to-lucian` | >100 | >100 | >100 | outranked | 5 query terms occur in the gold passages but other passages score higher |
| C14.S8 | `lpc.quote.peter-the-sick-man-and-the-physician` | >100 | >100 | 11 | outranked | 3 query terms occur in the gold passages but other passages score higher |
| C14.S8 | `lpc.quote.shepherd-wounded-in-the-flock` | >100 | >100 | >100 | outranked | 5 query terms occur in the gold passages but other passages score higher |
| C14.S8 | `lpc.witness.grant-me-chastity-but-not-yet` | >100 | >100 | >100 | outranked | 3 query terms occur in the gold passages but other passages score higher |
| C14.S8 | `lpc.witness.restless-heart-and-the-unrepentant-enemy` | >100 | >100 | 2 | vocabulary mismatch | at most 1 query terms occur in the gold passages |
| C15.S1 | `lpc.witness.grant-me-chastity-but-not-yet` | >100 | >100 | >100 | vocabulary mismatch | at most 0 query terms occur in the gold passages |
| C15.S1 | `lpc.witness.marriage-a-threefold-good` | 72 | 54 | >100 | vocabulary mismatch | at most 1 query terms occur in the gold passages |
| C15.S2 | `lpc.witness.days-before-the-sun` | >100 | >100 | 4 | vocabulary mismatch | at most 1 query terms occur in the gold passages |
| C15.S4 | `lpc.quote.one-good-shepherd-not-many` | >100 | >100 | 1 | vocabulary mismatch | at most 1 query terms occur in the gold passages |
| C15.S4 | `lpc.witness.communion-over-separation` | >100 | >100 | >100 | outranked | 5 query terms occur in the gold passages but other passages score higher |
| C15.S5 | `lpc.witness.constantine-did-not-corrupt` | 21 | 36 | 28 | outranked | 4 query terms occur in the gold passages but other passages score higher |
| C15.S7 | `lpc.quote.the-sermon-and-the-readings-are-daily-bread` | >100 | >100 | 1 | vocabulary mismatch | at most 1 query terms occur in the gold passages |
| C2.S2 | `lpc.witness.restless-heart-and-the-unrepentant-enemy` | >100 | >100 | 2 | outranked | 3 query terms occur in the gold passages but other passages score higher |
| C2.S2 | `lpc.witness.violence-commanded-not-cruel` | >100 | >100 | >100 | outranked | 3 query terms occur in the gold passages but other passages score higher |
| C2.S3 | `lpc.witness.the-only-son-and-the-trinity` | 74 | >100 | >100 | outranked | 3 query terms occur in the gold passages but other passages score higher |
| C2.S5 | `lpc.witness.scripture-above-councils` | 44 | 26 | 1 | outranked | 3 query terms occur in the gold passages but other passages score higher |
| C2.S5 | `lpc.witness.the-only-son-and-the-trinity` | >100 | >100 | >100 | outranked | 4 query terms occur in the gold passages but other passages score higher |
| C2.S6 | `lpc.witness.restless-heart-and-the-unrepentant-enemy` | >100 | >100 | 2 | outranked | 4 query terms occur in the gold passages but other passages score higher |
| C2.S7 | `lpc.witness.violence-commanded-not-cruel` | >100 | >100 | >100 | outranked | 3 query terms occur in the gold passages but other passages score higher |
| C4.S1 | `lpc.quote.good-works-the-comfort-of-our-dangers` | >100 | >100 | >100 | outranked | 4 query terms occur in the gold passages but other passages score higher |
| C4.S1 | `lpc.quote.no-one-has-the-love-of-god-from-himself` | >100 | >100 | 1 | outranked | 2 query terms occur in the gold passages but other passages score higher |
| C4.S1 | `lpc.quote.what-is-done-by-you-he-does-in-you` | >100 | >100 | >100 | outranked | 3 query terms occur in the gold passages but other passages score higher |
| C4.S5 | `lpc.quote.bind-him-justly` | >100 | >100 | 1 | outranked | 2 query terms occur in the gold passages but other passages score higher |
| C4.S5 | `lpc.quote.peter-the-sick-man-and-the-physician` | >100 | >100 | 11 | vocabulary mismatch | at most 1 query terms occur in the gold passages |
| C4.S5 | `lpc.quote.reprove-and-forgive-the-surgeons-knife` | >100 | >100 | >100 | outranked | 7 query terms occur in the gold passages but other passages score higher |
| C5.S1 | `lpc.witness.scripture-above-councils` | >100 | >100 | 1 | outranked | 2 query terms occur in the gold passages but other passages score higher |
| C5.S2 | `lpc.quote.the-sermon-and-the-readings-are-daily-bread` | >100 | >100 | 1 | outranked | 2 query terms occur in the gold passages but other passages score higher |
| C5.S2 | `lpc.witness.heard-for-salvation-not-for-wish` | >100 | >100 | >100 | outranked | 3 query terms occur in the gold passages but other passages score higher |
| C5.S2 | `lpc.witness.violence-commanded-not-cruel` | 73 | >100 | >100 | outranked | 4 query terms occur in the gold passages but other passages score higher |
| C5.S3 | `lpc.witness.days-before-the-sun` | >100 | >100 | 4 | outranked | 4 query terms occur in the gold passages but other passages score higher |
| C5.S4 | `lpc.witness.days-before-the-sun` | >100 | >100 | 4 | outranked | 2 query terms occur in the gold passages but other passages score higher |
| C5.S6 | `lpc.quote.the-sermon-and-the-readings-are-daily-bread` | 74 | >100 | 1 | outranked | 2 query terms occur in the gold passages but other passages score higher |
| C5.S6 | `lpc.story.the-psalms-on-the-wall` | >100 | >100 | 4 | vocabulary mismatch | at most 1 query terms occur in the gold passages |
| C5.S7 | `lpc.witness.violence-commanded-not-cruel` | >100 | >100 | >100 | outranked | 2 query terms occur in the gold passages but other passages score higher |
| C5.S8 | `lpc.witness.days-before-the-sun` | >100 | >100 | 4 | outranked | 4 query terms occur in the gold passages but other passages score higher |
| C5.S8 | `lpc.witness.violence-commanded-not-cruel` | >100 | >100 | >100 | outranked | 7 query terms occur in the gold passages but other passages score higher |
| C6.S1 | `lpc.quote.ancient-venom-against-my-episcopate` | >100 | >100 | >100 | outranked | 5 query terms occur in the gold passages but other passages score higher |
| C6.S1 | `lpc.quote.clamour-and-tears` | >100 | >100 | 12 | outranked | 8 query terms occur in the gold passages but other passages score higher |
| C6.S1 | `lpc.quote.ye-belong-to-my-care` | >100 | >100 | >100 | outranked | 5 query terms occur in the gold passages but other passages score higher |
| C6.S1 | `lpc.story.election-of-cyprian` | >100 | 15 | >100 | outranked | 5 query terms occur in the gold passages but other passages score higher |
| C6.S2 | `lpc.quote.bishop-of-bishops` | >100 | >100 | 8 | outranked | 3 query terms occur in the gold passages but other passages score higher |
| C6.S3 | `lpc.witness.scripture-above-councils` | >100 | 41 | 1 | outranked | 4 query terms occur in the gold passages but other passages score higher |
| C6.S4 | `lpc.quote.one-good-shepherd-not-many` | >100 | >100 | 1 | outranked | 2 query terms occur in the gold passages but other passages score higher |
| C6.S4 | `lpc.witness.communion-over-separation` | 38 | 64 | >100 | outranked | 5 query terms occur in the gold passages but other passages score higher |
| C6.S4 | `lpc.witness.tradition-tested-by-apostolic-warrant` | 28 | 8 | >100 | outranked | 9 query terms occur in the gold passages but other passages score higher |
| C6.S5 | `lpc.quote.the-branch-cut-from-the-vine` | >100 | >100 | 11 | vocabulary mismatch | at most 1 query terms occur in the gold passages |
| C6.S7 | `lpc.witness.blamed-for-the-worlds-troubles` | >100 | >100 | >100 | vocabulary mismatch | at most 1 query terms occur in the gold passages |
| C6.S7 | `lpc.witness.constantine-did-not-corrupt` | 42 | 27 | 28 | outranked | 2 query terms occur in the gold passages but other passages score higher |
| C6.S8 | `lpc.quote.ancient-venom-against-my-episcopate` | >100 | >100 | >100 | outranked | 7 query terms occur in the gold passages but other passages score higher |
| C6.S8 | `lpc.quote.shepherd-wounded-in-the-flock` | >100 | >100 | >100 | outranked | 4 query terms occur in the gold passages but other passages score higher |
| C6.S8 | `lpc.story.the-plague-and-the-enemies` | >100 | >100 | 5 | outranked | 8 query terms occur in the gold passages but other passages score higher |
| C7.S1 | `lpc.term.catechesis` | 89 | 34 | >100 | outranked | 4 query terms occur in the gold passages but other passages score higher |
| C7.S1 | `lpc.witness.baptism-traced-to-the-apostles` | >100 | >100 | >100 | vocabulary mismatch | at most 1 query terms occur in the gold passages |
| C7.S2 | `lpc.witness.communion-over-separation` | >100 | >100 | >100 | outranked | 3 query terms occur in the gold passages but other passages score higher |
| C7.S3 | `lpc.quote.longing-expectation-is-a-prayer-for-me` | >100 | >100 | >100 | vocabulary mismatch | at most 1 query terms occur in the gold passages |
| C7.S3 | `lpc.quote.the-creed-first-then-the-prayer` | >100 | 55 | 4 | outranked | 2 query terms occur in the gold passages but other passages score higher |
| C7.S3 | `lpc.story.the-psalms-on-the-wall` | >100 | >100 | 4 | outranked | 2 query terms occur in the gold passages but other passages score higher |
| C7.S3 | `lpc.witness.heard-for-salvation-not-for-wish` | >100 | >100 | >100 | outranked | 2 query terms occur in the gold passages but other passages score higher |
| C7.S4 | `lpc.limit.ordinary-interior-life` | >100 | >100 | >100 | vocabulary mismatch | at most 1 query terms occur in the gold passages |
| C7.S4 | `lpc.quote.the-sermon-and-the-readings-are-daily-bread` | >100 | >100 | 1 | outranked | 2 query terms occur in the gold passages but other passages score higher |
| C7.S5 | `lpc.quote.bind-him-justly` | >100 | >100 | 1 | vocabulary mismatch | at most 0 query terms occur in the gold passages |
| C7.S5 | `lpc.quote.peter-the-sick-man-and-the-physician` | >100 | >100 | 11 | vocabulary mismatch | at most 1 query terms occur in the gold passages |
| C7.S5 | `lpc.story.celerinus-writes-to-lucian` | >100 | >100 | >100 | outranked | 3 query terms occur in the gold passages but other passages score higher |
| C7.S7 | `lpc.story.the-death-of-cyprian` | >100 | >100 | >100 | vocabulary mismatch | at most 1 query terms occur in the gold passages |
| C7.S7 | `lpc.witness.marriage-a-threefold-good` | >100 | >100 | >100 | vocabulary mismatch | at most 0 query terms occur in the gold passages |
| C7.S8 | `lpc.witness.apostolic-succession-of-bishops` | >100 | >100 | 3 | outranked | 2 query terms occur in the gold passages but other passages score higher |
| C7.S8 | `lpc.witness.tradition-tested-by-apostolic-warrant` | >100 | >100 | >100 | vocabulary mismatch | at most 1 query terms occur in the gold passages |
| C8.S4 | `lpc.witness.marriage-a-threefold-good` | 41 | 7 | >100 | outranked | 6 query terms occur in the gold passages but other passages score higher |
| C8.S5 | `lpc.witness.grant-me-chastity-but-not-yet` | >100 | >100 | >100 | outranked | 3 query terms occur in the gold passages but other passages score higher |
| C8.S5 | `lpc.witness.marriage-a-threefold-good` | 40 | 15 | >100 | outranked | 4 query terms occur in the gold passages but other passages score higher |
| C8.S7 | `lpc.term.catechesis` | >100 | >100 | >100 | vocabulary mismatch | at most 1 query terms occur in the gold passages |
| C8.S7 | `lpc.witness.baptism-traced-to-the-apostles` | >100 | >100 | >100 | vocabulary mismatch | at most 1 query terms occur in the gold passages |
| C9.S1 | `lpc.story.numidicus` | >100 | >100 | >100 | outranked | 3 query terms occur in the gold passages but other passages score higher |
| C9.S2 | `lpc.story.celerinus-writes-to-lucian` | >100 | >100 | >100 | outranked | 3 query terms occur in the gold passages but other passages score higher |
| C9.S2 | `lpc.story.numidicus` | >100 | >100 | >100 | vocabulary mismatch | at most 1 query terms occur in the gold passages |

## Effect of an OCR floor of 0.5

The same queries, with passages whose `ocr_score` is under 0.5 left out of the ranking (a passage with no score stays in). The segmenter report recommends 0.50 for retrieval.

| Level | Cases | @5 no floor | @5 floor | @10 no floor | @10 floor | @20 no floor | @20 floor |
|---|---:|---:|---:|---:|---:|---:|---:|
| wording | 535 | 1% | 1% | 1% | 1% | 2% | 2% |
| wording+label | 535 | 1% | 1% | 2% | 2% | 4% | 4% |
| record routing | 115 | 30% | 30% | 31% | 31% | 39% | 39% |
| best wording per pair | 119 | 3% | 3% | 5% | 5% | 8% | 8% |

Gold passages in the index: 381; 12 of them score under 0.5. Pairs reached within 20 by some wording: 9 without the floor, 10 with it. Lost by the floor: 0. Gained by the floor: 1.

- gained: C15.S5 `lpc.witness.constantine-did-not-corrupt`

## Run record: real segmentation

Run 2026-10-29 (UTC 18:54 to 19:17). Segmenter output: 338 files, 354,589 passages, 80,950,920 words, manifest code hash `f1fad6fd501f` (the hash of the segmenter's last commit on main, so no rebuild was needed).

| Index | Files | Passages | Build time | Size on disk | Version hash |
|---|---:|---:|---:|---:|---|
| union (all 338 files, no context lines) | 338 | 354,589 | 98.4 s | 2,657,689,600 bytes (2.5 GiB) | `e23132c46679` |
| lpc (this bench) | 112 | 116,116 | 25.0 s | 849,215,488 bytes (810 MiB) | `82091a7f121b` |

The index holds each passage's text twice (the table and the full-text index), so it is about 3.4 times the 785 MB of segmenter output. At the time of the run `df` showed 9.9 GB available on the shared volume before the union build and 5.4 GB after it; the volume's free space then fell to about 150 MB while other work wrote to it, and the lpc build failed once with "database or disk is full" until the union index was deleted to make room. The union index fits the allowance only when nothing else is on the volume. It was deleted after its verify run, and rebuilds in about 100 s.

### Verify: byte-span check

The check as first merged required each passage's text to equal the whitespace-normalised bytes `byte_start:byte_end` of the vendored file. It failed 124,155 of 354,589 passages (35%), in 316 of 338 files. The cause was the check, not the segmenter. The segmenter's documented contract (Stage 2 report, section 9, Check C) is that a range runs from the passage's first word to its last word, that suppressed page furniture (running heads, bare page numbers) lies inside the range but not in the text, and that markup files have tags and entities removed, with notes held as a second text stream. Three causes, in the order they were met:

| Cause | Passages failing after the earlier causes were handled |
|---|---:|
| Page furniture inside the range (plain-text files) | 124,155 failed before; 10,146 after the first fix |
| Tags and entities removed (XML and tagged .txt) | 6,171 after treating tags as the segmenter does |
| Inline note bodies set in a separate stream, and block tags breaking words | 0 |

The fix is in `Sandbox/answering-library/index/retrieve.py` (`span_contains_passage`) with a test. A passage now verifies when its words are an in-order subsequence of the range's words, with the first and last word equal to the range's own, reading markup by the segmenter's own token and tag rules (imported from `answering_library.markup`). Result on the union index: 0 of 354,589 passages fail. Words in the range that a passage does not carry: 285,115 across 284,753 passages on the plain path, with 230,434 of those passages exact and 54,319 missing at least one word. The segmenter report counts 229,658 furniture words in plain files, so about 55,000 more words are dropped than it counts as furniture; most plausibly these are tags in tagged .txt files that the plain path counts as words, but that was not traced. The check cannot say a passage lost a real word in the middle of its range; a passage with a dropped middle word would pass. A stricter check would need the segmenter to record the dropped furniture words per passage.

## Comparison with the interim-chunk numbers

The interim chunking (earlier bench, same questions and records) gave 2% at 20 with the visitor's wording and 42% at 20 with the record's `retrieve_when` text. On the real segmentation the same two measures are 2% (wording, all wordings against all records) and 39% (record routing). The wording figure is unchanged; the routing figure is 3 points lower, from 115 routing cases (a case count that differs from the interim set only if the ground-truth set changed; it was not re-checked here). Best wording per pair reaches 8% at 20. Adding the sub-question label lifts wording to 4% at 20. By cluster, routing reaches 0% at 20 in C8, C9 and C11 while the label query is the better of the three in C8 (35%) and C9 (21%).

## What this means

What was measured: BM25 over the real passages, with no context column, reaches the cited evidence for 9 of 119 sub-question-by-record pairs (8%) from the visitor's own words at rank 20, and for 39% of cases when the query is the record's own `retrieve_when` text. Of the 110 pairs no wording reaches, 77 are outranked (the gold passages share at least two query terms with the question but other passages score higher) and 33 are vocabulary mismatch (at most one query term occurs in the gold passages). No miss was classed as OCR, foreign-language source or division too coarse. An OCR floor of 0.5 changed nothing in the aggregate figures and moved one pair into reach (C15.S5 `lpc.witness.constantine-did-not-corrupt`); it lost none, and 12 of 381 gold passages sit under it. Options for Mark, not recommendations: keep lexical search alone and rely on routing by record; add the context line the design describes (`S1-05_InSystem_Context_Design.md`) and re-run this bench; or add a different retrieval layer. This bench measures only whether the cited evidence is among the top 20 passages; it says nothing about answer quality.

## Records left out (no resolvable citation in the index)

85 cell-by-record entries, 43 records.

- C1.S1 `lpc.witness.the-pattern-we-are-modelled-on`
- C1.S3 `lpc.witness.the-pattern-we-are-modelled-on`
- C1.S4 `lpc.limit.no-chain-of-witnesses (with City of God XXII.5 argument)`
- C1.S7 `lpc.witness.scripture-above-councils (F2)`
- C11.S1 `lpc.source.cyprian-minor-pastoral-treatises`
- C11.S2 `lpc.limit.the-outsiders-own-view`
- C11.S6 `lpc.contested.compel-coercion-development`
- C11.S6 `lpc.demo.compel-three-phase`
- C11.S6 `lpc.gravity.preaching-and-catechesis`
- C11.S6 `lpc.term.compel-them-to-come-in`
- C11.S7 `lpc.force.manichaeism-and-pelagian-anthropology`
- C11.S7 `lpc.term.heresy`
- C11.S7 `lpc.term.schism`
- C11.S8 `lpc.limit.the-outsiders-own-view`
- C14.S1 `lpc.force.plague-of-cyprian`
- C14.S4 `lpc.limit.the-lapsed-own-account`
- C14.S6 `lpc.demo.compel-three-phase`
- C14.S6 `lpc.demo.road-back-examined`
- C14.S6 `lpc.gravity.penitential-discipline`
- C14.S6 `lpc.limit.the-lapsed-own-account`
- C14.S7 `lpc.demo.road-back-examined`
- C14.S7 `lpc.force.recurring-contest-failed-member`
- C14.S7 `lpc.limit.the-lapsed-own-account`
- C14.S7 `lpc.term.libellatici-sacrificati`
- C15.S4 `lpc.term.communion`
- C15.S4 `lpc.term.schism`
- C15.S5 `lpc.contested.compel-coercion-development`
- C15.S5 `lpc.demo.compel-three-phase`
- C15.S6 `lpc.limit.womens-own-voice`
- C15.S8 `lpc.limit.the-lapsed-own-account`
- C2.S5 `lpc.gravity.conciliar-authority-theory`
- C2.S5 `lpc.limit.411-gesta-unread`
- C2.S7 `lpc.force.manichaeism-and-pelagian-anthropology`
- C3.S6 `lpc.force.plague-of-cyprian`
- C3.S7 `lpc.force.donatist-schism`
- C3.S7 `lpc.limit.the-outsiders-own-view`
- C4.S1 `lpc.contested.grace-pelagius-characterization`
- C4.S1 `lpc.gravity.grace-and-human-incapacity`
- C4.S1 `lpc.term.grace [Documented]`
- C4.S2 `lpc.gravity.grace-and-human-incapacity`
- C4.S2 `lpc.witness.baptism-traced-to-the-apostles (infant baptism 'handed down from the apostles')`
- C4.S3 `lpc.quote.two-hear-one-scorns-one-rises ('No man cometh unto Me, except it were given')`
- C4.S3 `lpc.term.grace (retrieve_when: free will, predestination)`
- C4.S4 `lpc.term.the-lapsed (retrieve_when: apostasy, backsliding)`
- C4.S5 `lpc.demo.road-back-examined`
- C4.S5 `lpc.gravity.penitential-discipline`
- C4.S5 `lpc.limit.the-lapsed-own-account`
- C4.S5 `lpc.term.reconciliation-penitential-discipline`
- C4.S7 `lpc.witness.almsgiving-quenches-sin [Documented] (Cyprian, On Works and Alms)`
- C4.S8 `lpc.quote.pardon-through-a-wicked-clergyman (Sermon 71 on Matt 12:32, indexed only for the wicked-minister question)`
- C6.S1 `lpc.term.suffrage`
- C6.S1 `lpc.term.the-people`
- C6.S2 `lpc.term.bishop-of-bishops`
- C6.S2 `lpc.term.the-one-episcopate`
- C6.S3 `lpc.gravity.conciliar-authority-theory`
- C6.S3 `lpc.term.plenary-council`
- C6.S4 `lpc.limit.apostolic-origin-undefended`
- C6.S5 `lpc.demo.compel-three-phase`
- C6.S5 `lpc.term.compel-them-to-come-in`
- C6.S5 `lpc.term.heresy`
- C6.S5 `lpc.term.schism`
- C6.S7 `lpc.limit.the-outsiders-own-view`
- C6.S7 `lpc.term.compel-them-to-come-in`
- C7.S1 `lpc.limit.apostolic-origin-undefended`
- C7.S1 `lpc.term.heresy`
- C7.S2 `lpc.term.communion`
- C7.S4 `lpc.term.preaching`
- C7.S5 `lpc.demo.road-back-examined`
- C7.S5 `lpc.term.certificates-letters-of-peace`
- C7.S5 `lpc.term.reconciliation-penitential-discipline`
- C7.S7 `lpc.witness.the-pattern-we-are-modelled-on`
- C7.S8 `lpc.limit.apostolic-origin-undefended`
- C8.S1 `lpc.limit.womens-own-voice`
- C8.S2 `lpc.limit.womens-own-voice`
- C9.S1 `lpc.force.decian-persecution-libelli-system`
- C9.S1 `lpc.force.valerianic-persecution`
- C9.S1 `lpc.limit.the-outsiders-own-view`
- C9.S2 `lpc.limit.the-lapsed-own-account`
- C9.S2 `lpc.term.certificates-letters-of-peace`
- C9.S3 `lpc.limit.the-outsiders-own-view`
- C9.S5 `lpc.contested.compel-coercion-development`
- C9.S5 `lpc.demo.compel-three-phase`
- C9.S5 `lpc.term.compel-them-to-come-in`
- C9.S6 `lpc.contested.compel-coercion-development`
- C9.S6 `lpc.limit.the-lapsed-own-account`
