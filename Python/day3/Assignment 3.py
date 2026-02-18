"""
Docstring for day 3.Assignment 3

Problems on Loop

1.Print square of all even numbers between 40-20
2.Print square of all even numbers between 40-20
3.Accept number from user if it is odd calculate cube else calculate square.
4.Print Series 1,8,27,64,125....n
5.Print Series 1,4,27,16,125....n
6.0,1,1,2,3,5,8,13...n
7.Check whether prime or not
8.Count no of digits from a number.
9.Find the sum of all digits in entered number
10.Accept any number and find out whether it is Armstrong or not.
11. Exit

"""

while(True):
    print("\n\nOperation List: ")
    print("1.Print square of all even numbers between 40-20")
    print("2.Print square of all even numbers between 40-20")
    print("3.Accept number from user if it is odd calculate cube else calculate square.")
    print("4.Print Series 1,8,27,64,125....n")
    print("5.Print Series 1,4,27,16,125....n")
    print("6.0,1,1,2,3,5,8,13...n")
    print("7.Check whether prime or not")
    print("8.Count no of digits from a number.")
    print("9.Find the sum of all digits in entered number")
    print("10.Accept any number and find out whether it is Armstrong or not.")
    print("11. Exit \n")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        for i in range(40,19,-1):
            if i % 2 == 0:
                print(f"{i**2}",end=",")

    elif choice == 2:
        for i in range(40,19,-1):
            if i % 2 == 0:
                print(f"{i**2}",end=",")

    elif choice == 3:
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            print(f"Square of {num} is: {num**2}")
        else:
            print(f"Cube of {num} is: {num**3}")

    elif choice == 4:
        n = int (input("Enter a number: "))
        for i in range(1, n+1):
            print(f"{i**3}",end=",")
    
    elif choice == 5:
        n = int (input("Enter a number: "))
        for i in range(1, n+1):
            if i % 2 == 0:
                print(f"{i**2}",end=",")
            else:
                print(f"{i**3}",end=",")

    elif choice == 6:
        n = int(input("Enter a number: "))
        a = 0
        b = 1
        print(f"{a},{b}",end=",")
        while(n-2):
            n -= 1
            print(f"{a + b}",end=",")
            temp = a
            a = b
            b = temp + b

    elif choice == 7:
        n = int(input("Enter a number: "))
        flag = 0
        if n <= 1:
            print("Enter a positive Number")
        else:
            for i in range(2,int(n/2)):
                if(n % i == 0):
                    flag = 1
            if flag == 1:
                print("Number is not Prime")
            else:
                print("Number is prime")

    elif choice == 8:
        n = int(input("Enter a number: "))
        count = 0
        while(n > 0):
            count += 1
            n = int(n / 10)
        print("No of digits: ",count)

    elif choice == 9:
        n = int(input("Enter a number: "))
        digiSum = 0
        while(n > 0):
            x = int(n % 10)
            digiSum += x
            n = int(n / 10)
        print("Sum of Digits is: ",digiSum)
    
    elif choice == 10:
        n = int(input("Enter a number: "))
        power = 0
        x = n
        while(x > 0):
            power += 1
            x = int(x / 10)
        arms = 0
        y = n
        while(y > 0):
            x = int(y % 10)
            arms += x**power
            y = int(y / 10)
        if arms == n:
            print("The Number is an Armstrong one")
        else:
            print("Not an Armstrong number")

    if choice == 11:
        break
print("Thank you for using the program.")

# def fibo( n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         print(fibo(n-1) + fibo(n-2))
