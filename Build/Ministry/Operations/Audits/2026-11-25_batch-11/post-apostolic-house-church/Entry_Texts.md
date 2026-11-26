# Entry texts: The Post-Apostolic House Churches

New `tile`, `intro`, `summary` and `recordHolds` for `entry` of `post-apostolic-house-church` in `cic-website/data/world-census.json` (Open-Gaps 416, "A built world's card texts were not graded"; Open-Gaps 405 on the summary). The census is not edited here. Each new text is written from the finished brief (`post-apostolic-house-church.brief.txt`), `Outline.md` (the heart, Setting, Do not say) and `Source_Sheet.md`, and adds no claim the brief does not hold. Dates and scope follow the brief: "in the hundred years after the apostles", Antioch, the cities of Asia Minor and Rome, with no year numbers (Outline, Setting: "No year numbers"). The census's 70–200 is not in the brief, so it goes from these texts.

Scores (`python3 -m engine.m1.profile_readability`, `tools/check_brief_craft.py`), old against new:

| Field | Old | New |
|---|---|---|
| tile | 172 words, grade 8.2, ease 61.9, pass | 189 words, grade 7.9, ease 69.6, pass; craft 0 |
| intro | 28 words, grade 10.5, ease 47.1, FAIL | 34 words, grade 7.6, ease 64.1, pass; craft 0 |
| summary | 78 words, grade 6.4, ease 67.6, pass | 81 words, grade 7.8, ease 73.2, pass; craft 0 |
| recordHolds | 18 words, grade 4.3, ease 80.2, pass | 22 words, grade 6.9, ease 71.0, pass; craft 0 |

## tile

Old:
> In Antioch, Asia Minor, and Rome, between about 70 and 200 CE, house churches grew up on their own. No single power ruled over them — letters carried by couriers held the network together instead. Once the apostles died, how to lead a church was never settled. Some followed a single bishop with elders beside him, others a council of elders alone. In Corinth, some elders were removed from office — an account that survives only in Rome's own letter asking for them back. That letter used real command language — “submit,” “receive correction” — but Rome claimed no formal power to force it. Corinth's own side is not preserved. They marked the Lord's Supper in different ways, too. One early manual gives thanks over the cup before the bread. Neither blessing tells the story of the Last Supper. Following Jesus could mean real danger: in one province, a governor had members questioned under torture, and in another, a bishop was marched under armed guard toward Rome. But this danger came and went — never constant, never empire-wide.

New:
> Early in the second century, Pliny, a Roman governor, questioned people who said they had stopped being Christians. They told him they used to meet before dawn and sing a hymn to Christ as to a god. In the hundred years after the apostles, Christians in Antioch, in the cities of Asia Minor and in Rome met together. Their letters greet one another household by household. Newcomers learned the Two Ways, of life and of death, before baptism. Only the baptized shared the thanksgiving over bread and a cup on the Lord's day. Elders, bishops and deacons led them. When the church at Corinth removed some of its elders, the church of Rome wrote, at Corinth's request. Men who had served blamelessly, it said, could not justly be removed. Ignatius, bishop of Antioch, wrote as a prisoner that each church should act as one around its bishop. Near the end of the century, Rome's bishop tried to cut off the churches of Asia, which kept Easter on the Passover date. Irenaeus of Lyon reminded him that Rome's earlier elders had lived at peace with visitors who kept Asia's day.

Why: the old tile makes claims the brief no longer makes and the outline bars. Its "between about 70 and 200 CE" is not in the brief. "No single power ruled over them", "Corinth's own side is not preserved" and "Neither blessing tells the story of the Last Supper" are absence-only claims (Do not say: say what they had). "This danger came and went — never constant, never empire-wide" is a modern judgment (Do not say). "asking for them back" and the quoted "submit," "receive correction" are not in the brief or the outline's quotes. It also leans on dashes for drama (Kit Part 1, Craft). The new tile follows the brief in order: its opening scene (Pliny, the dawn hymn, "as to a god" in lower case, per Do not say), the essence word for word in its two sentences, the Two Ways and the baptized-only thanksgiving, Rome's letter and its argument, Ignatius's charge to the churches, and the Easter ending. It is 17 words over the old tile, the cost of carrying the brief's ending; nothing in it is told that the brief does not tell.

## intro

Old:
> Chloe is a representative voice for the Christian tradition of the household churches after the apostles (70–200 CE). These churches had no fixed hierarchy and no finished New Testament.

New:
> Chloe is a representative voice for the Christian tradition of the house churches in the hundred years after the apostles. They met in Antioch, Asia Minor and Rome. Letters and messengers held them together.

Why: the name and frame are kept. "(70–200 CE)" becomes the brief's "in the hundred years after the apostles". The second sentence was absence-only ("no fixed hierarchy", "no finished New Testament": Do not say) and is replaced by what the essence says held them: "Letters and messengers carried between their churches held them together", with the brief's places. "household churches" becomes "house churches", the story's spoken name ("The Post-Apostolic House Churches"); this, with the short sentences, brings the old text from a hard-limit fail (grade 10.5, ease 47.1) to a pass.

## summary

Old:
> From about 70 to 200 CE, Christians in Antioch, the cities of Asia Minor and Rome gathered in households. No central body ruled them. Letters carried by hand held them together. After the apostles died, these churches had not yet settled who should lead. Ignatius's letters urged one bishop with elders beside him. At Rome, early letters show a council of elders leading. Being a Christian could bring real danger. Ignatius's letters say he was marched under guard toward death.

New:
> In the hundred years after the apostles, Christians in Antioch, in the cities of Asia Minor and in Rome met together. They taught newcomers a way of life before baptism, and gave thanks over bread and a cup on the Lord's day. Elders, bishops and deacons led them. Letters and messengers held their churches together. Rome wrote to Corinth when the church there removed some of its elders, and Ignatius of Antioch wrote to the churches of Asia as a prisoner.

Why: the new summary is the brief's essence, with its two best-known letters as the example of what held the churches together. The old one made claims the brief does not: the 70–200 dates; "gathered in households" (Do not say: "they all met in houses" → "met together"; do not say where they met); "No central body ruled them" (absence-only, Do not say); "had not yet settled who should lead" and "At Rome, early letters show a council of elders leading" (the outline tells each witness's own naming of the leaders and does not settle the order, Source_Sheet §5, "Who led"); and "toward death" (Ignatius's death is not told, Do not say). It also ran as a string of short one-act sentences (Kit Part 1, Craft). The Rome and Ignatius clauses come from the brief: "At Corinth's request, the church of Rome wrote" and "Ignatius, bishop of Antioch, was brought from Syria as a prisoner… On the road he wrote to the churches of Asia".

## recordHolds

Old:
> Rich in letters, church order and worship. Thin on enslaved members and the people who could not write.

New:
> Their own letters, a short manual and Justin's account of their Sunday. Beside them stands the letter of a hostile Roman governor.

Why: the old second sentence only says what is missing (Kit Part 1, Craft: "No sentence that only says what is missing"); the brief makes no claim about enslaved members or the unlettered in the record. The new text names what the record holds, as the brief and the outline's Who tells it give it: the churches' own letters (Rome's, Ignatius's), "a short manual, whose writer, date and place no one knows", Justin's Sunday, and "Pliny, a hostile witness". Dionysius's and Irenaeus's words, kept by Eusebius, are not named, to stay near the old length.
