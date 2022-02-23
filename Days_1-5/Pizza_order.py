
print("\n*** Pizza order ***")

bill = 0

small_pizza = 15
medium_pizza = 20
large_pizza = 25

pepperoni_for_small = 2
pepperoni_for_medium_or_larger = 3
extra_cheese = 1

size = input("What size pizza do you want S, M or L? ")

if size == "S":
    print(f"Small size selected, added {small_pizza}£ to total amount.")
    bill += small_pizza
elif size == "M":
    print(f"Medium size selected, added {medium_pizza}£ to total amount.")
    bill += medium_pizza
else:
    print(f"Large size selected, added {large_pizza}£ to total amount.")
    bill += large_pizza

pepperoni = input("\nDo you want pepperoni Y or N? ")

if pepperoni == "Y":
    if size == "S":
        print(f"Pepperoni for small pizza is {pepperoni_for_small}£ extra.")
        bill += pepperoni_for_small
    else:
        print(
            f"Pepperoni for medium and large pizza is {pepperoni_for_medium_or_larger}£ extra.")
        bill += pepperoni_for_medium_or_larger
else:
    print("No pepperoni selected.")
    
cheese = input("\nDo you want extra cheese Y or N? ")

if cheese == "Y":
    print(f"Extra cheese selected, added {extra_cheese}£ to total amount.")
    bill += extra_cheese
    
print(f"Your final bill is {bill}£.")
        

