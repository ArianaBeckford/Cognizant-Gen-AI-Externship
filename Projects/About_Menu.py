def factorial(n): #recursive factorial function
    if (n == 0 or n==1): #base case
        return 1
    else: #call factorial again until base case is reached
        return (n * factorial(n-1))

def fibonacci(n): #recursive fibonacci sequence function
    if n == 0: #base case
        return 0
    elif n == 1: #base case
        return 1
    else: #call fibonacci again until base case is reached
        return fibonacci(n-1) + fibonacci(n-2)
        
run = True
while run:
    print("Welcome to the Recursive Artistry Program!")
    print("Choose an option: ")
    print("1. Calculate Factorial")
    print("2. Find Fibonacci")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")
    if choice == '1':
        factorial_input = input("Enter a number to find its factorial: ")
        if factorial_input.isdigit(): #isdigit() used to make sure input is viable
            factorial_input = int(factorial_input) #cast input to int
            factorial_result = factorial(factorial_input) #call factorial method to compute factorial
            print("The factorial of " + str(factorial_input) + " is " + str(factorial_result) + ".")
        else:
            print("Please enter a non-negative whole number.")   
    elif choice == '2':
        fibonacci_input = input("Enter the position of the Fibonacci number: ")
        if fibonacci_input.isdigit(): #isdigit() used to make sure input is viable
            fibonacci_input = int(fibonacci_input) #cast input to int
            fibonacci_result = fibonacci(fibonacci_input) #call fibonacci method to compute fibonacci sequence
            print("The " + str(fibonacci_input) + "th Fibonacci number is " + str(fibonacci_result) + ".")
        else:
            print("Please enter a non-negative whole number.")
    elif choice == '3':
        print("Thank you for using the Recursive Artistry Program!")
        print("Exiting program.")
        run = False
    else:
        print("Invalid option. Please choose between 1 and 3.")
