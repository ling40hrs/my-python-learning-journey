
import random

print("--- Character Creation ---")

hero_name = input("Enter your hero's name: > ")
strength = int(input("Enter your strength (1-10): > "))
health = int(input("Enter your starting health: > "))

items = [
"Rusty Sword",
"Iron Sword",
"Diamond Sword"
]

inventory = []

def explore():
    is_duplicate = False
    item_index = items[random.randrange(0,len(items))]
    for item in inventory:
        if item == item_index:
            is_duplicate = True
            break
    if not is_duplicate:
        inventory.append(item_index)
        print(f"You found 1 {item_index}")  
    else:
        print(f"Already has {item_index}")
def attack():
    global health
    taken_damage = random.randrange(2,7)
    if strength >= 5:
        taken_damage *= 0.5
    health -= taken_damage
    health = round(health)
    print(f"""You fought bravely! You took {taken_damage} damage.
Your current health is {health}""")

def stats():
    print(f"""--- Character Sheet ---
Name: {hero_name}
Health: {health}
Strength: {strength}
Inventory:
 {inventory}""")
    input()
    
while health > 0:
    print("""Your adventure begins!
-------------------------
(1) Explore the dark cave
(2) Fight the goblin
(3) Check your stats
(4) Quit the game
""")
    user_input = int(input("What do you do? > "))
    if user_input == 1:
        explore()
    elif user_input == 2:
        attack()
    elif user_input == 3:
        stats()
