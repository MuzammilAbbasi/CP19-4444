def sidesquare():
    rows = int(input('How many rows you want : '))
    num1 = input('Enter 1st For Shape : ')
    num2 = input('Enter 2nd For Shape : ')
    k = rows
    u = 1
    h = 2
    n = 1
    for i in range(1,rows+1):
        for l in range(k):
            print(' ',end=' ')
        k = k-1
        for j in range(1,u+1):
            if(j == n or (n%rows) == 0):
                print(num1,end=' ')
            else:
                print(num2,end=' ')
        n = n+1
        print()
        u = 2+u
    u = u-2
    n = n-3
    for i in range(1,rows):
        for l in range(h):
            print(' ',end=' ')
        h = h+1
        u = u-2
        for j in range(u):
            if(j == n):
                print(num1,end=' ')
            else:
                print(num2,end=' ')
        n -= 1
        print()

sidesquare()
