from posixpath import split
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("*** Welcome to the PyPassword Generator! ***\n")

input_letters = 3
input_numbers = 3
input_symbols = 3

pass_letters = random.choices(letters, k=input_letters)
pass_numbers = random.choices(numbers, k=input_numbers)
pass_symbols = random.choices(symbols, k=input_symbols)

combined_inputs = pass_letters + pass_numbers + pass_symbols
random.shuffle(combined_inputs)

password = ""

for letter in combined_inputs:
    password += letter


print(f"Your secure generated password is {password}")
