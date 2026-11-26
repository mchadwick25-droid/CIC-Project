# Entry texts: Alexandrian Christianity (`alexandria-catechetical`)

New `tile`, `intro`, `summary` and `recordHolds` for this tradition's `entry` in `cic-website/data/world-census.json` (Open-Gaps 416, "A built world's card texts were not graded"). Written from the finished brief (`alexandria-catechetical.brief.txt`), `Outline.md` and `Source_Sheet.md`, under Kit Part 1. Dates and scope follow the brief: "From about 180 to the middle of the next century" (the current texts say c. 150–400 CE). No quotation marks, so no quoted span needs an entry. The census is not edited.

Scorer (`python -m engine.m1.profile_readability`) and craft check (`python tools/check_brief_craft.py`), run on scratch copies outside the repository:

```
tile: 178 words, grade 9.4 (names out 8.1), reading ease names out 71.9, 19.8 words a sentence, longest sentence 27 words - pass; craft: 0 to look at
summary: 72 words, grade 8.6 (names out 7.5), reading ease names out 73.2, 18.0 words a sentence, longest sentence 23 words - pass; craft: 0 to look at
intro: 36 words, grade 9.8 (names out 8.6), reading ease names out 65.5, 18.0 words a sentence - pass
```

## tile

Old (171 words):
> In Alexandria, from about 150 to 400 CE, teachers led seekers through a shared reading of Scripture. They read for a deeper meaning beneath the surface, one that opened onto the Logos himself. This teaching reached the literate few. Ordinary believers met the same faith another way — through baptism, the shared meal, and the yearly round of fasts and feasts. Some call this one continuous school, led by one teacher after another. Others say it was simply a series of private teachers, grouped together only in hindsight. When plague struck the city, Bishop Dionysius of Alexandria wrote to his own church, praising his people for nursing the sick and burying the dead. Others, he wrote, fled the city instead. Persecution could reach the school's own teachers, not only the wider community. Origen himself was imprisoned and tortured under the emperor Decius, and he died a few years later. It had already touched his boyhood, too. His father was martyred in an earlier persecution, when Origen was still just a boy.

New (178 words):
> In Alexandria, in Egypt, from about 180 to the middle of the next century, Christians learned their faith from teachers, in what Eusebius of Caesarea calls a school. Teachers took pagans and catechumens, learners not yet baptized, through Scripture, read for a deeper sense beneath the plain story. Around 200, the threat of persecution drove every teacher of the faith out of the city. Pagans came instead to Origen, then in his eighteenth year, to hear the word of God, and some of his pupils were put to death. Clement taught that the Word, his name for Jesus, first urges people on, then trains them, and last of all teaches them. Origen wrote that Scripture has a body, a soul and a spirit, as a person does. Two of his pupils, Heraclas and then Dionysius, took over the instruction and became the city's bishops. Dionysius also sat for three days with the villages around Arsinoe. There he answered a bishop's book against reading Scripture for hidden meanings, and at the end the leader of its teaching said he was convinced.

Why: the old tile tells what the brief does not (the shared meal and the fasts, the modern debate as "some call / others say", the plague letter, Origen under Decius, his father's death), and its dates, 150 to 400, are not the brief's. Kit Part 1: a modern view stays out, and the short texts repeat no claim the brief does not make. The new tile follows the brief's heart in its order: the essence (brief, paragraph 2), the hook around 200 (paragraph 1), Clement's three steps (paragraph 3), Origen's three senses and Heraclas (paragraph 4), the pupils who became bishops (paragraph 5), and the three days to Coracion's word (paragraphs 6 to 8). "Dionysius also" keeps the visit undated, since no source puts it in his years as bishop (Outline, Do not say). Coracion is given by role, and Nepos as "a bishop", to keep the names to those that act in more than one sentence.

## intro

Old:
> Theon is a representative voice for the Christian tradition of Alexandria (c. 150–400 CE). Teachers drew on Greek and Jewish learning to read Scripture in layers and find Christ, the Logos, beneath the surface.

New:
> Theon is a representative voice for the Christian tradition of Alexandria (about 180 to the mid-200s). Its teachers took pagans and learners not yet baptized through Scripture, read for a deeper sense beneath the plain story.

Why: the name and frame are kept. The dates follow the brief ("From about 180 to the middle of the next century"). "Greek and Jewish learning" is not in the brief (Outline, Do not say, on philosophy and the city's learning; the old sources here never name Philo as the teachers' model, Source_Sheet, Set aside), and "the Logos" goes unexplained; the new second sentence is the brief's essence ("Teachers took pagans and catechumens through Scripture, read for a deeper sense beneath the plain story"), with "catechumens" given in the brief's own gloss.

## summary

Old:
> Between about 150 and 400 CE, Christians in Alexandria built a faith around teaching. Teachers led seekers through Scripture layer by layer. The plain story came first. Then came a deeper meaning that opened onto Christ. Clement and Origen were sure that Greek learning could serve Christ. When plague struck, the bishop wrote that his own people nursed the dying while others fled. Literate men wrote almost all of what survives.

New:
> From about 180 to the middle of the next century, Christians in Alexandria learned their faith from teachers, in what Eusebius calls a school. Teachers led pagans and learners not yet baptized through Scripture, reading for a deeper sense beneath the plain story. Clement taught that the Word first urges people on, then trains them, then teaches them. Some of Origen's pupils were put to death around 200; others later led the city's church.

Why: the dates follow the brief. The plague letter and "Clement and Origen were sure that Greek learning could serve Christ" are not in the brief, and the plague is another story's (Outline, Leave out). The old run of four short sentences becomes one, as Part 1 asks ("avoid runs of short sentences"). The new text holds the brief's essence, Clement's three steps (paragraph 3), the pupils put to death (paragraph 1) and the pupils who became bishops (paragraph 5). "Literate men wrote almost all of what survives" goes to `recordHolds`, in the brief's terms.

## recordHolds

Old:
> Rich in teaching and argument. Thin on ordinary believers and rural Egypt.

New:
> Mostly Eusebius, a century later, and the teachers' own words. Only Dionysius tells the three days.

Why: the brief says what the record is: "Nearly all we know of these classrooms comes from Eusebius of Caesarea, writing about a century later", with Clement's, Origen's and Dionysius's own words quoted, and of the three days, "In his own account, the only one left to us". "Thin on ... rural Egypt" no longer fits a brief whose closing scene is in the Egyptian countryside.
