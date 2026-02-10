

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

sentence_in_list = sentence.split()

new_dict = {word:len(word) for (word) in sentence_in_list}

print(new_dict)