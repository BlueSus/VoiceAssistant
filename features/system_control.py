import pyautogui
import time
from speech_utils import speak

def handle(cmd):
    if any(word in cmd for word in ["notepad", "notes", "text editor"]):
        speak("Opening Notepad")
        pyautogui.hotkey("win", "r")
        time.sleep(0.5)
        pyautogui.write("notepad")
        pyautogui.press("enter")
        return True
    elif any(phrase in cmd for phrase in ["read screen", "what's on screen", "screenshot text"]):
        from features.ocr_tools import read_screen
        read_screen()
        return True
    return False
