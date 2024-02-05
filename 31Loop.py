# For loop : A for loop is used for iterating over a sequence.

# 1.

names = ["Kashyap", "Vivek", "Meet", "Darshit"]

for x in names:
    print(x)

#-------------------------------------------------------------------------------------------------------------------------------------
# 2.
    
name = "vivek"       # OR also use directly.-->  for x in "vivek"  

for x in name:
    print(x)
    
#-------------------------------------------------------------------------------------------------------------------------------------
# 3.
    
sum = 0   # range(10) : this function print the value 0 to 9 not contain 10. it's like range(start, stop, step).

for i in range(20):
    print(i, end=" ")  
    sum = sum + i 

print("\nSum of first 10 numbers :",sum)

# Second example : 

i = int(input("Enter the number : "))

for j in range(1, 11):
	print(i, "*", j, "=", i*j)
print()

#-------------------------------------------------------------------------------------------------------------------------------------
# 4.

for i in range(10):      # We can use the break statement with the for loop to terminate the loop when a certain condition is met.
    if i == 5:           # for i in range(10): --> print(i) --> if i==5: --> break --> OUTPUT : 0 1 2 3 4 5
        break
    print(i)

#-------------------------------------------------------------------------------------------------------------------------------------
print('CONTINUE')
# 5.
# We can use the continue statement with the for loop to skip the current iteration of the loop and jump to the next iteration.
    
for i in range(10):  
    if i == 5:           # for i in range(10): --> print(i) --> if i==5: --> continue --> OUTPUT : 0 1 2 3 4 5 6 7 8 9
        continue
    print(i)

#-------------------------------------------------------------------------------------------------------------------------------------
print('PASS')
# 6.
# For loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to 
# ____avoid getting an error.

a = 10
b = 20

if(a<b):
    pass
else:
    print("b<a")

#-------------------------------------------------------------------------------------------------------------------------------------
print("Nested Loop")
# 7.

n = int(input("Enter the number : "))
        
for outer in range(n):
    for inner in range(outer+1):
        print("*",end="")
    print()

# Second Example : 
    
n = int(input("Enter the number : "))
        
for outer in range(n,0,-1):
    for inner in range(outer,0,-1):
        print("*",end="")
    print()

#-------------------------------------------------------------------------------------------------------------------------------------
# 8. Check Prime number : 
    
n = int(input("Enter the number : "))

flag = False

if n == 1:
    print(n, "is not a prime number")
elif n > 1:
    for i in range(2, n):
        if (n % i) == 0:
            flag = True
            break

    if flag:
        print(n, "is not a prime number")
    else:
        print(n, "is a prime number")
    

