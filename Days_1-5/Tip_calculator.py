
print("\n*** Tip calculator ***")

bill = int(input("What was the total bill? "))
people = int(input("How many people to split the bill? "))
tip = "0." + input("How much tip do you want to give? 10, 12 or 15? ")


bill_with_tip = (bill * float(tip)) + bill
amount_to_pay = round(bill_with_tip / people, 2)

print(f"Each person should pay {amount_to_pay}£.")