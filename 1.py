def func():
    rows = int(input('How many rows you want : '))
    num1 = input('Enter 1st For Shape : ')
    num2 = input('Enter 2nd For Shape : ')
    k = rows
    u = 1
    for i in range(1,rows+1):
        for l in range(k):
            print(' ',end=' ')
        k = k-1
        for j in range(u):
            if((j%2) == 1):
                print(num2,end=' ')
            else:
                print(num1,end=' ')
        u = 2+u
        print()

func()
