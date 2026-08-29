import sys 
import os 
import wave
import pyaudio

# Audio format
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 10

WAVE_OUTPUT_FILENAME = "audio_file/for_whisper.wav"

# Whisper to transcribe user's audio input
WHISPER = "base"

# Model to summarize the text
SUMMARY = "qwen3:4b"

# For Piper text to speech
VOICE = "voice_model/en_GB-jenny_dioco-medium.onnx"
TEST_VOICE = "fly me to the moon and let me play among the stars"


