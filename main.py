import generator
import converToJson
from random import randint, choice
import json

# !NSL = No Suggestion List
with open('notSuggestionList_game.json') as file:
    nicknames = json.load(file)

with open('nicknames.json', 'r') as previous_nicknames:
    previous_nicknames = json.load(previous_nicknames)

NSL_game = nicknames['NSL_game']
NSL_social = []  # Nickname Suggestions List

block_break = False  # If true, the program will break out of the loop
word_suggestions = []  # To store all the word suggestions

showPreviousNicknames = str(input(
    "Do you want to know the previous nicknames generated? [Y/N]\n")).lower().strip()

if (showPreviousNicknames == "y" or showPreviousNicknames == "yes"):
    if len(previous_nicknames) == 0:
        print("\nThere is no previous nicknames generated\n")
    else:
        print()
        for i in range(len(previous_nicknames)):
            print(previous_nicknames[i])
            print()

while True:
    if block_break:  # If the user wants to break out of the loop
        break
    try:
        user_input = input("\nWould you like to suggest a specific word?\nYes or No: ")
        if user_input == 'yes' or user_input == 'Yes' or user_input == 'y' or user_input == 'Y':
            try:
                specific_word = str(input("Please type the word:\n"))
                # Append the word to the list
                word_suggestions.append(specific_word)
            except ValueError:
                print("Please enter a valid word.")
            while True:
                user_input = input("Would you like to add another word?\nYes or No: ")
                if user_input == 'yes' or user_input == 'Yes' or user_input == 'y' or user_input == 'Y':
                    specific_word = input("Please type the word:\n")
                    if user_input in word_suggestions:
                        print("This word is already in the list.")
                    else:
                        word_suggestions.append(specific_word)
                else:
                    # If the user doesn't want to add another word, the program will break out of the loop
                    block_break = True
                    break
        elif user_input == 'no' or user_input == 'No' or user_input == 'n' or user_input == 'N':
            print()  # Print a blank line
            break
        else:
            print("Error - unexpected input")
    except ValueError:
        print("Error - unexpected input")

# ==============================================================================

block_break = False  # Resetting block_break to False
num_suggestions = []  # list of numbers of suggestions

while True:
    if block_break:  # If the user wants to break out of the loop
        break
    try:
        user_input_num = input(
            "Would you like to add some numbers?\nYes or No: ")
        if user_input_num == 'yes' or user_input_num == 'Yes' or user_input_num == 'y' or user_input_num == 'Y':

            try:
                # input number of suggestions
                num_input = int(input("Please type the numbers:\n"))
                # add number of suggestions to list
                num_suggestions.append(num_input)
            except ValueError:  # if user input is not a number
                print("Error - unexpected input")  # print error message

            while True:  # loop until user input is valid
                user_input = input(
                    "Would you like to add more numbers?\nYes or No: ")
                if user_input == 'yes' or user_input == 'Yes' or user_input == 'y' or user_input == 'Y':
                    try:
                        num_input = int(input("Please type the numbers:\n"))
                        if num_input in num_suggestions:
                            print("Error - number already exists")
                        else:
                            num_suggestions.append(num_input)
                    except ValueError:
                        print("Error - unexpected input")
                if user_input == 'no' or user_input == 'No' or user_input == 'n' or user_input == 'N':
                    # If the user doesn't want to add another number, the program will break out of the loop
                    block_break = True
                    break

        elif user_input_num == 'no' or user_input_num == 'No' or user_input_num == 'n' or user_input_num == 'N':
            print()
            break
    except ValueError:
        print("Error - unexpected input")

user_input_total = int(input("How many nicknames do you want to generate?\n"))
print()

generated_nickname = generator.generator_nickname(
    NSL_game, word_suggestions, num_suggestions, user_input_total)  # call the generator function
for x in range(len(generated_nickname)):
    print(f"{generated_nickname[x]}\n")
