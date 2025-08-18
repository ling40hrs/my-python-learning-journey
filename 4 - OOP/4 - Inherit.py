'''
Basic 1v1 simulation, bias towards hero.
'''

import random

class Character:
    def __init__(self, name, health=100, is_alive=True):
        self.name = name
        self.health = health
        self.is_alive = is_alive

    def life(self):
        if self.health <= 0:
            self.is_alive = False

    def alive_check(self):
        return self.is_alive

    def attack(self, target):
        print(f"{self.name} attacks {target.name}!")
        rand_damage = random.randrange(5,10)
        target.health -= rand_damage
        if target.health <= 0:
            target.health = 0
            target.is_alive = False
        else:
            print(f"{target.name} has {target.health} health left")

class Player(Character):
    def __init__(self, name, health=100, is_alive=True):
        super().__init__(name, health, is_alive)
    
    def potion(self, status):
        self.status = status
        if self.status == True:
            potion_random_effect = random.randrange(5,10)
            old_health = []
            old_health.append(self.health)
            self.health += potion_random_effect
            if self.health > 100:
                self.health = 100        
            print(f"{self.name} took a potion. They now have ", end = "") 
            print(*old_health, end="")
            print(f" -> {self.health} health.")
            old_health = []
        else:
            return None

class Enemy(Character):
    def __init__(self, name, health=100, is_alive=True):
        super().__init__(name, health, is_alive)

player1 = Player("Hero")
enemy1 = Enemy("Goblin")

while True:
    player1.life()
    enemy1.life()
    turn = 0
    while player1.is_alive == True and enemy1.is_alive == True:
        turn += 1
        print(f"--- Turn {turn} ---")
        
        if player1.alive_check() == True:
            if turn != 1:
                player1.potion(random.choice([True, False]))
            player1.attack(enemy1)      

        if enemy1.alive_check() == True:
            enemy1.attack(player1)     

        if enemy1.alive_check() == False:
            print(f"{player1.name} won!")
            break

        elif player1.alive_check() == False:
            print(f"{enemy1.name} won!")
            break
    break