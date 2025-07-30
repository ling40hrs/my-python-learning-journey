'''
Mini-Project: The Vowel & Consonant Counter
Objective:
Write a program that asks the user for a word or phrase and then calculates and reports how many vowels and how many consonants it contains.
Concepts You'll Need to Use:
for loops to iterate over a string.
if/elif/else statements to make decisions.
Variables to use as counters.
input() to get text from the user.
String methods, specifically .lower() to simplify your checks.
'''
VOWELS: str = {"a","e","i","o","u"} #intentionally uses set instead of list for efficient searching
vowels_out: int = 0



input_word: str = input("Please enter a word or phrase: > ")
input_word_striplower = input_word.strip().lower().replace(" ", "")

for vowelchar in input_word_striplower:
    if vowelchar in VOWELS:
        vowels_out += 1
consonants_out: int = len(input_word_striplower) - vowels_out

print("--- Analyzing ---")
print(f"""Vowels: {vowels_out}
Consonants: {consonants_out}
""")
