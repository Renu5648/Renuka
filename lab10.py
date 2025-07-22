#1
def prime_num_gen():
    num = 2
    while True:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num
        num +=1    
            
gen =prime_num_gen()
for _ in range(15):
    print(next(gen))

#2

import random
import time

def temp_simulator():
    while True:
        yield random.randint(-10, 35)  
simulator = temp_simulator()
for _ in range(10):
    print("Temperature:", next(simulator), "°C")
    time.sleep(1)

#3

def fibonacci_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
def sum_fibonacci(n):
    gen = fibonacci_gen()
    total = 0
    for _ in range(n):
        total += next(gen)
    return total
print("Sum of first 10 Fibonacci numbers:", sum_fibonacci(10))

#4
def filter_string(data):
    for item in data:
        if type(item) == str:
            yield item
mixed_data = [1, "hello", 3.14, "world", 42]
for string in filter_string(mixed_data):
    print(string)

    
