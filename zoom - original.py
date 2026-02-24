import ctypes
from ctypes import wintypes
import time
import keyboard

# ==============================
# Windows Magnification API
# ==============================
magnification = ctypes.WinDLL("Magnification.dll")
user32 = ctypes.windll.user32

magnification.MagInitialize.restype = wintypes.BOOL
magnification.MagUninitialize.restype = wintypes.BOOL
magnification.MagSetFullscreenTransform.argtypes = [
    wintypes.FLOAT,
    wintypes.INT,
    wintypes.INT,
]
magnification.MagSetFullscreenTransform.restype = wintypes.BOOL

# ==============================
# Screen size
# ==============================
SCREEN_WIDTH = user32.GetSystemMetrics(0)
SCREEN_HEIGHT = user32.GetSystemMetrics(1)


# ==============================
# Magnifier helpers
# ==============================
def initialize_magnifier():
    if not magnification.MagInitialize():
        raise RuntimeError("Failed to initialize magnifier")


def set_centered_zoom(zoom_level: float):
    """
    Centers fullscreen magnifier regardless of resolution.
    """
    visible_width = SCREEN_WIDTH / zoom_level
    visible_height = SCREEN_HEIGHT / zoom_level

    offset_x = int((SCREEN_WIDTH - visible_width) / 2)
    offset_y = int((SCREEN_HEIGHT - visible_height) / 2)

    if not magnification.MagSetFullscreenTransform(
        zoom_level, offset_x, offset_y
    ):
        raise RuntimeError("Failed to set zoom")


def reset_zoom():
    if not magnification.MagSetFullscreenTransform(1.0, 0, 0):
        raise RuntimeError("Failed to reset zoom")


# ==============================
# Main loop
# ==============================
def main():
    try:
        initialize_magnifier()

        zoom_level = 1.0
        reset_zoom()
        print("Magnifier at 100%")

        while True:
            # 4x zoom (centered)
            if keyboard.is_pressed("F5"):
                if zoom_level != 2.0:
                    zoom_level = 2.0
                    set_centered_zoom(zoom_level)
                    print("Magnifier set to 200%")

            # 2x zoom (centered)
            elif keyboard.is_pressed("0"):
                if zoom_level != 2.0:
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

    except RuntimeError as e:
        print("Error:", e)

    finally:
        magnification.MagUninitialize()
        print("Magnifier uninitialized")


#if __name__ == "__main__":
#    main()
