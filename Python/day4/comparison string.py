a = "Hello" 
c = "hello"
print(a == c) # this will print False because the case of the characters is different.
print(a > c) # this will print False because the case of the characters is different.
print(a < c) # this will print True because the case of the characters is different.
print(a >= c) # this will print False because the case of the characters is different.

# comparision steps:
#  size of the string is same, so we will compare the characters one by one.
#  H and h are different because of the case, so we will compare their ASCII values to determine which one is greater.
#  ASCII value of H is 72 and ASCII value of h is 104, so H is less than h, which means a is less than c.

print(a * 3) # this will print the string a three times, which is HelloHelloHello
print(a + c) # this will print the concatenation of a and c, which is
# Hellohello
print(3*a) # this will print the string a three times, which is HelloHelloHello
print(a * '@') # this gives syntax error because we cannot multiply a string with another string, we can only multiply a string with an integer.





