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
