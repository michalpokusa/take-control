import os
os.environ["DISPLAY"] = ":0"

import readchar
import pyautogui

class TakeControl:

    class Config:
        SMALL_MOUSE_MOVEMENT = 10
        BIG_MOUSE_MOVEMENT = 100

        SMALL_SCROLL_MOVEMENT = 5
        BIG_SCROLL_MOVEMENT = 25

    class Mouse:

        # Mouse movement
        def slow_move_up():
            pyautogui.move(0, -TakeControl.Config.SMALL_MOUSE_MOVEMENT)

        def slow_move_down():
            pyautogui.move(0, TakeControl.Config.SMALL_MOUSE_MOVEMENT)

        def slow_move_left():
            pyautogui.move(-TakeControl.Config.SMALL_MOUSE_MOVEMENT, 0)

        def slow_move_right():
            pyautogui.move(TakeControl.Config.SMALL_MOUSE_MOVEMENT, 0)

        def fast_move_up():
            pyautogui.move(0, -TakeControl.Config.BIG_MOUSE_MOVEMENT)

        def fast_move_down():
            pyautogui.move(0, TakeControl.Config.BIG_MOUSE_MOVEMENT)

        def fast_move_left():
            pyautogui.move(-TakeControl.Config.BIG_MOUSE_MOVEMENT, 0)

        def fast_move_right():
            pyautogui.move(TakeControl.Config.BIG_MOUSE_MOVEMENT, 0)

        # Mouse clicks
        def left_click():
            pyautogui.click()

        def left_double_click():
            pyautogui.doubleClick(button="left")

        def right_click():
            pyautogui.rightClick()

        def right_double_click():
            pyautogui.doubleClick(button="right")

        # Mouse pressing
        def left_down():
            pyautogui.mouseDown(button="left")

        def left_up():
            pyautogui.mouseUp(button="left")

        def right_down():
            pyautogui.mouseDown(button="right")

        def right_up():
            pyautogui.mouseUp(button="right")

        # Scrolling
        def slow_scroll_up():
            pyautogui.scroll(TakeControl.Config.SMALL_SCROLL_MOVEMENT)

        def fast_scroll_up():
            pyautogui.scroll(TakeControl.Config.BIG_SCROLL_MOVEMENT)

        def slow_scroll_down():
            pyautogui.scroll(-TakeControl.Config.SMALL_SCROLL_MOVEMENT)

        def fast_scroll_down():
            pyautogui.scroll(-TakeControl.Config.BIG_SCROLL_MOVEMENT)

    class Keyboard:

        def type():
            text_to_type = input("Text to type: ")
            pyautogui.write(text_to_type)

        def hotkey():
            hotkey_to_press = input("Hotkey to press: ")
            pyautogui.hotkey(*hotkey_to_press.split(", "))

        def press():
            key_to_press = input("Key to press: ")
            pyautogui.press(key_to_press)

        def press_down():
            key_to_press = input("Key to press down: ")
            pyautogui.keyDown(key_to_press)

        def press_up():
            key_to_press = input("Key to press up: ")
            pyautogui.keyUp(key_to_press)

    def take_control():
        while "In control":
            print("You are in control...")
            key = readchar.readkey()

            # Slow cursor moving
            if key == 'w': TakeControl.Mouse.slow_move_up(); continue
            if key == 'a': TakeControl.Mouse.slow_move_left(); continue
            if key == 's': TakeControl.Mouse.slow_move_down(); continue
            if key == 'd': TakeControl.Mouse.slow_move_right(); continue

            # Fast cursor moving
            if key == 'W': TakeControl.Mouse.fast_move_up(); continue
            if key == 'A': TakeControl.Mouse.fast_move_left(); continue
            if key == 'S': TakeControl.Mouse.fast_move_down(); continue
            if key == 'D': TakeControl.Mouse.fast_move_right(); continue

            # Clicking mouse buttons
            if key == 'j': TakeControl.Mouse.left_click(); continue
            if key == 'J': TakeControl.Mouse.left_double_click(); continue
            if key == 'l': TakeControl.Mouse.right_click(); continue
            if key == 'L': TakeControl.Mouse.right_double_click(); continue

            # Pressing mouse buttons
            if key == 'u': TakeControl.Mouse.left_down(); continue
            if key == 'U': TakeControl.Mouse.left_up(); continue
            if key == 'o': TakeControl.Mouse.right_down(); continue
            if key == 'O': TakeControl.Mouse.right_up(); continue

            # Scrolling
            if key == 'i': TakeControl.Mouse.slow_scroll_up(); continue
            if key == 'I': TakeControl.Mouse.fast_scroll_up(); continue
            if key == 'k': TakeControl.Mouse.slow_scroll_down(); continue
            if key == 'K': TakeControl.Mouse.fast_scroll_down(); continue

            # Typing
            if key == 't': TakeControl.Keyboard.type(); continue

            # Hotkey
            if key == 'h': TakeControl.Keyboard.hotkey(); continue

            # Pressing keyboard keys
            if key == 'p': TakeControl.Keyboard.press(); continue
            if key == 'P':
                second_sequence_key = readchar.readchar()
                if second_sequence_key == 'd': TakeControl.Keyboard.press_down(); continue
                if second_sequence_key == 'u': TakeControl.Keyboard.press_up(); continue

            # Quiting
            if key == 'q':
                print("You lost control...")
                break

TakeControl.take_control()
