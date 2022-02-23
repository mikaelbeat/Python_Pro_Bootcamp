
from Art import logo


def add(value1, value2):
    return value1 + value2

def subtract(value1, value2):
    return value1 - value2

def multiply(value1, value2):
    return value1 * value2

def divide(value1, value2):
    return value1 / value2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def show_operations():
    for operation in operations:
        print(operation)


def calculator():
    print(logo)
    continue_calculation = True
    
    num1 = float(input("Enter first number: "))
    while continue_calculation:
        show_operations()
        selection = input("Pick operation from list: ")
        num2 = float(input("Enter next number: "))
        calculation = (operations[selection])
        result = calculation(num1, num2)
        print(f"Result for {num1} {selection} {num2} = {result}.")
        keep_going = input(f"Type 'y' to continue calculation with {result}, 'n' to exit and x for fresh start: ")
        if keep_going == "y":
            num1 = result
        elif keep_going == "n":
            continue_calculation = False
        elif keep_going == "x":
            calculator()

calculator()

