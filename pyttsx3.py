import pyttsx3
i = pyttsx3.init()
l = 3

while(l<=5):
    a = input('Enter Message : ')
    if(a=='exit'):
        break
    else:
        i.say(a)
        i.runAndWait()