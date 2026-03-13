@echo off

echo Installing Desktop Shortcut Sync to Windows startup...

set PY_PATH=%~dp0main.py
set STARTUP=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup

if not exist "%PY_PATH%" (
    echo ERROR: Python script not found at %PY_PATH%
    pause
    exit /b
)

copy "%PY_PATH%" "%STARTUP%" /Y

echo.
echo Installed successfully.
echo The app will start automatically with Windows as long as Python is installed.
pause