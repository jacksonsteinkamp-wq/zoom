import ctypes
from ctypes import wintypes
import time
import keyboard

#I needed help from ChatGPT on how to use the windows magnification tool and how to get the monitor(s) info (resolution, oreintion)
# Windows Magnification API (AI)
magnification = ctypes.WinDLL("Magnification.dll") #Make sure to understand this part
user32 = ctypes.windll.user32
ctypes.windll.shcore.SetProcessDpiAwareness(2) #CHAT USED THIS, #TODO test at home as well
magnification.MagInitialize.restype = wintypes.BOOL
magnification.MagUninitialize.restype = wintypes.BOOL
magnification.MagSetFullscreenTransform.argtypes = [wintypes.FLOAT,wintypes.INT,wintypes.INT]
magnification.MagSetFullscreenTransform.restype = wintypes.BOOL

# find screen size (AI)
SCREEN_WIDTH = user32.GetSystemMetrics(0) #Make sure to understand this part
SCREEN_HEIGHT = user32.GetSystemMetrics(1)
print("Finding Monitor Specs...")
print("Screen Width: " + str(SCREEN_WIDTH) + "\nScreen Height: " + str(SCREEN_HEIGHT))
    
#WHERE MY CODE STARTS
def set_centered_zoom(zoom_level: float): #Centers fullscreen magnifier regardless of monitor resolution (always on whichever monitor is primary)
    visible_width = SCREEN_WIDTH / zoom_level
    visible_height = SCREEN_HEIGHT / zoom_level
    offset_x = int((SCREEN_WIDTH - visible_width) / 2) #Make sure to understand this part
    offset_y = int((SCREEN_HEIGHT - visible_height) / 2)
    magnification.MagSetFullscreenTransform(zoom_level, offset_x, offset_y) #AI assist

#TODO make these actual user inputs from the other file. Figure out a way for there to be as many as we want. 
keyinput2 = 'F5'
keyinputone = 'p' 
zoominputone = 2 
zoominputtwo = 4 

def main():
    quit = 0
    magnification.MagInitialize() #AI helped me understand this
    zoom_level = 1 #here because otherwise the if statements don't know what zoom_level means and would throw and error
    print("Magnifier at 1x")
    while True:
        # 4x zoom on 'F5' key
        if keyboard.is_pressed(keyinput2):
            if zoom_level != zoominputtwo:
                zoom_level = zoominputtwo #4x
                set_centered_zoom(zoom_level)
                print("Magnifier at " + str(zoom_level) + "x")
                
        # 2x zoom on 'p' key
        elif keyboard.is_pressed(keyinputone):
            if zoom_level != zoominputone:
                zoom_level = zoominputone #2x
                set_centered_zoom(zoom_level)
                print("Magnifier at " + str(zoom_level) + "x")
                        
        # reset when nothing held
        elif zoom_level != 1:
            zoom_level = 1
            set_centered_zoom(zoom_level)
            print("Magnifier at 1x")
                
        time.sleep(0.05)
        if keyboard.is_pressed('ESC'):
            quit += 1
            if quit == 1:
                print("\033[2J\033[H", end="")
                print("Exiting in 3 Seconds!")
            elif quit == 20:
                print("\033[2J\033[H", end="")
                print('Exiting in 2 Seconds!')
            elif quit == 40:
                print("\033[2J\033[H", end="")
                print("Exiting!")
            if quit >= 60:
                exit()
        else:
            quit = 0
            