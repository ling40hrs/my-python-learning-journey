import sys

character = {
    "Name": "Arin",
    "Class": "Warrior",
    "Strength": 8,
    "Health": 100
}
def view_stats():
    for x,y in character.items():
        print(f"{x}: {y}")    

def get_nonempty(prompt):   #for validation
    while True:
        value = input(prompt).strip()
        if value:
            return value

while True:
    print("""--- Character Creator ---
(1) View Character Stats
(2) Change a Stat
(3) Add a New Attribute
(4) Quit""")
    
    user_input = input("> ")

    if user_input == "1":
        view_stats()
        input("")

    elif user_input == "2":
        is_present = False 
        view_stats()

        while not is_present:   #validate first
            change_key_input = input("What do you want to change? > ")
            for x in character:
                if change_key_input == x:
                    is_present = True
                    break
            if not is_present:
                print("Invalid input. Case sensitive")

        change_value_input = input("To? > ")
        character[change_key_input.strip()] = change_value_input.strip()
        view_stats()

    elif user_input == "3":
        add_key_input = get_nonempty("What do you want to add? > ")
        add_value_input = get_nonempty("Value > ")
        character[add_key_input] = add_value_input 
        view_stats()

    elif user_input == "4":
        sys.exit()