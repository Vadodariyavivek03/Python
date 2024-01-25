# map() : this function returns a map object(which is an iterator) of the results after applying the given function to each item of
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

# reduce() : 
