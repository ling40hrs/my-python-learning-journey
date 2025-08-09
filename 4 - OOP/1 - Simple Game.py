
import random

items = [
"Rusty Sword",
"Iron Sword",
"Diamond Sword"
]

inventory = []

class Player:

    def __init__(self, name, strength, health=100):
        self.name = name
        self.strength = strength
        self.health = health
    def healthh(self):
        return self.health
    def explore(self):
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

    def attack(self):
        taken_damage = random.randrange(2,7)
        if self.strength >= 5:
            taken_damage *= 0.5
        self.health -= taken_damage
        self.health = round(self.health)
        print(f"""You fought bravely! You took {taken_damage} damage.
Your current health is {self.health}""")

    def stats(self):
        print(f"""--- Character Sheet ---
Name: {self.name}
Health: {self.health}
Strength: {self.strength}
Inventory:
{inventory}""")
        input()

print("--- Character Creation ---")

hero_name = input("Enter your hero's name: > ")
strength = int(input("Enter your strength (1-10): > "))

player = Player(hero_name, strength)

while player.healthh() > 0:
    print("""Your adventure begins!
-------------------------
(1) Explore the dark cave
(2) Fight the goblin
(3) Check your stats
(4) Quit the game
""")
    try:
        user_input = int(input("What do you do? > "))
        if user_input == 1:
            player.explore()
        elif user_input == 2:
            player.attack()
        elif user_input == 3:
            player.stats()
        elif user_input == 4:
            break
    except ValueError:
        continue