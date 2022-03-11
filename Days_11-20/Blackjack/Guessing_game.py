
import random
from replit import clear


NUMBER = random.randint(1, 100)
EASY_MODE = 10
HARD_MODE = 5

playing_game = True


def choose_difficulty():
    difficulty = input("Choose difficulty, easy or hard? ")
    if difficulty == "easy":
        print("You chose easy mode and have 10 guesses in total.")
        return EASY_MODE
    else:
        print("You chose hard mode and have 5 guesses in total.")
        return HARD_MODE


def play_game(tries):  
    guesses_left = tries
    guess = 0
    while guess != NUMBER:
        if guesses_left > 0:
            guess = int(input("\nMake a guess: "))
            if guess > NUMBER:
                guesses_left -= 1
                print("Too high, guess again.")
                print(f"You have {guesses_left} guesses left.")
            elif guess < NUMBER:
                guesses_left -= 1
                print("Too low, guess again.")
                print(f"You have {guesses_left} guesses left.")
            else:
                print("You guessed the number!")
                print(f"You had {guesses_left} guesses left.")
        else:
            print("No more guesses left, game over!")
            print(f"Number was {NUMBER}.")
        
clear()
print("*** Guessing game ***\n")
print("Try to guess number between 1 and 100")
tries = choose_difficulty()
play_game(tries)

