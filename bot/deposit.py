import win32api
import time
import pyautogui
from random import randint, uniform


def click_bank(x=randint(393, 1012), y=randint(293, 333)):
    win32api.SetCursorPos((x, y))
    time.sleep(round(uniform(0.40, 0.49), 2))
    pyautogui.click(clicks=1, interval=(round(uniform(0.09, 0.12), 2)))
    time.sleep(round(uniform(0.09, 0.12), 2))


def deposit_items(x=randint(991, 1014), y=randint(324, 342)):
    win32api.SetCursorPos((x, y))
    time.sleep(round(uniform(0.40, 0.49), 2))
    pyautogui.click(clicks=1, interval=(round(uniform(0.09, 0.12), 2)))
    time.sleep(round(uniform(0.09, 0.12), 2))
