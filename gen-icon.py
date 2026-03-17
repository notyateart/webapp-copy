from pathlib import Path
from PIL import Image
import shutil

BASE = Path(__file__).parent

SOURCE = BASE / "icon.png"
ICON_DIR = BASE / "icons"

ICON_DIR.mkdir(exist_ok=True)

TRAY = ICON_DIR / "tray.png"
ICO = ICON_DIR / "app.ico"

# copy tray icon
shutil.copy2(SOURCE, TRAY)

# build exe icon
img = Image.open(SOURCE)

img.save(
    ICO,
    format="ICO",
    sizes=[
        (16,16),
        (32,32),
        (48,48),
        (64,64),
        (128,128),
        (256,256)
    ]
)

print("Icons generated in:", ICON_DIR)