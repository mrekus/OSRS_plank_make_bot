from bot.get_items import click_plank_bank
from bot.make import click_log_inventory
from bot.deposit import click_bank, deposit_items
import pyautogui
import time
from random import uniform


def main():
    while True:
        click_plank_bank()
        pyautogui.press("esc")
        time.sleep(round(uniform(0.08, 0.12), 2))
        pyautogui.press("f3")
        click_log_inventory()
        time.sleep(round(uniform(0.08, 0.12), 2))
        click_bank()
        time.sleep(round(uniform(0.08, 0.12), 2))
        deposit_items()
        time.sleep(round(uniform(0.08, 0.12), 2))


if __name__ == "__main__":
    time.sleep(5)
    main()
