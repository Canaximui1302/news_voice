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

import speech_text as stt

voice = config.voice
CHANNELS = config.CHANNELS
RATE = config.RATE
FORMAT = config.FORMAT
CHUNK = config.CHUNK
REC_TIME = config.RECORD_SECONDS
OUTPUT_FILE = config.WAVE_OUTPUT_FILENAME

# client = Client(headers={'Authorization': f"Bearer {os.getenv('OLLAMA_API_KEY')}"})

# key = os.getenv("OLLAMA_API_KEY")

# print("Key exists:", key is not None)
# print("Key length:", len(key) if key else 0)


# sample_rate = voice.config.sample_rate
# print("Record sample rate: ", sample_rate)



stt.record_user()
stt.transcribe_user()

