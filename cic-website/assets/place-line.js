(function (root) {
  function joinNames(list) {
    return list.length < 2 ? (list[0] || '') : list.slice(0, -1).join(', ') + ' and ' + list[list.length - 1];
  }
  function formatPlace(entry, opts) {
    const today = !!(opts && opts.today);
    const label = (entry && entry.placeLabel) || '';
    if (!label) return '';
    const beyond = / and beyond$/.test(label);
    const places = label.replace(/ and beyond$/, '').split(' · ');
    const named = new Set(places);
    const qualifiers = entry.placeQualifiers || {};
    const byPlace = {};
    (entry.modernCountries || []).forEach(c => {
      const list = byPlace[c.place] || (byPlace[c.place] = []);
      if (!list.includes(c.country)) list.push(c.country);
    });
    const groups = [];
    places.forEach(p => {
      const countries = (byPlace[p] || []).filter(c => !named.has(c));
      const key = countries.join('|');
      const last = groups[groups.length - 1];
      if (last && key && last.key === key) last.places.push(p);
      else groups.push({ places: [p], countries, key });
    });
    const text = groups.map(g => g.places.map(p => p + (qualifiers[p] || '')).join(' · ') +
      (g.countries.length ? (today ? ', today in ' : ', ') + joinNames(g.countries) : '')).join(' · ');
    return text + (beyond ? ' and beyond' : '');
  }
  root.CFTPlace = { formatPlace };
})(typeof globalThis !== 'undefined' ? globalThis : this);
