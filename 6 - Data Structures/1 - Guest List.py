'''
Lists
'''

import sys

guest_init = []

while True:
    
    print("""--- Guest List Manager ---
    (1) View Guest List
    (2) Add Guest
    (3) Remove Guest
    (4) Quit""")
    user_input = input("> ")
    
    if user_input == "1":
        if not guest_init:
            print("No guests yet.")
            continue
        else:
            for i, names in enumerate(guest_init, 1):
                print(f"{i}. {names}")

    elif user_input == "2":
        while True:
            guest_input = input("Enter a guest name, press q to go back to menu: ").title()
            if guest_input == "Q":
                break
            guest_init.append(guest_input)

    elif user_input == "3":
        for i, names in enumerate(guest_init,1):
            print(f"{i}. {names}")
        
        guest_pop_input = input("Enter the number of whom you want to remove n,n: ").strip()
        try:
            guest_remove_list = sorted(map(int,guest_pop_input.split(",")),reverse=True)

            for i in guest_remove_list:
                if 1 <= i <= len(guest_init):
                    try:
                        x = int(i) - 1
                        del guest_init[x]
                    except:
                        print(f"{i} is invalid. (Try/except block)")
                else:
                    print(f"{i} is invalid. (If block)")
        except ValueError:
            print("ValueError")

    elif user_input == "4":
        sys.exit()