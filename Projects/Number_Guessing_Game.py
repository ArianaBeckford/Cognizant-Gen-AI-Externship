import random
number_to_guess = random.randint(1, 100)
#print(number_to_guess) #used for testing
correct = False #end while loop when correct is true
attempts = 0 #number of attempts
while(correct == False and attempts <= 10): #runs prompt until user correctly guesses or runs out of attempts
    attempts += 1 #increase attempts by 1 at beginning of each loop
    guess = int(input("Guess the number (between 1 and 100): "))
    if guess == number_to_guess:
        print(str(guess) + " is correct. Congratulations! You guessed it in " + str(attempts) + " attempts!")
        correct = True
    elif guess < number_to_guess:
        print(str(guess) + " is too low! Try again.")
    else:
        print(str(guess) + " is too high! Try again.")
if attempts > 10: #print game over message if user runs out of attempts
    print("Game over! Better luck next time!")
