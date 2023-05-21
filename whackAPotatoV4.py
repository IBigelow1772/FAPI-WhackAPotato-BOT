
# Online Python - IDE, Editor, Compiler, Interpreter

from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    clickOccurred = True

def clickStart():
    win32api.SetCursorPos((1287,775))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

pixelXCoordinates = [
    1152,
    1220,
    1292,
    1361,
    1431
]
pixelYCoordinates = [
    410,
    525,
    639
]

clickPixelColorMin = 135
clickPixelColorMax = 200

print("Auto Wack Started")
clickOccurred = False

while keyboard.is_pressed('q') == False:
    clickStart()
    
    clickOccurred = False
    
    for pixelX in pixelXCoordinates:
        for pixelY in pixelYCoordinates:
            pixelColor = pyautogui.pixel(pixelX, pixelY)
            
            if pixelColor[1] <= clickPixelColorMax and pixelColor[1] >= clickPixelColorMin:
                click(pixelX, pixelY)
                break
        if clickOccurred:
            break
