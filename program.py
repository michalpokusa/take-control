import os
os.environ["DISPLAY"] = ":0"

import readchar
import pyautogui


while True:
    key = readchar.readkey()

    # Slow cursor moving
    if key == 'w': pyautogui.move(0, -10)
    if key == 'a': pyautogui.move(-10, 0)
    if key == 's': pyautogui.move(0, 10)
    if key == 'd': pyautogui.move(10, 0)

    # Fast cursor moving
    if key == 'W': pyautogui.move(0, -100)
    if key == 'A': pyautogui.move(-100, 0)
    if key == 'S': pyautogui.move(0, 100)
    if key == 'D': pyautogui.move(100, 0)

    # Clicking
    if key == 'j': pyautogui.click()
    if key == 'l': pyautogui.rightClick()
    if key == 'u': pyautogui.doubleClick()

    # Draging
    if key == 'o': pyautogui.mouseDown()
    if key == 'p': pyautogui.mouseUp()

    # Scrolling
    if key == 'i': pyautogui.scroll(10)
    if key == 'k': pyautogui.scroll(-10)

    # Quiting
    if key == 'q': break
