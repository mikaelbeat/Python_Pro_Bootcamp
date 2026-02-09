
import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_phonetics = {row.letter:row.code for (index, row) in data.iterrows()}

data = "PETRI"
name_in_phonetics = [nato_phonetics[letter] for letter in data]
print(name_in_phonetics)