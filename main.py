import sys 
import os 
import wave
import pyaudio
import whisper
import piper
import ollama
from piper import PiperVoice


# Setting up Ollama key
from ollama import chat
from ollama import Client

import config

voice = config.voice
CHANNELS = config.CHANNELS
RATE = config.RATE
FORMAT = config.FORMAT
CHUNK = config.CHUNK
REC_TIME = config.RECORD_SECONDS
OUTPUT_FILE = config.WAVE_OUTPUT_FILENAME

client = Client(headers={'Authorization': f"Bearer {os.getenv('OLLAMA_API_KEY')}"})

key = os.getenv("OLLAMA_API_KEY")

print("Key exists:", key is not None)
print("Key length:", len(key) if key else 0)

# Hyperparameters for recording


sample_rate = voice.config.sample_rate
print("Record sample rate: ", sample_rate)


### Short record with Pyaudio

def record():
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

record()