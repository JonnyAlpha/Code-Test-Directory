import pyttsx3
import speech_recognition as sr
from moviepy.editor import *
from time import sleep

# initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# generate audio from text
text = "Hello, how are you doing today?"
engine.say(text)
engine.runAndWait()
print("Text to speech")
sleep(1)

# use speech recognition to transcribe the audio
r = sr.Recognizer()
with sr.AudioFile('temp_audio.wav') as source:
    audio = r.record(source)
    transcription = r.recognize_google(audio)
print("Did I save the audio?")
# load avatar image and create video clip with mouth animation
avatar = ImageClip('avatar.png').set_duration(len(transcription))
mouth = ImageClip('mouth.png').set_duration(len(transcription)).subclip(0, len(transcription)/10)
final = CompositeVideoClip([avatar, mouth.set_position(('center', 'bottom'))])

# add audio to video clip and render final video
audio = AudioFileClip('temp_audio.wav')
final.set_audio(audio)
final.write_videofile('output.mp4', fps=30)
