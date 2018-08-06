#Google STT(from Virtual assist pdf)


import speech_recognition as sr
import webbrowser as wb
import RoboResponses
import speak
import time, os

#global reply_msg


lang = 'en'
alert = 'Beep.wav'


chrome_path = '/usr/bin/chromium-browser %s'


def main():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #os.system('aplay '+ alert)
        print("Say something!")
   
    
        audio = r.listen(source)
        # recognize speech using Google Speech Recognition

    try:
        # for testing purposes, you're just using the default API key
        # to use another API key, use `r.recognize_google(audio,key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`

        text = r.recognize_google(audio)
        print("Google thinks,  you said... " + text )
        #text = "salaam Alaikum"
        reply_msg1 = RoboResponses.responses(text)
        print("Robo Response : " + reply_msg1)
        #text = 'hello, its a surprise for me'
        speak.tts(reply_msg1,lang)
        
        main()
    

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        main()
    
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service;{0}".format(e))
        main()
        
        
        
        
main()


    
    