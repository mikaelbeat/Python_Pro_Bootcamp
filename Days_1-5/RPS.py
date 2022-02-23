
import random


print("*** Rock Paper Scissors ***\n")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("What would you choose?")
#selection = input("0 -> Rock, 1 -> Paper and 2 -> Scissors: ")
signs = [rock, paper, scissors]
value = "0"
selection = signs[int(value)]
ai_selection = random.choice(signs)

if selection == rock:
    print(rock)
elif selection == paper:
    print(paper)
else:
    print(scissors)
    
print("\n*** AI selection ***\n")

if ai_selection == rock:
    print(rock)
elif ai_selection == paper:
    print(paper)
else:
    print(scissors)
    
if selection == rock and ai_selection == scissors:
    print("You win! Rock wins against scissors.") 
elif selection == paper and ai_selection == rock:
    print("You win! Paper wins against rock.")  
elif selection == scissors and ai_selection == paper:
    print("You win! Scissors wins against paper.")
elif selection == ai_selection:
    print("It's a draw!")
else:
    print(f"You lose!")
