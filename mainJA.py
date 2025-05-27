from speech_utils import speak, listen
from command_handler import handle_command
from command_aliases import TRIGGER_PHRASES, EXIT_PHRASES
speak("Say wake word to begin.")

while True:
    command = listen(active=False).strip()
    matched_trigger = next((trigger for trigger in TRIGGER_PHRASES if command.startswith(trigger)), None)
    if matched_trigger:
        clean_command = command[len(matched_trigger):].strip()
        if clean_command:
            handle_command(clean_command)
        else:
            followup = listen(active=True).strip()
            if any(phrase in followup for phrase in EXIT_PHRASES):
                speak("Shutting down. Goodbye.")
                break
            elif followup:
                handle_command(followup)
