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

  root.CFTSearch = Object.assign(root.CFTSearch || {}, { normalize, stem, words, withinOneTypo });
  if (typeof module !== 'undefined' && module.exports) module.exports = root.CFTSearch;
})(typeof globalThis !== 'undefined' ? globalThis : this);
