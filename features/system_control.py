from features.ocr_tools import read_screen
from speech_utils import speak

def handle(cmd):
    if "read screen" in cmd or "screenshot text" in cmd:
        text = read_screen()
        speak(f"{text}" if text else "I didn't find any text.")
        return True
    return False
