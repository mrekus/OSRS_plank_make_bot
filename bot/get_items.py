import win32api
import time
import pyautogui
from random import randint, uniform


def click_plank_bank(x=randint(636, 652), y=randint(112, 129)):
    win32api.SetCursorPos((x, y))
    time.sleep(round(uniform(0.1, 0.2), 2))
    pyautogui.click(clicks=1, interval=(round(uniform(0.02, 0.05), 2)))
    time.sleep(round(uniform(0.07, 0.10), 2))
