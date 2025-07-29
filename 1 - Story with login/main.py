username = "Ling"
password = "LingLing123"
while True:
    un_input = input("Enter username: ")
    pw_input = input("Enter password: ")
    un_chck = un_input == username
    pw_chck = pw_input == password


    if [un_input, pw_input] == ["Admin", "12345"]:
        login_status = True
        print("Admin login.")
        break

    elif un_chck:
        if pw_chck:
            print("Login successful.")
            login_status = True
            break
        else:
            print("Incorrect password.")
    else:
        print("Incorrect username.")


door = ["wooden", "stone"]
action = ["read", "ignore"]
sneak_threshold = 5
stone = 0

while True:
    print("""You stand before two doors in a spooky old castle.
One is a large 'wooden' door. The other is a 'stone' door.""")
    door_input = input("Which door do you choose? (wooden/stone): > ")
    if door_input == "wooden":
        print("You enter a dusty library. In the center is a book on a pedestal.")
        action_input = input("Do you 'read' the book or 'ignore' it? > ")
        if action_input == "read":
            print("You gain ancient knowledge! You win!")
            break
        elif action_input == "ignore":
            print("The book was a trap! The floor gives way. You lose.")
            break
    elif door_input == "stone":
        print("The door grinds open to reveal a long, dark hallway with a single torch.")
        stone = 1
        break
    else:
        print("Invalid input!")
        print("---*---" * 6)

while stone == 1:
    sneak = input("A monster is sleeping. How many steps do you take to sneak past it? (Enter a number): > ")
    if int(sneak) <= sneak_threshold:
        print("You sneak past successfully! You win!")
        break
    elif int(sneak) > sneak_threshold:
            print("You took too much steps leading to the monster detecting you. Try again!.")