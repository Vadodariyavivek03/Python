# Identity Operators -- Identity operators are used to compare the objects. 

x = ['car','bus','bike']
y = ['car','bus']
z = x

print(x is y)       # Returns True if both variables are the same object
print(x is z)
print(x is not y)   # Returns True if both variables are not the same object
print(x == y)
print(x != y)