import speech_recognition as sr
import webbrowser
from gtts import gTTS
import os


# This module is imported so that we can
# play the converted audio
# get audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak:")
    audio = r.listen(source)

try:
    print("You said " + r.recognize_google(audio))

    # Import the required module for text
    # to speech conversion
    # The text that you want to convert to audio
    mytext = 'reddy u searched for ' + r.recognize_google(audio)

    # Language in which you want to convert
    language = 'en'

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    myobj = gTTS(text=mytext, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome
    myobj.save("reddy.mp3")

    # Playing the converted file
    os.system("mpg321 reddy.mp3")
    url = "https://www.google.com.tr/search?q="
    query = r.recognize_google(audio)
    # # MacOS
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    # # Windows
    # # chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'

    # # Linux
    # # chrome_path = '/usr/bin/google-chrome %s'

    # webbrowser.get(chrome_path).open(query)
    webbrowser.open_new(url + query)
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


# try:
#     from google import search
# except ImportError:
#     print("No module named 'google' found")

# to search


# for j in search(query, tld="co.in", num=2, stop=1, pause=2):
#     print(j)
#     url = j
#     break;
# # url = 'http://docs.python.org/'
