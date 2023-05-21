
# Online Python - IDE, Editor, Compiler, Interpreter

from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api, win32con

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

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.015)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def clickStart():
    win32api.SetCursorPos((1287,775))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

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

    while keyboard.is_pressed('q') == False:
        clickStart()
        
        clickPixel()

main()
