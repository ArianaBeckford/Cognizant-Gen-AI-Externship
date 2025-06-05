#Task 1 - Slicing and Indexing

first_string = "Python is amazing!"
print("First word: " + first_string[0:6])
print("Amazing part: " + first_string[10:17])
print("Reversed string: " + first_string[::-1])

#Task 2 - String Methods
second_string = " hello, python world! "
rmv_spaces = second_string.strip()
print("This is the string with the extra spaces removed: " + rmv_spaces)
capitalized = rmv_spaces.capitalize()
print("This is the string with the first letter capitalized: " + capitalized)
replaced = capitalized.replace("world", "universe")
print("This is the string with a word replaced: " + replaced)
uppercase = replaced.upper()
print("This is the string fully capitalized: " + uppercase)

#Task 3 - Check for Palindromes

third_string = input("Choose a word: ").lower()
reversed_string = third_string[::-1]
if third_string == reversed_string:
    print("Yes, " + third_string + " is a palindrome!")
else:
    print("No, " + third_string + " is not a palindrome.")