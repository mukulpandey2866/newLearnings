a=10
b=10.45
c="Hello"
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

# variable object ( a, b, c),   data type are classes
# <class 'int'>
# <class 'float'>
# <class 'str'>

# >>> dir(int) give the directory of the class int,
# ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt_
# these many functions(members) are there in in the int class

# >>> dir(bool)
# ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__di
# double underscore has a different mening in python, it is used to denote the special functions of the class, these are called as dunder methods (double underscore methods)

# Multiple assignment
a, b, c = 10, 20.45, "Hello"
print(a)
print(b)
print(c)
# Multiple assignment with same value
x = y = z = 100
print(x)
print(y)
print(z)

# ?Identifiers in Python
# caseSensitive
# can contain letters, digits and underscore
# cannot contain special characters like @, #, $, etc
# cannot start with a digit
# cannot use reserved keywords, or built-in function names as identifiers
_one = 1
print(_one)
# 1a=10 incalid identifier
#  a@=10 invalid identifier

a = True
print(type(a))
a = 'True'
print(type(a))
