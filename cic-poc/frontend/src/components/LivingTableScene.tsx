/**
 * The Living Table scene - the seated-Representatives visual (In-App Icons &
 * Graphics thread). One SVG per seat count (1-3, Phase 1's cap), each
 * figure's bust drawn first, the table rim drawn over it (hides the flat
 * seating edge), then each world's own held object rested on the rim in
 * front of its figure, then nameplates - which invert to nameplate--speaking
 * for whichever representative is currently talking.
 *
 * Every number below (ellipse geometry, the 12-unit body/rim overlap, the
 * 3-unit object/rim clearance, the 0.9 object-to-figure scale ratio) is
 * carried over from the mockup built and tuned live in that thread, not
 * re-derived here - see the mockup's own verification notes for why each
 * value is what it is.
 */
import { WORLD_ICONS } from '../data/worldIcons';
import type { World } from '../types/conversation';

interface Ellipse {
  cx: number;
  cy: number;
  rx: number;
  ry: number;
  strokeWidth: number;
}

interface TableLayout {
  viewBoxWidth: number;
  viewBoxHeight: number;
  ellipse: Ellipse;
  seatCenters: number[];
  nameplateWidth: number;
}

const LAYOUTS: Record<number, TableLayout> = {
  1: {
    viewBoxWidth: 460,
    viewBoxHeight: 175,
    ellipse: { cx: 230, cy: 180.5, rx: 160, ry: 50, strokeWidth: 11 },
    seatCenters: [230],
    nameplateWidth: 140,
  },
  2: {
    viewBoxWidth: 700,
    viewBoxHeight: 200,
    ellipse: { cx: 350, cy: 203, rx: 150, ry: 50, strokeWidth: 11 },
    seatCenters: [290, 410],
    nameplateWidth: 100,
  },
  3: {
    viewBoxWidth: 800,
    viewBoxHeight: 180,
    ellipse: { cx: 400, cy: 185.5, rx: 340, ry: 55, strokeWidth: 14 },
    seatCenters: [210, 400, 590],
    nameplateWidth: 130,
  },
};

// Every icon shares this bust-bottom and bust-center convention (World-Icons
// asset spec §2/§7a) - true whether the silhouette is round-domed or, like
// Papnoute's cowl, a different shape entirely.
const FLAT_BOTTOM_LOCAL = 150;
const BUST_CENTER_LOCAL = 60;

const FIGURE_SCALE = 0.95;
const OBJECT_SCALE = FIGURE_SCALE * 0.9;
const BODY_RIM_OVERLAP = 12;
const OBJECT_RIM_CLEARANCE = 3;
const NAMEPLATE_GAP = 2.5;
const NAMEPLATE_HEIGHT = 22;

function rimTopAt(x: number, ellipse: Ellipse): number {
  const ratio = (x - ellipse.cx) / ellipse.rx;
  return ellipse.cy - ellipse.ry * Math.sqrt(Math.max(0, 1 - ratio * ratio));
}

// Same speaker-key convention TheTable.tsx already uses for lexicon lookups
// (message.name lowercased, spaces to underscores) - kept identical so a
// single derived value works for both.
export function speakerKeyFor(world: World): string {
  return world.representative.name.toLowerCase().replace(/ /g, '_');
}

interface SeatGeometry {
  world: World;
  centerX: number;
  figureX: number;
  figureY: number;
  objectX: number;
  objectY: number;
  nameplateX: number;
  nameplateY: number;
}

function computeSeats(worlds: World[], layout: TableLayout): SeatGeometry[] {
  return worlds.map((world, i) => {
    const centerX = layout.seatCenters[i];
    const rimTop = rimTopAt(centerX, layout.ellipse);
    const figureY = rimTop + BODY_RIM_OVERLAP - FLAT_BOTTOM_LOCAL * FIGURE_SCALE;
    const flatBottom = figureY + FLAT_BOTTOM_LOCAL * FIGURE_SCALE;

    const icon = WORLD_ICONS[world.id];
    const objectTargetBottom = rimTop + OBJECT_RIM_CLEARANCE;
    const objectY = icon ? objectTargetBottom - icon.objectBottomY * OBJECT_SCALE : 0;
    const objectX = icon ? centerX - icon.objectCenterX * OBJECT_SCALE : centerX;

    return {
      world,
      centerX,
      figureX: centerX - BUST_CENTER_LOCAL * FIGURE_SCALE,
      figureY,
      objectX,
      objectY,
      nameplateX: centerX - layout.nameplateWidth / 2,
      nameplateY: flatBottom + NAMEPLATE_GAP,
    };
  });
}

export interface LivingTableSceneProps {
  /** 1-3 seated worlds, in seat order. */
  worlds: World[];
  /** speakerKeyFor() of whoever is currently talking, or null if no one is. */
  speakingKey: string | null;
}

export function LivingTableScene({ worlds, speakingKey }: LivingTableSceneProps) {
  const layout = LAYOUTS[worlds.length];
  if (!layout) return null;

  const seats = computeSeats(worlds, layout);

  return (
    <svg
      className="living-table-scene"
      viewBox={`0 0 ${layout.viewBoxWidth} ${layout.viewBoxHeight}`}
      role="img"
      aria-label={`${worlds.map((w) => w.representative.name).join(', ')} seated at the table.`}
    >
      {seats.map(({ world, figureX, figureY }) => {
        const icon = WORLD_ICONS[world.id];
        if (!icon) return null;
        return (
          <g key={world.id} transform={`translate(${figureX},${figureY}) scale(${FIGURE_SCALE})`}>
            {icon.body}
          </g>
        );
      })}

      <ellipse
        cx={layout.ellipse.cx}
        cy={layout.ellipse.cy}
        rx={layout.ellipse.rx}
        ry={layout.ellipse.ry}
        fill="var(--color-tabletop)"
        stroke="var(--color-wood)"
        strokeWidth={layout.ellipse.strokeWidth}
      />

      {seats.map(({ world, objectX, objectY }) => {
        const icon = WORLD_ICONS[world.id];
        if (!icon) return null;
        return (
          <g key={`${world.id}-object`} transform={`translate(${objectX},${objectY}) scale(${OBJECT_SCALE})`}>
            {icon.object}
          </g>
        );
      })}

      {seats.map(({ world, nameplateX, nameplateY }) => {
        const isSpeaking = speakingKey !== null && speakerKeyFor(world) === speakingKey;
        return (
          <foreignObject
            key={`${world.id}-nameplate`}
            x={nameplateX}
            y={nameplateY}
            width={layout.nameplateWidth}
            height={NAMEPLATE_HEIGHT}
          >
            <div style={{ width: '100%', textAlign: 'center' }}>
              <span className={`nameplate${isSpeaking ? ' nameplate--speaking' : ''}`}>
                {world.representative.name}
              </span>
            </div>
          </foreignObject>
        );
      })}
    </svg>
  );
}
