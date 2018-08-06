#Google STT(from Virtual assist pdf)


#import webbrowser as wb
import RoboResponses

#global reply_msg


lang = 'en'
alert = 'Beep.wav'

def main():
    text="My name is Dominic"
    text = input("Enter Q : ")
    print("you said... " + text )

    reply_msg1 = str(RoboResponses.responses(text))
    print("Robo Says : " + reply_msg1)
    main()

main()

    