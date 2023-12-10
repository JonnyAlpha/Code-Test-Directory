# Program to show sound output as a value and print the value to a text file
# Tested and working on Macbook 10 Dec 23

import pyaudio
import audioop

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 60

p = pyaudio.PyAudio()

sound_value = [] # Create an empty list to store the output values

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

with open("output.txt", "w") as file: #Create the teaxt file to store the results
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK, 
                           exception_on_overflow=False)
        rms = audioop.rms(data, 2) 
        sound_value.append(rms) #Add the latest value to the list sound_value
        file.write(str(rms) + "\n") #Write the results to the open text file 
        print(rms)

stream.stop_stream()
stream.close()
p.terminate()