from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
#from win32ctypes.pywin32 import win32api
#import win32con

while 1:
    if pyautogui.locateOnScreen("brownTato32.png") != None:
        print("I can see it")
        time.sleep(0.5)
    else:
        print("I am unable to see it")
        time.sleep(0.5)
