jwejhhjananhunjsjsrrgjsjwfffywyjghGe hshahgghhhajshprint("HEllo","World")
print("hello"+"World")

age=int(input("enter age: "))
salary=float(input("enter salary: "))
print("Hello, name is Ram, Age is :"+str(age),"Salary is :",salary) 
# used both here                     +         and          ,
# comment 1

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

# Type conversion(automatic) and type casting(manual)fgh
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
print(str1[:7])  start index taken by default.
slicing with backword or negative indexing.
str1="apple"
print(str1[-3:-1]) #prints pl

# pyhton string functions
str1= "i eat apple"
print(str1.endswith("ple")) #true if ends with ple else false
print(str1.capitalize()) # capitals the first letter, only once

#for permanent changes:
str1=str1.capitalize()
print(str1)
print(str1.replace("e","M")) #("old value","new value")
print(str1.find("app")) #return index of 1st occurence, -1 if not found
print(str1.count("pp")) #returns the total couunt of "pp"

# next if elif and many more
#here both if statements can execute
num=5
if(num>2):
    print("greater than 2")
    print("gre than two")
if(num==5):
    print("it is five")
    print("it is 5")

# here only one set of if statements can execute since using elif.
num=5
if(num>2):
    print("greater than 2")
    print("gre than two")
elif(num==5):      #this does not execute 
    print("it is five")
    print("it is 5")

# nested if
num=5
if(num>2):
    print("greater than 2")
    if(num>=5):
        print("gre than or equal to five")

        
if elif ladder:  #see the indentation..all are at the same level.

a=int(input("Enter A: "))
b=int(input("Enter B: "))
c=int(input("Enter C: "))

if(a>b and a>c):
    print("a is greatest",a,b,c)
elif(b>c):
    print("b is greatest",a,b,c)
else:
    print("c is greatest",a,b,c)
#see the indentation:
q3ogiuhwfafrgaregsawefyrdsergoij
aweffdsrgzsdviuhfwefjfj
awefiuhawefygvy
aerghugtfctfufawrgoWDN
aefawef
