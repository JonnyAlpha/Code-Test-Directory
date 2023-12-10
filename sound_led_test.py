# Sound_level - this program reads the output volume level and stores it as a variable rms
# We then check the value of rms and if greater than a specific value (we have sound) we turn on an LED
# Needs to be tested on a Pi

import tkinter as tk
from tkgpio import TkCircuit

# initialize the circuit inside the GUI

configuration = {
    "width": 300,
    "height": 200,
    "leds": [
        {"x": 50, "y": 40, "name": "LED 1", "pin": 21},
        {"x": 100, "y": 40, "name": "LED 2", "pin": 22}
    ],
    "buttons": [
        {"x": 50, "y": 130, "name": "Press to toggle LED 2", "pin": 11},
    ]
}

circuit = TkCircuit(configuration)
@circuit.run

def main ():
    
    # now just write the code you would use on a real Raspberry Pi

    from gpiozero import LED
    import pyaudio
    import audioop
    from time import sleep

    # Initialize the GPIO pins
    led = LED(21)
    # Turn off LED
    led.off()

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
        if rms > 200:
            print("Sound Detected")
            led.on()
            sleep(0.25) 
            led.off()
    stream.stop_stream()
    stream.close()
    p.terminate()

main()