num = 100
if num>10:
    print("Number is greater than 10")
    print("This is inside the if block")
elif num == 10:
    print("Number is equal to 10")
elif num == 100:
    print("Number is equal to 100")
else: # Else block in the end is not mandatory, you can have multiple elif blocks but only one else block and it should be at the end of the if-elif ladder.
    print("Number is less than 10")
print("This is outside the if block")

n1 = int(input("enter any no.: "))
if n1 > 0:
    print("Number is positive")
    if n1 % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")
elif n1 == 0:
    print("Number is zero")
else:
    print("Number is negative")
    if n1 % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")