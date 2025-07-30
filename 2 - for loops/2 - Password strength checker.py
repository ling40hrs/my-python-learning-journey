"""
A Strong password must be at least 8 characters long AND contain at least one uppercase letter, one lowercase letter, and one number.
A Medium password meets some but not all of the criteria for a strong password.
A Weak password is less than 8 characters long.
"""

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

    has_uppercase = False
    has_lowercase = False
    has_number = False

while True:

    password_input = input("Enter your password here or enter 'quit' to quit: ")

    if password_input == "quit":
        break

    pw_length = len(password_input)
    if pw_length < 8:
        weak = True

    if weak:
        print("Your password is weak! Try again.")
        weak = False #I WAS STARING AT MY TERMINAL ON WHY ITS STILL WEAK AFTER INPUTTING MEDIUM PASSWORD, I FIGURED OUT THAT ITS ALWAYS TRUE AFTERWARDS T_T (kinda felt genius after it though :P)
        continue



    for characters in password_input:

        if characters.isupper:
            has_uppercase = True
        if characters.isdigit:
            has_number = True
        if characters.islower:
            has_lowercase = True        





    if (has_uppercase or has_lowercase or has_number) and not weak:
        medium = True
        reset()

    if medium:
        print("Your password is moderately weak! Try again.")
        continue
    
