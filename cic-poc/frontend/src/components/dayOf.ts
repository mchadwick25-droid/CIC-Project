export function dayOf(iso: string | null): string {
  if (!iso) return '';
  const date = new Date(`${iso.slice(0, 10)}T12:00:00Z`);
  return Number.isNaN(date.getTime()) ? iso.slice(0, 10) : date.toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric', timeZone: 'UTC' });
}
