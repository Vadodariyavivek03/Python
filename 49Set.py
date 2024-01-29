# Immutable Set : Python does have a built-in immutable set-like object called frozenset.

x = frozenset([1, 2, 3, 4, 5])

print(x)
print(type(x))

# you cannot add, remove, or modify elements. Immutable nature : 
# x.add(5)
# print(x) ---> error!

# Union, Intersection, Difference : 

x = frozenset([1, 2, 3, 4, 5])
y = frozenset([4, 5, 6, 7, 8, 9, 10])

z = x.union(y)
print("Union : ",z)

z = x.intersection(y)
print("Intersection : ",z)

z = x.difference(y)
print("Difference : ",z)

print(3 in x)
print(2 not in y)

print(len(x))

z = set(x)
print(z)

# For Loop : 

for i in x:
    print("Frozenset : ",i)

