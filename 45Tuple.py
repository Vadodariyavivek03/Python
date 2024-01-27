# Basic built-in function : 

a = (41, 55, 12, 36, 14, 20, 92, 63, 84, 94)

print(len(a))

print(max(a))

print(min(a))

x = tuple(a)
print("Tuple : ",x)

# cmp() : This is python 2 function. In Python 3 we can use compare operator( == , is).

# python 2

# tuple1 = [1, 2, 3, 4]
# tuple2 = [1, 2, 3, 4]

# x = cmp(tuple1, tuple2)

# if x == 0:
#     print("tuple are equal.")
# elif x < 0:
#     print("tuple1 is smaller.")
# else:
#     print("tuple1 is larger.")

#python 3

# == :

tuple1 = (1, 2, 3, 4)
tuple2 = (1, 2, 3, 4)

if tuple1 == tuple2:
    print("tuple are equal.")

# is : 

print(tuple1 is tuple2)



