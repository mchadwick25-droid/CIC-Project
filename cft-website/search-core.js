(function (root) {
  const SAINT = /\bst\.?(?=\s)/g;

  // Lowercase, no accents, no punctuation, one space between words; "St" and "Saint" are one word.
  function normalize(text) {
    return String(text == null ? '' : text)
      .normalize('NFD').replace(/[\u0300-\u036f]/g, '')
      .toLowerCase()
      .replace(/[’‘`]/g, "'")
      .replace(/'s\b/g, '')
      .replace(/[–—‐-]/g, ' ')
      .replace(SAINT, 'saint')
      .replace(/[^a-z0-9 ]+/g, ' ')
      .replace(/\s+/g, ' ')
      .trim();
  }

  // Plain plural handling for words of four or more letters: "churches" and "church", "bodies" and "body".
  function stem(word) {
    if (word.length < 4 || /\d/.test(word)) return word;
    if (/ies$/.test(word)) return word.slice(0, -3) + 'y';
    if (/(ss|us|is)$/.test(word)) return word;
    if (/(ch|sh|x|z|s)es$/.test(word)) return word.slice(0, -2);
    if (/s$/.test(word)) return word.slice(0, -1);
    return word;
  }

  function words(text) {
    const out = [];
    for (const w of normalize(text).split(' ')) if (w) out.push(stem(w));
    return out;
  }

  // One word each side differs by one inserted, dropped, changed or swapped letter.
  function withinOneTypo(a, b) {
    if (a === b) return true;
    const la = a.length, lb = b.length;
    if (Math.abs(la - lb) > 1) return false;
    let i = 0;
    while (i < la && i < lb && a[i] === b[i]) i++;
    if (la === lb) {
      if (a.slice(i + 1) === b.slice(i + 1)) return true;
      return a[i] === b[i + 1] && a[i + 1] === b[i] && a.slice(i + 2) === b.slice(i + 2);
    }
    return la > lb ? a.slice(i + 1) === b.slice(i) : b.slice(i + 1) === a.slice(i);
  }


  // Every path here is text a visitor can read on the entry's own card or tree page. "[]" walks a list.
  const TEXT_PATHS = [
    'teaser', 'longDescription', 'why', 'floorNote', 'relationsSummary', 'peopleNote',
    'voices[]', 'legacy',
    'experienceToday[].text',
    'documentedStories[].title', 'documentedStories[].teaser', 'documentedStories[].text', 'documentedStories[].caveat',
    'card.otherNames[].note', 'card.knownFor', 'card.role', 'card.placeNote', 'card.datesNote', 'card.uncertain[]',
    'card.keyWorks[].title', 'card.keyWorks[].about',
    'card.legacy.traces[]', 'card.legacy.remembered[]',
    'card.quotationOriginals[].modern',
    'council.knownFor', 'council.calledBy', 'council.issue[]', 'council.attended[]', 'council.decided[]',
    'council.outcome[]', 'council.uncertain[]', 'council.record[].note', 'council.traditions[].note',
  ];

  function collect(value, parts, out) {
    if (value == null) return;
    if (parts.length === 0) {
      if (typeof value === 'string') out.push(value);
      return;
    }
    const head = parts[0], rest = parts.slice(1);
    const list = /\[\]$/.test(head);
    const key = list ? head.slice(0, -2) : head;
    const next = value[key];
    if (next == null) return;
    if (list) {
      if (Array.isArray(next)) for (const el of next) collect(el, rest, out);
    } else collect(next, rest, out);
  }

  function visibleText(entry) {
    const out = [];
    for (const p of TEXT_PATHS) collect(entry, p.split('.'), out);
    return out;
  }

  // How a sourced name is described to the visitor. The words come from the kind the names file records.
  const NAME_NOTE = {
    o: 'another name', l: 'an older name', p: 'another spelling',
    x: 'a name its opponents gave it',
  };

  // Dates: "1054", "c. 1054", "1054 AD", "1000-1100", "1000 to 1100", "11th century".
  function parseDate(query) {
    const q = String(query || '').toLowerCase().replace(/[–—]/g, '-').replace(/\ba\.?d\.?|\bc\.?e\.?\b/g, ' ')
      .replace(/\b(?:circa|ca|c)\.?(?=\s*\d)/g, ' ').replace(/\s+/g, ' ').trim();
    let m = /^(\d{1,2})(?:st|nd|rd|th)?\s+century$/.exec(q);
    if (m && +m[1] >= 1 && +m[1] <= 21) return { type: 'century', a: (+m[1] - 1) * 100 + 1, b: +m[1] * 100, n: +m[1] };
    m = /^(\d{1,4})\s*(?:-|to)\s*(\d{1,4})$/.exec(q);
    if (m && +m[1] <= +m[2]) return { type: 'range', a: +m[1], b: +m[2] };
    m = /^(\d{1,4})$/.exec(q);
    if (m && +m[1] > 0) return { type: 'year', a: +m[1], b: +m[1] };
    return null;
  }

  function eraYears(dates) {
    const nums = String(dates || '').match(/\d+/g) || [];
    return [+nums[0] || 0, +nums[nums.length > 1 ? nums.length - 1 : 0] || 9999];
  }

  const QUERY_STOP = new Set(('what does did do say says said about how who why which where when is are was were the a an of ' +
    'in on to for and or by with from tell me us view views think thought believe believed taught teach teaches ' +
    'say mean means').split(' '));

  function decodeWordList(list) {
    const map = new Map();
    for (const line of list.words) {
      const cut = line.indexOf(' ');
      let prev = 0;
      map.set(line.slice(0, cut), line.slice(cut + 1).split(',').map((g) => (prev += parseInt(g, 36))));
    }
    return map;
  }

  // Entries that use every word of the question (words of three or more letters, question words left out).
  function searchWords(wordMap, query) {
    const tokens = [], shown = [];
    for (const raw of normalize(query).split(' ')) {
      const w = stem(raw);
      if (raw.length >= 3 && !QUERY_STOP.has(raw) && !tokens.includes(w)) { tokens.push(w); shown.push(raw); }
    }
    if (!tokens.length) return { tokens, shown, ids: [], missing: [] };
    let ids = null;
    const missing = [];
    for (const t of tokens) {
      let list = wordMap.get(t);
      if (!list && t.length >= 5) {
        for (const [w, l] of wordMap) if (w[0] === t[0] && withinOneTypo(t, w)) { list = l; break; }
      }
      if (!list) { missing.push(t); continue; }
      ids = ids ? ids.filter((i) => list.includes(i)) : list.slice();
    }
    return { tokens, shown, ids: missing.length ? [] : ids || [], missing };
  }

  // The sentence in the entry's visible text that holds most of the words. Returned exactly as written.
  function bestSentence(texts, tokens) {
    let best = null, bestScore = 0;
    for (const text of texts) {
      for (const raw of text.split(/(?<=[.!?])\s+/)) {
        const sentence = raw.trim();
        if (!sentence) continue;
        const have = new Set(words(sentence));
        const score = tokens.filter((t) => have.has(t)).length;
        if (score > bestScore) { best = sentence; bestScore = score; }
      }
    }
    return best;
  }

  // info[i] describes entry i of the names index: { id, name, short, kind, start, end, living, era, countries, place }.
  function createSearcher(index, info, wordMap) {
    const stemmed = index.names.map(([n, i, k]) => ({ n, s: words(n).join(' '), w: words(n), i, k }));
    const placeRows = (index.places || []).map(([n, t, v, k]) => ({ s: words(n).join(' '), w: words(n), t, v, k }));
    const byCountry = new Map();
    info.forEach((e, i) => {
      if (!e) return;
      for (const c of e.countries || []) {
        let list = byCountry.get(c);
        if (!list) byCountry.set(c, (list = []));
        list.push(i);
      }
    });
    const countryNames = [...byCountry.keys()].sort().map((c) => ({ name: c, s: words(c).join(' '), w: words(c) }));
    const placeText = info.map((e) => (e ? normalize(e.place || '') : ''));
    const eraRows = index.eras.map(([num, title, academic, dates], at) => ({
      num, at, label: title, dates, years: eraYears(dates),
      parts: [words(title), academic ? words(academic) : null, [stem('era'), String(num)]].filter(Boolean),
    }));
    const riverRows = index.rivers.map(([k, name, common]) => ({ k, label: name, common, parts: [words(name), common ? words(common) : null].filter(Boolean) }));

    function rankText(s, w, qs, qt) {
      if (s === qs) return 0;
      if (s.startsWith(qs)) return 1;
      if (qt.every((t) => w.some((x) => x.startsWith(t)))) return 2;
      if (withinOneTypo(s, qs) && qs.length >= 4) return 3;
      if (qt.every((t) => t.length >= 4 && w.some((x) => x.length >= 4 && withinOneTypo(t, x)))) return 3;
      return 9;
    }

    function matchNames(qs, qt) {
      const best = new Map();
      for (const r of stemmed) {
        const rank = rankText(r.s, r.w, qs, qt);
        if (rank > 3) continue;
        const cur = best.get(r.i);
        if (!cur || rank < cur.rank) best.set(r.i, { i: r.i, rank, via: r.k, matched: r.n });
      }
      return best;
    }

    function inCountry(name) { return byCountry.get(name) || []; }
    function inRegion(phrase) {
      const out = [];
      placeText.forEach((t, i) => { if (t && (' ' + t + ' ').includes(' ' + phrase + ' ')) out.push(i); });
      return out;
    }
    function inYears(a, b) {
      const out = [];
      info.forEach((e, i) => { if (e && e.start != null && e.end != null && e.start <= b && e.end >= a) out.push(i); });
      return out;
    }
    function eraOf(year) {
      let hit = -1;
      eraRows.forEach((e) => { if (hit < 0 && year >= e.years[0] && year < e.years[1]) hit = e.at; });
      if (hit < 0 && eraRows.length && year >= eraRows[eraRows.length - 1].years[0]) hit = eraRows[eraRows.length - 1].at;
      return hit;
    }

    function search(query) {
      const out = { query, entries: [], places: [], parts: [], date: null, nearest: null, strong: false };
      const date = parseDate(query);
      if (date) {
        const ids = inYears(date.a, date.b);
        out.date = Object.assign({ ids }, date);
        const first = eraOf(date.a), last = eraOf(date.b);
        for (let e = first; e >= 0 && e <= last; e++) out.parts.push({ type: 'era', at: e, label: eraRows[e].label, rank: 0 });
        out.strong = true;
        return out;
      }
      const qs = words(query).join(' '), qt = words(query).filter((t) => t.length >= 2);
      if (!qt.length) return out;
      const best = matchNames(qs, qt);
      const spoken = normalize(query).split(' ');
      out.question = spoken.length >= 3 && spoken.some((w) => QUERY_STOP.has(w));
      if (out.question) {
        for (const w of spoken) {
          if (QUERY_STOP.has(w) || w.length < 4) continue;
          const t = stem(w), named = new Map();
          for (const r of stemmed) if (r.w.includes(t) && !named.has(r.i)) named.set(r.i, { i: r.i, rank: 2, via: r.k, matched: r.n });
          if (named.size <= 5) for (const hit of named.values()) if (!best.has(hit.i)) best.set(hit.i, hit);
        }
      }
      for (const hit of best.values()) if (info[hit.i]) out.entries.push(hit);
      out.entries.sort((a, b) => a.rank - b.rank || (info[a.i].start || 0) - (info[b.i].start || 0) || a.i - b.i);
      const seen = new Set();
      for (const c of countryNames) {
        const rank = rankText(c.s, c.w, qs, qt);
        if (rank <= 3 && !seen.has(c.name)) { seen.add(c.name); out.places.push({ type: 'country', label: c.name, ids: inCountry(c.name), rank }); }
      }
      for (const r of placeRows) {
        const rank = rankText(r.s, r.w, qs, qt);
        if (rank > 3) continue;
        const label = r.t === 'c' ? r.v : r.v;
        const key = r.t + ':' + label;
        if (seen.has(key)) continue;
        seen.add(key);
        const ids = r.t === 'c' ? inCountry(r.v) : inRegion(normalize(r.v));
        out.places.push({ type: r.t === 'c' ? 'country' : 'region', label, alias: r.s, note: NAME_NOTE[r.k], ids, rank });
      }
      out.places.sort((a, b) => a.rank - b.rank);
      for (const e of eraRows) {
        const rank = Math.min(...e.parts.map((p) => rankText(p.join(' '), p, qs, qt)));
        if (rank <= 3) out.parts.push({ type: 'era', at: e.at, label: e.label, rank });
      }
      for (const r of riverRows) {
        const rank = Math.min(...r.parts.map((p) => rankText(p.join(' '), p, qs, qt)));
        if (rank <= 3) out.parts.push({ type: 'river', k: r.k, label: r.label, common: r.common, rank });
      }
      out.parts.sort((a, b) => a.rank - b.rank);
      out.strong = out.entries.some((e) => e.rank <= 2) || out.places.some((p) => p.rank <= 2) || out.parts.some((p) => p.rank <= 2);
      if (!out.entries.length && !out.places.length && !out.parts.length && qs.length >= 3) out.nearest = nearest(qs);
      return out;
    }

    // The closest name to a word that matched nothing, found by the letters it shares at the start and by edits.
    function nearest(qs) {
      let best = null, bestScore = 0;
      const consider = (label, s) => {
        let score = 0;
        const n = Math.min(s.length, qs.length);
        while (score < n && s[score] === qs[score]) score++;
        if (score >= 3 && score > bestScore) { best = label; bestScore = score; }
      };
      for (const r of stemmed) if (info[r.i]) consider(info[r.i].short || info[r.i].name, r.s);
      for (const c of countryNames) consider(c.name, c.s);
      return best;
    }

    return { search, inCountry, inRegion, inYears, eraOf, eraRows, riverRows, searchWords: (q) => (wordMap ? searchWords(wordMap, q) : null) };
  }

  root.CFTSearch = Object.assign(root.CFTSearch || {}, {
    normalize, stem, words, withinOneTypo, TEXT_PATHS, visibleText, NAME_NOTE, parseDate, eraYears, QUERY_STOP,
    decodeWordList, searchWords, bestSentence, createSearcher,
  });
  if (typeof module !== 'undefined' && module.exports) module.exports = root.CFTSearch;
})(typeof globalThis !== 'undefined' ? globalThis : this);
