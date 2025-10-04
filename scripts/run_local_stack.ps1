# FILE: scripts\run_local_stack.ps1

$ErrorActionPreference = "Stop"

# --- 0) Vars ---------------------------------------------------------------
$ROOT = "D:\whisper-laced"
$env:PYTHONPATH = $ROOT
$env:DATABASE_URL = "sqlite:///D:/whisper-laced/backend/db.sqlite3"
$env:SECRET_KEY   = "THIS_IS_MY_ONE_FIXED_SECRET_ChangeMe_NOW"

# --- 1) Install Memurai (Redis for Windows) if missing ---------------------
function Ensure-Memurai {
  try {
    Get-Service memurai | Out-Null
    Write-Host "[OK] Memurai service already present."
  } catch {
    Write-Host "[INFO] Installing Memurai via winget..."
    try {
      winget install -e --id Memurai.MemuraiDeveloper --accept-package-agreements --accept-source-agreements
    } catch {
      $item = winget search memurai | Select-String -Pattern "Memurai" | Select-Object -First 1
      if (-not $item) { throw "Could not find Memurai in winget search." }
      $id = ($item -split '\s{2,}')[0].Trim()
      if (-not $id) { throw "Could not parse Memurai ID from winget." }
      winget install -e --id $id --accept-package-agreements --accept-source-agreements
    }
  }
}

Ensure-Memurai

# --- 2) Start Memurai (Redis) ----------------------------------------------
try { Start-Service memurai } catch {}
try { Set-Service memurai -StartupType Automatic | Out-Null } catch {}
Write-Host "[OK] Memurai started (Redis @ 127.0.0.1:6379)."

# --- 3) Kill anything holding port 5000 (old uvicorn) ----------------------
$net = (netstat -ano | Select-String ":5000\s+LISTENING") | ForEach-Object {
  ($_ -replace '.*\s(\d+)$','$1')
} | Where-Object { $_ -match '^\d+$' } | Select-Object -Unique
if ($net) {
  Write-Host "[INFO] Killing PID(s) on :5000 -> $($net -join ', ')"
  $net | ForEach-Object { try { taskkill /PID $_ /F | Out-Null } catch {} }
}

# --- 4) Init DB (safe to re-run) ------------------------------------------
Write-Host "[INFO] Ensuring DB schema..."
python -m backend.scripts.init_db

# --- 5) Start API (window 1) ----------------------------------------------
Write-Host "[INFO] Starting API on http://127.0.0.1:5000 ..."
Start-Process powershell -ArgumentList @(
  "-NoExit","-Command",
  "Set-Location `"$ROOT`";",
  "`$env:DATABASE_URL='$env:DATABASE_URL'; `$env:SECRET_KEY='$env:SECRET_KEY';",
  "python -m uvicorn backend.app.main:app --host 127.0.0.1 --port 5000 --reload"
)

# --- 6) Start Celery worker (window 2) -------------------------------------
Write-Host "[INFO] Starting Celery worker (solo pool) ..."
Start-Process powershell -ArgumentList @(
  "-NoExit","-Command",
  "Set-Location `"$ROOT`";",
  "`$env:PYTHONPATH='$ROOT'; `$env:SECRET_KEY='$env:SECRET_KEY';",
  "python -m celery -A backend.celery_app worker -P solo -l info"
)

# --- 7) Quick smoke for Phase 10 (window 3) --------------------------------
if (Test-Path "$ROOT\scripts\smoke_phase10.ps1") {
  Write-Host "[INFO] Launching phase-10 smoke..."
  Start-Process powershell -ArgumentList @(
    "-NoExit","-Command",
    "Set-Location `"$ROOT`"; .\scripts\smoke_phase10.ps1"
  )
} else {
  Write-Host "[WARN] scripts\smoke_phase10.ps1 not found; skipping auto-smoke."
}

# --- 8) Queue a couple Celery jobs (window 4) ------------------------------
Write-Host "[INFO] Queueing demo batch_generate tasks..."
Start-Process powershell -ArgumentList @(
  "-NoExit","-Command",
  "Set-Location `"$ROOT`";",
  "`$env:PYTHONPATH='$ROOT'; `$env:SECRET_KEY='$env:SECRET_KEY';",
  "python -m backend.scripts.batch_generate `"a scented candle`" `"a lace pattern`""
)

Write-Host "`nALL SET:"
Write-Host " - API window: uvicorn running on :5000"
Write-Host " - Worker window: Celery connected to Redis (Memurai)"
Write-Host " - Smoke window: Phase 10 checks"
Write-Host " - Batch window: queued demo tasks"
