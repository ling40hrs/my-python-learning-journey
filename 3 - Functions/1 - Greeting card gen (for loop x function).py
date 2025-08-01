"""
Mini-Project: The Reusable Greeting Card
Objective:
You will write a program that prints several personalized greeting cards. \
    You will do this by creating a single, simple function that contains the "recipe" for a \
        greeting, and then you will call that function multiple times with different names.

Concepts You'll Need to Use:
Defining a function using the def keyword.
Naming a function and defining its parameters (the inputs it needs).
Calling a function by its name and passing it arguments (the actual values for the parameters).
Using f-strings or string concatenation inside your function.
"""
name_list = ["Alice", "Bob", "Charlie"]

print("--- Generating Cards ---")

def greeting_cards(name):
    """
    Prints a personalized greeting card for the given name.
    """
    print(f"""***************************
Happy Birthday, {name}!
Hope you have a wonderful day.
***************************
""")

for names in name_list:
    greeting_cards(names)
