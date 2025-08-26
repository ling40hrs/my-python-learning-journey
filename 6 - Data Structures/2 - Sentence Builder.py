'''
List
Uses .join method,
if/else expression inside f string
'''

raw_sentence = []
loop = False
                      
while True:

    print(f"""\n--- Sentence Builder ---

Your sentence so far: {
    
        " ".join(raw_sentence)
        if loop == True
        else
        ""
    } 
-------------------------
(1) Add a word
(2) Undo (remove the last word)
(3) Done (view the final sentence)""")
    
    user_input = input("> ")

    if user_input == "1":
        input_word = input("Enter a word: > ")
        raw_sentence.append(input_word.strip())
        loop = True

    elif user_input == "2":
        if raw_sentence:
            del raw_sentence[-1]
        else:
            print("Nothing to delete")
    
    elif user_input == "3":
        break

    else:
        print("Unknown!")

print(f"""Here is your final sentence:
{" ".join(raw_sentence) if loop else "Did not get input"}.""")