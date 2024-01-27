# List : Used to store multiple items in a single variable. list is orderd, mutable and allow duplicate value.

# list() : 

my_list = ['kutch','porbandar', 'baroda']

x = list(my_list)

print("List : ",x)

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

del list
print(list)

# or clear method use........
# print(list.clear())

# cmp() : This is python 2 function. In Python 3 we can use 'sorted()' function or we can use compare operator( == , <=, >=, !=, <, >).

# list1 = [1, 2, 3, 4]
# list2 = [1, 2, 3, 4]

# x = cmp(list1, list2)

# if x == 0:
#     print("List are equal.")
# elif x < 0:
#     print("List1 is smaller.")
# else:
#     print("List1 is larger.")