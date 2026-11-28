"""Build the set of 15 new era 1 person briefs, and the packets the readers read.

The method is ../2026-11-25_person-council-grades/build_set.py, with the set taken from the
final brief texts on their branches instead of the census. Run from the repository root after
fetching the branches:
python Build/Ministry/Operations/Audits/2026-11-28_era1-new-grades/build_set.py
Reads only; writes Set.json, Cards.json and packets/ in this folder.
"""
import json
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..', '..'))
BATCH = 'Build/Ministry/Operations/Audits/2026-11-26_batch-12'
PETER = 'origin/claude/cft-story-peter-of-alexandria'
REST = 'origin/claude/cft-release-batch12-13'
MAIN = 'origin/main'
THIRTEEN = ['ignatius-of-antioch', 'clement-of-alexandria', 'valentinus', 'pontius-the-deacon',
            'methodius-of-olympus', 'pamphilus-of-caesarea', 'tacitus', 'origen', 'suetonius',
            'anatolius-of-alexandria-and-laodicea', 'hippolytus-of-rome', 'lactantius', 'tatian']
TOUR = {'josephus'}
FLOOR = {'person': 300}
CARD_FIELDS = ['role', 'knownFor', 'shortDescription', 'datesNote', 'placeNote', 'keyWorks']


def show(ref, path):
    return subprocess.run(['git', 'show', f'{ref}:{path}'], cwd=ROOT, capture_output=True,
                          text=True, check=True).stdout


def main():
    census = {m['id']: m for m in json.loads(show(MAIN, 'cic-website/data/world-census.json'))['movements']}
    texts, cards, where = {}, {}, {}
    j = census['josephus']
    texts['josephus'] = j['longDescription']
    cards['josephus'] = j.get('card') or {}
    where['josephus'] = 'main: census longDescription'
    for slug, ref in [('peter-of-alexandria', PETER)] + [(s, REST) for s in THIRTEEN]:
        texts[slug] = show(ref, f'{BATCH}/{slug}/{slug}.brief.txt')
        cards[slug] = json.loads(show(ref, f'{BATCH}/{slug}/{slug}.card.json'))
        where[slug] = f'{ref[7:]}: {BATCH}/{slug}/{slug}.brief.txt'
    rows = []
    for slug in sorted(texts, key=lambda s: (census.get(s, {}).get('activeYear') or 0, s)):
        m = census.get(slug, {})
        home = census.get(m.get('toldWithin') or '', {})
        rows.append({
            'id': slug, 'name': m.get('name', slug), 'kind': 'person', 'era': m.get('era'),
            'batch': '12', 'reference': False, 'words': len(texts[slug].split()), 'floor': FLOOR['person'],
            'scan': 'this audit', 'text_from': where[slug],
            'tour': slug in TOUR, 'major': bool(m.get('major')),
            'home': m.get('toldWithin') or '',
            'home_built': home.get('status') == 'Built & Live',
            'home_living': bool(home.get('living')),
        })
    json.dump(rows, open(os.path.join(HERE, 'Set.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    json.dump({s: {k: c.get(k) for k in CARD_FIELDS if c.get(k)} for s, c in cards.items()},
              open(os.path.join(HERE, 'Cards.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    json.dump(texts, open(os.path.join(HERE, 'Texts.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)

    def write(name, prefix):
        with open(os.path.join(HERE, 'packets', name + '.md'), 'w', encoding='utf-8') as f:
            f.write(f'# Packet {name}: new era 1 person briefs (final text)\n')
            for r in rows:
                f.write(f"\n## {prefix}{r['id']}\n\n{r['name']}\n\n{texts[r['id']].strip()}\n")

    write('L01', '')
    write('S01', 'tree/')
    print(len(rows), 'stories;', 'words', min(r['words'] for r in rows), 'to', max(r['words'] for r in rows))


if __name__ == '__main__':
    main()
