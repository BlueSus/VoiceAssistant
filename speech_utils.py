import pyttsx3
import speech_recognition as sr
import pyaudio
import audioop
import os
import uuid
import requests
import re
from pydub import AudioSegment
from pydub.playback import play
from dotenv import load_dotenv
load_dotenv()

engine = pyttsx3.init()
def safe_filename(text):
    sanitized = re.sub(r'[\\/*?:"<>|\n\r\'¥]', '_', text)
    return sanitized[:50] if len(sanitized) > 50 else sanitized
def speak(text):
    print("Bot:", text)
    file_safe = safe_filename(text)
    file_path = f"voice_cache/{file_safe}.mp3"
    if os.path.exists(file_path):
        sound = AudioSegment.from_file(file_path, format="mp3")
        play(sound)
        return
    api_key = os.getenv("ELEVENLABS_API_KEY")
    voice_id = "JBFqnCBsd6RMkjVDRZzb"
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json"
    }
    payload = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.7,
            "similarity_boost": 0.75
        }
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        os.makedirs("voice_cache", exist_ok=True)
        with open(file_path, "wb") as f:
            f.write(response.content)
        sound = AudioSegment.from_file(file_path, format="mp3")
        play(sound)
    except Exception as e:
        print("[Voice Error]", e)

def listen(active=False):
    import math
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 200
    recognizer.dynamic_energy_threshold = True
    recognizer.pause_threshold = 0.6
    recognizer.phrase_threshold = 0.2
    recognizer.non_speaking_duration = 0.3
    mic_index = 46
    sample_rate = 48000
    chunk = 1024
    format = pyaudio.paInt32
    channels = 2
    max_chunks = int(sample_rate / chunk * 6)
    if active:
        speak("Listening")
    p = pyaudio.PyAudio()
    stream = p.open(format=format, channels=channels, rate=sample_rate,
                    input=True, input_device_index=mic_index,
                    frames_per_buffer=chunk)
    frames = []
    silence_threshold = 1000
    silent_chunks = 0
    max_silence_chunks = 10
    try:
        for i in range(max_chunks):
            data = stream.read(chunk, exception_on_overflow=False)
            frames.append(data)
            volume = audioop.rms(data, 4)
            if volume < silence_threshold:
                silent_chunks += 1
            else:
                silent_chunks = 0
            if i > 10 and silent_chunks >= max_silence_chunks:
                break
    except Exception as e:
        print("[ERROR]", e)
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()
    raw_data = b''.join(frames)
    try:
        data_16bit_stereo = audioop.lin2lin(raw_data, 4, 2)
        mono_audio = audioop.tomono(data_16bit_stereo, 2, 0.5, 0.5)
        mono_audio = audioop.bias(mono_audio, 2, 128)
        mono_audio = audioop.lin2lin(mono_audio, 2, 2)
    except Exception as e:
        print("[Audio Conversion Error]", e)
        return ""
    audio_data = sr.AudioData(mono_audio, sample_rate, 2)
    try:
        text = recognizer.recognize_google(audio_data)
        print(f"[You said]: {text}")
        return text.lower().strip()
    except sr.UnknownValueError:
        if active:
            speak("Could not understand audio")
    except sr.RequestError:
        if active:
            speak("Speech service not available")
    return ""
