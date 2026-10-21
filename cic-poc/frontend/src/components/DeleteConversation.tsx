import { useState } from 'react';

interface DeleteConversationProps {
  onDelete: () => Promise<void>;
  onCancel: () => void;
}

// The participant's own deletion request, asked once before it is done.
export function DeleteConversation({ onDelete, onCancel }: DeleteConversationProps) {
  const [deleting, setDeleting] = useState(false);
  const [failed, setFailed] = useState(false);

  const confirm = async () => {
    setDeleting(true);
    setFailed(false);
    try {
      await onDelete();
    } catch {
      setFailed(true);
      setDeleting(false);
    }
  };

  return (
    <div className="delete-conversation delete-conversation--confirm sans" role="alertdialog" aria-labelledby="delete-conversation-title">
      <p id="delete-conversation-title" className="delete-conversation__title">Delete this conversation?</p>
      <p>It is removed now and cannot be recovered. Copies in our daily backups are gone within 14 days.</p>
      {failed && <p role="alert">Something went wrong and nothing was deleted. Please try again.</p>}
      <div className="delete-conversation__actions">
        <button type="button" className="delete-conversation__delete" disabled={deleting} onClick={confirm}>
          Delete
        </button>
        <button type="button" className="delete-conversation__keep" autoFocus disabled={deleting} onClick={onCancel}>
          Keep it
        </button>
      </div>
    </div>
  );
}

export function DeletedNotice({ onRestart, restartLabel }: { onRestart: () => void; restartLabel: string }) {
  return (
    <div className="conversation__composer">
      <p className="conversation__bar-note sans" role="status" style={{ marginBottom: 'var(--spacing-sm)' }}>
        The conversation has been deleted.
      </p>
      <button type="button" className="doorway__begin" onClick={onRestart}>
        {restartLabel}
      </button>
    </div>
  );
}
