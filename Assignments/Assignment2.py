#Task 1 - Counting Down with Loops
#prints from input number down to 1
start_num = int(input("Enter the starting number: "))
while (start_num > 0):
    print(start_num)
    start_num = start_num - 1
print("Blast off!")

#Task 2 - Multiplication Table with for Loops
#prints multiplcation table for input from 1 to 10
mult_num = int(input("Enter a number: "))
for i in range(1, 11):
    prod = mult_num * i
    print(str(mult_num) + " x " + str(i) + " = " + str(prod))

#Task 3 - Find the Factorial
input_num = int(input("Enter a number: "))
result = input_num
count = result - 1
while(count > 0):
    result = result * count
    count = count - 1
print("The factorial of " + str(input_num) + " is " + str(result))