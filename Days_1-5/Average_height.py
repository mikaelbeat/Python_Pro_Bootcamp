
print("*** Average height ***\n")

data = [156, 178, 165, 171, 187]

sum = 0
values = len(data)

for value in data:
    sum += value
    
result = sum /  values
    

print(round(result))