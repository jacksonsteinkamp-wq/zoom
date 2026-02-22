import ctypes
from ctypes import wintypes
import time
import keyboard

# Windows Magnification API (NEEDED HELP FROM CHATGPT)
magnification = ctypes.WinDLL("Magnification.dll")
user32 = ctypes.windll.user32
magnification.MagInitialize.restype = wintypes.BOOL
magnification.MagUninitialize.restype = wintypes.BOOL
magnification.MagSetFullscreenTransform.argtypes = [wintypes.FLOAT,wintypes.INT,wintypes.INT]
magnification.MagSetFullscreenTransform.restype = wintypes.BOOL

# Screen size (NEEDED HELP FROM CHATGPT)
SCREEN_WIDTH = user32.GetSystemMetrics(0)
SCREEN_HEIGHT = user32.GetSystemMetrics(1)

def initialize_magnifier(): #(NEEDED HELP FROM CHATGPT)
    if not magnification.MagInitialize():
        raise RuntimeError("Failed to initialize magnifier")
    
#WHERE MY CODE STARTS

def set_centered_zoom(zoom_level: float):
    #Centers fullscreen magnifier regardless of resolution.
    visible_width = SCREEN_WIDTH / zoom_level
    visible_height = SCREEN_HEIGHT / zoom_level
    offset_x = int((SCREEN_WIDTH - visible_width) / 2)
    offset_y = int((SCREEN_HEIGHT - visible_height) / 2)
    magnification.MagSetFullscreenTransform(zoom_level, offset_x, offset_y)

def reset_zoom():
    magnification.MagSetFullscreenTransform(1.0, 0, 0)

def main():
    initialize_magnifier()
    print("Magnifier at 100%")
    zoom_level = 1.0
    while True:
        # 4x zoom on 'F5' key
        if keyboard.is_pressed("F5"):
                zoom_level = 4.0
                set_centered_zoom(zoom_level)
                print("Magnifier set to 400%")

        # 2x zoom on 'p' key
        elif keyboard.is_pressed("p"):
                zoom_level = 2.0
                set_centered_zoom(zoom_level)
                print("Magnifier set to 200%")
                    
        # reset when nothing held
        else:
            if zoom_level != 1.0:
                zoom_level = 1.0
                reset_zoom()
                print("Magnifier reset to 100%")

        time.sleep(0.05)
        
main()