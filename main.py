import os
import shutil
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import pystray
from PIL import Image, ImageDraw
import threading

DESKTOP = Path(os.path.join(os.environ["USERPROFILE"], "Desktop"))
STARTMENU = Path(os.environ["APPDATA"]) / r"Microsoft\Windows\Start Menu\Programs"


def sync_shortcuts():
    for file in DESKTOP.glob("*.lnk"):
        target = STARTMENU / file.name
        try:
            shutil.copy2(file, target)
        except Exception as e:
            print("Sync error:", e)


class DesktopHandler(FileSystemEventHandler):

    def process(self, path):
        if path.endswith(".lnk"):
            src = Path(path)
            target = STARTMENU / src.name
            try:
                shutil.copy2(src, target)
            except Exception as e:
                print("Copy error:", e)

    def on_created(self, event):
        if not event.is_directory:
            self.process(event.src_path)

    def on_modified(self, event):
        if not event.is_directory:
            self.process(event.src_path)

    def on_moved(self, event):
        if not event.is_directory:
            self.process(event.dest_path)


def start_watcher():
    event_handler = DesktopHandler()
    observer = Observer()
    observer.schedule(event_handler, str(DESKTOP), recursive=False)
    observer.start()
    return observer


def create_icon():
    icon_path = Path(__file__).parent / "icons" / "tray.png"
    return Image.open(icon_path)


def sync_action(icon, item):
    sync_shortcuts()


def quit_action(icon, item):
    icon.stop()
    os._exit(0)


def run_tray():
    icon = pystray.Icon(
        "Shortcut Sync",
        create_icon(),
        "Desktop → Start Menu Sync",
        menu=pystray.Menu(
            pystray.MenuItem("Sync now", sync_action),
            pystray.MenuItem("Quit", quit_action),
        ),
    )

    icon.run()


if __name__ == "__main__":
    sync_shortcuts()
    observer = start_watcher()

    tray_thread = threading.Thread(target=run_tray)
    tray_thread.start()