import sys 
import os 
import wave
import pyaudio
import whisper
import config

CHANNELS = config.CHANNELS
RATE = config.RATE
FORMAT = config.FORMAT
CHUNK = config.CHUNK
RECORD_SECONDS = config.RECORD_SECONDS

WAVE_OUTPUT_FILENAME = config.WAVE_OUTPUT_FILENAME

WHISPER = config.WHISPER

# Setting up Whisper
transcriber = whisper.load_model(WHISPER)

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

## Function to transcribe audio data
def transcribe_user():
    res = transcriber.transcribe(WAVE_OUTPUT_FILENAME)['text']
    # print(res)
    return res