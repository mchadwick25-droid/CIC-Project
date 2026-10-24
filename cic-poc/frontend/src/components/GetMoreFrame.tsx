/**
 * The app as the site's landing page frames it for "Get more conversations":
 * the offer panel alone, with no conversation behind it. The site page owns
 * the slide-out; this only draws the panel inside it.
 */
import { useEffect } from 'react';
import { AccountHome } from './AccountHome';
import { GoDeeperPanel } from './GoDeeperPanel';

export function GetMoreFrame() {
  useEffect(() => {
    document.documentElement.classList.add('is-framed', 'is-panel-only');
  }, []);
  return (
    <div className="app-shell">
      <AccountHome />
      <GoDeeperPanel panelOnly />
    </div>
  );
}
