@echo off

echo Installing Desktop Shortcut Sync to Windows startup...

set EXE_PATH=%~dp0dist\webapp-copy.exe
set STARTUP=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup

if not exist "%EXE_PATH%" (
    echo ERROR: EXE not found at %EXE_PATH%
    pause
    exit /b
)

copy "%EXE_PATH%" "%STARTUP%" /Y

echo.
echo Installed successfully.
echo The app will start automatically with Windows.
pause