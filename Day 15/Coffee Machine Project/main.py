MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
from coffee_data import MENU,resources, art

def check_resources(menu, u_select, c_resource):
    ingredients = menu[u_select]['ingredients']
    if (ingredients.get('milk', 0) <= c_resource['milk']
            and ingredients['water'] <= c_resource['water']
            and ingredients['coffee'] <= c_resource['coffee']):
        return True
    elif ingredients.get('milk', 0) > c_resource['milk']:
        print("There is not enough milk")
        return False
    elif ingredients['water'] > c_resource['water']:
        print("There is not enough water")
        return False
    else:
        print("There is not enough coffee")
        return False

def add_coins(q, d, n, p):
    total = q * 0.25 + d * 0.1 + n * 0.05 + p * 0.01
    return total


# print(MENU)
# print(resources)

run_program = True
money = 0

while run_program:
    print(art)
    selection = input('What would you like? (espresso/latte/cappuccino):').lower()
    if selection == 'off':
        run_program = False
    elif selection == 'report':
        print(f"Water: {resources['water']}\n"
              f"Milk: {resources['milk']}\n"
              f"Coffee: {resources['coffee']}\n"
              f"Money: ${money}")
    else:
        if check_resources(MENU, selection, resources):
            drink_cost = MENU[selection]['cost']
            print(f"The cost is ${drink_cost}")
            quarters = int(input("Insert Quarters: "))
            dimes = int(input("Insert Dimes: "))
            nickels = int(input("Insert Nickels: "))
            pennies = int(input("Insert Pennies: "))
            cus_total = add_coins(quarters, dimes, nickels, pennies)
            if cus_total == drink_cost:
                print(f"Thank you. Enjoy your beverage.")
                money += drink_cost
            elif cus_total > drink_cost:
                change = round(cus_total - drink_cost, 2)
                print(f"Thank you. Your change is ${change}.\nEnjoy your beverage.")
                money += drink_cost
            else:
                print("I'm sorry, that is not enough money.")



