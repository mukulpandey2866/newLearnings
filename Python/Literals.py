# literals are the values that are directly represented in the source code. They can be of various types, such as integers, floating-point numbers, strings, booleans, and more. Here are some examples of literals in Python:
# literals are the values assigned to the variables or constants in the code. They can be of various types, such as integers, floating-point numbers, strings, booleans, etc.
# Integer literal
a = 10
# String literal
b = "Hello, World!"
# double single and triple quotes can be used to represent string literals
c = 'Hello, World!'
d = """Hello, World!"""

# Floating-point literal
e = 3.14

# Boolean literal
f = True
# f =true  # invalid boolean literal, it should be capitalized


# List , Tuple, Set, Dictionary literals are all Class not datatypes, they are used to create objects of the respective classes.
# List literal
a = [1, 2, 3, 4, 5]
print(type(a))
# Tuple literal
b = (1, 2, 3, 4, 5)
print(type(b))
# Set literal
c = {1, 2, 3, 4, 5}
print(type(c))
# Dictionary literal
d = {"name": "Alice", "age": 30, "city": "New York"}
print(type(d))

# Commets are not literals, they are used to add explanations or notes to the code. They are ignored by the interpreter and do not affect the execution of the program. In Python, comments can be created using the hash symbol (#) for single-line comments, or triple quotes (''' or """) for multi-line comments.
# Use # for single-line comments
# This is a single-line comment
# Use triple quotes for multi-line comments
'''
This is a multi-line comment
spanning multiple lines.
'''

# Dynamically typed language: Python is a dynamically typed language, which means that you do not need to declare the data type of a variable when you create it. The interpreter will automatically determine the data type based on the value assigned to the variable. For example:
a = 10  # a is an integer ( no need to decalare int a; a = 10; in C or Java)

# Data Types in Python: Python has several built-in data types, including:

# Numeric data types: class names ( int, float, complex)
# Dictionary
# Boolean: class name is bool, it has two literals True and False, these are the only two values that can be assigned to a variable of type bool. The bool class is a subclass of the int class, which means that True is equivalent to 1 and False is equivalent to 0 in numerical contexts.

# Set: class name is set, it is an unordered collection of unique elements. It is defined using curly braces {} or the set() constructor. For example:
# set and frozenset are the two types of sets in Python. The set is mutable, which means that you can add or remove elements from it, while the frozenset is immutable, which means that you cannot modify it after it is created. The set and frozenset classes are part of the built-in data types in Python and are used to create sets of unique elements.

# Sequence data types: ( String , Tuple, List) class names are str, tuple, list respectively. These are used to create sequences of elements. String is a sequence of characters, while tuple and list are sequences of any type of elements. The main difference between tuple and list is that tuple is immutable, which means that you cannot modify it after it is created, while list is mutable, which means that you can add or remove elements from it.

# Mapping data type: Dictionary ( class name is dict) is a collection of key-value pairs, where each key is unique and maps to a corresponding value. It is defined using curly braces {} or the dict() constructor. For example:
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(type(my_dict))

# int alone can store integer of any length ( size, signed unsigned, etc), it is not like C or Java where we have different data types for different sizes of integers ( int, long, short, etc). In Python 3, there is only one integer type, which can store integers of arbitrary size. The size of the integer is limited only by the amount of memory available on the system. This means that you can work with very large integers without worrying about overflow or underflow issues that can arise in other programming languages.

# String
data = '''This is a string literal.
It can be enclosed in single quotes,
double quotes, or triple quotes.'''
print(data)

# type conversion (typecasting) is the process of converting a value from one data type to another. In Python, you can use built-in functions like int(), float(), str(), etc., to perform type conversion. For example:
# Implicit type conversion (type coercion)
n1 = 10
n2 = 3.14
n3 = n1 + n2  # n3 will be of type float, because of the presence of a float in the expression
print(n3)
print(type(n3))

# Conversion Functions (Explicit type conversion)
print(type(int(n2)))  # converts float to int,
print(int(n2)) # converts float to int, it will truncate the decimal part and return only the integer part

n2 = int(n2)  # n2 will now be of type int, and its value will be 3
print(n2)

'''
Explicit type conversion lists:
int(x) - converts x to an integer
float(x) - converts x to a floating-point number
str(x) - converts x to a string
bool(x) - converts x to a boolean value (True or False)
complex(x) - converts x to a complex number
list(x) - converts x to a list
tuple(x) - converts x to a tuple
set(x) - converts x to a set
dict(x) - converts x to a dictionary
'''
