# While Loop : it is used when you want to repeatedly execute a block of code as long as a certain condition is true.

n = int(input("Enter the decimal56 number : "))

binary = ""

while n > 0:
    binary = str(n%2) + binary
    n //= 2
print(binary)

# Second Example : 

def fibonacci(n):
    n1,n2,n3=0,1,0

    while not n1>n:
        print(n1, end=" ")
        n3 = n1 + n2
        n1 = n2
        n2 = n3

n = int(input("Enter a number : " ))
print("Fibonacci series up to number",n)
fibonacci(n)