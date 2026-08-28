import sys 
import os 
import wave
import pyaudio
import whisper
# import piper
# import ollama
# from piper import PiperVoice

import config

voice = config.voice
CHANNELS = config.CHANNELS
RATE = config.RATE
FORMAT = config.FORMAT
CHUNK = config.CHUNK
REC_TIME = config.RECORD_SECONDS
OUTPUT_FILE = config.WAVE_OUTPUT_FILENAME


### Short record with Pyaudio
def record_user():
    p = pyaudio.PyAudio()

    stream = p.open(channels=CHANNELS, 
                    rate=RATE, 
                    format=FORMAT, 
                    frames_per_buffer=CHUNK, 
                    input=True)

    print("*** RECORDING ***")

    frames = []

    for i in range(0, int(RATE / CHUNK * REC_TIME)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("*** Done recording ***")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(OUTPUT_FILE, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    return None


def transcribe_user():
    model = whisper.load_model("base")
    result = model.transcribe(OUTPUT_FILE)
    print(result['text'])