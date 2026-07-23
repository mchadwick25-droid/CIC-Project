/**
 * The six Representative icons (Ministry/Communication/Brand-Assets/World-Icons/),
 * split into `body` (the bust, everything except the held object) and `object`
 * (the world's own held object, drawn separately so LivingTableScene can rest
 * it on the table rather than cradle it at the chest - the In-App Icons &
 * Graphics thread's own decision, a deliberate departure from the icon spec's
 * §7a "cradled at the chest" rule).
 *
 * Both `body` and `object` paths are in each icon's own local coordinate
 * space (the same raw path data as the locked master SVGs in World-Icons/,
 * viewBox "-15 15 150 150"). `objectBottomY`/`objectCenterX` locate the
 * object's own base so LivingTableScene can seat it on the rim regardless of
 * which seat position it lands in.
 *
 * Keyed by world_id (world_manifest.py) - matches what the seated World.id
 * actually is at runtime.
 */
import type { ReactNode } from 'react';

export interface WorldIconData {
  body: ReactNode;
  object: ReactNode;
  objectBottomY: number;
  objectCenterX: number;
}

export const WORLD_ICONS: Record<string, WorldIconData> = {
  'post-apostolic-house-church': {
    body: (
      <>
        <path d="M18 150 Q16 96 40 84 Q30 60 44 46 Q60 30 76 46 Q90 60 80 84 Q104 96 102 150 Z" fill="#B87A50" stroke="#2A2521" strokeWidth={2.6} strokeLinejoin="round" />
        <path d="M42 150 Q44 102 60 94 Q76 102 78 150 Z" fill="#D9CDB2" stroke="#2A2521" strokeWidth={2.2} strokeLinejoin="round" />
        <path d="M50 100 Q60 108 70 100" fill="none" stroke="#2A2521" strokeWidth={1.8} strokeLinecap="round" />
        <path d="M44 46 Q60 34 76 46 Q86 62 78 82 Q60 74 42 82 Q34 62 44 46 Z" fill="#F1E7D0" stroke="#2A2521" strokeWidth={2.2} />
        <path d="M46 58 Q46 82 60 84 Q74 82 74 58" fill="#D8B184" stroke="#2A2521" strokeWidth={2} />
        <path d="M46 58 Q60 57 74 58" fill="none" stroke="#2A2521" strokeWidth={1.4} strokeLinecap="round" />
        <ellipse cx={52.5} cy={63} rx={2.4} ry={1.5} fill="#2A2521" />
        <ellipse cx={67.5} cy={63} rx={2.4} ry={1.5} fill="#2A2521" />
        <path d="M60 66 v6" stroke="#2A2521" strokeWidth={1.8} strokeLinecap="round" />
        <path d="M55 76 q5 1.5 10 0" stroke="#2A2521" strokeWidth={1.8} fill="none" strokeLinecap="round" />
      </>
    ),
    object: (
      <>
        <path d="M50 132 h20 v6 a10 6 0 0 1 -20 0 z" fill="#2A2521" />
        <path d="M60 144 v4" stroke="#2A2521" strokeWidth={2.4} />
        <ellipse cx={60} cy={148} rx={6} ry={2} fill="#2A2521" />
      </>
    ),
    objectBottomY: 150,
    objectCenterX: 60,
  },

  'desert-monasticism': {
    body: (
      <>
        <path d="M18 150 Q14 98 34 86 Q28 56 42 44 Q52 31 60 30 Q68 31 78 44 Q92 56 86 86 Q106 98 102 150 Z" fill="#756950" stroke="#2A2521" strokeWidth={2.6} strokeLinejoin="round" />
        <path d="M46 58 Q46 82 60 84 Q74 82 74 58" fill="#A97B4A" stroke="#2A2521" strokeWidth={2} />
        <path d="M46 58 Q60 57 74 58" fill="none" stroke="#2A2521" strokeWidth={1.4} strokeLinecap="round" />
        <ellipse cx={52.5} cy={63} rx={2.4} ry={1.5} fill="#2A2521" />
        <ellipse cx={67.5} cy={63} rx={2.4} ry={1.5} fill="#2A2521" />
        <path d="M60 66 v6" stroke="#2A2521" strokeWidth={1.8} strokeLinecap="round" />
        <path d="M56.5 77 q3.5 1 7 0" fill="none" stroke="#2A2521" strokeWidth={1.5} strokeLinecap="round" />
        <path d="M45 68 Q42 102 60 122 Q78 102 75 68 Q68 83 60 82 Q52 83 45 68 Z" fill="#D9D2C4" stroke="#2A2521" strokeWidth={1.6} strokeLinejoin="round" />
      </>
    ),
    object: (
      <>
        <path d="M51 135 Q50 148 60 150 Q70 148 69 135 Q69 129 63 127 L57 127 Q51 129 51 135 Z" fill="#BC8A5E" stroke="#2A2521" strokeWidth={2.2} strokeLinejoin="round" />
        <path d="M57 127 Q56.5 124 57.5 123 L62.5 123 Q63.5 124 63 127" fill="#BC8A5E" stroke="#2A2521" strokeWidth={1.8} strokeLinejoin="round" />
        <path d="M56 123 Q60 121.5 64 123" fill="none" stroke="#2A2521" strokeWidth={1.5} strokeLinecap="round" />
        <path d="M63 128 q6 1 5 7" fill="none" stroke="#2A2521" strokeWidth={2} strokeLinecap="round" />
        <path d="M55 137 l3 2.5 l-2 3" fill="none" stroke="#2A2521" strokeWidth={1.3} strokeLinecap="round" strokeLinejoin="round" />
      </>
    ),
    objectBottomY: 150,
    objectCenterX: 60,
  },

  'alexandria-catechetical': {
    body: (
      <>
        <path d="M18 150 Q16 96 40 84 Q30 60 44 46 Q60 30 76 46 Q90 60 80 84 Q104 96 102 150 Z" fill="#EDE4CE" stroke="#2A2521" strokeWidth={2.6} strokeLinejoin="round" />
        <path d="M46 54 Q46 43 60 41 Q74 43 74 54 Q74 82 60 84 Q46 82 46 54 Z" fill="#CDA478" stroke="#2A2521" strokeWidth={2} />
        <path d="M47 46 Q60 40 73 46 Q73 43 60 39 Q47 43 47 46 Z" fill="#C7BFAE" stroke="#2A2521" strokeWidth={1.2} strokeLinejoin="round" />
        <ellipse cx={52.5} cy={63} rx={2.4} ry={1.5} fill="#2A2521" />
        <ellipse cx={67.5} cy={63} rx={2.4} ry={1.5} fill="#2A2521" />
        <path d="M60 66 v6" stroke="#2A2521" strokeWidth={1.8} strokeLinecap="round" />
        <path d="M55 76 q5 1.5 10 0" stroke="#2A2521" strokeWidth={1.8} fill="none" strokeLinecap="round" />
      </>
    ),
    object: (
      <>
        <path d="M42 124 L78 124 L78 140 L42 140 Z" fill="#EEE2C4" stroke="#2A2521" strokeWidth={1.8} strokeLinejoin="round" />
        <path d="M47 129 h26" stroke="#2A2521" strokeWidth={1.1} strokeLinecap="round" />
        <path d="M47 133 h26" stroke="#2A2521" strokeWidth={1.1} strokeLinecap="round" />
        <path d="M47 137 h20" stroke="#2A2521" strokeWidth={1.1} strokeLinecap="round" />
        <rect x={37} y={120} width={6} height={26} rx={3} fill="#9A7248" stroke="#2A2521" strokeWidth={1.4} />
        <rect x={77} y={120} width={6} height={26} rx={3} fill="#9A7248" stroke="#2A2521" strokeWidth={1.4} />
        <circle cx={40} cy={120} r={3.4} fill="#7E5A34" stroke="#2A2521" strokeWidth={1.2} />
        <circle cx={40} cy={146} r={3.4} fill="#7E5A34" stroke="#2A2521" strokeWidth={1.2} />
        <circle cx={80} cy={120} r={3.4} fill="#7E5A34" stroke="#2A2521" strokeWidth={1.2} />
        <circle cx={80} cy={146} r={3.4} fill="#7E5A34" stroke="#2A2521" strokeWidth={1.2} />
      </>
    ),
    objectBottomY: 149.4,
    objectCenterX: 60,
  },

  'syriac-edessa-nisibis': {
    body: (
      <>
        <path d="M18 150 Q16 96 40 84 Q30 60 44 46 Q60 30 76 46 Q90 60 80 84 Q104 96 102 150 Z" fill="#9C6350" stroke="#2A2521" strokeWidth={2.6} strokeLinejoin="round" />
        <path d="M46 54 Q46 43 60 41 Q74 43 74 54 Q74 82 60 84 Q46 82 46 54 Z" fill="#B58A5A" stroke="#2A2521" strokeWidth={2} />
        <path d="M47 46 Q60 40 73 46 Q73 43 60 39 Q47 43 47 46 Z" fill="#3A2E22" stroke="#2A2521" strokeWidth={1.2} strokeLinejoin="round" />
        <ellipse cx={52.5} cy={63} rx={2.4} ry={1.5} fill="#2A2521" />
        <ellipse cx={67.5} cy={63} rx={2.4} ry={1.5} fill="#2A2521" />
        <path d="M60 66 v6" stroke="#2A2521" strokeWidth={1.8} strokeLinecap="round" />
        <path d="M56.5 76 q3.5 1 7 0" stroke="#2A2521" strokeWidth={1.5} fill="none" strokeLinecap="round" />
        <path d="M46 69 Q44 98 60 114 Q76 98 74 69 Q68 82 60 81 Q52 82 46 69 Z" fill="#3A2E22" stroke="#2A2521" strokeWidth={1.6} strokeLinejoin="round" />
      </>
    ),
    object: (
      <>
        <rect x={52} y={119} width={20} height={27} rx={1.5} fill="#E8DCBF" stroke="#2A2521" strokeWidth={1.3} />
        <rect x={49} y={116} width={20} height={27} rx={2} fill="#6E4A2E" stroke="#2A2521" strokeWidth={1.8} />
        <path d="M53 117 v25" stroke="#3A2718" strokeWidth={1.3} strokeLinecap="round" />
        <rect x={56} y={121} width={9} height={17} rx={1} fill="none" stroke="#2A2521" strokeWidth={0.9} strokeOpacity={0.45} />
      </>
    ),
    objectBottomY: 146,
    objectCenterX: 60,
  },

  'hieronymian-ascetic-literary': {
    body: (
      <>
        <path d="M18 150 Q16 96 40 84 Q30 60 44 46 Q60 30 76 46 Q90 60 80 84 Q104 96 102 150 Z" fill="#A99B7E" stroke="#2A2521" strokeWidth={2.6} strokeLinejoin="round" />
        <path d="M42 150 Q44 102 60 94 Q76 102 78 150 Z" fill="#D9CDB2" stroke="#2A2521" strokeWidth={2.2} strokeLinejoin="round" />
        <path d="M50 100 Q60 108 70 100" fill="none" stroke="#8F805E" strokeWidth={1.8} strokeLinecap="round" />
        <path d="M46 54 Q46 43 60 41 Q74 43 74 54 Q74 82 60 84 Q46 82 46 54 Z" fill="#E5C6A0" stroke="#2A2521" strokeWidth={2} />
        <path d="M46 51 Q47 54 51 52 Q56 47 58 47 Q66 58 74 50 Q75 44 66 41 Q58 40 52 41 Q47 42 46 51 Z" fill="#C4BCA8" stroke="#2A2521" strokeWidth={1.2} strokeLinejoin="round" />
        <path d="M54 42 q2 2 1 4" fill="none" stroke="#2A2521" strokeWidth={1} strokeOpacity={0.5} strokeLinecap="round" />
        <ellipse cx={52.5} cy={63} rx={2.4} ry={1.5} fill="#2A2521" />
        <ellipse cx={67.5} cy={63} rx={2.4} ry={1.5} fill="#2A2521" />
        <path d="M60 66 v6" stroke="#2A2521" strokeWidth={1.8} strokeLinecap="round" />
        <path d="M55 76 q5 1.5 10 0" stroke="#2A2521" strokeWidth={1.8} fill="none" strokeLinecap="round" />
      </>
    ),
    object: (
      <>
        <rect x={48} y={127} width={24} height={19} rx={2} fill="#9A7248" stroke="#2A2521" strokeWidth={1.8} />
        <rect x={51} y={130} width={18} height={13} rx={1} fill="#4A3B2A" stroke="#2A2521" strokeWidth={1.2} />
        <path d="M54 134 h12" stroke="#B6A784" strokeWidth={0.9} strokeOpacity={0.7} strokeLinecap="round" />
        <path d="M54 138 h9" stroke="#B6A784" strokeWidth={0.9} strokeOpacity={0.7} strokeLinecap="round" />
        <path d="M76 120 L66 134" stroke="#7A6544" strokeWidth={2.4} strokeLinecap="round" />
        <circle cx={76.5} cy={119.5} r={2.1} fill="#7A6544" stroke="#2A2521" strokeWidth={1} />
      </>
    ),
    objectBottomY: 146,
    objectCenterX: 60,
  },

  'imperial-juridical-christianity': {
    body: (
      <>
        <path d="M18 150 Q16 96 40 84 Q30 60 44 46 Q60 30 76 46 Q90 60 80 84 Q104 96 102 150 Z" fill="#7A2E2E" stroke="#2A2521" strokeWidth={2.6} strokeLinejoin="round" />
        <path d="M46 54 Q46 43 60 41 Q74 43 74 54 Q74 82 60 84 Q46 82 46 54 Z" fill="#D6B48A" stroke="#2A2521" strokeWidth={2} />
        <path d="M47 46 Q60 40 73 46 Q73 43 60 39 Q47 43 47 46 Z" fill="#3A2E22" stroke="#2A2521" strokeWidth={1.2} strokeLinejoin="round" />
        <ellipse cx={52.5} cy={63} rx={2.4} ry={1.5} fill="#2A2521" />
        <ellipse cx={67.5} cy={63} rx={2.4} ry={1.5} fill="#2A2521" />
        <path d="M60 66 v6" stroke="#2A2521" strokeWidth={1.8} strokeLinecap="round" />
        <path d="M55 76 q5 1.5 10 0" stroke="#2A2521" strokeWidth={1.8} fill="none" strokeLinecap="round" />
        <path d="M33 88 Q56 112 78 136" fill="none" stroke="#2A2521" strokeWidth={9} strokeLinecap="butt" />
        <path d="M33 88 Q56 112 78 136" fill="none" stroke="#E8DCBF" strokeWidth={6.5} strokeLinecap="butt" />
        <path d="M34 140 Q58 105 84 88" fill="none" stroke="#2A2521" strokeWidth={6.5} strokeLinecap="round" />
        <path d="M34 140 Q58 105 84 88" fill="none" stroke="#5A3D24" strokeWidth={4.5} strokeLinecap="round" />
      </>
    ),
    object: (
      <>
        <ellipse cx={60} cy={112} rx={7} ry={3} fill="#7E5A34" stroke="#2A2521" strokeWidth={1.4} />
        <rect x={53} y={112} width={14} height={34} rx={6} fill="#6E4A2E" stroke="#2A2521" strokeWidth={1.8} />
        <path d="M53 122 q-5 3 0 7" fill="none" stroke="#2A2521" strokeWidth={1.3} strokeLinecap="round" />
      </>
    ),
    objectBottomY: 146,
    objectCenterX: 60,
  },
};
