for i in range(10):
    if(i==1):
        for l in range(4):
            print(' ',end='')
        for j in range(1):
            print('7')
    elif(i==2):
        for l in range(3):
            print(' ',end='')
        for j in range(4):
            if(j==1 or j==3):
                print('6',end='')
            elif(j==2):
                print('7',end='')
        print()
    elif(i==3):
        for l in range(2):
            print(' ',end='')
        for j in range(1,6):
            if(j==3):
                print('7',end='')
            else:
                print('6',end='')
        print()
    elif(i==4):
        for l in range(1):
            print(' ',end='')
        for j in range(1,8):
            if(j==4):
                print('7',end='')
            else:
                print('6',end='')
        print()
    elif(i==5):
        for j in range(1,10):
                print('7',end='')
        print()
    elif(i==6):
        for l in range(1):
            print(' ',end='')
        for j in range(1,8):
            if(j==4):
                print('7',end='')
            else:
                print('6',end='')
        print()
    elif(i==7):
        for l in range(2):
            print(' ',end='')
        for j in range(1,6):
            if(j==3):
                print('7',end='')
            else:
                print('6',end='')
        print()
    elif(i==8):
        for l in range(3):
            print(' ',end='')
        for j in range(4):
            if(j==1 or j==3):
                print('6',end='')
            elif(j==2):
                print('7',end='')
        print()
    elif(i==9):
        for l in range(4):
            print(' ',end='')
        for j in range(1):
            print('7')