# Witness Openings Review — lpc doctrinal_witness rewrites

- **Date:** 2026-10-24
- **Reviewer:** independent adversarial reviewer, running as Claude Opus 5.5 (`claude-opus-5-5`)
- **Scope:** the 14 uncommitted records in `records/lpc/doctrinal_witness/` (`git diff -- records/lpc/doctrinal_witness/`). Every changed `text` and `positions[n]` field (22 fields) was compared with its HEAD version and with the vendored source at each record's `sources[].locus`. The record files were not modified. `Build/worlds/lpc/lpc_Claims_Register.md` is also modified in the working tree; it is outside this review's scope.
- **Stated intent of the change:** remove openings that restate the participant's question, and bring flagged fields to FK ≤ 10 and FRE ≥ 60. Nothing else was meant to change.

## Method

1. **Quotations.** I extracted every double-quoted string from each changed field and searched for it in the record's cited `cic/texts/` file, with tags stripped, whitespace normalised and trailing punctuation ignored. **All 25 quoted strings match verbatim.** I also read each cited locus by its line numbers to check the paraphrased claims around the quotes.
2. **Meaning.** I compared each field's old and new versions sentence by sentence. Where a claim was already in the old text, it is marked *pre-existing*. It is still reported when it fails source fidelity, because each record must pass on its own merits.
3. **Readability.** `python -m engine.m10.cli regate lpc` gives **PASS**: 22 edited fields, none regressed, 9 below FK 8 (reported, not failed). Per-field scores from `engine.m1.fk` are below. Every edited field is now at FK ≤ 9.3 and FRE ≥ 60.2. Old-to-new improvements on fields that had failed: apostolic-succession `text` 11.1/51.0 → 8.0/60.8; apostolic-succession `positions[0]` 10.3/55.4 → 9.0/61.3; baptism `text` 9.3/58.3 → 7.2/65.0; baptism `positions[0]` 11.4/41.5 → 6.4/64.6; constantine `text` 11.7/54.9 → 9.0/63.4; marriage `positions[0]` 10.2/50.5 → 7.0/60.2; violence `text` 10.3/62.0 → 7.2/70.0; tradition `text` 8.7/59.7 → 8.2/60.9.

## Verification of the specific watch items in the brief

- **Constantine absence claim.** The old text said Augustine "does not answer that question directly anywhere in our own record". The new text says "Nowhere in our own record does Augustine answer directly". Both have the same scope, and the claim is not stronger. City of God V.25 (npnf102 lines 11099–11122) is about earthly prosperity, not corruption of the church, so the absence is honestly stated. No finding.
- **Violence: "once troubled him, before he held our own faith".** This attribution is **not new**; the HEAD text says the same. It is **verified**. Confessions III.vii.12 (npnf101 lines 5893–5895) gives the Manichaean questions, "Are they to be esteemed righteous who had many wives at once and did kill men, and sacrificed living creatures?", and then "At which things I, in my ignorance, was much disturbed". The surrounding passage sits within his Manichaean period. Reply to Faustus XXII.73–74 (npnf104 lines 8125–8129) supplies "showed not ferocity but obedience", "acted not in cruelty, but in righteous retribution, giving to all what they deserved" and the Abraham "unnatural" / "praiseworthy compliance" contrast. XXII.76 supplies "not a bodily action, but an inward disposition" and the martyrs-versus-sword ordering. A separate problem was introduced in the same record's closing lines; see below.
- **Lost hedges.** One real case: scripture-above-councils moves its qualification from "only authority" onto "above our own bishops", which the source does not qualify (P1 below). One minor case: days-before-the-sun drops the attribution on "we must believe it" (P2).
- **"We" voice taking over one author's claim.** violence-commanded-not-cruel now states flatly that "we found this untroubling" (P1 below).

## Findings by record

### lpc.witness.almsgiving-quenches-sin

