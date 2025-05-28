import threading
import time
from datetime import datetime, timedelta
from speech_utils import speak
import re
import json
import os

REMINDER_FILE = "reminders.json"
reminders = []
def load_reminders():
    global reminders
    if os.path.exists(REMINDER_FILE):
        with open(REMINDER_FILE, "r") as file:
            raw = json.load(file)
            reminders.extend((task, datetime.fromisoformat(when)) for task, when in raw)
def save_reminders():
    with open(REMINDER_FILE, "w") as file:
        json.dump([(task, when.isoformat()) for task, when in reminders], file)
def parse_reminder(command):
    in_time = re.match(r".*remind me to (.+) in (\d+) minutes?", command)
    at_time = re.match(r".*remind me to (.+) at (\d{1,2}:\d{2})", command)
    if in_time:
        task, mins = in_time.groups()
        remind_time = datetime.now() + timedelta(minutes=int(mins))
        return task.strip(), remind_time
    if at_time:
        task, timestr = at_time.groups()
        now = datetime.now()
        target = datetime.strptime(timestr, "%H:%M").replace(year=now.year, month=now.month, day=now.day)
        if target < now:
            target += timedelta(days=1)
        return task.strip(), target
    return None, None
def add_reminder(command, speak):
    task, remind_time = parse_reminder(command)
    if task and remind_time:
        reminders.append((task, remind_time))
        save_reminders()
        speak(f"Okay, I will remind you to {task} at {remind_time.strftime('%I:%M %p')}.")
    else:
        speak("Sorry, I couldn't understand the reminder.")
def list_reminders(speak):
    if not reminders:
        speak("You have no reminders.")
    else:
        for task, when in reminders:
            speak(f"Reminder to {task} at {when.strftime('%I:%M %p')}.")
def cancel_reminder(command, speak):
    for task, when in reminders[:]:
        if task in command:
            reminders.remove((task, when))
            save_reminders()
            speak(f"Cancelled reminder to {task}.")
            return
    speak("I couldn't find a reminder to cancel.")
def reminder_loop(speak):
    while True:
        now = datetime.now()
        for task, when in reminders[:]:
            if now >= when:
                speak(f"Reminder: {task}")
                reminders.remove((task, when))
                save_reminders()
        time.sleep(5)

load_reminders()
