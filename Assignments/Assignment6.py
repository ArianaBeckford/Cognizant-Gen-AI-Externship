#Task 1 - Understanding Python Exceptions
try:
    number_input = int(input("Enter a number: "))
    quotient = 100 / number_input
    print("100 divided by " + str(number_input) + " is " + str(quotient) + ".")
except ZeroDivisionError:
    print("Oops! You cannot divide by zero.")
except ValueError:
    print("Please enter a valid number.")

#Task 2 - Types of Exceptions
try:
    a = [2, 4, 6]
    print(a[3])
except IndexError:
    print("IndexError occurred! List index out of range.")

try:
    student_dict = {'Class_Standing': 'Senior', 'GPA': 3.5}
    student_id = student_dict['ID']
    print(student_id)
except KeyError:
    print("Key not found in the dictionary")

try:
    print("Apple" + 4)
except TypeError:
    print("TypeError occurred! Unsupported operand types.")

#Task 3 - Using try...except...else...finally
try:
    first_input = int(input("Enter the first number: "))
    second_input = int(input("Enter the second number: "))
    result = first_input / second_input
except ZeroDivisionError:
    print("Oops! You cannot divide by zero.")
except ValueError:
    print("Please enter a valid number.")
else:
    print("The result is " + str(result) + ".")
finally:
    print("This block always executes.")