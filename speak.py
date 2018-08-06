from gtts import gTTS
#import pyglet
import time, os
from mutagen.mp3 import MP3



def tts(text, lang):
    file = gTTS(text = text, lang = lang)
    filename = 'speak1.mp3'
    file.save(filename)

 
    os.system('mpg321 '+ filename)
    
    print ('text ' + text)
    print('langs '+lang)
    
    
    music = MP3(filename)
    print(music.info.length)
    #time.sleep(music.info.length)
    os.remove(filename)


lang = 'en'


#text = 'Around a quarter of BBC revenues come from its commercial arm BBC Studios Ltd (formerly BBC Worldwide), which sells BBC programmes and services internationally and also distributes the BBCs international 24-hour English-language news services BBC World News, and from BBC.com, provided by BBC Global News Ltd.'
#tts(text,lang)

#text = 'hello, its a surprise for me'
#tts(text,lang)


#text = 'I am Dominic... I love to see you'
#tts(text,lang)

