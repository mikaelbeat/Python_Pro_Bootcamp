
total = 0

for number in range(1, 101):
    if number % 2 == 0:
        total += number
        
print(f"Sum of even numbers from 1 - 100 is {total}.")
