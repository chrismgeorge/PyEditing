import pyaudio
import numpy as np
import wave
import math

CHUNK = 1024 * 4
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

wf = wave.open('psong.wav', 'rb')
p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

def rms(data):
    count = len(data)
    sum_squares = 0.0
    for sample in data:
        n = sample * (1.0/32768)
        sum_squares += n*n
    return math.sqrt( sum_squares / count )

def getDB():
    loud = []
    data = wf.readframes(CHUNK)
    while len(data) != 0:
        data_int = np.fromstring(data, dtype=np.int16)
        x_hold = rms(data_int)
        x_submit = (x_hold * 100) // 1
        loud.append(int(x_submit))
        data = wf.readframes(CHUNK)
    return loud

loudRating = getDB()
print(loudRating)
