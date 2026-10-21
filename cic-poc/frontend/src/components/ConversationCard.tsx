import type { WorldEntry } from '../data/worlds';
import { eraFor } from '../lib/eras';

interface ConversationCardProps {
  world: WorldEntry;
  speaking?: boolean;
}

export function ConversationCard({ world, speaking = false }: ConversationCardProps) {
  const era = eraFor(world.eraStart);
  return (
    <div className={speaking ? 'conv-card conv-card--speaking' : 'conv-card'} style={{ ['--era' as string]: era.tint }}>
      <div className="conv-card__frame">
        <div className="conv-card__inner">
          <div className="conv-card__band sans" title={`${era.no}. ${era.name}`}>
            {era.no}. {era.name}
          </div>
          <div className="conv-card__pic">
            <img src={world.portraitImage} alt="" />
          </div>
          <div className="conv-card__name">{world.representativeName}</div>
        </div>
      </div>
    </div>
  );
}
