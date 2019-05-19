import math

num = input('Enter any Number')
j = 1
while(j <= 5):
    if(num != 'x'):
        num = int(num)
        m = int(math.sqrt(num))
        if(num == m*m):
          print(num,"is a Perfect Square",m)
        elif(num != m*m):
          print(num,"is Not Perfect Square")
        num = input('Enter any Number')
    elif(num == 'x'):
        break
