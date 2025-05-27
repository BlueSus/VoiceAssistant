import pyaudio
import audioop
import speech_recognition as sr
def wait_for_trigger(trigger_word="jarvis", mic_index=46, sample_rate=48000, duration=3):
    recognizer = sr.Recognizer()
    chunk = 1024
    format = pyaudio.paInt32
    channels = 2
    p = pyaudio.PyAudio()
    stream = p.open(format=format, channels=channels, rate=sample_rate,
                    input=True, input_device_index=mic_index,
                    frames_per_buffer=chunk)
    frames = []
    for _ in range(int(sample_rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    p.terminate()
    raw_data = b''.join(frames)
    data_16bit_stereo = audioop.lin2lin(raw_data, 4, 2)
    mono_audio = audioop.tomono(data_16bit_stereo, 2, 0.5, 0.5)
    audio_data = sr.AudioData(mono_audio, sample_rate, 2)
    try:
        text = recognizer.recognize_google(audio_data)
        print(f"[DEBUG] Trigger Check Heard: {text}")
        return trigger_word in text.lower()
    except:
        return False