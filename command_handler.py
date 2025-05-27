from features import system_control
from speech_utils import speak
from command_aliases import ALIASES
from features import open_app
COMMAND_LOOKUP = {alias: cmd for cmd, aliases in ALIASES.items() for alias in aliases}
def resolve_alias(cmd):
    return COMMAND_LOOKUP.get(cmd, cmd)
def handle_command(cmd):
    if not cmd:
        return
    base_command = resolve_alias(cmd)
    if open_app.handle_open(cmd):
        return
    if system_control.handle(cmd):
        return
    speak(f"Command not recognized: {cmd}")
