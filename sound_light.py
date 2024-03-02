
import alsaaudio

def main ():
    
    # now just write the code you would use on a real Raspberry Pi
    # Sound to light program for Dalek dome lights
    from gpiozero import LED
    import time
    import alsaaudio

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
            #sound_level = max(abs(int.from_bytes(data,byteorder='little')))
            sound_level = max(abs(int.from_bytes(data,byteorder='little')))
            if sound_level > SOUND_THRESHOLD:
                led.on()
            else:
                led.off()

    except KeyboardInterrupt:
        pass
    led.off()

main()
    












