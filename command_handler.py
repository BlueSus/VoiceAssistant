from features import system_control, time_weather
from speech_utils import speak
from command_aliases import ALIASES
from features import open_app
from features import reminder_manager
COMMAND_LOOKUP = {alias: cmd for cmd, aliases in ALIASES.items() for alias in aliases}
def resolve_alias(cmd):
    return COMMAND_LOOKUP.get(cmd, cmd)
def handle_command(cmd):
    if not cmd:
        return
    base_command = resolve_alias(cmd)
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
    speak(f"Command not recognized: {cmd}")
