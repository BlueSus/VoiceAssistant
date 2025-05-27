import pytesseract
import pyautogui
from PIL import Image
import time
from speech_utils import speak

def read_screen():
    speak("Select area in 3 seconds.")
    time.sleep(3)
    screenshot = pyautogui.screenshot()
    screenshot.save("temppic.png")
    text = pytesseract.image_to_string(Image.open("temppic.png"))
    print("Screen says:", text)
    speak("Here's what's on the screen.")
    speak(text)