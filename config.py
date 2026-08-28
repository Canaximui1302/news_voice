import sys 
import os 
import wave
import pyaudio
import whisper
import piper
import ollama
from piper import PiperVoice


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