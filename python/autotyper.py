import time
from pynput.keyboard import Key, Controller

filename = "tmp.txt" #text file for autotyper to read from
keyboard = Controller()

def autotyper(filename): 

    #set up cursor where you wish for autotyping to occur, to be alt-tabbed to

    with keyboard.pressed(Key.alt):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)

    time.sleep(0.5) #500ms delay so autotyping doesn't start before alt-tabbed
    
    file = open(filename, "r") #read text file
    
    for line in file:
        
        if line in ['\n', '\r\n']: #if line is empty
   
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)

        else:

            for character in line:
                keyboard.press(character)
                keyboard.release(character)
                time.sleep(0.005) #time delay between each keypress

autotyper(filename)


