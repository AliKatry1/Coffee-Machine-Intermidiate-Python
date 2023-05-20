from ingredients import MENU, resources
money = 0


# TODO: 1.Print a report
def report():
    print(f"""Water: {resources["water"]}ml
Milk: {resources["milk"]}ml
Coffee: {resources["coffee"]}g""")
    print(f"Money : ${money}")


# TODO: 2.Make a function to check for the ingredients
def check_for_ingredients(drink):
    for ingredient in MENU[drink]["ingredients"]:
        if resources[ingredient] > MENU[drink]["ingredients"][ingredient]:
            resources[ingredient] -= MENU[drink]["ingredients"][ingredient]
        else:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


# TODO: 3. Make function to check for money
def check_for_money(drink):
    global money
    if MENU[drink]["cost"] <= money:
        print(f"Here is your {drink} ☕️. Enjoy!")
        money -= MENU[drink]["cost"]
    else:
        print("Sorry that's not enough money. Money refunded. ")

# TODO: 5. Make function to calculate money
def calculate_money():
    quarters = int(input("how many quarters?: ")) * 0.25  # Quarter = 0.25$
    dimes = int(input("how many dimes?: ")) * 0.10  # Dime = 0.10
    nickles = int(input("how many nickles?: ")) * 0.05  # Nickel = 0.05
    pennies = int(input("how many pennies?: ")) * 0.01  # Penny = 0.01
    global money
    money += quarters + dimes + nickles + pennies


while True:
    order = input("  What would you like? (espresso/latte/cappuccino): ")

    if order == "report":
        report()
    else:
        if check_for_ingredients(order):
            # TODO: 4.Ask for money
            print("Please insert coins.")
            calculate_money()
            check_for_money(order)






