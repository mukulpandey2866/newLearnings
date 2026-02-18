name = "Student"
age = 25
greeting = "My name is {} and I am {} years old.".format(name, age)
print(greeting)
 
greeting = "My name is {0} and I am {1} years old.".format(name, age)  # Positional
greeting = "My name is {name} and I am {age} years old.".format(name="Sumit", age=25)
 
print("Python  "*4)
 
# default arguments
print("Hi  {}, Contact No- {}.".format("Sandra", 123456))
 
# positional arguments
print("Hello {0}, Contact No-  {1}.".format("Sandra", 230.2346))
 
# keyword arguments
print("Hi there  {name}, Contact No-  {cno}.".format(name="Sandra", cno=234567891))
 
# mixed arguments
print("Hello {0}, your balance is {blc}.".format("Sandra", blc=200000))
 
greeting = f"My name is {name} and I am {age} years old."
print(greeting)
 
print(f"Next year, {name} will be {age + 1} years old.")