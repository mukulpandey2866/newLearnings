
# range(start, stop, step)
for i in range(1, 10, 2):
    print(i)  # this will print odd numbers from 1 to 9, because the start value is 1, the stop value is 10 (exclusive), and the step value is 2.
# range(stop)
for i in range(5):
    print(i)  # this will print numbers from 0 to 4, because the stop value is exclusive.
# range(start, stop)
for i in range(1, 6):
    print(i)  # this will print numbers from 1 to 5, because the start value is 1 and the stop value is 6 (exclusive).

# Print table of 9
for i in range(1, 11):  # we write 11, because range is from start to stop - 1, so it will print from 1 to 10.
    print(f"9 * {i} is: {9*i}")

# print table of any number
num = int(input("Enter a number to print its table: "))
for i in range(1, 11):
    # print(f"{num} * {i} is: {num*i}")
    # print(num,"*",i," is: ",num*i,end=" ",sep=",")  # end is used to print in the same line and sep is used to separate the values with a comma instead of space.
    if i < 10:  # this is used to avoid printing comma after the last value.
        print(num*i, end=", ",sep=",")  # this will print only the result of multiplication in the same line separated by space.
        # print(f"{num} * {i} is: {num*i}")
        # print(num,"*",i," is: ",num*i,end=" ",sep=",")  # end is used to print in the same line and sep is used to separate the values with a comma instead of space.
    else:
        print(num*i)  # this will print a comma after each value except the last one.
    # sep cannot be used here because we are not printing multiple values, we are printing only one value which is the result of multiplication, so sep will not work here.
    # sep example
print("Hello", "World", sep="-")  # this will print Hello-World, because sep is used to separate the values with a hyphen instead of space.

# while loop
# take care: start, stop, inc/dec
while (num >= 0):
    print(num)
    num -= 1  # this is used to decrement the value of num by 1 in each iteration, otherwise it will run indefinitely.


# factorial with while loop
num = int(input("Enter a number: "))
fact = 1
while num > 0:
    fact *= num
    num -= 1
print(f"The factorial is: {fact}")


# print 2 raised the power of n to 0
n = int(input("Enter the value of n: "))
while n >= 0:
    print(2**n)
    n -= 1
    

# brak and continue in while loop

# stop while loop with break
num = int(input("Enter a number: "))
fact = 1
while num > 0:
    fact *= num
    num -= 1
    if num == 3:
        break  # this will stop the loop when num is equal to 3, so the factorial will be calculated only for numbers greater than 3.
print(f"The factorial is: {fact}")

# continue in while loop
num = int(input("Enter a number: "))
while num >= 0:
    if num == 5:
        num -= 1  # this will decrement num before the continue statement to avoid infinite loop
        continue  # this will skip the iteration when num is equal to 5, so it will not print 5.
        num -= 1  # this will cause an infinite loop because num will always be 5, so we need to decrement num before the continue statement.
    else:
        print(num)
    num -= 1
