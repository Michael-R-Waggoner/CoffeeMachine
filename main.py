import library
import sys

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

# TODO: 1. Ask customer for order
request = [""]
request[0] = input("What would you like?")


# TODO: 5. Process coins

def process_coins():
    num_quarters = int(input("Quarters: "))
    num_dimes = int(input("Dimes: "))
    num_nickels = int(input("Nickels: "))
    num_pennies = int(input("Pennies: "))
    quarter = 0.25
    dime = 0.1
    nickel = 0.05
    penny = 0.01
    return (num_quarters * quarter) + (num_dimes * dime) + (num_nickels * nickel) + (num_pennies * penny)


# TODO: 4. Check resources

# noinspection PyShadowingNames
def check_resources(request=request[0]):
    global resources
    if request[0] != "espresso":
        milk_needed = library.MENU[request[0]]["ingredients"]["milk"]
        milk_remaining = resources["milk"] - milk_needed
        resources["milk"] = milk_remaining
        if milk_remaining < 0:
            print("There is not enough milk for that drink.")
    water_needed = library.MENU[request[0]]["ingredients"]["water"]
    coffee_needed = library.MENU[request[0]]["ingredients"]["coffee"]
    water_remaining = resources["water"] - water_needed
    resources["water"] = water_remaining
    if water_remaining < 0:
        print("There is not enough water for that drink")
    coffee_remaining = resources["milk"] - coffee_needed
    resources["coffee"] = coffee_remaining
    if coffee_remaining < 0:
        print("There is not enough coffee for that drink.")


# TODO: 6. Check Transaction

# noinspection PyShadowingNames
def check_transaction(request=request[0]):
    global resources
    payment = process_coins()
    cost = library.MENU[request[0]]["cost"]
    if cost > payment:
        print("That is not enough for this drink.")
    elif cost < payment:
        change = payment - cost
        print(f"Your change is ${change}")
        resources["money"] = cost
    elif cost == payment:
        resources["money"] = cost


# TODO: 7. Make Coffee
def make_espresso():
    check_transaction(request)
    check_resources(request)


def make_latte():
    check_transaction(request)
    check_resources(request)


def make_cappuccino():
    check_transaction(request)
    check_resources(request)


# noinspection PyShadowingNames
def order(request):
    # TODO: 3. Print report.
    if request[0] == "report":
        print(resources)
    # TODO: 2. Turn off coffee machine with input 'off'
    elif request[0] == "off":
        sys.exit("Turning Off")
    elif request[0] == "espresso":
        make_espresso()
    elif request[0] == "latte":
        make_latte()
    elif request[0] == "cappuccino":
        make_cappuccino()
    request[0] = input("What would you like?")
    order(request)


order(request)
