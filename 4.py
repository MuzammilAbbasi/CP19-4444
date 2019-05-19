def func():
    num = int(input('Write numbers in series '))
    a = 0
    b = 1
    print(a,',',b,end=' , ')
    for l in range(num):
        if(l%2==1):
            c = a + b
            b = c
            print(b,end=' , ')
        elif(l%2==0):
            c = a + b
            a = c
            print(a,end=' , ')
    print()

func()
