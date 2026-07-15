/**
 * RefreshWarningBanner - small persistent reminder shown during an active
 * conversation.
 *
 * Pulled out of the main onboarding text on purpose (see OnboardingScreen's
 * own note, per Ministry/Operations/CiC_Prototype_Testing_Pilot_Plan_DRAFT_
 * V0_1.md Section 3): a tester needs to remember this *during* the
 * conversation, not just once before it starts, since sessions aren't
 * persistent - a refresh or dropped connection loses the conversation with
 * no recovery.
 */

export function RefreshWarningBanner() {
  return (
    <div className="refresh-warning-banner">
      Known limitation: refreshing this page or losing connection will lose your conversation. Stay in this one tab.
    </div>
  );
}
