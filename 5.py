c = 4
while(c <= 5):
    chat = input('Ask Question : ')
    if(chat=='quit'):
        print('bye')
        break
    else:
        if('country name' in chat):
            print('Pakistan')
        elif('your name' in chat):
            print('m-0.2-version')
        elif('city name' in chat):
            print('Karachi')
        elif('how are you' in chat):
            print('Fine,I am glad You Ask.Thank You!!!')
        elif('who are you' in chat):
            print('I am ChatBot Created By Brilliant Programmer')
        elif('university name' in chat):
            print('Mohammad Ali Jinnah University')
        elif('joke' in chat):
            print('My friend said he knew a man with a wooden leg named Smith.So I asked him "What was the name of his other leg?"')
        elif('riddle' in chat):
            print("Brothers and sisters I have none but this man's father is my father's son.Who is the man?")
            print("Answer : man's son")
        elif('sad' in chat):
            print("Don't be sad,hard times are parts of life")
        else:
            print('I am not sure I can give the answer')
        