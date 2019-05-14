number = int(input("Enter number you want: "))
Previous_1 = 0
Previous_2 = 1
print(Previous_1," , ",Previous_2,end=" , ")
for i in range(1,number):
    Next = Previous_1 + Previous_2
    print(Next, end=" , ")

    Previous_1 = Previous_2
    Previous_2 = Next
    
