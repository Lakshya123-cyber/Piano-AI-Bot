from pyautogui import *
import pyautogui
# pyautogui.displayMousePosition()
import time
import keyboard
import random
import win32api, win32con

# ONE HAS TO CHANGE THE VALUES FOR THE TILES
# SINCE WE ALL DON'T REALLY HAVE THE SAME DIMENSIONS FOR THE MONITOR :)

# Tile 1 Position: X: 1277 Y: 779 RGB: (180, 179, 232)
# Tile 2 Position: X: 1376 Y: 779 RGB: (0, 0, 0)
# Tile 3 Position: X: 1479 Y: 779 RGB: (171, 168, 231)
# Tile 4 Position: X: 1591 Y: 779 RGB: (176, 174, 231)

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1) # This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(1277, 779)[0] == 0:
        click(1277, 779)
    if pyautogui.pixel(1376, 779)[0] == 0:
        click(1376, 779)
    if pyautogui.pixel(1479, 779)[0] == 0:
        click(1479, 779)
    if pyautogui.pixel(1591, 779)[0] == 0:
        click(1591, 779)
