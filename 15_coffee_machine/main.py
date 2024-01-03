# Initial resources
water = 300
milk = 200
coffee = 100
money = 0.0

# Coffee Flavours
coffee_menu = {
    "espresso": {"water": 50, "milk": 0, "coffee": 18, "cost": 1.5},
    "latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 2.5},
    "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 3.0}}


def check_resources(coffee_flavour):
    if coffee_flavour in ["espresso", "latte", "cappuccino"]:
        ingredients = coffee_menu[coffee_flavour]
        if water - ingredients["water"] < 0:
            print("Sorry, there is not enough water.")
            return False
        elif milk - ingredients["milk"] < 0:
            print("Sorry, there is not enough milk.")
            return False
        elif coffee - ingredients["coffee"] < 0:
            print("Sorry, there is not enough coffee powder.")
            return False
        else:
            return True
    else:
        print("That's not a valid option..!! \nPlease try again.")
        return False


def process_coins(coffee_flavour):
    print("Please insert coins.")
    quarter = int(input("how many quarters?: "))
    dime = int(input("how many dimes?: "))
    nickel = int(input("how many nickels?: "))
    penny = int(input("how many penny's?: "))
    user_money = (quarter * 0.25) + (dime * 0.10) + (nickel * 0.05) + (penny * 0.01)
    global money

    if coffee_flavour in ["espresso", "latte", "cappuccino"]:
        coffee_cost = coffee_menu[coffee_flavour]["cost"]
        balance = round(user_money - coffee_cost, 2)
        if balance == 0:
            money += coffee_cost
            return True
        elif balance > 0:
            money += coffee_cost
            print(f"Here is ${balance} in change.")
            return True
        else:
            print("Sorry, that's not enough money")
            return False
    else:
        print("That's not a valid option..!! \nPlease try again.")
        return False


def make_coffee(coffee_flavour):
    ingredients = coffee_menu[coffee_flavour]
    global water, milk, coffee
    water -= ingredients["water"]
    milk -= ingredients["milk"]
    coffee -= ingredients["coffee"]
    print(f"Here's your {coffee_flavour} ☕️. Enjoy..!!")


serve_coffee = True

while serve_coffee:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        serve_coffee = False
        print("Thank You..!!")
    elif user_choice == "report":
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")
    elif user_choice in ["espresso", "latte", "cappuccino"]:
        if check_resources(user_choice):
            if process_coins(user_choice):
                make_coffee(user_choice)
    else:
        print("That's not a valid option..!! \nPlease try again.")
