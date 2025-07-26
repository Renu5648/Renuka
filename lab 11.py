# 1
def non_negative_integers_only(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, int) or arg < 0:
                return "Invalid input: All arguments must be non-negative integers"
        return func(*args)
    return wrapper

@non_negative_integers_only
def calculate_square_root(x):
    return x ** 0.5

# Test cases
print(calculate_square_root(9))   
print(calculate_square_root(-9))  

# 2
def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Function: {func.__name__}")
        print(f"Arguments: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Return value: {result}")
        return result
    return wrapper

@debug
def add(a, b):
    return a + b

# Test
add(3, 5)

# 3
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                print(f"Execution {i+1}:")
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator
@repeat(3)  
def greet(name):
    print(f"Hello, {name}!")

greet("Renuka")

# 4
def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        print(f"Function '{func.__name__}' called {wrapper.call_count} time(s).")
        return func(*args, **kwargs)
    wrapper.call_count = 0  
    return wrapper
@count_calls
def say_hello():
    print("Hello!")

say_hello()
say_hello()
say_hello()
