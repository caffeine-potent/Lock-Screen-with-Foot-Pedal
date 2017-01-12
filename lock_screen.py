import ctypes
from pynput import keyboard

def on_press(key):
    if key == keyboard.Key.f14:
        ctypes.windll.user32.LockWorkStation()

def on_release(key):
	pass

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()