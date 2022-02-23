
import random


print("*** Banker Roulette ***\n")

names = "Angela, Ben, Jenny, Michael, Chloe"

data = names.split(", ")

random_value = random.randint(0, len(data) -1)
print(f"Person who should pay the bill is {data[random_value]}.")

print("\n**********************************************")

print("\nUsing random choice")
print(f"Randomly chosen person to pay the bill is {random.choice(data)}.")
