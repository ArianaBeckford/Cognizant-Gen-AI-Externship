#Task 1 - Variables: Your First Python Intro

name = "Katniss Everdeen"
age = 17
height = 5.9

print("Hey there, my name is " + name + "! I'm " + str(age) + " and " + str(height) + " feet tall.")

#Task 2 - Operators: Playing with Numbers

num1 = 6
num2 = 3
print("The sum of 6 and 3 is", num1 + num2) #printing addition
print("The difference of 6 and 3 is", num1 - num2) #printing subtraction
print("The product of 6 and 3 is", num1*num2) #printing multiplication
print("The quotient of 6 and 3 is", num1//num2) #printing floor division

#Task 3 - Conditional Statements: The Number Checker
number = int(input("Enter a number: ")) #cast input as int
if number > 0:
    print("This number is positive. Awesome!")
elif number < 0:
    print("This number is negative. Better luck next time!")
else:
    print("Zero it is. A perfect balance!")
