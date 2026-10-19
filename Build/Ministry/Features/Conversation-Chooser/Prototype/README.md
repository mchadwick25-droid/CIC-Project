# Prototype: the three directions

`chooser-directions.template.html` is deliverable 3 as shown to Mark on 2026-10-19 (private page: `https://claude.ai/artifact/Npf19NpmiF9hKsPKcsj5ah`). It is a template: two placeholders hold data that is generated from the repo, so the file stays small and the portraits stay in one place.

- `/*THUMBS*/` takes a JSON object mapping each thumbnail name to a `data:image/webp;base64,…` URI, built from `cic-website/assets/portraits/thumb/*.webp`.
- `/*SEARCH*/` takes a JSON object mapping each live world's census id to its lowercased search text: the census `name`, `informalName`, `region` and `voices` strings.

To rebuild the page:

```
python3 - <<'EOF'
import base64, glob, json, os, re
thumbs = {os.path.splitext(os.path.basename(f))[0]: 'data:image/webp;base64,' + base64.b64encode(open(f,'rb').read()).decode()
          for f in glob.glob('cic-website/assets/portraits/thumb/*.webp')}
census = json.load(open('cic-website/data/world-census.json'))
search = {}
for m in census['movements']:
    if m.get('status','').startswith('Built'):
        parts = [m.get('name',''), m.get('informalName') or '', m.get('region') or ''] + [v for v in (m.get('voices') or []) if isinstance(v, str)]
        search[m['id']] = re.sub(r'\s+', ' ', ' '.join(parts).lower())
t = open('Build/Ministry/Features/Conversation-Chooser/Prototype/chooser-directions.template.html').read()
out = t.replace('/*THUMBS*/', json.dumps(thumbs), 1).replace('/*SEARCH*/', json.dumps(search), 1)
open('/tmp/chooser-directions.html', 'w').write(out)
EOF
```

The page is a prototype, not the build. Its card words are drafts; Donatism is provisional. The design the build follows is in `../Build-Plan.md`.
