from fuzzywuzzy import fuzz
data1 = open(r'ques.txt', 'r+')
data2 = open(r'ans.txt', 'r+')
predic = []
answers = []

for u in data1: 
    predic.append(u)
for n in data2:
    answers.append(n)
print("All data loaded! ")
print("Start by typing a message !")
def call():
    inputer = input("")
    for i in predic:
        a = fuzz.partial_ratio(inputer,i)
        if inputer == ('exit' or 'bye'):
            print('bye')
            break
        elif a > 95:
            index = predic.index(i)
            o = answers[index]
            print ('Bot : ' + (answers [index]))
            call()
                
call()

data1.close()
data2.close()
