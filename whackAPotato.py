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
	time.sleep(0.1)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

goldenTatoBlue = [175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,167]
brownTatoBlue = [138,139,140,141,142,143,144,145,146,147,148,149,150,152,153,154,155,156,157]

#click(1287,775)
click(1108,299)

print("Auto Wack Started")

while keyboard.is_pressed('q') == False:
        #Check if the pixel fo reach potato is green or yellow
        #ROW 1 -----------------------
        if pyautogui.pixel(1152,410)[1] in brownTatoBlue or pyautogui.pixel(1152,410)[1] in goldenTatoBlue:
                #Click
                click(1148,435)
                continue
                

        if pyautogui.pixel(1220,410)[1] in brownTatoBlue or pyautogui.pixel(1220,410)[1] in goldenTatoBlue:
                #Click
                click(1217,435)
                continue

        if pyautogui.pixel(1292,410)[1] in brownTatoBlue or pyautogui.pixel(1292,410)[1] in goldenTatoBlue:
                #Click
                click(1287,435)
                continue

        if pyautogui.pixel(1361,410)[1] in brownTatoBlue or pyautogui.pixel(1361,410)[1] in goldenTatoBlue:
                #Click
                click(1359,435)
                continue

        if pyautogui.pixel(1431,410)[1] in brownTatoBlue or pyautogui.pixel(1431,410)[1] in goldenTatoBlue:
                #Click
                click(1427,435)
                continue

        #ROW 2 -----------------------
        if pyautogui.pixel(1152,525)[1] in brownTatoBlue or pyautogui.pixel(1152,525)[1] in goldenTatoBlue:
                #Click
                click(1148,550)
                continue

        if pyautogui.pixel(1220,525)[1] in brownTatoBlue or pyautogui.pixel(1220,525)[1] in goldenTatoBlue:
                #Click
                click(1217,550)
                continue

        if pyautogui.pixel(1292,525)[1] in brownTatoBlue or pyautogui.pixel(1292,525)[1] in goldenTatoBlue:
                #Click
                click(1287,550)
                continue

        if pyautogui.pixel(1361,525)[1] in brownTatoBlue or pyautogui.pixel(1361,525)[1] in goldenTatoBlue:
                #Click
                click(1359,550)
                continue

        if pyautogui.pixel(1431,525)[1] in brownTatoBlue or pyautogui.pixel(1431,525)[1] in goldenTatoBlue:
                #Click
                click(1427,550)
                continue

        #ROW 3 -----------------------
        if pyautogui.pixel(1152,639)[1] in brownTatoBlue or pyautogui.pixel(1152,639)[1] in goldenTatoBlue:
                #Click
                click(1148,665)
                continue

        if pyautogui.pixel(1220,639)[1] in brownTatoBlue or pyautogui.pixel(1220,639)[1] in goldenTatoBlue:
                #Click
                click(1217,665)
                continue

        if pyautogui.pixel(1292,639)[1] in brownTatoBlue or pyautogui.pixel(1292,639)[1] in goldenTatoBlue:
                #Click
                click(1287,665)
                continue

        if pyautogui.pixel(1361,639)[1] in brownTatoBlue or pyautogui.pixel(1361,639)[1] in goldenTatoBlue:
                #Click
                click(1359,665)
                continue

        if pyautogui.pixel(1431,639)[1] in brownTatoBlue or pyautogui.pixel(1431,639)[1] in goldenTatoBlue:
                #Click
                click(1427,665)
                continue
                
        if pyautogui.pixel(1106,299)[0] == 255 and pyautogui.pixel(1106,299)[1] == 255 and pyautogui.pixel(1106,299)[2] == 255:
                click(1287,775)
                continue
