@echo off

echo  Building App

REM activate venv if it exists
if exist ".venv\Scripts\activate.bat" (
    call .venv\Scripts\activate.bat
)

echo.
echo Generating icons...
python gen-icon.py

if errorlevel 1 (
    echo Icon generation failed
    pause
    exit /b
)

echo.
echo Building EXE...

pyinstaller ^
 --onefile ^
 --noconsole ^
 --name webapp-copy ^
 --icon icons\app.ico ^
 main.py

if errorlevel 1 (
    echo Build failed
    pause
    exit /b
)

echo.
echo Build complete

pause