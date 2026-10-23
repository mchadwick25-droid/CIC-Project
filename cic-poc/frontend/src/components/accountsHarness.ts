import { vi } from 'vitest';

export type Reply = { status?: number; body?: unknown };
export type Call = { path: string; method: string; headers: Record<string, string>; body: Record<string, unknown> | null };
export type Routes = Record<string, Reply | ((body: Record<string, unknown> | null) => Reply)>;

export const BALANCE = { signed_in: true, available: true, free_left: 440, free_total: 550, refill_on: 'Nov 14', codes_held: 0, code_tokens: 0 };

export function serve(routes: Routes) {
  const calls: Call[] = [];
  vi.stubGlobal(
    'fetch',
    vi.fn(async (url: string, init: RequestInit = {}) => {
      const path = String(url).replace('/api/accounts', '');
      const body = init.body ? (JSON.parse(String(init.body)) as Record<string, unknown>) : null;
      calls.push({ path, method: init.method ?? 'GET', headers: (init.headers ?? {}) as Record<string, string>, body });
      const hit = routes[path];
      const reply = typeof hit === 'function' ? hit(body) : hit;
      if (!reply) return new Response(JSON.stringify({ detail: 'x' }), { status: 404 });
      return new Response(JSON.stringify(reply.body ?? {}), { status: reply.status ?? 200 });
    })
  );
  return calls;
}

export const signedOut = (providers: Record<string, string> = {}): Routes => ({
  '/me': { body: { signed_in: false } },
  '/providers': { body: { providers } },
});

export const signedIn = (methods: string[], providers: Record<string, string> = {}, extra: Partial<Record<string, unknown>> = {}): Routes => ({
  '/me': { body: { signed_in: true, recovery_pending: null, sign_in_methods: methods, has_recovery_code: true, refill_day: 14, ...extra } },
  '/providers': { body: { providers } },
  '/balance': { body: BALANCE },
  '/shelf': { body: { conversations: [] } },
});
