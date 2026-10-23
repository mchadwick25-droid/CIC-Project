/**
 * Google's and Apple's own sign-in scripts. Neither is loaded until the person presses a provider
 * button. Each is then readied for the nonce this server issued, and the person finishes in the
 * provider's own button or window, which yields a signed ID token for that nonce.
 */
export type Provider = 'google' | 'apple';

const SCRIPTS: Record<Provider, string> = {
  google: 'https://accounts.google.com/gsi/client',
  apple: 'https://appleid.cdn-apple.com/appleauth/static/jsapi/appleid/1/en_US/appleid.auth.js',
};

const loading = new Map<Provider, Promise<void>>();

function load(provider: Provider): Promise<void> {
  const held = loading.get(provider);
  if (held) return held;
  const started = new Promise<void>((resolve, reject) => {
    const script = document.createElement('script');
    script.src = SCRIPTS[provider];
    script.async = true;
    script.onload = () => resolve();
    script.onerror = () => {
      loading.delete(provider);
      script.remove();
      reject(new Error('script'));
    };
    document.head.appendChild(script);
  });
  loading.set(provider, started);
  return started;
}

interface GoogleId {
  initialize(options: { client_id: string; nonce: string; callback: (response: { credential?: string }) => void; auto_select: boolean }): void;
  renderButton(parent: HTMLElement, options: { type: string; theme: string; size: string; text: string }): void;
}
interface AppleAuth {
  init(options: { clientId: string; scope: string; redirectURI: string; state: string; nonce: string; usePopup: boolean }): void;
  signIn(): Promise<{ authorization?: { id_token?: string } }>;
}
interface ProviderWindow {
  google?: { accounts: { id: GoogleId } };
  AppleID?: { auth: AppleAuth };
}

let googleDone: ((credential: string | null) => void) | null = null;

/** Loads the provider's script and readies it for this nonce. Called on a press, never before. */
export async function prepare(provider: Provider, clientId: string, nonce: string): Promise<void> {
  await load(provider);
  const scope = window as unknown as ProviderWindow;
  if (provider === 'google') {
    const google = scope.google?.accounts.id;
    if (!google) throw new Error('script');
    google.initialize({ client_id: clientId, nonce, auto_select: false, callback: (response) => googleDone?.(response.credential ?? null) });
    return;
  }
  const apple = scope.AppleID?.auth;
  if (!apple) throw new Error('script');
  apple.init({ clientId, scope: '', redirectURI: window.location.origin, state: 'cic', nonce, usePopup: true });
}

/** Google's own button, drawn into the element. The token arrives through onToken when the person finishes. */
export function renderGoogleButton(parent: HTMLElement, onToken: (credential: string | null) => void): void {
  const google = (window as unknown as ProviderWindow).google?.accounts.id;
  if (!google) {
    onToken(null);
    return;
  }
  googleDone = onToken;
  google.renderButton(parent, { type: 'standard', theme: 'outline', size: 'large', text: 'continue_with' });
}

/** Apple's window. Called straight from the person's press, so the browser lets it open. */
export async function appleSignIn(): Promise<string | null> {
  const apple = (window as unknown as ProviderWindow).AppleID?.auth;
  if (!apple) return null;
  const result = await apple.signIn();
  return result.authorization?.id_token ?? null;
}
