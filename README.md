# Webapp Icon Sync

<picture>
  <img src="icon.png" width="64" height="64" alt="Preview of the app">
</picture>

My work PC Windows regularly deletes MS Edge Webapps from my Start Menu. So I made a watchdog that copies the shortcuts from the Desktop back to the Start Menu folder.

## Setup

### 1. (optional) Install a venv

    python -m venv .venv

### 2. (optional) Activate the venv

    ./.venv/Scripts/Activate.ps1

### 3. Install all packages

    pip install -r requirements.txt

## Running

There are two ways to run this:

### 1. Run as python file

    python main.py


### 2. Build as exe
#### Either use the bat

    ./build.bat

#### Or manually build it

Icons first:

    python gen-icon.py

Then run pyinstaller:

    pyinstaller --onefile --noconsole --icon icons/app.ico webapp-copy.py

## Autostart
To autostart the app build it and then run the autostart.bat file:

    ./autostart-exe.bat

Or autostart the python file:

    ./autostart-py.bat

Note that the python file will only work if the venv is activated. Either install all dependencies globally or make sure to activate the venv inside the batch file for startup.