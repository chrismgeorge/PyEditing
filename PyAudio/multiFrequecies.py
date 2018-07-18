import pyaudio
import numpy as np
import wave
import math

CHUNK = 1024 * 4
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

wf = wave.open('test.wav', 'rb')
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
    resizeSize = 8
    while len(data) != 0:
        data_int = np.fromstring(data, dtype=np.int16)
        wf_data = np.array(data_int)[::]
        # wf_data = np.array(wf_data) - 128
        # wf_data = wf_data * 0.04
        wf_data = wf_data.tolist()
        if (len(wf_data) == 8192):
            curFrame = []
            for i in range(4):
                curBit = wf_data[:(i+1)*1024]
                x_hold = rms(curBit)
                x_submit = (x_hold * 100) // 1
                curFrame.append(int(x_submit))
        loud.append(curFrame)
        
        data = wf.readframes(CHUNK)
    return loud

loudRating = getDB()
print(loudRating)
