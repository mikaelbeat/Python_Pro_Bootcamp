
from clear_screen import clear
from Art import logo


print(logo)

print("\nWelcome to the secret auction program.")

bids = {}

def enter_bids():
    others = True
    while others:
        name = input("What's your name? ")
        bid = int(input("What's your bid? "))
        bids[name] = bid
        others = input("Are there any other bidders, yes or no? ")
        clear()
        if others == "no":
            others = False
        elif others == "yes":
            clear()


def select_highest_bid():
    bids_in_list = bids.values()
    temp_list = []

    for value in bids_in_list:
        temp_list.append(value)

    max_bid = max(temp_list)

    for key, value in bids.items():
        if max_bid == value:
            print(f"Highest bid {max_bid} was from {key}.")
        
enter_bids()
select_highest_bid()
