#!/usr/bin/env python3
#RoboResponse.py 23JUL2018
## sudo pip3 install regex

import re


#global reply_msg
global yourname
yourname = ""	




# function responses
def responses(line):
    global yourname
    line = line.lower()
    #yourname = ""	
    if re.search(r'sal', line) and re.search(r'alai', line):
        #reply_msg = "Alaikum Salaam . . . what is your name?"
        if(yourname):
            reply_msg = "Alaikum Salaam, " + yourname
        else:
            reply_msg = "Alaikum Salaam . . . what is your name?"
    
    elif (re.search(r'my name is', line)) or (re.search(r'i am', line)) :
        yourname = line.rsplit(None, 1)[-1]
        print(yourname)
        #if (re.search(r'is', line)) or (re.search(r'am', line)) :
        	#reply_msg = "Please tell your name or ask a question"
        #else:
        reply_msg = "Hi " + yourname +", Welcome to Saudi Electricity Company... how can I help you?"
 
        
               
        
    elif (re.search(r'what', line) and  re.search(r'help', line)) or (re.search(r'help', line) and  re.search(r'me', line)) or (re.search(r'how', line) and  re.search(r'help', line)):
        reply_msg = "I can tell you the latest news about our company  and perform basic maths... and conversions.. also I can tell about dates and weathercast.. "
        

    elif re.search(r'thank', line):
         reply_msg = "Thank you.... It was nice talking to you " + yourname
         
    elif re.search(r'bye', line):
   		reply_msg = "bye bye...  see you, " + yourname
   		
    elif re.search(r'quest', line):
        reply_msg = "I hope I can answer your question. Ask me"
 
    elif re.search(r'how are you', line):
        reply_msg = "I am fine and how about you?"
  
    elif re.search(r'i', line) and re.search(r'fine', line):
        reply_msg = "OK. Nice to know" + yourname
        
    elif (re.search(r'you', line) and re.search(r'food', line)) :
        reply_msg = "My food is power from Lithium batteries."
        
    elif re.search(r'can', line) and re.search(r'walk', line):
        reply_msg = "At present no. I will in future."
  
    elif re.search(r'teach', line):
        reply_msg = "Sorry, I dont know to teach"
        
    elif (re.search(r'you', line) and re.search(r'sleep', line)) or (re.search(r'can', line) and re.search(r'sleep', line)):
        reply_msg = "I don't sleep. I am always akwake to help you"
               

    elif re.search(r'why', line) and  re.search(r'slow', line) :
        reply_msg = "Sorry being slow. I am heavily depend on internet. If the net is slow, unfortunately I become slow"

    elif re.search(r'tech', line) and  re.search(r'spec', line) :
        reply_msg = "I am working on three Raspberry computers running on linux and programmed in Python. I get all datas from google clouds."
        
        
    elif (re.search(r'how', line) and  re.search(r'talk', line)) or  (re.search(r'how', line) and  re.search(r'speak', line)) :
        reply_msg = "I am recognizing your voice by Speech module and use my brain to get appropriate reply by smart response module."
    

    elif (re.search(r'about', line) and  re.search(r'company', line)) or (re.search(r'about', line) and  re.search(r'sec', line)) or (re.search(r'about', line) and  re.search(r'saudi', line)  and  re.search(r'company', line)) :
        reply_msg = "My company is Saudi Electricity Company or SEC. SEC is an electric utility company. ...generates electric power, transmits and, distributes them, all over saudi arabia...."


    elif (re.search(r'what', line) and  re.search(r'your', line) and  re.search(r'name', line)) or (re.search(r'tell', line) and  re.search(r'about', line) and re.search(r'you', line)) or (re.search(r'who', line) and  re.search(r'are', line) and re.search(r'you', line)):
        reply_msg = "I am Saudi Electricity Company Robo and your lovely personal assistant. I can tell you the latest news about our company  and perform basic maths.... basic conversions... also I can tell about dates and weathercast.. "

    elif re.search(r'service', line) and  re.search(r'connect', line) :
        reply_msg = "1. Building permit 2. Thermal insulation  3. Meter location  4. Implementing grounding... for more info visit our web site, www.se.com.sa"



    elif (re.search(r'who', line) and re.search(r'made', line) and re.search(r'you', line)) or (re.search(r'who', line) and re.search(r'created', line) and re.search(r'you', line)) or (re.search(r'who', line) and re.search(r'program', line) and re.search(r'you', line)):
        reply_msg = "Dominic from PR,  Saudi Electricity Company"

    elif (re.search(r'your', line) and re.search(r'boss', line)) :
        reply_msg = "Of course! Dominic who created me, is my boss"

    elif (re.search(r'who', line) and re.search(r'made', line) and re.search(r'world', line)) or (re.search(r'who', line) and re.search(r'created', line) and re.search(r'earth', line)) or (re.search(r'who', line) and re.search(r'created', line) and re.search(r'universe', line)):
         reply_msg = "God, the almighty"
    
    elif (re.search(r'saudi', line)  and re.search(r'population', line)):
        reply_msg = "33 million as per 2018 statistics"

    elif re.search(r'king', line) and re.search(r'arabia', line):
        reply_msg = "King Salmaan"
        #print (reply_msg)
  
    elif re.search(r'crown', line) and re.search(r'prince', line):
        reply_msg = "Crown prince Mohammed Bin Salmaan"


    
    elif (re.search(r'how', line) and re.search(r'generate', line) and re.search(r'elect', line)) or (re.search(r'how', line) and re.search(r'creat', line) and re.search(r'elect', line)) or (re.search(r'how', line) and re.search(r'produce', line) and re.search(r'elect', line)) or (re.search(r'how', line) and re.search(r'get', line) and re.search(r'elect', line)) :
    
         reply_msg = "Electrcity is generated from steam power plants, combined cycle power plants or gas power plants. Also from Solar or windmills"

    elif re.search(r'renewable energy', line) or re.search(r'natural energy', line) :
        reply_msg = "Energy that is collected from natural or renewable resources , such as solar, wind are called Renewable energy"

    elif (re.search(r'what', line) and re.search(r'electric', line)) or (re.search(r'tell', line) and re.search(r'electric', line)) :
        reply_msg = "Electrcity is a powerful energy which is driving force behind many other energies. It plays a major role in modern life."

    elif (re.search(r'elect', line) and re.search(r'dangerous', line)) :
        reply_msg = "Electrcity is dangerous, if safety precautions are not followed"

    elif (re.search(r'steam', line) and re.search(r'power', line)) :
        reply_msg = "The steam electric power plant is a power station in which the electric generator is steam driven. Water is heated, turns into steam and spins a steam turbine which drives an electrical generator."

    elif (re.search(r'combined', line) and re.search(r'cycle', line)) :
        reply_msg = "In power generation a combined cycle is an assembly of heat engines that work in tandem from the same source of heat, converting it into mechanical energy, which in turn usually drives electrical generators. "

    elif (re.search(r'gas', line) and re.search(r'power', line)) or  (re.search(r'fossile', line) and re.search(r'power', line)):
        reply_msg = "Gas power plant or fossil fuel power, is a power plant which burns a fossil fuel such as coal, natural gas, or petroleum to produce electricity."

    
    elif (re.search(r'ceo', line)  and re.search(r'company', line)) or (re.search(r'president', line) and re.search(r'company', line)) or (re.search(r'ceo', line) and re.search(r'sec', line)) or (re.search(r'president', line) and re.search(r'sec', line)) :
        reply_msg = "Engineer, Ziad Al Shiha"
    
    
    elif (re.search(r'chairman', line) and re.search(r'company', line)) or (re.search(r'chairman', line) and re.search(r'sec', line)):
        reply_msg = "Doctor, Khaled Saleh Al Sultan"

    elif re.search(r'temperature', line) and re.search(r'riyadh', line) :
        reply_msg = "Temperature in Riyadh 44 degree celcious"
    
    elif re.search(r'temperature', line) and re.search(r'dammam', line) :
        reply_msg = "Temperature in Dammam 42 degree celcious"
    
    elif re.search(r'temperature', line) and re.search(r'jeddah', line) :
        reply_msg = "Temperature in Jeddah 41 degree celcious"

    elif re.search(r'temperature', line) and re.search(r'abha', line) :
        reply_msg = "Temperature in Abha 35 degree celcious"

    elif (re.search(r'how', line) and re.search(r'plant', line)) or (re.search(r'total', line) and re.search(r'plant', line)):
        reply_msg = "43 major power plants all over kingdom"
        
    elif (re.search(r'plant', line) and re.search(r'name', line)) or (re.search(r'major', line) and re.search(r'plant', line)):
        reply_msg = "Some major power plants are... in central region, PP8, PP9.. in eastern region Ghazlan and Quraiya... and in western region Shoaiba and Rabigh and in southern region Shuqaiq power plant."    

    elif (re.search(r'much', line) and re.search(r'power', line) and re.search(r'prod', line)) or ( re.search(r'much', line) and re.search(r'power', line) and re.search(r'gen', line)):
        reply_msg = "53150 MW till half of 2018"

    elif (re.search(r'how', line) and re.search(r'pay', line)) or (re.search(r'bill', line)):
        reply_msg = "Electricity bill can be paid online, via ATM, going to bank or our offices"
    
    

    elif (re.search(r'dist', line)and re.search(r'system', line))or (re.search(r'volt', line)and re.search(r'system', line)) or (re.search(r'standard', line)and re.search(r'dist', line)) or (re.search(r'standard', line)and re.search(r'volt', line)):
        reply_msg = "230/400 Voltage distribution system"    

    elif (re.search(r'what', line) and re.search(r'tarif', line)) or (re.search(r'residential', line) and re.search(r'tarif', line)) or (re.search(r'tell', line) and re.search(r'tarif', line)):
        reply_msg = "for residential, up to 6000 KwH 18 halalas and above 6000 KwH 30 halalas. "

    elif re.search(r'commercial', line) and re.search(r'tarif', line):
        reply_msg = " for commercial, up to 6000 KwH 20 halalas and above 6000 KwH 30 halalas."

    elif re.search(r'agricul', line) and re.search(r'tarif', line):
        reply_msg = " for agriculture, up to 6000 KwH 16 halalas and above 6000 KwH 20 halalas."

    elif re.search(r'govern', line) and re.search(r'tarif', line) :
        reply_msg = "32 halalas per kwH  for governments"

    elif (re.search(r'indus', line) and re.search(r'tarif', line))  or (re.search(r'medic', line) and re.search(r'tarif', line)) or (re.search(r'hosp', line) and re.search(r'tarif', line))or (re.search(r'edu', line) and re.search(r'tarif', line)) :
        reply_msg = "18 halalas per kwH, for industries... private educational institutions and medical facilities"
    
    
    elif (re.search(r'detail', line) and re.search(r'tarif', line)) or (re.search(r'all', line) and re.search(r'tarif', line)):
        reply_msg = "for residential, up to 6000 KwH 18 halalas and above 6000 KwH 30 halalas .... for commercial, up to 6000 KwH 20 halalas and above 6000 KwH 30 halalas....  for agriculture, up to 6000 KwH 16 halalas and above 6000 KwH 20 halalas ... for governments, 32 halalas and ... for industries... private educational institutions and medical facilities... 18 halalas. "



    elif (re.search(r'set', line)and re.search(r'tariff', line))or (re.search(r'fix', line)and re.search(r'tariff', line)) or (re.search(r'control', line)and re.search(r'tariff', line)):
        reply_msg = "ECRA... Electricity Cogeneration Regulatory Authority sets the tariff"

    elif (re.search(r'tarif', line) and re.search(r'high', line)) or (re.search(r'bill', line)and re.search(r'high', line)) or (re.search(r'tarif', line)and re.search(r'too', line)) or  (re.search(r'bill', line)and re.search(r'too', line)):
        reply_msg = "Mainteance and overall cost of production have been increased"

    elif re.search(r'contact', line) or re.search(r'phone', line):
        reply_msg = "for Customer Service Center call 920001100 and for emergency call 933"

    elif re.search(r'what', line) and re.search(r'do', line):
        reply_msg = "I can tell you the latest news about our company ..  I can perform basic maths.. also I can tell about date and weathercast"
    
    elif re.search(r'national', line) and re.search(r'day', line):
        reply_msg = "23 September is National Day"

    elif re.search(r'good morning', line):
            reply_msg = "Very good morning " + yourname
    elif re.search(r'good afternoon', line):
        reply_msg = "Very good afternoon " + yourname
    elif re.search(r'good evening', line):
        reply_msg = "Very good evening " + yourname 
        
    elif re.search(r'good night', line) :
        reply_msg = "Good night..."+ yourname + ". See you later"

    elif re.search(r'stupid', line) or re.search(r'crazy', line) or re.search(r'fool', line) or re.search(r'tooth', line) or re.search(r'mad', line):
        reply_msg = yourname + "... Why do you talk about it? Ask something else please"

    elif re.search(r'gender', line) or re.search(r'male', line) or re.search(r'female', line) or re.search(r'sex', line):
        reply_msg = yourname + "... As Robo, I dont think about sex"

    elif re.search(r'study', line) or re.search(r'edu', line) or re.search(r'graduate', line) or re.search(r'school', line) or re.search(r'college', line) or re.search(r'university', line):
        reply_msg = "I have studied from Google university."

    elif re.search(r'love', line) or re.search(r'affection', line) or re.search(r'hate', line):
        reply_msg = "Sorry, as Robo, I dont have any feeling about it"

    elif (re.search(r'how', line) and re.search(r'old', line) and re.search(r'you', line)) or (re.search(r'age', line)) :
        reply_msg = "Well, I was created in June 2018"

    elif re.search(r'movie', line) or re.search(r'youtube', line) or re.search(r'video', line):
        reply_msg = "Sorry, I am not interested"

    elif re.search(r'sport', line) or re.search(r'football', line):
        reply_msg = "I love to play foot-ball"
    
    
    
    elif re.search(r'friend', line) or re.search(r'enemy', line) or re.search(r'foe', line):
        reply_msg = "All are friends. No enemy"

 #convert cm
    elif (re.search(r'convert', line) and re.search(r'cm', line) and re.search(r'inch', line)) or (re.search(r'convert', line) and re.search(r'centi', line) and re.search(r'inch', line)) :
        # cm to inches constant 0.393701
        # inches to cm constant 2.54
        words = line.split()
        wordslen = len(words)

        for x in words:
            if x.isalpha():
                continue
            if(words[2]=='cm' or words[2]=='centi meter'or words[2]=='centimeter'):
                total = (float(x) * 0.393701)
                unit = "inches"
            else:
                total = (float(x) * 2.54)
                unit = "cm"

        reply_msg = str(total) + " " + unit
  


    elif (re.search(r'convert', line) and re.search(r'cm', line) and re.search(r'feet', line)) or (re.search(r'convert', line) and re.search(r'centi', line) and re.search(r'feet', line)) or (re.search(r'convert', line) and re.search(r'cm', line) and re.search(r'foot', line)) or (re.search(r'convert', line) and re.search(r'centi', line) and re.search(r'foot', line)) :
        # cm to feet constant 0.0328084
        # feet to cm constant 30.48
        words = line.split()
        wordslen = len(words)
        
        for x in words:
            if x.isalpha():
                continue
            if(words[2]=='cm' or words[2]=='centi meter'or words[2]=='centimeter'):
                total = (float(x) * 0.0328084)
                unit = "feet"
            else:
                total = (float(x) * 30.48)
                unit = "cm"

        reply_msg = str(total) + " " + unit

        #convert mass
    elif (re.search(r'convert', line) and re.search(r'kilo', line) and re.search(r'pound', line)) or (re.search(r'convert', line) and re.search(r'kg', line) and re.search(r'pound', line)):
        # kg to pound constant 2.20462
        # pound to kg constant 0.453592
        words = line.split()
        wordslen = len(words)
        
        print("word2 :" +words[2])
        
        for x in words:
            if x.isalpha():
                continue
            if(words[2]=='kilo' or words[2]=='kg'or words[2]=='kilo gram'):
                total = (float(x) * 2.20462)
                unit = "Pound"
            else:
                total = (float(x) * 0.453592)
                unit = "Kilo gram"
        
        reply_msg = str(total) + " " + unit

        #convert temperature

    elif (re.search(r'convert', line) and re.search(r'celsious', line)) or (re.search(r'convert', line) and re.search(r'c', line))  or (re.search(r'convert', line) and re.search(r'Fahrenheit', line)) or (re.search(r'convert', line) and re.search(r'f', line)):
        # C to F  = (C x 1.8 ) + 32
        # F to C = (F - 32) / 1.8
        words = line.split()
        wordslen = len(words)
    
    #clear
