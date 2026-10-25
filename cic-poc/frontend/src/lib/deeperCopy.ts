export const deeperCopy = {
  heading: 'Get more conversations',
  introHeld: 'Tokens pay for each new conversation and each round. Add more any time. Your conversation stays open.',
  intro: 'Every conversation starts free. You have 550 free tokens every 30 days: 50 to launch a new conversation, 20 to 25 for each question.',
  open: 'Get more conversations',
  close: 'Close',
  getMore: 'Get more conversations',
  haveCode: 'I have a code',
  low: 'Your tokens are running low.',
  fieldLabel: 'Your code',
  useCode: 'Use this code',
  saved: 'Code saved on this device.',
  removeCode: 'Remove code',
  badCode: "That doesn't look like a code. Check it and try again.",
  claimAsk: 'A code came with this link. Use it?',
  claimReplace: 'You already have a code. This one will be added to it.',
  claimUse: 'Use it',
  claimLater: 'Not now',
  claimFailed: "We couldn't get that code. Try the page where you paid.",
  giveEyebrow: 'Help others take part',
  giveHeading: 'Keep the door open for others',
  giveBody:
    'Free conversations are limited, and gifts keep them open. Every gift goes to the Accessibility Fund. It helps more people, in more languages, explore more Christian traditions.',
  giveOnce: 'Give once',
  giveMonthly: 'Give monthly',
  giveFine:
    'Church in Conversation is part of Faithways Studio, Inc., a Colorado public benefit corporation \u2014 not a nonprofit. Contributions are not tax-deductible. Both go through Stripe.',
  showCode: 'Show my code',
  hideCode: 'Hide my code',
  yourCode: (code: string) => `Your code is ${code}. Keep it safe. Enter it on another device to use your tokens there.`,
  left: (n: number) => `${n.toLocaleString('en-US')} tokens left`,
  balance: (n: number) => `${n.toLocaleString('en-US')} tokens left.`,
  freeLeft: (n: number) => `${n.toLocaleString('en-US')} free tokens left.`,
};

export const pilotCopy = {
  group: 'Free pilot pack',
  joining: 'Getting your free pack.',
  readyHeading: 'Your free pack is ready',
  ready: (tokens: number, conversations: number) =>
    `You have ${tokens.toLocaleString('en-US')} tokens, about ${conversations} conversations. They are saved in this browser, so there is nothing to copy.`,
  start: 'Start a conversation',
  already: 'You have joined the pilot. Your pack is in this browser.',
  full: 'The pilot is full. Thank you for your interest.',
  ended: 'The pilot has ended. Thank you.',
  addressLimit: 'This connection has already taken the free packs the pilot allows.',
  failed: "We couldn't get your pack. Try again from the pilot page.",
};

export const askAgainCopy = {
  body: 'You asked this earlier in this conversation. Ask it again? It will use tokens.',
  bodyFree: 'You asked this earlier in this conversation. Ask it again?',
  ask: 'Ask again',
  decline: "Don't ask",
};
