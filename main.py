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

client = Client(headers={'Authorization': f"Bearer {os.getenv('OLLAMA_API_KEY')}"})

key = os.getenv("OLLAMA_API_KEY")

print("Key exists:", key is not None)
print("Key length:", len(key) if key else 0)

# Hyperparameters for recording
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = "audio_file/for_whisper.wav"

# Setting voice for text to speech
voice = PiperVoice.load("en_GB-jenny_dioco-medium.onnx")
# with wave.open("audio_file/test.wav", "wb") as wav_file:
#     voice.synthesize_wav("Welcome to the world of speech synthesis!", wav_file)

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

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("*** Done recording ***")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    return None

record()