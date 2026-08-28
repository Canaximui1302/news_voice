import sys 
import os 
import wave
import pyaudio
from piper import PiperVoice
from ollama import Client
from ollama import chat
import config

# Init voice
voice = PiperVoice.load(config.VOICE)
sample_rate = voice.config.sample_rate


def speaker(text):
    p = pyaudio.PyAudio()

    stream = p.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=sample_rate,
        output=True,
    )

    # text = "Hello! This audio is being generated and played directly."

    for chunk in voice.synthesize(text):
        stream.write(chunk.audio_int16_bytes)

    stream.stop_stream()
    stream.close()
    p.terminate()