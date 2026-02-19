"""

() tuple
{} set
{key: value} dict
[] list


"""

lst  = [1, 2, 3, 4, 5]
lst1 = ["q","w","e","r","t","y",1,2,3,4,5]
lst2 = [1, 2, 3, 4, 5, [6, 7, 8], ["a", "b", "c"]]

print(type(lst2)) # this will print the type of the variable lst2, which is <class 'list'>
print(lst2) # this will print the list lst2, which is [1,

l2 = [1, 2, 3, 'Seed', 12.45, True]
print(l2) # this will print the list l2, which is [1, 2, 3, 'Seed', 12.45, True]
print(l2[0]) # this will print the first element of the list, which is 1
print(l2[3]) # this will print the fourth element of the list, which is
l2[3] = "Seed Pune" # this will change the fourth element of the list to "Seed Pune"
print(l2) # this will print the list l2, which is [1, 2, 3, 'Seed Pune', 12.45, True]

print(type(l2[3])) # this will print the type of the fourth element of the list, which is <class 'str'> because we have changed it to "Seed Pune"
print(type(l2[4])) # this will print the type of the fifth element of the list, which is <class 'float'>

# list are mutable
# list can have duplicate elements
# list can have elements of different data types
# list can have nested lists


# Reverse indexing in list
print(l2[-1]) # this will print the last element of the list, which is True
print(l2[-2]) # this will print the second last element of the list, which


# Constructor method to create a list
l3 = list() # this will create an empty list

l3 = [[1,1,1],[23,24,35],[],"Seed",123, True]
print(l3[1]) # this will print the second element of the list, which is [23, 24, 35]
print(l3[1][2]) # this will print the third element of the second element
z = l3[1][2] # this will assign the value 35 to the variable z
print(z) # this will print the value of z, which is 35
print(id(l2)) # this will print the memory address of the list l2
print(id(l3[1][2])) # this will print the memory address of the third element of the second element of the list l3

print(id(z)) # this will print the memory address of the variable z
print(id(l3[1][1])) # this will print the memory address of the second element of the second element of the list l3


# To access: index and slicing can be used in list just like string. The only difference is that the stop index is inclusive in list, which means it will be included in the result.

# list append and extend functions are used to add elements to the list. The append function adds a single element to the end of the list, while the extend function adds multiple elements to the end of the list.
l3.append("New Element") # this will add the string "New Element" to the
print(l3) # this will print the list l3, which is [[1, 1, 1], [23, 24, 35], [], 'Seed', 123, True, 'New Element']
l3.extend([1, 2, 3]) # this will add the elements 1, 2, 3 to the end of the list l3
print(l3) # this will print the list l3, which is [[1, 1, 1], [23, 24, 35], [], 'Seed', 123, True, 'New Element', 1, 2, 3]
l2 = [1, 2, 3, 'Seed', 12.45, True]
l3.append(l2) # this will add the list l2 as a single element to the end of the list l3
print(l3) # this will print the list l3, which is [[1, 1, 1], [23, 24, 35], [], 'Seed', 123, True, 'New Element', 1, 2, 3, [1, 2, 3, 'Seed', 12.45, True]]
l3.extend(l2) # this will add the elements of the list l2 to the end of the list l3
print(l3) # this will print the list l3, which is [[1, 1, 1], [23, 24, 35], [], 'Seed', 123, True, 'New Element', 1, 2, 3, [1, 2, 3, 'Seed', 12.45, True], 1, 2, 3, 'Seed', 12.45, True]


# insert function is used to add an element at a specific index in the list. The first argument is the index at which the element should be added, and the second argument is the element to be added.
l3.insert(2, "Inserted Element") # this will add the string "Inserted Element" at index 2 in the list l3
print(l3) # this will print the list l3, which is [[1, 1, 1], [23, 24, 35], 'Inserted Element', [], 'Seed', 123, True, 'New Element', 1, 2, 3, [1, 2, 3, 'Seed', 12.45, True], 1, 2, 3, 'Seed', 12.45, True]
l4 = [1, 2, 3, 4, 5]
l4.insert(2, [6,7,8,9]) # this will add the list [6,7,8,9] at index 2 in the list l4
print(l4) # this will print the list l4, which is [1, 2, [6, 7, 8, 9], 3, 4, 5]
list1 = [1, 2, 3, 4, 5]
list2 = ["Banglore", "Pune", "Mumbai", "Delhi"]
list3 = ["Satara"]
list1.append(list2) # this will add the list list2 as a single element to the end of the list list1
print(list1)
list1.append(list3) # this will add the list list3 as a single element to the end of the list list1
print(list1)
list1.extend(list2) # this will add the elements of the list list2 to the end of the list list1
print(list1)
list1.extend(list3) # this will add the elements of the list list3 to the end of the list list1
print(list1)

print(list1.count("e")) # this will print the number of occurrences of the character "e" in the list list1, which is 4
print(list1.count("Pune")) # this will print the number of occurrences of the string "Pune" in the list list1, which is 1
print(list2[1].count("e")) # this will print the number of occurrences of the character "e" in the string at index 1 of the list list2, which is 1 because the string at index 1 is "Pune" and it contains one "e"

# Other opeartions that can be performed on list are:
# 1. len() function to find the length of the list
# 2. min() and max() functions to find the minimum and maximum element in the list respectively. These functions can be used only if all the elements in the list are of the same data type and are comparable.
# 3. sum() function to find the sum of all the elements in the list. This function can be used only if all the elements in the list are of the same data type and are numeric.
# remove() function to remove the first occurrence of a specific element from the list. If the element is not found in the list, it raises a ValueError.
# pop() function to remove and return the last element of the list. If the list is empty, it raises an IndexError. We can also specify the index of the element to be removed and returned as an argument to the pop() function.
# clear() function to remove all the elements from the list, which will make the list empty.
# del keyword to delete the entire list or a specific element from the list. If we use del keyword to delete the entire list, it will remove the list from memory and we will not be able to access it anymore. If we use del keyword to delete a specific element from the list, it will remove that element from the list and shift all the elements after it to the left.
print(list1.pop(2)) # this will remove and return the element at index 2 of the list list1, which is [6, 7, 8, 9]
print(list1) # this will print the list list1 after removing the element at index

# in string pop() function is not available because string is immutable, which means we cannot change the string after it is created. We can only create a new string by performing operations on the existing string.

# del is predefined keyword in Python, which is used to delete the entire list or a specific element from the list. If we use del keyword to delete the entire list, it will remove the list from memory and we will not be able to access it anymore. If we use del keyword to delete a specific element from the list, it will remove that element from the list and shift all the elements after it to the left.
del list1[2] # this will delete the element at index 2 of the list list1, which is [6, 7, 8, 9]
print(list1) # this will print the list list1 after deleting the element at index

# differnce between pop and remove is that pop() function removes and returns the last element of the list, while remove() function removes the first occurrence of a specific element from the list. If the element is not found in the list, it raises a ValueError. On the other hand, if we try to pop an element from an empty list, it raises an IndexError.
# pop throws the object but remove does not throw the object, it just removes the object from the list. If we want to remove an element from the list and also get the value of that element, we can use pop() function. If we just want to remove an element from the list without caring about its value, we can use remove() function.
