from fuzzywuzzy import fuzz
data1 = open(r'C:\Users\RukmanAly\Desktop\ques.txt', 'r+')
data2 = open(r'C:\Users\RukmanAly\Desktop\ans.txt', 'r+')

def reach ():
    a = input("Enter the question? ")
    print (a)
    if a == "Exit":
        return
    data1.write(str(a)+'\n')
    b = input("Enter the answer for "+a+" ")
    print (b)
    data2.write(str(b)+'\n'),
    reach()




predic = []
answers = []


for u in data1: 
    predic.append(u)
for n in data2:
    answers.append(n)
    print(" All data loaded! ")
print("Start by typing a message !")
def call():
    inputer = input("")
    for i in predic:
        a = fuzz.partial_ratio(inputer,i)
        if a > 90:
            index = predic.index(i)
            print ('Bot :' + (answers [index]))
            call()
                
call()

data1.close()
data2.close()
