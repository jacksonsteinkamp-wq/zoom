#CHAT STARTS
import ctypes
from ctypes import wintypes
import time
import keyboard

magnification = ctypes.WinDLL("Magnification.dll")
user32 = ctypes.windll.user32
ctypes.windll.shcore.SetProcessDpiAwareness(2) 
magnification.MagInitialize.restype = wintypes.BOOL
magnification.MagUninitialize.restype = wintypes.BOOL
magnification.MagSetFullscreenTransform.argtypes = [wintypes.FLOAT,wintypes.INT,wintypes.INT]
magnification.MagSetFullscreenTransform.restype = wintypes.BOOL
SCREEN_WIDTH = user32.GetSystemMetrics(0)
SCREEN_HEIGHT = user32.GetSystemMetrics(1)
print("Finding Monitor Specs...")
print("Screen Width: " + str(SCREEN_WIDTH) + "\nScreen Height: " + str(SCREEN_HEIGHT))
time.sleep(1.5)
def set_centered_zoom(zoom_level: float):
    visible_width = SCREEN_WIDTH / zoom_level
    visible_height = SCREEN_HEIGHT / zoom_level
    offset_x = int((SCREEN_WIDTH - visible_width) / 2) 
    offset_y = int((SCREEN_HEIGHT - visible_height) / 2)
    magnification.MagSetFullscreenTransform(zoom_level, offset_x, offset_y)

VK_MOUSE = {
    "left": 0x01,
    "right": 0x02,
    "middle": 0x04,
    "x": 0x05,
    "x2": 0x06,
}

def is_key_pressed(key):
    if key in VK_MOUSE:
        return bool(user32.GetAsyncKeyState(VK_MOUSE[key]) & 0x8000)
    else:
        return keyboard.is_pressed(key)

#CHAT ENDS

def clear():
    print("\033[2J\033[H", end="") 

def main(data):
    magnification.MagInitialize()
    zoom_level = 1
    clear()
    print("Magnifier at 1x")
    keys = data[2]
    quit = 0
    while True:
        pressed = False
        for mode, key, zooms in keys:
            if is_key_pressed(key):
                if mode == "Hold":
                    if zoom_level != zooms[0]:
                        zoom_level = zooms[0]
                        set_centered_zoom(zoom_level)
                        clear()
                        print("Magnifier at " + str(zoom_level) + "x")
                elif mode == "Toggle" or mode == "AWP":
                    clear()
                    print("Mode not available (Coming soon!)")
                pressed = True
                break
        if not pressed and zoom_level != 1:
            zoom_level = 1
            set_centered_zoom(zoom_level)
            print("Magnifier at 1x")
        if keyboard.is_pressed('ESC'):
            quit += 1
            if quit == 1:
                clear()
                print("Exiting in 3 Seconds!")
            elif quit == 20:
                clear()
                print('Exiting in 2 Seconds!')
            elif quit == 40:
                clear()
                print("Exiting!")
            if quit == 60:
                magnification.MagUninitialize()
                exit()
        else:
            quit = 0
        time.sleep(0.05)


#import presetanalyzer
#main(presetanalyzer.readpresetdata("Test | 2 (Hold : p : 1.25)(Hold : left : 1.25) <>"))