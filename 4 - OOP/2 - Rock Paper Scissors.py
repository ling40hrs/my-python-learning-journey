import random, sys

print("ROCK, PAPER, SCISSORS")

moves = ["r", "p", "s"]

move_wins = {
    "r": "s",
    "s": "p",
    "p": "r"
}

class Player:
    def __init__(self, wins=0, losses=0, ties=0):
        self.wins = wins
        self.losses = losses
        self.ties = ties

    def stats(self):
        print(f"{self.wins} Wins, {self.losses} Losses, {self.ties} Ties.")

    def user_input(self):
        player_move = input("> ")
        return player_move
    def tie(self):
        self.ties += 1
        print("It's a tie!")
    def win(self):
        self.wins += 1
        print("You won!")
    def lose(self):
        self.losses += 1
        print("You lost!")

class Enemy:
    def move(self):
        enemy_move = random.choice(moves)
        return enemy_move

player = Player()
enemy = Enemy()

while True:
    print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
    try:
        y = player.user_input()   
        x = enemy.move()
        player.stats()         
        if y == x:
            player.tie()
        elif y == "q":
            sys.exit()
        elif move_wins[y] == x:
            player.win()            
        else:
            player.lose()
        print(f"Computer chose {x}")
    except ValueError:
        continue
