'''
Create a program that simulates renaming a list of files by adding a prefix \
    (like vacation_) to each one.
This will force you to see how the for loop takes one item (x) from a list (y), \
    lets you work with it,
and then moves on to the next.

Concepts You'll Need to Use:
Creating a list of strings.
A for loop to iterate over that list.
input() to get the prefix from the user.
String concatenation (+) to build the new "filenames".

⭐ Extra Challenge:
Modify your program so it only renames files that are images. 
Add an if statement inside your for loop to check if the current filename (x) \
    ends with .jpg or .png before printing
the "Renaming..." line. (Hint: strings have a helpful .endswith() method).
'''

files = []

while True:

    files_input = input("Enter your desired file here with their extension name; one at a time. > ")
    print("Enter 'done' if done.")

    if files_input.lower() == "done":
        break

    files.append(files_input)

prefix_input = input("What prefix would you like to add? > ")
print("--- Renaming Files ---\n")

for pi in files:
    if pi.endswith((".jpg", ".png")) : #uses a tuple
        x = f"{prefix_input}{pi}"
        y = f"Renaming '{pi}'  >>  '{x}'"
        print(y)
    else:
        print(f"Did not rename '{pi}'; not a .jpg nor .png file.")
        continue

print("--- Done ---")
