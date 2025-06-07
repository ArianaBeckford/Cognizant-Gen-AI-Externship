password = input("Enter a password: ")
length_check = False
upper_check = False
lower_check = False
digit_check = False
special_char_check = False
score = 0
if len(password) >= 8:
    length_check = True #1
    score += 2

for i in range(len(password)):
    if password[i].isupper():
        upper_check = True #2
    elif password[i].islower():
        lower_check = True #3
    elif password[i].isdigit():
        digit_check = True #4
    else:
        special_char_check = True #5

missing = [] #append missing requirements message to this list
if not length_check:
    missing.append("at least 8 characters")

if not upper_check:
    missing.append("at least one uppercase letter")
else:
    score += 2

if not lower_check:
    missing.append("at least one lowercase letter")
else:
    score += 2

if not digit_check:
    missing.append("at least one digit")
else:
    score += 2

if not special_char_check:
    missing.append("at least one special character")
else:
    score += 2

if len(missing) == 0:
    print("Your password is strong!")
else:
    m = "Your password needs: "
    if len(missing) == 1:
        print(m + missing[0] + ".")
    elif len(missing) == 2:
        print(m + " and ".join(missing) + ".")
    else:
        message = ", ".join(missing[:-1]) + ", and " + missing[-1] + "."
        print(m + message)
print("Your password strength score is: " + str(score) + " out of 10.")