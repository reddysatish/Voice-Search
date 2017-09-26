import speech_recognition as sr
from gtts import gTTS
import os
import wikipedia

# This module is imported so that we can
# play the converted audio
# get audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak:")
    audio = r.listen(source)

try:
    # The text that you want to convert to audio
    mytext = 'reddy u searched for ' + r.recognize_google(audio)

    # Language in which you want to convert
    language = 'en'

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    test = wikipedia.summary(r.recognize_google(audio), sentences=1)
    myobj = gTTS(text=test, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    myobj.save("reddy.mp3")

    # Playing the converted file
    os.system("mpg321 reddy.mp3")

except sr.UnknownValueError:
    print("Could not understand audio")
    myobj = gTTS(text="please speek clear", lang='en', slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome
    myobj.save("error.mp3")

    # Playing the converted file
    os.system("mpg321 error.mp3")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))