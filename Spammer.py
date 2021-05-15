import pyautogui
import time
import keyboard
from pynput.keyboard import Key, Listener

msg = input("Enter message for spam...\n")

time.sleep(3)

print('Place the cursor in the typebox and press space')

def show(key):
    if key == Key.backspace:
        exit()

    if key == Key.space:

        if msg == "file":

            f = open("file.txt", "rt")
            lines = f.readlines()

            for line in lines:
                if keyboard.is_pressed('backspace'):
                    exit()
                pyautogui.typewrite(line)
                keyboard.press_and_release('enter')
                time.sleep(3)
            
        else:

            while keyboard.is_pressed('backspace') == False:
                pyautogui.typewrite(msg)
                keyboard.press_and_release('enter')
                time.sleep(3)

        exit()

with Listener(on_press = show) as listener:
    listener.join()