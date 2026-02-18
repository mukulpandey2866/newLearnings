# For loop is used to iterate over a sequence (like a list, tuple, string) or other iterable objects. It is used when we know the number of iterations beforehand.


from itertools import count


data = "Hello, World!"
print(data[0])  # this will print the first character of the string, which is H
print(data[len(data)-1])  # this will print the last character of the string, which is !

for i in data:
    print(i, end=" ")  # this will print each character of the string in the same line separated by space.
print("\nEnd of the string")  # this will print a new line after printing all the characters of the string.

for i in range(0,len(data),1):
    print(i, end=" ")  # this prints numbeers

print("\nEnd of the number line")  # this will print a new line after printing all the numbers from 0 to len(data)-1.


for i in range(0,len(data),1):
    print(data[i], end=" ")  # this will print the index and the character at that index in the same line separated by space.

print("\nEnd of the string")  # this will print a new line after printing all the characters of the string.

stringg = input("Enter a string: ")
vow = 0
cons = 0
for i in stringg:
    if i in "aeiouAEIOU":
        vow += 1
    else:
        cons += 1
print(f"The number of vowels in the string is: {vow}")
print(f"The number of consonants in the string is: {cons}")
print(f"The number of characters in the string is: {len(stringg)}")


