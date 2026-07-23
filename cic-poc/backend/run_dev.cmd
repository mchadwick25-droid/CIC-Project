@echo off
cd /d "%~dp0"

REM Pre-flight port check -- see check_port_free.ps1 for why this exists
REM (a real, reproduced Windows hazard: a second uvicorn can silently bind
REM the same port and receive zero traffic instead of erroring).
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0check_port_free.ps1" -Port 8000
if errorlevel 1 exit /b 1

"venv\Scripts\python.exe" -m uvicorn app.main:app --reload
