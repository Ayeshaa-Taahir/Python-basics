# 1 Built-in Function
# Using built-in print() and sorted() functions
print("This is a built-in function example")
numbers = [3, 6, 1, 8]
print("Sorted list:", sorted(numbers))  # sorted() returns a new sorted list

# 2 User-defined Function
# Defining and calling a basic function
def greet_user():
    print("Hello from a user-defined function")

greet_user()  # calling the user-defined function

# 3 Recursive Function
# A function that calls itself to calculate factorial
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)# recursion

print("Factorial of 5:", factorial(5)) 

# 4 Lambda Function
# Small anonymous function to calculate square of a number
square = lambda x: x * x
print("Square of 4 using lambda:", square(4)) 

# 5 Higher-order Function
# A function that takes another function as an argument
def shout(text):
    return text.upper()

def apply_function(func, word):
    return func(word)  # calling the passed function

print("Higher-order function result:", apply_function(shout, "hello"))  

# 6 Generator Function
# A function that yields values one by one using 'yield'
def countdown(n):
    while n > 0:
        yield n  # yield returns a value and pauses the function
        n -= 1

print("Countdown using generator:")
for i in countdown(3):# iterating through generator
    print(i)

# 7 Asynchronous Function
# Function that works asynchronously using 'async' and 'await'
import asyncio

async def async_hello():
    print("Hello (start)") # First part runs
    await asyncio.sleep(1)# Pauses for 1 second (non-blocking)
    print("Hello (end)")# Resumes after 1 second

# Running the asynchronous function
print("Calling async function:")
asyncio.run(async_hello()) # Executes the async function

# 8 Decorator Function
# A function that modifies the behavior of another function
def my_decorator(func):
    def wrapper():
        print("Before decorated function")# runs before original function
        func()# call the original function
        print("After decorated function")# runs after original function
    return wrapper

@my_decorator  # applying decorator to the function below
def say_hello():
    print("Hello from decorated function")

say_hello()  # Output includes decorator's behavior