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
        while True:
            key = readchar.readkey()

            # Slow cursor moving
            if key == 'w': TakeControl.Mouse.slow_move_up()
            if key == 'a': TakeControl.Mouse.slow_move_left()
            if key == 's': TakeControl.Mouse.slow_move_down()
            if key == 'd': TakeControl.Mouse.slow_move_right()

            # Fast cursor moving
            if key == 'W': TakeControl.Mouse.fast_move_up()
            if key == 'A': TakeControl.Mouse.fast_move_left()
            if key == 'S': TakeControl.Mouse.fast_move_down()
            if key == 'D': TakeControl.Mouse.fast_move_right()

            # Clicking mouse buttons
            if key == 'j': TakeControl.Mouse.left_click()
            if key == 'J': TakeControl.Mouse.left_double_click()
            if key == 'l': TakeControl.Mouse.right_click()
            if key == 'L': TakeControl.Mouse.right_double_click()

            # Pressing mouse buttons
            if key == 'u': TakeControl.Mouse.left_down()
            if key == 'U': TakeControl.Mouse.left_up()
            if key == 'o': TakeControl.Mouse.right_down()
            if key == 'O': TakeControl.Mouse.right_up()

            # Scrolling
            if key == 'i': TakeControl.Mouse.slow_scroll_up()
            if key == 'I': TakeControl.Mouse.fast_scroll_up()
            if key == 'k': TakeControl.Mouse.slow_scroll_down()
            if key == 'K': TakeControl.Mouse.fast_scroll_down()

            # Typing
            if key == 't': TakeControl.Keyboard.type()

            # Pressing keyboard keys
            if key == 'P': TakeControl.Keyboard.press()
            if key == 'p':
                second_sequence_key = readchar.readchar()
                if second_sequence_key == 'd': TakeControl.Keyboard.press_down()
                if second_sequence_key == 'u': TakeControl.Keyboard.press_up()

            # Quiting
            if key == 'q': break

TakeControl.take_control()
