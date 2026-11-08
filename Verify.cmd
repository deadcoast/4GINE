@echo off
if not exist "%~dp0.venv\Scripts\python.exe" (
  echo ERROR: Local Python is missing. Run Bootstrap.cmd first.
  exit /b 1
)
"%~dp0.venv\Scripts\python.exe" "%~dp0scripts\verify.py" %*
exit /b %errorlevel%
