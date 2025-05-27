import os
import webbrowser
import difflib
from speech_utils import speak
from command_aliases import APP_ALIASES

def get_best_app_match(spoken_text):
    spoken_text = spoken_text.lower()
    matches = difflib.get_close_matches(spoken_text, APP_ALIASES.keys(), n=1, cutoff=0.7)
    return matches[0] if matches else None

def is_probably_url(text):
    return "." in text or text.startswith("www") or text.endswith(".com")

def handle_open(cmd):
    lowered = cmd.lower()
    best_match = get_best_app_match(lowered)
    if best_match:
        exe = APP_ALIASES[best_match]
        speak(f"Launching {best_match}.")
        os.system(f"start {exe}")
        return True
    if "open" in lowered or "go to" in lowered:
        words = lowered.replace("open", "").replace("go to", "").strip()
        if "." in words or "www" in words:
            speak(f"Opening {words}.")
            webbrowser.open(f"https://{words}")
            return True
        else:
            speak(f"Searching for {words}.")
            webbrowser.open(f"https://www.google.com/search?q={words}")
            return True
    if "search" in lowered:
        query = lowered.replace("search", "").replace("google", "").replace("for", "").strip()
        speak(f"Searching for {query}.")
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return True
    return False