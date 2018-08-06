import speech_recognition as sr
import webbrowser as wb
import speak

chrome_path = '/usr/bin/chromium-browser %s'


r = sr.Recognizer()
with sr.Microphone() as source:
    print ('Say Something!')
    audio = r.listen(source)
    print ('Done!')

try:

    text = r.recognize_google(audio)
    print ('I think :\n' + text)
    lang = 'en'
    
    
    speak.tts(text, lang)
    
    f_text = 'https://wwww.google.com/search?q=' + text
    wb.get(chrome_path).open(f_text)

except sr.UnknownValueError:
    print("Google Speech could not understand audio")
except sr.RequestError as e:
    print("Could not reqeust results from Google Speech Recognition service; {0}".format(e))


