for i in range(6):
    if(i==1):
        for l in range(4):
            print(' ',end='')
        for j in range(1):
            print('4')
    elif(i==2):
        for l in range(3):
            print(' ',end='')
        for j in range(3):
            if(j%2==0):
                print('2',end='')
            elif(j%2==1):
                print('4',end='')
        print()
    elif(i==3):
        for l in range(2):
            print(' ',end='')
        for j in range(5):
            if(j%2==0):
                print('4',end='')
            elif(j%2==1):
                print('2',end='')
        print()
    elif(i==4):
        for l in range(1):
            print(' ',end='')
        for j in range(7):
            if(j%2==0):
                print('2',end='')
            elif(j%2==1):
                print('4',end='')
        print()
    elif(i==5):
        for j in range(9):
            if(j%2==0):
                print('4',end='')
            elif(j%2==1):
                print('2',end='')
        print()