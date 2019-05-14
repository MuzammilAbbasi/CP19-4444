X = int(input("Enter a 5 digit number: "))
reversed_order = 0
for i in range(1,6):
        
    reminder = X%10
        
    print("Reminder is:",reminder)
    X = X//10
    print("Number left:",X)
    reversed_order = reversed_order+(reminder*(10**(5-i)))
    print("Reverse order of number is",reversed_order)
