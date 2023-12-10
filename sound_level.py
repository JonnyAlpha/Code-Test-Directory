# Sound_level - this program reads the output volume level and shows it as an integer

import pyaudio
import audioop

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 60

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)


for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK, 
                       exception_on_overflow=False)
    rms = audioop.rms(data, 2)   
    print(rms)

stream.stop_stream()
stream.close()
p.terminate()