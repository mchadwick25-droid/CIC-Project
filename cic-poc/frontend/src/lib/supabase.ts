/**
 * Supabase client for participant sign-in (magic link) and session-token
 * retrieval. Reads its project URL/anon key from Vite env vars, which are
 * unset in local dev until Mark's Supabase project exists - `supabaseEnabled`
 * is false in that case, and the app skips sign-in entirely (same "off until
 * configured" discipline as the backend's session_cap.py/transcript_logging.py).
 */

import { createClient, type SupabaseClient } from '@supabase/supabase-js';

const url = import.meta.env.VITE_SUPABASE_URL as string | undefined;
const anonKey = import.meta.env.VITE_SUPABASE_ANON_KEY as string | undefined;

export const supabaseEnabled = Boolean(url && anonKey);

export const supabase: SupabaseClient | null = supabaseEnabled
  ? createClient(url as string, anonKey as string)
  : null;

/** The current signed-in participant's access token, or null if not signed in / not configured. */
export async function getAccessToken(): Promise<string | null> {
  if (!supabase) return null;
  const { data } = await supabase.auth.getSession();
  return data.session?.access_token ?? null;
}
