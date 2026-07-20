/**
 * SignInScreen - shown before world selection once a real Supabase project
 * is configured (see src/lib/supabase.ts's supabaseEnabled). Passwordless:
 * a participant enters their email, Supabase sends a magic sign-in link,
 * and returning to this page (or clicking the link, which redirects back
 * here) completes sign-in - no password to set, reset, or forget.
 *
 * Skipped entirely in local dev / before a Supabase project exists, so this
 * never blocks development or the existing pilot flow.
 */

import { useState } from 'react';
import { supabase } from '../lib/supabase';

export function SignInScreen() {
  const [email, setEmail] = useState('');
  const [linkSent, setLinkSent] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [isSending, setIsSending] = useState(false);

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    if (!supabase || !email.trim()) return;

    setIsSending(true);
    setError(null);

    const { error: signInError } = await supabase.auth.signInWithOtp({
      email: email.trim(),
      options: { emailRedirectTo: window.location.href },
    });

    setIsSending(false);
    if (signInError) {
      setError(signInError.message);
      return;
    }
    setLinkSent(true);
  };

  return (
    <div className="onboarding-screen">
      <div className="onboarding-screen__content">
        <h2>Sign in to begin</h2>

        {linkSent ? (
          <p>
            Check <strong>{email}</strong> for a sign-in link. Click it and you'll be brought right
            back here, signed in.
          </p>
        ) : (
          <>
            <p>
              This pilot is by invitation. Enter the email you were invited with, and we'll send you
              a link to sign in — no password to create or remember.
            </p>
            <form onSubmit={handleSubmit}>
              <input
                type="email"
                required
                autoFocus
                placeholder="you@example.com"
                value={email}
                onChange={(event) => setEmail(event.target.value)}
                className="chat-input__field"
                style={{ marginBottom: '1rem', width: '100%' }}
              />
              {error && <p style={{ color: 'var(--madder, #A13E2B)' }}>{error}</p>}
              <button
                type="submit"
                className="chat-button chat-button--primary chat-button--large"
                disabled={isSending}
              >
                {isSending ? 'Sending…' : 'Send my sign-in link'}
              </button>
            </form>
          </>
        )}
      </div>
    </div>
  );
}