| Field | Problem | Sev | Proposed text |
|---|---|---|---|
| text | "We had rich members." is accurate (On Works and Alms §§14–15 addresses "a wealthy and rich matron in Christ's Church"), but "members" is a modern institutional word in the world's own voice. | P2 | "Some among us were rich." |
| text | Pre-existing, not changed by this edit: the `tensions` field of this wealth record disclaims a full account of *marriage*. This is out of scope here and noted for the owner. | P2 | none (flag only) |

Meaning, quotes and readability are otherwise fine (FK 7.0, FRE 65.6).

### lpc.witness.apostolic-succession-of-bishops

| Field | Problem | Sev | Proposed text |
|---|---|---|---|
| text | **Unsupported claim, pre-existing but in a changed field:** "Linus, the successor named by Peter himself". Letter LIII §2 (npnf101 lines 29696–29712) says only "The successor of Peter was Linus". Nothing says Peter named him. This is an invented detail. | **P1** | "He reached Linus, Peter's own successor -- "In this order of succession no Donatist bishop is found."" |
| text | The opener still echoes the question's frame ("itself, not just this or that practice"). | P2 | "Our bishops' office was traced back to the apostles by name. It was done in two ways, by two different hands." |
| text, positions[0] | "he named a second chair the same way. These were Peter's own seat at Rome and James's at Jerusalem": "a second chair" followed by "These were" two seats does not add up. Answer to Petilian II.51 (npnf104 line 16912) names both chairs. | P2 | "Against a different Donatist opponent, Petilian, he named two chairs the same way: Peter's own seat at Rome and James's at Jerusalem." (In text, keep "each still filled, "to-day," by a living bishop." as its own sentence.) |
| positions[0] | One sentence runs to 41 words ("He reckoned from Peter ... the bishop then sitting."). The standard is about 25. | P2 | "He reckoned from Peter, to whom the Lord said "upon this rock will I build my Church." Then he listed every bishop of Rome by name, from Linus and Clement on through the centuries. He ended with Anastasius, the bishop then sitting." |

### lpc.witness.baptism-traced-to-the-apostles

| Field | Problem | Sev | Proposed text |
|---|---|---|---|
| text | "Augustine did it, in his own hands." is awkward and adds a passive opener with no gain. | P2 | Replace the first two sentences with: "Augustine traced two of our practices back to the apostles by name, not just by general conviction." |
| positions[0] | "He says so by name, not only from a general belief." reads as if he named something without saying what. | P2 | "Augustine names two of our practices as coming from the apostles, by name, not only from a general belief." (Keep the rest.) |

Quotes verified against On Baptism II.7.10 (npnf104 line 12163ff) and IV.24.32 (line 12631ff). No change of meaning.

### lpc.witness.blamed-for-the-worlds-troubles

| Field | Problem | Sev | Proposed text |
|---|---|---|---|
| text | Hollow meta-opener: "We can tell you one real charge our neighbours made". This is one of the AI tells the brief names. | **P1** | "One charge our neighbours made comes down to us, because Cyprian wrote a whole reply to it." |
| text | "We still cannot tell you ... We cannot tell you ..." repeats the same frame. These are honest-limit statements, so the substance stays, but the cadence repeats. | P2 | "We still cannot say, in a stranger's own voice, what he found strangest about us. Nor can we say whether Constantine corrupted what we were, or whether we were really hiding in catacombs." |

The Demetrianus locus (anf05 lines 45605–45660) supports the charge: wars, famine and pestilence imputed to Christians for not worshipping the gods. No change of meaning.

### lpc.witness.constantine-did-not-corrupt

| Field | Problem | Sev | Proposed text |
|---|---|---|---|
| text | The 28-word list sentence ("Constantine reigned long ... to succeed him."). It is pre-existing. | P2 | "Constantine reigned long and held the empire alone. He founded a city with no temple to the old gods. He died of old age, with his sons to succeed him." |

