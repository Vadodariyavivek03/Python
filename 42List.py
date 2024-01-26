# map() : This function returns a map object(which is an iterator) of the results after applying the given function to each item of
# ________a given iterable. (list, tuple etc.)

l = ['rajkot', 'surat','ahmedabad', 'morbi']

str = list(map(list, l))
print("Map : ",str)

# map() : 

def add(n):
	return n + n

n = (1, 2, 3, 4)
result = map(add, n)
print("Map : ",list(result))

# reduce() :This function is used to apply a particular function passed in its argument to all of the list elements mentioned in the       
# ___________sequence passed along.This function is defined in “functools” module.

import functools 

lis = [1, 3, 5, 6, 2] 

print("Sum : ", end="") 
print(functools.reduce(lambda a, b: a+b, lis)) 

print("Maximum : ", end="") 
print(functools.reduce(lambda a, b: a if a > b else b, lis)) 

# filter() : This method filters the given sequence with the help of a function that tests each element in the sequence to be true or not. 

def func(variable):
	letters = ['a', 'e', 'i', 'o', 'u']

	if (variable in letters):
		return True
	else:
		return False

sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

filtered = filter(func, sequence)

print('The filtered letters are:')
for s in filtered:
	print("Filter : ",s)

# fuction with lambda function : 
	
seq = [0, 1, 2, 3, 5, 8, 13]

result = filter(lambda x: x % 2 != 0, seq)
print(list(result))

result = filter(lambda x: x % 2 == 0, seq)
print(list(result))

