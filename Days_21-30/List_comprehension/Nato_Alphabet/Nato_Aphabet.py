
with open("nato_phonetic_alphabet.csv") as file:
  data = file.readlines()

nato_aphabets = {new_key:new_value.strip() for (new_key, new_value) in [item.split(",") for item in data]}

name = "Petri"
name_in_phonetics = [letter.upper() for letter in list(name)]

result = [nato_aphabets[letter] for letter in name_in_phonetics if letter in nato_aphabets.keys()]
print(result)