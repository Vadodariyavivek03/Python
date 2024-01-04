#Type conversion in str to int........explicit type -- manual conversion
#Explicit can convert in str() to int() and it's reverse.

x = "23"   #str
y =  10    #int

x1 = int(x) # convert str to int

x2 = x1 + y 

print(x2)  #Ans in int

print(type(x))
print(type(y))
print(type(x1))
print(type(x2))