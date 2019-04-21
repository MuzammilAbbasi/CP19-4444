n = input('Enter Number with commas : ')
n = n+','
w = ''
maxi = 0
mini = 1111111111111111111111111
for l in n:
    if(l!=','):
        w += l
        o = int(w)
    elif(l==','):
        if(maxi<o):
            maxi = o
        if(mini>o):
            mini = o
        w = ''
    
print('maximum',maxi)
print('minimum',mini)