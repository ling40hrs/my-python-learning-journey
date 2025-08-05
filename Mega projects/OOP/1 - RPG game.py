
import random
print("--- Character Creation ---")
def get_username():
    while True:
        user_name_input = input("Enter your character's name > ").strip().title()
        if user_name_input == "" or len(user_name_input) > 10 or user_name_input.isdigit():
            print("Name cannot be empty/number, and must not be >10 characters. Please try again.")
            continue
        break
    return user_name_input

name = get_username()
strength = 1
health = 100

class Enemy:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def boss_attack(self):
        self.name = f"Giant {self.name}"
        self.damage *= 2
        print("")
        print(f"{self.name} did {self.damage} damage.")
        player.damage(self.damage)
        player.health_check()

        self.name = self.name.replace("Giant ", "") 
        self.damage = DEFAULT_NORMAL_ENEMY_DAMAGE              
    
    def attack(self):
        print(f"{self.name} did {self.damage} damage.")
        player.damage(self.damage)        
        player.health_check()
    
    def __str__(self):
        return f"{self.name} {self.damage}"

class Item:
    def __init__(self, name, damage=0, strength=0, luck=0, item_health=0, quantity=1):
        self.name = name
        self.damage = damage
        self.strength = strength
        self.luck = luck
        self.item_health = item_health
        self.quantity = quantity

weapons = [
    Item("Wooden Sword", damage=1),
    Item("Iron Sword", damage=5),
    Item("Cursed Dagger", damage=7, luck=-5, item_health=-10)
]

armor = [
    Item("Battle Armor", strength=4, item_health=10),
    Item("Old Boots", luck=1)
]

accessories = [
    Item("Lucky Charm", luck=10),
    Item("Warrior Amulet", strength=3, luck=2, item_health=5)
]

consumables = [
    Item("Healing Potion", item_health=20),
    Item("Golden Apple", strength=2, luck=5, item_health=15)
]

normal_enemy_names = ["Bat", "Slime", "Rat", "Goblin", "Cave Spider"]
game_enemies = []
DEFAULT_NORMAL_ENEMY_DAMAGE = 10

for enemy in normal_enemy_names:
    enemy_object = Enemy(enemy, DEFAULT_NORMAL_ENEMY_DAMAGE)
    game_enemies.append(enemy_object)

random_index = random.randint(0, len(normal_enemy_names) - 1) 

class Inventory:
    def __init__(self):
        self.slots = 27
        self.max_per_slots = 64
        self.available_slots = self.max_per_slots
        self.items = []
    def add(self):
        

    class Armor_slots:
        def __init__(self):
            self.arm_slots = 4

    def __str__(self):
        return f"""Available slots {self.available_slots}/{self.slots}"""

class Player:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength
        self.health = 100
    def damage(self, dmg_amount):
        self.dmg_amount = dmg_amount
        self.health -= self.dmg_amount
    def health_check(self):
        return print(f"You now have {self.health} health.")
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False
    def __str__(self):
        return f"""--- Character Sheet ---
Name: {self.name}
Health: {self.health}
Inventory:
"""


player = Player(name, strength)
inventory = Inventory()

print("""
Your adventure begins!""")
while player.is_alive():
    print("""
-------------------------
(1) Explore the dark cave
(2) Fight a boss
(3) Check your stats
(4) Quit the game
    """)
    try:
        choice =  int(input("What do you do? > ").strip())
    except ValueError:
        print("Invalid input, please try again.")
        continue

    if choice == 4:
        break
    elif choice == 3:
        print("")
        print(player)
        input("Press any key to go back > ")
    elif choice == 2:
        game_enemies[random_index].boss_attack()


