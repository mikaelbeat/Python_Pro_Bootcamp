

from cgitb import reset
from itertools import count
from unittest import result


name1 = "Jack Bauer"
name2 = "Angela Yu"

true = ["t", "r", "u", "e"]
true_result = 0

love = ["l", "o", "v", "e"]
love_result = 0



def calculate_love(name1, name2):
    for letter in true:
        global true_result
        letter_result = 0
        result = name1.lower().count(letter)
        letter_result += result
        true_result += result
        result = name2.lower().count(letter)
        letter_result += result
        true_result += result
        print(f"{letter.upper()} occurs {letter_result} times.")
        
    print("------------------")
    print(f"Total score is {true_result}.\n")
    
    for letter in love:
        global love_result
        letter_result = 0
        result = name1.lower().count(letter)
        letter_result += result
        love_result += result
        result = name2.lower().count(letter)
        letter_result += result
        love_result += result
        print(f"{letter.upper()} occurs {letter_result} times.")

    print("------------------")
    print(f"Total score is {love_result}.")
    print(f"\nLove score is {true_result}{love_result}.")


calculate_love(name1, name2)
