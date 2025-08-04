
import random

user_input_prompts = ["Input strength 1-10 > ", "Input health 1-100 > "]

def get_username():
    while True:
        user_name_input = input("Enter your character's name > ").strip().title()
        if user_name_input == "" or len(user_name_input) > 10 or user_name_input.isdigit():
            print("Name cannot be empty/number, and must not be >10 characters. Please try again.")
            continue
        break
    return user_name_input

def integer_inputs(less_than, greater_than, prompt):
    while True:
        try:
            user_input_stats = int(input(prompt))
            if user_input_stats < less_than or user_input_stats > greater_than:
                print(f"Invalid input! Enter {less_than}-{greater_than} only.")
                continue
            return user_input_stats
        except ValueError:
            print("Invalid input!")
            continue

name = get_username()
strength = integer_inputs(1,10,"Input strength 1-10 > ")
health = integer_inputs(1,100,"Input health 1-100 > ")

for luck in range(1,11,1):


stats = [strength, health]

normal_enemies = ["Bat", "Slime", "Rat", "Goblin", "Cave Spider"]

heavy_enemies = []

for heavy_concatinate in normal_enemies:
    heavy_enemies.append("Giant " + heavy_concatinate)

print