"""
A Strong password must be at least 8 characters long AND contain at least one uppercase letter, one lowercase letter, and one number.
A Medium password meets some but not all of the criteria for a strong password.
A Weak password is less than 8 characters long.
"""
import sys

strong = False
medium = False
weak = False
pw_length = 0

has_uppercase = False
has_lowercase = False
has_number = False



def reset():
    global has_uppercase
    global has_lowercase
    global has_number
    global weak
    global medium

    has_uppercase = False
    has_lowercase = False
    has_number = False
    weak = False
    medium = False

while True:
    reset()
    password_input = input("Enter your password here or enter 'quit' to quit: ")

    if password_input == "quit":
        sys.exit()

    pw_length = len(password_input)
    if pw_length < 8:
        weak = True

    if weak:
        print("Your password is weak! Try again.")
        reset() #weak = False -> reset() I WAS STARING AT MY TERMINAL ON WHY ITS STILL WEAK AFTER INPUTTING MEDIUM PASSWORD, I FIGURED OUT THAT ITS ALWAYS TRUE AFTERWARDS T_T (kinda felt genius after it though :P)
        continue

    for characters in password_input:
        if characters.isupper():
            has_uppercase = True
        if characters.isdigit():
            has_number = True
        if characters.islower():
            has_lowercase = True        

    strong_status = has_lowercase and has_number and has_uppercase and not weak
    if strong_status is True:
        print("Your password is strong!")
        sys.exit()

    if (has_uppercase or has_lowercase or has_number) and not weak:
        medium = True

    if medium:
        print("Your password is moderately weak! Try again.")
        reset()
        continue
    else:
        print("Try again!")
