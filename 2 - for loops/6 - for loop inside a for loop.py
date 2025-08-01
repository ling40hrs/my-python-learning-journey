"""The ASCII Art Drawer"""

print("--- ASCII Art Drawer ---")
row_input = 0
char = ""

def inputs():
    """
    This function takes user input for the size and character.
    It modifies global variables 'row_input' and 'char'.
    """
    global row_input, char
    row_input = int(input("What size? > "))
    char = input("What character? > ")

row_input_int = int(row_input)

while True:
    shape = input("What shape would you like to draw (square/triangle)? > ")
    if shape == "square":
        inputs()
        for row in range(row_input):
            print("")
            for coloumn in range(row_input):
                print(char, end = "")
        break

    elif shape == "triangle":
        inputs()
        x=0
        for row in range(row_input):
            x += 1
            print("")
            for coloumn in range(x):
                print(char, end = "")
        break
