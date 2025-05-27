ALIASES = {
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
APP_ALIASES = {
    "notepad": "notepad.exe",
    "steam": "steam.exe",
    "discord": "discord.exe",
    "chrome": "chrome.exe",
    "firefox": "firefox.exe",
    "edge": "msedge.exe",
    "calculator": "calc.exe",
    "paint": "mspaint.exe",
    "task manager": "taskmgr.exe",
    "file explorer": "explorer.exe",
    "explorer": "explorer.exe",
    "cmd": "cmd.exe",
    "powershell": "powershell.exe",
    "snipping tool": "snippingtool.exe",
    "word": "winword.exe",
    "excel": "excel.exe",
    "powerpoint": "powerpnt.exe",
    "outlook": "outlook.exe",
    "windows terminal": "wt.exe",
    "control panel": "control.exe",
    "settings": "ms-settings:",
    "registry editor": "regedit.exe",
    "device manager": "devmgmt.msc",
    "event viewer": "eventvwr.exe",
    "resource monitor": "resmon.exe",
    "system information": "msinfo32.exe",
    "services": "services.msc",
    "defender": "windowsdefender:",
    "magnifier": "magnify.exe",
    "narrator": "narrator.exe"
}
COMMAND_LOOKUP = {
    alias: command for command, aliases in ALIASES.items() for alias in aliases
}