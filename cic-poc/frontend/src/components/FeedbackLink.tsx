const FEEDBACK_FORM_URL = 'https://tally.so/r/PdMgbd';

export function FeedbackLink() {
  return (
    <a
      className="conversation__bar-note conversation__bar-link sans"
      href={FEEDBACK_FORM_URL}
      target="_blank"
      rel="noopener noreferrer"
    >
      Tell us what you found
    </a>
  );
}
