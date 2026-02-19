s = "Hello World!"

# slicing [start:stop:step]
# if start is not provided, it will be considered as 0
# if stop is not provided, it will be considered as len(s)
# if step is not provided, it will be considered as 1
# always remember that the stop index is exclusive, which means it will not be included in the result.

print(s[4:7:1])
print(s[3:7:1])
print(s[:6:])
print(s[:5:])
print(s[7::])
print(s[6::])
print(s[0::2])
print(s[::])


print(s[2:-4:])
print(s[-1:-4:-1]) # we have to add -1 as step


print(s[4:7:1])

# Reverse the string

print(s[len(s)-1::-1]) # we have to add -1 as step
print(s[::-1]) # this is the best way to reverse a string
print(s[0:len(s):-1]) # this will not reverse the string because the step is negative and the start index is less than the end index.
print(s[-1:-len(s):-1]) # this will not reverse the string because the step is negative and the start index is less than the end index.
print(s[-len(s):-1]) # this will not reverse the string because the step is negative and the start index is less than the end index.

# Since string is immutable, You cannot change it
# upper, lower, title, capitalize, casefold are some of the functions that can be used to change the case of the string.
# They return a new string with the desired case, but they do not change the original string.