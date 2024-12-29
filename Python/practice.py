print("HEllo","World")
print("hello"+"World")

age=int(input("enter age: "))
salary=float(input("enter salary: "))
print("Hello, name is Ram, Age is :"+str(age),"Salary is :",salary) 
# used both here                     +         and          ,


# one liner codes if else and others:
# quizlink:https://play.novelvista.com/quiz-lobby/0179ae72-b1e2-4412-8787-16185608d7d6.co.in


# st1 if <condition> else st2
print ("Hello") if True else print("World")
print ("Hello") if False else print("World")
# another example
food=input("enter food name cake or tea: ")
choice= "Yes" if food=="cake" else "No"
print(choice)

# clever if ternary operator
# <var>= (false val, true val) [<condition>] remember the square brackets
age=int(input("enter age: "))
allowed=("No","Yes") [ age>18 ]
print("allowed: ",allowed)

sal=float(input("Enter salary: "))
tax=(0.1,0.2) [sal>50000]
print("Your tax is:",tax*sal)
# this is also corect
taxx=sal*(0.1,0.2) [sal>50000]
print("Your taxx is:",taxx)

# get info about all operators
print(5+3)

# Type conversion(automatic) and type casting(manual)
a=4
b=4.5
print(a+b)
# type casting
a=4
b="4.5"
print(a+float(b))

# input in python is always a String convert it while input to use it wisely..#deone..
age=input("enter your age: ")
print(type(age),age)
sal=float(input("Enter sal: "))
print(type(sal),sal)

# new topic remainder thing
Numerator---: + - + -
Denominator-: + - - +
result------: + + - +
# if num is positive and deno is negativ3e then remainder is -ve.

+ for concat.
len(str)

# escape characters
\n
etc.
# ?pyhton string example
str1="mahesh"
str2='suresh'
str3="""Ganesh"""
len1=len(str1)
final=(str1+ " " + str2 + " " + str3 + "\n"+"dinesh")
print(len1)
print(final)
print(len(final))
print(len("\n"))
# we cann access chars with index
print(str[1])
str[1]="@" X not possible.
# but we cannot change the values..string is immutable.

# slicing in Python used for Machine Learning. does no tinclude the outer index.
str1="mahesh suresh"
print(str1[0:])
print(str1[0:6]) last index is not included
print(str1[7:])
print(str1[0:len(str1)]) 
# ```to access last index```




