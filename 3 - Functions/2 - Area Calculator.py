"""
This module contains functions for calculating geometric areas.
"""

def calculate_square_area(side_length):
    """
    Calculates the area of a square given its side length.
    """
    square_area = side_length * side_length
    return square_area

def calculate_triangle_area(base, height):
    """
    Calculates the area of a triangle given its base and height.
    """
    triangle_area = (base * height) / 2
    return triangle_area

while True:

    shape = input("What shape do you want to calculate? ('square' or 'triangle')> ").strip().lower()

    if shape == "square":
        try:
            length = float(input("What is the side length? > "))
            square_result = calculate_square_area(length)
            print(f"The area of the square is {square_result}")
            break
        except ValueError:
            print("Try again")

    elif shape == "triangle":
        try:
            base_input = float(input("Enter number of base > "))
            height_input = float(input("Enter number of height > "))
            triangle_result = calculate_triangle_area(base_input, height_input)
            print(triangle_result)
            break
        except ValueError:
            print("Try again")
