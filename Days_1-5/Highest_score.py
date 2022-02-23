
print("*** Highest score ***\n")

scores = [78, 65, 89, 86, 55, 91, 64, 89, 99]

print(max(scores))

max_value = 0

for score in scores:
    if score > max_value:
        max_value = score
        
print(max_value)