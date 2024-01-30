# Decorator : It is powerful and flexible tool that allows you to modify or extend the behavior of functions or methods without
#_____________changing their actual code. 

# Creating a Decorator : 

def my_decorator(func):

    def wrapper():
        print("Hey!!")
        func()
        print("How are you?")

    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Use Cases for Decorators : 
# 1.Logging : 

def log_function_call(func):

    def wrapper(*args, **kwargs):

        print(f"Calling {func.__name__} with arguments {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")

        return result
    
    return wrapper

@log_function_call
def add(x, y):
    return x + y

result = add(3, 5)

# 2.Timing : 

import time

def timing_decorator(func):

    def wrapper(*args, **kwargs):

        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds")

        return result
    
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(2)
    print("Function executed!")

slow_function()

# 3.Memorization : 

def memoize(func):
    cache = {}

    def wrapper(*args):
        
        if args not in cache:
            cache[args] = func(*args)

        return cache[args]

    return wrapper

@memoize
def fibonacci(n):
    if n in (0, 1):
        return n
    return fibonacci(n-1) + fibonacci(n-2)

result = fibonacci(10)
