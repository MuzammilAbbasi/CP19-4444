print('Number Should Between 0 to 42 or Enter x for stopping program')
a = input('Enter Number : ')
p = 0
n = 0
i = 0
while(i <= 10):
    if(a == 'x'):
        break
    else:
        o = int(a)
        if(o>0):
            p = p+1
        elif(o<0):
            n = n+1
    a = input('Enter Number : ')

print('Number of Positive no: From Given Numbers',p)
print('Number of Negative no: From Given Numbers',n)