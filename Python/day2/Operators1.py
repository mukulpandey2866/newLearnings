import math

import operators
dir(math)

a = 10.4
b = 3.3

print(a + b)  # Addition
print(a - b)  # Subtraction 
print(a * b)  # Multiplication
print(a / b)  # Division  (b)y default precision = 15)
print(a // b) # Floor Division  ( Quotient without the decimal part )
print(a % b)  # Modulus  ( Remainder )
print(a ** b) # Exponentiation

print(math.pow(a, b)) # Exponentiation using math module
print(f"{a/b:.2f}") # this will print the result of a divided by b with 2 decimal places using f-string formatting.


# short hand operators
a += 5  # this is equivalent to a = a + 5, it adds 5 to the current value of a and assigns the result back to a.
print(a)  # this will print the updated value of a after the addition.
a /= 2 # this is equivalent to a = a / 2, it divides the current value of a by 2 and assigns the result back to a.
# Division results alwys in float, even if both operands are integers. So, after this operation, a will be a floating-point number.
print(a)  # this will print the updated value of a after the division.

# Comparison Operators
x = 5
y = 10
print(x > y)  # this will print False because 5 is not greater than 10.
print(x < y)  # this will print True because 5 is less than 10
print(x == y) # this will print False because 5 is not equal to 10.
print(x != y) # this will print True because 5 is not equal to 10.
print(x >= y) # this will print False because 5 is not greater than or equal
print(x <= y) # this will print True because 5 is less than or equal to 10.

# Logical Operators
a = True
b = False
print(a and b)  # this will print False because both a and b need to be True for the result to be True.
print(a or b)   # this will print True because at least one of a or b
print(not a)    # this will print False because not operator negates the value of a, which is True, resulting in False.
print(not b)    # this will print True because not operator negates the value of b

print (10 > 5 and 3 < 7)  # this will print True because both conditions are true.
print (10 > 5 or 3 > 7)   # this will print True because at least one of the conditions is true.
print (not (10 > 5))       # this will print False because the condition


# Bitwise Operators
x = 5  # in binary: 0101
y = 3  # in binary: 0011
print(x & y)  # this will print 1 because the bitwise AND of 0101 and 0011 is 0001.
print(x | y)  # this will print 7 because the bitwise OR of 0101 and 0011 is 0111.
print(x ^ y)  # this will print 6 because the bitwise XOR of 0101 and 0011 is 0110.
print(~x)     # this will print -6 because the bitwise NOT of 0101 is 1010 in two's complement representation, which is -6 in decimal.
print(x << 1) # this will print 10 because the left shift operator shifts the bits of x to the left by 1 position, resulting in 1010 in binary, which is 10 in decimal.
print(x >> 1) # this will print 2 because the right shift operator shifts the bits of x to the right by 1 position, resulting in 0010 in binary, which is 2 in decimal.


# Location operators
print(id(a))  # this will print the memory address of the variable a.a =
print(a is b)  # this will print False because a and b are different objects in memory, even though they may have the same value.
print(a is not b)  # this will print True because a and b are different objects
# is operator checks if two variables are pointing to same location or not, while == operator checks if the values of the variables are equal or not. So, even if a and b have the same value, they may not be the same object in memory, which is why a is b would be False.

# Python points to the same location in memory for small integers (typically between -5 and 256) and some strings, so if a and b were assigned the same small integer value or the same string value, then a is b would be True because they would be referencing the same object in memory. However, for larger integers or different string values, a and b would be different objects in memory, resulting in a is b being False.
#  same location also used for strings as well, so if a and b were assigned the same string value, then a is b would be True because they would be referencing the same object in memory. However, for different string values, a and b would be different objects in memory, resulting in a is b being False.


# Membership Operators
my_list = [1, 2, 3, 4, 5]   
print(3 in my_list)  # this will print True because 3 is an element of my_list.
print(6 in my_list)  # this will print False because 6 is not an element of my_list.
print(3 not in my_list)  # this will print False because 3 is an element of my_list.
print(6 not in my_list)  # this will print True because 6 is not an element of my_list.
c = "Seed"
print('Se' in c)  # this will print True because 'Se' is a substring in the string c.
print('a' in c)  # this will print False because 'a' is not a character in the string c.
print('e' not in c)  # this will print False because 'e' is a character in the string c.
print('a' not in c)  # this will print True because 'a' is  not a character in the string c.
# Checks both string and substring, so if the substring is present in the string, it will return True for 'in' operator and False for 'not in' operator. If the substring is not present in the string, it will return False for 'in' operator and True for 'not in' operator.



