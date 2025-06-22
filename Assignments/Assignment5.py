#Task 1 - Writing Functions
def greet_user(name): #accepts a name as parameters and prints personalized greeting
    print("Hello, " + name + "! Welcome aboard.")
greet_user("Alice")

def add_numbers(a, b): #takes two numbers as parameters and returns the sum
    return a + b
print("The sum of 5 and 10 is " + str(add_numbers(5, 10)))

#Task 2 - Using Default Parameters
def describe_pet(pet_name, animal_type="dog"): #prints description of a pet
    print("I have a " + animal_type + " named " + pet_name + ".")
describe_pet("Buddy")
describe_pet("Whiskers", "cat")

#Task 3 - Functions with Variable Arguments
def make_sandwich(*ingredients): #accepts a variable number of arguments for sandwich ingredients and prints them as a list
    print("Making a sandwich with the following ingredients: -")
    for i in ingredients:
        print(f"- {i}")
make_sandwich("Lettuce", "Tomato", "Cheese")

#Task 4 - Understanding Recursion
def factorial(n): #recursive factorial function
    if (n == 0 or n==1):
        return 1
    else:
        return (n * factorial(n-1))
print("The factorial of 5 is " + str(factorial(5)))

def fibonacci(n): #recursive fibonacci sequence function
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print("The 6th Fibonacci number is " + str(fibonacci(6)))