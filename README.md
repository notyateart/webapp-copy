# Webapp copy
My windows regularly deletes MS Edge Webapps from my Start Menu. So I made a watchdog that copies the shortcuts from the Desktop back to the Start Folder.

There are two ways to run this:

### 1. Run as python file

    python main.py


### 2. Build as exe
####

    python gen-icon.py

#### Install as exe

    pyinstaller --onefile --noconsole --icon icons/app.ico webapp-copy.py