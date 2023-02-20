import win32api
import pyautogui
import time
from random import randint, uniform


def click_spell(x=randint(1233, 1247), y=randint(394, 407)):
    win32api.SetCursorPos((x, y))
    time.sleep(round(uniform(0.05, 0.1), 2))
    pyautogui.click(clicks=1, interval=(round(uniform(0.02, 0.05), 2)))
    time.sleep(round(uniform(0.05, 0.1), 2))


def relocate(count, x, y):
    time.sleep(round(uniform(0.2, 0.3), 2))
    win32api.SetCursorPos((x, y))
    time.sleep(round(uniform(0.05, 0.1), 2))
    pyautogui.click(clicks=1, interval=(round(uniform(0.02, 0.05), 2)))
    time.sleep(round(uniform(0.07, 0.10), 2))
    count += 1
    time.sleep(round(uniform(1.9, 2.1), 2))


def click_log_inventory():
    count = 0
    for i in range(26):
        x = randint(1123, 1149)
        y = randint(236, 266)
        if count <= 6:
            if count == 0:
                click_spell()
                relocate(count, x, y)
            else:
                y += 36 * count
                click_spell()
                relocate(count, x, y)
        if 7 <= count <= 13:
            x += 45
            y = randint(236, 266)
            if count == 7:
                click_spell()
                relocate(count, x, y)
            else:
                y += 36 * (count - 7)
                click_spell()
                relocate(count, x, y)
        if 14 <= count <= 20:
            x = randint(1208, 1235)
            y = randint(236, 266)
            if count == 14:
                click_spell()
                relocate(count, x, y)
            else:
                y += 36 * (count - 14)
                click_spell()
                relocate(count, x, y)
        if 21 <= count <= 25:
            x = randint(1250, 1276)
            y = randint(236, 266)
            if count == 14:
                click_spell()
                relocate(count, x, y)
            else:
                y += 36 * (count - 21)
                click_spell()
                relocate(count, x, y)
