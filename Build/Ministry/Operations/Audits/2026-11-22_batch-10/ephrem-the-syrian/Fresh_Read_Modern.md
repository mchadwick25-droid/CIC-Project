# Ephrem the Syrian: fresh read, modern pass

Read: `ephrem-the-syrian.brief.txt` (final), against `Kit.md` as it now stands and `Outline.md`. Compared with `ephrem-the-syrian.brief.v4.txt`. No review, revision, check, reply or earlier fresh read opened. The folder holds no `Source_Sheet.md` or `Outline_Check.md`; claims were traced to `Outline.md` and re-read in the held texts.

## The four lines

- **Who:** Ephrem, a deacon of the Syriac church of Edessa, from Nisibis or its countryside, who wrote prose and hymns against rival teachers.
- **What happened:** he answered Mani, Marcion and Bardaisan, and when Harmonius's songs carried Greek ideas, he took the same meters and wrote hymns of the church's teaching; at the end he ran Edessa's famine relief for a year and died a month after.
- **What it was about:** teaching the church's faith in songs the people sang, against teachings already sung; and, at the end, care for the starving when the rich would not act.
- **Why the connection matters:** the Syrians sang his songs from then on, his works went into Greek and were read in churches after Scripture, and, in Barhadbeshabba's telling, his school at Edessa led to Narsai's at Nisibis and the schools that multiplied in Persia.

All four are clear after one hearing.

## Step 1: the test

- Named and explained: the famine relief (Palladius); the prose against rival teachers, through Mani's, Marcion's and Bardaisan's teachings; Bardaisan's denial that the body would rise, and Ephrem's answer; Harmonius's songs; Ephrem's hymns; the school at Edessa and Narsai's at Nisibis. Each says what it was.
- Essence (from the census and what he is known for): he taught the church's faith in hymns, sung in the meters of the songs he answered, and the Syrians sang his songs from then on. Also told: the refutations and what they answered, the spread of his works (Greek, Jerome, Theodoret), the school, the famine. The essence lands at word 110, inside the first minute; each part of what is also told is present with its weight.
- Order: after the essence the life runs once, prose, hymns, spread, school, and ends on his death, which the kit allows. The hook reaches ahead; nothing else goes back. No event is told twice.
- Ends on the person: yes, his death in his cell.
- Names: twelve. Each acts or credits a witness, or links (Basil). None loses the listener.
- Nowhere reads as a children's book.

## Step 3: the source check

Every sentence traced. The quote "See, on your behalf I appoint myself to take in and care for the needy." matches the `modern_rendering` in `records/syr/quote/syr.quote.palladius-hospitaller.md` word for word, and renders Clarke's "See, on your behalf I appoint myself hospitaller." (palladius_lausiac-history_clarke1918.txt 471).

Held by old sources, at their lines:
- Famine, left his cell, the rich, no one honest, "a man of God", a year of relief, death in his cell a month after: Palladius 471.
- Syriac-speaking, Osroene, Nisibis or its countryside: Sozomen III.16 (npnf202 32050-32051, 32076-32084); Edessa in Mesopotamia (Socrates, npnf202 5958); Nisibis handed to the Persians and Ephrem's move to Edessa (Scher 20436-20437).
- Deacon of Edessa: Palladius 471; Jerome 115 (npnf203 41540-41543).
- The prose against Mani, Marcion and Bardaisan as Ephrem's: the sixth-century manuscript's own titles, "Letters of the Blessed Ephraim ... against the False Teachings" and "A discourse made by the blessed Saint Ephraim" (Mitchell 111, 1352).
- Mani: two Roots, mixture, the body as Darkness's prison for the soul (Mitchell 415, 418, 431, 819). Marcion: the Stranger above the Maker, who came down, and souls ascending (Mitchell 592, 1003, 1549). Both credited to Ephrem.
- The hymn: "a book of Bardaisan ... How he blasphemes justice, And grace her fellow-worker. For if the body be not raised ..." (npnf213 11200-11214).
- Harmonius, the meters, "apprehensive, lest they should imbibe the same opinions", "From that period the Syrians sang the odes of Ephraim", Greek in his lifetime, Basil's admiration: Sozomen (npnf202 32060-32067, 32082-32100). Jerome on reading after the Scriptures: npnf203 41540-41543. Theodoret on the martyrs' festivals: npnf203 15063-15067.
- Barhadbeshabba, bishop, the book's title, the school and its growth, Narsai, the students of Edessa, the schools multiplying in Persia: Scher 17166-17169, 20434-20441, 20738-20741.

One sentence still rests on a modern reckoning (BLOCKING 1). No other sentence rests on a modern source or on a claim rated Dominant Modern Reconstruction or Inferential-Thin.

