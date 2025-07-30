"""
A string inspector that uses for loops.
"""
total = 0 

print("--- String Inspector ---")

word_input = input("Please enter a word or phrase: ")
specific_letter = input("What specific letter are you looking for? > ")
print(f"--- Inspecting '{word_input}' ---")

for word_search in word_input:
    if word_search == specific_letter:
        total = total + 1

print(f"Found the letter '{specific_letter}' a total of {total} times.")