The absence claim keeps its old scope, as verified above. The source supports the V.25 paraphrase. No blocking finding.

### lpc.witness.days-before-the-sun

| Field | Problem | Sev | Proposed text |
|---|---|---|---|
| positions[0] | Hollow meta-opener: "We have a real answer on whether we read Genesis ..." | **P1** | Replace the first two sentences with: "Augustine took up how to read the days of Genesis directly, in City of God." |
| text | The same meta-opener: "We have a real answer on whether ..." | **P1** | Replace the first two sentences with: "Augustine took up how to read the days of Genesis directly, in City of God." |
| text | "We must believe it without fully understanding it." now stands as its own sentence, so it loses its attribution to Augustine. "fully" also softens the source. XI.7 (npnf102 lines 20403–20406) says "neither can we understand how it was, and yet must unhesitatingly believe it". | P2 | "We cannot understand how it was, he wrote, and yet we must believe it." |

"highly mendacious" and "not 6000 years" were verified at npnf102 lines 22596–22598.

### lpc.witness.heard-for-salvation-not-for-wish

| Field | Problem | Sev | Proposed text |
|---|---|---|---|
| text | Hollow meta-opener: "We have something real to give you on prayer that goes unanswered." | **P1** | Replace the first two sentences with: "Augustine taught directly on prayer that goes unanswered, from the apostle Paul's own words." |
| text | A 33-word sentence (Paul's thorn). | P2 | "Paul asked God three times to take away a thorn in his flesh. He named it a messenger of Satan sent to buffet him. God did not take it away." |

Quote verified (Homily VI §6, npnf107 line 15210ff). No change of meaning.

### lpc.witness.marriage-a-threefold-good

| Field | Problem | Sev | Proposed text |
|---|---|---|---|
| text | "We had a teaching on marriage, not only weddings to attend." still echoes the participant's question frame. | P2 | Delete the sentence and open with "Augustine wrote a whole treatise defending marriage as a real good, ..." |
| text | A 28-word sentence (the sacrament clause). | P2 | "A marriage compact, he wrote, is entered into as a matter of a certain sacrament. It is not made void even by separation." |

The Good of Marriage §7 (npnf103 lines 32710–32716) supports the paraphrase. No change of meaning.

### lpc.witness.restless-heart-and-the-unrepentant-enemy

| Field | Problem | Sev | Proposed text |
|---|---|---|---|
| positions[0], text | "Augustine opened his own life's story with a mind that cannot quiet itself." This is awkward and swaps the world's own image (the restless heart) for the participant's phrasing. | P2 | "Augustine opened the story of his own life with a restless heart." |
| positions[0] | A 31-word sentence ("He did not treat the restlessness ..."). | P2 | "He did not treat the restlessness as a flaw to manage. He treated it as the shape of what a person is, until it finds what it was made for." |
| text | "He wrote on forgiving someone who is not sorry too." has a dangling "too" and a stiff cadence. | P2 | "He also wrote on forgiving someone who is not sorry." |

Quote verified (Confessions I.i.1). Enchiridion 73 (npnf103 lines 22392–22412) supports the two-standard structure. No change of meaning.

### lpc.witness.scripture-above-councils

| Field | Problem | Sev | Proposed text |
|---|---|---|---|
| text | **Hedge moved onto the wrong claim.** The old opener qualified "only authority". The new one, "We held scripture above our own bishops only in a specific sense, and not without real qualification", qualifies *scripture above bishops*. The source states that without qualification: the canon "stands so absolutely in a superior position to all later letters of the bishops" (On Baptism II.3.4, npnf104 lines 11301–11303). The record's own note puts the qualification on "only authority". As written, the opener narrows a documented claim and contradicts the record's next sentence. | **P1** | "Scripture stood above our bishops' own writings, but it was not our only authority." |

### lpc.witness.the-only-son-and-the-trinity

| Field | Problem | Sev | Proposed text |
|---|---|---|---|
| text | "saying Jesus is God and holding to the Trinity are really one question" is a category slip (saying and holding are not questions) and still echoes the question. | P2 | "For us, Jesus being God and the Trinity are not two questions but one." |

Enchiridion 56 (npnf103 line 21856) supports "the only Son of God, our Lord ... thus completing the Trinity which constitutes the Godhead". Possidius 17 supports the Maximinus conference. No change of meaning.

### lpc.witness.the-pattern-we-are-modelled-on

| Field | Problem | Sev | Proposed text |
|---|---|---|---|
| text | Number disagreement in the new opener: "His death and his resurrection are not a fact". | P2 | "His death and rising are not facts we simply affirm and set aside." |
| text | Two 39-word sentences. They are pre-existing. | P2 | "His crucifixion, burial, rising on the third day, ascension, and sitting at the Father's right hand were ordered deliberately. The life we lead here was modelled on them, not only mystically, but in reality." and "We set our affection on what is above, our life hidden with him in God. That is his ascension and his sitting at God's right hand, worked out in an ordinary life." |

Enchiridion 53 (npnf103 line 21778ff) supports the paraphrase. No change of meaning.

### lpc.witness.tradition-tested-by-apostolic-warrant

| Field | Problem | Sev | Proposed text |
|---|---|---|---|
| text | **Spoken garden-path introduced by the rewrite:** "They are not rebaptizing, and baptizing infants." Heard aloud, "They are not rebaptizing" sounds like a denial. Note that "we did not rebaptize" would be false for Cyprian's own Africa, so the fix must not put the practice in the "we" voice. | **P1** | "The two practices are baptizing infants, and refusing to baptize again someone already baptized among heretics." |

No other change of meaning. FK 8.2, FRE 60.9.

### lpc.witness.violence-commanded-not-cruel

| Field | Problem | Sev | Proposed text |
|---|---|---|---|
| text | **Claim sharpened and moved into the collective voice.** The old sentence was garbled but negated the reading: "What a modern reader may miss is not that we found this untroubling because we thought little of it." The new one asserts it: "A modern reader may miss why we found this untroubling." That has the whole "we" find the violence untroubling, which (a) contradicts the record's own opening ("much disturbed") and (b) goes beyond the source. Faustus XXII.74 says only that, once explained, the wars of Moses "will not excite surprise or abhorrence", and that is one author's argument. The `tensions` field frames the point as "not an absence of moral seriousness". | **P1** | "A modern reader may miss something here. Our bishop did not answer this way because he thought little of it." (Then continue: "We held that the earthly wars ...") |
| text, positions[0] | "the violence in (some of) these texts" has no antecedent now that the question is gone. This is pre-existing. | P2 | "the violence in some of our older Scriptures" |
| text, positions[0] | A 35-word sentence ("As a young man ... called righteous."). | P2 | "As a young man drawn to a rival teaching, he was, in his own words, "much disturbed" by one question. Could men who had many wives, and did kill men, really be called righteous?" |

## Counts

- Records reviewed: 14. Changed fields reviewed: 22. Quoted strings checked: 25, all verbatim.
- Readability: regate PASS. All 22 edited fields are at FK ≤ 10 and FRE ≥ 60.
- **P0: 0**
- **P1: 8**
  - apostolic-succession `text`: "named by Peter himself" (pre-existing)
  - blamed `text`: meta-opener
  - days-before-the-sun `positions[0]` and `text`: meta-opener (2)
  - heard-for-salvation `text`: meta-opener
  - scripture-above-councils `text`: hedge moved onto the wrong claim
  - tradition-tested `text`: garden-path
  - violence `text`: "we found this untroubling"
- **P2: 21**
- Records with no blocking finding: almsgiving, baptism, constantine, marriage, restless-heart, only-son, pattern.

This is a first-round review. Per the review cap, round 2 should be a targeted recheck of the 8 P1 fields only.

VERDICT: Substantial revision required
