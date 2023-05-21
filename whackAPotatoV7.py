
# Online Python - IDE, Editor, Compiler, Interpreter

from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api, win32con

pixelXCoordinates = [
    1148,
    1217,
    1288,
    1357,
    1427
]
pixelYCoordinates = [
    426,
    543,
    659
]

clickPixelColorMin = 120
clickPixelColorMax = 220
framerate = 1/30
animationDelay = 5/60

def click(x,y):
    win32api.SetCursorPos((x,y))
    #time.sleep(animationDelay)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(framerate)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def clickStart():
    click(1287, 775)

def shouldClickPixel(pixelColor):
    return (pixelColor <= clickPixelColorMax and pixelColor >= clickPixelColorMin)
    
def clickPixel():
    for pixelX in pixelXCoordinates:
        for pixelY in pixelYCoordinates:
            pixelColor = pyautogui.pixel(pixelX, pixelY)[1]
            
            if shouldClickPixel(pixelColor):
                click(pixelX, pixelY)
                return

def main():
    print("Auto Wack Started")
    
    clickStart()

    while keyboard.is_pressed('q') == False:
        clickPixel()
        clickStart()

main()
