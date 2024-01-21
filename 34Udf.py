# function : A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

def greet():
    print("Hello World !!!!")

greet()

# Function with parameters-------------------------------------------------------------------------------

def add(a,b):
    sum = a+b
    return sum

a = int(input("Enter the number1 : "))
b = int(input("Enter the number2 : "))

print("Sum is :",add(a,b))

# Function with return values-------------------------------------------------------------------------------    

def fact(n):
    if (n<=1):
        return 1
    return n*fact(n-1)

n = int(input("Enter the number : "))
print(f"Factorial of {n} is :", fact(n))