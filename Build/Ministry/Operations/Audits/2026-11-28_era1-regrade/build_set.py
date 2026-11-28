"""Build the set of six era 1 person briefs for the regrade, and the packets the readers read.

The method is ../2026-11-28_era1-new-grades/build_set.py, with each final brief taken from the
branch it was fixed or written on. Run from the repository root after fetching the branches:
python Build/Ministry/Operations/Audits/2026-11-28_era1-regrade/build_set.py
Reads only; writes Set.json, Texts.json and packets/ in this folder.
"""
import csv
import json
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..', '..'))
BATCH = 'Build/Ministry/Operations/Audits/2026-11-26_batch-12'
BEFORE = os.path.join(HERE, '..', '2026-11-28_era1-new-grades', 'Grades_Whole.csv')
SOURCES = [
    ('methodius-of-olympus', 'Methodius of Olympus', 'origin/claude/cft-release-batch12-13'),
    ('suetonius', 'Suetonius', 'origin/claude/cft-release-batch12-13'),
    ('hippolytus-of-rome', 'Hippolytus of Rome', 'origin/claude/cft-release-batch12-13'),
    ('tacitus', 'Tacitus', 'origin/claude/cft-release-batch12-13'),
    ('josephus', 'Josephus', 'origin/claude/cft-fix-josephus-grade'),
    ('cyprian-of-carthage', 'Cyprian of Carthage', 'origin/claude/cft-story-cyprian-of-carthage'),
]
FLOOR = 300


def show(ref, path):
    return subprocess.run(['git', 'show', f'{ref}:{path}'], cwd=ROOT, capture_output=True,
                          text=True, check=True).stdout


def main():
    before = {r['id']: r for r in csv.DictReader(open(BEFORE, encoding='utf-8'))}
    texts, rows = {}, []
    for slug, name, ref in SOURCES:
        path = f'{BATCH}/{slug}/{slug}.brief.txt'
        texts[slug] = show(ref, path)
        sha = subprocess.run(['git', 'rev-parse', ref], cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()
        b = before.get(slug)
        rows.append({'id': slug, 'name': name, 'kind': 'person', 'era': 1, 'batch': '12', 'reference': False,
                     'words': len(texts[slug].split()), 'floor': FLOOR, 'text_from': f'{ref[7:]} @ {sha[:8]}: {path}',
                     'before': {k: b[k] for k in ('rigor', 'craft', 'overall')} if b else 'new'})
    json.dump(rows, open(os.path.join(HERE, 'Set.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    json.dump(texts, open(os.path.join(HERE, 'Texts.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)

    def write(name, prefix):
        with open(os.path.join(HERE, 'packets', name + '.md'), 'w', encoding='utf-8') as f:
            f.write(f'# Packet {name}: six era 1 person briefs, regrade (final text)\n')
            for r in rows:
                f.write(f"\n## {prefix}{r['id']}\n\n{r['name']}\n\n{texts[r['id']].strip()}\n")

    write('L01', '')
    write('S01', 'tree/')
    print(len(rows), 'stories;', 'words', [r['words'] for r in rows])


if __name__ == '__main__':
    main()
