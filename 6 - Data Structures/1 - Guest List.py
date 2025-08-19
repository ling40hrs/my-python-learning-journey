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
        
        guest_pop_input = input("Enter the number of whom you want to remove n,n: ").strip().split(",")
        guest_pop_final = []
        guest_removed = []

        #validate first before removing
        
        for i in guest_pop_input:
            try:
                x = int(i) #convert to integer
                if 1 <= x <= len(guest_init): #checks if number provided is not less than 1 and not more than the guest count
                    if x not in guest_pop_final: #checks if duplicate
                        guest_pop_final.append(x)
                    else:
                        raise ValueError
                else:
                    raise ValueError
            except ValueError:
                print(f"{i} is not an integer/does not exist/a duplicate. It will be ignored.")
        
        guest_pop_final.sort(reverse=True)

        #mutation phase after validation

        for i in guest_pop_final:
             x = guest_init.pop(i-1)
             guest_removed.append(x)
        
        for i in guest_removed: #feedback
            print(f"{i} got removed from the list.")
        #can use print(f"\nSuccessfully removed: {', '.join(guest_removed)}\n") instead, but im too lazy to learn it for this specific case rn


    elif user_input == "4":
        sys.exit()