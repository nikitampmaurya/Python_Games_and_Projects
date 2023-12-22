"""
Description: Player must write the font colour of the given word. The game will have 10 rounds back to back.
For example: the given word is "white", then given option are "white" or "black". Here, the correct answer is "black", 
because player is expected to choose the colour of the font.  
"""

import random
from colorama import Fore, Style

def select_random_numbers():
    while True:
        num1 = random.randint(0, 5)
        num2 = random.randint(0, 5)
        num3 = random.randint(0, 5)
        if num1 != num2 and num1 != num3 and num2 != num3 and num1 != num2 != num3:
            break
    return num1, num2, num3

def print_random_word_and_options(word_list, color_list, num1, num2, num3):
    random_word = word_list[num1]
    random_color = color_list[num2]

    print(random_color + random_word + Style.RESET_ALL)

    list = [word_list[num3], word_list[num2]]
    random.shuffle(list)
    print(list[1], "or", list[0])

    return list, num2

def play_game():
    word_list = ["green", "white", "red", "purple", "blue", "yellow"]
    color_list = [Fore.GREEN, Fore.WHITE, Fore.RED, Fore.MAGENTA, Fore.BLUE, Fore.YELLOW]
    rounds = 0
    score = 0

    while rounds < 10:
        num1, num2, num3 = select_random_numbers()

        word_options, selected_color = print_random_word_and_options(word_list, color_list, num1, num2, num3)

        ans = input("a or b: ")
        new_list = {"a": word_options[1], "b": word_options[0]}

        if ans == "a" or ans == "b":
            if new_list[ans] == word_list[selected_color]:
                print("correct")
                score += 1
            else:
                print("wrong")
        else:
            print("Invalid input! Please choose 'a' or 'b'.")

        rounds += 1

    print("Your score:", score, "/", rounds)

# Run the game
play_game()
