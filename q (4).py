word = input('Enter Word')
j = 1
w = 0
length = 0
while(j<=2):
    if(word == '' or word == ' '):
        break
    else:
        length = len(word) + length
        w += 1
    word = input('Enter Word')
average = length/w
print('Average length of words is',round(average,0))