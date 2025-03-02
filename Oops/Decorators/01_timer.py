# Decorators in python are like tollbooths on road for functions adding functionality without changing the original function

# Timing function execution - Write a decorator that masures the time a function takes to execute
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper

@timer #decorated the timer function, now example_func will be passed through timer function.
def example_func(n):
    time.sleep(n)

example_func(2)