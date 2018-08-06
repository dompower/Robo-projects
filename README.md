++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

git clone http://people.csail.mit.edu/hubert/git/pyaudio.git

cd pyaudio

sudo python setup.py install

sudo apt-get install libportaudio-dev

sudo apt-get install python-dev

sudo apt-get install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev

sudo pip3 install SpeechRecognition

sudo apt-get install flac

sudo pip3 install pyaudio



++++++++++++++++++++
STT (Speech to Text)
STT.py


#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
 


import speech_recognition as sr
from gtts import gTTS
#quiet the endless 'insecurerequest' warning
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
 
from pygame import mixer
mixer.init()
 
while (True == True):
# obtain audio from the microphone
  r = sr.Recognizer()
  with sr.Microphone() as source:
    #print("Please wait. Calibrating microphone...")
    # listen for 1 second and create the ambient noise energy level
    r.adjust_for_ambient_noise(source, duration=1)
    print("Say something!")

    # tts1 = gTTS(text="Say something" , lang='en')
    # tts1.save("response1.mp3")
    # mixer.music.load('response1.mp3')
    # mixer.music.play()


    audio = r.listen(source,phrase_time_limit=5)
 
# recognize speech using Sphinx/Google
  try:
    #response = r.recognize_sphinx(audio)
    response = r.recognize_google(audio)
    print("I think you said '" + response + "'")
    tts = gTTS(text="I think you said "+str(response), lang='en')
    tts.save("response.mp3")
    mixer.music.load('response.mp3')
    mixer.music.play()
 
 
  except sr.UnknownValueError:
    print("Sphinx could not understand audio")
  except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))




+++++++++++++++++++++++++++++++++++++++++++++++++++++


+++++++++++++++++
TTS (Text to Speech)
Before running  TTS.py (text to speech)
pip3 install gTTS

apt-get install mpg321

chmod 777 text1.py

++++++++++++++
must run TTS.py as python3 TTS.py from your folder
TTS.py


#This works for any platform.
#Now we are all set to write a sample program that converts text to speech.
# Import the required module for text 
# to speech conversion 
from gtts import gTTS
 
# This module is imported so that we can 
# play the converted audio
import os
 
# The text that you want to convert to audio
#mytext = 'Hi shobha,I'd like you to join me and 500 growth marketers at our upcoming Transform event August 21 & 22 at the beautiful Seminary at Strawberry in Mill Valley, CA. Transform is the AI ev$

mytext = 'Welcome, Dominic ... all the best' 
# Language in which you want to convert
language = 'en'
 
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)
 
# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("welcome.mp3")
 
# Playing the converted file
os.system("mpg321 welcome.mp3")
























+++++++++++++++++++++++++++++++++++++++++++++++++++++

# speech2text
# scraper
# web_speech2text
# speak
# GUI STT

Use Google Speech Recognition API to convert your speech into text
Google Speech recognition automatically recognizes your spoken words and display them in the form of text.

Prerequisites:
  
  Python installed; 
  Google Speech Recognition API installed; 
  Active Internet Connection (The faster the better)
  Beautiful Soup (bs4)
  Pyglet
  GTTS (Google Text to Speech)


Download Python:
  https://www.python.org/downloads/
  
Download Goolge SpeechRecognition:
  https://pypi.python.org/pypi/SpeechRecognition/
  
                              OR
Install using PIP:

      pip install SpeechRecognition
  
      pip install bs4
  
      pip install pyglet
  
      pip install gtts
  
      pip install pygame
 
 Install all these dependencies and run any of the given programs, that will run Perfectly.
 
