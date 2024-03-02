import pyttsx3
import speech_recognition as sr
from moviepy.editor import *
from time import sleep

# initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)



r = sr.Recognizer()
with sr.Microphone() as source:
    print("speak")
    audio = r.listen(source)



# write audio to a WAV file
with open("microphone-results.wav", "wb") as f:
    f.write(audio.get_wav_data())

# use speech recognition to transcribe the audio
r = sr.Recognizer()
with sr.AudioFile('microphone-results.wav') as source:
    audio = r.record(source)
    transcription = r.recognize_google(audio)
print("Did I save the audio?")

# load avatar image and create video clip with mouth animation
avatar = ImageClip('reference.jpg').set_duration(len(transcription))
mouth = ImageClip('mouth.jpg').set_duration(len(transcription)).subclip(0, len(transcription)/10)
final = CompositeVideoClip([avatar, mouth.set_position(('center', 'center'))])

# add audio to video clip and render final video
audio = AudioFileClip('microphone-results.wav')
final.set_audio(audio)
final.write_videofile('output.mp4', fps=30)
