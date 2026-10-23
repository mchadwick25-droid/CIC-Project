import { useRef, useState, type ReactNode } from 'react';
import { ConversationMenu } from './ConversationMenu';
import { DeleteConversation } from './DeleteConversation';
import { ExperienceFeedbackCard } from './ExperienceFeedback';
import { AccountPanel } from './AccountPanel';
import { GoDeeperPanel } from './GoDeeperPanel';
import { ReportCard } from './PageFeedback';

type Panel = 'about' | 'feedback' | 'report' | 'delete' | null;

interface ConversationChromeProps {
  title: string;
  aboutLabel: string;
  about: ReactNode;
  feedbackPage: string;
  reportPage: string | null;
  onLeave: () => void;
  onDelete?: () => Promise<void>;
}

/** The slim bar, the token ribbon and the panels the more-menu opens, above the cards. */
export function ConversationChrome({ title, aboutLabel, about, feedbackPage, reportPage, onLeave, onDelete }: ConversationChromeProps) {
  const [panel, setPanel] = useState<Panel>(null);
  const [thanks, setThanks] = useState(false);
  const menuRef = useRef<HTMLButtonElement>(null);

  const open = (next: Panel) => () => {
    setThanks(false);
    setPanel(next);
  };
  const close = () => {
    setPanel(null);
    menuRef.current?.focus();
  };

  return (
    <>
      <div className="conversation__bar">
        <span className="conversation__title sans">{title}</span>
        <ConversationMenu
          buttonRef={menuRef}
          aboutLabel={aboutLabel}
          onAbout={open('about')}
          onFeedback={open('feedback')}
          onReport={reportPage ? open('report') : undefined}
          onLeave={onLeave}
          onDelete={onDelete ? open('delete') : undefined}
        />
      </div>
      <AccountPanel />
      <GoDeeperPanel />
      {panel === 'about' && (
        <div className="conversation__panel">
          {about}
          <button type="button" className="conversation__panel-close sans" autoFocus onClick={close}>
            Back to the conversation
          </button>
        </div>
      )}
      {panel === 'feedback' && <ExperienceFeedbackCard page={feedbackPage} onClose={close} />}
      {panel === 'report' && reportPage && (
        <div className="conversation__panel page-feedback sans">
          <ReportCard
            page={reportPage}
            onCancel={close}
            onSent={() => {
              close();
              setThanks(true);
            }}
          />
        </div>
      )}
      {panel === 'delete' && onDelete && (
        <div className="conversation__panel">
          <DeleteConversation onDelete={onDelete} onCancel={close} />
        </div>
      )}
      <p className="feedback-card__thanks sans" role="status">
        {thanks ? 'Thank you. A person will read it.' : ''}
      </p>
    </>
  );
}
