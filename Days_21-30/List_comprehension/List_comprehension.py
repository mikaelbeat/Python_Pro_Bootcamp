
numbers = [1, 2, 3, 4, 5]

new_numbers = [n + 1 for n in numbers]
print(new_numbers)
    
    
    
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)