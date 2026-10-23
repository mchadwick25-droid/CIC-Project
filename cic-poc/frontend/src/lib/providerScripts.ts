/**
 * Google's and Apple's own sign-in scripts. Neither is loaded until the person presses a provider
 * button; each yields a signed ID token made for the nonce this server issued.
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
      reject(new Error('script'));
    };
    document.head.appendChild(script);
  });
  loading.set(provider, started);
  return started;
}

interface GoogleId {
  initialize(options: { client_id: string; nonce: string; callback: (response: { credential?: string }) => void; auto_select: boolean; cancel_on_tap_outside: boolean }): void;
  prompt(moment: (notification: { isNotDisplayed(): boolean; isSkippedMoment(): boolean; isDismissedMoment(): boolean }) => void): void;
}
interface AppleAuth {
  init(options: { clientId: string; scope: string; redirectURI: string; state: string; nonce: string; usePopup: boolean }): void;
  signIn(): Promise<{ authorization?: { id_token?: string } }>;
}
interface ProviderWindow {
  google?: { accounts: { id: GoogleId } };
  AppleID?: { auth: AppleAuth };
}

export async function idTokenFrom(provider: Provider, clientId: string, nonce: string): Promise<string> {
  await load(provider);
  const scope = window as unknown as ProviderWindow;
  if (provider === 'google') {
    const google = scope.google?.accounts.id;
    if (!google) throw new Error('script');
    return new Promise<string>((resolve, reject) => {
      google.initialize({
        client_id: clientId,
        nonce,
        auto_select: false,
        cancel_on_tap_outside: true,
        callback: (response) => (response.credential ? resolve(response.credential) : reject(new Error('none'))),
      });
      google.prompt((moment) => {
        if (moment.isNotDisplayed() || moment.isSkippedMoment() || moment.isDismissedMoment()) reject(new Error('closed'));
      });
    });
  }
  const apple = scope.AppleID?.auth;
  if (!apple) throw new Error('script');
  apple.init({ clientId, scope: '', redirectURI: window.location.origin, state: 'cic', nonce, usePopup: true });
  const result = await apple.signIn();
  const token = result.authorization?.id_token;
  if (!token) throw new Error('none');
  return token;
}
