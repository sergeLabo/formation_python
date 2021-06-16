# # py_83_listener.py
from pynput import keyboard

INPUT = ""

def on_press(key):
    try:
        print(key.char)
        INPUT += key.char
        # #print(f'alphanumeric key {key.char} pressed')
    except AttributeError:
        # #print(f'special key {key} pressed')
        # #print(key.name, key.value)
        if key.name == "space":
            print(" ")
            INPUT += " "

def on_release(key):
    # #print('f{key} released')
    if key == keyboard.Key.esc:
        # Stop listener
        return False


# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
