import logging
logging.basicConfig(filename='error_log.txt', level = logging.ERROR) #basic logging configuration

run = True
print("Welcome to the Error-Free Calculator!")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")
while run:
    choice = input("Choose an operation: ")
    if choice == '1':
        try:
            first_input = int(input("Enter the first number: "))
            second_input = int(input("Enter the second number: "))
        except Exception as e:
            logging.error(f"{type(e).__name__} occurred: {e}") #writes log entry and produces exact string with exception name and message
            print("Invalid input! Please enter a valid number.")
        else:
            result = first_input + second_input
            print("The sum of " + str(first_input) + " and " + str(second_input) + " is " + str(result) + ".")
    elif choice == '2':
        try:
            first_input = int(input("Enter the first number: "))
            second_input = int(input("Enter the second number: "))
        except Exception as e:
            logging.error(f"{type(e).__name__} occurred: {e}") #writes log entry and produces exact string with exception name and message
            print("Invalid input! Plase enter a valid number.")
        else:
            result = first_input - second_input
            print("The difference between " + str(first_input) + " and " + str(second_input) + " is " + str(result) + ".")
    elif choice == '3':
        try:
            first_input = int(input("Enter the first number: "))
            second_input = int(input("Enter the second number: "))
        except Exception as e:
            logging.error(f"{type(e).__name__} occurred: {e}") #writes log entry and produces exact string with exception name and message
            print("Invalid input! Plase enter a valid number.")
        else:
            result = first_input * second_input
            print("The product of " + str(first_input) + " and " + str(second_input) + " is " + str(result) + ".")
    elif choice == '4':
        try:
            first_input = int(input("Enter the first number: "))
            second_input = int(input("Enter the second number: "))
            result = first_input / second_input
        except ZeroDivisionError as e:
            logging.error(f"{type(e).__name__} occurred: {e}") #writes log entry and produces exact string with exception name and message
            print("Oops! Division by zero is not allowed.")
        except ValueError as e:
            logging.error(f"{type(e).__name__} occurred: {e}") #writes log entry and produces exact string with exception name and message
            print("Invalid input! Please enter a valid number.")
        else:
            print("The quotient of " + str(first_input) + " and " + str(second_input) + " is " + str(result) + ".")
    elif choice == '5':
        run = False
        print("Goodbye!")
    else:
        print("Invalid option. Please choose between 1 and 5.")
    