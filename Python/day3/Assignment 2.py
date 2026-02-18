

# 8-Write a program to input a number and check if it is divisible by both 3 and 5

x = int(input("Enter a number: "))
if x % 3 == 0 and x % 5 == 0:
    print(f"{x} is divisible by both 3 and 5.")
else:
    print(f"{x} is not divisible by both 3 and 5.")


# 9=Write a program to input a person’s age and decide if they are:

age = int(input("Enter your age: "))
if age < 13:
    print("You are a child.")
elif age >= 13 and age <= 19:
    print("You are a teenager.")
elif age >= 20 and age <= 59:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# 10-Write a program to input grade of a employee and print the Grade:

grade = int(input("Enter grade of employee: "))
if grade >= 75000:
    print("Grade: A")
elif grade >= 60000 and grade <= 74999:
    print("Grade: B")
elif grade >= 40000 and grade <= 59999:
    print("Grade: C")
else:
    print("Grade: D")

# 11-Write a program to input a year and check whether it is a leap year or not.
# (Hint: A year is leap if divisible by 400 OR (divisible by 4 but not by 100))

year = int(input("Enter a year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# Write a program to create a simple calculator that performs addition, subtraction, multiplication, and division based on user choice.
# (Hint: Take two numbers as input and then ask the user to enter +, -, *, or /)


n1 = float(input("Enter number one: "))
n2 = float(input("Enter number two: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation == '+':
    print("Sum is: ", n1 + n2)
elif operation == '-':
    print("Difference is: ", n1 - n2)
elif operation == '*':
    print("Product is: ", n1 * n2)
elif operation == '/':
    if n2 != 0:
        print("Quotient is: ", n1 / n2)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation.")



# ord and chr functions
ord('A')  # this will return the ASCII value of the character 'A', which is 65.
chr(65)   # this will return the character corresponding to the ASCII value 65,






