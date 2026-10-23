/**
 * Every word the accounts screens show. Plain sentences, short, in the voice the rest of the app
 * uses. Lines that come from the server (a refused code, a full shelf) are shown as the server wrote them.
 */
const ordinal = (n: number) => {
  const tail = n % 100;
  if (tail >= 11 && tail <= 13) return `${n}th`;
  return `${n}${({ 1: 'st', 2: 'nd', 3: 'rd' } as Record<number, string>)[n % 10] ?? 'th'}`;
};

export const accountsCopy = {
  offline: 'We could not reach the server. Please try again.',
  failed: 'That did not work. Please try again.',
  back: 'Back',
  gotIt: 'Got it',

  // In the Get more conversations panel and the more menu
  keepHeading: 'Keep your conversations',
  keepBody:
    'Signing up allows you to keep your conversation and to purchase more conversations. The tokens are held by the account, not by a code in one browser. Codes stay for anyone without an account and for sponsors.',
  signInOrUp: 'Sign in or sign up',
  menuSignIn: 'Sign in to keep this conversation',
  menuHome: 'My home',
  savedToHome: 'Saved to your home. It stays until you delete it.',

  // Sign-in steps
  addressIntro: 'One address, one code. No password.',
  addressLabel: 'Your email address',
  sendCode: 'Send me a code',
  sending: 'Sending',
  keepsAddress: 'We keep no name. Your address is kept encrypted, only to send you sign-in codes and notices about your home and your purchases.',
  comesWithYou: 'This conversation comes with you.',
  codeHeading: 'Enter your code',
  codeSent: 'If that address can receive mail, a code is on its way. It works for ten minutes.',
  codeLabel: 'The six digits from the email',
  codeSignIn: 'Sign in',
  checking: 'Checking',
  newCode: 'Send a new code',
  junkNote: 'Check the junk folder if nothing arrives. Five wrong tries and the code is spent.',
  ageHeading: 'One click before your home opens',
  ageQuestion: 'Accounts are for people who are 18 or over.',
  ageYes: 'I am 18 or over',
  ageNo: 'I am under 18',
  ageNote:
    'Your home holds your conversations, your tokens and your free allowance. It holds no name. If you lose access to this email and to the recovery code offered later, the home cannot be recovered.',
  recoveryWaiting: (day: string) => `A recovery of this account is waiting until ${day}. If this was not you, sign in with your email and cancel it.`,

  // Google and Apple, recovery
  continueWith: (name: string) => `Continue with ${name}`,
  openProvider: (name: string) => `Open ${name}`,
  providerFailed: 'That sign-in did not finish. Please try again.',
  lostEmail: 'I cannot get to my email',
  recoveryHeading: 'Get back into your account',
  recoveryIntro: 'Enter the recovery code you saved and your new email address. We send a code to the new address and tell your old one.',
  recoveryCodeLabel: 'Your recovery code',
  newAddressLabel: 'Your new email address',
  recoveryDone: (day: string) => `Done. You can sign in with your new address from ${day}. Your old address has been told.`,
  newRecoveryCode: 'Your new recovery code. We show it only once. Save it somewhere safe.',
  cancelHeading: 'Stop a recovery',
  cancelIntro: 'Did you get a notice that your account is being moved, and it was not you? Enter your email address and the cancel code from the notice.',
  cancelCodeLabel: 'Cancel code',
  cancelSend: 'Stop the recovery',
  cancelDone: 'The recovery is stopped.',

  // Confirming it is you
  confirmIntro: 'To do this, please confirm it is you. We will send a code to your email address.',
  confirmWith: (name: string) => `Confirm with ${name}`,

  // Home
  homeHeading: 'My home',
  homeNote: 'Only you see this page. It holds no name.',
  backToConversation: 'Back to the conversation',
  tokensLeft: (n: number) => `${n.toLocaleString('en-US')} tokens left`,
  freeRefill: (left: number, total: number, day: number | null) =>
    day === null ? `${left.toLocaleString('en-US')} free.` : `${left.toLocaleString('en-US')} free. They refill to ${total.toLocaleString('en-US')} on the ${ordinal(day)} of each month.`,
  codeTokens: (n: number) => `${n.toLocaleString('en-US')} tokens on your codes.`,
  freeFirst: 'Free tokens are used first.',
  getMore: 'Get more conversations',
  addCodeLink: 'Add a code to my home',
  addCodeLabel: 'Your code',
  addCode: 'Add this code',
  codeAdded: 'The code is added to your home.',
  recoveryPrompt: 'Your first conversation is saved. Set up a way back in case you lose access to your email.',
  getRecoveryCode: 'Get my recovery code',
  conversationsHeading: 'Your conversations',
  conversationsEmpty: 'Nothing is saved yet. Conversations you start while signed in are saved here.',
  conversationsLoading: 'Loading your conversations',
  conversationsNote:
    'The voice and the day, nothing from inside. Kept until you delete them, or until this home sits unused for two years. Each conversation has its own delete in the ⋯ menu.',
  opening: 'Opening',
  remove: 'Delete',
  removeSure: 'Delete this conversation for good?',
  removeYes: 'Yes, delete it',
  removeNo: 'Keep it',
  ended: 'This conversation has ended.',
  settingsHeading: 'Settings',
  changeAddress: 'Change my email address',
  changeAddressDone: 'Your email address is changed.',
  recoveryCode: 'Recovery code',
  exportData: 'Download my data',
  signOut: 'Sign out',
  signOutEverywhere: 'Sign out everywhere',
  deleteHome: 'Delete my home',

  // Recovery code
  recoveryCodeHeading: 'A way back if you lose access to your email',
  recoveryCodeIntro: 'Your email is the usual way in. This code is for the day you cannot reach it. Keep it somewhere safe.',
  recoveryCodeFresh: 'We sent a fresh sign-in code first, so no one else can take this from your screen.',
  recoveryDownload: 'Download',
  recoveryPrint: 'Print',
  recoveryLater: 'Not now. I can come back to this in Settings.',
  recoveryCodeNote:
    'We keep only a scrambled copy, so we cannot show it again. It works once, and a new one takes its place. Using it starts a short waiting period, and we tell your old email address.',
  stopRecovery: 'Stop this recovery',

  // How you sign in
  methodsHeading: 'How you sign in',
  methodName: (method: string) => ({ address: 'Email address', google: 'Google', apple: 'Apple' }[method] ?? method),
  linkMethod: (name: string) => `Add ${name}`,
  unlinkMethod: (name: string) => `Remove ${name}`,
  methodDone: 'Done.',

  // Delete my home
  deleteIntro: 'This cannot be undone. First, a fresh code, so no one else can do this from your screen.',
  deleteGoesHeading: 'What goes',
  deleteGoes:
    'Every saved conversation and its words, and the scrubbed review copy of them. Your tokens, free, gift and purchased, with no refund except in a case we agree to. The encrypted copy of your email address and the scrambled key made from it. The link between your home and your codes.',
  deleteStaysHeading: 'What stays, for a while',
  deleteStays:
    "Stripe keeps its own record of any payment. The token system keeps each code's row and its payment reference, with no name. Backups drop deleted data within 14 days. The privacy page lists everything that stays.",
  deleteYes: 'Delete everything',
  deleteNo: 'Keep my home',

  // Signed out home
  homeSignedOutHeading: 'Sign in to open your home',
  newHere: 'New here? The same steps open a new home. You do not need one to have a conversation.',
  startWithout: 'Start a conversation without signing in',
  backToSite: 'Back to the site',

  // Reopened conversation
  resourcesFirst: 'Before you read on, the Facilitator said this earlier:',
};
