num =int(input('Enter Five Numbers: '))
b = num
a = 0
for l in range(5):
    r = b%10
    a = (a*10)+r
    b = b//10
print(a)
k = num - a
if(k == 0):
    print('Reversed Number Is Same')
else:
    print('Reversed Number Is Not Same')
