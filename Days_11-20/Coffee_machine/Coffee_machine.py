
from copy import copy

from pkg_resources import PkgResourcesDeprecationWarning
import Data
from replit import clear

RESOURCES = Data.resources
COFFEES = Data.MENU


def show_menu():
    print("*** Coffee machnine ***")
    print("""
        Options
        
        1 - Order coffee
        2 - Show report
        3 - Fill resources
        4 - Quit
        """)
    

def show_coffee_menu():
    clear()
    print("\n* Coffee menu *")
    row_number = 0
    for coffee in COFFEES:
        row_number += 1
        print(f"{row_number} -  {coffee}.")

def show_resources():
    clear()
    print("\n* Coffee machine resources *")
    row_number = 0
    for ingredient in RESOURCES:
        row_number += 1
        print(f"{row_number} - {ingredient}: {RESOURCES[ingredient]}")
        

def select_resource_to_fill(ingredient):
    if ingredient == "1":
        ingredient_name = "water"
        ingredient_stock = RESOURCES["water"]
        fill_resource(ingredient_name, ingredient_stock)
    elif ingredient == "2":
        ingredient_name = "milk"
        ingredient_stock = RESOURCES["milk"]
        fill_resource(ingredient_name, ingredient_stock)
    elif ingredient == "3":
        ingredient_name = "coffee"
        ingredient_stock = RESOURCES["coffee"]
        fill_resource(ingredient_name, ingredient_stock)
    
def fill_resource(name, stock):    
    fill = int(input(f"How much you would like to fill {name}? "))
    temp_stock = stock
    temp_stock += fill
    RESOURCES.update({name: temp_stock})
    show_resources()
    back = input("\nPress any key to continue.")
    
def process_payment(payment, coffee_price):
    temp_money = RESOURCES["money"]
    temp_money += payment
    RESOURCES.update({"money": temp_money})
    change = payment - coffee_price
    temp_money = RESOURCES["money"]
    temp_money -= change
    RESOURCES.update({"money": temp_money})
    print(f"\nYou paid {payment} and you will get {round(change, 2)} as a change.")
    payment_info = input("Thank you for payment, press any key to continue.")
    

def process_ingredients(order):
    coffee_water = COFFEES[order]["ingredients"]["water"]
    coffee_coffee = COFFEES[order]["ingredients"]["coffee"]
    
    stock_water = RESOURCES["water"]
    stock_coffee = RESOURCES["coffee"]
    stock_milk = RESOURCES["milk"]
    
    if order != "espresso":
        coffee_milk = COFFEES[order]["ingredients"]["milk"]
        if coffee_water > stock_water or coffee_milk > stock_milk or coffee_coffee > stock_coffee:
            return False
        else:
            temp_stock_water = stock_water - coffee_water
            temp_stock_milk = stock_milk - coffee_milk
            temp_stock_coffee = stock_coffee - coffee_coffee
            
            RESOURCES.update({"water": temp_stock_water})
            RESOURCES.update({"milk": temp_stock_milk})
            RESOURCES.update({"coffee": temp_stock_coffee})
            return True
    else:
            if coffee_water > stock_water or coffee_coffee > stock_coffee:
                return False
            else:
                temp_stock_water = stock_water - coffee_water
                temp_stock_coffee = stock_coffee - coffee_coffee
                RESOURCES.update({"water": temp_stock_water})
                RESOURCES.update({"coffee": temp_stock_coffee})
                return True
    
    
def pay_coffee(order):
    not_payed = True
    while not_payed:
        coffee_price = COFFEES[order]["cost"]
        print(f"\nCost for {order} is {coffee_price}.")
        payment = float(input("Please pay: "))
        if payment >= coffee_price:
            process_payment(payment, coffee_price)
            not_payed = False
            clear()
            show_menu()
        else:
            amount_left_to_pay = coffee_price - payment
            print(f"You payed {amount_left_to_pay} too little for coffee")
    
def make_coffee(order):
    enough_ingredients = process_ingredients(order)
    if enough_ingredients:
        pay_coffee(order)
    else:
        print("\nNot enough coffee ingredients in machine.")
        to_menu = input("Press any key to return to main menu.")
        clear()
        show_menu()
        
    
def order_coffee(coffee):
    if coffee == "1":
        order = "espresso"
        make_coffee(order)
    elif coffee == "2":
        order = "latte"
        make_coffee(order)
    elif coffee == "3":
        order = "cappuccino"
        make_coffee(order)


def coffee_machine():
    using_coffee_machine = True

    while using_coffee_machine:
        clear()  
        show_menu()
        selection = input("What do you want to do? ")
        if selection == "1":
            show_coffee_menu()
            selection = input(
                "\nWhat coffee would you like, or any other key to return to menu? ")
            order_coffee(selection)
        elif selection == "2":
            show_resources()
            selection = input("\nPress any key to return to main menu.")
        elif selection == "3":
            show_resources()
            selection = input("\nWhat resource you would like to fill, or any other key to return to menu? ")
            select_resource_to_fill(selection)
        elif selection == "4":
            print("\nQuitting coffee machine.")
            using_coffee_machine = False


coffee_machine()

