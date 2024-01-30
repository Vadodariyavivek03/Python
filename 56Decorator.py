# Decorators : 

def fibonacci_decorator(func):

    def wrapper(*args, **kwargs):

        fibonacci_series = [0, 1]

        for i in range(2, 10):
            fibonacci_series.append(fibonacci_series[i-1] + fibonacci_series[i-2])
        
        print(f"Fibonacci Series (up to 10 terms): {fibonacci_series}")
    
        result = func(*args, **kwargs)
        return result
    
    return wrapper

@fibonacci_decorator

def example_function():
    print("Executing the example function")

example_function()