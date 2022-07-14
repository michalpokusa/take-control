import os
os.environ["DISPLAY"] = ":0"

import readchar
import pyautogui

class TakeControl:

    class Config:
        SMALL_MOUSE_MOVEMENT = 10
        BIG_MOUSE_MOVEMENT = 100

    def take_control():
        while True:
            key = readchar.readkey()

            # Slow cursor moving
            if key == 'w': pyautogui.move(0, -TakeControl.Config.SMALL_MOUSE_MOVEMENT)
            if key == 'a': pyautogui.move(-TakeControl.Config.SMALL_MOUSE_MOVEMENT, 0)
            if key == 's': pyautogui.move(0, TakeControl.Config.SMALL_MOUSE_MOVEMENT)
            if key == 'd': pyautogui.move(TakeControl.Config.SMALL_MOUSE_MOVEMENT, 0)

            # Fast cursor moving
            if key == 'W': pyautogui.move(0, -TakeControl.Config.BIG_MOUSE_MOVEMENT)
            if key == 'A': pyautogui.move(-TakeControl.Config.BIG_MOUSE_MOVEMENT, 0)
            if key == 'S': pyautogui.move(0, TakeControl.Config.BIG_MOUSE_MOVEMENT)
            if key == 'D': pyautogui.move(TakeControl.Config.BIG_MOUSE_MOVEMENT, 0)

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

TakeControl.take_control()
