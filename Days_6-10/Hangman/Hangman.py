
import random, os

import Hangman_art as art, Hangman_words as words


print(f"{art.logo}\n")

lives = 6

random_word = random.choice(words.word_list)
random_word_lenght = len(random_word)

random_word_list = []
guessed_letters = []

for letter in range(random_word_lenght):
    random_word_list.append("_")


while "_" in random_word_list and lives > 0:
    
    guess = input("\nGuess a letter: ").lower()
        
    if guess in random_word and guess not in guessed_letters:
      os.system("cls")
      print(art.stages[lives])
      guessed_letters.append(guess)
      for position in range(random_word_lenght):
          letter = random_word[position]
          if letter == guess:
              random_word_list[position] = letter 
      print(f"\n{ ' '.join(random_word_list)}\n")
    elif guess in guessed_letters:
      os.system("cls")
      print(art.stages[lives])
      print(f"\nYou have already guessed letter {guess}.")
    else:
        os.system("cls")
        guessed_letters.append(guess)
        lives -= 1
        if lives > 0:
            os.system("cls")
            print(art.stages[lives])
            print(f"Guesses left: {lives}")
            print(f"\n{ ' '.join(random_word_list)}\n")
        else:
            os.system("cls")
            print(art.stages[lives])
            print("\nNo more guesses left, GAME OVER!")
            print(f"Word was {random_word}.")
            exit()


