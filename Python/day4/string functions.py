a = " hello World"

print(a.casefold()) # this will print the string in lowercase, which is hello world
print(a.capitalize()) # this will print the string with the first character in uppercase and the rest in lowercase, which is Hello world    
print(a.title()) # this will print the string with the first character of each word in uppercase and the rest in lowercase, which is Hello World
print(a.upper()) # this will print the string in uppercase, which is HELLO WORLD
print(a.lower()) # this will print the string in lowercase, which is hello woekd    

print(a.count("llo")) # this will print the number of occurrences of llo in the string, which is 1

# index and find functions are used to find the index of the first occurrence of a character in the string. The difference between them is that the index function raises a ValueError if the character is not found, while the find function returns -1 if the character is not found.
# if not fount then index will raise an error and find will return -1


print(a.index("o")) # this will print the index of the first occurrence of the character o in the string, which is 4
print(a.find("o")) # this will print the index of the first occurrence of the character o in the string, which is 4
print(a.rindex("o")) # this will print the index of the last occurrence of the character o in the string, which is 8


print(a.find("o",5)) # this will print the index of the first occurrence of the character o in the string starting from index 5, which is 8
print(a.find("o",9)) # this will print the index of the first occurrence of


# endswith and startswith functions are used to check if the string ends with or starts with a particular character or substring. They return True if the condition is satisfied, otherwise they return False.
print(a.endswith("d")) # this will print True because the string ends with d
print(a.endswith("k")) # this will print False because the string does not end with k
print(a.startswith(" ")) # this will print True because the string starts with a space
print(a.startswith("h")) # this will print False because the string does not start with h   

# check print(dir(str)) to see all the functions that can be used with strings.


print(help(a.isalpha)) # this will print the documentation of the isalpha function, which is used to check if all the characters in the string are alphabets. It returns True if all the characters are alphabets, otherwise it returns False.
print(help(a.upper)) 
b= "12345"
print(b.isdigit()) # this will print True because all the characters in the string are digits
print(a.isalpha()) # this will print False because the string contains a space and a comma, which are not alphabets.
print(a.isdigit()) # this will print False because the string does not contain any digits. 
c = "123,45"
print(c.isdigit()) # this will print False because the string contains a comma, which is not a digit.
a = " This only contains spaces and alphabets "
z = a.split() # this will split the string into a list of words, which is ['This', 'only', 'contains', 'spaces', 'and', 'alphabets']
print(z)
print(a.split("o")) # this will split the string at each occurrence of the character o, which is [' This only c', 'ntains spaces and alphabets ']
print(a.split("o",1)) # this will split the string at the first occurrence of the character o, which is [' This only c', 'ntains spaces and alphabets ']
print(a.split("o",2)) # this will split the string at the first two occurrences of the character o, which is [' This only c', 'ntains sp', 'aces and alphabets ']

print(a.splitlines()) # this will split the string into a list of lines, which is [' This only contains spaces and alphabets ']

# zfill function is used to fill the string with zeros until it reaches the specified width. If the width is less than the length of the string, it will return the original string.
print(a.zfill(50)) # this will fill the string with zeros until it reaches the width of 50, which is

# isalpha()
# Isnumeric()
# Isalnum()
 
# to check ifl characters in the string are alphabets, digits or alphanumeric respectively. They return True if the condition is satisfied, otherwise they return False.
# using not operator we can check if the string does not satisfy the condition. For example, if we want to check if the string does not contain any digits, we can use the following code:

