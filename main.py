import sys 
import os 
import wave
import pyaudio
import whisper
from piper import PiperVoice
from ollama import chat
from ollama import Client
import config
import speech_text as stt
import summary_voice as tts


CHANNELS = config.CHANNELS
RATE = config.RATE
FORMAT = config.FORMAT
CHUNK = config.CHUNK
RECORD_SECONDS = config.RECORD_SECONDS
WAVE_OUTPUT_FILENAME = config.WAVE_OUTPUT_FILENAME
WHISPER = config.WHISPER

# Init things
voice = PiperVoice.load(config.VOICE)

# Setting up Ollama key
key = os.getenv("OLLAMA_API_KEY")
def ollama_key_exist():
    print("Key exists:", key is not None)
    print("Key length:", len(key) if key else 0)



# Main body
# stt.record_user()
# stt.transcribe_user()

