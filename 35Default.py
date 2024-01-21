# Function with default argument and without argument : 

def greet(name="Guest", greeting="Hello"):
    print(f"{greeting}, {name}!")

greet()

greet("Vivek", "Good morning")

#-------------------------------------------------------------------------------------------------------------------------------

# This is valid
def valid(a, b, c=0, d=1):
    pass

# This will result in a syntax error
# def invalid(a=0, b, c=1):
#     pass

#-------------------------------------------------------------------------------------------------------------------------------
# you can override default values by providing explicit values during the function call.

def person(name, age, city="Unknown"):
    print(f"{name} is {age} years old and lives in {city}.")

person("Vivek", 22)
person("Meet", 24, "Ahemdabad")

#-------------------------------------------------------------------------------------------------------------------------------
# Default Values Are Evaluated Once:

def add(item, my_list=[]):
    my_list.append(item)
    return my_list

print(add(1))  
print(add(2))  
print(add(3))