## Step 4: the score

`python -m engine.m1.profile_readability`: 393 words, grade 8.3 (names out 6.6), reading ease names out 79.5, 17.9 words a sentence, longest sentence 28 words, pass. Under the 450 ceiling. After BLOCKING 1: 396.

## Step 2: the diff against v4

Five sentences changed; each traces to the outline's Modern pass and to the old source it cites.

1. `Around 372, famine struck Edessa,` → `Famine struck Edessa,` (Modern pass 1). Sozomen has "shortly before his death" (npnf202 32138-32140); Palladius gives the year and the death a month after (471), which the last line tells. Nothing lost.
2. `A later prayer of Mani's own followers names the same two powers.` cut (Modern pass 2). Mani's teaching stays as Ephrem's account. Nothing the story needs is lost; the card carries the prayer.
3. `In his own homily, though, Ephrem blames Bardaisan himself.` cut (Modern pass 3). Confirmed: the held homily lines ("He fashioned hymns ...") do not name Bardaisan; "attributing the work ... to Bardesan solely" is Gwynn's (npnf213 11234-11246). Sozomen and Theodoret both give Harmonius. No conflict between old sources is dropped.
4. `Around 600, Barhadbeshabba, the historian of the school of Nisibis, wrote that` → `Barhadbeshabba, a later bishop, wrote a book on how the schools were founded. It tells how` (Modern pass 4). Held: "Cause de la fondation des écoles, composée par Mar Barhadbsabba 'Arbaya, évêque de Halwan" (Scher 17166-17169); later, since he tells of Narsai's forty-five years (Scher 20742).
5. `the schools that spread through the Church of the East under Persia began with Ephrem` → `the schools then multiplied in the Persian empire` (Modern pass 5). Held: "Les écoles se multiplièrent dans l'empire des Perses" (Scher 20740-20741).

Nothing added that the old sources do not hold. Nothing lost the story needs: the famine scene, the heart (hymns in Harmonius's meters), what each teaching was, and the line from Edessa's school to Nisibis and Persia all stand.

## Scores

- **Voice: 4.** A steady documentary narrator; witnesses credited in the sentence, the famine told in Palladius's own exchange.
- **Craft: 4.** Clear hook into the essence, one pass through the life, ends on his death. The hook runs five sentences, longer than the kit's "about three", but the essence still lands at word 110.
- **Rigor: 4.** Every claim traced to an old source but one date, below.
- **Accessibility: 4.** Grade 8.3, ease 79.5, plain words. One phrase may blur on hearing (MINOR 1).

## Verdict: REVISE

One BLOCKING finding, one exact change.

## Findings

**BLOCKING 1. "In the next century" rests on a modern reckoning.** No old source in the brief's sources puts Theodoret a century after Ephrem. Doing so needs a year for Ephrem's death and one for Theodoret's writing; the first is the same modern sum the Modern pass removed (Chronicle of Edessa year 684 to 373 by Assemani's reckoning, Cowper 34, 103), and the second rests on the editor's dating of the Persian kings (npnf203 notes at 18060, 18129). The old sources hold only that Theodoret wrote later: his History runs past the Persian kings Isdigirdes, Vararanes and Vararanes's son (npnf203 18060, 18129), and Gennadius says he wrote "books of Ecclesiastical History ... down to his own time" (npnf203 3621-3623). His own word "still" (npnf203 15065) carries the time gap.
Change: `In the next century, Theodoret of Cyrrhus says, his hymns still brightened the festivals of the martyrs.` → `A later historian of the church, Theodoret of Cyrrhus, says his hymns still brightened the festivals of the martyrs.`
Traced: "These songs are still used to enliven the festivals of our victorious martyrs" (npnf203 15065-15066); "his books of Ecclesiastical History, which he wrote ... down to his own time" (Gennadius, npnf203 3621-3623).
Do not say line for the outline: Do not say "In the next century" or any century for Theodoret. Say "a later historian of the church".

**MINOR 1. "the body's birth, death and rebirth" can be heard as the body's resurrection,** just after Ephrem defends the body's rising, so Harmonius may sound as though he taught what Ephrem defends. Sozomen lists "the soul, the generation and destruction of the body, and the regeneration" (npnf202 32091-32093), without tying "regeneration" to the body.
Change: `Greek ideas about the soul and the body's birth, death and rebirth` → `Greek ideas about the soul, the body's birth and death, and rebirth`
Traced: Sozomen, npnf202 32091-32093.

**MINOR 2 (no change).** The hook runs five sentences against the kit's "about three". It is the approved wording, it carries the famine exchange and the quote, and the essence lands inside the first minute, so it stands.
