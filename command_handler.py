from features import system_control, time_weather, open_app, reminder_manager
from features.media_controls import mute, unmute, get_volume, set_volume
from speech_utils import speak
from command_aliases import ALIASES
from features import spotify_control
COMMAND_LOOKUP = {alias: cmd for cmd, aliases in ALIASES.items() for alias in aliases}
def resolve_alias(cmd):
    return COMMAND_LOOKUP.get(cmd, cmd)
def handle_command(cmd):
    if not cmd:
        return
    base_command = resolve_alias(cmd)
    if base_command in [
        "pause music","play music","next song","previous song","volume up","volume down","mute","unmute"
    ]:
        handle_media_command(base_command)
        return
    if "time" in cmd:
        time_weather.get_time()
        return
    if "weather" in cmd:
        city = cmd.replace("weather", "").strip()
        if not city:
            speak("Please say a city name")
        else:
            time_weather.get_weather(city)
        return
    if "remind me" in cmd:
        reminder_manager.add_reminder(cmd, speak)
        return
    elif "list reminders" in cmd or "show reminders" in cmd:
        reminder_manager.list_reminders(speak)
        return
    elif "cancel reminder" in cmd or "remove reminder" in cmd:
        reminder_manager.cancel_reminder(cmd, speak)
        return
    if open_app.handle_open(cmd):
        return
    if system_control.handle(cmd):
        return
    speak(f"Command not recognized")
def handle_media_command(command):
    if "pause music" in command:
        spotify_control.pause()
    elif "play music" in command:
        spotify_control.play()
    elif "next song" in command:
        spotify_control.next_track()
    elif "previous song" in command:
        spotify_control.previous_track()
    elif "mute" in command:
        mute()
    elif "unmute" in command:
        unmute()
    elif "volume up" in command:
        new_vol = min(get_volume() + 0.1, 1.0)
        set_volume(new_vol)
    elif "volume down" in command:
        new_vol = max(get_volume() - 0.1, 0.0)
        set_volume(new_vol)