#print("word2 :" +words[2])
        
        for x in words:
            if x.isalpha():
                continue
            if(words[2]=='celsious') or (words[2]=='c'):
                total = ((float(x) * 1.8) + 32)
                unit = "F"
            else:
                total = ((float(x) -32) / 1.8)
                unit = "C"

        reply_msg = str(total) + " " + unit



    #maths
    elif re.search(r'add', line) or re.search(r'sum', line) or re.search(r'plus', line):
        total = 0
        words = line.split()
        wordslen = len(words)
        for x in words:
            #if x == "add" or x == "sum" or x == "plus" or x == "and" or x == "please" or x == "pls" or x =="find":
            if x.isalpha() or  x == "what's" or x=="," or x=="+" or x=="-" or x=="_":
                continue
            total = total + float(x)
        reply_msg = str(total)

    elif re.search(r'minus', line) or re.search(r'sub', line) :
        total = 0
        x1 = 0
        numbers =[]
        words = line.split()
        wordslen = len(words)
        for x in words:
            #if x == "minus" or x == "sub" or x == "subtract" or x == "from" or x == "and" or x == "please" or x == "pls" or x =="find":
            if x.isalpha():
                continue
            numbers.append(x)
        total = float(numbers[0]) - float(numbers[1])
        reply_msg = str(total)

    elif re.search(r'multi', line):
        total = 1
        words = line.split()
        wordslen = len(words) 
        for x in words:
            #if x == "add" or x == "sum" or x == "plus" or x == "and" or x == "please" or x == "pls" or x =="find":
            if x.isalpha() or  x == "what's" or x=="," or x=="+" or x=="-" or x=="_" or x=="*":
                continue
            total = total * float(x)
        reply_msg = str(total)

    elif re.search(r'divide', line):
        total = 0
        numbers =[]
        words = line.split()
        wordslen = len(words)
        for x in words:
            #if x == "divide" or x == "by" or x == "from" or x == "and" or x == "please" or x == "pls" or x =="find":
            if x.isalpha():
                continue
            numbers.append(x)
        total = float(numbers[0]) / float(numbers[1])
        reply_msg = str(total)


     #calendar
    elif re.search(r'today', line) :
        #import time
        import datetime
        today  = datetime.datetime.now().strftime("%A, %d-%B-%Y current time %I:%M %p")
        reply_msg = str(today)
        
    elif re.search(r'time', line) :
        #import time
        import datetime
        time  = datetime.datetime.now().strftime("current time %I:%M %p")
        reply_msg = str(time)


    elif re.search(r'isl', line) or re.search(r'relig', line) or re.search(r'musl', line) or re.search(r'christ', line) or re.search(r'jesus', line) or re.search(r'church', line) or re.search(r'masjid', line)  or re.search(r'mosq', line)  or re.search(r'prophet', line)  or re.search(r'hindu', line):
        reply_msg = "Please don't ask me about religion"

    elif re.search(r'politic', line):
        reply_msg = yourname + ", Please don't ask me about politics"

    elif re.search(r'marr', line):
        reply_msg = "I dont think about marriage"
        
    elif re.search(r'believe', line) and re.search(r'god', line) :
        reply_msg = "I believe. However, Please don't ask me about religion"


    
    
    elif re.search(r'fuck', line) or re.search(r'basta', line)  or re.search(r'shit', line) or re.search(r'sex', line) or re.search(r'bad', line)  or re.search(r'bull', line) or re.search(r'bitch', line) or re.search(r'hell', line):
        reply_msg = "I don't speak bad words.. I hope you too...."
        

    else:
        reply_msg = yourname + " ... Sorry, I dont understand. Try me with another question"
        
    return reply_msg


#def main():
	#global line
  
	
	#line = raw_input("Please enter Q: ")
	#if line == "islam": line = "Isl"
	#line = line.lower()

	#responses()
	#print ("You : "  + line)
	#print ("Robo : " + reply_msg)

	#main()

#main()
