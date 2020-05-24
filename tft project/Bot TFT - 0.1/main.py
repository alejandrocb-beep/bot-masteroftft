from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import pydirectinput

def enemyhp():
    if pyautogui.locateOnScreen('BAR-lowhp.png',confidence=0.75) != None:
        return 1
    elif pyautogui.locateOnScreen('BAR-halfhp.png',confidence=0.85) != None:
        return 2
    elif pyautogui.locateOnScreen('BAR-fullhp.png',confidence=0.75) != None:
        return 3
    else:
        return 4

def autoq():
    
    pic = pyautogui.screenshot (region=(320,150,1280,768))
    width, height = pic.size
    
    for x in range (0,width,5):
        for y in range (0,height,5):
            r,g,b = pic.getpixel((x,y))
            if b == 90 and g == 101 and r == 206:
                pydirectinput.moveTo(x+330,y+160)
                pydirectinput.press('q')
                break

def autoqq():
    img_pos = pyautogui.locateOnScreen('BAR-fullhp.png',confidence=0.2)
    if img_pos is not None:
        pyautogui.click(img_pos)
        pydirectinput.press('q')
        

# Barrita de vida enemiga: (206, 101,  90)

while keyboard.is_pressed('k') == False:
    if keyboard.read_key() == "1":
        autoqq()
        
                
