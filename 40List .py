# List : Used to store multiple items in a single variable. list is orderd, mutable and allow duplicate value.

# Accessing values in list :

list = [25,69,42,75,36,12,5,89,32,24,54]
print(list)

print(len(list))

print(min(list))

print(max(list))

print(type(list))

print(list[2:8:2])
 
print(list[::-1])

# update list : 

list[2] = 23
print(list)

list[2:6] = [10, 20, 30, 40]
print(list)

# Delete list : 

print(list.clear())