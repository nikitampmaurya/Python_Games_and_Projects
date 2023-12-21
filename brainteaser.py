"""
Description: Player msut write the font of the given word. 
"""

import random
from colorama import Fore, Style

# List of words
word_list = ["green","white","red","purple","blue","yellow"]

# List of colors
color_list = [Fore.GREEN, Fore.WHITE, Fore.RED, Fore.MAGENTA, Fore.BLUE, Fore.YELLOW]

while True:
    num1 = random.randint(0, 5)
    num2 = random.randint(0, 5)
    num3 = random.randint(0, 5)
    if num1 != num2 and num1 != num3 and num2 != num3:
        break
# Select a random word and a random color
random_word = word_list[num1]
# Select a random word and a random font
random_color = color_list[num2]

# Print the word in the selected color
print(random_color + random_word + Style.RESET_ALL)
#preparing question, we need to shuffle the two words in the questions
list = [word_list[num3], word_list[num2]]
random.shuffle(list)
print(list[1], "or", list[0])
ans = input("a or b: ")
new_list = {"a":list[1], "b":list[0]}
#print(new_list)
#print("answer: ",ans)
#print("word_list[num2]: ",word_list[num2])
if ans == "a":
    if new_list[ans] == word_list[num2]:
        print("correct")
    else:
        print("wrong")
else:
    if ans == "b":
        if new_list[ans] == word_list[num2]:
            print("correct")
        else:
            print("wrong")

