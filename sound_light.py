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
    # Sound to light program for Dalek dome lights
    from gpiozero import LED

    # Initialize the GPIO pins
    led =LED(2)
    # Turn off LED
    led.off()


    # Create an ALSA audio input object
    audio = alsaaudio.PCM(alsaaudio.PCM_CAPTURE)
    audio.setformat(alsaaudio.PCM_FORMAT_S16_LE)
    audio.setrate(44100)
    audio.setperiodsize(160)

    #Threshold for sound detection
    SOUND_THRESHOLD = 5000

    try:
        while True:
            # Read audio data
            _, data = audio.read()
            sound_level = max(abs(int.from_bytes(data,byteorder='little')))
            if sound_level > SOUND_THRESHOLD:
                led.on()
            else:
                led.off()

    except KeyboardInterrupt:
        pass
    led.off()

    












