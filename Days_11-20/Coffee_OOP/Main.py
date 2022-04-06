
from Menu import Menu, MenuItem
from Coffee_maker import CoffeeMaker
from Money_machine import MoneyMachine
from replit import clear

menu = Menu()
coffeeMaker = CoffeeMaker()
money = MoneyMachine()


def process_coffee_order(order):
    coffee = menu.find_drink(order)
    payment_successful = money.make_payment(coffee.cost)
    if payment_successful:
        enough_ingredients = coffeeMaker.is_resource_sufficient(coffee)
        if enough_ingredients:
            coffeeMaker.make_coffee(coffee)
            cont = input("Order successfull, press any key to return to menu.")
        else:
            cont = input("Order unsuccessfull, press any key to return to menu.")
    else:
        cont = input("Payment unsuccessfull, press any key to return to menu.")

using_coffee_machine = True

while using_coffee_machine:
    clear()
    print("******** Coffee Machine ********")
    print(f"\nAvailable coffees are {menu.get_items()}")
    selection = input(f"What would you like to have? ")

    if selection == "latte":
        if menu.find_drink(selection):
            process_coffee_order(selection)
    elif selection == "espresso":
        process_coffee_order(selection)
    elif selection == "cappuccino":
        process_coffee_order(selection)
    elif selection == "status":
        clear()
        print("******** Ingredients status ********\n")
        coffeeMaker.report()
        cont = input("\nPress any key to return to menu.")
    elif selection == "money":
        clear()
        print("******** Money status ********\n")
        money.report()
        cont = input("\nPress any key to return to menu.")
    elif selection == "q":
        print("\nQuitting coffee machine.")
        using_coffee_machine = False