from speech_utils import speak, listen
from command_handler import handle_command

TRIGGER_PHRASES = [
    "jarvis", "hey jarvis", "yo jarvis", "okay jarvis", "hi jarvis",
    "assistant", "hey assistant", "yo assistant", "wake up", "hello there"
    "Blue Bus", "Bot", "Open"]

EXIT_PHRASES = [
    "goodbye", "shutdown", "exit", "sleep", "quit", "stop", "bye",
    "power down", "shut yourself down", "see you later",
    "that's enough", "terminate", "end session", "you can rest now",
    "take a break", "go to sleep"
]

speak("Say wake word to begin.")

while True:
    command = listen(active=False).strip()

    matched_trigger = next((trigger for trigger in TRIGGER_PHRASES if command.startswith(trigger)), None)

    if matched_trigger:
        clean_command = command[len(matched_trigger):].strip()

        if clean_command:
            speak("Yes, I'm listening.")
            handle_command(clean_command)
        else:
            speak("Yes?")
            followup = listen(active=True).strip()
            if any(phrase in followup for phrase in EXIT_PHRASES):
                speak("Shutting down. Goodbye.")
                break
            elif followup:
                handle_command(followup)
