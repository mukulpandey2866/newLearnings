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
    print("11. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        for i in range(40,19,-1):
            if i % 2 == 0:
                print(f"Square of {i} is: {i**2}")

    elif choice == 2:
        for i in range(40,19,-1):
            if i % 2 == 0:
                print(f"Square of {i} is: {i**2}")

    elif choice == 3:
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            print(f"Square of {num} is: {num**2}")
        else:
            print(f"Cube of {num} is: {num**3}")

    elif choice == 4:
        n = int (input("Enter a number: "))
        for i in range(1, n+1):
            print(i**3)
    
    elif choice == 5:
        n = int (input("Enter a number: "))
        for i in range(1, n+1):
            if i % 2 == 0:
                print(i**2)
            else:
                print(i**3)

    elif choice == 6:
        n = int(input("Enter a number: "))




    if choice == 11:
        break
print("Thank you for using the program.")