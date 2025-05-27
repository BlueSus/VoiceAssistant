from features import system_control
from speech_utils import speak

def handle_command(cmd):
    if not cmd:
        return
    if system_control.handle(cmd):
        return
    speak(f"Command not recognized: {cmd}")
