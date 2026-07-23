# Pre-flight port check for run_dev.cmd.
#
# Windows lets a second process bind and LISTEN on a port that's already in
# use (uvicorn sets SO_REUSEADDR unconditionally, and Windows' SO_REUSEADDR
# semantics allow simultaneous dual-bind, unlike Linux). Confirmed by direct
# reproduction 2026-07-22: the second listener prints its normal "Uvicorn
# running on ..." banner and looks completely healthy, but receives ZERO
# real traffic -- every connection silently goes to whichever process bound
# first, for as long as that process lives, even after it should logically
# have been replaced. If that stale first process is left over from an
# earlier/unrelated session, every request sent to what looks like a fresh
# server is actually answered by whatever the stale one is doing instead.
# This is the leading candidate explanation for the unreproduced 2026-07-20
# content-isolation incident (System Hub Decision Log, 2026-07-20).
param(
    [int]$Port = 8000
)

$conns = Get-NetTCPConnection -LocalPort $Port -State Listen -ErrorAction SilentlyContinue

if (-not $conns) {
    exit 0
}

$procs = $conns | ForEach-Object {
    $p = Get-Process -Id $_.OwningProcess -ErrorAction SilentlyContinue
    if ($p) { "$($p.ProcessName) (PID $($p.Id))" }
} | Select-Object -Unique

Write-Host ""
Write-Host "[run_dev] Port $Port is already in use by: $($procs -join ', ')" -ForegroundColor Red
Write-Host "[run_dev] Starting anyway would silently bind alongside it -- this NEW server would receive ZERO real traffic; the old process answers every request instead." -ForegroundColor Red
Write-Host "[run_dev] Stop it first (taskkill /PID <pid> /F for each PID above), then re-run this script." -ForegroundColor Red
exit 1
