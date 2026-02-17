date = "The date is:"
day = 17
month = 12
year = 2343
print(date, day, month, year)
print(date + " " + str(day) + "/" + str(month) + "/" + str(year))  # this will concatenate the string date with the string representation of day, month, and year, resulting in a formatted date string.
print(day, month, year, sep="/")  # this will print the values of day, month, and year in the order they are provided, separated by "/".


print(date, day, month, year,end="*") # end is * instead of \n, so the next print statement will continue on the same line after the asterisk
print(day, month, year, sep="/")


s1 = "Hello"
s2 = "World"
no = 100
print(s1, s2)  # this will print "Hello World" with a space in between
print(s1, s2, sep="-")  # this will print "Hello-World" with a hyphen in between
print(s1 + " " + s2) # + is used for concatenation, so this will also print "Hello World" with a space in between
# Both above are string

print(s1 + s2 + no) # The above line will raise a TypeError because you cannot concatenate a string (s1 + s2) with an integer (no) without converting the integer to a string first. To fix this, you can convert no to a string using str(no):
print(s1 + s2 + str(no))  # this will print "HelloWorld100" without any spaces in between, as the + operator concatenates the strings together.

emp_id = 123
emp_name = "John Doe"
emp_salary = 50000

# Format specifier for string formatting
print("Employee ID: %d, Name: %s, Salary: %.2f" % (emp_id, emp_name, emp_salary))  # this will print "Employee ID: 123, Name: John Doe, Salary: 50000.00" with the specified format for each variable.

# Positional Parameters
print("Employee Name: {1}, ID: {0}, Salary: {2:.2f}".format(emp_id, emp_name, emp_salary))  # this will print "Employee Name: John Doe, ID: 123, Salary: 50000.00" using positional parameters to specify the order of the variables in the output string.

# index parameters (WRITE index inside {} eg. {0}, {1}, {2})
print("Employee Name: {1}, ID: {0}, Salary: {2:.2f}".format(emp_id, emp_name, emp_salary))  # this will raise a KeyError because the format string is using named placeholders (name, id, salary) but the format() method is being called with positional arguments (emp_id, emp_name, emp_salary) instead of keyword arguments. To fix this, you can either change the format string to use positional placeholders or change the format() method to use keyword arguments.
# named parameters, 
print("Employee Name: {name}, ID: {id}, Salary: {salary:.2f}".format(id=emp_id, name="Amit", salary=emp_salary))  # this will print "Employee Name: John Doe, ID: 123, Salary: 50000.00" using named parameters to specify the variable names in the output string.
# named Placeholders (WRITE name inside {} eg. {name}, {id}, {salary})
print("Employee Name: {name}, ID: {id}, Salary: {salary:.2f}".format(id= 32, name="Amit", salary = 200))  # this will print "Employee Name: John Doe, ID: 123, Salary: 50000.00" using named placeholders to specify the variable names in the output string.
# f Formated raw strind,   it picks the variables decalared at the top and directly embed them in the output string without needing to use the format() method.
print(f"Employee Name: {emp_name}, ID: {emp_id}, Salary: {emp_salary:.2f}")  # this will print "Employee Name: John Doe, ID: 123, Salary: 50000.00" using f-string formatting to directly embed the variable values in the output string.
