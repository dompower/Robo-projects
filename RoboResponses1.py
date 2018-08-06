#!/usr/bin/env python3
#RoboResponse.py 23JUL2018
## sudo pip3 install regex



import re

#global yourname
#global reply_msg
reply_msg = "ddd"


# function responses
def responses(line):
    line = line.lower()
    yourname = " ++ "
    #global reply_msg
    #line="salaam Alaikum"
    
    if re.search(r'sal', line) and re.search(r'alai', line):
        reply_msg = "Alaikum Salaam . . . what is your name?"
        
        #print("asdasdasd")
        
        
    
    elif (re.search(r'my name is', line)) or (re.search(r'i am', line)) :
        yourname = line.rsplit(None, 1)[-1]
        print(yourname)
        reply_msg = "Hi " + yourname +", Welcome to Saudi Electricity Company... how can I help you?"
     
                  
        
    elif (re.search(r'what', line) and  re.search(r'help', line)) or (re.search(r'help', line) and  re.search(r'me', line)) or (re.search(r'how', line) and  re.search(r'help', line)):
        reply_msg = "I can tell you the latest news about our company  and perform basic maths... and conversions.. also I can tell about dates and weathercast.. "
        
    elif re.search(r'bye', line):
        reply_msg = "bye bye...  see you, " + yourname
      
    
    else:
        reply_msg = yourname + " ... Sorry, I dont understand. Try me with another question"

    return reply_msg