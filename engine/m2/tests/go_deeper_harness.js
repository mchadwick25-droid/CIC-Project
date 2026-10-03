const GD = require("../../../cic-website/assets/go-deeper.js");
const nodeCrypto = require("crypto").webcrypto;

function memoryStorage() {
  const data = new Map();
  return {
    getItem: (k) => (data.has(k) ? data.get(k) : null),
    setItem: (k, v) => void data.set(k, String(v)),
    removeItem: (k) => void data.delete(k),
    has: (k) => data.has(k),
  };
}

function reply(status, body) {
  return Promise.resolve({ ok: status >= 200 && status < 300, status, json: () => Promise.resolve(body) });
}

async function claimWith(script) {
  const storage = memoryStorage();
  storage.setItem("cic_claim_ref", JSON.stringify({ ref: "r".repeat(22), at: 0 }));
  const calls = [];
  const sleeps = [];
  let i = 0;
  const env = {
    apiBase: "https://api.test",
    storage,
    fetch: (url, init) => {
      calls.push({ url, init });
      const step = script[Math.min(i++, script.length - 1)];
      return step === "network" ? Promise.reject(new Error("offline")) : reply(step.status, step.body);
    },
    sleep: (ms) => {
      sleeps.push(ms);
      return Promise.resolve();
    },
  };
  const result = await GD.claimCodes("r".repeat(22), env);
  return { result, calls, sleeps, kept: storage.has("cic_claim_ref") };
}

const scenarios = {
  references() {
    const seen = new Set();
    for (let n = 0; n < 300; n++) seen.add(GD.makeReference(nodeCrypto));
    return { distinct: seen.size, allValid: [...seen].every((r) => /^[A-Za-z0-9_-]{22}$/.test(r)) };
  },
  purchase() {
    const storage = memoryStorage();
    const went = [];
    const env = { crypto: nodeCrypto, storage, now: () => 1000, go: (u) => went.push(u) };
    GD.startPurchase("https://buy.stripe.test/abc", env);
    const first = JSON.parse(storage.getItem("cic_claim_ref"));
    GD.startPurchase("https://buy.stripe.test/abc", env);
    const second = JSON.parse(storage.getItem("cic_claim_ref"));
    const withQuery = GD.purchaseUrl("https://buy.stripe.test/abc?prefilled=1", "XYZ");
    return { went, first, second, withQuery };
  },
  expiry() {
    const storage = memoryStorage();
    storage.setItem("cic_claim_ref", JSON.stringify({ ref: "keepme", at: 1000 }));
    const fresh = GD.readReference(storage, 1000 + 59 * 60 * 1000);
    const stale = GD.readReference(storage, 1000 + 61 * 60 * 1000);
    const staleRemoved = !storage.has("cic_claim_ref");
    storage.setItem("cic_claim_ref", "not json");
    const broken = GD.readReference(storage, 5);
    return { fresh, stale, staleRemoved, broken };
  },
  claimReady: () =>
    claimWith([{ status: 404 }, { status: 404 }, { status: 200, body: { codes: ["ABCD 2345 EFGH 6789 JKLM"], exchanges: 40 } }]),
  claimMissing: () => claimWith([{ status: 404 }]),
  claimServerError: () => claimWith([{ status: 500 }]),
  claimOffline: () => claimWith(["network"]),
  handOff() {
    const sent = [];
    const live = { closed: false, postMessage: (m, o) => sent.push([m, o]) };
    const a = GD.handOff(live, ["ABCD"], "https://app.test");
    const b = GD.handOff({ closed: true, postMessage: () => sent.push("closed") }, ["ABCD"], "https://app.test");
    const c = GD.handOff(null, ["ABCD"], "https://app.test");
    const d = GD.handOff({ closed: false, postMessage: () => { throw new Error("blocked"); } }, ["ABCD"], "https://app.test");
    return { a, b, c, d, sent };
  },
  async deliver() {
    const log = [];
    function env(opener, answer) {
      let listener = null;
      const later = [];
      return {
        env: {
          opener,
          appOrigin: "https://app.test",
          onMessage: (fn) => (listener = fn),
          later: (fn) => later.push(fn),
          waitMs: 3000,
          close: () => log.push("close"),
          redirect: (u) => log.push("redirect " + u),
        },
        answer: () => answer && listener && listener(answer),
        timeout: () => later.forEach((fn) => fn()),
      };
    }
    const open = () => ({ closed: false, postMessage: () => {} });
    const out = {};
    // several codes: left on the page
    out.pack = await GD.deliver(["A", "B"], env(open(), null).env);
    // an answering opener: closes, never redirects
    let t = env(open(), { origin: "https://app.test", data: { type: "cic-deeper-saved" } });
    let p = GD.deliver(["ABCD 2345"], t.env);
    t.answer();
    out.answered = await p;
    // an opener that never answers: redirects after the wait
    t = env(open(), null);
    p = GD.deliver(["ABCD 2345"], t.env);
    t.timeout();
    out.silent = await p;
    // an answer from the wrong origin does not count
    t = env(open(), { origin: "https://evil.test", data: { type: "cic-deeper-saved" } });
    p = GD.deliver(["ABCD 2345"], t.env);
    t.answer();
    t.timeout();
    out.wrongOrigin = await p;
    // no opener at all: straight to the app
    t = env(null, null);
    out.noOpener = await GD.deliver(["ABCD 2345"], t.env);
    out.log = log;
    return out;
  },
  limits: () => ({ poll: GD.POLL_MS, tries: GD.MAX_TRIES }),
};

Promise.resolve(scenarios[process.argv[2]]()).then((out) => console.log(JSON.stringify(out)));
