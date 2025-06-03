#Step 1: Ask the User’s Age
age = int(input("How old are you? "))
#Step 2: Decide the Eligibility
if age >= 18: #if user is at least 18 they can vote
    print("Congratulations! You are eligible to vote. Go make a difference!")
else: #otherwise calculate how many years they have until they can vote
    years_to_go = 18 - age
    print("Oops! You're not eligible yet. But hey, only " + str(years_to_go) + " more years to go!")
