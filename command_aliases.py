ALIASES = {
    "notepad": ["open notepad","start notepad","launch notepad","run notepad"],
    "read screen": ["read the screen", "what's on screen", "screenshot text", "look at screen"]
}
TRIGGER_PHRASES = [
    "jarvis", "hey jarvis", "yo jarvis", "okay jarvis", "hi jarvis",
    "assistant", "hey assistant", "yo assistant", "wake up", "hello there",
    "blue bus", "bot", "open", "hey bot", "buddy", "my guy", "start listening",
    "let's go", "wake jarvis", "begin", "listen up"
]
EXIT_PHRASES = [
    "goodbye", "shutdown", "exit", "sleep", "quit", "stop", "bye",
    "power down", "shut yourself down", "see you later", "that's enough",
    "terminate", "end session", "you can rest now", "take a break",
    "go to sleep", "that's it", "we're done", "pause", "turn off", "rest mode"
]
COMMAND_LOOKUP = {
    alias: command for command, aliases in ALIASES.items() for alias in aliases
}