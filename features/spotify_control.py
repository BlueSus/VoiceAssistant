import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
load_dotenv()
scope = "user-modify-playback-state user-read-playback-state"
_sp = None
def get_spotify():
    global _sp
    if _sp is None:
        _sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, open_browser=True))
    return _sp
def play():
    print("play command")
    get_spotify().start_playback()
def pause():
    print("pause command")
    get_spotify().pause_playback()
def next_track():
    print("next track command")
    get_spotify().next_track()
def previous_track():
    print("previous track command")
    get_spotify().previous_track()
