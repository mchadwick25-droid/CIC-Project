(function (root) {
  "use strict";

  var REFERENCE_KEY = "cic_claim_ref";
  var REFERENCE_TTL_MS = 60 * 60 * 1000;
  var POLL_MS = 3000;
  var MAX_TRIES = 20;
  var ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_";

  function makeReference(cryptoApi) {
    var bytes = new Uint8Array(16);
    cryptoApi.getRandomValues(bytes);
    var out = "";
    var acc = 0;
    var bits = 0;
    for (var i = 0; i < bytes.length; i++) {
      acc = (acc << 8) | bytes[i];
      bits += 8;
      while (bits >= 6) {
        bits -= 6;
        out += ALPHABET.charAt((acc >> bits) & 63);
      }
      acc &= (1 << bits) - 1;
    }
    if (bits > 0) out += ALPHABET.charAt((acc << (6 - bits)) & 63);
    return out;
  }

  function purchaseUrl(link, reference) {
    return link + (link.indexOf("?") === -1 ? "?" : "&") + "client_reference_id=" + encodeURIComponent(reference);
  }

  function readReference(storage, now) {
    try {
      var raw = storage.getItem(REFERENCE_KEY);
      if (!raw) return null;
      var held = JSON.parse(raw);
      if (typeof held.ref !== "string" || typeof held.at !== "number" || now - held.at > REFERENCE_TTL_MS) {
        storage.removeItem(REFERENCE_KEY);
        return null;
      }
      return held.ref;
    } catch (e) {
      return null;
    }
  }

  function startPurchase(link, env) {
    var reference = makeReference(env.crypto);
    try {
      env.storage.setItem(REFERENCE_KEY, JSON.stringify({ ref: reference, at: env.now() }));
    } catch (e) {
      return false;
    }
    env.go(purchaseUrl(link, reference));
    return true;
  }

  function claimCodes(reference, env) {
    var tries = 0;
    function attempt() {
      tries += 1;
      return env
        .fetch(env.apiBase + "/api/deeper/claim", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          credentials: "omit",
          referrerPolicy: "no-referrer",
          body: JSON.stringify({ reference: reference }),
        })
        .then(function (response) {
          if (response.ok) {
            return response.json().then(function (body) {
              return { status: "ready", codes: body.codes, exchanges: body.exchanges };
            });
          }
          if ((response.status === 404 || response.status === 429) && tries < MAX_TRIES) {
            return env.sleep(POLL_MS).then(attempt);
          }
          return { status: response.status === 404 ? "missing" : "error" };
        })
        .catch(function () {
          if (tries < MAX_TRIES) return env.sleep(POLL_MS).then(attempt);
          return { status: "error" };
        });
    }
    return attempt();
  }

  // Hands the code to the conversation that opened this window, if it is still
  // there, to that one origin only. The caller shows the code regardless.
  function handOff(opener, codes, appOrigin) {
    try {
      if (!opener || opener.closed) return false;
      opener.postMessage({ type: "cic-deeper-code", codes: codes }, appOrigin);
      return true;
    } catch (e) {
      return false;
    }
  }

  var api = { handOff: handOff, makeReference: makeReference, purchaseUrl: purchaseUrl, readReference: readReference, startPurchase: startPurchase, claimCodes: claimCodes, POLL_MS: POLL_MS, MAX_TRIES: MAX_TRIES };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else root.GoDeeper = api;
})(typeof window !== "undefined" ? window : this);
