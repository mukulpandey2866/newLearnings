a= 10
b = str(a)  # str() is a built-in function that converts the integer value of a to a string
print(type(a))
print(type(b))  # this will print <class 'str'>, which indicates that b is now a string
c = '100'
a = a + 10
b = b + '10Seed'  # this will concatenate the string '10Seed' to the string value of b, resulting in '10010Seed'
print(a)  # this will print 20, which is the result of adding 10
print(b)  # this will print '10010Seed', which is the result of concatenating '10Seed' to '100'


import keyword
print(keyword.kwlist)

# help(keyword)
print(keyword.iskeyword('if'))