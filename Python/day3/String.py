

data = "data"
data1 = 'data'
data2 = '''data'''

# data3 = ""data""  # this is using 4 quotes

print(data)
print(data1)
print(data2)

print(dir(str))  # gives the directory of the class str, it will give all the functions(members) of the class str

print(data.upper())  # this will convert the string to uppercase, it will return a new string, the original string will remain unchanged

# Indexing and Slicing of String 
# ( indexing from 0 to len(s)-1)
s = "Hello, World!"
print(s[0])  # this will print the first character of the string, which is
print(s[7])  # this will print the 8th character of the string, which is W
print(len(s))
print(s[len(s)-1])  # this will print the last character of the string, which is !
print(s[-1])  # this will also print the last character of the string, which is !, negative indexing starts from the end of the string, -1 is the last character, -2 is the second last character and so on.

# Negative Indexing (from -1 to -len(s)) // positive inxing is till len(s) - 1)
print(s[-1])  # this will print the last character of the string, which is !
print(s[-len(s)]) # this will print the first character of the string, which is H
print(s[0]) # this will also print the first character of the string, which is H




