# Basic list operators : 

# concatenation : 

a = [1, 2, 3 , 4, 5]
b = [6, 7, 8, 9, 10, 11]

c = a + b
print("concatenation : ",c)
print(type(c))

# Repetition : 

x = [1, 2, 3 , 4, 5]
y = 2

z = x * y
print("Repetition : ",z)

# Iteration : 

for i in [x]:
    print("Iteration : ",i)

# Indexing : 
    
x = [1, 2, 3 , 4, 5, 6, 7, 8, 9, 10, 11][5]
print("Indexing : ",x)

# Slicing : 

x = [1, 2, 3 , 4, 5, 6, 7, 8, 9, 10, 11][0:5]
print("Slicing : ",x)

# Sorting :

x = [5, 2, 9, 12, 3, 6, 0, 7, 4, 1, 8].sort()
print("Sorting : ",x)

